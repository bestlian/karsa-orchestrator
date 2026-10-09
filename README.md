# Antigravity Fullstack Skills (KARSA Orchestrator)

A rigorous, zero-guesswork full-stack delivery orchestrator for Google Antigravity. This plugin transforms your AI assistant into an enterprise-grade Project Manager (KARSA) and a team of specialized sub-agents, enforcing strict traceability, 4-layer testing doctrines, anti-slop visual design, and aggressive QA remediation loops.

## 🚀 Features

- **The KARSA Orchestrator:** A disciplined, unyielding PM persona that manages the entire lifecycle from idea to containerized deployment.
- **15-File Architecture Standard:** Enforces a complete, traceable planning suite (`docs/01` through `docs/15`) before a single line of business logic is written.
- **UI/UX Preference Interview:** Acts as an Art Director, explicitly asking for your aesthetic preferences (Vibe, Colors, Typography) before drafting the Visual Direction Contract (VDC).
- **Anti-Slop UI Mandate:** Strictly bans generic "AI Card Soup", uninspired default fonts (Inter/Roboto), and cliché gradients. Enforces bespoke layouts and signature brand elements.
- **Mathematical WCAG AA Contrast Gate:** Eliminates eyeball guessing by running deterministic Python contrast calculations (`contrast-check.py`). Requires >=4.5:1 for normal text and >=3.0:1 for large text.
- **Anti-Slop Code Comment Hygiene:** Forbids AI banner separators (`// =======`), step-by-step workflow narration, empty labels, and decorative emoji. Preserves non-obvious invariants and locking logic.
- **Human-First Copywriting:** Bams empty AI vocabulary (*unlock, elevate, delve, seamless, next-level*), significance inflation, and chatbot conversation residue.
- **Responsive Mobile Reflow Doctrine:** Enforces 3-state reflow, dynamic viewport units (`dvh`), fluid `clamp()` type, and a zero-horizontal-scroll-leak guarantee at 375px.
- **Offline Modern Web Standards (140+ Guides):** Equips sub-agents with offline access to modern baseline web APIs (Popover API, View Transitions, Container Queries, WebMCP, Chrome Built-in AI).
- **4-Layer Testing Doctrine:** Sub-agents must prove code works via (1) Functional AC, (2) Database Fixtures/Dummies, (3) Live API subprocesses, and (4) E2E Browser UI interactions. No mocked databases allowed.
- **UAT & Security Remediation Loop:** Aggressive end-of-sprint testing. Any functional bug or security vulnerability forces the code back to the programmer. Release is blocked until reports are 100% clean.
- **RED CODE (Credential Leaks):** Hardcoded secrets, API keys, or emails immediately trigger a RED CODE blocker, forcing them into `.env` and `.gitignore`.
- **Dynamic Model Optimization:** Automatically routes complex planning/coding tasks to `pro` models, and mechanical terminal/QA tasks to `flash` models for maximum speed and cost-efficiency.
- **Optional DevOps & CI/CD:** Interactively asks to generate Dockerfiles and GitHub Actions pipelines at the end of the release.

## 📦 Installation

To install this plugin globally in your Antigravity environment, you can install it directly from the repository:

```bash
agy plugin install https://github.com/bestlian/karsa-orchestrator.git
```

**For Developers / Local Testing:**
If you want to modify the rules, skills, or agents locally:

```bash
git clone https://github.com/bestlian/karsa-orchestrator.git
cd karsa-orchestrator
agy plugin install .
```

*Note: The installation process automatically mounts all rules, skills, and agents to your global `~/.gemini/config/plugins/` directory.*

## 🤖 Standalone Agent & Usage

KARSA can run both as an ambient development doctrine and as a **Standalone Custom Agent** (`karsa`).

### How to Use KARSA:

1. **Antigravity IDE / Desktop App:**
   - In the chat interface, switch the active agent to **KARSA Orchestrator** in the Agent selector dropdown.
   - Or tag `@karsa` directly in your prompt.
2. **Antigravity CLI (`agy`):**
   - Launch an interactive session directly with the KARSA agent:
     ```bash
     agy --agent karsa
     ```
   - Run a headless one-shot task:
     ```bash
     agy --agent karsa -p "Design and scaffold an e-commerce backend with FastAPI and PostgreSQL"
     ```
3. **Autonomous Execution (`/goal` Mode):**
   - Trigger KARSA with the `/goal` slash command for long-running autonomous project delivery:
     ```text
     /goal Scaffold and implement Sprint 0 for a logistics tracking dashboard.
     ```
   - Provide explicit delegation upfront (e.g., *"Saya serahkan keputusan arsitektur sepenuhnya padamu"*) to let KARSA execute end-to-end through the 7 phases without blocking on every intermediate choice.

## 🧠 Agents Architecture

KARSA operates as a Lead Orchestrator commanding a team of specialized sub-agents:

0. **`karsa` (Lead Orchestrator - Primary Agent)**: Manages the high-level 7-phase delivery pipeline, enforces the 15-document planning suite, and routes tasks to specialized sub-agents.

1. **`contract-manager`**: The Supreme Auditor. Verifies that no features are hallucinated and that every sprint ticket traces back to the approved Product Brief.
2. **`execution-manager`**: The Sprint Cutter. Slices the global backlog into manageable daily increments (`artifacts/increment_manifest.md`).
3. **`execution-strategist`**: The Business Analyst. Drafts detailed Functional Requirements, API Contracts, and Execution Flows.
4. **`scope-mapper`**: The Release Planner. Breaks down the vision into S0, S1, S2 release phases.
5. **`strict-programmer`**: The Coder. Bound by the 4-Layer Doctrine. Refuses to mock databases, writes pessimistic tests, and explicitly reports proof gaps.
6. **`integration-tester`**: The Terminal QA (`flash`). Quickly runs test suites (`pytest`, `cypress`) and feeds terminal output back to the team.
7. **`contract-reviewer`**: The Acceptance Checker (`flash`). Validates output against the Functional Requirements.

## ⚙️ The KARSA Workflow (7-Phase Pipeline)

1. **Phase 1: Discovery & UI Interview:** Decomposes the user's intent, extracts constraints, interviews the user for UI/UX preferences, and drafts the Product Brief (`docs/01`).
2. **Phase 2: Master Planning:** Generates the complete 15-file architecture and UX documentation (including the Anti-Slop Visual Direction Contract).
3. **Phase 3: Traceability Audit & Sprint Formation:** `contract-manager` audits the docs. If 100% clean, KARSA halts to ask for **Master Planning Approval**. Once approved, Sprint 0 is formed.
4. **Phase 4: Environment Scaffold Gate:** Before any business logic is written, `strict-programmer` is forced to initialize the project (install frameworks, linters, base folder structure).
5. **Phase 5: Execution & Testing:** The programmer implements tickets one by one, adhering strictly to the TDD and Anti-Mocking rules, updating the Sprint Manifest gap-table continuously.
6. **Phase 6: UAT & Security Loop:** At the end of the sprint, the UAT Auditor (`verify-quality`) and Security Auditor (`review-security`) test the code. If ANY bug or RED CODE vulnerability is found, KARSA violently routes it back to the programmer.
7. **Phase 7: Release & DevOps Handover:** Once 100% clean, a final `README.md` is generated. KARSA asks if you need CI/CD/Docker generation. Finally, you receive the **Handover Report** to test your robust, enterprise-grade application.

## 📜 License
MIT License. See `LICENSE` for details.
