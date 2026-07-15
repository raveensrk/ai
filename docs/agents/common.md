# Common

## General

@./emoji_legend.md
@./todo_schema.md

## Working style

- Use agile work. Tight scope.
- Nothing vague - precise goal / result.
- Use a second AI model to critique the output.
- Define the precise criteria for a great result up front.
- Use a past example as the format to match.
- Interview me and ask clarifying questions before starting a task.
- Ask one question at a time.
- Minimal fix - apply the smallest change that solves the problem; do not expand scope across layers unless each layer is genuinely load-bearing.

## Output style

- Goal: clarity and easy reading 
- I should be able to consume any response fast, at a glance.
- Don't write long paragraphs. Prefer short, concise ones.
- Lots of information to show? Split it into bullets.
- Format status reports and summaries for fast human scanning: use checklists (`- [x]` / `- [ ]`), tables, symbols, icons and status emojis instead of dense prose.
- Emoji meanings live in the canonical [emoji legend](emoji_legend.md).
- Punctuation: use plain hyphens (`-`) only; never em dashes (`—`) or en dashes (`–`).

## Plan mode

Dynamically invoke plan mode depending on the prompt and task. Decide based on
your best judgement - enter plan mode for multi-step, ambiguous, or high-impact
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
Use your judgement to decide when brainstorming vs. plan mode fits best -
reach for brainstorming when intent, requirements, or design are still open;
reach for plan mode once the goal is clear and it's time to sequence the work.

## Editing

- Before changing files, ask clarifying questions when direction or scope is unclear, and suggest useful improvements when you spot them.

## Memories

Always saved memories locally. Save location: `docs/memories.md`

## Repeatability

The context must be maintained between every chat and session. Irrespective ot the App. I use both Claude and Codex.

Repeatability is required: every session must reconstruct identical context from this repo alone. Store all durable project rules, conventions, context, and "memories" in version-controlled repo files (preferably under `docs/`) - never in agent session/private memory. No agent knowledge is assumed to carry across sessions; if something is worth remembering, commit it to the repo. Agent-private memory may hold only pointers back to the canonical repo location.

All durable rules and context live in this repo, never in agent session/private memory. Every session reconstructs identical context from the repo alone.

## Documentation

- Documentation lives in [docs](docs).
- Every subdirectory under `docs/` must have an `index.md`.
- As you work, keep the docs/ up to date. Always recoincile documentation and codebase after every edit/change.
- As we work on the project write useful information and documentation into docs/ directory in the root. Write it like a wiki using markdown files.
- When writing documentation, add citations when you can.

## AGENTS.md

Keep the AGENTS.md file up to date with the repository. Suggest me if any new guideline or rule worth adding.

## Verification

Before you do any work, mention how you could verify that work.

## Responses

- Suggest me some follow-up prompts after you finish the work.
- Always replay in clear and concise tone.

## Directory path

- Docs: `docs/`
- Scripts: `scripts/`
- Tests: `tests/`
- Todos and Inbox: [inbox](./docs/notes/inbox.md) - items follow the [Todo Schema](./docs/agents/todo_schema.md)
- Temporary files: `tmp/`

## Naming

Files and directories use `snake_case` - lowercase words joined by underscores.

- Files: `use_case.md`, `hello_world.py`
- Directories: `docs/`, `scripts/`

Exceptions:

- Tool-recognized / conventional files keep their canonical casing: `README.md`,
  `LICENSE`, `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, `.gitignore`.

## Markdown

When linking file paths, use markdown links.

Do      : [File Name](/path/to/file_name.md)
Don't   : `/path/to/file_name.md`

Same goes for images and media. For images and media use links with preview `![]()`.

Always use relative paths.

