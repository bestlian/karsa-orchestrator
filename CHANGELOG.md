# Changelog

This project follows Keep a Changelog.

## [Unreleased]

### Added
- Natural-language requests to create new web, mobile, cross-platform, frontend-and-backend, or full-stack apps now bootstrap through `fullstack-orchestrator` before planning or coding begins.
- Deterministic `<project-root>` resolution and `<project-root>/artifacts/` placement for lifecycle files, with one location question and a stop when the root is still ambiguous.
- The README is now fully English, including its examples and usage notes.
- Documented GitHub installation followed by a Gemini Chat prompt to copy the global orchestrator rule, including overwrite authorization, source preservation, hash verification, and a host-discovery caveat.

### Changed
- All eight specialist contracts now inherit the same artifact-root contract, while their relative `fullstack-skill-handoff/v1` `output_path` values stay unchanged.
- Routing now emits its six-field summary and then loads and executes the selected specialist inline in the same agent. It does not stop merely for skill selection.
- Paired lifecycle routes execute sequentially in the same agent while their approval joins remain unchanged; no concurrent or background subagents are implied.

### Fixed
- `artifacts/...` paths are now consistently resolved under `<project-root>`, and lifecycle output stays out of the plugin installation and unrelated working directories.
- All nine ZIP distributions were refreshed, and each one still preserves `SKILL.md` and `THIRD_PARTY_NOTICES.md` parity.
- `next_skills` is consistently documented as advisory handoff data rather than evidence that a skill ran, work started, or approval was granted.
