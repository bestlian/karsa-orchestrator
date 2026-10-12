#!/usr/bin/env python3
"""
CI Consistency & Anti-Drift Linter for KARSA Orchestrator Plugin
Checks:
1. Parity between skills/<skill>/ and dist/<skill>.zip (files and byte content)
2. Stale naming detection (e.g. execution-manager, fullstack-orchestrator) outside CHANGELOG.md
3. Subagent definition validity and least-privilege tool hygiene
"""

import hashlib
import os
import sys
import zipfile
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SKILLS = [
    "discover-product",
    "design-experience",
    "define-architecture",
    "plan-delivery",
    "karsa-orchestrator",
    "implement-feature",
    "verify-quality",
    "review-security",
    "prepare-release",
]

SUBAGENTS = [
    "delivery-planner",
    "integration-tester",
    "strict-programmer",
]

FORBIDDEN_TERMS = [
    "execution-manager",
    "fullstack-orchestrator",
    "scope-mapper",
    "contract-manager",
    "contract-reviewer",
    "execution-strategist",
]

FORBIDDEN_SUBAGENT_TOOLS = [
    "schedule",
    "generate_image",
    "notebook_edit",
]

TEXT_EXTENSIONS = {
    ".md", ".py", ".json", ".csv", ".sh", ".txt", ".yml", ".yaml",
    ".html", ".css", ".js", ".ts", ".xml", ".svg"
}

errors = []


def hash_content(data: bytes, filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    if ext in TEXT_EXTENSIONS:
        data = data.replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def check_skill_parity():
    print("Checking skill directory vs dist/*.zip parity...")
    for skill in SKILLS:
        skill_dir = os.path.join(ROOT, "skills", skill)
        zip_path = os.path.join(ROOT, "dist", f"{skill}.zip")

        if not os.path.isdir(skill_dir):
            errors.append(f"Missing skill directory: skills/{skill}")
            continue

        if not os.path.isfile(zip_path):
            errors.append(f"Missing zip archive: dist/{skill}.zip")
            continue

        # Collect files from disk
        disk_files = {}
        for root_dir, _, files in os.walk(skill_dir):
            for f in files:
                rel = os.path.relpath(os.path.join(root_dir, f), skill_dir).replace("\\", "/")
                with open(os.path.join(root_dir, f), "rb") as fh:
                    disk_files[rel] = hash_content(fh.read(), f)

        # Collect files from zip
        zip_files = {}
        with zipfile.ZipFile(zip_path, "r") as zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                norm_name = info.filename.lstrip("./").replace("\\", "/")
                zip_files[norm_name] = hash_content(zf.read(info.filename), info.filename)

        # Compare sets
        disk_set = set(disk_files.keys())
        zip_set = set(zip_files.keys())

        if disk_set != zip_set:
            missing_in_zip = disk_set - zip_set
            extra_in_zip = zip_set - disk_set
            if missing_in_zip:
                errors.append(f"[{skill}] Files in skills/ but missing in dist zip: {missing_in_zip}")
            if extra_in_zip:
                errors.append(f"[{skill}] Files in dist zip but missing in skills/: {extra_in_zip}")

        # Compare content hashes for common files
        for common in disk_set & zip_set:
            if disk_files[common] != zip_files[common]:
                errors.append(f"[{skill}] Content mismatch in file: {common} (disk != zip)")


def check_stale_names():
    print("Checking for stale naming drifts...")
    skip_dirs = {".git", "dist", ".gemini", "node_modules", "__pycache__"}
    skip_files = {"CHANGELOG.md", "lint-consistency.py"}

    for root_dir, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for f in files:
            if f in skip_files or f.endswith(".zip") or f.endswith(".png") or f.endswith(".ico"):
                continue
            file_path = os.path.join(root_dir, f)
            rel_path = os.path.relpath(file_path, ROOT).replace("\\", "/")
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as fh:
                    for line_no, line in enumerate(fh, start=1):
                        for term in FORBIDDEN_TERMS:
                            if term in line:
                                errors.append(f"Stale term '{term}' found at {rel_path}:{line_no}")
            except Exception as e:
                errors.append(f"Failed to read file {rel_path}: {e}")


def check_agent_least_privilege():
    print("Checking subagent definitions and least privilege guardrails...")
    # Check lead agent
    karsa_path = os.path.join(ROOT, "agents", "karsa.md")
    if not os.path.isfile(karsa_path):
        errors.append("Lead agent missing: agents/karsa.md")

    # Check each subagent
    for name in SUBAGENTS:
        agent_path = os.path.join(ROOT, "agents", name, "agent.md")
        if not os.path.isfile(agent_path):
            errors.append(f"Subagent definition missing: agents/{name}/agent.md")
            continue

        with open(agent_path, "r", encoding="utf-8") as fh:
            content = fh.read()

        # Parse frontmatter tools
        fm_match = re.search(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
        if not fm_match:
            errors.append(f"agents/{name}/agent.md has invalid frontmatter")
            continue

        frontmatter = fm_match.group(1)
        for forbidden in FORBIDDEN_SUBAGENT_TOOLS:
            if re.search(rf"-\s+{forbidden}\b", frontmatter):
                errors.append(f"agents/{name}/agent.md has forbidden tool under least-privilege: '{forbidden}'")


def main():
    print(f"Running consistency lint in: {ROOT}")
    check_skill_parity()
    check_stale_names()
    check_agent_least_privilege()

    if errors:
        print(f"\n[FAIL] Consistency Lint failed with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\n[PASS] All consistency and anti-drift checks passed successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
