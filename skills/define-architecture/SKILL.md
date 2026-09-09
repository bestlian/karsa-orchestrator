---
name: define-architecture
description: Use when an approved product brief must become a framework-neutral application blueprint for delivery planning.
---

# Define Architecture

## Purpose

Turn an approved product brief into `artifacts/architecture/application-blueprint.md`.

Keep the result framework-neutral: describe the system that should exist, not an invented vendor or stack. Record a user-confirmed stack, including a confirmed default offer, as a constraint without imposing it.

## When To Use

Use this skill when:

* A product brief has already been approved.
* The work needs an application blueprint before plan-delivery starts.
* The brief must be translated into architecture decisions, boundaries, and contracts.
* The work can run after discover-product and alongside design-experience.

## Do Not Use When

Do not use this skill when:

* The brief is still unapproved or changing.
* The task is only about UI, copy, or interaction design.
* The task is to write backlog items, implementation steps, or release plans.
* The task is to write code, deploy systems, or pick a framework without evidence.
* The task is to self approve architecture or skip review.

## Operating Rules

* Start from the approved brief and only use evidence from that brief, existing product context, and confirmed constraints. Verify that the approval evidence names the exact current brief path and revision; an active editor, another URI, a prior revision, or a current phase does not transfer it.
* If the brief leaves a gap, mark it as an open question or assumption. Do not guess.
* Do not choose a framework, cloud service, database, queue, or vendor unless the brief or evidence already supports it. Do not create a database default.
* Preserve the independent approved readiness target and architecture shape. A prototype is explicitly not a production-ready claim. A production-ready full-stack application must define the backend owner, API boundaries, persistence, shared-data, staff roles and permissions, and authentication/authorization boundaries. When there is no user sign-in, define the anonymous or service identity boundary explicitly; real-payment boundaries are required when payments are in scope.
* Keep framework neutrality unless the user confirmed a stack or approved a recommendation. For a new full-stack application lacking an explicit stack, the confirmed offer may be FastAPI backend with React and Vite frontend; record that evidence without treating it as a vendor choice. Preserve an existing project stack unless migration is requested. A frontend-only prototype may use React and Vite without FastAPI. If the confirmed stack cannot meet an approved requirement, explain why and ask before switching. Visual minimalism is a design-direction decision, not a stack decision. Do not exclude a managed backend/BaaS merely because it is managed when it provides the real backend capability the approved need requires.
* Do not create a backlog. This skill ends at the blueprint.
* Do not write code.

## Project MCP Preflight

Before architecture is finalized, recommend only project-relevant MCP capabilities. Prefer native tools and do not require an MCP to run the application. For every recommendation, document its purpose, project scope, prerequisites, configuration or install action, verification, minimum permissions, and restart/reload note. Do not install, register, or overwrite configuration.

For browser evidence, recommend merging this documented Playwright configuration into `<project-root>/.agents/mcp_config.json` without replacing existing servers:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Antigravity documents project `.agents/mcp_config.json` and global `~/.gemini/config/mcp_config.json`. `npx` starts the server for the host; it is not an application dependency. The verified optional CLI registration is `agy mcp add --type stdio playwright npx @playwright/mcp@latest`, then `agy mcp list`, but neither the current help nor the official docs exposes a project-scope flag. Do not call that registration project-scoped or invent `--scope`; prefer the project config for project scope. Recommend database MCP only for an approved need, with read-only nonproduction credentials and no automatic mutation. Omit GitHub or documentation MCP unless the project needs it and a current vendor command is verified. Sources: https://antigravity.google/docs/cli/mcp/ and https://github.com/microsoft/playwright-mcp.

## Production-Ready Architecture Gate

For a `production-ready` target, specify substantive `<project-root>/backend/` and `<project-root>/frontend/` (or `<project-root>/mobile/`) output. The backend must be a runnable server with API contracts and database integration; the frontend or mobile client must be a runnable application (web client or mobile app) that consumes the API. Empty directories and `localStorage` substitutes fail this gate. Each area needs start, environment, and applicable test documentation. A managed backend remains valid only with substantive configuration, functions, and API contracts. Root `artifacts/`, shared code, and optional shared tests may remain at root; this does not prescribe restructuring this plugin.

Make gates proportional to the approved scope. Cover applicable run target, process/concurrency model, security and staff authorization, durable persistence, backup/restore, migrations, configuration and secrets, logging/operations, and payment boundary. SQLite is legitimate when file location, permissions, backup/restore, migrations, locking/concurrency, and operating limits are documented. Add an independent audit recommendation when risk warrants it, but do not claim an audit passed or prescribe Kubernetes, a cloud vendor, or other gold plating.

When the approved architecture names SQLite or another database as authoritative storage, record its driver or connection boundary, schema and migration path, and the API path that reads and writes it. Implementation MUST NOT replace it with a writable JSON store unless a human approves an architecture revision. JSON may be used only as a non-authoritative fixture or seed when labeled as such.

## Architecture Quality Filter

* Keep evidence, unknowns, filler, and validation separate. Every architecture claim should be traceable to evidence, marked as an unknown, or stated as an explicit assumption, and every major section should end with the observable check that would prove it.
* Treat design direction and configuration as data when the brief says they vary by mode, tenant, audience, environment, or approval state.
* Define source-code readability as maintainability for developers who will read, change, and own the generated application.
* Prefer repository configured complexity or size limits when they exist. If none exist, use evidence backed refactoring triggers such as mixed responsibilities, excessive branching or fan out, hidden side effects, repeated decision points, weak test seams, or concrete navigation or change risk. Do not set a universal line cap.
* Use stable addressable identifiers for maintainability decisions so downstream plan-delivery can resolve them to exact approved blueprint anchors.
* Do not use patch scripts, generated rewrites, or source or CSS mutation scripts as substitutes for maintainable boundaries.
* If any adapted rule or phrase needs attribution, point to `THIRD_PARTY_NOTICES.md`.

## Required Blueprint Content

The blueprint must cover these areas, in plain language and with enough detail for downstream planning:

### 1. System Context

Describe the product scope, the primary user goals, the external systems it touches, and the high level system boundary.

Include:

* The problem statement.
* The in scope and out of scope parts of the product.
* The main actors and external dependencies.
* The system context in text form or a simple diagram description.
* The confirmed readiness target and architecture shape, its acceptance boundary, and either the prototype demo limits or production-ready backend and persistence boundary.

### 2. Boundaries And Trust Zones

Define where trust changes.

Include:

* Public entry points.
* Internal services and private zones.
* Third party dependencies.
* Privileged operations and where they are isolated.
* Assumptions about what is trusted, semi trusted, and untrusted.
* For each major boundary, state its purpose, owner, rationale, tradeoff, and observable contract.
* Reject generic labels like `service`, `module`, or `layer` unless the responsibility and contract are explicit.

### 3. Components

List the major components and what each one owns.

Include:

* User facing surfaces.
* For a confirmed full-stack application, backend services, shared services, and storage and integration components.
* For a confirmed prototype, the deliberate absence of production backend, persistence, auth, payment, and deployment capabilities, with its demo limitations.
* The responsibility of each component.
* What each component must not do.
* For each major component or module, state its responsibility, public contract, owner, prohibited responsibilities, rationale, tradeoff, and observable contract.
* Assign each major module a stable `MOD-NNN` identifier and each public contract a stable `CON-NNN` identifier.
* Include a module and public contract map that carries those IDs, shows which component exposes which contract, and shows which consumers depend on it.
* Describe the intended dependency direction between modules, the allowed cross boundary references, and the acyclic module graph the design is meant to preserve.
* Assign each dependency direction rule or approved cycle exception a stable `DEP-NNN` identifier.
* Call out any circular dependency. If it is unresolved or not justified, treat it as a blocker.
* Require cycle exceptions to be explicit human approved `DEP-NNN` decisions with rationale, bounded edges, and evidence.
* Define domain vocabulary and naming boundaries where overlapping terms could obscure ownership or behavior.
* Assign each evidence backed refactoring decision a stable `MNT-NNN` identifier when repository configured limits are absent or an observed maintainability trigger is accepted.
* State the boundary test strategy for major module interactions, including contract tests or other observable checks that prove the public contract at the boundary.
* Ensure the module map, contract map, and dependency map can be cited by stable ID in downstream planning source_refs.
* Reject generic component labels unless the responsibility and contract are explicit.

### 4. Data Ownership And Data Model

Define the source of truth for each important data domain.

Include:

* Core entities and relationships.
* Which component owns each entity.
* Read and write paths.
* Data retention and deletion expectations.
* Data that is derived, cached, replicated, or ephemeral.

For confirmed full-stack work, define the persistent source of truth and the owner for each shared domain. `localStorage` is not an implicit substitute for shared persistence. For a prototype, label sample or local data as demo-only and do not represent it as production persistence.

For resource reservations, define an interval model with an authoritative resource ID, real start and end date-time values, and an end-after-start invariant. A unique `start_time` alone is not a conflict control for multi-hour reservations. Define the database or service-level exclusion strategy and transaction boundary that rejects same-start, staggered overlap, enclosing, and enclosed intervals while allowing adjacent intervals. Define stock, order, payment, manual settlement, audit event, and financial-total ownership together when they must commit as one business action; manual settlement must be authenticated Staff-only and idempotent by a stable business key.

### 5. API And Event Contracts

Describe the contract surface between components.

Include:

* Public and internal APIs.
* Request and response shapes at a conceptual level.
* Event names, producers, consumers, and payload intent.
* Versioning rules.
* Idempotency, retries, ordering, and error handling assumptions.
* How each public `CON-NNN` contract is exercised and verified at module boundaries.

For confirmed full-stack work, include every required backend API and integration boundary. For a prototype, record that there is no production API contract rather than inventing one.

For authenticated production-ready full-stack work, publish an endpoint matrix. Treat only approved catalog, login, and registration routes as public. Namespace protected routes as `/api/user/...` and `/api/staff/...`, or record an equally clear approved equivalent. User routes must enforce the token subject's ownership for personal resource operations (such as creating, reading, updating, or cancelling their own transactions, orders, or bookings). Staff/Admin routes must enforce server-side roles for operational management, inventory/resource control, settlement, and reporting. Missing, malformed, invalid-signature, or expired credentials produce `401`; a valid identity without role or ownership produces `403`, or a scoped `404` only where the approved privacy policy intentionally hides existence.

### 6. Authentication And Authorization

Define identity and access control at the architecture level.

Include:

* Who authenticates the user or system.
* What authority model is used.
* Roles, permissions, and ownership checks.
* Service to service trust.
* Session or token expectations.

For confirmed full-stack work with auth, authorization, or real payments in scope, define those boundaries and their owner. For a prototype with simulated behavior, state the simulation and limitation explicitly; never silently turn it into a production security or payment claim.

For customer or staff authentication, specify the approved identity lifecycle, password hashing algorithm and parameters, session or token storage, secure first-admin setup in the project test environment, and credential source. Never seed a shared default administrator password or a fast unsalted hash such as SHA-256. When initial local credentials are needed, plan generated environment-bound credentials or a documented one-time bootstrap, not a user-invented secret. Define ownership checks for user resource reads, updates, and cancellations, and role checks for staff management, operational records, and manual settlement. A manual settlement is an authenticated staff action that persists an auditable actor, amount, state transition, and idempotency reference; do not represent it as a simulated paid state unless that simulation is explicitly approved.

### JWT User And Staff Baseline

For an authenticated production-ready full-stack target, the blueprint must make JWT verification a server-owned boundary, not a header-presence check. Record the fixed allowed signing algorithm, required expiry, issuer or audience checks when used, secure production secret source, rotation or invalidation assumptions, and an active account plus current role lookup by token subject on every protected request. The verifier must select only the configured allowed algorithm, never an algorithm supplied by the token header. Production secrets come from the approved environment or secret boundary with no hard-coded fallback. Ephemeral generated secrets may be used only in isolated development or test fixtures and must be labeled as such.

Passwords must use Argon2 or bcrypt with modern parameters and must never use raw SHA-256 or a shared default password. First Staff provisioning must be a secure one-time bootstrap path with no world-known credential, and public registration can create only the approved unprivileged User identity. The frontend contract must state how it sends a Bearer token for protected calls, its token storage choice and XSS or CSRF tradeoff, refresh behavior if any, expiry recovery, logout or revocation behavior, and the prohibition on logging tokens or secrets. Require HTTPS in the production deployment plan without performing a deployment.

### 7. Privacy

State how personal or sensitive data is handled.

Include:

* Data classification assumptions.
* Collection, storage, use, and sharing limits.
* Retention and deletion rules.
* Access restrictions.
* Any consent or disclosure needs.

### 8. Reliability

State the expected resilience level.

Include:

* Availability goals if they are known.
* Failure modes and recovery expectations.
* Retry and timeout assumptions.
* Degraded mode behavior.
* Disaster recovery or backup needs when relevant.

### 9. Performance

State the expected scale and latency needs.

Include:

* Expected traffic shape.
* Latency or throughput targets if known.
* Hot paths and likely bottlenecks.
* Caching or batching assumptions.
* Capacity risks.

### 10. Observability

Define how the system will be understood in production.

Include:

* Logs, metrics, and traces.
* Key business signals.
* Alerting signals.
* Audit needs for sensitive actions.
* What must be visible to support and operations.

### 11. Migrations And Rollback

If the blueprint replaces or changes an existing system, describe the transition.

Include:

* Migration phases.
* Compatibility needs.
* Data backfill or dual write concerns.
* Rollback triggers and rollback path.
* What can and cannot be reversed.

### 12. Threat Assumptions

Write the threat model assumptions that matter to architecture.

Include:

* Likely attackers or misuse cases.
* Trusted and untrusted inputs.
* Sensitive assets.
* Main abuse paths.
* Security controls assumed to exist elsewhere.

### 13. Alternatives And ADRs

Capture the choices that were considered.

Include:

* At least the main alternative for each important decision.
* Why the preferred path fits the evidence best.
* Any decision record entries that need to exist, including `DEP-NNN` cycle exceptions and `MNT-NNN` maintainability decisions.
* Open questions that should become ADRs later if evidence changes.

### 14. Requirement Traceability

Map every approved requirement to the blueprint.

Include:

* A stable requirement identifier for each brief item.
* Where it is addressed in the blueprint.
* Whether it is solved, deferred, or blocked.
* Any assumption tied to the requirement.
* A source_refs entry or equivalent exact anchor for every maintainability decision and contract reference, resolved through the stable IDs in this blueprint.

The traceability map must retain every original `FR-*` and accepted proposal from the product obligation ledger. For each required entry, name the planned vertical stories and release slice or mark it blocked with the owning decision. A release slice cannot erase an unmapped requirement.

### 15. Handoff

End the blueprint with a structured handoff block.

```yaml
schema: fullstack-skill-handoff/v1
producing_skill: define-architecture
artifact_id: application-blueprint
output_path: artifacts/architecture/application-blueprint.md
inputs:
  - approved product brief
  - confirmed readiness target, architecture shape, and acceptance boundary
  - confirmed constraints and evidence
requirement_refs:
  - approved product requirement IDs
decision_refs:
  - architecture decisions, ADR references, and `DEP-NNN` or `MNT-NNN` maintainability decisions
  - confirmed backend owner, API, persistence, auth, payment, stack, and deployment decisions when applicable
assumptions:
  - explicitly stated architecture assumptions
open_questions:
  - unresolved architecture questions that still need a decision
risks:
  - reliability, performance, privacy, or migration risks
validation_evidence:
  - system context
  - trust zones
  - component ownership
  - `MOD-NNN` module map
  - `CON-NNN` public contract map
  - `DEP-NNN` dependency direction and cycle analysis
  - naming vocabulary and boundary rules
  - `MNT-NNN` maintainability decisions and source_refs anchors
  - contracts and traceability
  - boundary test strategy
  - maintainability constraints and refactoring triggers
status: awaiting-approval
approval: pending
next_skills:
  - plan-delivery
```

## Chat Review Protocol

Label the body with an immutable `Artifact Revision`. A Review Record is independent from handoff status and has status `pending`, `resolved`, or `superseded`. Preserve past records and allow only one active request across the lifecycle. It binds request ID, canonical path, content revision, exact question, simplified options (`Yes`, `No`, and `Other` for user typing/comments), prompt evidence, and the source user reply or decision evidence.

Use native `ask_question` only when the host exposes it with its actual schema; otherwise ask: `Review artifacts/architecture/application-blueprint.md@[revision]. Approve this exact content?` Options are `Yes` (approve), `No` (reject and pause), and `Revision` (meaningful freeform feedback). A direct Yes or No is valid only for this unchanged shown question and needs no path, revision, or host ID. Stale, duplicate, summary, unrelated, or host replies have no effect. On resume, re-read the blueprint and show the bound pending question once.

Yes resolves the record and updates only closed governance metadata to approved. No resolves it as rejected and waits for an explicit user request to revise. Comments or feedback entered via `Other` (or user typing) without meaningful content ask only for clarifying feedback; sufficient feedback sets the artifact to `draft` and routes to this owner. A substantive revision supersedes the old record, creates a new Artifact Revision, invalidates affected approvals, and asks again only after the revised blueprint returns to `awaiting-approval`. Do not intentionally create, update, or open `implementation_plan.md`, editor tabs, or `RequestFeedback` metadata. Native host presentations are not approval evidence, and host-mandated opening cannot be controlled by this plugin.

Do not mark the work approved on your own.

## Writing Process

1. Read the approved brief and extract the stable requirements.
2. Identify system context, trust zones, and major components first.
3. Define data ownership before contracts, because ownership shapes the interfaces.
4. Write contracts, auth, privacy, reliability, performance, and observability next.
5. Add migration, rollback, threat assumptions, and alternatives only where they apply.
6. Assign stable `MOD-NNN`, `CON-NNN`, `DEP-NNN`, and `MNT-NNN` IDs before finalizing traceability so source_refs can resolve to exact approved blueprint anchors.
7. Build the requirement traceability map last so every requirement points to a finished section and every maintainability source_refs entry resolves to an exact approved blueprint anchor.
8. Finish with the handoff block and set the status to `awaiting-approval` every time the blueprint is generated, even if a previous version was already approved.

## Completion Criteria

The skill is complete only when all of these are true:

* `artifacts/architecture/application-blueprint.md` exists.
* The blueprint is framework-neutral and evidence based.
* The blueprint covers every required area in this skill.
* The blueprint preserves the readiness target and architecture shape, with explicit prototype limits or required production-ready backend, API, persistence, staff authorization, payment, and operations boundaries as applicable.
* A production-ready blueprint defines the substantive backend/frontend output, proportional readiness gates, and appropriate audit recommendations without prescribing a framework or gold-plated platform.
* The blueprint states source-code maintainability expectations, module ownership, public contracts, dependency direction, cycle constraints, naming boundaries, and boundary test strategy.
* The blueprint uses stable `MOD-NNN`, `CON-NNN`, `DEP-NNN`, and `MNT-NNN` identifiers and every maintainability source_refs entry resolves to an exact approved blueprint anchor.
* Every approved requirement has traceability.
* Open questions and assumptions are explicit.
* Refactoring triggers are evidence backed and do not rely on a universal line cap.
* No backlog, code, or deployment content was added.
* The handoff block is present and uses the shared schema.

## Output Artifact

Write the final blueprint to `artifacts/architecture/application-blueprint.md`.

## Artifact Root Contract

`fullstack-orchestrator` resolves `<project-root>` before this specialist starts. Every lifecycle artifact path in this contract is project-relative: resolve `artifacts/...` as `<project-root>/artifacts/...`. Keep the existing `output_path` value in the `fullstack-skill-handoff/v1` block unchanged as a relative `artifacts/...` path. Never write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. If bootstrap did not supply a root, STOP for bootstrap; do not independently infer a root or ask a second location question.

The document should be ready for plan-delivery to consume without extra interpretation.
