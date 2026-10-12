# Authoritative Evidence & Reconciliation Specification

This reference details the binding rules for artifact lifecycle state, Review Record management, approval persistence, and evidence invalidation.

---

## 1. The Handoff Contract (`fullstack-skill-handoff/v1`)

Visible artifacts below `<project-root>/artifacts/` and `docs/` and their handoffs are authoritative. Chat memory, LLM summaries, prior routing responses, and `next_skills` are strictly non-authoritative.

- **Schema:** MUST be `fullstack-skill-handoff/v1`.
- **Status Enum:** Lifecycle `status` MUST remain one of `draft | awaiting-approval | approved | rejected | blocked`.
- **Decoupled Approval:** Approval state MUST remain separate from artifact lifecycle status. Artifact status, specialist technical verdict, and explicit human approval are separate facts; one MUST NOT be inferred from another.
- **Advisory Downstream:** `next_skills` is advisory downstream guidance only. It does NOT constitute evidence that a skill was invoked, work ran, or approval was granted.
- **Terminal Verdicts:** `awaiting-approval` is NOT approval. A technical `pass`, `pass-with-findings`, `complete`, or `PASS` is NOT approval.

---

## 2. Review Record Lifecycle & Human Approval Gate

Human approval MUST be explicit and visible in the evidence used for downstream routing.

1. **Artifact Revision Tagging:**
   - Before requesting approval, every specialist artifact MUST label an immutable `Artifact Revision` in its document body (e.g. `@VDC-001`, `@BL-001`).
   - The output path and that exact revision are the approval target.

2. **Review Record State Machine:**
   - A content `Review Record` has an independent status: `pending`, `resolved`, or `superseded`.
   - It is `pending` only while its canonical artifact has handoff status `awaiting-approval`.
   - Persisted fields: `request_id`, canonical `target_path`, immutable `content_revision`, exact `question`, options (`Yes`, `No`, `Other`), prompt evidence, user identity, `source_user_reply`, and decision evidence.

3. **Resolution Actions:**
   - **`Yes`**: Records approval source reply, sets target handoff status to `approved`, sets approval to approved, resolves the record, and advances to next lifecycle stage.
   - **`No`**: Records rejection reply, sets target handoff status to `rejected`, sets approval to rejected, resolves the record, and stops execution. Never rerun automatically after rejection.
   - **`Revision`**: Accepts explicit revision feedback tied to current target. Resolves record as `Revision`, sets artifact to `draft`, and re-routes only to owning specialist.

4. **Substantive Invalidation:**
   - A substantive content change before a terminal decision supersedes the pending Review Record, creates a new Artifact Revision, and resets approval.

---

## 3. Evidence Invalidation & Checksum Re-reading

Before every route, resume, quality gate, security review, or release plan, KARSA reconciles canonical sources rather than trusting summaries:

- Re-read every required source report at its exact path and revision.
- Verify explicit human approval and technical result; compare those facts to the increment manifest and downstream candidate; block on any mismatch.
- Tie code and test evidence to a stable revision or checksum of the tested executable, configuration, and source scope.
- Any change in that tested scope invalidates dependent evidence until the required verification checks run again.
- Persist resume-required scope, source revisions, and unresolved gates only in the existing backlog and increment manifests; never introduce an external database engine for governance state.
