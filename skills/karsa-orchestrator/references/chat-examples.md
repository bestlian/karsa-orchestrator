# Natural-Chat Interaction Examples

This reference provides turn-by-turn conversational interaction examples across all delivery phases. Load this file when reviewing chat progression patterns or formulating user responses.

---

### Direct Casual Greeting & Identity

User: `Siapa kamu?`

```text
Saya Karsa, partner pengembang sistem Anda. Ada ide aplikasi atau proyek yang ingin kita diskusikan?
```

*(Direct, friendly, natural. No AI metanarration like "Sebagai seorang...", and no reciting job descriptions).*

---

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

---

### Resume With Approved Brief

User: `Resume. The product brief handoff is visible and approved.`

```text
Observed evidence: Approved product brief with fullstack-skill-handoff/v1; no experience specification or blueprint.
Selected next skill(s): design-experience and define-architecture, paired sequential execution, join required
Why: The approved brief opens both branches.
Missing prerequisites: Approved experience specification and approved application blueprint before planning.
Approval required: Separate explicit human approval for both branch artifacts.
Stop condition: Dispatch design-experience and define-architecture in parallel; stop at each required human-approval boundary, and plan-delivery waits for both approvals.
Specialist output: design-experience
<Dispatch the design-experience contract to a subagent and verify its artifact on disk.>
Specialist output: define-architecture
<On a later turn after the preceding approval stop is resolved, re-evaluate evidence and run define-architecture if eligible. Do not emit this section before it runs.>
```

---

### Awaiting Approval

User: `Continue from an experience specification marked awaiting-approval.`

```text
Observed evidence: Experience specification status awaiting-approval; approval pending for artifacts/ux/experience-spec.md@VDC-002.
Selected next skill(s): none
Why: Awaiting-approval is a mandatory approval stop, not approval.
Missing prerequisites: Explicit human decision on the experience specification.
Approval required: Review artifacts/ux/experience-spec.md@VDC-002. Approve this exact content? Yes / No / Other (type comments directly).
Stop condition: STOP until the bound current Review Record receives a direct Yes, No, or user typing/comments response via Other.
```

Use native `ask_question` only when the host exposes it with a known schema; otherwise ask this plain-chat question. Host review surfaces are not approval evidence. Do not create or update `implementation_plan.md` for this review.

---

### Development Start Authorization

User: `Continue.`

```text
Observed evidence: Foundation is approved through delivery-backlog@BL-004; no development-start authorization is recorded for its scope.
Selected next skill(s): none
Why: Development-start stop applies before scaffolding, installing dependencies, or application edits.
Missing prerequisites: Explicit authorization against delivery-backlog@BL-004 and its first Ready item.
Approval required: Start development for delivery-backlog@BL-004? First item: STORY-001. Expected runnable outcome: a local UI that completes the approved inventory-create flow. Yes / No / Other (type comments directly).
Stop condition: STOP until the separate bound development-start request is answered and persisted with the revision, scope, identity, and exact user evidence.
```

The backlog's approval, a native Process result, or an unrelated plan does not satisfy this stop. `Yes` authorizes only this already approved backlog scope. `No` starts nothing and is not re-asked until the user explicitly asks to start or revise. Comments or feedback entered via `Other` return to planning or the owning prerequisite and do not start coding.

---

### Remediation

User: `Quality is approved with fail and security is approved with block. Continue.`

```text
Observed evidence: Approved quality report verdict fail; approved security review verdict block.
Selected next skill(s): plan-delivery
Why: Blocking verifier verdicts require a traceable remediation backlog item.
Missing prerequisites: One human-approved remediation backlog item.
Approval required: Human approval of the remediation item before implementation.
Stop condition: Dispatch plan-delivery; stop when the remediation item reaches awaiting-approval. After approval use implement-feature, then dispatch both verifiers in parallel.
Specialist output: plan-delivery
<Dispatch the plan-delivery contract to a subagent and verify its artifacts on disk.>
```

---

### Stale VDC/VIS

User: `Implement the UI item using experience-spec@VDC-001#VIS-004, but the current approved spec is VDC-002.`

```text
Observed evidence: Backlog reference experience-spec@VDC-001#VIS-004 conflicts with current approved VDC-002.
Selected next skill(s): design-experience
Why: The UI reference is stale and blocks implementation.
Missing prerequisites: Approved current VIS reference, replanned backlog mapping, and regenerated affected evidence.
Approval required: Human approval after each design, planning, and affected implementation boundary.
Stop condition: Dispatch design-experience; stop at the revised experience specification approval, then execute plan-delivery and affected implement-feature work in order.
Specialist output: design-experience
<Dispatch the design-experience contract to a subagent and verify its artifact on disk.>
```

---

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

---

### Release Route

User: `Quality is approved with pass. Security is approved with pass-with-findings, all nonblocking, and there is no blocker.`

```text
Observed evidence: Approved current quality report verdict pass; approved current security report verdict pass-with-findings; findings nonblocking; no blocker.
Selected next skill(s): prepare-release
Why: Both verifier branches satisfy the release-planning join.
Missing prerequisites: Release candidate ID, version or build ID, and scope summary required by prepare-release.
Approval required: Human approval of the resulting release plan; separate authorization is required outside this suite for any deployment.
Stop condition: Dispatch prepare-release; stop when the release plan reaches awaiting-approval. Do not deploy.
Specialist output: prepare-release
<Dispatch the prepare-release contract to a subagent and verify its artifacts on disk.>
```
