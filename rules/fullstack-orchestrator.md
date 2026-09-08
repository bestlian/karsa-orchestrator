# Fullstack Orchestrator

This imported rule makes `fullstack-orchestrator` bootstrap mandatory for an in-scope new-application request. Before native planning, coding, or a direct specialist workflow starts, route the request through `fullstack-orchestrator` to resolve the project root, inspect visible lifecycle artifacts, and identify the next enabled specialist skill.

In scope: natural-language requests to create, build, or scaffold a new web app, mobile app, cross-platform app, frontend-and-backend app, or full-stack app, including equivalent phrasing such as a new product, MVP, or blank-slate application.

Out of scope: bug fixes, changes to existing applications, libraries, CLIs, general questions, and isolated pages or prototypes unless the user explicitly requests one as a new application.

Resolve `<project-root>` before artifact inspection or lifecycle routing. An explicit user target path wins. Otherwise use the active workspace only when it is clearly the target application and is not this plugin repository. If that remains ambiguous, ask exactly one location question, `Which project-root path should contain this new application?`, and STOP. Do not write lifecycle artifacts to the plugin installation or repository, or to an unrelated current working directory. Every lifecycle artifact path is project-relative: resolve `artifacts/...` below `<project-root>`.

Routing remains advisory: it does not invoke skills. Preserve specialist prerequisites and joins, require explicit human approval at every phase boundary, and resume only from visible artifacts. Do not assume background execution, self-approval, or cross-chat persistence.
