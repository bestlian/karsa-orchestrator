# Tiered ADLC Rigor & Track Sizing (`Track S / Track M / Track L`)

KARSA adapts documentation weight to the scope of work while **never skipping whole-system impact analysis, prioritization, or human approval before code changes**.

Even the smallest patch (**Track S**) MUST have an approved **Impact & Priority Plan** before `strict-programmer` touches any file, so fixes account for cross-module logic dependencies, caller contracts, and overall application flow—not just local function best practices.

---

## 1. Track Selection Matrix

Classify every incoming engineering request into one of three tracks during initial triage. If scope boundaries are ambiguous, state the recommended track and confirm once with the user.

| Track | Scope & Typical Requests | Mandatory Pre-Code Planning Artifacts | Human Approval Gate | Verification & Merge Gate |
|---|---|---|---|---|
| **Track S** *(Patch / Hotfix / Security Upgrade)* | Bug fix, CVE dependency upgrade, single-concern hardening, small config/validation fix on an existing codebase | **`artifacts/plans/<change-id>-impact-plan.md`** (Whole-System Impact Map, Cross-Logic Ripple, Priority & Sequence, Rollback Plan, Verification Proof Plan) | Approve Impact & Priority Plan before coding | `strict-programmer` (`Workspace: branch`) → `integration-tester` + `security-scanner` (`/security-scan` / affected checks) → `VERDICT pass` → Lead merges to `main` |
| **Track M** *(Brownfield Enhancement / Migration)* | New feature module on an existing codebase, framework/SDK major upgrade (e.g. `.NET 10`, React/Next major), multi-controller refactor | **Brownfield Planning Set (`artifacts/plans/` or `docs/`):**<br>1. Change Brief & Whole-System Impact Analysis<br>2. Prioritized Execution & Rollback Plan<br>3. Contract / API Delta & Point-to-Point Test Checklist<br>4. Baseline Security Scan (`scan_security.py`) | Approve Brownfield Plan before coding | `strict-programmer` (`Workspace: branch`) → `integration-tester` (A2A max 3 rounds) → `verify-quality` + `security-scanner` (`review-security`) → Merge Gate → Lead merges to `main` |
| **Track L** *(Greenfield Full-Stack Application)* | New web, mobile, cross-platform, or full-stack application built from scratch | **Full 15-Document Contract Suite (`docs/01`–`docs/15`)** audited by `delivery-planner` against `depth-rubric.md` | Brief Approval → Design/Arch Approval → Master Planning Approval → Development Start Authorization | Full 7-Phase Pipeline (Scaffold Gate, TDD, 4-Layer Proof, Parallel UAT + Full Security Audit, Merge Gate, Release Handover) |

### Escalation Rules (Automatic Track Promotion)
- **Track S → Track M:** Escalate immediately if impact analysis reveals database schema changes, breaking API contract changes across FE/BE, authentication/RBAC redesign, or >3 coupled modules affected.
- **Track M → Track L:** Escalate if the work introduces a brand-new standalone service/app requiring fresh product discovery, UX architecture, and full domain modeling.

---

## 2. Track S Mandatory Artifact: Impact & Priority Plan

Save to `<project-root>/artifacts/plans/<change-id>-impact-plan.md`. Zero placeholders allowed; every section must cite real files/symbols inspected on disk.

```markdown
# Track S Impact & Priority Plan — <change-id>

## 1. Problem / Trigger & Root Cause
- Concrete symptom, CVE advisory, or defect with file:line evidence.

## 2. Whole-System Impact & Cross-Logic Ripple Map
- **Direct files to change:** exact paths and symbols.
- **Upstream / Downstream callers:** FE/BE consumers, middleware order, shared helpers, background workers, external clients.
- **Invariants & Contracts affected:** HTTP status codes, JSON payload schemas, auth/RBAC boundaries, DB transaction / execution strategy, caching, logging.
- **Unintended side-effect risks & mitigations:** what could break elsewhere in the application flow and how the change prevents it.

## 3. Priority Queue & Safe Execution Sequence
| Priority | Order | Task | Dependency / Rationale | Rollback Strategy |
|---|---:|---|---|---|
| P0 (Critical) | 1 | ... | Must land first because ... | `git revert` / restore version |
| P1 (High) | 2 | ... | Depends on step 1 | ... |

## 4. Verification & Proof Plan
- Exact build, unit/integration test, security scan (`scan_security.py`), and manual/point-to-point regression checks required before merge.
- Explicit **Does NOT Prove** / post-deploy smoke test items (if any environment cannot be replicated locally).
```

---

## 3. Track M Mandatory Artifact Set (Brownfield Enhancement / Migration)

For existing codebases undergoing multi-module enhancements or framework/dependency migrations:
1. **`artifacts/plans/<change-id>-brownfield-plan.md`:** Scope boundaries, whole-system architectural ripple (middleware, ORM/DB behavior, serialization, auth, background jobs), compatibility matrix, priority sequence, and rollback strategy.
2. **`artifacts/plans/<change-id>-contract-delta.md`:** Explicit diff of API routes, request/response schemas, HTTP error codes, DB schema/queries, and FE↔BE sync requirements (or explicit proof of zero breaking changes).
3. **`artifacts/plans/<change-id>-test-checklist.md` (or `.xlsx`):** Point-to-point verification scenarios covering Auth/Security, impacted endpoints, and FE-BE integration.
4. **`artifacts/security/dependabot-ghas-report.md`:** Baseline deterministic scan from `security-scanner` before and after migration.

---

## 4. Governing Invariants Across All Tracks

1. **No Blind Edits:** `strict-programmer` never starts coding on Track S, M, or L without an approved plan artifact on disk.
2. **Whole-Flow Best Practice:** Every plan evaluates architectural coherence across the entire request/data lifecycle—not just isolated function cleanliness.
3. **Branch Isolation Preserved:** `strict-programmer` still operates in `Workspace: branch`; only Lead merges into `main` after verifier `VERDICT pass`.
4. **Bounded A2A Loops:** Verification fix loops (`strict-programmer <-> integration-tester` and `strict-programmer <-> security-scanner`) stay capped at 3 rounds across all tracks.
