# Changelog

This project follows Keep a Changelog.

## [1.0.0] - 2026-09-09

### Added
- Slash Commands `/audit` and `/review`: added native Antigravity commands for instant codebase auditing and feature recommendation workflows without writing long prompts.
- Existing Project Review & Feature Discovery: enables the plugin to natively handle existing projects for comprehensive code quality, maintainability, architectural, and security audits (`verify-quality` + `review-security`), as well as domain feature recommendations (`discover-product`), without forcing re-scaffolding of existing code.
- Mandatory Background Process Cleanup: enforces that all background processes (dev servers, uvicorn/node daemon tasks, background test runners, or browser subagents) started during development, feature implementation, testing, or quality verification MUST be terminated immediately when development, testing, verification, or release handoff concludes, without requiring user confirmation. Ensures ports are completely released for user convenience without socket binding errors (such as Windows Error 10013).
- Simplified Confirmation & Review Options: streamlines all interactive confirmation and review prompts (`ask_question`, Chat Review Protocol, Development Start Authorization, and Discovery proposals) to strictly `Yes`, `No`, and `Other` (user typing for comments/feedback). When using `ask_question`, options are simplified to `["Yes", "No"]`, relying on the default write-in 'Other' box for user comments and revision feedback.
- Strict Anti-Slop & Anti-UI Sameness hard gates: restores the true purpose of anti-slop by outlawing AI design monoculture (uniform card soup, uncritical Inter/system font fallback, unmotivated purple/cyan gradients, neon glow borders, and cookie-cutter 4-metric dashboard templates); mandates intentional type pairings, bespoke semantic color identity, content-driven layout grammar (flat divided rows, split panes, asymmetrical grids), and a signature design moment in `design-experience`, with violations enforced as release-blocking Major defects in `verify-quality`.
- Natural conversational discovery & zero-guesswork principle: requirements gathering during discovery is natural and conversational; strictly prohibits the model from guessing or fabricating business rules, pricing, or operating policies unless the user explicitly delegates decisions.
- All-stories-upfront backlog review: mandates that all user stories across all epics and release slices must be fully articulated and formed upfront in `delivery-backlog.md`, allowing the human user to review and approve the complete delivery roadmap before development authorization (`AUTH-DEV`) or coding begins.
- Streamlined low-bureaucracy implementation: eliminates micro-approval fatigue by treating per-story implementation reports and intermediate slice manifests as automated developer execution records under the human-granted `AUTH-DEV`; consolidates human review touchpoints to meaningful milestone boundaries (working slice demo, quality/security verification, and release plan).
- Platform-agnostic & domain-neutral architecture covering Web (SPA, SSR), Mobile (iOS/Android via React Native/Expo, Flutter), and multi-platform applications.
- Anti-monolith page stacking rules prohibiting single-page endless scroll sprawl for disparate user journeys; applications must maintain structured navigation views (web tabs/routes/drawers, mobile bottom navigation/screen stacks/sheets).
- Core journey vs. add-on separation requiring non-blocking quick-checkout for primary services or products and opt-in drawer/modal/tab/sheet flows for secondary add-ons.
- Privileged staff operational surface isolation requiring dedicated views or portals separated from customer-facing discovery and transaction views.
- Delivery Gate requirement in release preparation enforcing a user-facing README.md at project root with quickstart, credentials, and test documentation.
- Full-request obligation ledgers that map original requirements and accepted proposals to thin stories, slices, evidence, and explicit scope-reduction decisions; slice release approval now re-evaluates remaining authorized work instead of ending the request.
- Production-ready User/Staff JWT baseline covering fixed-algorithm signature verification, expiry, active subject and role lookup, Argon2/bcrypt, secure first-Staff bootstrap, ownership/RBAC endpoint matrix, Bearer/session threat model, and negative token tests.
- Required interval, concurrency, transaction, settlement audit, and financial-total verification for reservation, inventory, order, and payment scope, using isolated repeatable fixtures.
- Evidence records for command, working directory, exit code, raw output, tested revision, and owned bounded test-process cleanup, plus explicit backend/frontend maintainability checks.
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
- An application obligation ledger that maps every original requirement and accepted proposal to executable items, release slices, and verified completion evidence.
- Secure authentication and manual-settlement architecture requirements, including generated local bootstrap credentials, modern password hashing, protected ownership and staff operations, and settlement auditability.
- Reservation interval, simultaneous-connection, inventory, ownership, and idempotency test contracts, plus time-bounded test-server cleanup requirements.

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
- Source-backed QA now requires command, working directory, exit code, raw-output path, tested source identity, captured browser artifacts, and process-cleanup evidence; absent project-native lint is reported as a maintainability gap.
