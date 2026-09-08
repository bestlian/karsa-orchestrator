# Antigravity Fullstack Skills

This repository is the Antigravity Fullstack Skills orchestration package for building greenfield full-stack applications end to end. `fullstack-orchestrator` is the natural-language control plane. The other eight skills are phase-specific specialists. The flow guides work from idea and discovery through UX, architecture, planning, implementation, QA, security, and release preparation.

## About the Project

`fullstack-orchestrator` reads the visible artifacts and recommends the next best skill. It is a control layer, not a worker. For in-scope requests to create a new application, the plugin rules require bootstrap through the orchestrator before native planning, coding, or direct specialist workflows begin.

It does not run specialist skills directly, does not chain work automatically, does not keep state across chats, does not self-approve, does not create new orchestrator artifacts, does not deploy, and does not replace specialist skill contracts. All skills remain installed as separate directories in the same workspace.

## Bootstrap Scope and Platform Limits

Bootstrap is mandatory for natural-language requests to create, build, or scaffold a new web app, mobile app, cross-platform app, frontend-and-backend app, or full-stack app, including variants such as a new product, MVP, or blank-slate app.

Bootstrap does not apply to bug fixes, changes to an existing application, libraries, CLIs, general questions, or isolated pages or prototypes unless the user explicitly asks for that page or prototype as a new application.

Imported rules are the strongest plugin-level enforcement: a host that follows the imported instructions must perform this bootstrap. The plugin cannot guarantee compliance if the host ignores the imported instructions. This plugin also does not guarantee automatic skill invocation, background execution, or cross-chat state. This suite governs lifecycle and evidence for cross-platform applications; it does not provide platform SDKs, platform code generators, or automatic deployment.

## Lifecycle

The official sequence is `discover-product -> (design-experience + define-architecture) -> plan-delivery -> one-item implement-feature loop -> (verify-quality + review-security) -> prepare-release`.

Core rules:

- `discover-product` starts from visible evidence, then produces a product brief that is ready for human approval.
- `design-experience` and `define-architecture` run in parallel only after the product brief is explicitly approved. They form a join, so both approved outputs must exist before moving on.
- `plan-delivery` runs only after the brief, experience spec, and blueprint are approved.
- `implement-feature` runs one ready item per cycle, not a batch.
- `verify-quality` and `review-security` run in parallel only after all required items and the increment manifest are approved. This is also a join, so both reports must exist and be approved before moving on.
- `prepare-release` may only be chosen after quality and security pass according to the applicable rules.

## Approval and Joins

Every transition to the next phase requires explicit human approval of the upstream artifact used by that phase. Artifact status, technical verdict, PASS gate, `next_skills`, and human approval are separate facts.

- `awaiting-approval` is not approval.
- `PASS`, `pass`, `pass-with-findings`, `complete`, or a favorable `technical_verdict` does not mean human approval has been granted.
- `next_skills` is only downstream guidance. It is not evidence that a skill was called, work has started, or approval was given.
- When two skills are run in parallel, both branches must finish and be approved before the join opens.

If `verify-quality` fails or returns `conditional`, or `review-security` returns `block` with fixable findings, the path is remediation. Create one traceable remediation item, ask for human approval, run `implement-feature` for that single item, then repeat both verifications until release requirements are met.

## Handoff and Artifacts

Use `fullstack-skill-handoff/v1` for handoff between stages. This structure stays in place as is.

Valid statuses:

- `draft`
- `awaiting-approval`
- `approved`
- `rejected`
- `blocked`

`implement-feature` uses `technical_verdict: complete | partial | blocked` in the work report. `verify-quality` and `review-security` have their own technical verdicts, separate from artifact status.

Canonical visual references always use the form `experience-spec@VDC-NNN#VIS-NNN`. Example: `experience-spec@VDC-001#VIS-001`.

Resumes must start from the visible artifacts, not from chat memory. If you move to another chat, bring the latest artifacts and the latest handoff, then continue from there. Conversation memory is not an authoritative source.

### Project Artifact Root

All `artifacts/...` paths are relative to `<project-root>` and must be resolved as `<project-root>/artifacts/...`. An explicit user target path wins. If there is no explicit path, use the active workspace only when that workspace is clearly the target application and not this plugin repository. If the location is still ambiguous, the orchestrator asks exactly one location question and then stops: `Which project-root path should contain this new application?`

The `output_path` value in `fullstack-skill-handoff/v1` remains project-relative to preserve the existing schema. Lifecycle artifacts, manifests, reports, and proofs must not be written to the plugin installation or repository, or to an unrelated current working directory.

## Readability and Maintainability

Readability means the source code is easier to understand and change for the developer who receives and maintains the generated application.

- Architecture defines module responsibilities, public contracts, and dependency direction.
- Planning turns those decisions into acceptance criteria, tests, quality gates, and required proof.
- Implementation uses TDD, repository conventions, evidence-backed modularity, and Design And Maintainability evidence.
- Quality verifies independently and blocks material failures or unresolved required evidence.
- Repository-configured checks take priority. Optional tooling that is not available is recorded as an evidence gap, not fabricated as a pass and not treated as an automatic installation requirement.
- There is no universal line limit, no universal framework mandate, no universal SOLID policy, and no subjective style preference used as a release gate.

## Nine Packages

1. `fullstack-orchestrator`, natural-language control plane
2. `discover-product`
3. `design-experience`
4. `define-architecture`
5. `plan-delivery`
6. `implement-feature`
7. `verify-quality`
8. `review-security`
9. `prepare-release`

## Installation and Package Format

### Antigravity Plugin (Recommended)

Install the full suite directly from the repository:

```bash
agy plugin install https://github.com/bestlian/antigravity-fullstack-skills
```

Verify that the plugin is registered:

```bash
agy plugin list
```

This plugin registers all nine skills from `skills/` and the orchestrator rule from `rules/fullstack-orchestrator.md`. Each skill is still selected or activated explicitly; plugin installation does not run skills automatically.

### Manual ZIPs (Fallback)

Each ZIP is a portable distribution artifact. Each ZIP must contain exactly one skill.

Steps:

1. Extract each package to `.agents/skills/<skill-name>/`.
2. After extraction, each skill directory must have `SKILL.md` and `THIRD_PARTY_NOTICES.md` in its root.
3. Install all nine skill directories in the same Antigravity workspace.
4. Existing skill names remain unchanged.

### Build and Validate Packages

Run the following commands from the repository root after changing a skill or notice:

```powershell
.\scripts\build-dist.ps1
.\scripts\test-package-parity.ps1
agy plugin validate .
```

The PowerShell validation checks the nine expected packages, the two exact root archive files, and byte-for-byte parity between each source `SKILL.md` or `THIRD_PARTY_NOTICES.md` file and the ZIP entry. This validation intentionally does not test routing prose content; routing semantics are an instruction contract that requires manual review and acceptance.

## How to Use

Natural-language start example:

```text
Build a new inventory app, use the visible artifacts.
```

Resume example:

```text
Continue from the approved product brief, then check the latest handoff for the design and architecture branches.
```

Optional slash command example:

```text
/fullstack-orchestrator
/discover-product
/design-experience
/define-architecture
/plan-delivery
/implement-feature
/verify-quality
/review-security
/prepare-release
```

## Visual Contract

- `VDC-NNN` is the approved Visual Direction Contract revision in `experience-spec.md`.
- `VIS-NNN` is the numbered visual decision within that revision.
- `direction_mode` can be `restrained` or `expressive`, chosen for the product goal, not aesthetic taste.
- Visual references are used only as provenance and comparison. They do not grant permission to copy a brand, protected assets, or material without the proper license and approvals.
- Real-browser visual validation uses the approved width, or the 375, 768, and 1280 CSS px fallback when the product does not define one. Screenshots alone are not enough.
- Generic defaults written in the contract, a missing signature moment, a verified mismatch, or missing required proof will fail quality and must go through remediation in the same lifecycle.

## Anti-Slop Curation

Anti-slop only acts as an additional quality guardrail. Anti-slop is not the orchestration engine, not the main framework of this project, and is not imported in full.

Only the upstream curation that helps reduce generic or template-like application output, visual sameness, fabricated evidence, fake interaction, and unverified quality claims is used.

The pinned upstream source is anti-slop `v3.2.4`, commit `44be68777e96d53d113edad33dbc4ab380f5d054`, MIT licensed. The upstream source reference is [anti-slop](https://github.com/miqdadbadjuber/anti-slop). This project is not affiliated with, endorsed by, or representative of the upstream project.

The principles used across phases are:

- claims must be traceable to real evidence, decisions, or artifacts;
- if real data is not available yet, write `[REAL DATA NEEDED]` and say what is missing;
- do not fill gaps with unproven numbers, quotes, results, or statuses;
- keep evidence in artifacts, not in narrative.

`THIRD_PARTY_NOTICES.md` must remain in the root of every distributed ZIP. That notice must not be removed when a package is moved, copied, or repackaged.
