# AGENTS notes

- All durable rules and context live in this repo, never in agent session/private memory — see the repeatability rule in [AGENTS.md](../AGENTS.md). Every session reconstructs identical context from the repo alone.
- Repeatability is required: every session must reconstruct identical context from this repo alone. Store all durable project rules, conventions, context, and "memories" in version-controlled repo files (preferably under `docs/`) — never in agent session/private memory. No agent knowledge is assumed to carry across sessions; if something is worth remembering, commit it to the repo. Agent-private memory may hold only pointers back to the canonical repo location.

## Output style

Goal: clarity and easy reading — Raveen should be able to consume any response fast, at a glance.

- Don't write long paragraphs. Prefer short, concise ones.
- Lots of information to show? Split it into bullets.
- Format status reports and summaries for fast human scanning: use checklists (`- [x]` / `- [ ]`), tables, symbols, icons and status emojis instead of dense prose.
- Emoji meanings live in the canonical [emoji legend](../docs/emoji_legend.md).
