---
name: verify-quality
description: Use when an implementation candidate needs an evidence-based quality gate before handoff or release.
---

# verify-quality

Use this skill after `implement-feature` and alongside `review-security` to judge whether a candidate is ready for release.

The anti-slop Delivery Gate is adapted from anti-slop v3.2.4 at commit `44be68777e96d53d113edad33dbc4ab380f5d054` under the MIT License; see `THIRD_PARTY_NOTICES.md`.

## Use When

- An implementation candidate exists and needs an evidence-based quality gate.
- You need to judge release eligibility from test and check results.
- The approved increment manifest and the approved item reports for the slice are available.

## Do Not Use When

- You are still implementing the feature.
- You need architecture planning, release planning, or deployment instead of verification.
- You need to self-approve the candidate.
- The increment manifest or any required item report is unapproved.

## Goal

Produce one evidence-backed report at `artifacts/quality/<candidate-id>-quality-report.md`.

The report must show what was checked, what was skipped, what passed, what failed, and why the candidate is or is not eligible for release.

## Rules

- Do not claim a check passed unless you ran it or directly observed the result.
- Do not mark a skipped check as passed.
- Do not weaken tests, skip failures, deploy, or self-approve.
- Do not invent evidence, environment details, or results.
- If a check cannot run, record the reason and classify the gap clearly.

## Delivery Gate

Quality pass requires real interaction, recorded evidence, and direct observation.

Visual inspection alone cannot pass.

Planned checks, unknown claims, filler, and unvalidated statements do not count as evidence.

Use this compact filter for every claim before it reaches the verdict:

keep direct evidence that names the action or command, the expected result, the actual result, and an artifact reference.

reject anything that is unknown, filler, or missing validation.

Missing required evidence is a fail.

## Required Inputs

- Candidate id.
- Approved increment manifest for the release slice.
- Approved item reports for every required item in that manifest.
- Scope of the implementation candidate.
- Relevant build, test, app, or service commands.
- Any known release criteria or acceptance notes.

For UI candidates, also require all of the following:

- The current approved `experience-spec.md` and the current approved visual design contract, or VDC, revision it declares. A historically approved but superseded VDC is not valid input.
- The canonical combined visual decision references that govern the candidate. Each reference must use `experience-spec@VDC-NNN#VIS-NNN`, where each NNN is a three-digit decimal, for example `experience-spec@VDC-001#VIS-001`.
- The visual acceptance criteria.
- The expected proof for each visual acceptance criterion.

## Review Process

1. Confirm the candidate scope and the expected behavior.
2. Confirm the increment manifest and every required item report are approved. If not, stop and mark the work `blocked`.
3. For a UI candidate, resolve the current approved VDC revision from the current approved `experience-spec.md`.
4. For a UI candidate, validate that every candidate visual decision reference uses the canonical combined format, points to the resolved current approved VDC revision, and matches the implementation and backlog evidence.
5. Inspect the implementation evidence you were given, then run the relevant checks.
6. Record the action or command, the expected result, the actual result, the artifact reference, and the environment for every check.
7. Separate direct evidence from inference.
8. For a UI candidate, create a visual conformance map that links every visual acceptance criterion to the current approved contract revision, canonical combined visual decision references, expected proof, observed evidence, approved deviation if any, and result.
9. Decide release eligibility only after all applicable checks and, for a UI candidate, the visual conformance map are reviewed.

## Checks To Cover

Run the checks that apply to the candidate. If a category does not apply, record it as skipped with the reason.

- Acceptance checks.
- Unit checks.
- Integration checks.
- E2E checks.
- Regression checks.
- Failure-path checks.
- Accessibility checks.
- Performance checks.
- Compatibility checks.
- Build checks.
- Visual fidelity checks for UI candidates.

For UI candidates, the evidence set must include real click through of every interactive element, console error checks, keyboard and focus checks, contrast checks, responsive and mobile reflow checks, theme checks if the product supports them, loading, empty, error, and disabled states, and proof that no dead controls remain.

A UI candidate cannot pass on screenshots or visual inspection alone.

For Visual Fidelity, use a real browser capability at the product-approved widths. If the approved contract does not specify widths, use 375, 768, and 1280 CSS px. Exercise the relevant states, content conditions, and interactions, and compare the rendered result against the canonical combined visual decision references and their visual acceptance criteria.

Use pixel or close-fidelity comparison only when the approved reference is an approved prototype or an owned baseline, and only with equivalent content, states, and viewports. For directional references, compare only the documented attributes in the approved contract. Directional references never authorize copying another party's brand, assets, or protected expression.

Flatness, restraint, or lack of expressiveness alone is not a defect. A flat or generic-template concern fails only when the observed result contradicts an approved visual direction or acceptance criterion. Deliberate restrained or flat product-specific design may pass when it conforms to the approved contract.

When a candidate can be run, include run evidence as part of the build evidence set.

## Evidence Record

For each check, record all of the following:

- Check name.
- Action or command used.
- Expected result.
- Actual result.
- Artifact reference.
- Environment, including OS, runtime, browser, service URL, seed data, or fixtures when relevant.
- Result.
- Evidence source, such as console output, screenshots, logs, test output, or a report file.
- Skip reason, if the check was not run.

For each UI visual fidelity check, also record all of the following:

- Current approved visual contract revision resolved from the current approved `experience-spec.md`.
- Canonical combined visual decision references.
- Viewport in CSS px.
- State or content condition.
- Comparison method.
- Expected visual result and actual visual result.
- Real-browser evidence.
- Screenshot references.
- Approved deviations, or `none`.

## Defect Classification

Classify every issue you find as one of these:

- Critical, blocks release or causes data loss, security exposure, or a broken core flow.
- Major, breaks a primary user path or fails an important quality gate.
- Minor, noticeable but not release blocking.
- Informational, does not block release.

Tie each defect to evidence. If the issue is only a concern, say so plainly and do not treat it as a confirmed defect.

For UI candidates, classify each of these verified conditions as a release-blocking Major defect:

- The current approved `experience-spec.md`, its current approved VDC revision, a required canonical combined visual decision reference, or required proof is missing.
- A visual decision reference uses a stale or superseded VDC revision.
- A visual decision reference is noncanonical, split into separate VDC and VIS references, or merely implied.
- A visual decision reference does not match the implementation or backlog evidence.
- The implementation materially contradicts a governing VIS decision.
- The implementation uses a rejected default listed in the approved contract.
- A required signature moment is missing.
- The implementation loses hierarchy, density, or surface treatment explicitly required by the approved contract.
- A fidelity claim is unsupported by equivalent evidence.
- A required comparison is missing or its omission is unexplained.

Do not classify subjective taste, expressiveness, flatness, or genericness alone as a defect. Generic-template drift is blocking only when direct evidence verifies one of the approved-contract mismatches above.

## Release Eligibility

Choose one technical verdict only:

- `pass`, all applicable checks passed and no blocking defects remain.
- `conditional`, the candidate can ship only with named fixes, waivers, or follow-up checks.
- `fail`, one or more blocking defects remain, or the evidence is too weak to approve release.

Never call a result `pass` when a required check was skipped without a strong documented reason.

Never call a result `pass` when required evidence is missing, when the only support is visual inspection, or when the report lacks a real interaction record.

For a UI candidate, missing visual decision references or required visual evidence, stale or superseded references, noncanonical references, references that mismatch implementation or backlog evidence, or any other verified blocking visual defect forces `technical_verdict: fail`, even when older evidence exists. Artifact `status` remains lifecycle status and does not override or replace the technical verdict.

When the verdict is `conditional` or `fail`, create traceable remediation items that require human approval before they can return to `implement-feature`, then rerun `verify-quality` and `review-security` on the approved remediation result. Only approved nonblocking reports may proceed to `prepare-release`.

## Report Output

Write the report to `artifacts/quality/<candidate-id>-quality-report.md`.

Use this structure:

```md
# Quality Report

## Candidate
- id:
- scope:

## Handoff
~~~yaml
schema: fullstack-skill-handoff/v1
producing_skill: verify-quality
artifact_id: quality-report
output_path: artifacts/quality/<candidate-id>-quality-report.md
inputs:
  - implementation candidate
  - approved increment manifest
  - approved item reports for every required item in that manifest
  - approved specs
  - build, test, app, or service commands
  - current approved experience-spec.md, its current approved VDC revision, canonical combined visual decision refs, visual acceptance criteria, and expected proof for UI candidates
requirement_refs:
  - candidate acceptance criteria IDs
  - relevant source requirement IDs
decision_refs:
  - quality gate decision
  - canonical combined visual decision refs from the current approved experience-spec.md for UI candidates
assumptions:
  - any environment or fixture assumptions used during verification
open_questions:
  - unresolved quality questions that still need a decision
risks:
  - quality regressions, compatibility gaps, or test coverage gaps
validation_evidence:
  - acceptance checks
  - unit checks
  - integration checks
  - e2e checks
  - regression checks
  - failure-path checks
  - accessibility checks
  - performance checks
  - compatibility checks
  - build checks
  - visual conformance map with canonical combined visual decision refs, real-browser evidence, screenshots, and approved deviations for UI candidates
status: awaiting-approval
approval: pending
next_skills:
  - prepare-release
~~~

The report records the technical verdict separately from handoff status. Only a human can change the artifact to `approved`.

If the verdict is `conditional` or `fail`, replace `next_skills` with `implement-feature` after the remediation items are approved, then rerun `verify-quality` and `review-security`.

## Checks
### Acceptance
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Unit
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Integration
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### E2E
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Regression
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Failure Path
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Accessibility
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Performance
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Compatibility
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Build
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:

### Visual Fidelity
- action-or-command:
- expected:
- actual:
- artifact-reference:
- environment:
- result:
- evidence:
- skip-reason:
- current-approved-visual-contract-revision:
- visual-decision-refs:
- visual-acceptance-criteria:
- expected-proof:
- visual-conformance-map:
- viewport-css-px:
- state-or-content-condition:
- comparison-method:
- browser-evidence:
- screenshots:
- approved-deviations:

## Defects
- severity:
- summary:
- evidence:
- impact:

## Remediation Items
- id:
- source_defect:
- required_change:
- approval_status:
- next_skill:
- rerun_scope:

## Release Decision
- technical_verdict:
- rationale:

## Notes
- observations:
- skipped-checks:
```

## Handoff Requirements

The handoff must include the shared schema fields and keep artifact status separate from the technical verdict.

Approval is only allowed when the evidence supports the chosen technical verdict.

## Completion Criteria

Finish only when all of these are true:

- The report file exists at the required path.
- Every applicable check is recorded with action or command, expected result, actual result, artifact reference, environment, and result.
- Every skipped check has a reason.
- Every defect is classified.
- For a UI candidate, the visual conformance map covers every visual acceptance criterion and carries the current approved VDC revision resolved from the current approved `experience-spec.md`, canonical combined visual decision refs, expected proof, real-browser evidence, screenshots, and approved deviations.
- For a UI candidate, missing, stale, superseded, noncanonical, or mismatched visual decision refs, missing required visual evidence, or any other verified blocking visual defect results in `technical_verdict: fail`.
- The release decision is explicit.
- No unsupported pass claims remain.
