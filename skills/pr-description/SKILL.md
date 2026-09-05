---
name: pr-description
description: Write or update concise GitHub PR descriptions with clear outcomes, measured results, and relevant tradeoffs.
metadata:
  harness: [claude, codex]
  platform: [darwin, linux]
  scope: fleet
---

# PR description

Help someone understand what changed and why in under 30 seconds. Write like
a colleague explaining the change in plain, professional language.

Apply [unslop](/Users/anurag/kafka/fleet/skills/unslop/SKILL.md) to every draft.
Fallback: [GitHub](https://github.com/anuragts/fleet/blob/main/skills/unslop/SKILL.md).

## Default shape

- Start with one sentence stating the outcome. Lead with measured results
  when performance is the main point.
- Add a few short bullets for meaningful changes. One idea per bullet.
  Skip bullets when one sentence already explains the whole PR.
- Include a material tradeoff or known limitation when one exists.
- End with one short verification line stating what actually passed. Say
  what remains unverified when it matters.

Aim for 80–150 words for an ordinary PR. Smaller changes can be much shorter.
Use more space only when needed to explain consequential behavior or risks.
Do not pad the description or force a fixed bullet count.
Follow a required repository template; otherwise skip headings and labels.

## What to say

- Explain the observable change first. "Fixes the sidebar briefly appearing
  before opening" is clearer than "Moves panel geometry into the shell."
- Include technical details only when they explain an important decision,
  compatibility change, or risk. Do not require cause plus mechanism for
  every bullet.
- For performance, state before and after, units, and the measured action.
  Include brief test context. Distinguish delay before an animation starts
  from time until it finishes. Never invent measurements or imply that a
  local benchmark proves a production-wide improvement.
- State costs neutrally. "Adds 166 KB of compressed JavaScript upfront"
  gives useful information. "Only 166 KB, which is fine" makes an unsupported
  judgment. Do not claim "faster" without evidence; describe the change when
  measurements are unavailable.
- Keep important limitations visible. Put lengthy benchmark methodology or
  supporting logs in a collapsible section only when useful.

## What to cut

- File, function, selector, and prop inventories already visible in the diff.
- Incidental cleanup, unless it is the purpose of the PR. "Cleanup" alone
  does not explain a change.
- Reviewer narration such as "A reviewer can see" or "This allows reviewers
  to verify." State the result or check directly.
- Dense implementation phrases such as "first-click chunk wait" when
  "delay on the first click" says enough.
- Hype, casual judgments, repeated summaries, and the history of the work.

## Examples

These illustrate style. Use only facts and checks supported by the actual PR.

### Performance and UI changes

> Reduces the delay before the chat sidebar starts opening from **314 ms to
> 17 ms**, about **95% less delay** in local production tests.
>
> - Adds a bottom-right button to open chat.
> - Makes Ask AI open and close the sidebar.
> - Fixes the sidebar briefly appearing before opening on mobile.
> - Makes Search and Ask AI shortcut hints consistent.
>
> Loads chat upfront instead of on the first click, adding 166 KB of
> compressed JavaScript to the initial load.
>
> Verified with 43 passing tests, lint, a production build, and mobile/desktop
> browser checks.

### Small fix

> Fixes the copy button covering the code block's scrollbar on Chrome.
>
> Verified in Chrome with a production build. Firefox still shows the overlap.

### Refactor without a measured speedup

> Moves sidebar width limits into one shared function so dragging and window
> resizing use the same bounds. The width limits remain unchanged.
>
> Verified with the existing resize tests and a production build.

## Keeping it current

Describe the complete final change, not the first draft or commit history.
Update the title and description when authorized PR work changes their scope.
Writing a draft does not itself authorize publishing it.

For title conventions, read
[file-pr](/Users/anurag/kafka/fleet/skills/file-pr/SKILL.md).
Fallback: [GitHub](https://github.com/anuragts/fleet/blob/main/skills/file-pr/SKILL.md).
