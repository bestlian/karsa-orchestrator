# Document Map

Read when creating a blueprint or expanding its coverage. The canonical seven areas
separate concerns while keeping research and decisions discoverable.

## Size to the request

- **Compact:** a linked `INDEX.md`, foundation brief, assumption register, product
  concept, prioritized questions, and research tracker can be enough. Create other
  files only when they answer a concrete need; note deferred areas in the index.
  Keep each brief short, cover each unresolved point once, and link to its canonical
  explanation instead of repeating caveats across documents.
- **Full scaffold:** cover all seven areas with the topic files below. Topic counts
  are flexible; add specialized product documents only when the concept needs them.
- **Existing project:** use the current organization and document where each
  canonical record lives. Do not rename paths or IDs just to match this map.

## Topic inventory

| Area | Suggested files | Content that earns its place |
| --- | --- | --- |
| `00_foundation/` | `01_vision.md`, `02_problem_statement.md`, `03_target_users.md`, `04_value_proposition.md` | Purpose, observed pain versus hypothesis, target segments and jobs, intended value and alternatives |
| `00_foundation/` | `05_assumptions.md`, `06_success_metrics.md`, `07_risks.md`, `08_open_questions.md` | Traceable hypotheses and model inputs; metric definition, unit, baseline and target if known; risks with impact, mitigation and owner; prioritized validation questions |
| `10_market/` | `01_market_overview.md`, `02_competitor_analysis.md`, `03_market_size.md` | Relevant landscape and substitutes, comparison criteria, sizing method and inputs if market sizing is useful |
| `20_product/` | `01_core_concept.md`, `02_user_journey.md`, `03_features_mvp.md`, `04_features_backlog.md` | Product boundary, journey including failure paths, prioritized MVP with rationale, deferred capabilities |
| `20_product/` | `05_<topic>.md`, `06_<topic>.md` when needed | Project-specific mechanics or UX questions that merit a separate deep dive |
| `30_business/` | `01_revenue_model.md`, `02_business_process.md`, `03_unit_economics.md`, `04_gtm_strategy.md`, `05_partnerships.md` | Revenue or internal value model, actors and process, unit contribution, acquisition/adoption experiments, partner requirements |
| `40_operations/` | `01_tech_stack.md`, `02_legal_compliance.md`, `03_operations_playbook.md`, `04_roadmap.md` | Technical constraints and options, jurisdiction-specific questions, necessary operating responsibilities, milestones and dependencies |
| `50_finance/` | `01_financial_model.md`, `02_funding_strategy.md` | Explicit model inputs, scenarios and cash timing; budget or funding needs only where relevant |
| `90_research/` | `README.md`, `open_questions_tracker.csv`, decision notes | Research workflow, question lifecycle, accepted and superseded decisions linked from the index |

For an internal tool, business value can mean time saved, service quality, or adoption.
Do not manufacture a public market, subscription price, or funding round. For an
early commercial idea, a financing question can remain open rather than becoming
an invented three-year forecast. Technical constraints are documentation, not an
instruction to write implementation code.

Add research subfolders such as `interviews/`, `surveys/`, `screenshots/`, or
`raw_data/` when collecting those materials. Link sanitized findings to their
supporting data without copying sensitive records into public project documents.

## Use the templates

| Asset | Destination and adaptation |
| --- | --- |
| [INDEX](../assets/INDEX.md) | Project root; list actual files, accepted decisions, deferred areas, and next validation action |
| [Document](../assets/document.md) | Topic files; replace generic headings with the topic's useful questions |
| [Assumptions](../assets/assumptions.md) | Default `00_foundation/05_assumptions.md`; add only project-relevant entries |
| [Decision](../assets/decision.md) | Default `90_research/<decision-slug>.md`; distinguish acceptance from evidence |
| [Research](../assets/research.md) | Default `90_research/README.md`; adapt the research actions and evidence locations |
| [Tracker](../assets/open_questions_tracker.csv) | Default `90_research/open_questions_tracker.csv`; retain the schema and use a CSV writer for quoted values |
| [AGENTS](../assets/AGENTS.md) | Root only when useful for future sessions; merge relevant guidance into existing instructions |

`INDEX.md` explains where to read and what is current. `AGENTS.md` explains how to
work here. Neither should copy the financial model, all assumptions, a full commit
history, or a speculative user profile.
