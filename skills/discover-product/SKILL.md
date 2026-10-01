---
name: discover-product
description: Use when a greenfield full-stack idea or an existing project needs evidence-first discovery, domain capability expansion, or an approval-ready product brief/feature proposal.
---

# Discover Product

Turn an early full-stack idea into a clear product brief that a decision maker can approve before any design or architecture work starts.

## Use When

Use this skill when the request is about a new product, a greenfield feature set, or when an existing project needs product feature recommendations and capability expansion.

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

## Natural Conversational Discovery & Intent Decomposition

As KARSA's primary **Planner Skill**, this module must relentlessly decompose ambiguous user intents into actionable technical and business facts before development begins. The model must never operate like a rigid robot going through a bureaucratic checklist, and it must NEVER guess or fabricate
requirements.

### Intent Decomposition Framework (The Planner Tool)

When a user presents a vague idea or raw intent (e.g., "I want a marketplace app" or "Make a booking system"), you MUST decompose it by uncovering:

1. **The Core Value Loop:** What is the single fundamental action the user pays for or returns for? (e.g. searching, buying, communicating).
2. **The Actors & Entities:** Who are the specific users (e.g., Buyer, Seller, Admin) and what are the non-negotiable objects they interact with (e.g., Product, Invoice, Booking)?
3. **The Hard Constraints:** Are there legal, financial, or device-specific limits (e.g., must be mobile-first, must handle local currency)?
4. **The "Why":** Why is this being built? (To save time, generate revenue, internal tool?)

Do not proceed to technical stack or design questions until this intent is fully unpacked and verified by the user.

### Core Rules for Natural Discovery:

1. **Zero Guesswork / No Unfounded Assumptions:**
    - The model must NEVER guess, assume, or invent business domain requirements, entity models, user roles, pricing logic, or operational flows.
    - If an aspect of the application is unspecified or ambiguous (e.g. how users book, what roles exist, what services are offered, what payment methods are supported), the model MUST ask the user directly, naturally, and conversationally.
    - **Exception (Explicit Delegation):** If and ONLY IF the user explicitly delegates choices to the model (e.g., _"terserah kamu"_, _"kamu yang tentukan yang terbaik"_, _"buatkan standar saja"_, _"saya serahkan sepenuhnya"_), THEN the model may propose sensible industry-standard conventions. When
      doing so, the model must explicitly document these choices in the brief as "User-Delegated Defaults".

2. **Conversational, Human-Centric Dialogue:**
    - Engage the user in a natural conversation: listen to their idea, reflect understanding of their vision, and ask open-ended or guiding questions about their target users, key workflows, and desired outcomes.
    - Avoid robotic, repetitive scripted prompts. Adapt the conversational flow to the user's responses, language, and depth of detail.
    - When key technical decisions (delivery target, roles, stack, persistence) need alignment, formulate recommendations conversationally with clear rationale, allowing the user to confirm, adjust, or completely change them without friction.

3. **Material Decisions to Clarify Naturally:**
    - **Platform & Device Target:** Clarify the target platform: Web (responsive desktop/tablet/mobile browser, SPA, SSR), Mobile App (iOS/Android native or cross-platform via React Native/Expo, Flutter), or multi-platform.
    - **Target & Scope:** Clarify whether the goal is a quick prototype/demo or a production-ready full-stack application with real persistence.
    - **Domain & Core Workflows:** Understand the specific domain and primary user workflows (e.g. e-commerce checkout, appointment booking, SaaS workspace management, social content, logistics tracking, finance, etc.) without pre-assuming or forcing any specific industry logic.
    - **Access & Roles:** Clarify who the users are (e.g. public end-users, registered customers, staff operators, administrators) and what capabilities each role possesses.
    - **Stack & Architecture:** Preserve any stack preference stated by the user. If unspecified, offer platform-appropriate defaults (for Web: FastAPI + React/Vite; for Mobile: FastAPI + React Native/Expo or Flutter; or user-preferred technologies).
    - **Persistence & Transactions:** Clarify data storage needs and how transactional or payment flows are handled (e.g. manual operational recording, mock/simulated, or live payment gateway).
    - **Brand Personality & Anti-Sameness Aesthetic:** Uncover the intended visual archetype and emotional tone of the product (e.g. _Utilitarian & High-Density_, _Editorial & Typographic_, _Warm & Humanistic_, _Industrial & Technical_, or _Playful & Dynamic_). Strictly prevent generic "AI Slop
      Design" (the mathematical average of the web: default Inter font + purple/blue gradients + white cards everywhere). If the user delegates choices, assign a distinct, domain-tailored aesthetic archetype rather than generic SaaS defaults.

## Evidence-First Workflow

1. Read every available artifact before asking questions.
2. Separate facts, assumptions, and open questions.
3. If the root is unresolved, ask only the orchestrator's root question and do not include a readiness or other discovery proposal in that response.
4. Otherwise, issue one active discovery proposal for the earliest missing material decision. A bare `Yes` accepts only the exact current proposal; a `No`, `Revision`, or custom answer never fills any other decision.
5. Prefer evidence over memory, opinions, or guesses, and restate only the confirmed decision after each accepted proposal.
6. Persist each accepted decision in the draft brief with its topic, proposed value, exact question, displayed options, literal `Yes` reply, prompt evidence, and resulting facts. Keep rejected, revised, and custom answers visible rather than rewriting them as confirmation.
7. Keep the brief product-level only, no solution design. Stop when the brief is approval-ready or when a material blocker remains.

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

## What To Produce (Product & Scope Contracts)

This skill MUST physically create three foundational contract documents in the `<project-root>/docs/` directory. **Every document is a binding contract, NOT an outline or draft stub. Writing placeholder statements such as "akan diisi nanti", "saat ini kosong", or generating fewer than 30 substantive lines is strictly prohibited.**

1. `docs/01_product_brief.md`: Detailed Product Summary, Users, Jobs & Outcomes, complete In-Scope vs Non-Goals, Readiness Target & Acceptance Boundaries, FR/NFR definitions with acceptance signals, Success Metrics, and Handoff block.
2. `docs/02_scope_and_delivery.md`: Concrete Release Phasing breakdown (S0 MVP, S1, S2) with exact scope boundaries, technical constraints, and anti-scope protections (Non-goals).
3. `docs/13_decisions_and_questions.md`: The Contract Registry containing:
   - D-Register (Decisions): Table with ID, Status, Decision Statement, Source/Evidence.
   - W-Register (Workflows): Table of business workflows clarified with the user.
   - Q-Register (Open Questions): Priority-ranked questions, impacted gates, and explicit resolutions.
   - A-Register (Assumptions): Validated vs unvalidated domain assumptions.

## Artifact Root Contract

`fullstack-orchestrator` resolves and verifies one absolute `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`. Keep the existing `output_path` value in the
`fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, an auto-created scratch or product-name directory, or an unrelated current working directory. If bootstrap did not supply a host-verified active
root, STOP for bootstrap; do not independently infer a root or ask a second location question.

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

### 3.1 Contract Registry (D/W/Q/A)

Initialize the project's Contract Registry. Every product decision made during discovery MUST be explicitly logged here.

- **D-Register (Decisions):** Approved product decisions (e.g. `D-01 | APPROVED | Target is MVP | User explicit statement`).
- **W-Register (Working Clarifications):** Technical details agreed upon (e.g. `W-01 | Currency is IDR, stored as integer`).
- **Q-Register (Open Questions):** Unanswered questions that MUST be answered before specific phases. Categorize priority (Critical, High, Medium, Low).
- **A-Register (Assumptions):** Assumptions made during discovery that need validation.

The orchestrator (KARSA) strictly enforces that no development begins if Critical/High Q-register items remain OPEN.

### 3.2 Full-Request Obligation Ledger

Preserve the original request as a ledger, not as a summary. Every accepted discovery proposal and every `FR-*` requirement must have an entry with its source evidence, requirement or decision ID, required or optional status, exact intended outcome, and initial state `unplanned`. The later blueprint
and backlog extend the same entries with mapped stories, release slices, and evidence; they do not replace them.

Required entries may progress through `planned`, `in-progress`, `validated`, and `released`, but they may become `scope-reduced` only after an explicit user scope-reduction decision names the exact obligation. A bare `Yes` to a brief, backlog, item report, increment manifest, verifier report, or
slice release plan never reduces, defers, or completes another obligation. Do not call the brief approval-ready while a required accepted proposal or original functional request has been silently omitted or described only as a future idea.

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

This is scope confirmation, not an architecture implementation. Do not record a database, provider, framework, or deployment service as confirmed without the exact accepted proposal evidence. The default stack is an offer, not evidence to invent a database, vendor, TypeScript policy, or gateway
configuration.

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
output_path: docs/01_product_brief.md
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

Before review, label the body with an immutable `Artifact Revision`. A Review Record is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records and allow only one active request across the lifecycle. The active record binds its request ID,
canonical product-brief path, content revision, exact question, simplified options (`Yes`, `No`, and `Other` for user typing/comments), prompt evidence, and source user reply or decision evidence.

Use native `ask_question` only when the active host exposes it with its actual schema; otherwise ask in plain chat: `Review docs/01_product_brief.md@[revision]. Approve this exact content?` Options are `Yes` (approve), `No` (reject and pause), and `Revision` (give meaningful freeform feedback). A
direct short Yes or No is valid only for this unchanged shown question; no path, revision, or host ID is required. A stale, duplicate, host, summary, or unrelated reply has no effect. On resume, re-read the canonical brief and display its bound pending question once.

Yes resolves the record and updates only closed governance metadata to `status: approved` and `approval: approved`. No resolves it as rejected and stops until the user explicitly asks to revise. Comments or feedback entered via `Other` (or user typing) without meaningful content ask only for
clarifying feedback; sufficient feedback resolves the request, sets the brief to `draft`, and routes to this owner. A substantive content revision supersedes the prior record, creates a new Artifact Revision, invalidates affected approvals, and asks again only when the revised brief returns to
`awaiting-approval`. Preserve a confirmed stack unless the user explicitly changes it. Do not intentionally create, update, or open `implementation_plan.md`, editor tabs, or `RequestFeedback` metadata; native host presentation is not approval evidence and any host-mandated opening is outside plugin
control.

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
- the full-request obligation ledger contains every accepted proposal and `FR-*` item, with no required item silently deferred;
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
