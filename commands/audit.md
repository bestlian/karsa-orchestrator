---
name: audit
description: Perform an evidence-based code quality, architectural maintainability, anti-slop UI, and security vulnerability audit on the current project codebase.
---

# /audit

Audit the current workspace codebase for code quality, architectural maintainability, visual design integrity, and security vulnerabilities without altering existing working code.

## Execution Steps:
1. Resolve the project root and inspect the existing project structure (backend, frontend, database, configurations, and test suites).
2. Execute `verify-quality` in **Existing Project Audit Mode**:
   - Run existing automated test suites (`pytest`, `npm test`, `npm run build`) and record real exit codes.
   - Audit modular boundary layers, cyclomatic complexity, and detect any AI design slop (card soup, monolith page stacking, unstyled typography).
   - Produce `artifacts/quality/<project-name>-quality-report.md`.
3. Execute `review-security` in **Existing Project Security Audit Mode**:
   - Reconcile threat boundaries across public callers, authenticated users, staff roles, and admin functions.
   - Trace sensitive sinks (authentication, password hashing, JWT verification, SQL injection vectors, and RBAC enforcement).
   - Produce `artifacts/security/<project-name>-security-review.md`.
4. Clean up any test/daemon processes immediately without asking for user confirmation.
5. Present a clear, consolidated executive audit summary to the user highlighting critical findings and release readiness.
