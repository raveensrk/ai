# Codex

## Install Codex CLI {{{1

On macOS, Linux, or WSL:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex --version
codex login
```

For unattended installs:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh
```

On Windows PowerShell:

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex
codex --version
codex login
```

If you work in WSL2, install and run Codex inside WSL, keep repositories under the Linux home directory, and open VS Code from the WSL shell with `code .`.

## Install Editor Integration {{{1

Use the Codex IDE extension when you want Codex inside your editor.

After installing, sign in with ChatGPT or an API key. The IDE extension shares Codex configuration with the CLI through `~/.codex/config.toml`.

## Create `AGENTS.md` {{{1

`AGENTS.md` is the durable instruction file Codex reads before work. It should be short, specific, and operational.

You can scaffold one from Codex:

```text
/init
```

Or create one manually:

```md
# AGENTS.md

## Project Overview

- This repository contains ...
- Main app code lives in ...
- Tests live in ...

## Commands

- Install: `...`
- Run: `...`
- Test: `...`
- Lint: `...`
- Type check: `...`

## Working Rules

- Keep changes scoped to the requested task.
- Do not commit secrets or local config files.
- Prefer existing project patterns before adding new dependencies.
- Update docs when command behavior or public APIs change.

## Done Means

- Relevant tests pass.
- Lint/type checks pass when applicable.
- The diff is reviewed before commit.
```

Put global personal preferences in `~/.codex/AGENTS.md`. Put project rules in `AGENTS.md` at the repository root. Add nested `AGENTS.md` or `AGENTS.override.md` files only when a subdirectory has special rules.

For use local rules, `AGENTS.local.md`.


## Codex Configuration Basics {{{1

Codex stores durable settings in `config.toml`.

| Scope | Location | Use for |
| --- | --- | --- |
| User config | `~/.codex/config.toml` | Personal defaults across projects |
| Project config | `.codex/config.toml` | Repo-specific defaults, loaded only for trusted projects |
| Profile config | `~/.codex/<profile>.config.toml` | Named variants for special workflows |
| Environment | `CODEX_HOME` | Alternate Codex home, config, auth, sessions, logs |

Configuration precedence, highest first:

1. CLI flags and `--config` overrides
2. Project `.codex/config.toml`
3. Selected profile config
4. User config
5. System config
6. Built-in defaults

## Plan Mode and Goal Mode {{{1

Use `/plan` when:

- the task is ambiguous
- the codebase is unfamiliar
- you want Codex to ask questions first
- you need an implementation plan before edits

Use `/goal` when:

- the task may take many steps
- Codex needs persistent completion criteria
- you want progress tracking across a longer run

Good goal:

```text
Migrate the dashboard package from JavaScript to TypeScript. Done when it builds in strict mode, all existing tests pass, and new explicit `any` usages are justified or removed.
```


## Code Review and Diffs {{{1

Use `/review` before committing substantial work.

## Non-interactive Codex {{{1

```bash
codex exec "summarize this repository"
codex exec --json "summarize this repository" | jq
codex exec --ephemeral "triage the failing tests"
codex exec --sandbox workspace-write "fix the failing test"
codex exec resume --last "implement the plan"
```

Use `CODEX_API_KEY` inline for one non-interactive run when needed:

```bash
CODEX_API_KEY=... codex exec "summarize the release notes"
```

Do not set API keys job-wide in CI jobs that run repository-controlled code.

## Official References {{{1

Use these as the source of truth when details drift:

- [Codex overview](https://developers.openai.com/codex/overview)
- [Codex quickstart](https://developers.openai.com/codex/quickstart)
- [Codex app](https://developers.openai.com/codex/app)
- [Codex CLI](https://developers.openai.com/codex/cli)
- [Codex IDE extension](https://developers.openai.com/codex/ide)

## Final Beginner Advice {{{1

Start small. Ask Codex to explain before you ask it to edit. Keep every project in Git. Write down the real commands in `AGENTS.md`. Give clear done criteria. Review diffs. Let Codex run tests, but learn to understand the output yourself.

The goal is not to make Codex do mysterious magic. The goal is to build a working loop where you can describe intent, Codex can act, your tools can verify, and you can confidently accept, steer, or reject the result.
