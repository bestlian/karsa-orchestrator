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
* For each major component, state its purpose, owner, rationale, tradeoff, and observable contract.
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
* Any decision record entries that need to exist.
* Open questions that should become ADRs later if evidence changes.

### 14. Requirement Traceability

Map every approved requirement to the blueprint.

Include:

* A stable requirement identifier for each brief item.
* Where it is addressed in the blueprint.
* Whether it is solved, deferred, or blocked.
* Any assumption tied to the requirement.

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
  - architecture decisions and ADR references
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
  - contracts and traceability
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
6. Build the requirement traceability map last so every requirement points to a finished section.
7. Finish with the handoff block and set the status to `awaiting-approval` every time the blueprint is generated, even if a previous version was already approved.

## Completion Criteria

The skill is complete only when all of these are true:

* `artifacts/architecture/application-blueprint.md` exists.
* The blueprint is framework-neutral and evidence based.
* The blueprint covers every required area in this skill.
* Every approved requirement has traceability.
* Open questions and assumptions are explicit.
* No backlog, code, or deployment content was added.
* The handoff block is present and uses the shared schema.

## Output Artifact

Write the final blueprint to `artifacts/architecture/application-blueprint.md`.

The document should be ready for plan-delivery to consume without extra interpretation.
