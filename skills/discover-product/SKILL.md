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

- Is the requested result a `prototype` or a `production-ready` application? If the user says `MVP`, record it as a separate scope or release label and map it to one of those readiness targets.
- Independently, must the architecture be `frontend-only` or `full-stack`? A readiness target never implies an architecture shape.
- Is a visually minimal or restrained experience a product-direction choice? It is independent of the architecture and stack choice.
- Will data be single-user/local or multi-user/shared, and what persistence is required?
- Which identities, including staff roles, permissions, ownership checks, and service or anonymous access, are in scope? Do not silently defer staff authorization.
- Are authentication, authorization, and payments simulated or real? For real payments, which provider and operational boundary are approved?
- Is a stack required, or may the user approve a recommendation? For a new full-stack application with no explicit stack, offer FastAPI for the backend and React with Vite for the frontend, then confirm once. Record the explicit choice or confirmed offer separately from visual direction; do not ask again after an explicit user choice.
- What run target, expected concurrency, security, persistence, backup, migration, configuration, secret handling, logging, and operations scope are proportionate to the requested readiness target?

For shared booking data, recommend a full-stack architecture when evidence supports it, but require explicit scope confirmation before selecting it. Never silently choose `localStorage`, simulated payments, a backend substitute, or a database. A recorded approval for simulated payments is an approved simulation, not an unapproved gap, but it prevents a live-payment-ready claim. Capture only scope-relevant operations needs; do not prescribe universal Kubernetes, managed services, or other gold plating. Respect a technically specified or existing project stack. Otherwise offer, but do not impose, FastAPI with React and Vite for a new full-stack application; a frontend-only prototype may use React and Vite without a FastAPI backend. Keep architecture framework-neutral until a stack is confirmed.

A `production-ready` target requires the substantive backend and frontend acceptance boundary defined by this suite. If a user requests both `production-ready` and `frontend-only`, record the conflict and require a revised target or architecture decision; do not silently downgrade the target or invent a backend.

## Evidence-First Workflow

1. Read every available artifact before asking questions.
2. Separate facts, assumptions, and open questions.
3. Ask 2 to 4 focused questions at a time, only about gaps that can change the brief. Ask the readiness-target and architecture-shape questions early unless their answers are already explicit.
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

Record the two independent delivery decisions before product requirements:

- readiness target: `prototype` or `production-ready`, with evidence and confirming human; record `MVP`, when used, as a separate optional scope or release label mapped to that readiness target;
- architecture shape: `frontend-only` or `full-stack`, with evidence and confirming human;
- the acceptance boundary: what demonstrates the prototype, item, slice, application, and, where applicable, production readiness;
- for a prototype, demo limitations and an explicit statement that it is not a production-ready claim;
- for a production-ready full-stack target, the backend owner, API and integration boundaries, persistence expectation, shared-data model, staff roles and permissions, and real or simulated auth and payment decisions;
- the confirmed stack decision and evidence: explicit user stack, preserved existing stack, or confirmed FastAPI backend with React and Vite frontend offer for a new full-stack application; a frontend-only prototype may confirm React and Vite without FastAPI;
- managed-backend/BaaS capability and deployment preference when the user supplied one, otherwise a visible open question rather than an invented choice;
- a proportional operations scope covering run target, concurrency, security, persistence, backups, migrations, configuration, secrets, logging, and ownership.

This is scope confirmation, not an architecture implementation. Do not select a database, provider, framework, or deployment service without confirmed evidence. The default stack is an offer, not evidence to invent a database, vendor, or TypeScript policy.

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
  - confirmed readiness target, architecture shape, and acceptance boundary
  - confirmed backend owner, API, persistence, staff roles, auth, payment, stack, and deployment decisions when applicable
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

The handoff stays product-level. It records the confirmed readiness target, architecture shape, and acceptance boundary without adding architecture, backlog, or implementation detail.

Attribution: adapted from anti-slop v3.2.4, commit `44be687`, MIT. See `THIRD_PARTY_NOTICES.md`.

## Chat Review Protocol

Before review, label the body with an immutable `Artifact Revision`. A Review Record is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records and allow only one active request across the lifecycle. The active record binds its request ID, canonical product-brief path, content revision, exact question, `Yes`/`No`/`Revision` options, prompt evidence, and source user reply or decision evidence.

Use native `ask_question` only when the active host exposes it with its actual schema; otherwise ask in plain chat: `Review artifacts/discovery/product-brief.md@[revision]. Approve this exact content?` Options are `Yes` (approve), `No` (reject and pause), and `Revision` (give meaningful freeform feedback). A direct short Yes or No is valid only for this unchanged shown question; no path, revision, or host ID is required. A stale, duplicate, host, summary, or unrelated reply has no effect. On resume, re-read the canonical brief and display its bound pending question once.

Yes resolves the record and updates only closed governance metadata to `status: approved` and `approval: approved`. No resolves it as rejected and stops until the user explicitly asks to revise. Revision without meaningful feedback asks only for the missing feedback; sufficient feedback resolves the request, sets the brief to `draft`, and routes to this owner. A substantive content revision supersedes the prior record, creates a new Artifact Revision, invalidates affected approvals, and asks again only when the revised brief returns to `awaiting-approval`. Preserve a confirmed stack unless the user explicitly changes it. Do not intentionally create, update, or open `implementation_plan.md`, editor tabs, or `RequestFeedback` metadata; native host presentation is not approval evidence and any host-mandated opening is outside plugin control.

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
- the independent readiness target and architecture shape are confirmed, including visible prototype limitations or production-ready backend, persistence, staff authorization, and payment boundaries;
- no unresolved question can materially change the product brief.

If any of these are false, mark the output `blocked` or `draft`, and explain why.

Do not self-approve.

## Completion Criteria

Consider the skill complete when:

- `artifacts/discovery/product-brief.md` exists and reflects the evidence gathered;
- the brief contains product summary, users, jobs, outcomes, scope, non-goals, `FR-*`, `NFR-*`, success metrics, risks, assumptions, and open questions;
- the brief records the readiness target, architecture shape, acceptance boundary, and applicable backend, persistence, staff authorization, payment, stack, deployment, operations, and demo-limit decisions;
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
