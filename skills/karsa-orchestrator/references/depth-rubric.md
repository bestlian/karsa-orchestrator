# Contractual Depth & Anti-Stub Rubric (Zero-Placeholder Rule)

Used by `delivery-planner` and the lead when auditing `docs/01` to `docs/15`, and by any agent writing those documents. Load this file when auditing or when a dispatch brief lists it in `inputs`.

Every documentation file created in `docs/` is a binding engineering contract, NOT an outline, summary, or draft stub. 
1. **Zero-Placeholder Constraint:**
   - Writing placeholder statements such as "akan diisi seiring project berjalan", "saat ini kosong", "TBD", or "N/A" without complete technical specification is strictly FORBIDDEN.
   - Any document containing such placeholder evasions or possessing fewer than 30 substantive lines is classified as an **INCOMPLETE STUB** and causes the Traceability Audit to immediately fail with a hard **BLOCKER**.
2. **Minimum Semantic Depth Rubrics:**
   - **`04_functional_requirements.md`**: Each requirement MUST define: Actor, Trigger, Pre-conditions, Gherkin acceptance criteria (`Given - When - Then`), input validation rules, and error conditions.
   - **`05_domain_and_business_rules.md`**: MUST contain canonical conventions (UUIDs, UTC timestamps, currency/integers), complete Entity schema tables with field types and constraints, mathematical invariants, full State Machine transition matrices (`Current State` x `Event` -> `Next State` + Side Effects), and explicit concurrency locking policies (pessimistic row-locking or optimistic versioning).
   - **`06_api_contract.md`**: MUST NOT be a bare route list. MUST detail for EVERY endpoint: Method, URL, Auth/Role boundary, full Request JSON Schema with field types and validations, full 200/201 Response JSON Schema, and exhaustive Error Status Codes with structured error payload schemas.
   - **`09_architecture_operations.md`**: MUST include component topology, database migration and connection management, full environment variables dictionary, CORS policies, and process isolation.
   - **`10_security_privacy.md`**: MUST define auth lifecycle (JWT claims, expiration, refresh), password hashing algorithms and cost factors (Bcrypt/Argon2 with byte limits), endpoint RBAC permission matrix, and Anti-RED-CODE boundary.
   - **`11_quality_metrics_release.md`**: MUST define concrete numerical coverage targets (e.g. >=80% total, 100% domain state machine), performance budgets (API latency p95 < 200ms, frontend FCP/LCP), and Anti-Mocking real-database testing policy.
   - **`12_insight_resolution_plan.md`**: MUST document actual architectural trade-offs (e.g., chosen database and framework vs discarded alternatives), known domain failure scenarios, and their explicit technical resolutions. Placeholder text is forbidden.
   - **`14_source_traceability.md`**: MUST contain an exhaustive 4-column traceability matrix linking `PRD Requirement ID` -> `Backlog Story ID` -> `Code Unit (File/Class/Function)` -> `Automated Test Case`.
   - **`15_execution_flow.md`**: MUST define the target execution loop diagram, state verification criteria, gated sequence (Pre-conditions, Actions, Post-conditions), and rollback/failure mitigation procedures.
