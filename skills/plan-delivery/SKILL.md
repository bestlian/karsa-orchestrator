---
name: plan-delivery
description: Use when approved product, UX, and architecture artifacts need to be turned into a traceable implementation backlog for the next build step.
---

# Plan Delivery

Convert approved product, UX, and architecture artifacts into one delivery backlog file at `artifacts/planning/delivery-backlog.md`.

Attribution: this skill is informed by anti-slop v3.2.4, commit `44be68777e96d53d113edad33dbc4ab380f5d054`, under MIT. See `THIRD_PARTY_NOTICES.md`.

## When To Use

Use this skill only after these inputs are approved by a human:

- Product artifact, with goals, scope, constraints, and requirement IDs
- UX artifact, with flows, states, and interaction rules
- Architecture artifact, with system boundaries, data flow, and technical decisions
- A confirmed delivery shape and acceptance boundary: prototype demo limitations, or full-stack backend owner, API, persistence, shared-data, auth, authorization, payment, stack, and deployment decisions as applicable

If any required input is missing or not approved, stop and mark the work `blocked`. For each input, verify that approval evidence names its exact current path and revision; an active editor, another URI, a prior revision, or a current phase does not transfer approval.

## Do Not Use When

- The product, UX, or architecture inputs are still unapproved.
- You need to discover scope, design the experience, define the architecture, or implement code.
- You need release execution instead of planning.

## What This Skill Produces

Create a backlog that is ready for `implement-feature` to pull one story at a time.

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`, including expected visual proof target paths. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

The backlog must include:

- Epics
- Vertical stories that deliver user value end to end
- Technical tasks that support a story, not replace it
- Dependencies between items
- Priority for each item
- Release slices that group work into buildable batches
- Requirement traceability back to source artifact IDs
- Propagation of approved Visual Direction Contract and VIS decisions into measurable visual acceptance and expected proof for every UI-affecting item
- Acceptance criteria for every story and task
- Definition of Ready and Definition of Done for every item
- Security tasks and quality tasks where they are needed
- Risks and blockers that can stop the work
- A delivery-shape trace from the approved brief and blueprint into every affected item's Ready criteria and verification

## Shared Evidence, Unknown, Filler, And Validation Filter

Reject any item draft that does not carry all of these:

- Purpose
- Evidence refs
- Observable behavior
- Test intent
- Validation
- Actual proof expected at completion
- Reason for any major sequencing or priority decision
- Marked unknowns and assumptions that stay visible as assumptions

Also reject filler language that hides missing scope or proof, including vague tasks like `polish`, `improve`, or `make modern`, unless the item also states measurable acceptance.

## Backlog Rules

- Start with epics, then break each epic into vertical stories.
- Keep stories thin enough to build and verify in one focused pass.
- Add technical tasks only when they support a story, shared platform work, or a clear dependency.
- Keep architecture changes in the architecture artifact, not hidden inside delivery tasks.
- Do not mark a story ready unless all required prerequisites are approved and the Definition of Ready is met.
- Epics group stories and tasks only. They are never implementation units.
- `Ready` means planning prerequisites are met; it does not authorize scaffolding, dependency installation, or application edits. Development requires the separately persisted start authorization below.
- Do not self-approve anything.
- Do not add deployment work unless it is part of the approved scope.
- Do not rewrite scope, invent new goals, or widen the release plan.
- Keep discovery assumptions marked as assumptions until they are confirmed by approved source material or delivery evidence.
- Do not turn an assumption into a fact, acceptance criterion, or dependency without proof.
- For confirmed full-stack delivery, plan backend API, persistence, shared-data, and authentication/authorization boundary work. When there is no user sign-in, plan the explicit anonymous or service identity boundary instead of omitting it. Plan real-payment boundary work when payments are in scope. Do not substitute local-only storage or simulated payment unless that exact limitation was approved. For a prototype, record that it is not production full-stack delivery and keep its demo limitations in acceptance and verification.

## Development Start Authorization

The approved backlog body must contain a `Development Start Authorization` record before implementation begins. It does not add a new top-level `fullstack-skill-handoff/v1` field. Use the record to persist:

- the exact approved backlog revision;
- authorized scope and first Ready story or task;
- expected runnable outcome;
- human identity, explicit `authorized` or `not authorized` decision, and exact user evidence;
- whether a material scope change has invalidated the authorization.

When there is no valid record, `fullstack-orchestrator` asks: `Shall I start development against [approved backlog revision]? First item: [item]. Expected runnable outcome: [outcome].` and stops before any scaffold, install, or application edit. A single exact user response may approve this pending backlog revision and authorize its already specified scope, first item, and outcome; record the lifecycle approval and the start decision separately. Backlog approval alone, bare `approved`, a native Process result, or an unrelated plan cannot fill this record. Do not ask again for the same authorized revision and scope; renew it for a material scope change.

## Item Structure

Each backlog item should carry these fields:

- `id`
- `type`, one of `epic`, `story`, `task`
- `title`
- `summary`
- `purpose`
- `source_refs`, the approved requirement, UX, and architecture IDs that justify the item. For code-affecting items, include the approved module, public contract, and dependency decision IDs that govern the change
- `source_refs` must also cite the confirmed delivery shape and acceptance boundary when the item touches prototype limits, backend APIs, persistence, shared data, auth, authorization, payments, a confirmed stack, or deployment
- `evidence_refs`, the artifact lines, test cases, logs, mocks, or review notes that support the item
- `visual_decision_refs`, the exact approved VDC revision and VIS decision references that govern UI-affecting work
- `visual_acceptance_criteria`, the measurable visual outcomes mapped to those VIS decisions
- `expected_visual_proof`, the artifact types and target paths that will prove those outcomes
- `parent_id`, when the item belongs under another item
- `dependencies`, the items that must land first
- `priority`, use `high`, `medium`, or `low`
- `release_slice`, the planned delivery batch
- `acceptance_criteria`, measurable outcomes, including maintainability outcomes for code-affecting items
- `observable_behavior`
- `test_intent`, the behavior or boundary the checks must cover, including public-contract, module-boundary, or integration intent for code-affecting items
- `expected_completion_proof`, the reports, check output, dependency evidence, and explicit evidence gaps that will prove completion
- `sequencing_rationale`
- `assumptions`
- `unknowns`
- `delivery_gate`, one of `PASS` or `FAIL`
- `definition_of_ready`
- `definition_of_done`
- `security_tasks`
- `quality_tasks`, repository-native checks or direct inspection steps
- `risks`
- `blockers`
- `handoff_status`

## Planning Rules

### Epics

Use epics to group a meaningful user or platform outcome. Each epic should have a short purpose, a scope boundary, evidence refs, and a traceability summary.

### Vertical Stories

Write stories as user-visible slices of value. A story should be testable without waiting for unrelated stories in the same epic.

Each story must say:

- What user need it serves
- What behavior changes
- What must already exist before it starts
- How it will be accepted
- What proof should exist when it is complete

### Visual Decision Propagation

For every UI-affecting epic, story, or task, translate approved visual decisions from the Visual Direction Contract in `experience-spec.md` into the item contract. Planning propagates those decisions; it must not choose art direction, add product scope, or require expressive styling when the approved direction is operational.

Use canonical references in the form `experience-spec@VDC-NNN#VIS-NNN`, where `NNN` is the exact three-digit approved ID; for example, `experience-spec@VDC-001#VIS-001`. Preserve the exact approved VDC revision and VIS decision ID. Do not use an unapproved revision, a stale revision superseded by the approved source, an alias, or an implied reference.

For each UI-affecting item:

- Populate `visual_decision_refs` with every approved VIS decision that governs the item.
- Write each entry in `visual_acceptance_criteria` so it identifies a relevant viewport, state, content condition, or component, states a measurable outcome, and maps to a referenced VIS decision.
- Write each entry in `expected_visual_proof` so it names an artifact type, its target path, and the VIS decision it proves. Wording such as `looks correct`, `polished`, or `matches the design` is not proof.
- Add a visual-quality task under `quality_tasks` whenever the item creates or changes rendered UI. State the checks and evidence needed without prescribing a specific browser or design tool.
- Keep the VDC/VIS reference, visual criterion, and expected proof linked without inventing behavior beyond approved product, UX, architecture, or visual scope.

Treat the three visual fields as lists. They may be empty only for a genuinely non-UI item, and the item must state the reason in `summary`. Indirect support for rendered UI is UI-affecting when the task can change the rendered result.

### Maintainability Decision Propagation

For every code-affecting epic, story, or task:

- Populate `source_refs` with the approved architecture decisions that cover module responsibility, public contracts, dependency direction, and any repo-configured complexity or size limits that apply
- Write `acceptance_criteria` as measurable maintainability outcomes, such as correct module ownership, stable public contracts, no new dependency cycles, cohesion that matches the approved boundary, domain names that match approved vocabulary, removal of real duplication or dead code when proven, and comments only where non-obvious rationale is needed
- Use `test_intent` to name the boundary or contract being checked, such as module boundary, public contract, dependency graph, integration path, or regression path
- Use `quality_tasks` for repository-native checks or direct inspection, such as lint, tests, dependency checks, search for duplicate logic, dead code review, unused dependency checks, and verification against repo-configured limits
- Write `expected_completion_proof` as the concrete report, command output, review note, or dependency evidence that proves the change met the maintainability criteria, plus any gaps when a tool or direct check was not available
- Allow abstraction only when repeated behavior or policy has been verified, or when a variation point is proven. Reject speculative indirection
- If the repository config defines size or complexity limits, use those exact limits. If it does not, require evidence-backed refactoring and do not invent a universal line count

For non-code items, if maintainability proof does not apply, state that reason clearly in `summary` and keep the other evidence honest.

### Technical Tasks

Use tasks for shared services, data shape changes, migrations, component support, or test harness work that a story depends on.

Technical tasks must:

- Link to the story or epic they support
- Explain why the task exists
- State the visible effect, even if indirect
- State the test intent and the proof expected at completion
- Avoid hiding product or architecture decisions

For code-affecting technical tasks, the acceptance criteria, test intent, quality tasks, and expected completion proof must form one maintainability chain from approved architecture decisions to observable checks and evidence.

### Dependencies

List dependencies explicitly and keep them real.

- Do not imply parallel work can start if it cannot.
- Do not mark later items ready when earlier prerequisites are still open.
- If a dependency is blocked, the dependent item stays blocked too.

### Priorities

Use simple delivery priorities:

- `high` for work that blocks the main flow, a launch slice, or a critical risk
- `medium` for important work that can follow the main path
- `low` for follow-up work that is useful but not release blocking

Priority and sequencing decisions must name the proof pressure they answer, such as blocked dependency, user-visible risk, test setup, or release slice shape.

### Release Slices

Group items into release slices that a team can build and verify as a unit.

- Put the smallest viable user outcome in the first slice.
- Keep slice names plain and direct.
- Do not spread one user outcome across too many slices without a clear reason.

Release slices stay intact even when delivery gates change, and a gate never rewrites slice order by itself.

The release slice is the unit whose approved item reports later join `verify-quality` and `review-security`. Completion of an item never claims the slice or application is complete. An exactly approved scaffold item may state `item complete` after its own acceptance proof, but it must state `slice incomplete` and `application not ready`; a scaffold standing in for a broader functional story is partial.

## Delivery Gate

Every backlog item must carry a delivery gate value:

- `PASS` means the item has clear purpose, evidence refs, observable behavior, test intent, expected completion proof, and a traceable reason for its sequencing or priority. For code-affecting items, it also has approved maintainability source refs, objective maintainability acceptance criteria, named checks, and proof evidence or named gaps.
- `FAIL` means any of those are missing, vague, or only implied, including filler tasks with no measurable acceptance. A code-affecting item also fails when approved module, public contract, or dependency refs are missing, maintainability outcomes are subjective, configured limits are ignored, abstraction is speculative, or proof gaps are hidden.

For a UI-affecting item, the gate is `FAIL` when its visual contract cites an unapproved or stale VDC revision, omits a required VIS reference, contains a vague visual acceptance criterion, leaves expected visual proof unspecified, or lacks the required visual-quality task.

A `PASS` gate does not replace human approval. It only says the item is backed by evidence and is ready for the next approval step in its release slice.

`delivery_gate` is an item-level evidence check and stays separate from `handoff_status`; neither can grant human approval.

## Requirement Traceability

Every epic, story, and task must map back to approved source IDs.

Use traceability to show:

- Which product requirement started the item
- Which UX flow or state it supports
- Which architecture decision it depends on, including module, public contract, and dependency decisions for code-affecting items
- Which repo-configured complexity or size limit applies, or which evidence-backed refactor path applies when no limit is configured
- Which exact approved VDC revision and VIS decisions govern any UI-affecting result
- Which visual acceptance criteria translate each referenced VIS decision
- Which expected visual proof artifact and target path will verify each criterion
- Which maintainability checks, direct inspection steps, and evidence gaps prove the code change stayed within the approved architecture decision
- Which release slice contains it
- Which evidence proves the item is still grounded in approved intent

If an approved source artifact changes, update the traceability before any story is marked ready. A changed VDC revision makes prior visual references stale until each affected item points to the exact approved revision and its criteria and proof mappings are revalidated.

## Definition Of Ready

An item is ready only when all of these are true:

- The source requirement is approved
- The UX behavior is approved, if the item touches the user flow
- The architecture needed for the item is approved
- The approved product brief, UX specification, architecture blueprint, and delivery backlog together form Foundation; a scaffold does not satisfy Foundation
- For code-affecting work, the approved architecture refs include the relevant module, public contract, and dependency decisions, and the verification method is testable
- Dependencies are listed and available or scheduled
- Acceptance criteria are clear and testable
- Purpose, evidence refs, observable behavior, test intent, and expected completion proof are present
- For code-affecting work, maintainability outcomes are objective, the checks are named, and the completion proof can show any evidence gaps
- For UI-affecting work, the exact VDC revision and all required VIS decisions are approved, current, and present in `visual_decision_refs`
- For UI-affecting work, every visual acceptance criterion is measurable, names a relevant viewport, state, content condition, or component, and maps to a referenced VIS decision
- For UI-affecting work, expected visual proof names an artifact type and target path, and a visual-quality task is included for rendered UI changes
- For genuinely non-UI work, empty visual fields have an explicit reason in `summary`
- For non-code work, any maintainability evidence that is not applicable is explained in `summary`
- For confirmed full-stack work, affected API, persistence, shared-data, auth, authorization, payment, backend-owner, and boundary-test acceptance is explicit; for a prototype, its approved demo limitation is explicit
- A confirmed full-stack backlog contains testable backend API, persistent-data, and authentication/authorization-boundary work before dependent user-facing work is considered Ready
- Risks and blockers are noted
- Security and quality work is included where needed

If any of these are missing, the item stays not ready. A UI-affecting item also stays not ready when its visual contract is unapproved, revision-stale, missing a required VIS reference, vague, or unsupported by specified proof.

## Definition Of Done

An item is done only when all of these are true:

- The backlog entry is specific and testable
- The traceability links are complete
- Acceptance criteria are written in plain language
- The delivery gate is `PASS` and the proof is attached or referenced
- For code-affecting work, maintainability evidence is attached or referenced, no material criterion is unresolved, and any direct-inspection limitation is called out in the proof
- UI-affecting work preserves the exact approved VDC revision and VIS references, satisfies the mapped visual acceptance criteria, and attaches or references the expected visual proof at its stated target paths
- The visual-quality task is complete for every rendered UI change
- UI-affecting proof requires real-browser capability and names the expected run URL, viewport, actions, observed outcomes, console results, screenshot or report artifact paths, and, for a new scaffold, starter-screen detection and entrypoint wiring. A build or HTTP 200 is not the UI proof.
- The dependency chain is honest
- The item is placed in the right release slice
- Security and quality tasks are present where needed
- No hidden architecture work is buried inside the item

## Security And Quality Tasks

Add explicit security and quality tasks when the item touches any of these areas:

- Authentication or session handling
- Authorization or permissions
- Input handling or persistence
- Network boundaries or third party data
- Migration, rollout, or rollback risk
- Core user flows that need verification
- Code paths where module boundaries, public contracts, dependency direction, cohesion, duplication, dead code, or complexity limits can change

These tasks should cover the needed checks, tests, or reviews without turning the backlog into implementation code.

## Risks And Blockers

Call out any risk that could change scope, timing, or sequencing.

Use `blockers` for missing approvals, unresolved architecture decisions, required source changes, or missing maintainability evidence that blocks a code-affecting item from being objective.

Use `risks` for things that are known but not yet blocking, such as complex integration, data migration sensitivity, or tight release timing.

Keep unknowns visible in the item until they are resolved. If an unknown is still open, it belongs in `unknowns` and may also belong in `blockers` or `risks`, but it must not be rewritten as settled scope.

## Handoff

```yaml
schema: fullstack-skill-handoff/v1
producing_skill: plan-delivery
artifact_id: delivery-backlog
output_path: artifacts/planning/delivery-backlog.md
inputs:
  - approved product artifact
  - approved UX artifact
  - approved architecture artifact
requirement_refs:
  - approved product requirement IDs
  - approved UX journey and screen IDs
  - approved architecture decision IDs
decision_refs:
  - backlog prioritization and release slicing decisions
  - exact approved VDC revision and VIS decision references propagated into UI-affecting items
  - confirmed delivery shape and acceptance boundary propagated from the brief and blueprint
assumptions:
  - any planning assumptions that remain visible in the backlog
open_questions:
  - unresolved sequencing or dependency questions
risks:
  - delivery, dependency, or release risks
validation_evidence:
  - epics
  - stories
  - tasks
  - dependency map
  - DoR and DoD coverage
  - delivery gate PASS and FAIL examples
  - maintainability source refs, objective acceptance criteria, checks, proof, and named gaps for code-affecting items
  - VIS-mapped visual acceptance criteria and expected visual proof artifact target paths
  - development-start authorization record for the approved backlog revision and scope
status: awaiting-approval
approval: pending
next_skills:
  - implement-feature
```

## Approval Evidence Protocol

Before requesting review, label the document body with an immutable `Artifact Revision`; its combination with `artifacts/planning/delivery-backlog.md` is the approval target. Bind a review request to that exact pending path and revision. If the host supports `RequestFeedback` metadata, apply `RequestFeedback: true` only to that exact artifact and revision; it is host-specific metadata, not a universal API, and must never be placed on a proxy such as `implementation_plan.md`. A path-only host event fails closed unless it demonstrably binds the pending content revision; then request the exact chat fallback.

Ingest a valid current user decision before routing, then use an already recorded valid decision if present. It must name the pending path and revision; a category or artifact-tree decision, a different URI, active editor, phase, or old revision never transfers approval. `approve` sets existing `status` and `approval` to `approved`; `reject` sets them to `rejected`; `revise` sets `status` to `draft` and `approval` to `revise` awaiting owner revision. Append the path, revision, human identity, decision, and exact evidence to existing `decision_refs` and/or the body `Approval Record`.

These lifecycle status, approval, appended approval `decision_refs`, and Approval Record changes are closed governance metadata: they retain the Artifact Revision and valid approval. Development Start Authorization decision/evidence is also closed metadata only when it fills this already specified backlog revision and scope. None of these updates may change scope, first item, expected outcome, acceptance, or other substantive content. Any substantive content change creates a new revision, resets approval, and re-evaluates/rebinds start authorization. A revise or remediation request never grants downstream permission.

## Completion Criteria

This skill is complete when all of these are true:

- `artifacts/planning/delivery-backlog.md` exists
- All approved product requirements are traced into the backlog
- All in-scope UX and architecture decisions are reflected
- All code-affecting items carry maintainability traceability from approved architecture decisions to acceptance criteria, checks, and proof or named gaps
- Every UI-affecting item preserves the exact approved VDC revision and required VIS references through visual acceptance criteria and expected visual proof artifact target paths
- Epics, stories, and tasks are structured cleanly
- Dependencies, priorities, release slices, and risks are filled in
- Acceptance criteria, DoR, and DoD are present
- Security and quality tasks are included where needed
- Visual-quality tasks are included for every rendered UI change
- The backlog records the approved delivery shape, its prototype limits or full-stack boundaries, and a pending or valid Development Start Authorization record for its exact revision and scope
- The handoff status is `awaiting-approval`.
- No item is marked ready without approval
- The delivery gate is `PASS` for each ready item, backed by evidence refs and observable behavior; UI-affecting ready items also have approved, current visual refs, measurable VIS-mapped criteria, and specified proof; code-affecting ready items also have maintainability source refs, objective acceptance criteria, named checks, and proof or named gaps

Do not mark the work `approved`. Human review is the last step.
