# Decisions and Consistency

Read when changing a blueprint or auditing cross-document drift.

## Propagate a decision

1. Identify what is actually decided, what is only a suggestion, and which prior
   decision it replaces. Use the latest explicit user direction without asking for
   the same confirmation again.
2. For a substantive decision, create or update a dated strategic note using
   [the decision template](../assets/decision.md). Preserve earlier rationale and
   link both ways when replacing a note. For a small correction, update its existing
   record rather than creating a ceremonial new decision file.
3. Update affected assumptions and inputs in their canonical register. Keep stable
   IDs; record source, units, confidence, and evidence separately from acceptance.
4. Trace implications through relevant documents using the map below. Update all
   affected active content in the current task, including worked examples.
5. Update question resolutions and any newly exposed questions. Add current decision
   links to `INDEX.md`; update `AGENTS.md` only if instructions or terminology change.
6. Verify affected links, calculations, and terminology before completing the work.

| Change | Likely dependent content |
| --- | --- |
| Audience or positioning | Problem, personas, value proposition, core concept, journey, adoption/GTM, research sampling |
| Form factor or capability | Product concept, journey and failure paths, MVP/backlog, technical options, operating process, partners, costs |
| Price, fee, volume, or cost | Assumptions, revenue model, unit economics, financial model, funding/runway, worked examples |
| Funding approach | Funding strategy, cash timing, staffing assumptions, roadmap; verify legal duties independently rather than assuming they can be deferred |
| Eligibility threshold or behavioral ratio | Target users, assumptions, research inclusion criteria, acquisition/adoption plan, sizing calculations |
| Terminology | Active product and business descriptions, glossary, navigation, affected examples |

## Question lifecycle

Use this CSV schema:

```csv
question_id,question_short,owner,status,target_date,resolution,notes
```

Statuses are `open`, `in_progress`, `resolved`, and `dropped`. A resolved row needs
the answer and a decision or evidence reference; a dropped row needs a reason.
Unknown owners or dates stay blank. Preserve the original question and its ID;
make the resolution explicit instead of erasing the alternatives considered.
The foundation question document adds priority and context and links to this
tracker. If an existing project repeats statuses in both, synchronize them.

## Audit for drift

1. Establish the current authoritative inputs and decisions. If two sources conflict
   and neither is authoritative, expose the conflict as a question; do not silently
   pick the more plausible number.
2. Map each changed input or term to its expected consumers. Search by ID, parameter
   name, current value, and outdated values using `rg` or an equivalent tool.
3. Read each match in context. Historical scenarios, competitor prices, quoted
   material, and unrelated metrics can legitimately contain the old value.
4. Patch only real inconsistencies. Review the diff and recompute affected outputs.
   Use [financial modeling](financial-modeling.md) for numerical dependencies and
   [evidence validation](evidence-validation.md) for external facts.
5. Check navigation, status dates, assumption links, supersession links, and resolved
   questions. Report material unresolved contradictions with their affected scope.

Do not invent missing fees, growth rates, or accounting classifications to make
totals reconcile. Distinguish a deterministic arithmetic correction from a new
business assumption that needs input or evidence.

## Terminology

Follow an explicit requested scope, including a global rename when specified.
Otherwise standardize active descriptions while retaining accurate market categories,
competitor wording, historical context, and source quotations. Ask about scope only
when ambiguity would materially change meaning. A glossary can capture context:

| Context | Preferred term | Allowed alternative | Avoid here | Source |
| --- | --- | --- | --- | --- |
| Product description | Chosen product term | Established synonym, if useful | Obsolete product name | Accepted decision link |

Keep the glossary in an existing suitable file, `AGENTS.md`, or a dedicated file
when its size justifies one. Do not enforce bans inferred from an unrelated project.

## Reliable edits

Use available editing tools; Markdown tables do not inherently require a special
runtime. If exact matching fails, re-read the current text and use sufficient unique
context. For a batch script, require expected match counts before writing, preserve
encoding and newlines, and inspect every changed file. Do not blindly replace
numbers or retry the same failed patch without new evidence.
