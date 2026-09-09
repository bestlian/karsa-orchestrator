---
name: prepare-release
description: Use when approved quality and security evidence is ready and you need a release plan that stops before deployment.
---

# Prepare Release

Create a release plan from approved quality and security evidence. Stop at planning and approval. Do not deploy.

## Use This Skill When

Use this skill when the work is ready for release planning and you have approved quality and security reports whose technical verdicts already satisfy the release rules.

## Do Not Use When

- Either report is missing, unapproved, or contains blockers.
- The quality report technical verdict is `conditional` or `fail`.
- The security report technical verdict is `block`.
- You need to deploy, run migrations, or change shared infrastructure.
- You need release execution instead of planning.

## Required Inputs

1. Approved quality report with technical verdict `pass`.
2. Approved security report with technical verdict `pass` or `pass-with-findings` and no blocker.
3. Release candidate identifier.
4. Version or build identifier.
5. Scope summary for the release.

Before planning, re-read the quality report, security report, implementation reports, and increment manifest at their exact paths and revisions. Confirm each explicit approval and technical result, compare them with the release candidate, and block on any mismatch. Tie tested code to a stable revision or checksum of executable, configuration, and source scope only; a change in that scope invalidates affected evidence, while governance documents and review state do not. Do not promote labels from summaries, screenshots, manifest normalization, or a report alone. Quality must be exactly `pass`, and security must be `pass` or `pass-with-findings` with only nonblocking findings and no blocker.

This skill plans one candidate release slice, not the end of the original request. Re-read the approved backlog's Full-Request Obligation Ledger and every required slice manifest before writing the plan. The plan must name delivered obligations, required obligations still pending or blocked, and the next authorized route. An approved release plan may finalize its candidate slice only. It must not make an application-ready, full-scope-delivered, or request-complete claim while any required ledger entry remains unresolved. If required work remains and no next item is Ready, the next route is `plan-delivery` for a traceable planning repair, not completion. A bare `Yes` to this plan never reduces remaining scope or requires a repeated development authorization for the same approved backlog revision and scope.

If either report is missing, unapproved, or contains blockers, or if the technical verdict does not satisfy these rules, stop and report that the release cannot be planned yet.

## Release Planning Eligibility

1. Human approval is required for both reports.
2. Quality planning accepts only technical verdict `pass`.
3. Security planning accepts technical verdict `pass` or `pass-with-findings` only when findings are nonblocking and the report has no blocker.
4. `conditional`, `fail`, and `block` remain in remediation even if the artifact is approved or waiver wording suggests otherwise.
5. Artifact approval does not override the technical verdict.

## What To Produce

Write the release plan to `artifacts/release/<candidate-id>-release-plan.md`.

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`, including release plans and release evidence. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

The plan must include:

1. Scope and version.
2. Prerequisites.
3. Migration and backup steps.
4. Rollout plan.
5. Rollback plan.
6. Monitoring and alerts.
7. Verification steps.
8. Communications plan.
9. Ownership and approvers.
10. Go or no go checklist.
11. Residual risks.

The plan must also include a separate final Delivery Gate section. That gate reports one overall verdict, exactly `PASS` or `FAIL`, and it stays separate from the artifact status and from the upstream technical verdicts.

The plan must name the truthful release classification separately from deployment: `prototype` is a validated demonstration with its recorded limits; `MVP` is a defined scope label, not proof of production readiness; `production-ready` means the approved proportional readiness gates have evidence; `deployed` requires separate authorized deployment execution and observed deployment evidence outside this suite. An approved payment simulator is valid simulation evidence but cannot support a live-payment-ready claim.

## Final Delivery Gate

Use one compact shared filter before writing the final verdict:

1. Evidence, approved reports, upstream technical verdicts, manifest checks, notices, and blocker status count.
2. Unknown, missing, or unclear items count as missing evidence.
3. Filler, praise, and mixed status language do not count as evidence.
4. Validation claims need direct proof in the plan, not adjectives.

The final delivery output must contain one and only one overall verdict line, exactly `PASS` or `FAIL`.

Set the verdict to `FAIL` if any of these are missing or unresolved:

1. Required quality evidence, or an approved quality report whose technical verdict is not exactly `pass`.
2. Required security evidence, or an approved security report whose technical verdict is not `pass` or `pass-with-findings` with only nonblocking findings and no blocker.
3. Unresolved approvals, blockers, or remediation-only verdicts (`conditional`, `fail`, `block`).
4. For a UI candidate, missing required real-browser evidence, including run URL, viewport, actions and observed outcomes, console result, and linked artifacts. Build success, a running process, or HTTP 200 cannot substitute.
5. Archive manifest checks.
6. Required third party notice preservation, including an attribution pointer to `THIRD_PARTY_NOTICES.md`, and a comprehensive user-facing `README.md` in the project root documenting project purpose, quickstart setup, prerequisites, seed accounts, and automated test execution.
7. For a production-ready target, substantive backend/frontend API integration, durable data, applicable staff authorization, configuration/secrets, migrations/backups, logging/operations, concurrency/process evidence, and required independent audit recommendations or explicit scope limits.
8. A Full-Request Obligation Ledger showing every required original `FR-*` and accepted proposal as delivered in the candidate set, explicitly remaining for a later slice, blocked, or explicitly scope-reduced by the user. Any remaining required entry makes an application-complete claim `FAIL`, even when this candidate slice can be released.

The gate must reject mixed status language. Do not claim `ready`, `secure`, `production ready`, or similar wording unless the plan cites evidence for each claim.

The gate must preserve distributable license and notice text. If a distributable omits required notices, the verdict is `FAIL`.

Keep the artifact status as `awaiting-approval`. The status is not the verdict. A separate human go or no go approval is still required before any deployment work starts.

## Procedure

1. Confirm the quality report is approved and has no blockers.
2. Confirm the quality report technical verdict is exactly `pass`.
3. Confirm the security report is approved, its technical verdict is `pass` or `pass-with-findings`, and any findings are nonblocking with no blocker.
4. Summarize the release scope and exact version.
5. List prerequisites that must be true before release starts.
6. Describe migration and backup actions, but do not run them.
7. Define the rollout sequence and the stop points for manual review.
8. Define rollback triggers, rollback steps, and who decides to roll back.
9. List monitoring signals, alert thresholds, and the response owner.
10. Define the verification checks that prove the release worked.
11. Draft the communication plan for stakeholders and support.
12. Record the release owner, the approver, and any required support roles.
13. Add a go or no go checklist with explicit pass criteria.
14. Capture residual risks that remain after approval.
15. State full-request scope status: delivered obligations, remaining obligations, and next route. Use `application not ready` whenever required scope remains.
16. End the document with status `awaiting-approval`.
17. Add the final Delivery Gate with a single overall verdict line, exactly `PASS` or `FAIL`, plus the rationale that cites the upstream technical verdicts.

## Completion Criteria

Finish only when all of these are true:

1. Both reports are approved.
2. The quality report technical verdict is exactly `pass`.
3. The security report technical verdict is `pass` or `pass-with-findings`, and any findings are nonblocking with no blocker.
4. The release decision rationale states why the upstream verdicts allow planning or why planning is blocked.
5. The artifact status remains `awaiting-approval`.
6. The final Delivery Gate is explicit and separate from the upstream verdicts.

## Hard Rules

1. Do not deploy.
2. Do not publish.
3. Do not run migrations.
4. Do not change shared infrastructure.
5. Do not create accounts.
6. Do not incur costs.
7. Do not self approve.
8. Do not treat this skill as release execution.
9. Require separate, explicit human authorization before any deployment work starts.
10. Preserve distributable license and notice text, including `THIRD_PARTY_NOTICES.md` attribution pointers.
11. Never let human artifact approval override an ineligible upstream technical verdict.
12. Keep `PASS | FAIL` as the release plan verdict and keep report verdicts separate.
13. Ensure all background processes, dev servers, and daemon tasks from earlier phases are completely terminated before presenting the release plan, ensuring clean ports and environment for user handover without requiring user confirmation.

## Handoff

```yaml
schema: fullstack-skill-handoff/v1
producing_skill: prepare-release
artifact_id: release-plan
output_path: artifacts/release/<candidate-id>-release-plan.md
inputs:
  - approved quality report with technical verdict `pass`
  - approved security report with technical verdict `pass` or `pass-with-findings`
  - release candidate identifier
  - version or build identifier
  - release scope summary
requirement_refs:
  - quality report IDs
  - security report IDs
decision_refs:
  - go or no go decision inputs
assumptions:
  - any release assumptions that remain visible in the plan
open_questions:
  - unresolved release questions that still need a decision
risks:
  - rollout, rollback, monitoring, or communication risks
validation_evidence:
  - prerequisites
  - migration and backup steps
  - rollout plan
  - rollback plan
  - monitoring and alerts
  - verification steps
  - communications plan
  - go or no go checklist
  - archive manifest checks
  - third party notice preservation
status: awaiting-approval
approval: pending
next_skills: []
```

## Chat Review Protocol

Label the canonical release plan with its immutable `Artifact Revision`. A Review Record is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records and permit only one active request across the lifecycle. It binds request ID, canonical path, content revision, exact question, simplified options (`Yes`, `No`, and `Other` for user typing/comments), prompt evidence, and the source user reply or decision evidence.

Use native `ask_question` only when the host exposes it with its actual schema; otherwise ask: `Review artifacts/release/<candidate-id>-release-plan.md@[revision]. Approve this exact content?` Options are `Yes` (approve), `No` (reject and pause), and `Revision` (meaningful freeform feedback). A direct Yes or No is valid only for this unchanged shown question and needs no path, revision, or host ID. Stale, duplicate, summary, unrelated, or host replies have no effect. On resume, re-read the plan and show the bound pending question once.

Yes resolves the record and updates only closed governance metadata to approved. No resolves it as rejected and waits for an explicit user request to revise. Comments or feedback entered via `Other` (or user typing) without meaningful content ask only for clarifying feedback; sufficient feedback sets the plan to `draft` and routes to this owner. A substantive revision supersedes the old record, creates a new Artifact Revision, invalidates affected evidence and approvals, and asks again only after the revised plan returns to `awaiting-approval`. Do not intentionally create, update, or open `implementation_plan.md`, editor tabs, or `RequestFeedback` metadata. Native host presentations are not approval evidence, and host-mandated opening cannot be controlled by this plugin.

The plan stops before deployment. If deployment is requested, hand off to the deployment flow under separate human authorization.

## Release Plan Format

Use a direct, reviewable structure like this:

1. Title and candidate id.
2. Version and scope.
3. Evidence summary.
4. Prerequisites.
5. Migration and backup.
6. Rollout.
7. Rollback.
8. Monitoring and alerts.
9. Verification.
10. Communications.
11. Ownership.
12. Go or no go checklist.
13. Residual risks.
14. Status: `awaiting-approval`.
15. Final Delivery Gate, with one overall verdict line, exactly `PASS` or `FAIL`.
16. Full-request scope status and next authorized route; never use slice approval to close unresolved required scope.

## Stop Condition

When the plan is written, stop. If deployment is requested, require a separate explicit human authorization and hand off to the proper deployment flow.
