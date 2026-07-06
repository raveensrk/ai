# Repository Guidelines

## AGENT INSTRUCTIONS

- Interview me and ask clarifying questions before starting a task.
- Ask one question at a time.

## Always-on rules

These apply to every task without needing a trigger:

- Minimal fix — apply the smallest change that solves the problem; do not expand scope across layers unless each layer is genuinely load-bearing.

## Directory path

- Notes and reference: `notes/`
- Docs: `docs/`
- Scripts: `scripts/`
- Tests: `tests/`
- Todos and Inbox: [inbox](./notes/inbox.md) — items follow the [Todo Schema](./docs/todo_schema.md)
- Temporary files: `tmp/`

## Naming

Files and directories use `snake_case` — lowercase words joined by underscores.

- Files: `use_case.md`, `hello_world.py`
- Directories: `notes/`, `scripts/`

Exceptions:

- Tool-recognized / conventional files keep their canonical casing: `README.md`,
  `LICENSE`, `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, `.gitignore`.
- Skill directories under `.agents/skills/` use `kebab-case` per the
  [Agent Skills](https://agentskills.io) protocol — e.g.
  `reverse-image-search-video`.

## Aliases and Shared Terminologies

These are case insensitive.

| Command | Meaning |
|---------|---------|
| `y` | yes |
| `n` | no |
| `<` | previous |
| `>` | next |


## Reporting emojis

Use the [Emoji Legend](./docs/emoji_legend.md) in all reports and summaries.

## Markdown

When linking file paths, use markdown links.

Do      : [File Name](/path/to/file_name.md)
Don't   : `/path/to/file_name.md`

Same goes for images and media. For images and media use links with preview `![]()`.

Always use relative paths.

## Bookmarks

Rules for [Bookmarks](./notes/bookmarks.md):

- Every bookmark goes under a `##` category section — never directly under the
  `# Bookmarks` heading.
- YouTube videos are filed under `## Blog Posts` — it is a general
  content/media category, not just written articles.
- If no existing category fits, ask what to name the new one.

## Tasks

[Tasks](./notes/tasks.md)

## Citations

When writing documentation, add citations when you can.
