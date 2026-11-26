---
name: security-scan
description: Run a read-only Dependabot-style dependency vulnerability scan (SCA), secret scan, and GHAS CodeQL SAST pre-flight check via security-scanner, produce a report, and hand off approved upgrades to strict-programmer followed by a verification re-scan.
---

# /security-scan

Run **`security-scanner`** in **Fast Dependabot / GHAS Pre-Flight Mode** (`skills/review-security/SKILL.md`) on the active project workspace.

## Execution Steps

1. Resolve the active `<project-root>`.
2. Dispatch `security-scanner` (read-only, model `flash`) to run `skills/review-security/scripts/scan_security.py` and save the report to `<project-root>/artifacts/security/dependabot-ghas-report.md`.
3. Triage any Critical/High SAST hits in source code to separate confirmed findings from false positives.
4. Present the GHAS Gate summary (`PASS` / `BLOCKED`) with dependency CVEs, redacted secret hits, confirmed SAST risks, recommended upgrades, and explicit proof gaps — **stopping without modifying any project files**.
5. If vulnerabilities or confirmed findings exist, ask the user for confirmation to hand off remediation to **`strict-programmer`** (isolated branch). Once `strict-programmer` completes the upgrades/fixes and build verification, re-dispatch **`security-scanner`** to re-scan and issue the final `VERDICT pass`.
