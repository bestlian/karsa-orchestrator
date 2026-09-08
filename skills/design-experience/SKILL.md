---
name: design-experience
description: Use when an approved product brief must become an approval-ready experience specification.
---

# Design Experience

Turn an approved product brief into a clear experience specification that can be reviewed, approved, and handed to planning.

## Use When

- The product brief is approved and the next step is experience definition.
- You need journeys, information architecture, screen inventory, and state coverage.
- You need a traceable spec that links requirements to the proposed experience.
- You need a lightweight prototype outline, not production UI.

## Do Not Use When

- The product brief is still open, drafted, or disputed.
- You need backend architecture, data modeling, or infrastructure choices.
- You need a frontend framework decision or production UI implementation.
- You need deployment, release orchestration, or self-approval.

## Prerequisite

Start only after an approved product brief exists. Verify that the approval evidence names the exact current brief path and revision; an active editor, another URI, a prior revision, or a current phase does not transfer it. If the brief is not approved, stop and return that gap instead of inventing experience decisions.

The brief should provide, at minimum:

- problem statement and intended outcome;
- target users and primary job;
- scope boundaries and exclusions;
- approved readiness target and architecture shape, including prototype limits or production-ready auth, persistence, staff authorization, and payment boundaries;
- requirement IDs or a clear source of truth for them;
- known constraints, risks, and dependencies.

## Working Rules

1. Read the approved product brief before writing the spec.
2. Keep the experience aligned to the brief, not to personal taste.
3. Do not choose backend architecture or production implementation details.
4. Trace each meaningful experience decision to requirement IDs.
5. Include happy, loading, empty, error, permission, and destructive states.
6. Keep the prototype lightweight enough to validate the experience only.
7. Do not mark the work approved. Human approval is required.
8. Do not allow UI planning to proceed until the Visual Direction Contract has an explicit approval from its named human approval owner.
9. Preserve the independent approved readiness target and architecture shape. A prototype experience must state its demo limits and cannot be presented as production-ready behavior; a full-stack experience must expose the UX implications of backend, shared data, staff authorization, and real-payment decisions without choosing their implementation. A restrained visual direction never selects a technology stack.

## Curated UX Filter

Use this compact filter while shaping the experience spec.

- Sort every notable choice into evidence, unknown, filler, or validation.
- Evidence stays only when it is tied to the approved brief, research, content, analytics, constraints, or approved assets.
- Unknowns stay explicit. If a choice is not known, mark it as an open question instead of inventing it.
- Filler gets removed. Skip generic layout, decorative treatments, claims, or copy that does not help the task.
- Validation needs a check. If a choice needs proof, say how the prototype or review will test it.
- Pass the UX purpose test. If a screen element does not help task completion, wayfinding, trust, or feedback, leave it out.
- Write one sentence that states the design direction before detailing the rest.
- Give reasons for major design decisions.
- Build the composition from content and task flow, not from a clone-like template.
- Show observable feedback and state changes for hover, focus, selection, loading, success, empty, error, disabled, and destructive states.
- Use real identity assets when approved. If they are not available, call out honest placeholders.
- On small screens, reflow content instead of shrinking everything.
- Keep contrast, keyboard access, visible focus, and reduced motion checks explicit.
- Use restrained motion only when it clarifies feedback or transition.
- Evaluate card soup, excessive pills, arbitrary gradients, oversized operational heroes, generic icon grids, unjustified glass, template-first composition, and decorative motion as conditional anti-template risks, not universal bans.
- Accept or reject each notable visual choice according to product purpose, content, user tasks, and operating context; record the product-specific reason either way.
- Treat restrained operational design as valid and potentially distinctive when deliberate density, hierarchy, typography, navigation, or wayfinding gives it a clear product-specific character.

Attribution note: this filter is curated from anti-slop v3.2.4 commit 44be68777e96d53d113edad33dbc4ab380f5d054 under MIT. See `THIRD_PARTY_NOTICES.md`.

## Output

Write the experience specification to `artifacts/ux/experience-spec.md`.

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`, including visual proof target paths. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

The spec should be concise, reviewable, and ready for approval.

## Required Spec Content

### 1. Summary

- product name or initiative name;
- approved brief reference;
- scope in one short paragraph;
- out of scope items;
- confirmed readiness target and architecture shape, including prototype demo limitations or the full-stack behaviors that the experience must cover;
- experience status.

### 2. Visual Direction Contract

Define one complete, product-specific Visual Direction Contract inside the experience spec before UI planning begins. The contract owns visual direction for the artifact and must be internally consistent with the approved brief, journeys, states, responsive behavior, and accessibility guidance.

Use these canonical fields:

- `visual_contract_revision`: a unique, immutable revision ID in `VDC-NNN` format, where `NNN` is a three-digit decimal number;
- `visual_approval_owner`: the named human owner responsible for explicit visual approval;
- `direction_mode`: `restrained` or `expressive`, selected according to product purpose rather than aesthetic preference;
- `product_specific_rationale`: why this direction fits the product, users, tasks, content, and operating context;
- `provenance`: the evidence, research, approved assets, constraints, and comparison references that informed the direction, including source and allowed use;
- `validation_widths`: product-approved validation widths in CSS pixels, or the fallback widths 375, 768, and 1280 CSS px when the product defines none;
- `visual_decisions`: an ordered set of decisions, each with a unique `VIS-NNN` ID within the revision, where `NNN` is a three-digit decimal number.

Each entry in `visual_decisions` must include:

- `id`;
- `typography`;
- `color`;
- `spacing_and_density`;
- `layout_grammar`;
- `material_and_surface_language`;
- `component_anatomy`;
- `imagery_and_iconography`;
- `motion`;
- `responsive_intent`;
- `accessibility`;
- `states`;
- `signature_moment`;
- `rejected_defaults`, with a product-specific reason for every rejection.

Make every visual decision concrete enough for planning and validation. The `signature_moment` identifies the product-specific visual or interaction expression that makes the experience recognizable; it may be quiet and operational in a restrained direction. A restrained contract can be distinctive through deliberate density, hierarchy, typography, navigation, or wayfinding and does not need gradients, glass, animation, or an expressive aesthetic.

Use `none` or `not-applicable` only when the relevant field includes a product-specific rationale. Do not use either value to avoid a decision, state, responsive case, or accessibility obligation.

Treat references only as provenance and comparison inputs. They never grant permission to clone a product, imitate a named brand, copy protected assets, or reuse material without an appropriate license or approval.

Validate the contract, its visual decisions, signature moment, relevant states, responsive intent, and accessibility at every product-approved validation width. If no widths have been approved, validate at 375, 768, and 1280 CSS px. Record what was checked, the result, and any unresolved inconsistency.

Downstream work must cite a visual decision with the canonical reference `experience-spec@VDC-NNN#VIS-NNN`, where each `NNN` is a three-digit decimal number. For example: `experience-spec@VDC-001#VIS-001`. Plain ASCII characters are required. A revision-only reference does not substitute for a decision reference.

An initial or revised contract stays at `draft` until it is complete and internally consistent, then moves to `awaiting-approval`. If any approved Visual Direction Contract decision changes, create a new `VDC-NNN` revision, return the artifact to `draft`, complete consistency and validation checks, and then return it to `awaiting-approval` for explicit human approval. All downstream references to the superseded revision are stale and block UI planning or implementation until the new revision is approved and the references are updated.

### 3. Journeys

Describe the core user journeys in order of importance.

For each journey include:

- journey ID;
- actor;
- trigger;
- goal;
- preconditions;
- main steps;
- alternate paths;
- failure and recovery paths;
- completion signal;
- linked requirement IDs.

### 4. Information Architecture

Define:

- major views and subviews;
- navigation model;
- entry points and return paths;
- content grouping;
- terminology and labels;
- role-based differences, if any;
- deep links or cross-links that matter to the journey.

### 5. Screen Inventory

List every screen or view needed to cover the approved brief.

For each screen include:

- screen ID and name;
- purpose;
- linked journeys;
- linked requirement IDs;
- key content blocks;
- primary action;
- secondary actions;
- notes on reuse or variation.

### 6. State Coverage

For every important screen or flow, define:

- happy state;
- loading state;
- empty state;
- error state;
- permission state;
- destructive or high-impact confirmation state.

State notes should say what the user sees, what the user can do next, and how the experience recovers.

### 7. Responsive Behavior

State how the experience changes across supported sizes.

Include:

- minimum supported viewport;
- what stays visible first;
- what collapses or reflows;
- how tables, dense content, and side panels behave;
- how touch and pointer use differ where relevant;
- how long content and zoom affect layout.

### 8. Content Rules

Set rules for the content that appears in the experience.

Cover:

- tone and voice;
- title length and label style;
- empty-state copy;
- error-message style;
- permission copy;
- destructive-action copy;
- formatting for names, numbers, dates, and counts;
- handling for long, missing, or partial content.

### 9. Accessibility

Write accessibility guidance with a WCAG mindset.

Include:

- target standard, usually WCAG 2.2 AA if that is the project baseline;
- semantic structure and reading order;
- keyboard support for every critical action;
- focus order and focus return;
- visible focus treatment;
- non-color status cues;
- announcements for dynamic updates;
- reduced-motion behavior;
- touch target and spacing expectations;
- any known screen reader concerns.

Do not claim compliance unless the project has agreed verification evidence.

### 10. Prototype Or Full-Stack Experience Expectations

Describe the appropriate review surface for the confirmed readiness target and architecture shape.

For a confirmed prototype, keep it to:

- the minimum screens needed to review the journeys;
- realistic sample content;
- simple state switching or scenario notes;
- no production API calls;
- no production auth logic;
- no framework choice;
- no deployment plan.

State the prototype's demo limitations and that it is not production full-stack delivery. For a confirmed full-stack application, define the journeys and states that depend on backend API results, persistent or shared data, authentication and authorization, and real payment outcomes when they are in scope. This remains an experience contract, not an implementation or vendor choice.

### 11. Traceability

Map each journey and screen back to requirement IDs.

Use the requirement IDs exactly as they appear in the approved brief or source backlog.

Every important requirement should have at least one linked journey or screen.

## Handoff

```yaml
schema: fullstack-skill-handoff/v1
producing_skill: design-experience
artifact_id: experience-spec
output_path: artifacts/ux/experience-spec.md
inputs:
  - approved product brief
  - requirement IDs from the brief
  - supporting evidence and constraints
requirement_refs:
  - approved product requirement IDs
decision_refs:
  - approved product brief
  - confirmed readiness target, architecture shape, and acceptance boundary from the product brief
  - approved Visual Direction Contract revision in VDC-NNN format
  - "exact approved visual decision references in experience-spec@VDC-NNN#VIS-NNN format"
  - named human visual approval decision for the current VDC-NNN revision
assumptions:
  - any interaction assumptions that remain visible in the spec
open_questions:
  - unresolved UX decisions that can still change the spec
risks:
  - usability, accessibility, or scope risks
validation_evidence:
  - journeys
  - screen inventory
  - state coverage
  - prototype notes
  - visual provenance, including sources, approved assets, constraints, allowed use, and comparison inputs
  - validation widths in CSS pixels and results at each width
  - visual state validation results
  - signature moment validation results
  - responsive intent validation results
  - accessibility evidence for the visual decisions
status: awaiting-approval
approval: pending
next_skills:
  - plan-delivery
```

The handoff stays experience-level. It does not add backend architecture, production implementation detail, or deployment steps, but it preserves the approved readiness target, architecture shape, and acceptance boundary for planning.

## Review And Approval Protocol

Label the canonical specification with its immutable `Artifact Revision`. A `Review Record` is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records. The canonical specification may have at most one pending record, and only while its handoff status is `awaiting-approval`; it identifies the canonical path, artifact revision, request identity, and supported presentation reference or `none`. Use normal filesystem reads and writes without intentionally opening or focusing an IDE editor. Do not retry the known unsupported `write_to_file` plus `ArtifactMetadata` project-artifact route (`invalid path ... must be inside brain`) or invent feedback metadata. A supported presentation is view-only and cannot become another authority.

Accept `Proceed` only when the host proves binding to the pending canonical path and revision; otherwise require exact chat `approve`, `reject`, or `revise`. Any terminal decision resolves the pending record and records the human decision plus an internal source-message reference; users do not need to provide host event IDs. Metadata normalization cannot self-approve. After any terminal decision, close only a supported review tab without discarding unsaved changes; otherwise report that auto-close is unavailable. Reopen or update a supported presentation once only for the next approval. A substantive revision before a terminal decision supersedes the pending record, resets approval, and creates a new pending record only when the specification returns to `awaiting-approval`.

## Completion Criteria

The task is complete when all of these are true:

- the product brief is approved and cited;
- the confirmed readiness target, architecture shape, and acceptance boundary are cited, with prototype demo limitations or full-stack state coverage reflected in the experience;
- the Visual Direction Contract has a unique `VDC-NNN` revision, a named human approval owner, a direction mode, product-specific rationale, provenance, validation widths, and complete unique `VIS-NNN` decisions;
- every visual decision defines all required visual-system fields, states, a signature moment, and rejected defaults with product-specific reasons;
- visual validation covers the product-approved widths, or 375, 768, and 1280 CSS px when none exist;
- journeys are defined with triggers, steps, recovery, and completion;
- information architecture and screen inventory are complete;
- state coverage includes happy, loading, empty, error, permission, and destructive cases;
- responsive behavior, content rules, and accessibility guidance are written;
- traceability covers the relevant requirement IDs;
- the handoff `decision_refs` includes the approved VDC revision, exact canonical VIS references, and named human visual approval decision;
- the handoff `validation_evidence` includes provenance, validation widths, states, signature moment, responsive intent, and accessibility evidence;
- the output exists at `artifacts/ux/experience-spec.md`;
- the work is not self-approved.

The artifact cannot be approval-ready while the Visual Direction Contract is missing, incomplete, internally inconsistent, unvalidated, stale, or awaiting updates to downstream references.

## Quality Checks

- Does the spec stay inside the approved brief?
- Can planning use it without guessing the experience?
- Is the Visual Direction Contract complete, product-specific, internally consistent, and tied to one current `VDC-NNN` revision?
- Does every `VIS-NNN` decision contain all required fields, provenance-informed rationale, relevant states, a signature moment, and reasoned rejected defaults?
- Was visual behavior validated at every product-approved width, or at 375, 768, and 1280 CSS px when none exist?
- Are all downstream visual references current and written as `experience-spec@VDC-NNN#VIS-NNN`, with each `NNN` replaced by a three-digit decimal number?
- Does the handoff carry the approved VDC revision, exact canonical VIS references, and named visual approval decision under `decision_refs`?
- Does the handoff carry provenance, validation widths, states, signature moment, responsive intent, and accessibility evidence under `validation_evidence`?
- Has the named human visual approval owner explicitly approved the current VDC revision before UI planning proceeds?
- Are any missing requirements called out as open questions or blockers?
- Does every important screen support the stated journeys?
- Is the approval boundary clear?

If the answer to any of these is no, or if the Visual Direction Contract is incomplete or inconsistent, keep the status at `draft`, `awaiting-approval`, or `blocked` rather than `approved`.
