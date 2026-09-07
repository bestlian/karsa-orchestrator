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

If any of those are missing, stop and ask for the missing input. Do not guess.

## First Check

Read the repository conventions, configured quality tools, approved module responsibilities, public contracts, dependency decisions, relevant manifests, nearby implementation files, and current tests before editing. Then read the selected backlog item, its approved release-slice definition, and its approved specs. Read the current increment manifest when it exists; for the first item in a slice, initialize it as `draft` from the approved release-slice definition.

For UI-affecting work, resolve the exact `VDC-*` revision and every referenced `VIS-*` ID before editing. Confirm that the visual contract is current and approved, that its IDs match the backlog item, and that its rejected defaults, `visual_acceptance_criteria`, and `expected_visual_proof` are explicit. A stale or unapproved revision, a missing or mismatched reference, or incomplete visual acceptance or proof requirements blocks implementation. Do not infer a newer visual direction from nearby code or replace the approved contract with personal preference.

If the item is not ready, or the specs are not approved, do not start.

## Work Flow

1. Select one item and restate its ID, scope, acceptance criteria, and expected outcome. For UI-affecting work, also restate the exact approved `VDC-*` revision, referenced `VIS-*` IDs, `visual_acceptance_criteria`, and `expected_visual_proof`.
2. Map the item to the smallest set of files that need to change.
3. Build a simple impact map for module boundaries, public contracts, dependency edges, affected manifests, boundary tests, and checks so you know what behavior, tests, checks, and, where applicable, approved visual decisions and visual acceptance criteria are affected.
4. Write the failing test first. For UI-affecting work, write a failing visual or behavioral check first when automation exists. When automation does not exist, interact with the pre-change UI in a real browser and record the contract mismatch as red evidence before implementation.
5. Make the smallest code change that passes the test.
6. Refactor only after the behavior is green.
7. Keep repeating red, green, refactor until the item is complete.
8. Update the increment manifest with the item report, the slice state, and the current approval state.
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

## Verification Rules

Run the checks that fit the change.

1. Diagnostics for changed files, plus configured cycle, complexity, size, duplication, dead-code, and unused-dependency checks when available.
2. Build or type check when the repo has one.
3. Focused unit, integration, and acceptance tests for the touched slice.
4. Manual QA through the real surface when the change is user visible.
5. For UI-affecting work, interact with the implementation in a real browser at the product-approved widths. If the visual contract specifies none, use `375`, `768`, and `1280` CSS px. Exercise every relevant specified state, including applicable default, hover, focus, active, disabled, loading, empty, error, and success states, and compare the result with the approved references and acceptance criteria.

Screenshots may support visual evidence but do not replace browser interaction evidence. Use deterministic synthetic fixtures for visual verification. Evidence must contain no credentials, personal data, or production secrets.

Do not mark the work complete unless the checks actually ran, or the repo has no matching surface and that limitation is stated plainly. For UI-affecting work, a missing browser surface or missing required fidelity evidence prevents a complete technical verdict.

If a configured check is unavailable, inspect the changed code directly and record the evidence gap instead of fabricating a pass or requiring a new tool.

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
viewports_checked:
states_exercised:
browser_evidence:
screenshot_evidence:
reference_comparison:
intentional_deviations:
```

Use `none` only when a field genuinely has no applicable evidence, and explain why. `browser_evidence` must describe observed interaction results, not only screenshot paths. `reference_comparison` must state how the implementation matches the approved visual acceptance criteria and identify any verified drift.

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
  - increment manifest update
status: awaiting-approval
approval: pending
next_skills:
  - implement-feature
```

Record the technical verdict in the report body. The handoff status stays on the artifact lifecycle and only moves to `approved` after explicit human approval. While required slice items remain, emit only `implement-feature` in `next_skills`. After every required item report and the increment manifest are explicitly approved, replace that route and emit only `verify-quality` and `review-security` in `next_skills`.

## Technical Verdict

Record one value in the report body:

- `technical_verdict: complete`
- `technical_verdict: partial`
- `technical_verdict: blocked`

Use `technical_verdict` for the implementation outcome only. Do not turn it into an artifact status. `technical_verdict: complete` can survive missing optional tooling only when direct evidence establishes the required properties. Otherwise, use `technical_verdict: partial` or `technical_verdict: blocked`.

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

If any of those fail, report `technical_verdict: partial` or `technical_verdict: blocked` instead of `technical_verdict: complete`. Missing required fidelity evidence, a missing referenced signature moment, or verified unapproved visual drift can never receive `technical_verdict: complete`.
