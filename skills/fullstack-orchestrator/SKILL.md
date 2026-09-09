---
name: fullstack-orchestrator
description: Mandatory bootstrap for natural-language requests to create, build, or scaffold a new web, mobile, cross-platform, frontend-and-backend, or full-stack application; resolves the project root, requires artifact-bound approval and development-start authorization, and routes then executes enabled specialist skills inline in the same agent.
---

# Full-Stack Orchestrator

## Role

This skill is a deterministic natural-language routing and execution contract for greenfield application work. It inspects visible evidence, selects the next specialist route, loads that skill contract, and executes it inline in the same agent.

The orchestrator does not replace specialist ownership, produce a separate orchestrator artifact, self-approve, retain persistent state, deploy, or claim cross-chat persistence. The selected specialist owns its artifacts and output even when this agent executes it. After selecting a skill, the orchestrator MUST NOT stop merely to report that selection or wait for a second agent. It MUST load and execute the selected contract inline. It MUST NOT delegate lifecycle specialist ownership, concurrent branches, or background orchestration. A host-native `browser_subagent` may collect bounded interaction evidence only; it cannot edit features, make approval decisions, select or advance lifecycle phases, or satisfy a join.

## Mandatory Bootstrap Scope

This skill is the mandatory bootstrap before native planning, coding, scaffolding, dependency installation, or a direct specialist workflow for an in-scope request. In scope includes natural-language requests to create, build, or scaffold a new web app, mobile app, cross-platform app, frontend-and-backend app, or full-stack app, including equivalent requests for a new product, MVP, or blank-slate application.

The bootstrap does not apply to bug fixes, changes to existing apps, libraries, CLIs, general questions, or isolated pages or prototypes unless the user explicitly requests one as a new application. Outside this scope, do not claim this lifecycle owns the request.

## Project Root And Artifact Contract

Resolve and verify one absolute `<project-root>` before emitting a routing summary, inspecting lifecycle evidence, creating lifecycle state, or writing an artifact:

1. Accept a root only when the host exposes it as the active registered or mounted project directory. Retain the exact absolute path and host evidence used to verify it.
2. An explicit user target is the preferred candidate, but it must match that host-visible active directory. A product name, auto-created scratch directory, conversation label, plugin installation, or inferred shell current directory is never root evidence.
3. If the host reports conflicting or multiple roots, state the exact absolute candidates, make one root-only proposal naming the recommended mounted root, and stop for confirmation. A `Yes` confirms only that proposed root; `No`, `Revision`, or custom text does not select another root. Do not add readiness or discovery questions to this response.
4. If the host does not expose an active registered project directory, do not claim to see the shell working directory. Ask the user to open, mount, or register the intended absolute project directory with the host, then stop. The plugin does not bind a CLI project or workspace by itself.
5. Once the host-visible path and target agree, use that exact absolute path as `<project-root>`. The first six-field routing summary MUST begin its observed evidence with `Resolved project root: <absolute path>` and state the verification source. Do not emit a routing summary or specialist output with a guessed, relative, scratch, or product-name root.

All lifecycle artifacts and evidence paths are project-relative. Resolve every `artifacts/...` path in this contract as `<project-root>/artifacts/...`, including product, UX, architecture, planning, implementation, quality, security, release, proof, and manifest artifacts. Never write lifecycle artifacts into the plugin installation or repository, an auto-created scratch or product-name directory, or an unrelated current working directory. Keep `fullstack-skill-handoff/v1` `output_path` values as their existing project-relative `artifacts/...` paths; the root is execution context, not a new handoff field.

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

## Authoritative Evidence And Reconciliation

Visible artifacts below `<project-root>/artifacts/` and their handoffs are authoritative. Chat memory, summaries, prior routing responses, and `next_skills` are non-authoritative.

Preserve the existing handoff contract:

- `schema` MUST be `fullstack-skill-handoff/v1`.
- Artifact lifecycle `status` MUST remain one of `draft | awaiting-approval | approved | rejected | blocked`.
- `approval` MUST remain separate from artifact lifecycle status.
- `next_skills` MUST remain advisory downstream guidance. It is not evidence that a skill was invoked, work ran, or approval was granted.
- Artifact status, specialist technical verdict, and explicit human approval MUST remain separate facts. One MUST NOT be inferred from another.
- `awaiting-approval` is not approval. A technical `pass`, `pass-with-findings`, `complete`, or `PASS` is not approval.
- Human approval MUST be explicit and visible in the evidence used for downstream routing. It applies only to the exact active Review Record target. A direct `Yes` or `No` needs no path or revision only when it unambiguously answers the unchanged current displayed question; another URI, revision, active editor, current phase, summary, stale reply, or host event MUST NOT transfer approval.
- Before requesting approval, every specialist artifact MUST label an immutable `Artifact Revision` in its document body. The output path and that revision are the approval target; this is document evidence, not a new `fullstack-skill-handoff/v1` top-level key.
- A content `Review Record` has a status independent from the handoff status: `pending`, `resolved`, or `superseded`. Preserve past records. It is pending only while its canonical artifact has handoff status `awaiting-approval`. A `Development Start Authorization` request on an already approved backlog uses the same binding-field schema with a fresh unique `request_id` and also counts as the one active request across the lifecycle. Each persists `request_id`, canonical `target_path`, immutable `content_revision`, exact `question`, options `Yes`, `No`, and `Revision`, prompt evidence, human identity when known, `source_user_reply`, and decision evidence.
- Ask the review question with native `ask_question` only when the active host exposes that tool, using its actual schema. Otherwise ask in plain chat: `Review [target_path]@[content_revision]. Approve this exact content?` Options are `Yes` (approve this exact content), `No` (reject and pause), and `Revision` (provide revision feedback). Do not require a command, an artifact path, a revision, or a host ID in the human reply; a current exact-path reply remains supported.
- Write and read canonical project artifacts with normal filesystem operations. Do not intentionally create, update, open, or focus `implementation_plan.md`, an editor tab, or `RequestFeedback` metadata for approval. Native host review events or presentations are not approval signals. The plugin cannot suppress a host or system mandate that independently creates or opens an artifact; state that limit rather than claiming UI control.
- `Yes` records the approval source reply, sets the target handoff status to `approved`, sets approval to approved, resolves the record, and re-evaluates. `No` records the source reply, sets the target handoff status to `rejected`, sets approval to rejected, resolves the record, and stops. Do not automatically rerun an owner after rejection, including on resume; wait for an explicit user request to revise. `Revision` accepts only explicit revision feedback tied to the current target. If its text is empty, ask only for the missing feedback and keep the same request active. Unrelated or clarification questions leave the request pending and do not modify the artifact or re-run approval automatically. When feedback is sufficient, resolve the request as `Revision`, set the artifact to `draft`, and route only to the owning specialist. A revision keeps an already confirmed stack unless the user explicitly asks for a different stack or migration.
- These status, approval, appended approval `decision_refs`, Review Record state changes, and Development Start Authorization operations are permitted closed governance metadata, not self-approval. They retain the current Artifact Revision and valid approval. They MUST NOT change scope, first item, expected outcome, acceptance, technical result, or other substantive content.
- A substantive content change before a terminal decision supersedes the pending Review Record, creates a new Artifact Revision, and resets approval. Create a new pending record only when the revised artifact returns to `awaiting-approval`. Only an explicit current `Revision` selection or clearly target-bound change feedback is revision feedback; unrelated or clarification questions keep the request pending until answered and do not modify the artifact or re-run approval automatically. A consumed duplicate has no effect. On resume, re-read the current canonical artifact and display its still-pending bound question once; never infer a decision from a summary or a stale reply. A changed backlog re-evaluates and rebinds development authorization to its current scope. A reject, revision, or remediation request never grants downstream permission.
- Information Architecture and UI integrity must be preserved throughout feature implementation. Feature stories must not accumulate disparate user journeys into a single continuous-scroll page (the "Frankenstein page" anti-pattern). Disparate journeys must be structured into dedicated navigation views (such as tabs, distinct routes, or contextual drawers/modals). Secondary cross-sells or add-on services (such as equipment rentals or canteen refreshments) must remain non-blocking so that users can directly checkout core services without forced scrolling. Privileged operational surfaces (such as staff cashier desks or inventory management) must be cleanly isolated from customer booking surfaces. Every released project must include a comprehensive user-facing README.md at its project root.

Before every route, resume, quality gate, security review, or release plan, reconcile the canonical sources rather than trusting a chat summary, presentation, report label, or manifest alone. Re-read every required source report at its exact path and revision; verify its explicit human approval and technical result; compare those facts to the increment manifest and downstream candidate; and block on any mismatch. Tie code and test evidence to a stable revision or checksum of the tested executable, configuration, and source scope, not governance documents or Review Record state. A change in that scope invalidates the affected evidence until the required checks run again. Persist resume-required scope, source revisions, and unresolved gates only in the existing backlog and increment manifests; do not add a state database or engine. Metadata normalization may standardize known values but cannot promote labels, repair missing evidence, or approve work.

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

## Decision Ingestion And Discovery Proposals

Requirement Gathering & Zero-Guesswork Principle: Discovery conversations must be natural, collaborative, and evidence-first. The agent must NEVER invent, guess, or assume domain rules, pricing, operational policies, or business constraints. If the user's initial prompt leaves requirements open, ask natural, targeted clarification questions. The agent only defaults or chooses specifics on the user's behalf if the user explicitly delegates decisions (e.g., 'terserah kamu', 'kamu yang tentukan', 'serahkan sepenuhnya').

Before routing, process only the single visible active request. A `Discovery Proposal` is an input request, not a Review Record or Development Start Authorization. While `discover-product` has one active proposal, a direct `Yes` may accept only that exact recommendation and must be recorded with its exact question, displayed options, literal reply, and resulting decision facts before any next proposal. A `No`, `Revision`, or custom reply affects only that proposal. Never process batched discovery answers as multiple approvals, create a lifecycle approval from a discovery answer, or ask a lifecycle review or start question while a discovery proposal is active.

If no lifecycle request is active, skip lifecycle decision ingestion and evaluate routing from recorded artifact evidence. The selected discovery specialist owns its single current proposal and must not issue a second proposal until the first resolves. Distinguish content review from development-start authorization before interpreting an active lifecycle answer. For a development-start question, Yes or No changes only the authorization record, never the already approved backlog's content approval or handoff status; Revision follows the development-start rule below. Each new question has a fresh unique request ID, not the consumed ID of its preceding review.

1. Re-read its canonical `target_path` and immutable `content_revision`, then confirm the persisted request ID, question, options, and prompt evidence still match the shown question.
2. A direct `Yes` or `No` is valid only when it is the unambiguous reply to that unchanged current question. Exact path-and-revision replies are accepted but not required. A host event, a summary, an active editor, another artifact, an old revision, a stale reply, or a duplicate consumed reply has no effect.
3. For `Yes`, resolve the record and update only the target's closed approval metadata to `approved`, then re-evaluate. For `No`, resolve the record, set the target to `rejected`, and stop until the user explicitly requests a revision. Never turn rejection into automatic owner work on a later `Resume`.
4. For `Revision`, collect nonempty meaningful freeform feedback. If it is missing, ask only for that feedback. When sufficient feedback is present, resolve the record, set the target to `draft`, run only its owner, and ask a new review question only after the revised artifact is ready. Preserve a previously agreed stack unless the user explicitly changes it.
5. If no valid decision is present, display the bound current question once and stop. Never synthesize approval from prior summaries or a recorded decision for another target.

## Deterministic Routing Procedure

After resolving `<project-root>`, apply these routing rules in order. The first matching rule determines the candidate route and its inline execution. Before emitting that route, apply the specialist availability guard below. A selected route is not a stop condition.

1. Evidence conflict or ambiguity: If artifacts disagree about status, approval, IDs, candidate, slice, current revision, or ownership, list the conflict, ask exactly one precise question that resolves the route, and stop for that required input. Do not guess.
2. New-chat recovery: Reconstruct state from visible artifacts below `<project-root>/artifacts/` and `fullstack-skill-handoff/v1` handoffs. If prior progress is claimed but the evidence is absent, request only the latest artifact and handoff needed to prove that state, then stop for that required input. If no lifecycle artifact exists, select and execute `discover-product`. Otherwise defer to approval, rejected, draft, blocked, and lifecycle logic; do not route any incomplete chain from recovery.
3. Approval stop: If an artifact needs review and no active request exists, create the one bound Review Record and ask: `Review [target_path]@[content_revision]. Approve this exact content?` with `Yes`, `No`, and `Revision` options, then stop. If a request is already active, display that exact question once and stop. Downstream routing waits only for its authoritative decision.
4. Development-start stop: Before any scaffold, package/dependency installation, generated starter-app output, or application edit, require Foundation and a valid development-start authorization. Foundation means the approved product brief, experience specification, application blueprint, and delivery backlog at the revisions referenced by the backlog; a Vite or other scaffold is not Foundation. Backlog approval alone is not authorization. Create a separate bound authorization request on that approved backlog, with the same binding-field schema and a fresh unique `request_id`, and the same target path, content revision, question, options, prompt evidence, and source-reply fields as a Review Record: `Start development for [approved backlog revision]? First item: [item]. Expected runnable outcome: [outcome].` with `Yes`, `No`, and `Revision`. Stop before development. `Yes` persists authorization for exactly the shown scope without a content revision bump. `No` records rejected authorization and makes no scaffold, install, or application edit; do not poll again until the user explicitly asks to start or revise. `Revision` requires explicit revision feedback tied to the current backlog or scope and routes to planning, or to the owning prerequisite when scope changes, then requires fresh Foundation reviews as applicable. Do not infer authorization from approval, a native process, an unrelated plan, or a current editor. A material scope or backlog-revision change requires a renewed authorization.
5. Rejection or revision: If an artifact is `rejected`, stop and wait for an explicit request to revise it. If sufficient revision feedback has set an artifact to `draft`, select and execute only its owner. That specialist stops at its next approval boundary.
6. Draft or blocked work: Select and execute the owner of a `draft` artifact. For `blocked`, select and execute the owner of the earliest missing prerequisite named by the evidence; a rejected prerequisite remains stopped until the human requests revision. If the blocker is ambiguous, apply rule 1.
7. Visual freshness: Before planning, UI implementation, verification, remediation, or release routing, compare every governing visual reference with the current approved experience specification. Every reference MUST exactly match `experience-spec@VDC-NNN#VIS-NNN`, with three decimal digits in both IDs. A revision-only, noncanonical, stale, superseded, or mismatched reference stops the normal route for missing current input. Select and execute `design-experience` first; after the revised experience specification is explicitly approved, select and execute `plan-delivery`; after the updated backlog is explicitly approved, seek a renewed development-start authorization when the affected scope is material, then select affected `implement-feature` items one at a time to regenerate implementation and evidence. Run both verifiers sequentially in this same agent when their prerequisites are approved. Never silently carry a prior visual reference forward.
8. Lifecycle route: If none of the stop rules applies, select and execute the next route from the lifecycle below.

Specialist availability guard: Before executing a selected route, confirm every selected specialist is enabled or available. If one is not, identify its exact name and stop for the missing skill contract or required input artifacts. Tell the human to enable that skill or provide its `SKILL.md` contract and required input artifacts, then retry. MUST NOT substitute another skill.

Every transition across major lifecycle phases (Discovery -> Foundation -> Planning -> Development Start -> Slice Milestone -> Release) requires explicit human approval at the governing milestone boundary. Automated verification steps within an authorized development phase run without redundant human micro-approvals.

## Lifecycle And Join Rules

1. Discovery: With no approved product brief, select and execute `discover-product`. It stops only for required discovery input or the resulting brief's human-approval boundary.
2. Experience and architecture: Only after the product brief is explicitly approved, select `design-experience` and `define-architecture` as a paired route. Load and execute them sequentially in this order in the same agent. Each branch has the same approved brief prerequisite and retains its own output and approval boundary.
3. Design-architecture join: `plan-delivery` MUST NOT be selected until both the experience specification and application blueprint are explicitly approved. If one branch is approved and the other is missing, draft, or blocked, select and execute only the incomplete branch. A rejected branch remains paused until the human explicitly requests revision. A change to shared approved input that invalidates either branch reopens that branch.
4. Planning: After the product brief, current experience specification, and application blueprint are approved, select and execute `plan-delivery`. All user stories across all epics and release slices for the entire known product scope must be formed, broken down, and detailed upfront in `artifacts/planning/delivery-backlog.md`. Never generate a partial backlog. Planning stops at the delivery backlog's explicit human-approval boundary so the human user can review and approve the complete story roadmap upfront before any development starts.
5. Implementation loop: After the delivery backlog is approved and its exact revision and scope have a persisted development-start authorization, execute Ready backlog stories with `implement-feature`. Items are implemented one at a time using rigorous TDD (red-green-refactor) and visual browser proof. To eliminate bureaucracy and approval fatigue, individual item reports and intermediate manifest updates serve as automated developer verification records under the human-granted `Development Start Authorization`; they do NOT each trigger separate interactive human modal approval stops. The authorization covers the full authorized scope. When an item is complete and its tests pass, `implement-feature` updates the manifest and proceeds seamlessly to the next Ready item in the authorized slice without asking redundant questions. For authenticated production-ready User/Staff work, JWT, password, server role, and ownership evidence is an early prerequisite; protected endpoints cannot be Ready or described as production-ready before it exists.
6. Quality-security gate and Slice Increment Review: When all items in the release slice are implemented and tested, automatically execute `verify-quality` and `review-security` as a paired sequential route against the completed candidate slice. Once automated quality and security checks pass (or identify blockers), present a consolidated Slice Increment Review to the human user with working browser proof, test results, and the increment demo. Human approval is requested at this meaningful working milestone rather than rubber-stamping internal developer scratch files.
7. Quality-security join: One verifier cannot satisfy the other branch. The join remains closed until both reports exist and are explicitly approved. Quality `conditional` or `fail`, or security `block`, enters remediation regardless of artifact approval. Security `pass-with-findings` is eligible only when every finding is nonblocking and no blocker exists.
8. Remediation: After blocking quality or security evidence is approved, select and execute `plan-delivery` for one traceable remediation backlog item. Stop for explicit human approval of that item. Then select and execute that one item with `implement-feature`, stop for approval of its report and updated manifest, and execute `verify-quality` then `review-security` against the remediated candidate. Repeat until both approved verifier reports satisfy the release criteria. A waiver MUST NOT convert `conditional`, `fail`, or `block` into an eligible verdict.
9. Release planning: Select and execute `prepare-release` only when the approved quality report has technical verdict `pass`, the approved security report has technical verdict `pass` or nonblocking `pass-with-findings`, no blocker exists, and all required evidence is approved and current. It stops when the release plan reaches its human-approval boundary. After that plan is explicitly approved, re-evaluate the application obligation ledger: select the next Ready item across the existing authorized scope, or `plan-delivery` when a required obligation lacks a Ready item. Only when no required obligation remains may the response say the full original scope is delivered. This suite does not deploy.

The only paired routes are `design-experience` with `define-architecture`, and `verify-quality` with `review-security`. Execute each pair sequentially in the same agent; never delegate lifecycle branches or use concurrent/background lifecycle orchestration. The same executing agent retains ownership of artifacts, edits, approvals, routing, and joins; a host-native `browser_subagent` may only collect bounded browser interaction evidence. Every join MUST wait for both branches and all required human approvals.

Sequential execution does not bypass a stop boundary. If the first specialist asks for input or reaches `awaiting-approval`, end the turn there. After the human responds, re-evaluate visible evidence before executing the remaining specialist. Never present output for a specialist that has not run.

## Development Outcome Claims

An implementation report MUST distinguish the one completed item from the release slice and the application. A completed item is not a completed slice, and a completed slice is not an application-ready claim. An exactly approved scaffold story or task may be `technical_verdict: complete` when its own concrete acceptance criteria and tests pass, but it must state `slice incomplete` and `application not ready`. A scaffold used as a substitute for a broader functional story is `partial`. For any user-facing UI claim, the report must carry the real-browser evidence required by `implement-feature` and `verify-quality`; a build or HTTP 200 result is boundary evidence only.

Application finalization requires the approved backlog's application obligation ledger to show every original requirement and accepted discovery proposal as `complete` with current approved implementation, slice-manifest, and verifier evidence. A generic `Yes` to a partial summary or slice approval never waives an obligation. Mark work `out-of-scope` only for a specific human decision that names the requirement and rationale. The final response MUST enumerate delivered and pending obligations and say `application not ready` whenever any required obligation, auth boundary, verifier gate, or evidence remains outstanding.

For a `production-ready` target, the candidate must contain substantive `<project-root>/backend/` and `<project-root>/frontend/` deliverables. `backend/` has a runnable server, API contracts, and real database integration; `frontend/` has a runnable client that consumes that API. Empty folders and a `localStorage` stand-in do not satisfy this boundary. Each area documents start, environment, and applicable test commands. A managed backend remains valid only with substantive backend configuration, functions, and API contracts. Root-level `artifacts/`, shared assets, and optional shared tests are allowed; do not restructure the plugin repository itself. SQLite is valid when its file location, permissions, backups, migrations, locking/concurrency, and operating limits are documented.

For a new full-stack application with no explicit stack, offer FastAPI backend with React and Vite frontend and confirm it once; record that confirmed decision in the brief, blueprint, and backlog. An explicit user stack needs no repeat question, and an existing project stack remains unless migration is requested. A frontend-only prototype may use React and Vite without FastAPI. If requirements cannot be met by the confirmed stack, explain the exception and ask before switching. Do not default a database, vendor, or TypeScript policy. Framework neutrality means this offer is never imposed.

## Architecture And Planning MCP Preflight

At the architecture preflight, and again before planning if the project changed, recommend only MCP capability justified by the approved project. Native project tools come first, and no MCP is required to run the application. Record purpose, project scope, prerequisites, install or configuration action, verification, minimum permissions, and restart or reload note. Do not install or modify configuration automatically.

For browser interaction evidence, the default relevant project configuration is a merge into `<project-root>/.agents/mcp_config.json`, preserving existing `mcpServers` entries:

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

Antigravity documents global `~/.gemini/config/mcp_config.json` and project `.agents/mcp_config.json` locations. The launcher uses `npx` when the host starts the server; it is neither native CLI registration nor an application dependency. The locally verified optional registration syntax is `agy mcp add --type stdio playwright npx @playwright/mcp@latest`, followed by `agy mcp list`; neither local help nor the cited docs exposes a project-scope flag, so never call that registration project-scoped or invent `--scope`. Prefer the project config when project scope is needed. Reload or restart only as the active host requires, then verify the server and permissions.

Recommend database MCP only when it adds an approved capability, use least-privilege read-only nonproduction credentials, never expose secrets or a production database, and never auto-mutate data. Recommend GitHub or documentation MCP only when the approved work requires it and a current vendor command is verified; otherwise omit it. Sources: https://antigravity.google/docs/cli/mcp/ and https://github.com/microsoft/playwright-mcp.

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
Observed evidence: Resolved project root: <absolute host-verified path>; <verification source; visible artifacts, handoffs, statuses, approvals, verdicts, and revision refs>
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
Observed evidence: Resolved project root: C:\\Projects\\inventory; host reports this directory as the active registered workspace; no lifecycle artifacts or handoffs are visible.
Selected next skill(s): discover-product
Why: Discovery is the earliest missing prerequisite.
Missing prerequisites: Product idea evidence required by discover-product.
Approval required: Human approval of the resulting product brief before design or architecture.
Stop condition: Continue inline with discover-product; stop only if it needs required discovery input or when its product brief reaches awaiting-approval.
Specialist output: discover-product
<Run the discover-product contract in this same agent. Its questions or product brief are specialist output, not routing fields.>
```

The first discovery proposal for this example may be:

```text
I recommend a production-ready full-stack application for inventory management, with a runnable frontend, backend API, and durable data. Proceed with this target?
Yes / No / Revision / custom requirement
```

A `Yes` accepts only this shown target. It does not accept a later access, stack, database, payment, brief-review, or development-start question.

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
Observed evidence: Experience specification status awaiting-approval; approval pending for artifacts/ux/experience-spec.md@VDC-002.
Selected next skill(s): none
Why: Awaiting-approval is a mandatory approval stop, not approval.
Missing prerequisites: Explicit human decision on the experience specification.
Approval required: Review artifacts/ux/experience-spec.md@VDC-002. Approve this exact content? Yes / No / Revision.
Stop condition: STOP until the bound current Review Record receives a direct Yes, No, or meaningful Revision response.
```

Use native `ask_question` only when the host exposes it with a known schema; otherwise ask this plain-chat question. Host review surfaces are not approval evidence. Do not create or update `implementation_plan.md` for this review.

### Development Start Authorization

User: `Continue.`

```text
Observed evidence: Foundation is approved through delivery-backlog@BL-004; no development-start authorization is recorded for its scope.
Selected next skill(s): none
Why: Development-start stop applies before scaffolding, installing dependencies, or application edits.
Missing prerequisites: Explicit authorization against delivery-backlog@BL-004 and its first Ready item.
Approval required: Start development for delivery-backlog@BL-004? First item: STORY-001. Expected runnable outcome: a local UI that completes the approved inventory-create flow. Yes / No / Revision.
Stop condition: STOP until the separate bound development-start request is answered and persisted with the revision, scope, identity, and exact user evidence.
```

The backlog's approval, a native Process result, or an unrelated plan does not satisfy this stop. `Yes` authorizes only this already approved backlog scope. `No` starts nothing and is not re-asked until the user explicitly asks to start or revise. `Revision` returns to planning or the owning prerequisite and does not start coding.

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
