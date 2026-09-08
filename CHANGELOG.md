# Changelog

This project follows Keep a Changelog.

## [Unreleased]

### Added
- Natural-language requests to create new web, mobile, cross-platform, frontend-and-backend, or full-stack apps now bootstrap through `fullstack-orchestrator` before planning or coding begins.
- Deterministic `<project-root>` resolution and `<project-root>/artifacts/` placement for lifecycle files, with one location question and a stop when the root is still ambiguous.
- The README is now fully English, including its examples and usage notes.

### Changed
- All eight specialist contracts now inherit the same artifact-root contract, while their relative `fullstack-skill-handoff/v1` `output_path` values stay unchanged.
- Routing remains advisory and still depends on the host honoring the imported rules.

### Fixed
- `artifacts/...` paths are now consistently resolved under `<project-root>`, and lifecycle output stays out of the plugin installation and unrelated working directories.
- All nine ZIP distributions were refreshed, and each one still preserves `SKILL.md` and `THIRD_PARTY_NOTICES.md` parity.
