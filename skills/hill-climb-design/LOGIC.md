# Logic: review flow

How one run goes, from brief to a passing design. Scoring rules live in
`SCORE.md`.

## Flow

```
brief + reference
      |
      v
1. Diverge ---- 5 distinct directions ----> user picks one
      |
      v
2. Capture  (screenshots of every state, reference captured the same way)
      |
      v
3. Council  (3 models, blind, independent)
      |
      v
4. Aggregate (merge defects, compute score)
      |
      v
5. Gate ---- pass? ----> done
      | no
      v
6. Fix      (top defects only, one change set)
      |
      v
7. Accept or revert ----> back to 2
```

## Steps

### 1. Diverge

Generate 5 directions that differ in kind, not in shade: layout model,
density, type personality, color strategy, motion approach. Five versions of
the same card with different radii do not count.

The user picks one. If the run is unattended, the council scores all 5 once
and the top one climbs.

### 2. Capture

Screenshot the target and the reference in the same set of states:

- idle, loading, empty, error, partial data
- hover and focus on the primary action
- 375px and 1440px widths
- light and dark

Also pass the source code, so reviewers can catch things a screenshot hides,
like missing `aria-*` or hardcoded colors.

### 3. Council

Three reviewers from different model families. Different families matter
because judges favor their own outputs, and the generator should never grade
itself. Each reviewer:

- sees the brief, the reference, its named traits, and the captures
- does not see other reviewers' output or any previous score
- writes defects first, then scores (see `SCORE.md`)

Reviewer output, typed:

```ts
type Severity = "blocker" | "major" | "minor";

type Defect = {
  id: string;
  dimension: Dimension;
  severity: Severity;
  where: string; // state + element, e.g. "empty state / CTA button"
  what: string; // the observed problem
  why: string; // the raw reasoning, why it hurts the user
  referenceGap: string; // what the reference does instead
  fix: string; // smallest change that would close it
};

type Review = {
  reviewer: string;
  defects: Defect[];
  scores: Record<Dimension, number>; // 0-10, see SCORE.md
  vsReference: Record<Dimension, "worse" | "on-par" | "better">;
  gatesFailed: GateId[];
};
```

### 4. Aggregate

- Merge defects that point at the same element and problem. A defect found by
  2 or 3 reviewers ranks above one found by a single reviewer.
- Per dimension score: the median of the 3 scores. Median, not mean, so one
  generous reviewer cannot drag the result up.
- Any gate failed by any reviewer counts as failed until a fix is verified.

### 5. Gate

Stop when the pass rule in `SCORE.md` holds. Otherwise continue.

### 6. Fix

Take the top 3 defects by (severity, number of reviewers who found it). Fix
those only. Small change sets make it clear which fix moved the score.

### 7. Accept or revert

This is the hill climb. Re-capture and re-run the council.

- Overall score went up and no new blocker appeared: keep the change.
- Otherwise revert and try the next defects in the list.

## Stop conditions

| Condition | Action |
| --- | --- |
| Pass rule holds | Done. Report final scores and the defect history |
| 8 iterations reached | Stop. Report where it plateaued |
| 2 iterations with no accepted change | Stop. Likely a local maximum. Suggest switching to another of the 5 directions |
| Reviewers disagree by 4+ points on a dimension | Ask the user to break the tie |

## Output of a run

- Final design and the chosen direction
- Score table per iteration, so the climb is visible
- Every accepted defect fix with its `why`
- Remaining minor defects that did not block the pass

## Open questions

- Which 3 models? Leaning Claude, GPT, and Gemini for family diversity.
- Capture tool: Playwright script, or the T3 preview tools?
- Use the `typesafe-ai` skill for the structured `Review` output?
  Local: `/Users/anurag/.agents/skills/typesafe-ai/SKILL.md`.
  GitHub: https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md
- Should the user approve each accepted change, or only the final result?
