# Fleet

My shared coding-agent instructions for Codex and Claude Code.

## What's included

`AGENTS.md` contains my preferences for architecture, code quality, frontend design, testing, reviews, agent collaboration, and writing.

## Skills

- [`unslop`](skills/unslop/SKILL.md) removes common AI writing patterns and applies to answers, docs, plans, GitHub comments, and other user-facing prose. The tracked copy comes from [Cursor's pstack plugin](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md).

## Install

From this repository:

```sh
mkdir -p ~/.codex ~/.claude
cp AGENTS.md ~/.codex/AGENTS.md
cp AGENTS.md ~/.claude/CLAUDE.md
mkdir -p ~/.codex/skills ~/.claude/skills
cp -R skills/unslop ~/.codex/skills/unslop
cp -R skills/unslop ~/.claude/skills/unslop
```

Restart the agent session after updating the global instruction files.
