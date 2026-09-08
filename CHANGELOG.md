# Changelog

This project follows Keep a Changelog.

## [Unreleased]

### Added
- Natural-language requests to create new web, mobile, cross-platform, frontend-and-backend, or full-stack apps now bootstrap through `fullstack-orchestrator` before planning or coding begins.
- Deterministic `<project-root>` resolution and `<project-root>/artifacts/` placement for lifecycle files, with one location question and a stop when the root is still ambiguous.
- The README is now fully English, including its examples and usage notes.
- Documented GitHub installation followed by a Gemini Chat prompt to copy the global orchestrator rule, including overwrite authorization, source preservation, hash verification, and a host-discovery caveat.
- Artifact-bound approval evidence, including exact path-and-revision validation and a chat fallback when host feedback cannot target the artifact.
- An explicit development-start authorization after all four Foundation artifacts are approved, persisted in the approved backlog body for its revision and scope.
- Early delivery-shape discovery for prototype versus full-stack work, shared data, auth, payment, stack, and deployment constraints.
- Required real-browser UI evidence and supported browser-tool recovery rules that distinguish it from optional static checks.
- Separate readiness target (`prototype` or `production-ready`) from architecture shape (`frontend-only` or `full-stack`), visual direction, and stack decision during discovery; `MVP` is an optional scope or release label mapped to an explicit readiness target.
- Production-ready topology and proportional readiness gates for substantive backend/frontend integration, durable data, staff authorization, operations, and audit recommendations.
- Canonical review records with independent `pending`, `resolved`, and `superseded` lifecycle states, terminal decisions with internal source-message evidence, and honest host UI limits.
- Per-project MCP preflight guidance with official Antigravity and Playwright MCP sources, project configuration, verified CLI syntax, scope caveats, and least-privilege recommendations.
- Chat-only lifecycle approval with one canonical, request-bound Yes/No/Revision Review Record at a time, including freeform revision feedback, stale-reply protection, and separate sequential reviews for independent artifacts.
- A confirmed default offer for new unspecified full-stack work: FastAPI backend with React and Vite frontend, while preserving explicit and existing project stacks and leaving database choice unassigned.
- Sequential proposal-based discovery: one domain-informed recommendation at a time, exact Yes/No/Revision/custom response handling, persisted decision evidence, and no ambiguous or batched Yes approvals.
- Host-verified project-root handling that requires an absolute active registered or mounted directory, reports the verification source, and stops rather than substituting a scratch, product-name, or unseen shell directory.

### Changed
- All eight specialist contracts now inherit the same artifact-root contract, while their relative `fullstack-skill-handoff/v1` `output_path` values stay unchanged.
- Routing now emits its six-field summary and then loads and executes the selected specialist inline in the same agent. It does not stop merely for skill selection.
- Paired lifecycle routes execute sequentially in the same agent while their approval joins remain unchanged; lifecycle work is not delegated, while a host-native bounded `browser_subagent` may collect required UI evidence without editing, approving, routing, or joining.
- UI implementation and quality contracts now require real click/fill interactions, state outcomes, console evidence, authorization negatives, dedicated test data, and starter-screen and entrypoint evidence rather than treating builds, screenshots, or HTTP success as UI proof.
- Resume, QA, security review, and release planning now reconcile exact approved report revisions and technical results against manifests, with source-revision/checksum invalidation only for executable, configuration, and source changes.

### Fixed
- `artifacts/...` paths are now consistently resolved under `<project-root>`, and lifecycle output stays out of the plugin installation and unrelated working directories.
- All nine ZIP distributions were refreshed, and each one still preserves `SKILL.md` and `THIRD_PARTY_NOTICES.md` parity.
- `next_skills` is consistently documented as advisory handoff data rather than evidence that a skill ran, work started, or approval was granted.
- Contracts now require revision-bound decisions, explicit start authorization, and correct item/slice/application scope before downstream work or release claims proceed.
- Removed unsupported review metadata guidance. Canonical artifacts are written normally; host-native review presentation is optional and cannot become an authoritative proxy.
- Backlog approval and development authorization are now separate Yes/No/Revision decisions; a rejected authorization never starts, scaffolds, installs, or edits an application until the user explicitly requests it.
- Local payment discovery now recommends authenticated staff-recorded manual or cash settlement when no gateway configuration exists; fake paid QR codes and simulated gateways cannot support a live-paid claim.
