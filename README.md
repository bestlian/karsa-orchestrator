# Antigravity Fullstack Skills (KARSA Orchestrator)

A rigorous, zero-guesswork full-stack delivery orchestrator for Google Antigravity. This plugin transforms your AI assistant into an enterprise-grade Project Manager (KARSA) and a team of specialized sub-agents, enforcing strict traceability, 4-layer testing doctrines, anti-slop visual design, and aggressive QA remediation loops.

## 🚀 Features

- **The KARSA Orchestrator:** A disciplined, unyielding PM persona that manages the entire lifecycle from idea to containerized deployment.
- **15-File Architecture Standard:** Enforces a complete, traceable planning suite (`docs/01` through `docs/15`) before a single line of business logic is written.
- **UI/UX Preference Interview:** Acts as an Art Director, explicitly asking for your aesthetic preferences (Vibe, Colors, Typography) before drafting the Visual Direction Contract (VDC).
- **Anti-Slop UI Mandate:** Strictly bans generic "AI Card Soup", uninspired default fonts (Inter/Roboto), and cliché gradients. Enforces bespoke layouts and signature brand elements.
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
If you want to modify the rules or agents yourself, clone it first:

```bash
git clone https://github.com/bestlian/karsa-orchestrator.git
cd karsa-orchestrator
agy plugin install .
```

*Note: The installation process automatically mounts all rules, skills, and sub-agents to your global `~/.gemini/config/plugins/` directory.*

## 🧠 Sub-Agents Included

This plugin ships with a pre-configured team of specialized sub-agents:

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
