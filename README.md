# ai
Repository to mess around with AI things.

## Stow Setup

This repo uses GNU Stow to manage individual global agent skills. The parent
directories are not owned by Stow.

Owned by this repo:

```text
~/.agents/skills/<skill-name>
```

Not owned by this repo:

```text
~/.agents
~/.agents/skills
```

Install or update skill links:

```bash
./install.sh
```

Dry-run install:

```bash
mkdir -p "$HOME/.agents/skills"
stow -nvt "$HOME" ai
```

Dry-run uninstall:

```bash
stow -nDvt "$HOME" ai
```

Expected links:

```text
~/.agents/skills/bookmark-manager -> ~/repos/ai/ai/.agents/skills/bookmark-manager
~/.agents/skills/<skill-name> -> ~/repos/ai/ai/.agents/skills/<skill-name>
```

If an older install made `~/.agents` a symlink to this repo, `./install.sh`
replaces that symlink with real directories before stowing the skill links.

## Agent Skills

Skills follow the [Agent Skills](https://agentskills.io) protocol and live
under `ai/.agents/skills/<name>/SKILL.md`. After running `./install.sh`, they
are available globally under `~/.agents/skills/`.

- **Codex CLI** and **Gemini CLI** scan `~/.agents/skills/` globally.
- **Claude Code** scans `.claude/skills/`, which is a symlink to
  `ai/.agents/skills/`.

Add future skills here:

```text
ai/.agents/skills/<skill-name>/SKILL.md
```
