# ai
Repository to mess arounds with ai things

## Agent Skills

Skills following the [Agent Skills](https://agentskills.io) protocol live
under `.agents/skills/<name>/SKILL.md`. They work with Claude Code, OpenAI
Codex CLI, and Gemini CLI.

- **Gemini CLI** auto-discovers `.agents/skills/` in this repo.
- **Claude Code** reads `.claude/skills/`; this repo symlinks each skill
  there so it's picked up automatically when working inside the repo.
- **Codex CLI** only reads user-level `~/.codex/skills/`. Run
  `scripts/install_skills.sh` once to link this repo's skills into all
  three user-level skill directories.
