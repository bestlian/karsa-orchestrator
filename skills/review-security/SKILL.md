---
name: review-security
description: Use when reviewing an implementation candidate or an existing application codebase for exploitable security risks, authorization boundaries, and release blockers.
---

# Review Security

Use this skill after `implement-feature` and alongside `verify-quality` to review one implementation candidate for security issues that can block release.

## Use When

- One implementation candidate needs an exploitability-focused security review.
- An existing application codebase needs an exploitability-focused security audit, auth/RBAC review, or sensitive sink validation.
- You need to validate trust boundaries, attack paths, and sensitive sinks.
- The increment manifest and the completed item reports for the slice are available under the authorized development scope.

## Do Not Use When

- You need general quality verification, release planning, or deployment.
- You need to self-approve or scan external systems.
- You do not have a concrete candidate or threat surface.
- The increment manifest or any required item report is missing, incomplete, or outside the authorized scope.

## Goal

Find exploitable risks, prove them with evidence, and separate real release blockers from generic hardening advice.

Attribution: this evidence discipline is adapted from curated anti-slop guidance. See `THIRD_PARTY_NOTICES.md`.

## Shared Evidence Filter

Use this filter for every security claim:

- Evidence, cite a test, config, code path, scan, or review artifact.
- Unknown, if you cannot cite one yet.
- Filler, remove unsupported certainty words and vague praise.
- Validation, keep checks local and read-only by default, and ask for approval before destructive, external, or live-exploit actions.

Do not label anything `secure`, `compliant`, `production-ready`, or `no vulnerabilities` unless the report includes direct evidence for that exact claim.

Each issue must be labeled explicitly as one of:

- confirmed finding
- rejected hypothesis
- untested surface
- residual risk

If an untested surface is release-critical, treat it as blocked until it is validated or explicitly waived.

## Do Not

- Do not use real credentials.
- Do not run destructive tests.
- Do not scan external systems.
- Do not try to exploit third parties.
- Do not copy secrets into reports.
- Do not deploy anything.
- Do not self-approve the review.

## Review Frame

Start by reconciling the threat model. State:

- What the component assumes about trusted callers, trusted data, and trusted infrastructure.
- Which inputs cross trust boundaries.
- Which identities, sessions, tenants, files, queues, jobs, or services can be influenced by an attacker.
- Which assets would be harmed if the candidate fails.

If the assumptions are unclear, mark that as a review gap and lower confidence until the code proves the boundary.

## What To Review

Check the candidate for:

- Authentication
- Authorization
- Sessions and token handling
- Data protection and privacy
- Injection
- SSRF
- File uploads
- Secrets handling
- Dependencies and supply chain risk
- Logging and leakage
- Abuse cases
- Business logic flaws

For each area, ask whether an attacker can cross a trust boundary, reach a sensitive sink, and cause measurable harm.

For JWT User/Staff candidates, independently inspect and, where safe, exercise the actual verification path: a fixed configured allowed algorithm, server signature verification, required expiry, no token-header algorithm selection, and an active subject plus current server-controlled role lookup. Check that production secrets have no hard-coded fallback, test-only secrets are isolated and labeled, passwords use Argon2 or bcrypt rather than raw SHA-256, no default shared administrator credential exists, and public registration cannot create Staff. Trace Bearer handling through the frontend's storage, refresh if any, expiry, logout, logging, and XSS or CSRF assumptions. Confirm the public matrix is limited to approved catalog, login, and registration paths; test protected `/api/user/...` ownership and `/api/staff/...` role boundaries with missing, tampered, missing-expiry, expired, wrong-role, and cross-user credentials. Missing, invalid, or expired credentials should be `401`; valid but unauthorized identities must follow the approved `403` or scoped `404` policy.

## Evidence Standard

Every finding must include:

- Exact file and symbol.
- Attacker preconditions.
- Attack path.
- Impact.
- Why the issue is exploitable.
- A calibrated severity.
- A minimal remediation.
- The claim status, using the explicit labels in the shared evidence filter.

If you cannot name the preconditions and impact, it is not a finding.
If you cannot cite evidence, the claim stays `unknown`.

## Severity Rules

Use calibrated labels such as `low`, `medium`, `high`, and `critical` only when the exploit path is concrete.

- `critical`, when exploitation is straightforward and the impact is severe.
- `high`, when exploitation is practical and the impact is serious.
- `medium`, when the issue is real but limited in reach or impact.
- `low`, when the weakness is narrow, indirect, or hard to abuse.

Tie severity to exploitability and impact, not to code smell.

## Existing Project Security Audit Mode

When invoked on an existing codebase:
1. Reconcile threat boundaries across public callers, authenticated users, staff roles, and administrative functions.
2. Trace sensitive sinks: authentication/password hashing, JWT verification, SQL injection vectors, and role-check enforcement.
3. Validate privilege escalation paths and unauthenticated endpoint leakage.
4. Issue an evidence-backed security review at `artifacts/security/<project-name>-security-review.md`.

## Workflow

1. Identify the candidate and its surrounding flow.
2. Re-read the increment manifest and every required item report at their exact paths and revisions. Confirm explicit approval and technical result, compare them with the candidate, and block on any mismatch. Tie reviewed code to a stable revision or checksum of executable, configuration, and source scope only; a change in that scope invalidates affected review evidence, while governance documents and review state do not. Never trust a compaction summary, screenshot, label, or metadata normalization as authoritative evidence.
3. Reconcile threat assumptions and trust boundaries.
4. Trace attacker-controlled inputs to sensitive sinks.
5. Check whether auth, authz, session, or tenant checks can be bypassed.
6. Look for data exposure, logging leaks, or unsafe persistence.
7. Check for injection, SSRF, upload abuse, or dependency risk.
8. Confirm whether the issue can be reached in a realistic deployment.
9. Write the result with evidence, severity, remediation, and claim status.

For production-ready work, review the substantive backend API/database integration and frontend API use, staff roles and authorization, secrets/configuration, logging, durable storage, migrations, backups, and process/concurrency assumptions that apply to the approved scope. Recommend an independent security or operational audit when warranted by payment, sensitive data, or privilege risk; that recommendation is not an audit result. Use isolated nonproduction fixtures and never a project live database.

For reservation, inventory, order, payment, or transactional work, verify that concurrency and conflict controls prevent race conditions, that concurrent requests use separate fixture connections matching the approved deployment model, and that Staff/Admin operations and manual settlements are idempotent, audited, and transactionally consistent with underlying records and financial totals. Record an untested required property as blocked rather than inferring safety from a report.

## Report Output

Write the review to:

`artifacts/security/<candidate-id>-security-review.md`

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`, including security reports and remediation evidence. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

The report must include:

- Candidate id
- Approved increment manifest for the release slice
- Approved item reports for every required item in that manifest
- Scope
- Threat assumptions
- Trust boundaries
- Claim status for each security statement, using `confirmed finding`, `rejected hypothesis`, `untested surface`, or `residual risk`
- Findings
- Security verdict
- Rejected or downgraded candidates
- Residual risk
- Handoff status

## Finding Format

For each finding, include:

- Title
- Severity
- Evidence
- Claim status
- Preconditions
- Impact
- Attack path
- Remediation

## Remediation Items
- id:
- source_finding:
- required_change:
- approval_status:
- next_skill:
- rerun_scope:

## Security Verdict

Choose one technical verdict only:

- `pass`, when no exploitable issues remain.
- `pass-with-findings`, when issues are documented but do not block release.
- `block`, when at least one finding is release blocking.

When the verdict is `block`, create traceable remediation items that require human approval before they can return to `implement-feature`, then rerun `verify-quality` and `review-security` on the approved remediation result. Only approved nonblocking reports may proceed to `prepare-release`.

## Handoff

```yaml
schema: fullstack-skill-handoff/v1
producing_skill: review-security
artifact_id: security-review
output_path: artifacts/security/<candidate-id>-security-review.md
inputs:
  - implementation candidate
  - approved increment manifest
  - approved item reports for every required item in that manifest
  - candidate scope
  - threat assumptions and trust boundaries
requirement_refs:
  - candidate scope IDs
  - security-sensitive requirement IDs when available
decision_refs:
  - security findings and downgrade decisions
assumptions:
  - any threat assumptions that remain visible in the review
open_questions:
  - unresolved security questions that still need a decision
risks:
  - auth, authz, injection, secrets, or supply-chain risks
validation_evidence:
  - exact file and symbol references
  - attacker preconditions
  - attack path
  - impact
  - remediation
status: awaiting-approval
approval: pending
next_skills:
  - prepare-release
```

The report records the technical verdict separately from handoff status.

If the verdict is `block`, replace `next_skills` with `implement-feature` after the remediation items are approved, then rerun `verify-quality` and `review-security`. If the verdict is `pass` or `pass-with-findings` and the report is approved, keep `prepare-release`.

## Chat Review Protocol

Label the canonical review with its immutable `Artifact Revision`. A Review Record is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records and permit only one active request across the lifecycle. It binds request ID, canonical path, content revision, exact question, simplified options (`Yes`, `No`, and `Other` for user typing/comments), prompt evidence, and the source user reply or decision evidence.

Use native `ask_question` only when the host exposes it with its actual schema; otherwise ask: `Review artifacts/security/<candidate-id>-security-review.md@[revision]. Approve this exact content?` Options are `Yes` (approve), `No` (reject and pause), and `Revision` (meaningful freeform feedback). A direct Yes or No is valid only for this unchanged shown question and needs no path, revision, or host ID. Stale, duplicate, summary, unrelated, or host replies have no effect. On resume, re-read the review and show the bound pending question once.

Yes resolves the record and updates only closed governance metadata to approved. No resolves it as rejected and waits for an explicit user request to revise. Comments or feedback entered via `Other` (or user typing) without meaningful content ask only for clarifying feedback; sufficient feedback sets the review to `draft` and routes to this owner. A substantive revision supersedes the old record, creates a new Artifact Revision, invalidates affected evidence and approvals, and asks again only after the revised review returns to `awaiting-approval`. Do not intentionally create, update, or open `implementation_plan.md`, editor tabs, or `RequestFeedback` metadata. Native host presentations are not approval evidence, and host-mandated opening cannot be controlled by this plugin.

## Completion Criteria

The review is complete only when all of these are true:

- Threat assumptions and trust boundaries are written down.
- Every real finding has evidence, preconditions, impact, severity, and remediation.
- Non findings are explicitly rejected or downgraded.
- The report is saved to `artifacts/security/<candidate-id>-security-review.md`.
- The handoff block is present and uses the shared schema.
- Release blockers are clearly marked so `prepare-release` can stop when needed.
