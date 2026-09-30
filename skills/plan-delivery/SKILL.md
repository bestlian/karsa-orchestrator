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
- Independent approved readiness target and architecture shape, plus the acceptance boundary: prototype limitations, or production-ready backend owner, API, persistence, shared-data, staff authorization, payment, stack, and operations decisions as applicable

If any required input is missing or not approved, stop and mark the work `blocked`. For each input, verify that approval evidence names its exact current path and revision; an active editor, another URI, a prior revision, or a current phase does not transfer approval.

## Do Not Use When

- The product, UX, or architecture inputs are still unapproved.
- You need to discover scope, design the experience, define the architecture, or implement code.
- You need release execution instead of planning.

## What This Skill Produces

Create a backlog that is ready for `implement-feature` to pull one story at a time.

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/docs/...`, including expected visual proof target paths. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `docs/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

The backlog must include:

- Complete upfront story inventory: all vertical user stories covering the entire product scope across all epics and slices must be fully articulated, broken down, and formed upfront before requesting user approval.
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
- An application obligation ledger that maps every original requirement and accepted discovery proposal to one or more executable story or task IDs, release slice, scope status (`required`, `complete`, `blocked`, or specific human-approved `out-of-scope`), and the implementation, manifest, and verifier evidence required to mark it verified

### Global Planning Documentation (docs/ directory)

In addition to the backlog, KARSA MUST ensure the project contains a standard set of planning documents in the `<project-root>/docs/` directory. For any new project, invoke the three specialized planning sub-agents (`scope-mapper`, `contract-manager`, `execution-strategist`) to generate or update:
1. `docs/INDEX.md` (via `execution-strategist`)
2. `docs/02_scope_and_delivery.md` (via `scope-mapper`)
3. `docs/04_functional_requirements.md` (via `execution-strategist`)
4. `docs/05_domain_and_business_rules.md` (via `execution-strategist`)
5. `docs/06_api_contract.md` (via `execution-strategist`)
6. `docs/07_core_workflows.md` (via `scope-mapper`)
7. `docs/10_security_privacy.md` (via `contract-manager`)
8. `docs/11_quality_metrics_release.md` (via `contract-manager`)
9. `docs/13_decisions_and_questions.md` (via `contract-manager`)
10. `docs/15_execution_flow.md` (via `execution-strategist`)

These documents serve as the permanent, domain-agnostic Contract Registry and Execution Guide for the project.

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

- **All-Stories-Upfront Principle**: All epics, release slices, and vertical user stories required to deliver the entire discovered and approved product scope must be formed, broken down, and detailed upfront in `artifacts/planning/delivery-backlog.md`. Never generate a partial backlog or postpone later stories to an unspecified future backlog. The human user must be presented with the complete roadmap, story inventory, and acceptance criteria upfront so they can review and approve the entire delivery plan before any development begins.
- **Pre-Development Review Boundary**: The human user reviews and approves the complete delivery backlog in its entirety. Only after this backlog review is explicitly approved may the orchestrator request `Development Start Authorization` (`AUTH-DEV`). Development must not begin while any part of the known scope remains unplanned.
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
- Maintain a `Full-Request Obligation Ledger` in the backlog. Copy every original `FR-*` and accepted discovery proposal with its source evidence, required or optional status, mapped thin vertical stories, release slice, current evidence, and status. Required entries are unresolved until their mapped work is validated and released; a slice approval, item approval, or release-plan approval never closes another entry. Only an explicit user scope-reduction decision naming the exact obligation may set it to `scope-reduced`.
- A generic Yes to a backlog, item, slice, or partial summary never makes an omitted requirement out of scope. Only a specific human decision naming the requirement and rationale may do that. If a required obligation has no Ready item, keep it visible and plan a repair; never use a release plan to hide it.
- Do not turn an assumption into a fact, acceptance criterion, or dependency without proof.
- For a production-ready full-stack target, plan substantive backend API, database integration, shared-data, staff authorization, and client API-consumption work. Include `backend/` and `frontend/` (or `mobile/`) runnable deliverables with start, environment, and applicable test documentation; empty folders or `localStorage` substitutes fail. When there is no user sign-in, plan the explicit anonymous or service identity boundary instead of omitting it. Plan real-payment boundary work when payments are in scope. A recorded simulation approval remains approved simulation, but it prevents a live-payment-ready claim. For a prototype, record its demo limitations and no production-ready claim.
- Make production-readiness work proportional: plan only applicable concurrency/process, persistence, backup/restore, migrations, configuration/secrets, logging/operations, security, and audit recommendations. SQLite is legitimate when its documented operational requirements match the approved target. For an approved database, plan verification of its actual driver or connection, authoritative API read/write path, and isolated write/restart persistence behavior; writable JSON may only be a labeled non-authoritative fixture or seed unless an approved architecture revision changes the storage decision. Do not prescribe a framework, Kubernetes, or a vendor merely to satisfy a checklist.
- Keep release slices as separate manifests and use thin vertical stories. Do not pack all remaining requirements into a megastory. Authentication, authorization, and ownership controls must be implemented and verified before any sensitive endpoint is exposed; sensitive user resource reads/cancels and staff operational, reports, or manual settlement work cannot be Ready without their approved auth model.
- Carry the confirmed stack evidence from the brief and blueprint into affected items. For a confirmed default on new full-stack work, plan the platform-appropriate stack (e.g. FastAPI backend with React/Vite for web; FastAPI with React Native/Expo for mobile); an explicit user stack or existing project stack wins. A frontend-only prototype using React/Vite or React Native does not require FastAPI. Do not add a database choice that was not approved.

## Development Start Authorization

The approved backlog body must contain a `Development Start Authorization` record before implementation begins. It does not add a new top-level `fullstack-skill-handoff/v1` field. It is a separate request from backlog review and persists:

- the exact approved backlog revision;
- request ID, canonical backlog path, content revision, exact question, simplified options (`Yes`, `No`, and `Other` for user typing/comments), prompt evidence, and source user reply or decision evidence;
- authorized scope and first Ready story or task;
- expected runnable outcome;
- human identity, `authorized` or `rejected` decision, and exact user evidence;
- whether a material scope change has invalidated the authorization.

After the backlog is approved and no other review request is active, `fullstack-orchestrator` asks: `Start development for [approved backlog revision]? First item: [item]. Expected runnable outcome: [outcome].` Options are `Yes`, `No`, and `Other` (user typing for comments/feedback). It stops before any scaffold, install, or application edit. Yes persists authorization for only the shown approved scope without changing the backlog content revision. No persists rejected authorization, makes no application changes, and is not asked again until the user explicitly requests start or revision. Revision requires meaningful freeform feedback and routes to planning, or the owning prerequisite for scope changes, then fresh Foundation approvals as needed; it never starts coding. Backlog approval, a native Process result, or an unrelated plan cannot fill this record. Do not ask again for the same authorized revision and scope; renew it for a material scope change.

## Source And Evidence Reconciliation

Before planning, resuming, marking Ready, or routing to QA or release, re-read each source artifact at its exact path and revision. Verify explicit approval and technical result where applicable, compare them with the delivery backlog and increment manifest, and block on mismatch rather than promoting a label. Store the required source revisions or checksums of tested executable, configuration, and source scope, unresolved gates, and resume state in the existing backlog or increment manifest only. Governance metadata and review state do not invalidate evidence. A change in that tested scope invalidates dependent test evidence until rerun. Metadata normalization cannot fill an approval, technical result, or missing evidence.

At planning preflight, re-check the approved project MCP recommendations. Prefer native tools, require no MCP to run the application, and recommend only needed capability with purpose, scope, prerequisites, verification, least permissions, and restart note. For project-scoped browser evidence, merge the documented Playwright `npx` launcher into `.agents/mcp_config.json` without overwriting existing servers. Do not install or register it automatically. The optional verified command `agy mcp add --type stdio playwright npx @playwright/mcp@latest` followed by `agy mcp list` has no documented project-scope flag, so it must not be presented as project-scoped. See `define-architecture` for the exact JSON and official sources.
## Contract Registry

The backlog MUST maintain a Contract Registry section tracking all key project agreements:
- **D-Register (Decisions):** Approved product/technical decisions. Format: `D-nn | Status | Decision | Source`.
- **W-Register (Working Clarifications):** Technical details agreed upon to make decisions actionable. Format: `W-nn | Clarification | Implication`.
- **Q-Register (Open Questions):** Unanswered questions that block specific gates. Format: `Q-nn | Priority (Critical/High/Medium/Low) | Question | Blocked Gate`.
- **A-Register (Assumptions):** Unvalidated assumptions. Format: `A-nn | Assumption | Risk if wrong`.
Q-register entries with OPEN status and Critical/High priority act as hard blockers for release planning.

## Gated Execution Sequence

The backlog MUST map the implementation items against a strict 7-step gated execution sequence:
1. **Baseline & Test Sandbox**: Fresh DB/upgrade path, compatible runtime, disposable test fixtures.
2. **Domain & Relations**: Ownership, money/state invariants, race conditions.
3. **Mobile/Frontend Loop**: End-to-end manual user loop from the app UI.
4. **Identity & Alignment**: Real auth sessions, OpenAPI/client alignment.
5. **Follow-up**: Timezones, background workers, push notifications.
6. **Release Rehearsal**: Staging migration, backup/restore, rollback plan.
7. **Next Milestone**: Further enhancements (AI, monetization).
Each step has explicit "Gate Before Proceeding" conditions. Implementation items must be sequenced to prove step N before claiming step N+1.

## Snapshot Manifest Format

When tracking progress, the agent MUST maintain a "Snapshot Manifest" section consisting of a 3-column table: `Area | Code Available | Gap Preventing Completion Claim`. This replaces simple checkbox lists. Checkboxes only track code creation; the manifest tracks functional proof.

## Item Structure

Each backlog item should carry these fields:

- `id`
- `type`, one of `epic`, `story`, `task`
- `title`
- `summary`
- `purpose`
- `source_refs`, the approved requirement, UX, and architecture IDs that justify the item. For code-affecting items, include the approved module, public contract, and dependency decision IDs that govern the change
- `source_refs` must also cite the confirmed readiness target, architecture shape, and acceptance boundary when the item touches prototype limits, backend APIs, persistence, shared data, auth, authorization, payments, a confirmed stack, or deployment
- `evidence_refs`, the artifact lines, test cases, logs, mocks, or review notes that support the item
- `visual_decision_refs`, the exact approved VDC revision and VIS decision references that govern UI-affecting work
- `obligation_refs`, every original `FR-*` or accepted proposal the item advances, including required status and the ledger entry it updates
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

For a production-ready authenticated full-stack request, create thin vertical stories that establish secure User and Staff authentication before privileged endpoints: password hashing and secure bootstrap, JWT issue and fixed-algorithm server verification, active-subject role lookup, public login/registration/catalog boundary, protected User ownership paths, protected Staff role paths, and frontend Bearer/session/logout behavior. Public registration may not create Staff. Do not defer this dependency to a final slice or label a slice production-ready before it exists.

When reservations, inventory, orders, payments, or transactional resources are accepted scope, plan explicit contract and integration tests for interval conflict control, real timestamp validation, negative quantities, concurrent database operations matching the approved deployment model, and atomic order/payment/settlement/audit/financial-total behavior. Pair Staff-only idempotent manual-settlement tests with the story that exposes the action. Dedicated repeatable fixtures that are independent of test ordering are required; no test may target a live project database.

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

Every slice owns its own increment manifest. The manifest lists its required items, their approved reports, slice-only evidence, unresolved obligations, and next eligible item. It is not an application-wide workflow engine. A slice may pass its own gate only when its required items are verified, but the application obligation ledger remains authoritative for whole-application readiness.

## Delivery Gate

Every backlog item must carry a delivery gate value:

- `PASS` means the item has clear purpose, evidence refs, observable behavior, test intent, expected completion proof, and a traceable reason for its sequencing or priority. For code-affecting items, it also has approved maintainability source refs, objective maintainability acceptance criteria, named checks, and proof evidence or named gaps.
- `FAIL` means any of those are missing, vague, or only implied, including filler tasks with no measurable acceptance. A code-affecting item also fails when approved module, public contract, or dependency refs are missing, maintainability outcomes are subjective, configured limits are ignored, abstraction is speculative, or proof gaps are hidden.

For a UI-affecting item, the gate is `FAIL` when its visual contract cites an unapproved or stale VDC revision, omits a required VIS reference, contains a vague visual acceptance criterion, leaves expected visual proof unspecified, or lacks the required visual-quality task.

A `PASS` gate does not replace human approval. It only says the item is backed by evidence and is ready for the next approval step in its release slice.

`delivery_gate` is an item-level evidence check and stays separate from `handoff_status`; neither can grant human approval.

## Requirement Traceability

Every epic, story, and task must map back to approved source IDs.

The application obligation ledger is mandatory and must be auditable: each row names the original requirement or accepted proposal, source evidence, mapped item IDs, release slice, status, and current proof. `complete` requires the mapped implementation evidence plus current approved manifest and applicable verifier evidence. `out-of-scope` requires a specific human choice, not an inferred waiver.

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
- For an authenticated production-ready target, the User/Staff endpoint matrix, password and secret boundary, JWT verification rules, frontend Bearer/session threat model, ownership and role denials, and negative token tests are explicit before any protected story is Ready
- For sensitive endpoints, the approved auth model, role/ownership policy, denial tests, and password/bootstrap policy are explicit before the endpoint is Ready
- A confirmed full-stack backlog contains testable backend API, persistent-data, and authentication/authorization-boundary work before dependent user-facing work is considered Ready
- For a production-ready full-stack target, the backlog also contains testable `backend/` server/database and `frontend/` API-consumption work, its run/environment/test documentation, and applicable readiness-gate evidence before dependent user-facing work is Ready
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
output_path: docs/08_delivery_backlog.md
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
  - confirmed readiness target, architecture shape, and acceptance boundary propagated from the brief and blueprint
  - confirmed stack decision and evidence propagated from the brief and blueprint
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

## Chat Review Protocol

Label the body with an immutable `Artifact Revision`. A Review Record is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records and permit only one active request across the lifecycle. It binds request ID, canonical path, content revision, exact question, simplified options (`Yes`, `No`, and `Other` for user typing/comments), prompt evidence, and the source user reply or decision evidence.

Use native `ask_question` only when the host exposes it with its actual schema; otherwise ask: `Review docs/08_delivery_backlog.md@[revision]. Approve this exact content?` Options are `Yes` (approve), `No` (reject and pause), and `Revision` (meaningful freeform feedback). A direct Yes or No is valid only for this unchanged shown question and requires no path, revision, or host ID. Stale, duplicate, summary, unrelated, or host replies have no effect. On resume, re-read the backlog and show the bound pending question once.

Yes resolves the record and updates only closed governance metadata to approved. No resolves it as rejected and waits for an explicit user request to revise. Comments or feedback entered via `Other` (or user typing) without meaningful content ask only for clarifying feedback; sufficient feedback sets the backlog to `draft` and routes to this owner. A substantive revision supersedes the old record, creates a new Artifact Revision, invalidates affected approvals and start authorization, and asks again only after the revised backlog returns to `awaiting-approval`. Closed review and authorization metadata cannot change scope, first item, expected outcome, acceptance, or technical result. Do not intentionally create, update, or open `implementation_plan.md`, editor tabs, or `RequestFeedback` metadata. Native host presentations are not approval evidence, and host-mandated opening cannot be controlled by this plugin.

## Completion Criteria

This skill is complete when all of these are true:

- `docs/08_delivery_backlog.md` exists
- All approved product requirements are traced into the backlog
- The application obligation ledger maps every original requirement and accepted proposal to executable items and release slices, with no inferred waivers
- All in-scope UX and architecture decisions are reflected
- All code-affecting items carry maintainability traceability from approved architecture decisions to acceptance criteria, checks, and proof or named gaps
- Every UI-affecting item preserves the exact approved VDC revision and required VIS references through visual acceptance criteria and expected visual proof artifact target paths
- Epics, stories, and tasks are structured cleanly
- Dependencies, priorities, release slices, and risks are filled in
- Acceptance criteria, DoR, and DoD are present
- Security and quality tasks are included where needed
- Visual-quality tasks are included for every rendered UI change
- The backlog records the approved readiness target, architecture shape, prototype limits or full-stack boundaries, and a pending or valid Development Start Authorization record for its exact revision and scope
- The handoff status is `awaiting-approval`.
- No item is marked ready without approval
- The delivery gate is `PASS` for each ready item, backed by evidence refs and observable behavior; UI-affecting ready items also have approved, current visual refs, measurable VIS-mapped criteria, and specified proof; code-affecting ready items also have maintainability source refs, objective acceptance criteria, named checks, and proof or named gaps

Do not mark the work `approved`. Human review is the last step.
