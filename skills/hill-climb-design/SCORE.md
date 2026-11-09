# Score: brutal by design

LLM judges are lenient. Left alone they hand out 8s to anything that renders.
Research backs this up: judges inflate absolute scores, favor their own
outputs, anchor on scores they have seen, and pick rubric options by
position. Each rule below targets one of those failures.

## Principles

1. **Start low and earn up.** Every dimension starts at 5. Each point above 5
   needs a cited observation from the captures. No evidence, no point.
2. **The reference is a 9.** Scores are relative to the reference, not to
   "the average website." Matching the reference is a 9. Beating it on a
   dimension is a 10 and should be rare.
3. **Defects before numbers.** A reviewer lists defects first and scores
   second. The score must be consistent with the defect list.
4. **Gates cap everything.** One broken basic drags the whole score down,
   however pretty the rest is.

## Dimensions

| Dimension | Asks | Weight |
| --- | --- | --- |
| Hierarchy | Is the primary action obvious in under a second? | 2 |
| Typography | Scale, weight, line height, baseline rhythm | 1.5 |
| Spacing and grid | 4/8px grid, alignment, consistent gaps | 1.5 |
| Color | Restraint, contrast, tokens, light and dark parity | 1 |
| States | idle, loading, empty, error, partial, all designed | 2 |
| Interaction | Hover, focus, active, keyboard, feedback timing | 1.5 |
| Motion | Purposeful, fast, respects reduced motion | 0.5 |
| Accessibility | Contrast, labels, focus order, hit targets | 1.5 |
| Polish | Pixel details, icon alignment, copy, consistency | 1 |

## Anchors

Every dimension uses the same anchors. A reviewer must name which anchor
the score sits on.

| Score | Meaning |
| --- | --- |
| 0-2 | Broken. Users would notice and complain |
| 3-4 | Works but looks unfinished. Template-level |
| 5 | Competent. Nothing wrong, nothing memorable. The default |
| 6 | Clearly cared for. One or two traits close to the reference |
| 7 | Good. Most traits match. Remaining gaps visible side by side |
| 8 | Very close to the reference. Gaps only a designer would spot |
| 9 | On par with the reference |
| 10 | Better than the reference on this dimension |

## Hard rules

- A dimension with any open **blocker** defect is capped at 4.
- A dimension with any open **major** defect is capped at 6.
- A score of 8 or above needs `vsReference` of `on-par` or `better`.
- A score of 9 or above needs zero open defects on that dimension.
- A reviewer must list at least 3 defects per review. If it truly finds
  fewer, it must say what it checked and failed to break.
- A score can rise between iterations only if a listed defect on that
  dimension was fixed. Score drift without a fix is discarded.

## Gates

Failing any gate caps the overall score at 4, regardless of dimension scores.

| Gate | Fails when |
| --- | --- |
| G1 states | Any of loading, empty, or error is missing or blank |
| G2 contrast | Body text below WCAG AA (4.5:1) |
| G3 keyboard | Primary action unreachable or focus invisible |
| G4 layout shift | Content jumps when data loads |
| G5 mobile | Horizontal scroll or clipped content at 375px |

## Overall score

```
weighted = sum(median_score[d] * weight[d]) / sum(weight)
overall  = min(weighted, lowest_dimension + 2)
overall  = 4 if any gate failed else overall
```

The `lowest_dimension + 2` cap stops a strong hierarchy from hiding a weak
states story.

## Pass rule

All of:

- overall at or above **8.0**
- no dimension below **7**
- no gate failed
- at least 2 of 3 reviewers rate the design `on-par` or `better` against the
  reference, overall

8.0 is deliberately hard. On this scale it means "a designer could find
gaps, a user could not." Start there and tune after real runs.

## Anti-inflation checklist

| Bias | Countermeasure |
| --- | --- |
| Leniency, scores bunch at 7-8 | Start at 5, evidence per point, defects first |
| Self-preference, judge likes its own output | Generator never reviews. Use 3 model families |
| Anchoring on prior scores | Reviewers never see earlier scores or other reviews |
| Position bias in rubric options | Shuffle dimension order per reviewer per run |
| Pairwise position bias | When comparing to the reference, run both orders. Count "on par" only if it holds both ways |
| One generous reviewer | Median across reviewers, not mean |
| Pretty screenshot, broken product | Gates checked from code and states, not just the happy path |

## Calibrating the judges

Before trusting the scale, run it on known points:

1. Score the reference itself. It should land at 9 or close. If it scores
   10, reviewers are lenient. If it scores 7, the traits are wrong.
2. Score a plain unstyled shadcn page. It should land around 4 to 5.
3. Score a page with one gate deliberately broken. It must land at 4.

If any of these miss, fix the prompt or anchors before running real climbs.

## Known limits

- Multimodal models agree with designers only moderately on holistic
  aesthetics, and are much worse at diagnosing exactly what is wrong. That is
  why the council outputs defects with locations, and why disagreement goes to
  the user.
- Critique-before-score is common practice, but I did not find direct
  evidence that it reduces leniency. Treat it as a hypothesis we measure in
  calibration.

## Sources

- [Evaluating Scoring Bias in LLM-as-a-Judge (arXiv 2506.22316)](https://arxiv.org/html/2506.22316v2)
- [Rubric position bias and balanced permutation (arXiv 2602.02219)](https://arxiv.org/abs/2602.02219v1)
- [Self-Preference Bias in Rubric-Based Evaluation (arXiv 2604.06996)](https://arxiv.org/pdf/2604.06996)
- [Anchoring Bias in LLM-as-a-Judge (arXiv 2608.25869)](https://arxiv.org/pdf/2608.25869)
- [Multi-judge ensemble for bias calibration (NeurIPS 2026)](https://neurips.cc/virtual/2026/178218)
- [MLflow: LLM judge calibration](https://mlflow.org/articles/llm-judge-calibration/)
- [MLLM as a UI Judge (arXiv 2510.08783)](https://arxiv.org/html/2510.08783v1)
- [UICrit: UI critique dataset (arXiv 2407.08850)](https://arxiv.org/html/2407.08850v3)
- [Graphic design aesthetics benchmark for VLMs (arXiv 2603.01083)](https://huggingface.co/papers/2603.01083.md)
- [AUV-Bench summary](https://chatpaper.com/paper/351304)
- [Grepture: LLM-as-a-judge bias](https://grepture.com/blog/llm-as-a-judge-bias)
