#!/usr/bin/env python3
"""Deterministic ADLC helper CLI for KARSA orchestrator and subagents.

Provides:
  - checksum: compute canonical SHA-256 scope_checksum over sorted project files.
  - log-dispatch: validate and atomically append an entry to artifacts/audit/dispatch-log.jsonl.
  - validate-dispatch-log: validate every JSONL line against the canonical schema.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

REQUIRED_KEYS = {
    "timestamp",
    "dispatch_id",
    "agent",
    "model",
    "workspace",
    "phase",
    "item_id",
    "rounds",
    "status",
    "evidence_path",
    "failure_category",
}

VALID_MODELS = {"flash", "pro", "inherit", "flash_lite"}
VALID_WORKSPACES = {"main", "branch", "inherit", "share"}
VALID_STATUSES = {"PASS", "FAIL", "BLOCKED", "STALE_CHECKSUM"}
VALID_FAILURE_CATEGORIES = {
    "contract_defect",
    "test_failure",
    "security_leak",
    "timeout",
    "stale_checksum",
}
GOVERNANCE_PREFIXES = ("docs/", "artifacts/")
DISPATCH_ID_RE = re.compile(r"^DSP-\d{3,}$")
ISO_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")


def _normalize_rel_path(root: Path, raw_path: str) -> tuple[str, Path]:
    """Resolve a path relative to root and reject traversal outside root."""
    cleaned = raw_path.strip().replace("\\", "/")
    if not cleaned:
        raise ValueError("Empty file path is not allowed.")
    candidate = (root / cleaned).resolve()
    root_resolved = root.resolve()
    try:
        rel = candidate.relative_to(root_resolved)
    except ValueError as exc:
        raise ValueError(f"Path escapes project root: {raw_path}") from exc
    return rel.as_posix(), candidate


def _collect_git_diff_files(root: Path, base_ref: str) -> list[str]:
    """Collect changed files relative to base_ref plus untracked files, excluding governance docs."""
    diff_cmd = ["git", "-C", str(root), "diff", "--name-only", base_ref]
    diff_res = subprocess.run(diff_cmd, capture_output=True, text=True, check=False)
    if diff_res.returncode != 0:
        raise RuntimeError(f"git diff failed ({diff_res.returncode}): {diff_res.stderr.strip()}")

    untracked_cmd = ["git", "-C", str(root), "ls-files", "--others", "--exclude-standard"]
    untracked_res = subprocess.run(untracked_cmd, capture_output=True, text=True, check=False)

    raw_paths = [
        line.strip().replace("\\", "/")
        for line in (diff_res.stdout.splitlines() + untracked_res.stdout.splitlines())
        if line.strip()
    ]
    scoped: list[str] = []
    for p in sorted(set(raw_paths)):
        if p.startswith(GOVERNANCE_PREFIXES):
            continue
        if (root / p).is_file():
            scoped.append(p)
    return scoped


def compute_scope_checksum(root: Path, rel_paths: list[str]) -> tuple[str, list[str]]:
    """Compute canonical SHA-256 over sorted relative POSIX paths with LF normalization for text."""
    resolved_map: dict[str, Path] = {}
    for raw in rel_paths:
        rel_posix, abs_path = _normalize_rel_path(root, raw)
        if not abs_path.is_file():
            raise FileNotFoundError(f"Scoped file not found: {rel_posix}")
        resolved_map[rel_posix] = abs_path

    if not resolved_map:
        raise ValueError("At least one existing file is required to compute scope_checksum.")

    sorted_paths = sorted(resolved_map.keys())
    hasher = hashlib.sha256()
    for rel_posix in sorted_paths:
        data = resolved_map[rel_posix].read_bytes()
        # Normalize CRLF to LF for non-binary files so Windows and Linux match identically.
        if b"\x00" not in data:
            data = data.replace(b"\r\n", b"\n")
        hasher.update(f"FILE:{rel_posix}\n".encode("utf-8"))
        hasher.update(f"LEN:{len(data)}\n".encode("utf-8"))
        hasher.update(data)
        hasher.update(b"\n")
    return hasher.hexdigest(), sorted_paths


def validate_dispatch_entry(entry: dict[str, Any]) -> list[str]:
    """Return a list of schema violation messages for a single dispatch-log entry."""
    errors: list[str] = []
    if not isinstance(entry, dict):
        return ["Entry must be a JSON object."]

    keys = set(entry.keys())
    missing = sorted(REQUIRED_KEYS - keys)
    extra = sorted(keys - REQUIRED_KEYS)
    if missing:
        errors.append(f"Missing required keys: {', '.join(missing)}")
    if extra:
        errors.append(f"Unexpected keys: {', '.join(extra)}")
    if missing:
        return errors

    ts = entry["timestamp"]
    if not isinstance(ts, str) or not ISO_UTC_RE.match(ts):
        errors.append(f"Invalid UTC ISO-8601 timestamp: {ts!r}")

    dispatch_id = entry["dispatch_id"]
    if not isinstance(dispatch_id, str) or not DISPATCH_ID_RE.match(dispatch_id):
        errors.append(f"Invalid dispatch_id (expected DSP-NNN): {dispatch_id!r}")

    for field in ("agent", "phase", "item_id"):
        val = entry[field]
        if not isinstance(val, str) or not val.strip():
            errors.append(f"Field '{field}' must be a non-empty string.")

    if entry["model"] not in VALID_MODELS:
        errors.append(f"Invalid model {entry['model']!r}; allowed: {sorted(VALID_MODELS)}")

    if entry["workspace"] not in VALID_WORKSPACES:
        errors.append(f"Invalid workspace {entry['workspace']!r}; allowed: {sorted(VALID_WORKSPACES)}")

    rounds = entry["rounds"]
    if isinstance(rounds, bool) or not isinstance(rounds, int) or rounds < 1:
        errors.append(f"Field 'rounds' must be an integer >= 1; got {rounds!r}")

    status = entry["status"]
    if status not in VALID_STATUSES:
        errors.append(f"Invalid status {status!r}; allowed: {sorted(VALID_STATUSES)}")

    evidence_path = entry["evidence_path"]
    if not isinstance(evidence_path, str):
        errors.append("Field 'evidence_path' must be a string.")
    else:
        norm_ev = evidence_path.replace("\\", "/")
        parts = norm_ev.split("/")
        if not norm_ev.startswith("artifacts/") or ".." in parts or len(norm_ev) <= len("artifacts/"):
            errors.append(f"Invalid evidence_path (must stay under artifacts/): {evidence_path!r}")

    failure_category = entry["failure_category"]
    if status == "PASS":
        if failure_category is not None:
            errors.append(f"failure_category must be null when status is PASS; got {failure_category!r}")
    elif status in VALID_STATUSES:
        if failure_category not in VALID_FAILURE_CATEGORIES:
            errors.append(
                f"Invalid failure_category {failure_category!r} for status {status}; "
                f"allowed: {sorted(VALID_FAILURE_CATEGORIES)}"
            )

    return errors


def _next_dispatch_id(log_path: Path) -> str:
    max_num = 0
    if log_path.is_file():
        for line in log_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                did = str(obj.get("dispatch_id", ""))
                if did.startswith("DSP-"):
                    max_num = max(max_num, int(did.split("-", 1)[1]))
            except (ValueError, json.JSONDecodeError):
                continue
    return f"DSP-{max_num + 1:03d}"


def cmd_checksum(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"[ERROR] Root directory does not exist: {root}", file=sys.stderr)
        return 2

    raw_files: list[str] = []
    if args.files:
        for item in args.files:
            raw_files.extend([p.strip() for p in item.split(",") if p.strip()])
    if args.files_from:
        list_file = Path(args.files_from)
        if not list_file.is_file():
            print(f"[ERROR] --files-from not found: {list_file}", file=sys.stderr)
            return 2
        raw_files.extend([ln.strip() for ln in list_file.read_text(encoding="utf-8").splitlines() if ln.strip()])
    if args.git_diff:
        try:
            raw_files.extend(_collect_git_diff_files(root, args.git_diff))
        except RuntimeError as exc:
            print(f"[ERROR] {exc}", file=sys.stderr)
            return 2

    if args.exclude_governance:
        raw_files = [p for p in raw_files if not p.replace("\\", "/").startswith(GOVERNANCE_PREFIXES)]

    try:
        digest, sorted_files = compute_scope_checksum(root, raw_files)
    except (ValueError, FileNotFoundError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(
            json.dumps(
                {
                    "scope_checksum": digest,
                    "file_count": len(sorted_files),
                    "files": sorted_files,
                },
                indent=2,
            )
        )
    else:
        print(digest)
    return 0


def cmd_log_dispatch(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"[ERROR] Root directory does not exist: {root}", file=sys.stderr)
        return 2

    log_path = root / "artifacts" / "audit" / "dispatch-log.jsonl"
    dispatch_id = _next_dispatch_id(log_path) if args.dispatch_id.lower() == "auto" else args.dispatch_id
    timestamp = args.timestamp or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    raw_fc = args.failure_category
    failure_category = None if (raw_fc is None or raw_fc.lower() in {"null", "none", ""}) else raw_fc
    evidence_path = args.evidence_path.replace("\\", "/")

    entry: dict[str, Any] = {
        "timestamp": timestamp,
        "dispatch_id": dispatch_id,
        "agent": args.agent,
        "model": args.model,
        "workspace": args.workspace,
        "phase": args.phase,
        "item_id": args.item_id,
        "rounds": args.rounds,
        "status": args.status,
        "evidence_path": evidence_path,
        "failure_category": failure_category,
    }

    errors = validate_dispatch_entry(entry)
    if errors:
        for err in errors:
            print(f"[ERROR] {err}", file=sys.stderr)
        return 1

    log_path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(entry, ensure_ascii=False)
    with log_path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(serialized + "\n")

    print(serialized)
    return 0


def cmd_validate_dispatch_log(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    log_path = Path(args.log_path).resolve() if args.log_path else (root / "artifacts" / "audit" / "dispatch-log.jsonl")
    if not log_path.is_file():
        print(f"[ERROR] Dispatch log not found: {log_path}", file=sys.stderr)
        return 1

    lines = log_path.read_text(encoding="utf-8").splitlines()
    seen_ids: set[str] = set()
    failures: list[str] = []
    valid_count = 0

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        try:
            obj = json.loads(stripped)
        except json.JSONDecodeError as exc:
            failures.append(f"Line {lineno}: invalid JSON ({exc})")
            continue

        errs = validate_dispatch_entry(obj)
        if errs:
            for err in errs:
                failures.append(f"Line {lineno}: {err}")
            continue

        did = obj["dispatch_id"]
        if did in seen_ids:
            failures.append(f"Line {lineno}: duplicate dispatch_id {did!r}")
            continue
        seen_ids.add(did)

        if args.check_files:
            ev_abs = (root / obj["evidence_path"]).resolve()
            if not ev_abs.is_file():
                failures.append(f"Line {lineno}: evidence_path missing on disk: {obj['evidence_path']}")
                continue

        valid_count += 1

    if failures:
        for msg in failures:
            print(f"[FAIL] {msg}", file=sys.stderr)
        return 1

    print(f"[PASS] Validated {valid_count} dispatch-log entries in {log_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="karsa-tools",
        description="Deterministic ADLC utilities for KARSA scope checksums and dispatch audit logs.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_cs = sub.add_parser("checksum", help="Compute canonical SHA-256 scope_checksum.")
    p_cs.add_argument("--root", default=".", help="Project root directory.")
    p_cs.add_argument("--files", nargs="*", help="Project-relative files (space or comma separated).")
    p_cs.add_argument("--files-from", help="Path to file containing newline-delimited project-relative paths.")
    p_cs.add_argument("--git-diff", help="Git base ref (e.g. main or HEAD) to collect changed non-governance files.")
    p_cs.add_argument(
        "--exclude-governance",
        action="store_true",
        help="Exclude docs/ and artifacts/ paths even when listed explicitly.",
    )
    p_cs.add_argument("--json", action="store_true", help="Output structured JSON with sorted file list.")
    p_cs.set_defaults(func=cmd_checksum)

    p_log = sub.add_parser("log-dispatch", help="Validate and append a JSONL entry to artifacts/audit/dispatch-log.jsonl.")
    p_log.add_argument("--root", default=".", help="Project root directory.")
    p_log.add_argument("--dispatch-id", default="auto", help="DSP-NNN or 'auto' to increment automatically.")
    p_log.add_argument("--agent", required=True, help="Dispatched agent role name.")
    p_log.add_argument("--model", required=True, help="Model tier: flash | pro | inherit | flash_lite.")
    p_log.add_argument("--workspace", required=True, help="Workspace mode: main | branch | inherit | share.")
    p_log.add_argument("--phase", required=True, help="Lifecycle phase (e.g. Track S, S0, UAT, Security, Release).")
    p_log.add_argument("--item-id", required=True, help="Backlog, patch, or candidate ID.")
    p_log.add_argument("--rounds", type=int, required=True, help="Number of bounded fix rounds (>= 1).")
    p_log.add_argument("--status", required=True, help="Status: PASS | FAIL | BLOCKED | STALE_CHECKSUM.")
    p_log.add_argument("--evidence-path", required=True, help="Project-relative path under artifacts/...")
    p_log.add_argument("--failure-category", default=None, help="Null on PASS; else failure category enum.")
    p_log.add_argument("--timestamp", default=None, help="Optional UTC ISO-8601 timestamp override.")
    p_log.set_defaults(func=cmd_log_dispatch)

    p_val = sub.add_parser("validate-dispatch-log", help="Validate artifacts/audit/dispatch-log.jsonl schema.")
    p_val.add_argument("--root", default=".", help="Project root directory.")
    p_val.add_argument("--log-path", default=None, help="Optional explicit path to dispatch-log.jsonl.")
    p_val.add_argument("--check-files", action="store_true", help="Verify every evidence_path exists on disk.")
    p_val.set_defaults(func=cmd_validate_dispatch_log)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
