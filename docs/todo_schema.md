# Todo Schema

Canonical format for todo items in documentation files ([inbox.md](inbox.md), task lists) across every project. It formalizes the format already in use in the inbox; referenced from [AGENTS.md](../AGENTS.md).

## Format

```markdown
- STATE: <content> (due: YYYY-MM-DD)
  - <optional sub-bullet details, free text>
```

- One item per top-level list line: uppercase state, colon, space, content.
- `(due: YYYY-MM-DD)` — optional, at the end of the content line, absolute ISO dates only.
- Details go in nested sub-bullets (2-space indent), free-form.
- Change state by editing the prefix in place — don't delete items (git keeps the history); drop an item by marking it `OBSOLETE`.

## States

| State | Meaning |
|-------|---------|
| `TODO` | Not started |
| `IN_PROGRESS` | Actively being worked |
| `DONE` | Completed |
| `OBSOLETE` | Dropped / no longer relevant (kept for history) |

Lifecycle: `TODO → IN_PROGRESS → DONE`; any state can move to `OBSOLETE`.

## Reporting

When summarizing todos in reports, use the [Emoji Legend](emoji_legend.md):

| State | Emoji |
|-------|-------|
| `TODO`, `IN_PROGRESS` | ⏳ |
| `DONE` | ✅ |
| `OBSOLETE` | 🗑️ |
| Past `(due:)` date | ⚠️ |

## Example

```markdown
- TODO: File quarterly GST return (due: 2026-07-20)
  - Collect purchase invoices from the shared drive first
- IN_PROGRESS: Create a methodology presentation on wiki documentation
  - Showcase and demos with real use cases
- DONE: Create discord bot with claude
- OBSOLETE: Create a skill to index all scripts in a directory
```

## Using from other repos

Reference this file — do not copy it. In the target repo's `AGENTS.md` / `CLAUDE.md`, add an import line:

```markdown
@~/repos/ai/docs/todo_schema.md
```
