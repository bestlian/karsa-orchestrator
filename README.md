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

Before discovery, the host must expose the actual active registered or mounted project directory. The first routing summary names that verified absolute root and its verification source. An explicit path must match it; the plugin does not infer a shell cwd, bind a CLI workspace, or replace it with a scratch or product-name folder. If the host does not expose a root or reports a conflict, it asks only for root resolution and writes nothing.

Discovery presents one concrete recommendation at a time with `Yes`, `No`, `Revision`, or custom freeform response. A bare `Yes` approves only the exact displayed proposal, never an unmentioned alternative or a later decision. For an unspecified app, it first offers one prompt-specific target, such as a production-ready full-stack application, then separately proposes only missing material choices: one least-privileged staff/customer access model, an existing or FastAPI plus React/Vite stack, suitable persistence, payments, and remaining scope. For an explicitly local single-process deployment, SQLite with migrations, constraints, and persistence tests is a recommendation; shared or scaled use instead receives one proportionate PostgreSQL proposal, or MySQL only when prompt evidence favors it. With no gateway credentials, it recommends authenticated staff record manual or cash settlements rather than a fake paid QR or simulated live gateway. A local production-ready scope is not an internet-deployment claim. `MVP` remains a separate optional scope or release label mapped to an explicit readiness target.

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

- **Approve in chat.** Only one Review Record may be active across the lifecycle. It binds a displayed Yes/No/Revision question to the canonical artifact path, content revision, request ID, prompt evidence, and eventual source reply. A direct `Yes` or `No` is valid only for that unchanged current question; `Revision` collects meaningful freeform feedback. Discovery proposals are earlier input decisions, not artifact approval or development authorization. No long path command is required. Rejected work stays rejected until the user explicitly asks to revise it.
- **Confirm development separately.** Once the brief, UX, blueprint, and backlog are approved, the agent asks a separate `Start development?` Yes/No/Revision question naming the first item and expected outcome. A `Yes` authorizes only that approved backlog scope and is saved for reuse; a `No` makes no application changes and is not polled again.
- **Complete the accepted request.** The approved backlog keeps a Full-Request Obligation Ledger mapping every original requirement and accepted proposal to thin stories, slices, and evidence. Approval of an item, manifest, verifier, or slice release plan never defers another required obligation. After a released slice, the agent automatically re-evaluates the next Ready item under the existing authorization, or routes to planning repair if required work has no Ready item. It reports delivered and remaining scope and never says application-ready while required scope remains.
- **Protect authenticated full-stack work.** Production-ready User/Staff applications require secure JWT verification, Argon2 or bcrypt passwords, environment-backed production secrets without fallbacks, secure first-Staff bootstrap, server-side active-role and ownership checks, and public registration that cannot assign Staff. Only approved catalog, login, and registration paths may be public; protected frontend calls use the documented Bearer/session/logout model. HTTPS is required for production deployment planning, not deployed by this suite.
- **Build real production-ready applications.** A production-ready full-stack target has substantive `backend/` and `frontend/` deliverables: a runnable API with database integration and a client that consumes it, with start, environment, and applicable test commands. Empty folders or `localStorage` substitutes fail. Approved payment simulation remains simulation, never a live-payment-ready claim.
- **Reconcile evidence.** Before resume, QA, or release, the agent re-reads exact source reports, approvals, technical results, and manifest entries. Tested executable, configuration, and source scope is tied to a stable revision or checksum; governance records do not invalidate evidence. Existing backlogs and manifests hold resume state.
- **Test the actual UI.** The executing agent uses supported browser tooling to click, fill, observe state outcomes, and inspect the console. A host-native `browser_subagent` may collect bounded browser evidence only; it cannot edit, approve, route, or satisfy a join. Screenshots support visual classification only. Missing required browser evidence blocks completion; builds and HTTP 200 are not UI tests.
- **Keep verification bounded.** Test evidence records command, working directory, exit code, raw output artifact, and tested revision. Any temporary test server has a bounded startup/test deadline, recorded owned PID and port, and cleanup result on every exit path. The suite uses project-local dependencies, never broad process kills, global installs, `--no-sandbox`, or fabricated browser passes.
- **Recommend MCP proportionately.** Native tools come first and no MCP is required to run an app. For justified browser evidence, merge the documented Playwright launcher into project `.agents/mcp_config.json`; do not overwrite existing servers. The optional `agy mcp add --type stdio playwright npx @playwright/mcp@latest` command has no documented project-scope flag, so prefer project config and do not invent `--scope`.
- **Report progress honestly.** A scaffold task may be complete while the application is not ready. Item completion is not whole-application completion. Technical success is not human approval.
- **Finish the authorized scope.** The backlog maintains an obligation ledger for every original requirement and accepted proposal. A slice or release-plan approval does not waive pending work; the router advances one eligible item at a time or repairs planning when no required item is Ready. Only a specific human out-of-scope decision can waive a named requirement.
- **Require reproducible evidence.** Test records name command, working directory, exit code, raw-output path, and tested source identity. Browser claims require captured actions, console results, and screenshot artifacts. Test servers are time-bounded and cleaned up unless the user explicitly asks to leave one running.
- **Keep the gates.** Blocking quality or security findings return through approved remediation and re-verification. The suite does not deploy or self-approve.

## Artifacts

All lifecycle documents, reports, and evidence belong in **`<project-root>/artifacts/`**, never in the plugin directory. The explicit user target path takes priority only after it matches the host-visible registered project root; if the host root is unclear or conflicts, the agent asks before proceeding and does not create a substitute directory.

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
