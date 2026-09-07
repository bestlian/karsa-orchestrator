---
name: define-architecture
description: Use when an approved product brief must become a framework-neutral application blueprint for delivery planning.
---

# Define Architecture

## Purpose

Turn an approved product brief into `artifacts/architecture/application-blueprint.md`.

Keep the result framework-neutral. Describe the system that should exist, not the stack that might build it.

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

* Start from the approved brief and only use evidence from that brief, existing product context, and confirmed constraints.
* If the brief leaves a gap, mark it as an open question or assumption. Do not guess.
* Do not choose a framework, cloud service, database, queue, or vendor unless the brief or evidence already supports it.
* Do not create a backlog. This skill ends at the blueprint.
* Do not write code.

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
* Backend services.
* Shared services.
* Storage and integration components.
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

### 5. API And Event Contracts

Describe the contract surface between components.

Include:

* Public and internal APIs.
* Request and response shapes at a conceptual level.
* Event names, producers, consumers, and payload intent.
* Versioning rules.
* Idempotency, retries, ordering, and error handling assumptions.
* How each public `CON-NNN` contract is exercised and verified at module boundaries.

### 6. Authentication And Authorization

Define identity and access control at the architecture level.

Include:

* Who authenticates the user or system.
* What authority model is used.
* Roles, permissions, and ownership checks.
* Service to service trust.
* Session or token expectations.

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

### 15. Handoff

End the blueprint with a structured handoff block.

```yaml
schema: fullstack-skill-handoff/v1
producing_skill: define-architecture
artifact_id: application-blueprint
output_path: artifacts/architecture/application-blueprint.md
inputs:
  - approved product brief
  - confirmed constraints and evidence
requirement_refs:
  - approved product requirement IDs
decision_refs:
  - architecture decisions, ADR references, and `DEP-NNN` or `MNT-NNN` maintainability decisions
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
* The blueprint states source-code maintainability expectations, module ownership, public contracts, dependency direction, cycle constraints, naming boundaries, and boundary test strategy.
* The blueprint uses stable `MOD-NNN`, `CON-NNN`, `DEP-NNN`, and `MNT-NNN` identifiers and every maintainability source_refs entry resolves to an exact approved blueprint anchor.
* Every approved requirement has traceability.
* Open questions and assumptions are explicit.
* Refactoring triggers are evidence backed and do not rely on a universal line cap.
* No backlog, code, or deployment content was added.
* The handoff block is present and uses the shared schema.

## Output Artifact

Write the final blueprint to `artifacts/architecture/application-blueprint.md`.

The document should be ready for plan-delivery to consume without extra interpretation.
