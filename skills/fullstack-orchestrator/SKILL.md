---
name: fullstack-orchestrator
description: Mandatory bootstrap for natural-language requests to create, build, or scaffold a new web, mobile, cross-platform, frontend-and-backend, or full-stack application; resolves the project root, infers visible artifact state, requires explicit human approval at every phase boundary, and routes then executes enabled specialist skills inline in the same agent.
---

# Full-Stack Orchestrator

## Role

This skill is a deterministic natural-language routing and execution contract for greenfield full-stack work. It inspects visible evidence, selects the next specialist route, loads that skill contract, and executes it inline in the same agent.

The orchestrator does not replace specialist ownership, produce a separate orchestrator artifact, self-approve, retain persistent state, deploy, or claim cross-chat persistence. The selected specialist owns its artifacts and output even when this agent executes it. After selecting a skill, the orchestrator MUST NOT stop merely to report that selection or wait for a second agent. It MUST load and execute the selected contract inline. It MUST NOT invoke background, concurrent, or subagents, or promise host-managed auto-execution.

## Mandatory Bootstrap Scope

This skill is the mandatory bootstrap before native planning, coding, or a direct specialist workflow for an in-scope request. In scope includes natural-language requests to create, build, or scaffold a new web app, mobile app, cross-platform app, frontend-and-backend app, or full-stack app, including equivalent requests for a new product, MVP, or blank-slate application.

The bootstrap does not apply to bug fixes, changes to existing apps, libraries, CLIs, general questions, or isolated pages or prototypes unless the user explicitly requests one as a new application. Outside this scope, do not claim this lifecycle owns the request.

## Project Root And Artifact Contract

Resolve `<project-root>` before inspecting lifecycle evidence or selecting a specialist:

1. An explicit user target path wins.
2. Otherwise, use the active workspace only when it is clearly the target application and is not this plugin repository.
3. If the location is ambiguous, ask exactly one question: `Which project-root path should contain this new application?` Then stop for that required input. Do not ask a second routing question. After the root is resolved, a selected specialist may ask the discovery questions required by its own contract.

All lifecycle artifacts and evidence paths are project-relative. Resolve every `artifacts/...` path in this contract as `<project-root>/artifacts/...`, including product, UX, architecture, planning, implementation, quality, security, release, proof, and manifest artifacts. Never write lifecycle artifacts into the plugin installation or repository, or into an unrelated current working directory. Keep `fullstack-skill-handoff/v1` `output_path` values as their existing project-relative `artifacts/...` paths; the root is execution context, not a new handoff field.

Route only to these exact skill names:

- `discover-product`
- `design-experience`
- `define-architecture`
- `plan-delivery`
- `implement-feature`
- `verify-quality`
- `review-security`
- `prepare-release`

No other skill may substitute for one of these specialists.

## Authoritative Evidence

Visible artifacts below `<project-root>/artifacts/` and their handoffs are authoritative. Chat memory, summaries, prior routing responses, and `next_skills` are non-authoritative.

Preserve the existing handoff contract:

- `schema` MUST be `fullstack-skill-handoff/v1`.
- Artifact lifecycle `status` MUST remain one of `draft | awaiting-approval | approved | rejected | blocked`.
- `approval` MUST remain separate from artifact lifecycle status.
- `next_skills` MUST remain advisory downstream guidance. It is not evidence that a skill was invoked, work ran, or approval was granted.
- Artifact status, specialist technical verdict, and explicit human approval MUST remain separate facts. One MUST NOT be inferred from another.
- `awaiting-approval` is not approval. A technical `pass`, `pass-with-findings`, `complete`, or `PASS` is not approval.
- Human approval MUST be explicit and visible in the evidence used for downstream routing. The orchestrator MUST NOT self-approve or rewrite an artifact to make it approved.

The router MUST inspect only the evidence needed to determine the earliest unsatisfied prerequisite. Relevant authoritative artifacts are:

| Owner | Artifact |
| --- | --- |
| `discover-product` | `<project-root>/artifacts/discovery/product-brief.md` |
| `design-experience` | `<project-root>/artifacts/ux/experience-spec.md` |
| `define-architecture` | `<project-root>/artifacts/architecture/application-blueprint.md` |
| `plan-delivery` | `<project-root>/artifacts/planning/delivery-backlog.md` |
| `implement-feature` | `<project-root>/artifacts/implementation/<item-id>-implementation-report.md` and `<project-root>/artifacts/implementation/<release-slice-id>-increment-manifest.md` |
| `verify-quality` | `<project-root>/artifacts/quality/<candidate-id>-quality-report.md` |
| `review-security` | `<project-root>/artifacts/security/<candidate-id>-security-review.md` |
| `prepare-release` | `<project-root>/artifacts/release/<candidate-id>-release-plan.md` |

## Deterministic Routing Procedure

After resolving `<project-root>`, apply these routing rules in order. The first matching rule determines the candidate route and its inline execution. Before emitting that route, apply the specialist availability guard below. A selected route is not a stop condition.

1. Evidence conflict or ambiguity: If artifacts disagree about status, approval, IDs, candidate, slice, current revision, or ownership, list the conflict, ask exactly one precise question that resolves the route, and stop for that required input. Do not guess.
2. New-chat recovery: Reconstruct state from visible artifacts below `<project-root>/artifacts/` and `fullstack-skill-handoff/v1` handoffs. If prior progress is claimed but the evidence is absent, request only the latest artifact and handoff needed to prove that state, then stop for that required input. If visible evidence shows an incomplete chain, select and execute the earliest missing prerequisite. If no lifecycle artifact exists, select and execute `discover-product`.
3. Approval stop: If the current artifact or either artifact at a join is `awaiting-approval`, ask the named human for one explicit `approve`, `reject`, or `revise` decision and stop for that approval. Downstream routing MUST wait until the decision is recorded as authoritative evidence.
4. Rejection or revision: If an artifact is `rejected`, or a human requests revision, select and execute only the specialist that owns that artifact. That specialist stops at its next approval boundary.
5. Draft or blocked work: Select and execute the owner of a `draft` artifact. For `blocked`, select and execute the owner of the earliest missing or rejected prerequisite named by the evidence. If the blocker is ambiguous, apply rule 1.
6. Visual freshness: Before planning, UI implementation, verification, remediation, or release routing, compare every governing visual reference with the current approved experience specification. Every reference MUST exactly match `experience-spec@VDC-NNN#VIS-NNN`, with three decimal digits in both IDs. A revision-only, noncanonical, stale, superseded, or mismatched reference stops the normal route for missing current input. Select and execute `design-experience` first; after the revised experience specification is explicitly approved, select and execute `plan-delivery`; after the updated backlog is explicitly approved, select and execute affected `implement-feature` items one at a time to regenerate implementation and evidence. Run both verifiers sequentially in this same agent when their prerequisites are approved. Never silently carry a prior visual reference forward.
7. Lifecycle route: If none of the stop rules applies, select and execute the next route from the lifecycle below.

Specialist availability guard: Before executing a selected route, confirm every selected specialist is enabled or available. If one is not, identify its exact name and stop for the missing skill contract or required input artifacts. Tell the human to enable that skill or provide its `SKILL.md` contract and required input artifacts, then retry. MUST NOT substitute another skill.

Every transition to a downstream phase requires explicit human approval of every upstream artifact used by that phase. The router MUST NOT weaken a specialist's own preconditions.

## Lifecycle And Join Rules

1. Discovery: With no approved product brief, select and execute `discover-product`. It stops only for required discovery input or the resulting brief's human-approval boundary.
2. Experience and architecture: Only after the product brief is explicitly approved, select `design-experience` and `define-architecture` as a paired route. Load and execute them sequentially in this order in the same agent. Each branch has the same approved brief prerequisite and retains its own output and approval boundary.
3. Design-architecture join: `plan-delivery` MUST NOT be selected until both the experience specification and application blueprint are explicitly approved. If one branch is approved and the other is missing, draft, rejected, or blocked, select and execute only the incomplete branch. A change to shared approved input that invalidates either branch reopens that branch.
4. Planning: After the product brief, current experience specification, and application blueprint are approved, select and execute `plan-delivery`. It stops at the delivery backlog's explicit human-approval boundary.
5. One-item implementation loop: After the delivery backlog is approved, select and execute exactly one Ready backlog item with `implement-feature`. Never batch items. It stops for required approval of each resulting item report and increment-manifest state. If required slice items remain after approval, select and execute the next single Ready item with `implement-feature`.
6. Quality-security gate: Select `verify-quality` and `review-security` as a paired route only after every required item report and the release-slice increment manifest are explicitly approved. Both MUST review the same candidate and approved evidence set. Load and execute them sequentially in this order in the same agent.
7. Quality-security join: One verifier cannot satisfy the other branch. The join remains closed until both reports exist and are explicitly approved. Quality `conditional` or `fail`, or security `block`, enters remediation regardless of artifact approval. Security `pass-with-findings` is eligible only when every finding is nonblocking and no blocker exists.
8. Remediation: After blocking quality or security evidence is approved, select and execute `plan-delivery` for one traceable remediation backlog item. Stop for explicit human approval of that item. Then select and execute that one item with `implement-feature`, stop for approval of its report and updated manifest, and execute `verify-quality` then `review-security` against the remediated candidate. Repeat until both approved verifier reports satisfy the release criteria. A waiver MUST NOT convert `conditional`, `fail`, or `block` into an eligible verdict.
9. Release planning: Select and execute `prepare-release` only when the approved quality report has technical verdict `pass`, the approved security report has technical verdict `pass` or nonblocking `pass-with-findings`, no blocker exists, and all required evidence is approved and current. It stops when the release plan reaches its human-approval boundary. This suite does not deploy.

The only paired routes are `design-experience` with `define-architecture`, and `verify-quality` with `review-security`. Execute each pair sequentially in the same agent, never with concurrent or background subagents. Every join MUST wait for both branches and all required human approvals.

Sequential execution does not bypass a stop boundary. If the first specialist asks for input or reaches `awaiting-approval`, end the turn there. After the human responds, re-evaluate visible evidence before executing the remaining specialist. Never present output for a specialist that has not run.

## Ambiguity And Missing Evidence

The router MUST NOT infer a project, candidate, release slice, approval, verdict, or VDC/VIS revision from conversational phrasing.

If more than one route remains possible:

1. State the conflicting or missing facts.
2. Ask one question whose answer selects exactly one route.
3. Stop for that missing input without selecting speculative work.

Examples of precise questions include `Which candidate ID should be evaluated?` and `Is VDC-002 the current human-approved revision?`

## Router Response Contract

Every routing decision MUST begin with this six-field routing summary, in this order, with concise values:

```text
Observed evidence: <resolved project-root; visible artifacts, handoffs, statuses, approvals, verdicts, and revision refs>
Selected next skill(s): <exact allowed skill name(s), or none>
Why: <first matching routing rule>
Missing prerequisites: <minimum missing evidence, or none>
Approval required: <exact human decision needed, or none>
Stop condition: <what must happen before routing can be evaluated again>
```

The routing summary is not specialist output. When a skill is selected, immediately load and execute its contract inline, then label the following content `Specialist output: <skill-name>`. The specialist output follows the selected contract and MUST NOT be presented as additional routing-summary fields. For a paired route, execute the named contracts sequentially and label each specialist output separately. When a stop rule applies, `Selected next skill(s)` MUST be `none`. The summary remains ephemeral routing guidance; the orchestrator MUST NOT create or require a persistent orchestrator report, handoff, schema, hidden state, lifecycle status, or technical verdict.

## Natural-Chat Examples

### Start

User: `Build a new inventory app. There are no artifacts yet.`

```text
Observed evidence: No lifecycle artifacts or handoffs are visible.
Selected next skill(s): discover-product
Why: Discovery is the earliest missing prerequisite.
Missing prerequisites: Product idea evidence required by discover-product.
Approval required: Human approval of the resulting product brief before design or architecture.
Stop condition: Continue inline with discover-product; stop only if it needs required discovery input or when its product brief reaches awaiting-approval.
Specialist output: discover-product
<Run the discover-product contract in this same agent. Its questions or product brief are specialist output, not routing fields.>
```

### Resume With Approved Brief

User: `Resume. The product brief handoff is visible and approved.`

```text
Observed evidence: Approved product brief with fullstack-skill-handoff/v1; no experience specification or blueprint.
Selected next skill(s): design-experience and define-architecture, paired sequential execution, join required
Why: The approved brief opens both branches.
Missing prerequisites: Approved experience specification and approved application blueprint before planning.
Approval required: Separate explicit human approval for both branch artifacts.
Stop condition: Execute design-experience then define-architecture inline; stop at each required human-approval boundary, and plan-delivery waits for both approvals.
Specialist output: design-experience
<Run the design-experience contract in this same agent.>
Specialist output: define-architecture
<On a later turn after the preceding approval stop is resolved, re-evaluate evidence and run define-architecture if eligible. Do not emit this section before it runs.>
```

### Awaiting Approval

User: `Continue from an experience specification marked awaiting-approval.`

```text
Observed evidence: Experience specification status awaiting-approval; approval pending.
Selected next skill(s): none
Why: Awaiting-approval is a mandatory approval stop, not approval.
Missing prerequisites: Explicit human decision on the experience specification.
Approval required: Approve, reject, or revise?
Stop condition: STOP until that decision is recorded in authoritative evidence.
```

### Remediation

User: `Quality is approved with fail and security is approved with block. Continue.`

```text
Observed evidence: Approved quality report verdict fail; approved security review verdict block.
Selected next skill(s): plan-delivery
Why: Blocking verifier verdicts require a traceable remediation backlog item.
Missing prerequisites: One human-approved remediation backlog item.
Approval required: Human approval of the remediation item before implementation.
Stop condition: Execute plan-delivery inline; stop when the remediation item reaches awaiting-approval. After approval use implement-feature, then run both verifiers sequentially.
Specialist output: plan-delivery
<Run the plan-delivery contract in this same agent.>
```

### Stale VDC/VIS

User: `Implement the UI item using experience-spec@VDC-001#VIS-004, but the current approved spec is VDC-002.`

```text
Observed evidence: Backlog reference experience-spec@VDC-001#VIS-004 conflicts with current approved VDC-002.
Selected next skill(s): design-experience
Why: The UI reference is stale and blocks implementation.
Missing prerequisites: Approved current VIS reference, replanned backlog mapping, and regenerated affected evidence.
Approval required: Human approval after each design, planning, and affected implementation boundary.
Stop condition: Execute design-experience inline; stop at the revised experience specification approval, then execute plan-delivery and affected implement-feature work in order.
Specialist output: design-experience
<Run the design-experience contract in this same agent.>
```

### Missing Skill

User: `The brief is approved, but define-architecture is not enabled.`

```text
Observed evidence: Approved product brief; define-architecture unavailable.
Selected next skill(s): none
Why: A required specialist is unavailable and no substitution is allowed.
Missing prerequisites: Enabled define-architecture contract and its required input artifacts.
Approval required: none
Stop condition: STOP; enable define-architecture or upload its SKILL.md contract, then retry.
```

### Release Route

User: `Quality is approved with pass. Security is approved with pass-with-findings, all nonblocking, and there is no blocker.`

```text
Observed evidence: Approved current quality report verdict pass; approved current security report verdict pass-with-findings; findings nonblocking; no blocker.
Selected next skill(s): prepare-release
Why: Both verifier branches satisfy the release-planning join.
Missing prerequisites: Release candidate ID, version or build ID, and scope summary required by prepare-release.
Approval required: Human approval of the resulting release plan; separate authorization is required outside this suite for any deployment.
Stop condition: Execute prepare-release inline; stop when the release plan reaches awaiting-approval. Do not deploy.
Specialist output: prepare-release
<Run the prepare-release contract in this same agent.>
```
