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

Before planning, confirm the approved quality report has technical verdict exactly `pass`, and the approved security report has technical verdict `pass` or `pass-with-findings` with only nonblocking findings and no blocker.

If either report is missing, unapproved, or contains blockers, or if the technical verdict does not satisfy these rules, stop and report that the release cannot be planned yet.

## Release Planning Eligibility

1. Human approval is required for both reports.
2. Quality planning accepts only technical verdict `pass`.
3. Security planning accepts technical verdict `pass` or `pass-with-findings` only when findings are nonblocking and the report has no blocker.
4. `conditional`, `fail`, and `block` remain in remediation even if the artifact is approved or waiver wording suggests otherwise.
5. Artifact approval does not override the technical verdict.

## What To Produce

Write the release plan to `artifacts/release/<candidate-id>-release-plan.md`.

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
4. Archive manifest checks.
5. Required third party notice preservation, including an attribution pointer to `THIRD_PARTY_NOTICES.md`.

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
15. End the document with status `awaiting-approval`.
16. Add the final Delivery Gate with a single overall verdict line, exactly `PASS` or `FAIL`, plus the rationale that cites the upstream technical verdicts.

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

## Stop Condition

When the plan is written, stop. If deployment is requested, require a separate explicit human authorization and hand off to the proper deployment flow.
