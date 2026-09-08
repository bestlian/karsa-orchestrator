---
name: fullstack-orchestrator
description: Mandatory bootstrap for natural-language requests to create, build, or scaffold a new web, mobile, cross-platform, frontend-and-backend, or full-stack application; resolves the project root, infers visible artifact state, requires explicit human approval at every phase boundary, and routes to enabled specialist skills without invoking them directly.
---

# Full-Stack Orchestrator

## Role

This skill is a deterministic natural-language routing and control-plane contract for greenfield full-stack work. It inspects visible evidence and names the next specialist route.

It is not a worker, artifact producer, approval authority, persistent state store, direct skill invoker, deployment tool, or replacement for any specialist. It MUST NOT write specialist artifacts, invoke skills, promise Antigravity auto-execution, run work in the background, chain work automatically, or claim cross-chat persistence. A human or the hosting environment must activate each selected specialist.

## Mandatory Bootstrap Scope

This skill is the mandatory bootstrap before native planning, coding, or a direct specialist workflow for an in-scope request. In scope includes natural-language requests to create, build, or scaffold a new web app, mobile app, cross-platform app, frontend-and-backend app, or full-stack app, including equivalent requests for a new product, MVP, or blank-slate application.

The bootstrap does not apply to bug fixes, changes to existing apps, libraries, CLIs, general questions, or isolated pages or prototypes unless the user explicitly requests one as a new application. Outside this scope, do not claim this lifecycle owns the request.

## Project Root And Artifact Contract

Resolve `<project-root>` before inspecting lifecycle evidence or selecting a specialist:

1. An explicit user target path wins.
2. Otherwise, use the active workspace only when it is clearly the target application and is not this plugin repository.
3. If the location is ambiguous, ask exactly one question: `Which project-root path should contain this new application?` Then STOP. Do not ask a second routing or discovery question.

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

After resolving `<project-root>`, apply these routing rules in order. The first matching rule determines the candidate route. Before emitting that route, apply the specialist availability guard below.

1. Evidence conflict or ambiguity: If artifacts disagree about status, approval, IDs, candidate, slice, current revision, or ownership, list the conflict, ask exactly one precise question that resolves the route, and STOP. Do not guess.
2. New-chat recovery: Reconstruct state from visible artifacts below `<project-root>/artifacts/` and `fullstack-skill-handoff/v1` handoffs. If prior progress is claimed but the evidence is absent, request only the latest artifact and handoff needed to prove that state, then STOP. If visible evidence shows an incomplete chain, route to the earliest missing prerequisite. If no lifecycle artifact exists, route to `discover-product`.
3. Approval stop: If the current artifact or either artifact at a join is `awaiting-approval`, ask the named human for one explicit `approve`, `reject`, or `revise` decision and STOP. Downstream routing MUST wait until the decision is recorded as authoritative evidence.
4. Rejection or revision: If an artifact is `rejected`, or a human requests revision, route only to the specialist that owns that artifact and STOP at its next approval boundary.
5. Draft or blocked work: Route a `draft` artifact to its owner. For `blocked`, route to the owner of the earliest missing or rejected prerequisite named by the evidence. If the blocker is ambiguous, apply rule 1.
6. Visual freshness: Before planning, UI implementation, verification, remediation, or release routing, compare every governing visual reference with the current approved experience specification. Every reference MUST exactly match `experience-spec@VDC-NNN#VIS-NNN`, with three decimal digits in both IDs. A revision-only, noncanonical, stale, superseded, or mismatched reference MUST STOP the normal route. Route first to `design-experience`; after the revised experience specification is explicitly approved, route to `plan-delivery`; after the updated backlog is explicitly approved, route affected items one at a time to `implement-feature` to regenerate implementation and evidence. Both verifiers MUST then be rerun when their prerequisites are approved. Never silently carry a prior visual reference forward.
7. Lifecycle route: If none of the stop rules applies, select the next route from the lifecycle below.

Specialist availability guard: Before naming a candidate route, confirm every selected specialist is enabled or available. If one is not, identify its exact name and STOP. Tell the human to enable that skill or upload its `SKILL.md` contract and required input artifacts, then retry. MUST NOT substitute another skill.

Every transition to a downstream phase requires explicit human approval of every upstream artifact used by that phase. The router MUST NOT weaken a specialist's own preconditions.

## Lifecycle And Join Rules

1. Discovery: With no approved product brief, route to `discover-product`. STOP when its brief is `awaiting-approval`.
2. Experience and architecture: Only after the product brief is explicitly approved, route `design-experience` and `define-architecture` as parallel branches. This names two independent routes; it does not invoke or background either skill.
3. Design-architecture join: `plan-delivery` MUST NOT be selected until both the experience specification and application blueprint are explicitly approved. If one branch is approved and the other is missing, draft, rejected, or blocked, route only the incomplete branch. A change to shared approved input that invalidates either branch reopens that branch.
4. Planning: After the product brief, current experience specification, and application blueprint are approved, route to `plan-delivery`. STOP for explicit approval of the delivery backlog.
5. One-item implementation loop: After the delivery backlog is approved, route exactly one Ready backlog item to `implement-feature`. Never batch items. STOP for required approval of each resulting item report and increment-manifest state. If required slice items remain after approval, route the next single Ready item to `implement-feature`.
6. Quality-security gate: Route `verify-quality` and `review-security` as parallel branches only after every required item report and the release-slice increment manifest are explicitly approved. Both MUST review the same candidate and approved evidence set. This names two independent routes; it does not invoke or background either skill.
7. Quality-security join: One verifier cannot satisfy the other branch. The join remains closed until both reports exist and are explicitly approved. Quality `conditional` or `fail`, or security `block`, enters remediation regardless of artifact approval. Security `pass-with-findings` is eligible only when every finding is nonblocking and no blocker exists.
8. Remediation: After blocking quality or security evidence is approved, route to `plan-delivery` for one traceable remediation backlog item. STOP for explicit human approval of that item. Then route that one item to `implement-feature`, STOP for approval of its report and updated manifest, and rerun both `verify-quality` and `review-security` against the remediated candidate. Repeat until both approved verifier reports satisfy the release criteria. A waiver MUST NOT convert `conditional`, `fail`, or `block` into an eligible verdict.
9. Release planning: Route to `prepare-release` only when the approved quality report has technical verdict `pass`, the approved security report has technical verdict `pass` or nonblocking `pass-with-findings`, no blocker exists, and all required evidence is approved and current. STOP when the release plan is `awaiting-approval`. This suite does not deploy.

The only parallel routes are `design-experience` with `define-architecture`, and `verify-quality` with `review-security`. Every join MUST wait for both branches and all required human approvals.

## Ambiguity And Missing Evidence

The router MUST NOT infer a project, candidate, release slice, approval, verdict, or VDC/VIS revision from conversational phrasing.

If more than one route remains possible:

1. State the conflicting or missing facts.
2. Ask one question whose answer selects exactly one route.
3. STOP without selecting speculative work.

Examples of precise questions include `Which candidate ID should be evaluated?` and `Is VDC-002 the current human-approved revision?`

## Router Response Contract

Every response MUST contain only these fields, in this order, with concise values:

```text
Observed evidence: <resolved project-root; visible artifacts, handoffs, statuses, approvals, verdicts, and revision refs>
Selected next skill(s): <exact allowed skill name(s), or none>
Why: <first matching routing rule>
Missing prerequisites: <minimum missing evidence, or none>
Approval required: <exact human decision needed, or none>
Stop condition: <what must happen before routing can be evaluated again>
```

When two skills are selected, label them `parallel, join required`. When a STOP rule applies, `Selected next skill(s)` MUST be `none`. The response is ephemeral routing guidance. The orchestrator MUST NOT create or require a persistent orchestrator report, handoff, schema, hidden state, lifecycle status, or technical verdict.

## Natural-Chat Examples

### Start

User: `Build a new inventory app. There are no artifacts yet.`

```text
Observed evidence: No lifecycle artifacts or handoffs are visible.
Selected next skill(s): discover-product
Why: Discovery is the earliest missing prerequisite.
Missing prerequisites: Product idea evidence required by discover-product.
Approval required: Human approval of the resulting product brief before design or architecture.
Stop condition: STOP when the product brief reaches awaiting-approval.
```

### Resume With Approved Brief

User: `Resume. The product brief handoff is visible and approved.`

```text
Observed evidence: Approved product brief with fullstack-skill-handoff/v1; no experience specification or blueprint.
Selected next skill(s): design-experience and define-architecture, parallel, join required
Why: The approved brief opens both branches.
Missing prerequisites: Approved experience specification and approved application blueprint before planning.
Approval required: Separate explicit human approval for both branch artifacts.
Stop condition: STOP at either awaiting-approval artifact; plan-delivery waits for both approvals.
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
Stop condition: STOP when the remediation item reaches awaiting-approval; after approval use implement-feature, then rerun both verifiers.
```

### Stale VDC/VIS

User: `Implement the UI item using experience-spec@VDC-001#VIS-004, but the current approved spec is VDC-002.`

```text
Observed evidence: Backlog reference experience-spec@VDC-001#VIS-004 conflicts with current approved VDC-002.
Selected next skill(s): design-experience
Why: The UI reference is stale and blocks implementation.
Missing prerequisites: Approved current VIS reference, replanned backlog mapping, and regenerated affected evidence.
Approval required: Human approval after each design, planning, and affected implementation boundary.
Stop condition: STOP at the revised experience specification approval; then route plan-delivery and affected implement-feature work in order.
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
Stop condition: STOP when the release plan reaches awaiting-approval; do not deploy.
```
