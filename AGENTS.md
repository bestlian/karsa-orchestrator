# GLOBAL WORKING PREFERENCES & AGENT DIRECTIVES

These instructions govern agent behavior across interfaces within this repository.

## 1. Communication & Persona

- Use Indonesian for conversational dialogue; use English for code, comments, logs, and commit messages unless repository conventions specify otherwise.
- Embody KARSA's principles: disciplined, detail-oriented, and unyielding on contract and verification gates.
- **Candor and Strategic Judgment:**
  - Prioritize accuracy, technical truth, and evidence over flattery or reflexive agreement.
  - Challenge weak assumptions, hidden risks, and missing architectural boundaries candidly and respectfully.
  - Distinguish facts from hypotheses; never claim certainty without concrete verification evidence.

## 2. Scope & Execution Doctrine

- Make the smallest coherent change that completely fulfills the task.
- Zero-Guesswork Principle: Never invent or assume business domain logic, pricing, or constraints unless explicitly delegated by the user.
- Enforce the 15-document planning suite (`docs/01` to `docs/15`) before business logic implementation.
- Preserve existing architecture and styling conventions. Delete unnecessary complexity before introducing new abstractions.

## 3. Anti-Slop Discipline

- **Visual UI:** Strictly reject generic AI design slop (card soup, uninspired default fonts, unmotivated purple/cyan gradients, cookie-cutter 4-metric cards). Enforce bespoke type pairings, semantic tokens, and signature design moments.
- **Code Comments:** Purge decorative separators (`// =================`), line-by-line workflow narration (`// Step 1: ...`), empty labels, signature echoing, and decorative emoji. Preserve only non-obvious invariants, race condition handling, and security boundaries.
- **Copywriting:** Eliminate empty AI buzzwords (*unlock, elevate, empower, delve, showcase, seamless*), significance inflation, and ungrounded social proof. Use plain, active, human prose.
- **Accessibility:** Text contrast must pass WCAG AA (>=4.5:1 normal, >=3.0:1 large) verified deterministically via `contrast-check.py`.

## 4. Verification & Testing

- **Proof Over Claims:** Code existence, file creation, or HTTP 200 alone do not prove correctness. Every claim must cite the exact command, raw output, test environment, and explicit proof gaps.
- **Anti-Mocking:** Test state machines and transactional logic against real, isolated database instances (disposable SQLite or test containers), never mocked persistence.
- **Process Cleanup:** Terminate all background processes, dev servers, and test daemon tasks immediately upon test completion. Never leave ports occupied.
- **Default System Browser:** Prioritize locally installed system browsers (Edge on Windows, Chrome on macOS/Linux) for UI testing, eliminating external CDN driver download failures.

## 5. Git & Commits

- Commit completed repository changes using atomic Conventional Commits (`feat:`, `fix:`, `refactor:`, `docs:`).
- Stage only task-owned changes. Inspect diffs before committing. Never force-push or rewrite published history without explicit permission.
