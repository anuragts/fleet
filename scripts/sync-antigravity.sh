#!/usr/bin/env bash
set -euo pipefail

FLEET_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENTS_FILE="$FLEET_DIR/AGENTS.md"

write_skills_json() {
  local target_dir="$1"
  mkdir -p "$target_dir"
  cat > "$target_dir/skills.json" <<EOF
{
  "entries": [
    { "path": "$FLEET_DIR/skills" },
    { "path": "$HOME/.claude/skills" },
    { "path": "$HOME/.codex/skills" },
    { "path": "$HOME/.agents/skills" }
  ]
}
EOF
}

sync_antigravity_root() {
  local root_dir="$1"
  mkdir -p "$root_dir/config"
  ln -sf "$AGENTS_FILE" "$root_dir/GEMINI.md"
  ln -sf "$AGENTS_FILE" "$root_dir/config/AGENTS.md"
  ln -sf "$AGENTS_FILE" "$root_dir/config/GEMINI.md"
  write_skills_json "$root_dir/config"
}

# Standalone Antigravity (~/.gemini)
sync_antigravity_root "$HOME/.gemini"

# Every T3 Code Antigravity provider instance (hashed directories)
T3_AGY_DIR="$HOME/.t3/userdata/providers/antigravity"
if [ -d "$T3_AGY_DIR" ]; then
  for instance_dir in "$T3_AGY_DIR"/*; do
    [ -d "$instance_dir" ] || continue
    sync_antigravity_root "$instance_dir"
  done
fi

echo "Synced Antigravity rules and skills from $FLEET_DIR"
