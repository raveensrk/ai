# ai
Repository to mess arounds with ai things

## Agent Skills

Skills follow the [Agent Skills](https://agentskills.io) protocol and live
under `.agents/skills/<name>/SKILL.md`. All three supported agents discover
them inside this repo with no extra setup:

- **Codex CLI** and **Gemini CLI** scan `.agents/skills/` natively.
- **Claude Code** scans `.claude/skills/`, which is a symlink to
  `.agents/skills/` — drop a new skill under `.agents/skills/` and all three
  agents pick it up.
