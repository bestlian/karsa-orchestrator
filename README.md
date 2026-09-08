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

The agent should clarify prototype versus full-stack delivery, shared data, authentication, payment integration, and technical preferences before choosing the architecture. Answers you already supplied should not be requested again.

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

- **Approve the correct document.** Feedback must identify its exact path and content revision. Use `RequestFeedback: true` only when the host can bind review to that artifact; otherwise approval is requested in chat. Approval of `implementation_plan.md` does not approve another document. Valid decisions are recorded before continuing; substantive revisions require new approval.
- **Confirm development start.** Once the brief, UX, blueprint, and backlog are approved, the agent asks whether to start development and states the first item and expected outcome. Authorization is saved in the backlog and reused for the same approved scope.
- **Agree on the backend.** Confirmed full-stack work includes the required backend API, persistence, and access boundaries. A frontend prototype, local-only storage, or simulated payment must be explicitly agreed, never silently substituted.
- **Test the actual UI.** Use working native browser tools first, including a bounded browser-testing subagent. Recover missing tooling through supported, permitted installation or configuration; request permission for external, global, or elevated installation. Missing required browser evidence blocks completion. Build success and HTTP 200 are not UI tests.
- **Report progress honestly.** A scaffold task may be complete while the application is not ready. Item completion is not whole-application completion. Technical success is not human approval.
- **Keep the gates.** Blocking quality or security findings return through approved remediation and re-verification. The suite does not deploy or self-approve.

## Artifacts

All lifecycle documents, reports, and evidence belong in **`<project-root>/artifacts/`**, never in the plugin directory. The explicit user target path takes priority; if the project root is unclear, the agent asks before proceeding.

Handoffs retain `fullstack-skill-handoff/v1` and project-relative `output_path` values. Detailed approval, testing, visual, and maintainability contracts live in each [skill's `SKILL.md`](skills/).

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
