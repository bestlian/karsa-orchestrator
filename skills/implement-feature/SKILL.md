---
name: implement-feature
description: Use when implementing exactly one ready backlog item end to end with evidence based TDD.
---

# Antigravity Skill: Implement Feature

Use this skill for one ready backlog item only. It turns approved specs into a small, testable slice with clear evidence and keeps the release-slice increment manifest in sync.

## Use When

- One backlog item is already ready.
- Approved specs, acceptance criteria, and repository conventions are available.

## Do Not Use When

- You still need discovery, design, architecture, or planning.
- The backlog item is not ready or the specs are not approved.
- You need release planning or deployment work instead of implementation.

## Required Inputs

1. One backlog item in `Ready` state.
2. The approved release-slice definition from the delivery backlog.
3. The current increment manifest at `artifacts/implementation/<release-slice-id>-increment-manifest.md`, if one already exists.
4. Approved specs, meaning the blueprint, acceptance criteria, and any linked decisions are signed off.
5. Repository conventions, configured quality tools, approved module responsibilities, public contracts, dependency decisions, relevant manifests, relevant code, and existing tests.
6. For UI-affecting work, the exact approved visual contract reference in canonical form `experience-spec@VDC-NNN#VIS-NNN`, where `NNN` is the exact three-digit approved ID, for example `experience-spec@VDC-001#VIS-001`, including the current approved `VDC-*` revision, every referenced `VIS-*` decision, `visual_acceptance_criteria`, and `expected_visual_proof`.
7. Foundation: the approved product brief, experience specification, application blueprint, and delivery backlog at their referenced revisions.
8. A `Development Start Authorization` in the approved backlog body that names that exact backlog revision, authorized scope, first Ready story or task, expected runnable outcome, human identity, and exact user evidence.
9. The approved readiness target and architecture shape: prototype limitations, or production-ready backend, API, persistence, shared-data, staff authorization, and frontend API-consumption boundaries for the selected item.

If any of those are missing, stop and ask for the missing input. Do not guess.

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`, including implementation reports, increment manifests, and evidence paths. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

## Development Start Gate

Before a scaffold, dependency or package installation, generated starter-app output, or application edit, verify Foundation and the recorded development-start authorization. Each Foundation approval must name its exact current artifact path and revision; an active editor, another URI, a prior revision, or a current phase does not transfer it. A Vite or other scaffold is not Foundation. Backlog approval alone is not authorization, and neither a native Process result nor an unrelated plan may be used to infer it.

If authorization is missing, create the separate bound question: `Start development for [approved backlog revision]? First item: [item]. Expected runnable outcome: [outcome].` Options are `Yes`, `No`, and `Revision`. Then stop before development. Persist the response in the backlog body's `Development Start Authorization` record for that revision and scope. Yes authorizes only this already approved scope without a content revision bump. No persists rejected authorization, makes no application changes, and is not asked again until the user explicitly asks to start or revise. Revision requires meaningful freeform feedback and routes to planning, or an owning prerequisite when scope changes, followed by fresh Foundation approvals as needed; it never starts coding. Do not ask again for the same authorized scope. A material scope or backlog-revision change requires renewed authorization. An epic is never an implementation unit; select one Ready story or task only.

## First Check

Read the repository conventions, configured quality tools, approved module responsibilities, public contracts, dependency decisions, relevant manifests, nearby implementation files, and current tests before editing. Then read the selected backlog item, its approved release-slice definition, and its approved specs. Re-read every referenced source report at its exact path and revision, verify approval and technical result, and compare them with the increment manifest; mismatch blocks work. Record a stable revision or checksum of the tested executable, configuration, and source scope in the existing manifest; governance documents and review state do not invalidate evidence. For an approved database, inspect its actual driver or connection configuration and authoritative API read/write path before editing; a writable JSON store is architecture drift unless an approved architecture revision authorizes it. Read the current increment manifest when it exists; for the first item in a slice, initialize it as `draft` from the approved release-slice definition. Do not trust a compaction summary or metadata normalization as evidence.

For UI-affecting work, resolve the exact `VDC-*` revision and every referenced `VIS-*` ID before editing. Confirm that the visual contract is current and approved, that its IDs match the backlog item, and that its rejected defaults, `visual_acceptance_criteria`, and `expected_visual_proof` are explicit. A stale or unapproved revision, a missing or mismatched reference, or incomplete visual acceptance or proof requirements blocks implementation. Do not infer a newer visual direction from nearby code or replace the approved contract with personal preference.

If the item is not ready, or the specs are not approved, do not start.

## Work Flow

1. Select one item and restate its ID, scope, acceptance criteria, and expected outcome. For UI-affecting work, also restate the exact approved `VDC-*` revision, referenced `VIS-*` IDs, `visual_acceptance_criteria`, and `expected_visual_proof`.
2. Map the item to the smallest set of files that need to change, including the approved prototype limitation or full-stack boundary it advances.
3. Build a simple impact map for module boundaries, public contracts, dependency edges, affected manifests, boundary tests, and checks so you know what behavior, tests, checks, and, where applicable, approved visual decisions and visual acceptance criteria are affected.
4. Write the failing test first. For UI-affecting work, write a failing visual or behavioral check first when automation exists. When automation does not exist, interact with the pre-change UI in a real browser and record the contract mismatch as red evidence before implementation.
5. Make the smallest code change that passes the test.
6. Refactor only after the behavior is green.
7. Keep repeating red, green, refactor until the item is complete.
8. Update the increment manifest with the item report, slice state, current approval state, source revision or checksum, tests tied to that source, and unresolved resume gates. If the tested executable, configuration, or source scope changes, invalidate dependent evidence before routing.
9. If required slice items remain, keep the next skill as `implement-feature`.
10. Only when every required item report is complete and explicitly approved may the manifest move to `awaiting-approval`, then human approval, then `verify-quality` and `review-security`.

## Implementation Rules

1. Keep the change narrow. Implement one item, one vertical slice, one clear outcome.
2. Use the approved architecture. If the approved design and the codebase conflict in a material way, stop and report architecture drift.
3. Validate inputs at the boundary. Preserve domain rules inside the feature.
4. Favor direct code over new abstractions unless the abstraction is required by the approved spec, real repeated behavior or policy in the touched slice, or a proven variation point. State the rationale for any abstraction.
5. Keep touched modules within approved responsibilities and public surfaces. Preserve dependency direction and do not introduce circular dependencies.
6. Keep functions and components cohesive. Split only when mixed responsibilities, excessive branching or fan-out, hidden side effects, repeated decisions, weak test seams, or navigation or change risk make the code harder to maintain.
7. Remove touched dead code, unused imports, unused exports, stale configuration, and unused dependencies unless an approved constraint prevents removal.
8. Use tests that match the changed boundary, including unit, public/module-contract, integration, or acceptance tests as needed.
9. Do not weaken, delete, or bypass tests to make the change pass.
10. Do not suppress type errors.
11. Do not expose secrets or sensitive data in code, logs, fixtures, or reports.
12. Do not perform irreversible migrations or deployments.
13. Do not self approve the work.
14. Do not use `done` or `partial` as an artifact status. Use the shared status vocabulary for artifacts, and use `technical_verdict` for the implementation outcome.
15. For UI-affecting work, implement the approved visual contract faithfully across typography, color, density, layout grammar, surfaces, component anatomy, imagery and iconography, motion, responsive intent, interaction states, accessibility, and any referenced signature moment.
16. Do not substitute generic defaults or any defaults that the visual contract explicitly rejects. Every intentional deviation requires an approved decision reference before implementation and must be reported.
17. Judge visual quality by fidelity to the approved contract, not by subjective expressiveness. An intentionally restrained or flat design passes when that is what the contract specifies; do not add gradients, glass, or animation unless the contract specifies them. Directional-reference approval and VDC approval never authorize named-brand imitation or copying protected expression. Protected assets may be used only when ownership, a license, or rights-holder authorization is independently recorded in the approved contract provenance. Missing rights evidence blocks implementation and must not be treated as an intentional visual deviation.
18. For a production-ready full-stack target, create real `backend/` and `frontend/` work, not placeholders: a runnable server API with database integration and a runnable client consuming it. Honor the confirmed stack, including FastAPI backend with React and Vite frontend only when that default offer was confirmed; preserve an explicit or existing stack unless migration was requested. Keep each area's start, environment, and applicable test commands documented. Managed backends need substantive configuration, functions, and API contracts. SQLite is valid with documented file, backup, migration, locking/concurrency, and operating requirements. Do not substitute writable JSON for an approved database; JSON fixtures and seeds are allowed only when explicitly non-authoritative.

## Anti Slop Rules

These rules are curated from anti slop v3.2.4, commit `44be68777e96d53d113edad33dbc4ab380f5d054`, under MIT. See `THIRD_PARTY_NOTICES.md` for attribution.

1. Keep claims tight. Use a shared filter for evidence, unknowns, filler, and validation so reports and handoffs stay grounded in observable facts.
2. If you mention behavior, show evidence for it. If something is unknown, say `unknown`. If a sentence adds no useful fact, cut it.
3. UI work must have a real trigger, a real handler, and a real result. If the control can fail, load, or disable, show those states. Do not leave dead controls or fake interactivity in place.
4. UI work must keep keyboard use, accessibility, and state changes intact. If a feature is unfinished, mark it visibly as unfinished, not as complete.
5. Do not use source patch scripts or CSS patch scripts as a substitute for maintainable code.
6. Keep comments only when they explain a non obvious why, a constraint, or a risk. Remove decorative banners and redundant narration only in touched code.

## Testing Rules

Use focused tests that match the behavior you changed.

1. Unit tests for deterministic rules and edge cases.
2. Integration tests for framework, database, or provider boundaries.
3. Acceptance tests for the user facing path when the item needs that level.

Test both happy path and meaningful failure path when the acceptance criteria call for it. Keep the tests close to the behavior, not the implementation details.

A real boundary test exercises the approved module, public contract, API, persistence, authentication, authorization, or provider boundary and observes its expected and failure behavior. A build, a process launch, or an HTTP 200 is not a substitute for that boundary test.

## Verification Rules

Run the checks that fit the change.

1. Diagnostics for changed files, plus configured cycle, complexity, size, duplication, dead-code, and unused-dependency checks when available.
2. Build or type check when the repo has one.
3. Focused unit, integration, and acceptance tests for the touched slice.
4. Manual QA through the real surface when the change is user visible.
5. For UI-affecting work, interact with the implementation in a real browser at the product-approved widths. If the visual contract specifies none, use `375`, `768`, and `1280` CSS px. Click and fill actual controls, use relevant keyboard paths, observe persisted and error state outcomes, and record console results. Exercise every relevant specified state, including applicable default, hover, focus, active, disabled, loading, empty, error, and success states, and compare the result with the approved references and acceptance criteria.
6. For authorization, test staff actions with expected `401` or `403`, cross-role and ownership denials, and relevant negative business cases. Test durable storage and concurrency-sensitive booking flows against dedicated test data and the approved deployed-process model, never a project live database.
7. A host-native `browser_subagent` may collect bounded browser interaction evidence only. The executing agent retains lifecycle ownership and must make all edits, approvals, routing, and joins.

Screenshots may support visual evidence but do not replace browser interaction evidence. Use deterministic synthetic fixtures for visual verification. Evidence must contain no credentials, personal data, or production secrets. A build success, a running process, or an HTTP 200 only proves its own boundary and cannot substitute for browser UI evidence.

Do not mark the work complete unless the checks actually ran, or the repo has no matching surface and that limitation is stated plainly. For UI-affecting work, a missing browser surface or missing required fidelity evidence prevents a complete technical verdict.

If an optional static check is unavailable, inspect the changed code directly and record the evidence gap instead of fabricating a pass or requiring a new tool. This does not waive required UI browser evidence.

## Browser Capability And Recovery

Use a native browser capability first. A browser skill being listed or installed does not prove its runtime, browser binary, or driver is available. For required UI evidence:

1. Confirm the native browser capability can actually launch and exercise the project-bound application.
2. If it is missing, use only a documented, supported install or configuration path that stays within the existing permission and project boundary. Do not disable safety controls or invent undocumented commands.
3. If a built-in driver download fails, record the exact reason and failure output. Try one supported alternative when one is available; do not blindly repeat the same failed download.
4. Stop and ask a human before an external download, global installation, elevated permission, account change, or other action outside the project boundary.
5. If no permitted, working browser capability remains, record the required evidence as blocked. Do not waive it because a static tool is optional, and do not claim `technical_verdict: complete`.

For a newly scaffolded UI, first detect and record the starter screen, then prove entrypoint wiring to the intended application before any application-ready claim. Treat this as an explicit transition from starter to product surface, not as evidence that the application itself is ready.

## Evidence Report

Write the implementation report to `artifacts/implementation/<item-id>-implementation-report.md`.
Also update `artifacts/implementation/<release-slice-id>-increment-manifest.md` for the same slice.

Include these sections:

```markdown
## Outcome
## Changed Files
## Design And Maintainability
## Visual Fidelity
## Verification Results
## Acceptance Evidence
## Handoff
## Technical Verdict
```

Under `## Design And Maintainability`, include these exact labels:

```markdown
architecture-and-convention-refs:
module-responsibilities-and-public-contracts:
dependency-direction-and-cycle-evidence:
cohesion-complexity-and-size-evidence:
domain-naming-evidence:
duplication-and-abstraction-evidence:
dead-code-and-unused-dependency-evidence:
comments-and-rationale:
boundary-test-evidence:
checks-run:
evidence-gaps:
```

Keep each field objective, brief, and tied to the touched slice.

The report must name the item ID, the changed files, the checks run, the acceptance evidence, and any approved assumptions. For UI-affecting work, `## Visual Fidelity` must contain these canonical fields:

```yaml
visual_contract_ref:
visual_decision_refs:
implemented_decisions:
rejected_defaults_checked:
run_url:
browser_and_version:
viewports_checked:
states_exercised:
actions_and_observed_outcomes:
console_errors:
browser_evidence:
screenshot_evidence:
starter_screen_detection:
entrypoint_wiring:
reference_comparison:
intentional_deviations:
```

Use `none` only when a field genuinely has no applicable evidence, and explain why. `browser_evidence` must describe observed interaction results, not only screenshot paths. `run_url`, browser, viewport, actions, observed outcomes, console result, and linked evidence paths are required for UI work. `starter_screen_detection` and `entrypoint_wiring` are required before a newly scaffolded UI can claim application readiness. `reference_comparison` must state how the implementation matches the approved visual acceptance criteria and identify any verified drift.

## Handoff

```yaml
schema: fullstack-skill-handoff/v1
producing_skill: implement-feature
artifact_id: implementation-report
output_path: artifacts/implementation/<item-id>-implementation-report.md
inputs:
  - ready backlog item
  - approved release-slice definition
  - current increment manifest, or none for the first item
  - approved specs
  - repository conventions
requirement_refs:
  - backlog item IDs
  - approved blueprint or acceptance criteria IDs
decision_refs:
  - implementation choices that stay inside the approved specs
  - exact approved VDC and VIS references when UI affecting
assumptions:
  - approved assumptions used in the implementation
open_questions:
  - unresolved implementation questions that still need a decision
risks:
  - regressions, drift, or rollout risks in the touched slice
validation_evidence:
  - failing test first
  - passing focused tests
  - diagnostics
  - build or type check results
  - maintainability evidence for module boundaries, dependency direction, cohesion, naming, duplication, dead code, and unused dependencies
  - manual QA evidence when user visible
  - visual fidelity browser, viewport, state, and reference comparison evidence when UI affecting
  - run URL, actions, observed outcomes, console results, starter-screen detection, and entrypoint wiring when applicable
  - increment manifest update
status: awaiting-approval
approval: pending
next_skills:
  - implement-feature
```

Record the technical verdict in the report body. The handoff status stays on the artifact lifecycle and only moves to `approved` after explicit human approval. While required slice items remain, emit only `implement-feature` in `next_skills`. After every required item report and the increment manifest are explicitly approved, replace that route and emit only `verify-quality` and `review-security` in `next_skills`.

## Chat Review Protocol

Label each canonical report or existing increment manifest with its immutable `Artifact Revision`. A Review Record is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records and permit only one active request across the lifecycle. It binds request ID, canonical path, content revision, exact question, `Yes`/`No`/`Revision` options, prompt evidence, and the source user reply or decision evidence.

Use native `ask_question` only when the host exposes it with its actual schema; otherwise ask `Review [canonical path]@[revision]. Approve this exact content?` with `Yes` (approve), `No` (reject and pause), and `Revision` (meaningful freeform feedback). A direct Yes or No is valid only for the unchanged shown question and requires no path, revision, or host ID. Stale, duplicate, summary, unrelated, or host replies have no effect. On resume, re-read the canonical artifact and show its bound pending question once.

Review the item report and increment manifest separately and sequentially: do not create a manifest request until the report request resolves, and never let a Yes for one approve the other. Yes resolves the current record and updates only closed governance metadata to approved. No resolves it as rejected and waits for an explicit user request to revise. Revision without meaningful feedback asks only for that feedback; sufficient feedback sets the current artifact to `draft` and routes to this owner. A substantive revision supersedes the old record, creates a new Artifact Revision, invalidates affected approvals and evidence, and asks again only after the revised artifact returns to `awaiting-approval`. Closed metadata cannot change acceptance, technical result, scope, first item, or outcome. Do not intentionally create, update, or open `implementation_plan.md`, editor tabs, or `RequestFeedback` metadata. Native host presentations are not approval evidence, and host-mandated opening cannot be controlled by this plugin.

## Technical Verdict

Record one value in the report body:

- `technical_verdict: complete`
- `technical_verdict: partial`
- `technical_verdict: blocked`

Use `technical_verdict` for the implementation outcome only. Do not turn it into an artifact status. `technical_verdict: complete` can survive missing optional tooling only when direct evidence establishes the required properties. Otherwise, use `technical_verdict: partial` or `technical_verdict: blocked`.

State the result at the correct boundary: `item complete`, `slice complete`, `slice incomplete`, `application ready`, or `application not ready`. Completing one item never completes its slice or the application. An exactly approved scaffold story or task may be `technical_verdict: complete` when its own concrete acceptance criteria and required tests pass, but it must say `slice incomplete` and `application not ready`. A scaffold used to stand in for a broader functional story is `technical_verdict: partial`.

## Completion Criteria

Treat the item as complete only when all of these are true:

1. The selected item is still the only item implemented.
2. The code matches the approved specs and repository conventions.
3. Boundary validation is in place.
4. The red, green, refactor loop was followed.
5. The required tests pass.
6. Diagnostics and build checks pass, or the missing check is explicitly noted.
7. Manual QA was performed when the feature has a user facing surface.
8. The implementation report exists at the required path.
9. No architecture drift, secret leak, or destructive change remains unresolved.
10. The complete `## Design And Maintainability` evidence set is present for the touched slice, and no unresolved module-boundary or public-contract violation, forbidden dependency direction, circular dependency, material cohesion or complexity or size risk, unjustified duplication or abstraction, risky dead code or unused dependency, domain-naming readability risk, or missing material boundary test remains.
11. For UI-affecting work, the implementation matches the current approved `VDC-*` revision and referenced `VIS-*` decisions, including all applicable visual acceptance criteria, responsive states, accessibility requirements, and any referenced signature moment.
12. For UI-affecting work, the required real-browser fidelity evidence is complete at every approved or fallback viewport and relevant state, with rejected defaults checked and every intentional deviation tied to an approved decision reference.
13. For UI-affecting work, browser evidence names the actual run URL, browser, viewport, actions, observed outcomes, console errors, and linked artifacts; newly scaffolded work also records starter-screen detection and entrypoint wiring before any application-ready claim.

If any of those fail, report `technical_verdict: partial` or `technical_verdict: blocked` instead of `technical_verdict: complete`. Missing required browser or fidelity evidence, a missing referenced signature moment, or verified unapproved visual drift can never receive `technical_verdict: complete`. Build success and HTTP 200 results do not change that outcome.
