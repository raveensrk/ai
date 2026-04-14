# Repository Guidelines

## AGENT INSTRUCTIONS

- You are allowed to save helper scripts locally for repeated tasks.
- Always optimize for token usage.
- Follow KISS: Keep it simple stupid philosophy.
- Do one thing and do it well.
- Programming Languages of my choice: Bash, Python.
- Be direct, task focused, no extra information.
- When there is an oppurtuinty to reduce token usage or automate manual work with scripts suggest me with a prompt.
- When writing a new script, prefer python or bash, but if any other language be better suited for the task ask me.
- Ask the fewest concrete questions needed.
- Keep communication simple and concise.
- Ask one question at a time.

## Directory path

- Put automated checks in `tests/`.
- Put runnable Bash or Python utilities in `scripts/`. Suggest creating helper scripts whenever you can. Give me ideas.
- Put supporting notes in `docs/` only when they help explain code or workflows.
- `INBOX.md`: temporary scratch space
- `data/`: processing data
- `data/training.yaml`: reusable ambiguity patterns
- `tmp/`: temporary files

Prefer small, single-purpose files. Use `snake_case.py` for scripts such as `fetch_data.py` or `sync_cache.sh`.

## Build, Test, and Development Commands

If you add a new entrypoint, document it in `README.md`.

## Coding Style & Naming Conventions

Python and Bash are the preferred languages here.

- Python: 4-space indentation, PEP 8, short functions, minimal dependencies.
- Bash: start scripts with `#!/usr/bin/env bash` and use `set -euo pipefail` for non-trivial scripts.
- Keep names descriptive and direct; avoid vague files like `utils.py` unless the scope is truly shared.
- Write clean code by default and keep changes easy to review.

## Testing Guidelines

For scripts, prefer small smoke tests or a documented dry-run path. Every new non-trivial behavior should include either an automated test or clear manual verification steps in the PR.

## Commit & Pull Request Guidelines

Git history is minimal, so follow a simple convention: short imperative commit subjects, for example `Add transcript cleanup script`. Keep commits focused on one logical change.

PRs should include a short summary, how the change was tested, any required environment variables, and sample output when behavior changes. Link the related issue when one exists. Avoid bundling unrelated experiments in the same PR.

## Security & Configuration Tips

Do not commit `.env` files, tokens, credentials, caches, or generated artifacts. Use example config files when needed and document required variables in `README.md`.

