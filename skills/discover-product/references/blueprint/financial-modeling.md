# Financial Modeling and Recalculation

Read when a blueprint includes prices, volumes, costs, fees, budgets, or forecasts.
Use only the business model and assumptions relevant to this project.

## Define inputs before calculating

Use canonical assumption IDs for uncertain inputs. Record currency, period, unit,
rate base, scenario, source, and who bears each cost. Separate capacity from actual
sales, transaction value from business revenue, and revenue from contribution and
cash flow. Cite factual inputs and preserve their date and scope.

For each scenario, calculate from one coherent input set. Do not mix optimistic
volume with base-case costs unless that combination is explicitly the scenario.
State rounding rules; fractional expected units are acceptable in an expectation
model, while operational allocations need a justified integer rule.

## Follow the dependency chain

```text
capacity and activity -> units sold -> transaction value -> revenue
                                 -> variable costs -> contribution
revenue and cost timing + fixed expenses + investment -> cash balance
```

For a simple direct-sale model, the relationships might be:

```text
units_sold = available_units * sell_through_rate
sales_value = sum(units_sold_by_variant * price_by_variant)
revenue = sales_value adjusted for the stated discounts/refunds model
variable_cost = sum(quantity_by_cost_driver * cost_per_driver)
contribution = revenue - variable_cost
```

For a marketplace, transaction value and the platform's retained revenue are
different. Define each fee base and cost bearer explicitly. Apply revenue shares,
secondary transactions, royalties, subscriptions, or multiple variants only if
they exist in the project. Listing a resale is not proof of a completed sale;
model completion separately when relevant. Sum repeated royalties from their
individual transaction bases rather than reusing a stale cumulative total.

Inventory purchases can affect cash before goods are sold. Do not equate production
costs with sold-unit costs or contribution with profit. Explain model classifications
and prevent double-counting when rolling up into the financial model.

## Verify and propagate

1. Recompute affected outputs with a calculator or a short script. Show formulas,
   input IDs, and a useful worked example in the document; a printed total alone
   does not make the calculation traceable.
2. Reconcile component sums, scenario totals, rate bases, and periods. Any allocation
   intended to partition a total should add to that total.
3. Update downstream revenue, margin, budget, cash/runway, and funding references
   where present. Recompute every modeled revenue stream affected by the change.
4. If missing assumptions prevent reconciliation, mark the affected calculation as
   unresolved and add a question. Correct demonstrable arithmetic errors directly.

## Units and display

Use explicit units and the document's locale. Indonesian prose can use
`Rp 1.250.000` or `Rp 1,25 juta`; keep machine-readable numbers unambiguous.
Do not infer whether `M` means million or miliar from the name of a funding round.
Derive magnitude from the input and equation. For example,
`5,000 * Rp 12,500,000 = Rp 62,500,000,000` in machine-style notation,
displayed as `Rp 62,5 miliar` in Indonesian prose.

For currency conversion, record the dated exchange-rate source or label a scenario
rate as an assumption. Recheck arithmetic after changing notation; formatting should
not change values. Retain precision during calculations and round for display.
