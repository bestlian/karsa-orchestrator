---
name: discover-product
description: Use when a greenfield full-stack idea needs evidence-first discovery and an approval-ready product brief before design or architecture work.
---

# Discover Product

Turn an early full-stack idea into a clear product brief that a decision maker can approve before any design or architecture work starts.

## Use When

Use this skill when the request is about a new product, a greenfield feature set, or a rough idea that still needs product discovery.

Typical triggers:

- new app idea, MVP idea, or startup concept;
- blank-slate full-stack product discovery;
- founder note, meeting note, or rough prompt that needs a product brief;
- unclear users, jobs, scope, or success measures;
- need for an approval-ready brief before design or architecture.

Non-triggers:

- writing UX flows, wireframes, or visual design;
- choosing architecture, frameworks, data stores, or infrastructure;
- creating backlog items, delivery plans, or engineering estimates;
- writing code, tests, or deployment steps;
- self-approval or external sign-off actions.

## Inputs

Start with whatever evidence exists, then ask only for what is still missing. Do not repeat an explicit user answer.

Required inputs when available:

- a one-line idea statement;
- the business problem or opportunity;
- known target users or buyer;
- any existing notes, docs, screenshots, or transcripts;
- constraints, deadlines, budget limits, or compliance concerns;
- the person who can approve the brief.

Ask early, in the first focused discovery round when the answer is not already explicit:

- Is the requested delivery a frontend prototype/mock or a full-stack application with backend API and persistent data?
- Will data be single-user/local or multi-user/shared, and what persistence is required?
- Are authentication, authorization, and payments simulated or real? For real payments, which provider and operational boundary are approved?
- Does the user require a stack, backend capability (including a managed backend/BaaS that meets the real backend need), or deployment preference?

For shared booking data, recommend full-stack delivery as the default recommendation, but require explicit scope confirmation before selecting it. Never silently choose `localStorage`, simulated payments, or a backend substitute. Respect a technically specified stack; otherwise keep the architecture framework-neutral.

## Evidence-First Workflow

1. Read every available artifact before asking questions.
2. Separate facts, assumptions, and open questions.
3. Ask 2 to 4 focused questions at a time, only about gaps that can change the brief. Ask the delivery-shape questions early unless their answers are already explicit.
4. Prefer evidence over memory, opinions, or guesses.
5. Restate what is confirmed after each round.
6. Keep the brief product-level only, no solution design.
7. Stop when the brief is approval-ready or when a material blocker remains.

## Anti-Slop Filter

Shared rules:

- Every factual claim, completion claim, and approval claim must point to evidence or be marked as an assumption.
- Unknown, untested, conflicting, and placeholder states must be labeled plainly.
- Cut any filler that does not change a requirement, decision, behavior, validation, or deliverable.
- Keep supporting proof in `validation_evidence`, not buried in narrative.

Discovery-specific rules:

- Every user, metric, testimonial, constraint, and research claim needs a source or evidence ID.
- Do not invent users, numbers, quotes, testimonials, constraints, findings, or research results.
- If evidence is missing, use `[REAL DATA NEEDED]` and say exactly what is missing.
- Cite evidence IDs beside the claim, such as `EV-001` or `EV-002`.

Evidence sources to check first:

- product notes, founder notes, meeting transcripts, and research summaries;
- prior briefs or proposals;
- customer feedback, support notes, and sales notes;
- any uploaded screenshots or examples;
- explicit user statements from the current conversation.

## What To Produce

Create one product brief at `artifacts/discovery/product-brief.md`.

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

The brief must be plain, concrete, and short enough to review quickly. It should include only the information needed to decide whether the idea is worth building.

## Brief Content

### 1. Product Summary

Include:

- the product idea in one paragraph;
- the problem it solves;
- the intended outcome;
- the decision maker or approval owner;
- the evidence used to shape the brief.

### 2. Users, Jobs, Outcomes

Document:

- primary users;
- secondary users, if any;
- their jobs to be done;
- the outcomes they want;
- what success looks like for each user group.

Use short, practical language. Do not invent personas with cosmetic detail.

### 3. Scope And Non-Goals

State:

- what is in scope for the first approval-worthy brief;
- what is explicitly out of scope;
- what should stay manual for now;
- what is deferred to later discovery.

### 4. Delivery Shape And Acceptance Boundary

Record the confirmed delivery shape before product requirements:

- `prototype` or `full-stack`;
- the explicit evidence for that choice and the human who confirmed it;
- the acceptance boundary: what demonstrates the prototype, item, slice, and application, respectively;
- for a prototype, its demo limitations and an explicit statement that it is not production full-stack delivery;
- for confirmed full-stack delivery, the backend owner, API and integration boundaries, persistence expectation, shared-data model, and real or simulated auth and payment decisions;
- a confirmed stack, managed-backend/BaaS capability, and deployment preference when the user supplied one, otherwise a visible open question rather than an invented choice.

This is scope confirmation, not an architecture implementation. Do not select a database, provider, framework, or deployment service without confirmed evidence.

### 5. Functional Requirements

List product requirements with stable IDs.

Use `FR-001`, `FR-002`, and so on.

Each requirement must be atomic, testable, and written from the user or business point of view.

Minimum fields for each `FR-*` item:

- ID;
- requirement statement;
- priority, `Must`, `Should`, `Could`, or `Won't`;
- source or evidence;
- acceptance signal.

Do not turn these into architecture decisions, API specs, or implementation tasks.

### 6. Nonfunctional Requirements

List measurable quality requirements with stable IDs.

Use `NFR-001`, `NFR-002`, and so on.

Cover only product-relevant constraints such as:

- response time expectations, if known;
- availability expectations;
- accessibility expectations;
- privacy or data handling expectations;
- localization or device support;
- supportability or maintainability needs that affect the product brief.

Each `NFR-*` item must state a measurable target or a clearly bounded assumption.

### 7. Success Metrics

Define the few metrics that prove the idea is working.

Use `SM-001`, `SM-002`, and so on.

Each metric should state:

- what is measured;
- how it is measured;
- what good looks like;
- when it should be reviewed.

### 8. Risks And Assumptions

Track risks and assumptions separately.

Use `RSK-001` and `ASM-001`.

For each item, include:

- the statement;
- why it matters;
- what would change if it is false;
- who should confirm it.

### 9. Open Questions

Capture unresolved questions with stable IDs.

Use `OQ-001`, `OQ-002`, and so on.

Only include questions that can still change the brief in a material way.

## Handoff

```yaml
schema: fullstack-skill-handoff/v1
producing_skill: discover-product
artifact_id: product-brief
output_path: artifacts/discovery/product-brief.md
inputs:
  - idea statement
  - product notes
  - interviews, transcripts, screenshots, or other evidence
requirement_refs: []
decision_refs:
  - product approval decision
  - confirmed delivery shape and acceptance boundary
  - confirmed backend owner, API, persistence, auth, payment, stack, and deployment decisions when applicable
assumptions:
  - evidence-backed assumptions that stay visible in the brief
open_questions:
  - unresolved product questions that can still change the brief
risks:
  - product, market, scope, or compliance risks
validation_evidence:
  - source notes
  - customer feedback
  - transcripts
  - screenshots
status: awaiting-approval
approval: pending
next_skills:
  - design-experience
  - define-architecture
```

The handoff stays product-level. It records the confirmed delivery shape and acceptance boundary without adding architecture, backlog, or implementation detail.

Attribution: adapted from anti-slop v3.2.4, commit `44be687`, MIT. See `THIRD_PARTY_NOTICES.md`.

## Approval Evidence Protocol

Before requesting review, label the document body with an immutable `Artifact Revision`; its combination with `artifacts/discovery/product-brief.md` is the approval target. Bind a review request to that exact pending path and revision. If the host supports `RequestFeedback` metadata, apply `RequestFeedback: true` only to that exact artifact and revision; it is host-specific metadata, not a universal API, and must never be placed on a proxy such as `implementation_plan.md`. A path-only host event fails closed unless it demonstrably binds the pending content revision; then request the exact chat fallback.

Ingest a valid current user decision before routing, then use an already recorded valid decision if present. It must name the pending path and revision; a category or artifact-tree decision, a different URI, active editor, phase, or old revision never transfers approval. `approve` sets existing `status` and `approval` to `approved`; `reject` sets them to `rejected`; `revise` sets `status` to `draft` and `approval` to `revise` awaiting owner revision. Append the path, revision, human identity, decision, and exact evidence to existing `decision_refs` and/or the body `Approval Record`.

These lifecycle status, approval, appended approval `decision_refs`, and Approval Record changes are closed governance metadata: they retain the Artifact Revision and valid approval. They cannot change scope, first item, expected outcome, acceptance, or other substantive content. Any substantive content change creates a new revision and resets approval. A revise or remediation request never grants downstream permission.

## Approval Gate

The brief is approval-ready only when all of the following are true:

- the problem statement is clear and supported by evidence;
- the primary users and their jobs are named;
- scope and non-goals are explicit;
- every `FR-*` item has a priority and acceptance signal;
- every `NFR-*` item is measurable or clearly bounded as an assumption;
- success metrics are defined;
- risks, assumptions, and open questions are visible;
- the approval owner is known;
- the delivery shape and acceptance boundary are confirmed, including visible limitations for a prototype or backend/persistence/auth/payment boundaries for full-stack work;
- no unresolved question can materially change the product brief.

If any of these are false, mark the output `blocked` or `draft`, and explain why.

Do not self-approve.

## Completion Criteria

Consider the skill complete when:

- `artifacts/discovery/product-brief.md` exists and reflects the evidence gathered;
- the brief contains product summary, users, jobs, outcomes, scope, non-goals, `FR-*`, `NFR-*`, success metrics, risks, assumptions, and open questions;
- the brief records the confirmed prototype or full-stack delivery shape, acceptance boundary, and applicable backend, persistence, auth, payment, stack, deployment, and demo-limit decisions;
- the handoff block is filled in with the allowed artifact status vocabulary;
- the approval gate status is clear;
- no design, architecture, backlog, code, or external action has been added.

## Guardrails

Never do any of the following in this skill:

- design UX flows, wireframes, or visual directions;
- choose a framework, architecture, database, or deployment shape;
- create backlog items, epics, or delivery plans;
- write code or tests;
- make approval claims without an explicit approver;
- perform external actions on the user's behalf.

If the idea is still too vague, keep the brief honest and leave the unresolved points visible instead of inventing detail.
