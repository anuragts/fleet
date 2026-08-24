---
name: pr-description
description: Write short, pointed GitHub PR descriptions as bullets, unslop applied.
metadata:
  harness: [claude, codex]
  platform: [darwin, linux]
  scope: fleet
---

# PR description

Write PR descriptions a reviewer can read in under 30 seconds. Apply the
`unslop` skill to every draft.

## Shape

1. **One-line intro.** Who reported it or why it matters, and where the change
   lives. "Fixes three code-block UI issues Ayush flagged on Slack. All CSS, in
   `app/styles/code-blocks.css`."
2. **One bullet per change.** Each bullet is cause plus fix, nothing else. If a
   bullet needs three sentences, the second and third are usually cut material.
3. **One verification line.** What you ran and where a reviewer can see it
   working. "Verified with `npm run build`. Eyeball on `/docs/faq/...` in dark
   mode."

## Rules

- Total length: intro, 2-5 bullets, verification. If the PR needs more than
  five bullets, the PR is probably too big.
- Say the mechanism, not the activity. "The fade gradient is a
  `background-image`, so `background-color: transparent` never cleared it"
  beats "improved the background handling".
- Skip the implementation inventory. Do not list every selector, function, or
  file you touched; the diff already shows that. Name only what the reviewer
  cannot infer: the cause, the decision, the tradeoff.
- Keep one known-gap line if a real gap exists ("Firefox cannot offset
  scrollbar tracks, so its scrollbar still tucks under the fade"). Cut it if
  there is none; do not invent caveats.
- No headings, no bold-label paragraphs, no "Summary / Changes / Testing"
  scaffolding. Bullets carry the structure.
- Unslop applies: no em dashes, no puffery, no "this ensures", plain verbs,
  active voice.

## Example

Bad (long, labeled paragraphs, restates the diff):

> **Shade in code tabs.** Headerless blocks paint a fade gradient behind the
> overlaid actions so long code lines dip under the buttons. The code-tabs
> variant tried to clear it with `background-color: transparent`, but ...
> (three more paragraphs)

Good:

> Fixes three code-block UI issues Ayush flagged on Slack. All CSS, in
> `app/styles/code-blocks.css`.
>
> - Shade behind copy/AI buttons in code tabs: the fade gradient is a
>   `background-image`, so `background-color: transparent` never cleared it.
>   The `background` shorthand does.
> - Hover states: the AI button got an accent pill on hover, the copy button
>   didn't. Both are color-only now.
> - Scrollbar under the copy button: the vertical track now starts below the
>   buttons (`::-webkit-scrollbar-track` margin). Chrome ignores webkit
>   scrollbar rules when `scrollbar-width`/`scrollbar-color` are set, so those
>   are Firefox-only now.
>
> Verified with `npm run build` and browser geometry checks. Eyeball on
> `/docs/faq/environment-variables` in dark mode.

## Keeping it current

Update the description whenever the branch picks up a change that alters the
story. The description describes the PR as merged, not its first draft. The
title too: a PR that started as one fix and grew to three needs a title that
covers all three (see `file-pr` for title conventions).
