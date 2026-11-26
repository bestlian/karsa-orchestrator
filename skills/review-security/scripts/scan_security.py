#!/usr/bin/env python3
"""
KARSA Security Scanner (Dependabot + GHAS Pre-Flight)
Deterministic read-only scanner for:
  1. SCA / Dependency Vulnerabilities (.NET NuGet, Node.js npm/pnpm/yarn, Python pip-audit)
  2. Secret Scanning (CWE-798) + .gitignore hygiene (always redacted, never prints secrets)
  3. SAST Pre-Flight (CodeQL High/Critical patterns aligned with OWASP & BINUS Standard v1.1)

Outputs a structured Markdown report (and optional JSON) inside the active project workspace.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


SKIP_DIRS = {
    ".git", "bin", "obj", "node_modules", "dist", "build", ".next", ".nuxt",
    "__pycache__", ".venv", "venv", ".vs", ".vscode", ".idea", "coverage",
    "TestResults", "artifacts", "packages", ".agents",
}

SCAN_TEXT_EXTS = {
    ".cs", ".csproj", ".vb", ".fs", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
    ".py", ".go", ".java", ".kt", ".rb", ".php", ".sql", ".json", ".yml", ".yaml",
    ".xml", ".config", ".cshtml", ".razor", ".html", ".sh", ".ps1", ".env",
}

SOURCE_CODE_EXTS = {
    ".cs", ".ts", ".tsx", ".js", ".jsx", ".py", ".cshtml", ".razor",
}

SEVERITY_ORDER = {"Critical": 0, "High": 1, "Moderate": 2, "Medium": 2, "Low": 3, "Info": 4}


@dataclass
class DepFinding:
    ecosystem: str
    manifest: str
    package: str
    resolved_version: str
    severity: str
    advisory_url: str
    kind: str  # direct | transitive | deprecated | outdated
    recommendation: str = ""


@dataclass
class CodeFinding:
    category: str  # SECRET | SAST | GITIGNORE
    rule_id: str
    cwe: str
    severity: str
    file: str
    line: int
    message: str
    snippet: str = ""


# ---------------------------------------------------------------------------
# Secret patterns (NEVER output raw matched secret; redact before storing)
# ---------------------------------------------------------------------------
SECRET_RULES: List[Tuple[str, str, str, re.Pattern, Optional[re.Pattern]]] = [
    (
        "SEC-SQL-PWD",
        "Critical",
        "Hardcoded database password in connection string",
        re.compile(r"""(?i)(?:Data\s+Source|Server|Initial\s+Catalog|User\s+Id|Uid|Persist\s+Security\s+Info)[^;\n]*;[^\n]*(?:Password|Pwd)\s*=\s*(?!REPLACE|YOUR_|<|\$\{|\*\*\*)[^;\s"']{4,}"""),
        None,
    ),
    (
        "SEC-PRIV-KEY",
        "Critical",
        "Private key material detected in tracked file",
        re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----"),
        re.compile(r"(?:IndexOf|Contains|StartsWith|ReadAndValidatePemFile|expectedMarker|marker|label)"),
    ),
    (
        "SEC-AWS-KEY",
        "Critical",
        "AWS Access Key ID pattern detected",
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        None,
    ),
    (
        "SEC-GH-TOKEN",
        "Critical",
        "GitHub personal/OAuth/app token pattern detected",
        re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b"),
        None,
    ),
    (
        "SEC-AZURE-CONN",
        "Critical",
        "Azure Storage / ServiceBus shared access key detected",
        re.compile(r"(?i)(?:AccountKey|SharedAccessKey)\s*=\s*[A-Za-z0-9+/=]{20,}"),
        None,
    ),
    (
        "SEC-HARDCODED-CRED",
        "High",
        "Potential hardcoded secret / API key / JWT secret assignment",
        re.compile(
            r"""(?i)\b(?:jwt[_-]?secret|secret[_-]?phrase|client[_-]?secret|api[_-]?key|smtp[_-]?password|db[_-]?password)\b\s*[:=]\s*["'](?!REPLACE|YOUR_|<|\$\{|ENV:|TODO|CHANGE_ME|DUMMY|TEST|EXAMPLE|\*\*\*)[^"'\s]{10,}["']"""
        ),
        None,
    ),
]

# ---------------------------------------------------------------------------
# SAST patterns (GHAS CodeQL High/Critical pre-flight checks)
# ---------------------------------------------------------------------------
SAST_RULES: List[Tuple[str, str, str, str, re.Pattern, Optional[re.Pattern]]] = [
    # (rule_id, cwe, severity, message, pattern, safe_context_exclusion)
    (
        "SAST-SQLI-RAW",
        "CWE-89",
        "High",
        "Potential SQL injection via string concatenation/interpolation in raw SQL call",
        re.compile(r"""(?i)(?:FromSqlRaw|ExecuteSqlRaw|SqlCommand|CommandText\s*=)\s*\(?\s*(?:\$"|"[^"]*"\s*\+|\s*String\.Format)"""),
        None,
    ),
    (
        "SAST-SQL-OPENQUERY",
        "CWE-89",
        "Moderate",
        "OPENQUERY / DBLINK / Linked Server usage detected (restricted by enterprise DB standards)",
        re.compile(r"(?i)\b(?:OPENQUERY|OPENROWSET|OPENDATASOURCE)\b"),
        None,
    ),
    (
        "SAST-PATH-TRAVERSAL",
        "CWE-22",
        "High",
        "Potential path traversal: uploaded FileName used directly in Path.Combine/FileStream without GetFileName/randomization",
        re.compile(r"(?:Path\.Combine|FileStream|File\.WriteAll|File\.Create)\s*\([^)]*\.(?:FileName)\b"),
        re.compile(r"Path\.GetFileName|Guid\.NewGuid"),
    ),
    (
        "SAST-XSS-RAWHTML",
        "CWE-79",
        "High",
        "Raw HTML rendering sink without visible DOMPurify/HTML sanitizer",
        re.compile(r"(?:dangerouslySetInnerHTML|\.innerHTML\s*=|@Html\.Raw\s*\()"),
        re.compile(r"DOMPurify|Sanitize|HtmlEncoder"),
    ),
    (
        "SAST-OPEN-REDIRECT",
        "CWE-601",
        "High",
        "Potential open redirect: request parameter passed to Redirect()",
        re.compile(r"\bRedirect\s*\(\s*(?:Request\.|returnUrl|redirectUrl|url\b)"),
        re.compile(r"Url\.IsLocalUrl|LocalRedirect"),
    ),
    (
        "SAST-TLS-BYPASS",
        "CWE-295",
        "High",
        "TLS certificate verification disabled (MITM risk)",
        re.compile(r"(?:EnableSslCertificateVerification\s*=\s*false|ServerCertificateCustomValidationCallback\s*=\s*(?:[^;\n]*=>\s*true|HttpClientHandler\.DangerousAcceptAnyServerCertificateValidator)|rejectUnauthorized\s*:\s*false|verify\s*=\s*False)"),
        None,
    ),
    (
        "SAST-WEAK-HASH",
        "CWE-327",
        "Moderate",
        "Weak hash algorithm (MD5/SHA1) detected — verify it is not used for passwords or security tokens",
        re.compile(r"\b(?:MD5\.Create|SHA1\.Create|MD5CryptoServiceProvider|SHA1CryptoServiceProvider|hashlib\.md5|hashlib\.sha1)\b"),
        None,
    ),
    (
        "SAST-STACKTRACE-EXPOSURE",
        "CWE-209",
        "Moderate",
        "Potential stack trace or raw internal exception detail returned in HTTP response",
        re.compile(r"(?:ex\.StackTrace|ex\.ToString\(\))"),
        re.compile(r"Log(?:Error|Warning|Debug|Information)|ErrorLog\.|Console\.Write"),
    ),
]


def norm_severity(sev: str) -> str:
    s = (sev or "Moderate").strip().lower()
    if s == "critical":
        return "Critical"
    if s == "high":
        return "High"
    if s in ("moderate", "medium"):
        return "Moderate"
    if s == "low":
        return "Low"
    return "Info"


def run_cmd(cmd: List[str], cwd: Path, timeout: int = 120) -> Tuple[int, str, str]:
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )
        return proc.returncode, proc.stdout, proc.stderr
    except FileNotFoundError:
        return -127, "", f"Command not found: {cmd[0]}"
    except subprocess.TimeoutExpired:
        return -124, "", f"Command timed out after {timeout}s: {' '.join(cmd)}"
    except Exception as e:
        return -1, "", f"{type(e).__name__}: {e}"


def get_git_tracked_files(root: Path) -> Optional[set]:
    code, out, _ = run_cmd(["git", "ls-files"], root, timeout=20)
    if code != 0:
        return None
    tracked = set()
    for line in out.splitlines():
        line = line.strip()
        if line:
            tracked.add((root / line).resolve())
    return tracked


def iter_workspace_files(root: Path, tracked_only: Optional[set] = None) -> List[Path]:
    result: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in filenames:
            p = (Path(dirpath) / fname).resolve()
            if tracked_only is not None and p not in tracked_only:
                continue
            result.append(p)
    return result


# ---------------------------------------------------------------------------
# 1. SCA: .NET (NuGet), Node.js (npm/pnpm/yarn), Python (pip-audit)
# ---------------------------------------------------------------------------
def scan_dotnet(root: Path, check_outdated: bool, findings: List[DepFinding], commands_log: List[str], proof_gaps: List[str]) -> int:
    csprojs: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.lower().endswith(".csproj"):
                csprojs.append(Path(dirpath) / fn)

    if not csprojs:
        return 0

    if not shutil.which("dotnet"):
        proof_gaps.append("Found .NET `.csproj` files, but `dotnet` CLI is not installed in PATH.")
        return len(csprojs)

    for proj in csprojs:
        rel_proj = os.path.relpath(proj, root).replace("\\", "/")
        # Vulnerable (direct + transitive)
        cmd = ["dotnet", "list", str(proj), "package", "--vulnerable", "--include-transitive", "--format", "json"]
        commands_log.append(f"`dotnet list {rel_proj} package --vulnerable --include-transitive --format json`")
        code, out, err = run_cmd(cmd, proj.parent, timeout=120)
        if code != 0:
            proof_gaps.append(f"`dotnet list --vulnerable` failed for `{rel_proj}` (exit {code}): {(err or out).strip()[:200]}")
            continue
        _parse_dotnet_json(out, rel_proj, "vulnerable", findings)

        # Deprecated
        cmd_dep = ["dotnet", "list", str(proj), "package", "--deprecated", "--format", "json"]
        commands_log.append(f"`dotnet list {rel_proj} package --deprecated --format json`")
        code_d, out_d, _ = run_cmd(cmd_dep, proj.parent, timeout=90)
        if code_d == 0:
            _parse_dotnet_json(out_d, rel_proj, "deprecated", findings)

        # Optional outdated
        if check_outdated:
            cmd_out = ["dotnet", "list", str(proj), "package", "--outdated", "--format", "json"]
            commands_log.append(f"`dotnet list {rel_proj} package --outdated --format json`")
            code_o, out_o, _ = run_cmd(cmd_out, proj.parent, timeout=120)
            if code_o == 0:
                _parse_dotnet_json(out_o, rel_proj, "outdated", findings)

    return len(csprojs)


def _parse_dotnet_json(raw: str, rel_proj: str, mode: str, findings: List[DepFinding]) -> None:
    try:
        data = json.loads(raw)
    except Exception:
        return

    for project in data.get("projects", []):
        for fw in project.get("frameworks", []):
            for bucket, is_trans in (("topLevelPackages", False), ("transitivePackages", True)):
                for pkg in fw.get(bucket, []) or []:
                    pkg_id = pkg.get("id", "unknown")
                    resolved = pkg.get("resolvedVersion", "?")
                    if mode == "vulnerable":
                        for vuln in pkg.get("vulnerabilities", []) or []:
                            sev = norm_severity(vuln.get("severity", "High"))
                            adv = vuln.get("advisoryurl") or vuln.get("advisoryUrl") or ""
                            kind = "transitive" if is_trans else "direct"
                            rec = (
                                f"Pin safe version via `dotnet add {rel_proj} package {pkg_id}` or upgrade parent package"
                                if is_trans
                                else f"Upgrade via `dotnet add {rel_proj} package {pkg_id}`"
                            )
                            findings.append(DepFinding("NuGet (.NET)", rel_proj, pkg_id, resolved, sev, adv, kind, rec))
                    elif mode == "deprecated":
                        reasons = ", ".join(pkg.get("deprecationReasons") or ["Deprecated"])
                        alt = (pkg.get("alternativePackage") or {}).get("id")
                        rec = f"Migrate to `{alt}`" if alt else f"Replace deprecated package ({reasons})"
                        findings.append(DepFinding("NuGet (.NET)", rel_proj, pkg_id, resolved, "Low", "", "deprecated", rec))
                    elif mode == "outdated":
                        latest = pkg.get("latestVersion")
                        if latest and latest != resolved:
                            findings.append(
                                DepFinding(
                                    "NuGet (.NET)", rel_proj, pkg_id, resolved, "Info", "", "outdated",
                                    f"Latest available: `{latest}`",
                                )
                            )


def scan_nodejs(root: Path, findings: List[DepFinding], commands_log: List[str], proof_gaps: List[str]) -> int:
    pkg_jsons: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if "package.json" in filenames:
            pkg_jsons.append(Path(dirpath) / "package.json")

    if not pkg_jsons:
        return 0

    for pj in pkg_jsons:
        folder = pj.parent
        rel_pj = os.path.relpath(pj, root).replace("\\", "/")
        if (folder / "pnpm-lock.yaml").exists() and shutil.which("pnpm"):
            cmd = ["pnpm", "audit", "--json"]
            commands_log.append(f"`pnpm audit --json` in `{os.path.relpath(folder, root)}`")
            code, out, err = run_cmd(cmd, folder, timeout=90)
            _parse_npm_like_audit(out, rel_pj, "pnpm (Node.js)", findings, proof_gaps, code, err)
        elif (folder / "package-lock.json").exists() and shutil.which("npm"):
            cmd = ["npm", "audit", "--json"]
            commands_log.append(f"`npm audit --json` in `{os.path.relpath(folder, root)}`")
            code, out, err = run_cmd(cmd, folder, timeout=90)
            _parse_npm_like_audit(out, rel_pj, "npm (Node.js)", findings, proof_gaps, code, err)
        elif (folder / "yarn.lock").exists() and shutil.which("yarn"):
            cmd = ["yarn", "audit", "--json"]
            commands_log.append(f"`yarn audit --json` in `{os.path.relpath(folder, root)}`")
            code, out, err = run_cmd(cmd, folder, timeout=90)
            _parse_yarn_audit(out, rel_pj, findings, proof_gaps, code, err)
        else:
            proof_gaps.append(f"Skipped Node.js audit for `{rel_pj}` (missing lockfile or package manager CLI in PATH).")

    return len(pkg_jsons)


def _parse_npm_like_audit(raw: str, rel_pj: str, eco: str, findings: List[DepFinding], proof_gaps: List[str], code: int, err: str) -> None:
    try:
        data = json.loads(raw)
    except Exception:
        if code not in (0, 1):
            proof_gaps.append(f"{eco} audit failed for `{rel_pj}`: {(err or raw).strip()[:200]}")
        return

    # npm v7+ format
    vulns = data.get("vulnerabilities")
    if isinstance(vulns, dict):
        for pkg_name, info in vulns.items():
            if not isinstance(info, dict):
                continue
            sev = norm_severity(info.get("severity", "Moderate"))
            is_direct = bool(info.get("isDirect", False))
            via_urls = []
            for v in info.get("via", []) or []:
                if isinstance(v, dict) and v.get("url"):
                    via_urls.append(v["url"])
            fix = info.get("fixAvailable")
            rec = "Check `npm audit fix`"
            if isinstance(fix, dict) and fix.get("name") and fix.get("version"):
                rec = f"Upgrade `{fix['name']}` to `{fix['version']}`" + (" (major/breaking)" if fix.get("isSemVerMajor") else "")
            elif fix is False:
                rec = "No automatic fix available; review advisory"
            findings.append(
                DepFinding(
                    eco, rel_pj, pkg_name, str(info.get("range", "*")), sev,
                    via_urls[0] if via_urls else "", "direct" if is_direct else "transitive", rec,
                )
            )
        return

    # pnpm / npm v6 advisories format
    advisories = data.get("advisories")
    if isinstance(advisories, dict):
        for adv in advisories.values():
            if not isinstance(adv, dict):
                continue
            findings.append(
                DepFinding(
                    eco, rel_pj, str(adv.get("module_name", "unknown")),
                    str(adv.get("vulnerable_versions", "*")),
                    norm_severity(adv.get("severity", "Moderate")),
                    str(adv.get("url", "")),
                    "direct",
                    str(adv.get("recommendation", "Upgrade to patched version")),
                )
            )


def _parse_yarn_audit(raw: str, rel_pj: str, findings: List[DepFinding], proof_gaps: List[str], code: int, err: str) -> None:
    parsed_any = False
    for line in raw.splitlines():
        try:
            obj = json.loads(line)
        except Exception:
            continue
        if obj.get("type") == "auditAdvisory":
            parsed_any = True
            adv = (obj.get("data") or {}).get("advisory") or {}
            findings.append(
                DepFinding(
                    "yarn (Node.js)", rel_pj, str(adv.get("module_name", "unknown")),
                    str(adv.get("vulnerable_versions", "*")),
                    norm_severity(adv.get("severity", "Moderate")),
                    str(adv.get("url", "")),
                    "direct",
                    str(adv.get("recommendation", "Upgrade to patched version")),
                )
            )
    if not parsed_any and code not in (0, 1):
        proof_gaps.append(f"yarn audit failed for `{rel_pj}`: {(err or raw).strip()[:200]}")


def scan_python(root: Path, findings: List[DepFinding], commands_log: List[str], proof_gaps: List[str]) -> int:
    req_files: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn in ("requirements.txt", "pyproject.toml") or (fn.startswith("requirements") and fn.endswith(".txt")):
                req_files.append(Path(dirpath) / fn)

    if not req_files:
        return 0

    if not shutil.which("pip-audit"):
        proof_gaps.append(
            f"Detected {len(req_files)} Python dependency manifest(s), but `pip-audit` is not installed (`pip install pip-audit`)."
        )
        return len(req_files)

    for rf in req_files:
        rel_rf = os.path.relpath(rf, root).replace("\\", "/")
        if rf.name.endswith(".txt"):
            cmd = ["pip-audit", "-r", str(rf), "--format", "json"]
        else:
            cmd = ["pip-audit", "--path", str(rf.parent), "--format", "json"]
        commands_log.append(f"`{' '.join(cmd)}`")
        code, out, err = run_cmd(cmd, rf.parent, timeout=90)
        try:
            data = json.loads(out)
        except Exception:
            if code != 0:
                proof_gaps.append(f"`pip-audit` failed for `{rel_rf}`: {(err or out).strip()[:200]}")
            continue
        for dep in data.get("dependencies", []) if isinstance(data, dict) else (data if isinstance(data, list) else []):
            for v in dep.get("vulns", []) or []:
                fix_vers = ", ".join(v.get("fix_versions") or [])
                findings.append(
                    DepFinding(
                        "PyPI (Python)", rel_rf, dep.get("name", "unknown"), dep.get("version", "?"),
                        "High", f"https://osv.dev/vulnerability/{v.get('id', '')}" if v.get("id") else "",
                        "direct", f"Upgrade to `{fix_vers}`" if fix_vers else "Review advisory",
                    )
                )
    return len(req_files)


# ---------------------------------------------------------------------------
# 2. Secret Scanning & .gitignore Hygiene
# ---------------------------------------------------------------------------
def scan_secrets_and_gitignore(root: Path, tracked: Optional[set], findings: List[CodeFinding]) -> int:
    # Check if sensitive local files exist untracked vs tracked
    sensitive_names = {"appsettings.json", ".env", ".env.local", ".env.production", "id_rsa"}
    if tracked is not None:
        for tp in tracked:
            if tp.name.lower() in sensitive_names or tp.suffix.lower() in (".pem", ".key", ".pfx", ".p12"):
                rel = os.path.relpath(tp, root).replace("\\", "/")
                findings.append(
                    CodeFinding(
                        "GITIGNORE", "SEC-TRACKED-SENSITIVE", "CWE-798", "High",
                        rel, 1,
                        f"Sensitive config/key file `{tp.name}` is tracked by Git — verify it contains no real credentials and add to `.gitignore`.",
                    )
                )

    files = iter_workspace_files(root, tracked_only=tracked)
    scanned = 0
    for p in files:
        if p.suffix.lower() not in SCAN_TEXT_EXTS:
            continue
        if p.name.lower().endswith(".example.json") or "example" in p.name.lower() and p.suffix.lower() == ".json":
            continue
        try:
            if p.stat().st_size > 1_500_000:
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        scanned += 1
        rel = os.path.relpath(p, root).replace("\\", "/")
        for lineno, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("//") or stripped.startswith("#") or stripped.startswith("*"):
                continue
            for rule_id, sev, msg, regex, excl in SECRET_RULES:
                if regex.search(line):
                    if excl and excl.search(line):
                        continue
                    redacted = regex.sub("***REDACTED***", stripped)[:140]
                    findings.append(CodeFinding("SECRET", rule_id, "CWE-798", sev, rel, lineno, msg, redacted))
                    break
    return scanned


# ---------------------------------------------------------------------------
# 3. SAST Pre-Flight (CodeQL High/Critical Patterns)
# ---------------------------------------------------------------------------
def scan_sast(root: Path, tracked: Optional[set], findings: List[CodeFinding]) -> int:
    files = iter_workspace_files(root, tracked_only=tracked)
    scanned = 0
    for p in files:
        if p.suffix.lower() not in SOURCE_CODE_EXTS:
            continue
        try:
            if p.stat().st_size > 1_500_000:
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        scanned += 1
        rel = os.path.relpath(p, root).replace("\\", "/")
        for lineno, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("//") or stripped.startswith("#") or stripped.startswith("*"):
                continue
            for rule_id, cwe, sev, msg, regex, safe_excl in SAST_RULES:
                if regex.search(line):
                    if safe_excl and safe_excl.search(line):
                        continue
                    findings.append(CodeFinding("SAST", rule_id, cwe, sev, rel, lineno, msg, stripped[:140]))
    return scanned


# ---------------------------------------------------------------------------
# Report Generator
# ---------------------------------------------------------------------------
def render_markdown(
    root: Path,
    dep_findings: List[DepFinding],
    secret_findings: List[CodeFinding],
    sast_findings: List[CodeFinding],
    stats: Dict[str, int],
    commands_log: List[str],
    proof_gaps: List[str],
) -> str:
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    sca_vulns = [f for f in dep_findings if f.kind in ("direct", "transitive")]
    sca_crit_high = [f for f in sca_vulns if f.severity in ("Critical", "High")]
    sec_crit_high = [f for f in secret_findings if f.severity in ("Critical", "High")]
    sast_crit_high = [f for f in sast_findings if f.severity in ("Critical", "High")]

    gate = "BLOCKED" if (sca_crit_high or sec_crit_high) else ("REVIEW NEEDED" if sast_crit_high else "PASS")

    lines: List[str] = [
        f"# Security Scan Report (Dependabot + GHAS Pre-Flight)",
        "",
        f"- **Target Workspace:** `{root}`",
        f"- **Scanned At:** {now_utc}",
        f"- **GHAS Gate Status:** **{gate}** *(Zero Critical/High CVEs & Zero Tracked Secrets required for PASS; High SAST hits require code verification)*",
        "",
        "## 1. Executive Summary",
        "",
        "| Layer | Scanned Scope | Critical | High | Moderate | Low / Info |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    def _counts(items, sev_attr="severity"):
        c = sum(1 for x in items if getattr(x, sev_attr) == "Critical")
        h = sum(1 for x in items if getattr(x, sev_attr) == "High")
        m = sum(1 for x in items if getattr(x, sev_attr) == "Moderate")
        l = sum(1 for x in items if getattr(x, sev_attr) in ("Low", "Info"))
        return c, h, m, l

    sc, sh, sm, sl = _counts(sca_vulns)
    ec, eh, em, el = _counts(secret_findings)
    ac, ah, am, al = _counts(sast_findings)
    lines.append(f"| **SCA (Dependencies)** | {stats['manifests']} manifest(s) | {sc} | {sh} | {sm} | {sl} |")
    lines.append(f"| **Secret Scanning** | {stats['secret_files']} tracked file(s) | {ec} | {eh} | {em} | {el} |")
    lines.append(f"| **SAST Pre-Flight** | {stats['sast_files']} source file(s) | {ac} | {ah} | {am} | {al} |")
    lines.append("")

    # Section 2: SCA
    lines.append("## 2. Dependency Vulnerabilities (Dependabot / SCA)")
    lines.append("")
    if sca_vulns:
        sca_vulns_sorted = sorted(sca_vulns, key=lambda x: (SEVERITY_ORDER.get(x.severity, 9), x.package))
        lines.append("| Severity | Ecosystem | Manifest | Package | Version | Type | Advisory | Recommendation |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for f in sca_vulns_sorted:
            adv_md = f"[Advisory]({f.advisory_url})" if f.advisory_url else "-"
            lines.append(f"| **{f.severity}** | {f.ecosystem} | `{f.manifest}` | `{f.package}` | `{f.resolved_version}` | {f.kind} | {adv_md} | {f.recommendation} |")
    else:
        lines.append("No vulnerable packages detected across scanned manifests.")
    lines.append("")

    deprecated = [f for f in dep_findings if f.kind == "deprecated"]
    if deprecated:
        lines.append("### Deprecated Packages")
        lines.append("")
        lines.append("| Manifest | Package | Version | Recommendation |")
        lines.append("|---|---|---|---|")
        for f in deprecated:
            lines.append(f"| `{f.manifest}` | `{f.package}` | `{f.resolved_version}` | {f.recommendation} |")
        lines.append("")

    outdated = [f for f in dep_findings if f.kind == "outdated"]
    if outdated:
        lines.append("### Outdated Packages (Informational)")
        lines.append("")
        lines.append("| Manifest | Package | Resolved | Latest |")
        lines.append("|---|---|---|---|")
        for f in outdated:
            lines.append(f"| `{f.manifest}` | `{f.package}` | `{f.resolved_version}` | {f.recommendation} |")
        lines.append("")

    # Section 3: Secrets
    lines.append("## 3. Secret Scanning & `.gitignore` Hygiene (CWE-798)")
    lines.append("")
    if secret_findings:
        lines.append("| Severity | Rule | Location | Description | Redacted Match |")
        lines.append("|---|---|---|---|---|")
        for f in sorted(secret_findings, key=lambda x: (SEVERITY_ORDER.get(x.severity, 9), x.file, x.line)):
            snip = f"`{f.snippet.replace('|', '\\|')}`" if f.snippet else "-"
            lines.append(f"| **{f.severity}** | `{f.rule_id}` | `{f.file}:{f.line}` | {f.message} | {snip} |")
    else:
        lines.append("No hardcoded secrets or tracked sensitive key/config files detected.")
    lines.append("")

    # Section 4: SAST
    lines.append("## 4. SAST Pre-Flight Patterns (GHAS CodeQL Pre-Check)")
    lines.append("")
    if sast_findings:
        lines.append("> Static regex matches require code-path verification to separate confirmed vulnerabilities from false positives.")
        lines.append("")
        lines.append("| Severity | Rule / CWE | Location | Description | Code Snippet |")
        lines.append("|---|---|---|---|---|")
        for f in sorted(sast_findings, key=lambda x: (SEVERITY_ORDER.get(x.severity, 9), x.file, x.line)):
            snip = f"`{f.snippet.replace('|', '\\|')}`"
            lines.append(f"| **{f.severity}** | `{f.rule_id}` ({f.cwe}) | `{f.file}:{f.line}` | {f.message} | {snip} |")
    else:
        lines.append("No high-risk SAST anti-patterns matched.")
    lines.append("")

    # Section 5: Commands & Proof Gaps
    lines.append("## 5. Verification Evidence & Proof Gaps")
    lines.append("")
    lines.append("### Commands Executed")
    if commands_log:
        for c in commands_log:
            lines.append(f"- {c}")
    else:
        lines.append("- Static file scans only (no package manager CLI executed).")
    lines.append("")
    lines.append("### Explicit Proof Gaps")
    if proof_gaps:
        for g in proof_gaps:
            lines.append(f"- {g}")
    else:
        lines.append("- Static SAST regex pre-check is not a full dataflow CodeQL AST analysis; run GitHub Advanced Security CodeQL in CI for full taint tracking.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="KARSA Security Scanner (Dependabot + GHAS Pre-Flight)")
    parser.add_argument("--root", default=".", help="Absolute or relative path to target project root")
    parser.add_argument("--output", default="", help="Markdown report output path (default: <root>/artifacts/security/dependabot-ghas-report.md)")
    parser.add_argument("--json-output", default="", help="Optional JSON report output path")
    parser.add_argument("--check-outdated", action="store_true", help="Also list outdated .NET packages")
    parser.add_argument("--skip-sca", action="store_true", help="Skip dependency vulnerability scanning")
    parser.add_argument("--skip-secrets", action="store_true", help="Skip secret scanning")
    parser.add_argument("--skip-sast", action="store_true", help="Skip SAST pre-flight checks")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"[ERROR] Project root not found: {root}", file=sys.stderr)
        return 1

    tracked = get_git_tracked_files(root)
    dep_findings: List[DepFinding] = []
    secret_findings: List[CodeFinding] = []
    sast_findings: List[CodeFinding] = []
    commands_log: List[str] = []
    proof_gaps: List[str] = []

    manifests = 0
    if not args.skip_sca:
        manifests += scan_dotnet(root, args.check_outdated, dep_findings, commands_log, proof_gaps)
        manifests += scan_nodejs(root, dep_findings, commands_log, proof_gaps)
        manifests += scan_python(root, dep_findings, commands_log, proof_gaps)
        if manifests == 0:
            proof_gaps.append("No supported dependency manifests (*.csproj, package.json, requirements.txt, pyproject.toml) found.")

    secret_files = 0
    if not args.skip_secrets:
        secret_files = scan_secrets_and_gitignore(root, tracked, secret_findings)

    sast_files = 0
    if not args.skip_sast:
        sast_files = scan_sast(root, tracked, sast_findings)

    stats = {"manifests": manifests, "secret_files": secret_files, "sast_files": sast_files}
    md = render_markdown(root, dep_findings, secret_findings, sast_findings, stats, commands_log, proof_gaps)

    out_path = Path(args.output) if args.output else (root / "artifacts" / "security" / "dependabot-ghas-report.md")
    if not out_path.is_absolute():
        out_path = (root / out_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")

    if args.json_output:
        jp = Path(args.json_output)
        if not jp.is_absolute():
            jp = (root / jp).resolve()
        jp.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "root": str(root),
            "stats": stats,
            "dependencies": [asdict(f) for f in dep_findings],
            "secrets": [asdict(f) for f in secret_findings],
            "sast": [asdict(f) for f in sast_findings],
            "commands": commands_log,
            "proof_gaps": proof_gaps,
        }
        jp.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    sca_ch = sum(1 for f in dep_findings if f.kind in ("direct", "transitive") and f.severity in ("Critical", "High"))
    sec_ch = sum(1 for f in secret_findings if f.severity in ("Critical", "High"))
    sast_ch = sum(1 for f in sast_findings if f.severity in ("Critical", "High"))

    print(f"Report saved : {out_path}")
    print(f"SCA Vulns    : {len([f for f in dep_findings if f.kind in ('direct', 'transitive')])} (Critical/High={sca_ch})")
    print(f"Secrets      : {len(secret_findings)} (Critical/High={sec_ch})")
    print(f"SAST Hits    : {len(sast_findings)} (Critical/High={sast_ch})")
    if proof_gaps:
        print(f"Proof Gaps   : {len(proof_gaps)}")
    return 2 if (sca_ch > 0 or sec_ch > 0) else 0


if __name__ == "__main__":
    sys.exit(main())
