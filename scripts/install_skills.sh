#!/usr/bin/env bash
# Install this repo's Agent Skills (.agents/skills/*) into the per-tool
# user-level directories, so Claude Code, Codex CLI, and Gemini CLI can
# discover them outside this repo.
#
# Symlinks each skill folder into:
#   ~/.claude/skills/<skill>
#   ~/.codex/skills/<skill>
#   ~/.gemini/skills/<skill>
#
# Re-run safely; existing symlinks are refreshed.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="$repo_root/.agents/skills"

if [[ ! -d "$src" ]]; then
  echo "No skills found at $src" >&2
  exit 1
fi

for tool_dir in "$HOME/.claude/skills" "$HOME/.codex/skills" "$HOME/.gemini/skills"; do
  mkdir -p "$tool_dir"
  for skill in "$src"/*/; do
    name="$(basename "$skill")"
    ln -sfn "$skill" "$tool_dir/$name"
    echo "linked $tool_dir/$name -> $skill"
  done
done
