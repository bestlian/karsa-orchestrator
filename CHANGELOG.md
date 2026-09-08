# Changelog

This project follows Keep a Changelog.

## [Unreleased]

### Added
- Natural-language requests to create new web, mobile, cross-platform, frontend-and-backend, or full-stack apps now bootstrap through `fullstack-orchestrator` before planning or coding begins.
- Deterministic `<project-root>` resolution and `<project-root>/artifacts/` placement for lifecycle files, with one location question and a stop when the root is still ambiguous.
- The README is now fully English, including its examples and usage notes.
- Documented GitHub installation followed by a Gemini Chat prompt to copy the global orchestrator rule, including overwrite authorization, source preservation, hash verification, and a host-discovery caveat.
- Artifact-bound approval evidence, including exact path-and-revision validation, host-specific `RequestFeedback` guidance, and a chat fallback when host feedback cannot target the artifact.
- An explicit development-start authorization after all four Foundation artifacts are approved, persisted in the approved backlog body for its revision and scope.
- Early delivery-shape discovery for prototype versus full-stack work, shared data, auth, payment, stack, and deployment constraints.
- Required real-browser UI evidence and supported browser-tool recovery rules that distinguish it from optional static checks.

### Changed
- All eight specialist contracts now inherit the same artifact-root contract, while their relative `fullstack-skill-handoff/v1` `output_path` values stay unchanged.
- Routing now emits its six-field summary and then loads and executes the selected specialist inline in the same agent. It does not stop merely for skill selection.
- Paired lifecycle routes execute sequentially in the same agent while their approval joins remain unchanged; lifecycle work is not delegated, while a host-provided bounded browser-testing tool may be used for required UI evidence.
- UI implementation and quality contracts now require run URL, viewport, interaction outcome, console, starter-screen, and entrypoint evidence rather than treating builds or HTTP success as UI proof.

### Fixed
- `artifacts/...` paths are now consistently resolved under `<project-root>`, and lifecycle output stays out of the plugin installation and unrelated working directories.
- All nine ZIP distributions were refreshed, and each one still preserves `SKILL.md` and `THIRD_PARTY_NOTICES.md` parity.
- `next_skills` is consistently documented as advisory handoff data rather than evidence that a skill ran, work started, or approval was granted.
- Contracts now require revision-bound decisions, explicit start authorization, and correct item/slice/application scope before downstream work or release claims proceed.
