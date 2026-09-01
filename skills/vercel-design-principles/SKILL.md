---
name: vercel-design-principles
description: Design or review evidence-led reports, comparisons, calculators, and narrative data pages using Vercel's restrained, reader-first design principles.
---

# Vercel design principles

Use Vercel's design judgment for reports, decision pages, benchmarks,
comparisons, calculators, and other evidence-heavy interfaces. The goal is not
to imitate Vercel decoration. Build confidence through clear claims, honest
evidence, precise typography, strong alignment, and restraint.

Preserve the host project's framework, routes, components, tokens, and delivery
format. Do not introduce Geist, Vercel branding, or a parallel visual system
unless the user asks for a Vercel-authored or Vercel-branded result.

## Protect meaning first

When requirements compete, protect them in this order:

1. Facts, formulas, units, qualifiers, privacy, and task constraints.
2. The caller's framework, established design system, and delivery surface.
3. The reader's question, the strongest supported answer, and its evidence.
4. A composition specific to the material.
5. Responsive craft, interaction, and visual detail.

Never invent certainty, causation, ownership, urgency, recommendations, or
commercial meaning. Distinguish observations, calculations, projections,
recommendations, and causal claims.

## Start with the reader's job

Before designing, identify:

- Who opens this, in what context, and what they need to decide or understand.
- The strongest supported answer.
- The evidence that earns that answer.
- The caveat or uncertainty that could change it.
- The detail that must remain available for audit without dominating the first
  read.

Order information by reader need, not source order. Support two reading speeds:

- The executive path uses the title, headings, decisive values, captions, and
  conclusion to communicate the argument quickly.
- The audit path preserves exact tables, assumptions, formulas, methodology,
  caveats, and sources.

Simplify the language, never the claim. Preserve every population, period, unit,
condition, comparison basis, and uncertainty that changes meaning.

## Make the first viewport carry the argument

The first viewport should reveal identity, the reader's question, and the
strongest evidence. It should not spend the entire opening on a masthead, mood,
or generic setup copy.

- Choose a claim-led, evidence-led, comparison-led, or tool-led opening based on
  the reader's job.
- Compare two materially different compositions before coding when the material
  admits more than one good structure. Change topology, density, and evidence
  placement, not merely color.
- Choose geometry before components. Map magnitude to position or length, time
  to horizontal order, composition to proportion, thresholds to distance from a
  boundary, and processes to connection and sequence.
- Keep one dominant object in each major reading moment. Each section must answer
  a new question.
- Give the artifact one evidence-bearing organizing move that belongs to its
  material. A comparison geometry, threshold, sequence, or interaction should
  clarify the subject rather than decorate it.

Use tables for precise lookup, prose for one conclusion, and charts only when a
relationship becomes faster to understand visually.

## Build hierarchy before decoration

- Align the page to a shared outer grid. Use 12 columns on desktop, 6 on tablet,
  and 4 on mobile when the host system has no stronger convention.
- Give reading prose about 6 or 7 desktop columns and a 60 to 68 character line
  length. Let tables, charts, calculators, and major comparisons use the full
  evidence width.
- Align every object to a shared edge, baseline, grid line, or deliberate optical
  center. Peer blocks share type roles, value positions, rows, and actions.
- Make gutters unmistakable. If adjacent columns can read as one sentence,
  widen the gutter, rebalance the copy, or stack the columns.
- Establish hierarchy through typography before surfaces or color. Use a small
  semantic type scale and keep equivalent peers identical.
- Give every gap one owner. Repair awkward grouping instead of adding a one-off
  margin to a child.
- Rewrite before shrinking. Do not use tiny muted text to force density.

Write sentence-case headings that state the claim, question, or needed decision.
A useful title says what happened or what changes. It does not merely name the
document category.

## Earn every surface and color

Start in monochrome. Add color only when it communicates state, action, or data,
and pair it with a non-color cue.

- Prefer one continuous canvas. Use a boundary only for selection, interaction,
  warning, contrast, or grouping that spacing cannot express.
- Use spacing, alignment, typography, and density before cards, borders, pills,
  or shadows.
- Diagnose quantity separately from intensity. If a page feels busy, remove or
  reorder content. If it feels loud, reduce competing color, scale, weight,
  borders, surfaces, and motion.
- Reject decorative gradients, glows, blobs, glass, textures, ornamental shadows,
  fake depth, and color fields that carry no meaning.

Restraint still needs a deliberate anchor. Do not flatten the page into equal,
neutral blocks.

## Make evidence honest

- Put units, periods, populations, bases, and material comparators next to the
  evidence they qualify.
- Use a zero baseline for length encodings unless a clearly marked range or delta
  view answers the question better.
- Give peer bars one scale and shared label, plot, value, and annotation lanes.
- Prefer direct labels to legends. Keep labels clear of marks and annotations.
- Give primary proof enough space and contrast to carry the first read.
- Use semantic tables. Align text and headers left, numbers and their headers
  right, and body cells to the first baseline. Keep peer units and precision
  consistent.
- Use a declared, neutral selection rule for filtered evidence. Always provide a
  way to inspect the full record.
- Pair material charts with a semantic table or concise text alternative.

## Treat interaction as evidence

For calculators and decision tools, define one canonical state model containing
variables, fixed inputs, formulas, units, precision, ranges, defaults, and
dependencies. One control owns each variable. Update dependent outputs atomically
from full-precision state, then format for display.

Pre-render the default result. Preserve invalid input and the last valid result
instead of silently clamping or resetting. Keep labels, units, focus, keyboard
operation, and screen-reader status clear.

Default to stillness. Add motion only when it explains a state change, preserves
continuity, or confirms an action. Never gate reading behind animation or use
marquees, simulated typing, decorative pulses, parallax, bounce, or universal
scroll reveals.

## Reject generated-design reflexes

Do not default to:

- A centered hero followed by a card grid.
- All-caps eyebrows, decorative section numbers, or generic praise.
- Repeated metric boxes when one relationship would be clearer.
- Cards inside cards, borders used to repair weak hierarchy, or pills for
  ordinary metadata.
- Decorative charts, redundant summaries, icon tiles, fake screenshots, or stock
  imagery.
- Identical section shapes for unrelated reader questions.
- Process narration that explains how the page was designed.

## Inspect and revise

Render the first viewport, full page, light and dark themes, and narrow layouts.
Review in this order:

1. Is the central relationship, decision, or tool obvious in the first viewport?
2. Can the least specialized reader explain the answer without losing qualifiers?
3. Does each section advance the argument, with one dominant object?
4. Are type roles, baselines, gutters, spacing ownership, and line lengths sound?
5. Does the geometry tell the truth, and is exact evidence still available?
6. Can any surface, border, pill, icon, color, or paragraph be removed without
   losing meaning or usability?
7. Do both themes and narrow layouts preserve hierarchy, contrast, and access?

Fix the highest-impact systemic problem, render again, and repeat. Deliver the
result, not the private critique.

## Related guidance and source

Use this with the `design-engineering` skill:

- Local: `/Users/anurag/kafka/fleet/skills/design-engineering/SKILL.md`
- GitHub: https://github.com/anuragts/fleet/blob/main/skills/design-engineering/SKILL.md

For Vercel-authored report work, read the complete fetched source before acting:

- Local: `/Users/anurag/kafka/fleet/skills/vercel-design-principles/references/vercel-design.md`
- GitHub: https://github.com/anuragts/fleet/blob/main/skills/vercel-design-principles/references/vercel-design.md

Original source: [Vercel design.md](https://vercel.com/design.md). The local
snapshot was fetched on 2026-09-02. The live source remains authoritative for
later changes.
