# Fleet

My shared coding-agent instructions for Codex, Claude Code, and Google Antigravity.

## What's included

`AGENTS.md` contains my preferences for architecture, code quality, frontend design, testing, reviews, agent collaboration, and writing.

## Skills

- [`unslop`](skills/unslop/SKILL.md) removes common AI writing patterns and applies to answers, docs, plans, GitHub comments, and other user-facing prose. The tracked copy comes from [Cursor's pstack plugin](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md).

## Install

From this repository:

### Codex and Claude Code

```sh
mkdir -p ~/.codex ~/.claude
cp AGENTS.md ~/.codex/AGENTS.md
cp AGENTS.md ~/.claude/CLAUDE.md
mkdir -p ~/.codex/skills ~/.claude/skills
cp -R skills/unslop ~/.codex/skills/unslop
cp -R skills/unslop ~/.claude/skills/unslop
```

### Google Antigravity (standalone and T3 Code)

```sh
./scripts/sync-antigravity.sh
```

This symlinks `AGENTS.md` and writes `skills.json` (pointing to `fleet/skills`, `~/.claude/skills`, `~/.codex/skills`, and `~/.agents/skills`) for `~/.gemini/` and for every T3 Code Antigravity provider instance under `~/.t3/userdata/providers/antigravity/*`. Re-run it if you add a new Antigravity provider instance in T3 Code.

Restart the agent session after updating the global instruction files.
