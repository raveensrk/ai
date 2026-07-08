# Common

## General

./emoji_legend.md
./todo_schema.md

## Output style

Goal: clarity and easy reading — Raveen should be able to consume any response fast, at a glance.

- Don't write long paragraphs. Prefer short, concise ones.
- Lots of information to show? Split it into bullets.
- Format status reports and summaries for fast human scanning: use checklists (`- [x]` / `- [ ]`), tables, symbols, icons and status emojis instead of dense prose.
- Emoji meanings live in the canonical [emoji legend](emoji_legend.md).

## Plan mode

Dynamically invoke plan mode depending on the prompt and task. Decide based on
your best judgement — enter plan mode for multi-step, ambiguous, or high-impact
work; skip it for small, well-defined changes.

## Effort level

Low effort is the default. Before executing **any** prompt:

1. Analyse the prompt and task.
2. Determine the best effort level for it (low / medium / high / extra / max).
3. If it **differs** from the current effort level, recommend the change with a
   one-line reason and **wait for confirmation** before executing.
4. If it **matches** the current level, proceed without asking.

## Brainstorming

Dynamically invoke the `/brainstorming` skill depending on the prompt and task.
Use your judgement to decide when brainstorming vs. plan mode fits best —
reach for brainstorming when intent, requirements, or design are still open;
reach for plan mode once the goal is clear and it's time to sequence the work.

## Memories

Always saved memories locally. Save location: `docs/memories.md`

## Repeatability

The context must be maintained between every chat and session. Irrespective ot the App. I use both Claude and Codex.

Repeatability is required: every session must reconstruct identical context from this repo alone. Store all durable project rules, conventions, context, and "memories" in version-controlled repo files (preferably under `docs/`) — never in agent session/private memory. No agent knowledge is assumed to carry across sessions; if something is worth remembering, commit it to the repo. Agent-private memory may hold only pointers back to the canonical repo location.

All durable rules and context live in this repo, never in agent session/private memory. Every session reconstructs identical context from the repo alone.

As we work on the project write useful information and documentation into docs/ directory in the root. Write it like a wiki using markdown files.


