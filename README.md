# Antigravity Fullstack Skills

Nine skills that guide new applications from discovery to release preparation. The orchestrator selects and runs each specialist in the same agent, pausing for missing information and human approval.

## Install

```bash
agy plugin install https://github.com/bestlian/antigravity-fullstack-skills
```

After installation, send this prompt to Gemini Chat. Use **copy**, not move, to preserve the plugin's source file:

```text
Copy the installed fullstack-orchestrator rule to my global Antigravity rules directory.

Source: ~/.gemini/config/plugins/antigravity-fullstack-skills/rules/fullstack-orchestrator.md
Destination: ~/.gemini/config/rules/fullstack-orchestrator.md

Resolve ~ to my home directory. If the source is missing, stop and report it.
Create the destination directory if needed. I authorize overwriting the destination file.
Preserve the source, copy its contents unchanged, and do not modify other rules or settings.
Compare the source and destination SHA-256 hashes and report the result.
Do not claim automatic activation just because the copy succeeded; I will test in a new session.
```

Back up the destination first if you customized it. Repeat the copy when an update changes the rule. These paths worked in the tested local installation; other hosts or versions may use different paths. Native installation does not provide a documented hook for this global copy.

Check registration with `agy plugin list`, then start a new Antigravity session.

## Use

Describe the application you want:

```text
Build a new web application for managing padel court bookings, rentals, and payments.
```

The first discovery round asks, unless already answered, whether the result is a prototype or production-ready application. `MVP` is a separate optional scope or release label and must map to one of those readiness targets. Discovery separately confirms frontend-only or full-stack architecture, visual direction, staff roles and permissions, payment simulation or live boundary, and stack choice. For a new full-stack application with no stated stack, it offers FastAPI for the backend and React with Vite for the frontend, then confirms that choice once. Answers you already supplied should not be requested again.

If automatic discovery does not work, start explicitly with `/fullstack-orchestrator`. Rule loading and compliance depend on the host; installation alone does not guarantee execution.

To resume, open the target project and ask the agent to continue from its latest artifacts. Artifacts, not chat memory, determine progress.

## Workflow

| Phase | Skill | Result |
| --- | --- | --- |
| Coordinate | `fullstack-orchestrator` | Select and execute the next eligible phase |
| Discover | `discover-product` | Product brief and confirmed delivery scope |
| Design | `design-experience` | UX and visual specification |
| Architect | `define-architecture` | Application blueprint |
| Plan | `plan-delivery` | Delivery backlog |
| Build | `implement-feature` | One Ready story or task per cycle |
| Test | `verify-quality` | Quality report |
| Review | `review-security` | Security report |
| Prepare | `prepare-release` | Release plan, not deployment |

Design and architecture must both be approved before planning. Quality and security must both satisfy their gates and be approved before release preparation. Paired phases run sequentially, not as independent lifecycle agents.

## Important Rules

- **Approve in chat.** Only one Review Record may be active across the lifecycle. It binds a displayed Yes/No/Revision question to the canonical artifact path, content revision, request ID, prompt evidence, and eventual source reply. A direct `Yes` or `No` is valid only for that unchanged current question; `Revision` collects meaningful freeform feedback. No long path command is required. Rejected work stays rejected until the user explicitly asks to revise it.
- **Confirm development separately.** Once the brief, UX, blueprint, and backlog are approved, the agent asks a separate `Start development?` Yes/No/Revision question naming the first item and expected outcome. A `Yes` authorizes only that approved backlog scope and is saved for reuse; a `No` makes no application changes and is not polled again.
- **Build real production-ready applications.** A production-ready full-stack target has substantive `backend/` and `frontend/` deliverables: a runnable API with database integration and a client that consumes it, with start, environment, and applicable test commands. Empty folders or `localStorage` substitutes fail. Approved payment simulation remains simulation, never a live-payment-ready claim.
- **Reconcile evidence.** Before resume, QA, or release, the agent re-reads exact source reports, approvals, technical results, and manifest entries. Tested executable, configuration, and source scope is tied to a stable revision or checksum; governance records do not invalidate evidence. Existing backlogs and manifests hold resume state.
- **Test the actual UI.** The executing agent uses supported browser tooling to click, fill, observe state outcomes, and inspect the console. A host-native `browser_subagent` may collect bounded browser evidence only; it cannot edit, approve, route, or satisfy a join. Screenshots support visual classification only. Missing required browser evidence blocks completion; builds and HTTP 200 are not UI tests.
- **Recommend MCP proportionately.** Native tools come first and no MCP is required to run an app. For justified browser evidence, merge the documented Playwright launcher into project `.agents/mcp_config.json`; do not overwrite existing servers. The optional `agy mcp add --type stdio playwright npx @playwright/mcp@latest` command has no documented project-scope flag, so prefer project config and do not invent `--scope`.
- **Report progress honestly.** A scaffold task may be complete while the application is not ready. Item completion is not whole-application completion. Technical success is not human approval.
- **Keep the gates.** Blocking quality or security findings return through approved remediation and re-verification. The suite does not deploy or self-approve.

## Artifacts

All lifecycle documents, reports, and evidence belong in **`<project-root>/artifacts/`**, never in the plugin directory. The explicit user target path takes priority; if the project root is unclear, the agent asks before proceeding.

Handoffs retain `fullstack-skill-handoff/v1` and project-relative `output_path` values. Detailed approval, testing, visual, and maintainability contracts live in each [skill's `SKILL.md`](skills/).

MCP configuration paths and syntax are documented by [Antigravity](https://antigravity.google/docs/cli/mcp/) and [Playwright MCP](https://github.com/microsoft/playwright-mcp). The suite recommends configuration only; it does not install MCPs or modify global configuration. It requires live runtime QA when the applicable specialist contract calls for it.

## Alternative Installation

**Local checkout:** run these commands from the repository root, then copy the installed rule using the prompt above:

```bash
agy plugin validate .
agy plugin install .
```

**Manual ZIPs:** extract all nine packages from [dist/](dist/) into `.agents/skills/<skill-name>/`. Each package contains only `SKILL.md` and `THIRD_PARTY_NOTICES.md`; it does not install the global rule.

## Changes and Attribution

See [CHANGELOG.md](CHANGELOG.md) for changes and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for attribution.

Selected quality guardrails are adapted from [anti-slop](https://github.com/miqdadbadjuber/anti-slop) v3.2.4, commit `44be68777e96d53d113edad33dbc4ab380f5d054`, under MIT. This project is not affiliated with or endorsed by that project. Preserve the notice in every distributed ZIP.
