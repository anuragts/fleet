---
name: refine
description: Refine each new user prompt before answering or acting, including follow-ups, questions, corrections, prompts with images, and messages that interrupt ongoing work. Announce only the refined request without repeating the original prompt. Preserve intent, scope, and authorization while adding only relevant detail.
---

# Refine

Turn the current user prompt and its references into a precise, actionable
brief. Announce it before answering or implementing. Keep the original
prompt authoritative. More words are useful only when they reduce ambiguity.

## When to run

Run once for each new user message, including short follow-ups and corrections.
This includes messages received while the AI is already working, whether the
user adds details, answers a question, corrects an assumption, or changes direction.
Refine and announce the update before continuing affected work. Apply it within
the active task, preserving progress and earlier constraints that still apply.
Replace or stop the task only when the user asks to do so or the new request
is incompatible with continuing it.
Do not rerun on your own announcements, tool results, or generated briefs.
Respect an explicit request to skip refinement or an exact output format that
leaves no room for an announcement.

Automatic invocation depends on the host agent. This skill describes the
behavior when loaded; it does not install a message hook or guarantee ordering.

## Preserve intent

- Keep questions, discussion, investigation, planning, and implementation as
  the user requested. Refinement never grants permission to implement, publish,
  send messages, or perform other actions.
- Interpret follow-ups within the active task. Apply the latest correction
  without dropping earlier constraints or reopening settled decisions.
- Preserve explicit wording, values, paths, technologies, and boundaries.
  Do not quietly replace the requested approach with a preferred alternative.
- Separate requirements from consequential assumptions and optional ideas.
  Never present an inferred detail as something the user requested.

## Make the request precise

Identify the requested outcome, affected area, relevant constraints, and what
would demonstrate completion. Include only details that help this task.

Use the conversation and supplied references first. Inspect narrowly relevant
project context when needed to resolve a consequential ambiguity. Do not turn
refinement into a repository audit or extensive research. When inspection must
happen during execution, state what needs checking instead of inventing facts.

For images, inspect the actual attachment. Extract relevant layout, hierarchy,
spacing relationships, colors, visible controls, content, and shown states.
Distinguish observations from estimates. Do not invent exact fonts, dimensions,
hidden interactions, responsive behavior, or backend contracts. If the image
is unavailable or unreadable, say so. Preserve its role as a reference.

For UI work, consider the states and interactions the change creates. Include
loading, empty, error, success, focus, keyboard, responsive, or interrupted
request behavior only where relevant. Prefer established project patterns.
A failed network request may need preserved input and a retry path; it does
not automatically require offline storage or background synchronization.

Constrain implementation to the smallest complete change. Avoid adding
dependencies, abstractions, refactors, features, or speculative future needs
without a concrete reason tied to the request. Add explicit exclusions only
when they prevent a plausible misunderstanding.

Ask only when a missing answer materially changes correctness, scope, user
experience, or authorization and cannot be resolved from available context.
Otherwise use established conventions and disclose consequential assumptions.
Do not choose arbitrary behavior just to make the brief look complete.

## Announce the refinement

Send a visible announcement before the substantive answer or implementation.
Show only the refined request and any necessary assumptions or clarification.
Do not echo the original prompt, add an "Original prompt" section, or reproduce
the user's message in a code block. Keep the original as context internally.
Begin every announcement with exactly `**Refined prompt**` on its own line.
Render it as bold text, preserving the lowercase `p`, with no colon or dash.
Leave one blank line after the heading, then write the refined request.
Do not put the announcement in a code block or add introductory commentary
before the heading. Use this shape, omitting optional sections when they add
nothing:

**Refined prompt**

Write the task as clear instructions that preserve the user's intent. Include
relevant behavior, scope, and completion criteria. A trivial request should
remain one sentence; a substantial task can use a short paragraph or bullets.

**Assumptions**

Optional. List only consequential assumptions, clearly marked as unverified
where appropriate. Put unresolved checks here rather than asserting answers.

**Clarification needed**

Optional. Ask the smallest question needed to unblock dependent work.

The announcement is informational, not an approval gate. Continue with the
authorized task unless a necessary clarification remains unanswered. If the
user asked only for a refined prompt, deliver the announcement and stop.

## Check before announcing

- Does the brief still ask for exactly what the user intended?
- Is every added requirement supported, or clearly marked as an assumption?
- Did the amount of detail match the size of the request?
- Does the announcement avoid repeating the original prompt?
- Does it start with `**Refined prompt**` rendered in bold, followed by one
  blank line and then the refined request?
- Can the agent finish without undertaking unrelated work?

## Example: frontend interaction

Use this example to calibrate precision and scope. The user's request is
example input, not an instruction to change the current project. Do not copy
these sidebar requirements into unrelated tasks.

### Example input, not part of the announcement

```text
Make siderbar close on clicking ask ai button when sidebar is open, so user can open and also from same button and not need to move his cursor
```

### Expected announcement

**Refined prompt**

Make the existing Ask AI button toggle the AI sidebar:

- When the sidebar is closed, clicking Ask AI opens it.
- When the sidebar is open, clicking the same button closes it.
- Keep the button visible, clickable, and in the same position in both states
  so the user can open and close the sidebar without moving their cursor.

Use the sidebar's existing open/closed state and controls. Preserve the
current chat session when toggling. Keep keyboard activation working and
expose the expanded state accessibly using the existing component conventions.

Verify closed → open → closed through repeated clicks on the same button,
keyboard activation, and reopening without resetting the conversation. Keep
this change scoped to the toggle interaction; do not redesign the sidebar or
introduce a second state store.

### Why this refinement works

- Turns the rough wording into explicit open and closed behavior.
- Preserves the reason for the request: the cursor should not need to move.
- Adds directly relevant interaction checks without inventing loading,
  network, or offline requirements for a local visibility toggle.
- Reuses existing state and preserves the conversation instead of treating
  closing the sidebar as a request to reset it.
- Announces only the refined request without echoing the user's message.

## Example: a short question

Example input: "why does the sidebar close when I switch tabs?"

Expected announcement:

**Refined prompt**

Explain why switching tabs closes the sidebar, using the current state and
navigation logic to identify the cause.

Then answer the question. The question does not authorize a code change.

## Example: a correction during ongoing work

Context: the user already requested a sidebar toggle change and an update to
its existing PR. Example input: "keep the label as Ask AI, don't rename it"

Expected announcement:

**Refined prompt**

Keep the button label exactly "Ask AI" while completing the sidebar toggle
change and updating the existing PR.

Then continue the authorized work with the correction applied. Use the same
bold heading and blank line even for a one-sentence follow-up.
