---
name: review
description: Review the current project codebase for quality and security health, and discover high-value feature recommendations.
---

# /review

Review the current workspace codebase and formulate structured domain feature recommendations for capability expansion.

## Execution Steps:
1. Resolve the project root and inspect existing application models, routes, and user journeys.
2. Execute `verify-quality` and `review-security` to establish baseline codebase health and security posture.
3. Execute `discover-product` in **Existing Project Feature Discovery Mode**:
   - Identify missing high-value domain capabilities across user roles (e.g. payment gateway integrations, notifications, rescheduling policies, operational locks, or reporting exports).
   - Formulate structured `FR-*` recommendations with clear business rationale and acceptance signals.
4. Clean up any background processes immediately without requiring user confirmation.
5. Present the findings and feature recommendations with simplified choices (`Yes`, `No`, and `Other` for user typing/comments).
