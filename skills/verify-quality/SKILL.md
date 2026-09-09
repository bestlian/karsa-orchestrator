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
- The increment manifest and the completed item reports for the slice are available under the authorized development scope.

## Do Not Use When

- You are still implementing the feature.
- You need architecture planning, release planning, or deployment instead of verification.
- You need to self-approve the candidate.
- The increment manifest or any required item report is missing, incomplete, or outside the authorized scope.

## Goal

Produce one evidence-backed report at `artifacts/quality/<candidate-id>-quality-report.md`.

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`, including quality reports, evidence, screenshots, and conformance artifacts. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

The report must show what was checked, what was skipped, what passed, what failed, and why the candidate is or is not eligible for release.

## Rules

- Do not claim a check passed unless you ran it or directly observed the result.
- Do not mark a skipped check as passed.
- Do not weaken tests, skip failures, deploy, or self-approve.
- Do not invent evidence, environment details, or results.
- If a check cannot run, record the reason and classify the gap clearly. A missing required UI browser check is a blocking evidence gap, not a waivable skipped check.
- Treat implementation-report claims as leads, not proof. Independently inspect current source, config, manifests, conventions, and tests before you trust them.
- Before QA or resume, re-read every required source report at its exact path and revision, verify its technical result and scope authorization, and compare each fact with the increment manifest and candidate. A mismatch blocks the verdict; labels, screenshots, summaries, and metadata normalization cannot promote it. Tie the tested code to a stable revision or checksum of executable, configuration, and source scope only; governance documents and review state do not invalidate evidence. Invalidate affected evidence when that scope changes.
- Require approved maintainability architecture decisions, backlog criteria, implementation evidence, repository conventions, source, manifests, configuration, and tests as relevant inputs.
- Use configured repository checks for dependency direction, cycles, complexity, size, dead code, and unused dependencies when they exist. If they do not exist, inspect directly where feasible and record the lower assurance.
- For cycles, block any new, forbidden, expanded, changed, unapproved, or unresolved cycle. An unchanged existing cycle may avoid that specific defect only when a human-approved `DEP-NNN` exception exists, the exact bounded edges and rationale match current source, and direct evidence shows no expansion or new risk. That exception does not waive other maintainability failures, and acyclic candidates pass this criterion.
- Never call an absent check passed. Missing optional static checks do not automatically require installation and must be recorded as evidence gaps. Required UI browser capability is different: recover it through a supported, permitted project-bound path or fail the UI candidate for missing required evidence.
- Local check results must be one of `pass`, `fail`, `evidence-gap`, or `not-applicable`. Keep those separate from lifecycle status and `technical_verdict`.
- A tool gap alone is not a defect. An unresolved required property is an evidence gap, and it blocks `technical_verdict: pass`. Required real-browser UI evidence is an unresolved required property, so build success, a running process, and an HTTP 200 cannot replace it.
- Accept a source-backed check only when its record contains command, working directory, exit code, raw-output artifact path, tested source revision or checksum, expected result, and actual result. Missing fields are an evidence gap, not a pass.

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
- Approved maintainability architecture decisions and backlog criteria, when the candidate includes maintainability constraints.
- Implementation evidence, repository conventions, source, manifests, configuration, and tests, as relevant to the candidate.
- Scope of the implementation candidate.
- The approved readiness target, architecture shape, and acceptance boundary, including prototype demo limitations or the full-stack API, persistence, shared-data, and authentication/authorization boundaries relevant to the release slice.
- Relevant build, test, app, or service commands.
- Any known release criteria or acceptance notes.

For UI candidates, also require all of the following:

- The current approved `experience-spec.md` and the current approved visual design contract, or VDC, revision it declares. A historically approved but superseded VDC is not valid input.
- The canonical combined visual decision references that govern the candidate. Each reference must use `experience-spec@VDC-NNN#VIS-NNN`, where each NNN is a three-digit decimal, for example `experience-spec@VDC-001#VIS-001`.
- The visual acceptance criteria.
- The expected proof for each visual acceptance criterion.

## Browser Capability And Recovery

Use a native browser capability first. A browser skill being present does not establish that its runtime, browser binary, or driver works. Before a UI candidate can pass:

1. Launch a real browser against the project-bound run URL and exercise the required views, states, and interactions.
2. If the native capability is unavailable, use only a documented, supported install or configuration path within current permission and the project boundary. Do not disable safeguards or fabricate undocumented commands.
3. If a built-in driver download fails, record the exact failure reason and output, then try one supported alternative when it exists. Do not repeat a failed download blindly.
4. Ask a human before any external download, global install, elevated permission, account change, or other action outside the project boundary.
5. If a permitted working browser cannot be recovered, record a blocking evidence gap and issue `technical_verdict: fail` for the UI candidate. Do not use static checks, screenshots, build success, or HTTP 200 as substitution.

A host-native `browser_subagent` may collect bounded browser interaction evidence only. The executing agent retains lifecycle ownership and must make all edits, approvals, routing, and joins.

For a newly scaffolded UI, record starter-screen detection and entrypoint wiring before evaluating an application-ready claim. A starter screen, even if it loads, proves only the scaffold boundary.

## Review Process

1. Confirm the candidate scope and the expected behavior.
2. Confirm the increment manifest and every required item report are approved. If not, stop and mark the work `blocked`.
3. Confirm the candidate and manifest preserve the independent approved readiness target and architecture shape. A prototype cannot claim production readiness; a production-ready full-stack candidate must verify its real `backend/` server/API/database integration, `frontend/` API consumption, persistence, staff authorization, and documented start/environment/test commands. Empty folders and `localStorage` substitutes fail. A managed backend needs substantive configuration, functions, and API contracts; SQLite is valid only with documented operational requirements. For an approved database, inspect manifests, drivers, connection configuration, and the live API read/write path to prove it remains authoritative; writable JSON is allowed only as a labeled non-authoritative fixture or seed unless an approved architecture revision changed the decision. After a write, restart the isolated test process and read the data back through the API.
4. For a UI candidate, resolve the current approved VDC revision from the current approved `experience-spec.md`.
5. For a UI candidate, validate that every candidate visual decision reference uses the canonical combined format, points to the resolved current approved VDC revision, and matches the implementation and backlog evidence.
6. Inspect the implementation evidence you were given, then run the relevant checks.
7. For a UI candidate, independently use the real browser rather than accepting implementation-report claims. Record the run URL, browser, viewport, actions, observed outcomes, console errors, and linked artifacts. Detect a starter screen and verify entrypoint wiring before treating a new UI as application-ready.
8. Record the action or command, the expected result, the actual result, the artifact reference, and the environment for every check.
9. For any process created for verification, confirm it was coupled to an imminent bounded test and record PID, port, deadline, cleanup action, and cleanup result. All background processes (such as dev servers, daemon tasks, or test runners) MUST be terminated immediately upon completion of verification, without requiring user confirmation. A live process left running after verification is a blocking hygiene failure; always terminate all background processes before concluding.
10. Separate direct evidence from inference.
11. For a UI candidate, create a visual conformance map that links every visual acceptance criterion to the current approved contract revision, canonical combined visual decision references, expected proof, observed evidence, approved deviation if any, and result.
12. For maintainability, create a conformance map that ties each criterion to an approved reference or repository convention, the inspected scope, the verification method, the expected and actual state, direct evidence, result, evidence gap, and blocking rationale. Run configured project-native lint; if none is configured, record a production maintainability gap instead of inventing a pass.
13. Decide release eligibility only after all applicable checks are reviewed and, when applicable, both the visual conformance map and the maintainability conformance map are reviewed.

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

For a production-ready FastAPI plus React/Vite candidate, require configured backend tests and lint, plus frontend build, lint, configuration validation, and applicable frontend tests. Inspect that routers, services, schemas, and components remain modular according to the approved architecture; a single all-business `App` component or handler is a conformance failure when it violates that boundary.

Treat build output, process launch, and HTTP reachability as evidence only for their own boundaries. They do not replace real module, public-contract, API, persistence, authentication, authorization, or browser interaction tests.

### Design And Maintainability
- Responsibilities and public contracts.
- Dependency direction and cycles, including human-approved `DEP-NNN` exceptions, exact bounded edges, and current-source rationale.
- Cohesion, configured complexity, and size.
- Domain naming.
- Duplication and abstraction rationale.
- Dead code and unused dependencies.
- Comments and rationale.
- Boundary tests.
- Checks run.
- Evidence gaps.

For UI candidates, the evidence set must include real click through and, where relevant, fill/submit behavior for every interactive element, run URL, browser and viewport, action and observed state outcome, console error checks, keyboard and focus checks, contrast checks, responsive and mobile reflow checks, theme checks if the product supports them, loading, empty, error, and disabled states, and proof that no dead controls remain. Screenshots classify visual appearance only; they are supporting evidence, never interaction, state, API, or authorization evidence. For new scaffolds it also includes starter-screen detection and entrypoint wiring before any application-ready claim.

For auth and staff functions, include valid-token success plus missing token, tampered signature, missing expiry, expired token, wrong-role, cross-role, and cross-user ownership denials. Assert `401` for missing, malformed, invalid, or expired credentials and the approved `403` or scoped `404` behavior for valid identities without role or ownership. Confirm protected user resource operations (e.g. user order/booking/record reads and cancellations) and staff operational, reports, and manual settlement routes against the approved auth model. Reject default shared credentials, seeded SHA-256 passwords, token-header-selected algorithms, missing server-side subject or active-role lookup, or unaudited manual settlements. For durable or transactional data, use dedicated test data, verify persistence, and test interval conflict semantics where applicable, real date and operational timestamp validation, negative quantities, and true simultaneous conflicts through separate database connections according to the approved deployed-process model. Verify transactions preserve data integrity, order/payment/settlement audits, and financial totals, including idempotent Staff settlement. Never point tests at a project live database. `npm audit` reports dependency findings only; it is not a full application-security verdict, authorization test, or production-readiness gate.

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
- Working directory, exit code, raw-output artifact path, and tested source revision or checksum.
- For created test processes, PID, port, deadline, cleanup action, and cleanup result.
- Skip reason, if the check was not run.
- Local check results use `pass`, `fail`, `evidence-gap`, or `not-applicable`, and they do not change lifecycle status or `technical_verdict`.

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
- Starter-screen detection and entrypoint-wiring result, when the candidate began from a scaffold.

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
- The implementation commits a Monolith Page Stacking violation by appending multiple distinct user journeys into a single continuous scroll view instead of structured navigation views (tabs, dedicated routes, or drawers).
- A secondary cross-sell, optional upsell, or add-on item forms a mandatory visual or physical scroll hurdle blocking the direct checkout or completion of a primary user conversion flow.
- Privileged operational/staff surfaces (such as admin consoles, cashier desks, or management dashboards) are stacked directly beneath or mixed into public customer-facing screens instead of isolated into dedicated views, routes, or role-gated portals.
- The implementation commits an AI Design Slop or UI Sameness violation by packaging arbitrary features into uniform rounded card containers ("card soup"), defaulting to uninspired Inter/system-ui without deliberate type pairing, using unmotivated purple/cyan gradients or neon glows, or using cookie-cutter metric cards/3-card grids that contradict or ignore the bespoke Visual Direction Contract.
- A fidelity claim is unsupported by equivalent evidence.
- A required comparison is missing or its omission is unexplained.
- Required real-browser capability or evidence is missing, blocked, or replaced by a build, process, HTTP 200, screenshot, or static check.
- A scaffold used to stand in for a broader functional story is represented as item complete, slice complete, or application ready without the broader acceptance evidence. An exactly approved scaffold item may be complete on its own acceptance and test evidence, but must state `slice incomplete` and `application not ready`.

For any code-affecting candidate, including UI candidates, classify each of these verified conditions as a release-blocking Major defect:

- An approved boundary or public-contract violation is present.
- A new, forbidden, expanded, changed, unapproved, or unresolved cycle is present.
- An existing cycle lacks a matching human-approved `DEP-NNN` exception, exact bounded edges and rationale that match current source, or direct evidence that there is no expansion or new risk.
- A confirmed forbidden dependency is present.
- A configured complexity or size violation is present.
- Evidence shows mixed responsibility, weak cohesion, or risky abstraction with concrete impact.
- Evidence shows divergent duplicated business rules or speculative indirection with concrete impact.
- Evidence shows risky dead code or an unused dependency.
- Material boundary coverage is missing.
- Any required maintainability property remains unverifiable.

Strictly enforce Anti-Slop & Anti-UI Sameness standards. Generic AI design slop, template monoculture, card soup, unmotivated gradients, and cookie-cutter layouts are release-blocking defects whenever they violate the approved Visual Direction Contract or substitute lazy AI defaults for intentional, brand-specific design. An intentionally restrained or flat operational design is valid only when it demonstrates purposeful density, hierarchy, and distinct character.

## Release Eligibility

Choose one technical verdict only:

- `pass`, all applicable checks passed and no blocking defects remain.
- `conditional`, the candidate can ship only with named fixes, waivers, or follow-up checks.
- `fail`, one or more blocking defects remain, or the evidence is too weak to approve release.

Never call a result `pass` when a required check was skipped without a strong documented reason. Missing required browser UI evidence always prevents `pass`; it is not an optional-tool exception.

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
  - approved readiness target, architecture shape, and acceptance boundary
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
  - run URL, browser, viewport, actions, observed outcomes, console results, starter-screen detection, and entrypoint wiring for UI candidates
  - design and maintainability conformance map with approved references or repository conventions, inspected scope, verification method, expected and actual state, direct evidence, result, evidence gap, and blocking rationale for any code-affecting candidate, including cycle status, any human-approved `DEP-NNN` exception, exact bounded edges, current-source match, and evidence of no expansion or new risk when a cycle exists
status: awaiting-approval
approval: pending
next_skills:
  - prepare-release
~~~

The report records the technical verdict separately from handoff status. Only a human makes the approval decision; the orchestrator may record that verified decision in existing approval metadata without rewriting report content.

If the verdict is `conditional` or `fail`, replace `next_skills` with `implement-feature` after the remediation items are approved, then rerun `verify-quality` and `review-security`.

## Chat Review Protocol

Label the canonical report with its immutable `Artifact Revision`. A Review Record is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records and permit only one active request across the lifecycle. It binds request ID, canonical path, content revision, exact question, simplified options (`Yes`, `No`, and `Other` for user typing/comments), prompt evidence, and the source user reply or decision evidence.

Use native `ask_question` only when the host exposes it with its actual schema; otherwise ask: `Review artifacts/quality/<candidate-id>-quality-report.md@[revision]. Approve this exact content?` Options are `Yes` (approve), `No` (reject and pause), and `Revision` (meaningful freeform feedback). A direct Yes or No is valid only for this unchanged shown question and needs no path, revision, or host ID. Stale, duplicate, summary, unrelated, or host replies have no effect. On resume, re-read the report and show the bound pending question once.

Yes resolves the record and updates only closed governance metadata to approved. No resolves it as rejected and waits for an explicit user request to revise. Comments or feedback entered via `Other` (or user typing) without meaningful content ask only for clarifying feedback; sufficient feedback sets the report to `draft` and routes to this owner. A substantive revision supersedes the old record, creates a new Artifact Revision, invalidates affected evidence and approvals, and asks again only after the revised report returns to `awaiting-approval`. Do not intentionally create, update, or open `implementation_plan.md`, editor tabs, or `RequestFeedback` metadata. Native host presentations are not approval evidence, and host-mandated opening cannot be controlled by this plugin.

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
- run-url:
- browser-and-version:
- actions-and-observed-outcomes:
- console-errors:
- starter-screen-detection:
- entrypoint-wiring:

### Design And Maintainability
- criterion:
- approved-ref-or-repository-convention:
- scope:
- verification-method:
- expected:
- actual:
- direct-evidence:
- result:
- evidence-gap:
- blocking-rationale:

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

The conformance map is required evidence for maintainability review, and every blocked or unresolved criterion must have direct evidence or a clear evidence gap.

## Completion Criteria

Finish only when all of these are true:

- The report file exists at the required path.
- Every applicable check is recorded with action or command, expected result, actual result, artifact reference, environment, and result.
- Every skipped check has a reason.
- Every defect is classified.
- For a UI candidate, the visual conformance map covers every visual acceptance criterion and carries the current approved VDC revision resolved from the current approved `experience-spec.md`, canonical combined visual decision refs, expected proof, real-browser evidence, screenshots, and approved deviations.
- For a UI candidate, required browser evidence records the actual run URL, browser, each viewport, actions and observed outcomes, console result, and linked artifacts; new scaffold work also proves starter-screen detection and entrypoint wiring before an application-ready claim.
- For any code-affecting candidate, including UI candidates, the design and maintainability conformance map covers every required criterion with an approved reference or repository convention, inspected scope, verification method, expected and actual state, direct evidence, result, evidence gap, and blocking rationale, and it records cycle status, any human-approved `DEP-NNN` exception, exact bounded edges, current-source match, and evidence of no expansion or new risk when a cycle exists.
- The report verifies the approved readiness target and architecture shape: prototype evidence preserves stated demo limits, and full-stack release-slice evidence covers its relevant API, persistence, shared-data, and authentication/authorization boundaries.
- The report verifies every application obligation in scope is either evidenced as complete or remains explicitly pending or blocked; a slice pass or release-plan approval cannot finalize an application with unresolved required obligations.
- For a UI candidate, missing, stale, superseded, noncanonical, or mismatched visual decision refs, missing required visual evidence, or any other verified blocking visual defect results in `technical_verdict: fail`.
- For any code-affecting candidate, including UI candidates, approved boundary or public-contract violations, any new, forbidden, expanded, changed, unapproved, or unresolved cycle, an existing cycle without a matching human-approved `DEP-NNN` exception plus exact bounded edges and current-source rationale and direct evidence of no expansion or new risk, confirmed forbidden dependencies, configured complexity or size violations, evidence-backed mixed responsibility or risky abstraction, divergent duplicated business rules, risky dead code or unused dependencies, missing material boundary coverage, or any required maintainability property that remains unverifiable results in `technical_verdict: fail`.
- The release decision is explicit.
- No unsupported pass claims remain.
