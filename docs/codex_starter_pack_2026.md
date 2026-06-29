# Codex Starter Pack 2026

Last updated: 2026-06-29

This guide is for someone who wants to use Codex independently on real software projects. It covers the tools to install, the Codex surfaces available in 2026, the topics to learn, setup checklists, common workflows, and safety practices.

Codex changes over time. Treat installation links, model names, pricing, feature maturity, and plan availability as time-sensitive. The recommendations below are based on the current OpenAI Codex manual on 2026-06-29.

## 1. What Codex Is

Codex is OpenAI's coding agent for software development. It can read a codebase, explain it, edit files, run commands, review code, debug problems, and automate recurring development tasks.

You can use Codex in several places:

| Surface | Best for | Runs where |
| --- | --- | --- |
| Codex app | Main desktop workflow, parallel threads, worktrees, local review, automations, browser previews, artifacts | Your Mac or Windows machine |
| Codex CLI | Terminal-first local work, scripting, non-interactive runs, fast repo inspection | Your machine, server, container, or CI runner |
| Codex IDE extension | Editing beside VS Code, Cursor, Windsurf, and other VS Code-compatible editors | Your editor plus local workspace |
| Codex web / cloud | Delegating parallel tasks, PR-ready changes, running from another device | OpenAI-managed cloud environment |
| GitHub integration | Code review and PR tasks from GitHub comments | Codex cloud |
| Slack and Linear integrations | Delegating tasks from team conversations or issues | Codex cloud |
| Codex SDK / app-server | Building internal tools and custom automation around Codex | Your application or automation environment |

For most beginners, start with the Codex app and one local project. Add the CLI once you are comfortable with terminal commands. Add cloud, GitHub, Slack, Linear, MCP, skills, and automations after your local workflow is reliable.

## 2. Essential Accounts, Apps, and Software

### 2.1 Day-One Minimum Stack

If you are starting from nothing, this is enough for your first real local project:

| Item | Why you need it |
| --- | --- |
| ChatGPT account with Codex access | Sign in and use Codex. |
| Codex app | Main beginner-friendly interface. |
| Git | Review and roll back changes safely. |
| Code editor | Inspect files and make manual edits when needed. |
| Terminal | Run project commands and use Codex CLI later. |
| Project runtime and package manager | Install dependencies, run the app, and run tests. |
| Browser | Preview local web apps and complete login flows. |

Add GitHub, Codex CLI, cloud, MCP, plugins, skills, and automations as soon as your first local loop is comfortable.

### 2.2 Accounts and Access

| Access | Required? | Why it matters | Notes |
| --- | --- | --- | --- |
| ChatGPT account with Codex access | Yes | Lets you sign in and use Codex | Current docs say every ChatGPT plan includes Codex, with limits and feature availability varying by plan and workspace policy. |
| OpenAI API key | Optional | Useful for API-billed local automation, CI, SDK usage, and some scripted workflows | API key auth supports local Codex workflows but does not unlock every ChatGPT workspace or cloud feature. |
| GitHub account | Strongly recommended | Needed for GitHub repos, cloud tasks, PRs, and code review workflows | Codex cloud works best after your repository is pushed to GitHub. |
| Workspace or organization access | Project-dependent | Needed for company repos, RBAC, SSO, Slack, Linear, or managed policy | Enterprise admins may control which Codex surfaces, plugins, and permissions are available. |

Use multi-factor authentication for accounts connected to source code, especially if you use cloud tasks.

### 2.3 Required Local Software

| Software | Minimum purpose | Beginner recommendation |
| --- | --- | --- |
| Codex app | Main local Codex interface | Install first on macOS or Windows. |
| Codex CLI | Terminal interface and automation entry point | Install after the app, then run `codex login`. |
| Git | Version control, diffs, branches, worktrees, rollbacks | Required for serious Codex work. |
| Code editor or IDE | Manual review and editing | VS Code, Cursor, Windsurf, JetBrains IDEs, or your preferred editor. |
| Project runtime | Lets Codex run your app and tests | Examples: Node.js, Python, Java, .NET, Go, Rust, Ruby, PHP. |
| Package manager | Installs project dependencies | Examples: npm, pnpm, yarn, pip, poetry, uv, cargo, go, Maven, Gradle. |
| Test and lint tools | Lets Codex verify work | Examples: pytest, vitest, jest, ruff, eslint, mypy, go test, cargo test. |
| Web browser | App preview, docs, auth flows | Chrome is useful if you plan to use the Codex Chrome extension. |
| Terminal shell | Running commands, dev servers, Git, Codex CLI | zsh, bash, PowerShell, Windows Terminal, or WSL shell. |

### 2.4 Strongly Recommended Developer Utilities

These are not all Codex-specific, but they make independent project work much smoother.

| Utility | Why it helps |
| --- | --- |
| `gh` GitHub CLI | View PRs, issues, checks, review comments, and CI logs from the terminal. |
| `rg` ripgrep | Fast code search. Codex and humans both benefit from it. |
| `jq` | Inspect JSON output from APIs, CLIs, and `codex exec --json`. |
| Docker or Podman | Run databases, services, and isolated dev environments. |
| Make or task runner | Standardizes repeated commands like test, lint, build, seed, run. |
| Language version manager | Keeps project runtime versions stable. Examples: nvm, fnm, pyenv, uv, mise, asdf, rustup. |
| Database clients | Needed when your app depends on Postgres, SQLite, MySQL, Redis, etc. |
| Cloud CLIs | Needed for deployed apps. Examples: `az`, `aws`, `gcloud`, `flyctl`, `vercel`, `railway`. |
| Pre-commit tooling | Catches formatting, lint, and secret mistakes before commits. |

### 2.5 Optional Codex Capabilities

| Capability | Use when | Setup surface |
| --- | --- | --- |
| In-app browser and Browser plugin | You are building web pages, local apps, dashboards, or static files that do not need login | Codex app settings and plugin setup |
| Codex Chrome extension | You need Codex to use your signed-in Chrome profile or browser extensions | Codex app Plugins, then Chrome Web Store setup |
| Computer Use | You need Codex to inspect or operate a desktop app visually | Codex app settings, OS permissions |
| MCP servers | Codex needs external tools or live context such as GitHub, Figma, Sentry, Linear, docs, or internal systems | `codex mcp` or `~/.codex/config.toml` |
| Skills | You repeat a workflow and want Codex to follow a reusable process | `.agents/skills`, `$HOME/.agents/skills`, or skill installer |
| Plugins | You want installable bundles of skills, apps, MCP config, or workflow assets | Codex app plugin directory or CLI plugin browser |
| Automations | You want scheduled checks, reminders, recurring triage, or thread wakeups | Codex app Automations |
| Subagents | You want parallel read-heavy work, multiple reviewers, or specialized agents | Prompt Codex explicitly or configure agents |
| GitHub Action | You want Codex in CI/CD | GitHub Actions workflow using `openai/codex-action@v1` |
| SDK | You want to build an internal tool around Codex | TypeScript or Python Codex SDK |

### 2.6 Complete Tool Inventory By Use Case

Use this as a shopping list. You do not need every item for every project.

| Use case | Tools, software, or apps |
| --- | --- |
| Local Codex work | Codex app, Codex CLI, Codex IDE extension |
| Remote Codex work | Codex web, cloud environments, GitHub connection |
| Version control | Git, GitHub, GitHub CLI `gh`, branch protection, pull requests |
| Editing | VS Code, Cursor, Windsurf, JetBrains IDEs, or another editor |
| Terminal work | macOS Terminal, iTerm2, Windows Terminal, PowerShell, WSL shell, bash, zsh |
| Search and inspection | `rg`, `jq`, language-aware grep/search inside your editor |
| JavaScript and TypeScript projects | Node.js, npm, pnpm, yarn, eslint, prettier, jest, vitest, Playwright |
| Python projects | Python, uv or pip, virtual environments, pytest, ruff, mypy, pyright |
| Go projects | Go toolchain, `go test`, `gofmt`, `golangci-lint` |
| Rust projects | Rustup, cargo, rustfmt, clippy |
| Java and JVM projects | JDK, Maven or Gradle, JUnit, project formatter |
| .NET projects | .NET SDK, NuGet, `dotnet test`, `dotnet format` |
| Databases and services | SQLite, Postgres, MySQL, Redis, Docker or Podman, database GUI/CLI clients |
| Frontend verification | Codex in-app browser, Browser plugin, Chrome, Codex Chrome extension, Playwright |
| Desktop or GUI verification | Computer Use plugin, macOS Screen Recording and Accessibility permissions, Windows visible desktop session |
| External systems | MCP servers, app connectors, GitHub, Linear, Slack, Google Drive, Gmail, Figma, Sentry, internal docs |
| Repeatable workflows | `AGENTS.md`, skills, plugins, rules, hooks, automations |
| CI/CD | GitHub Actions, Codex GitHub Action, `codex exec`, secrets manager, artifact upload/download |
| Deployment | Cloud provider CLI, hosting CLI, environment manager, logs and monitoring tools |
| Security | Secret scanner, dependency scanner, Codex Security plugin where available, MFA, least-privilege tokens |

## 3. Installation Checklist

### 3.1 Install Codex App

1. Download and install the Codex app for macOS or Windows.
2. Open Codex.
3. Sign in with your ChatGPT account or an OpenAI API key.
4. Add your first project folder.
5. Start in Local mode for your first task.

Use the app first if you want a visual diff, integrated terminal, worktrees, browser previews, automations, and easier review.

### 3.2 Install Codex CLI

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

### 3.3 Install Editor Integration

Use the Codex IDE extension when you want Codex inside your editor.

Supported editor families in the current docs include VS Code, Cursor, Windsurf, and other VS Code-compatible editors. JetBrains IDEs have a JetBrains integration.

After installing, sign in with ChatGPT or an API key. The IDE extension shares Codex configuration with the CLI through `~/.codex/config.toml`.

### 3.4 Connect GitHub for Cloud Work

For Codex web and cloud tasks:

1. Go to Codex on ChatGPT: `https://chatgpt.com/codex`.
2. Connect GitHub.
3. Create or select a cloud environment for the repository.
4. Add setup scripts, package versions, environment variables, and secrets as needed.
5. Push your repository to GitHub before delegating cloud tasks.

Cloud tasks run in containers. Setup scripts can access the internet to install dependencies. The agent phase is offline by default unless you enable internet access for that environment.

### 3.5 Platform Notes

| Platform | What to know |
| --- | --- |
| macOS | Codex sandboxing works with built-in macOS mechanisms. Grant extra permissions only when a task needs them, such as Computer Use or access to protected folders. |
| Windows | Prefer the native Windows sandbox when available. Use WSL2 when your tools or repositories already live in Linux. Windows 11 is the best baseline. |
| Linux and WSL2 | Install `bubblewrap` with your package manager for reliable sandboxing. Keep WSL repositories under the Linux home directory for better performance. |
| Cloud | Configure setup scripts, package versions, environment variables, secrets, and internet policy in the Codex cloud environment. |

## 4. First Project Setup

Run this checklist in every project you want to use with Codex.

### 4.1 Make the Project Git-backed

Codex works best when Git can show what changed and let you roll back.

```bash
git status
git branch --show-current
```

If the project is not a Git repository yet:

```bash
git init
git add .
git commit -m "Initial commit"
```

Do not let Codex make broad edits in an untracked folder unless you have backups.

### 4.2 Document Project Commands

Create or update a project guide with the commands Codex should use.

At minimum, know:

```text
Install dependencies:
Run the app:
Run tests:
Run lint:
Run type checks:
Format code:
Build production artifact:
Important environment variables:
Where logs appear:
```

### 4.3 Create `AGENTS.md`

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

### 4.4 Add a Local Environment for the Codex App

In the Codex app, local environments can define setup scripts and common actions for worktrees. Use them for commands such as:

```bash
npm install
npm run build
npm test
npm run dev
```

This matters because Codex worktrees are separate checkouts. They may need dependencies installed before the app can run.

### 4.5 Protect Local Secrets

Keep secrets out of Git and out of prompts.

Recommended patterns:

```gitignore
.env
.env.*
!.env.example
```

If Codex-managed worktrees need ignored setup files, use `.worktreeinclude` carefully:

```text
# .worktreeinclude
.env.local
config/local-development.json
```

Only include files that are truly needed for local worktree setup. Review this file before sharing it.

## 5. Codex Configuration Basics

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

### 5.1 Practical Starter Config

```toml
model = "gpt-5.5"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "cached"

[features]
memories = true
goals = true
```

This is a practical default for trusted local repositories:

- `workspace-write` lets Codex edit inside the workspace.
- `on-request` makes Codex ask before crossing sandbox boundaries.
- `cached` web search reduces exposure to live web prompt injection.
- `memories` helps Codex reuse prior context if you are comfortable with local memory storage.
- `goals` enables longer-running objective tracking.

Use `read-only` for planning, code review, unfamiliar repos, or sensitive projects.

### 5.2 Models

As of the current Codex docs:

| Model | Use for |
| --- | --- |
| `gpt-5.5` | Default starting point for complex coding, research, tool use, planning, and computer use |
| `gpt-5.4-mini` | Faster, lower-cost lighter coding tasks and subagents |
| `gpt-5.3-codex-spark` | Near-instant text iteration for eligible ChatGPT Pro subscribers, research preview |

Model availability can change. If you are reading this later, confirm current model guidance in the Codex docs before standardizing a team setup.

### 5.3 Permissions and Sandboxing

Understand these terms before giving Codex more autonomy.

| Concept | Meaning |
| --- | --- |
| Sandbox mode | What Codex can technically access when it runs commands |
| Approval policy | When Codex must ask before taking an action |
| Network access | Whether spawned commands can reach the internet |
| Rules | Command-specific allow, prompt, or forbid decisions |
| Permissions profiles | Reusable filesystem and network policies |

Common modes:

| Mode | Use when |
| --- | --- |
| `read-only` | You want Codex to inspect, explain, plan, or review without edits |
| `workspace-write` | You want normal local coding inside the current project |
| `danger-full-access` | You are in a controlled environment and intentionally want broad access |

Default local network access is off in the `workspace-write` sandbox unless enabled in config. Enable network only when needed, and prefer scoped domain rules over broad access.

## 6. Topics To Learn For Independent Work

You do not need to master everything before starting. Learn in this order.

### 6.1 Git Fundamentals

You should be comfortable with:

- `git status`
- `git diff`
- `git add`
- `git commit`
- `git branch`
- `git switch`
- `git pull --rebase`
- `git push`
- reading merge conflicts
- creating and reviewing pull requests
- using `.gitignore`
- recovering with Git before deleting files

Why it matters: Codex edits real files. Git is your safety net, review surface, and collaboration layer.

### 6.2 Terminal Basics

Learn:

- current directory: `pwd`
- list files: `ls`
- change directory: `cd`
- search files: `rg`
- run scripts: `npm test`, `python -m pytest`, etc.
- read logs
- stop a command with `Ctrl+C`
- understand exit codes
- use environment variables for local commands

Why it matters: Codex runs the same commands your project uses. If you can read the terminal, you can verify Codex instead of blindly trusting it.

### 6.3 Project Runtime and Package Manager

For each project, know:

- language and version
- package manager
- install command
- dev server command
- test command
- lint command
- build command
- where configuration lives
- what files are generated

Examples:

```bash
npm install
npm run dev
npm test
npm run lint
```

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest
```

### 6.4 Prompting Codex

A good Codex prompt has four parts:

| Part | Example |
| --- | --- |
| Goal | "Add password reset email support." |
| Context | "Relevant files are `src/auth/*`, `docs/auth.md`, and the failing test output below." |
| Constraints | "Do not add a new email provider. Keep API compatibility." |
| Done when | "Tests pass, docs mention the new behavior, and the diff is reviewed." |

Example:

```text
Add CSV export to the transactions page.

Context:
- UI lives in `src/pages/transactions.tsx`.
- Existing export helpers are in `src/lib/export.ts`.
- Follow the table filters already applied on screen.

Constraints:
- Do not add a new dependency.
- Keep the button accessible.
- Preserve existing tests.

Done when:
- Add or update tests.
- Run the relevant test command.
- Summarize the final diff and any risks.
```

### 6.5 Plan Mode and Goal Mode

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

### 6.6 Code Review and Diffs

Learn to inspect:

- file list
- per-file diff
- staged vs unstaged changes
- last-turn changes
- tests added or changed
- docs updated
- generated files
- dependency changes

Use `/review` before committing substantial work.

### 6.7 Testing and Verification

Codex should verify its work when possible. You need to know what verification is meaningful.

Common checks:

```bash
npm test
npm run lint
npm run typecheck
npm run build
python -m pytest
ruff check .
mypy .
go test ./...
cargo test
```

Ask Codex to run the narrowest relevant checks first, then broader checks before a PR.

### 6.8 Debugging

Learn to provide:

- exact error message
- command that failed
- stack trace
- expected behavior
- actual behavior
- reproduction steps
- recent changes
- logs

Good debugging prompt:

```text
`npm test` fails with the stack trace below. Reproduce it, identify the root cause, make the smallest fix, and rerun the failing test first. Do not refactor unrelated code.
```

### 6.9 Web and UI Verification

For frontend work, learn:

- start the dev server
- find the local URL
- inspect browser console errors
- test desktop and mobile widths
- compare screenshots
- check accessibility basics
- use the in-app browser for localhost and public pages without login
- use Chrome extension only when signed-in browser state is required

### 6.10 Security and Privacy

Know these rules cold:

- Do not paste secrets into prompts.
- Do not commit `.env`, tokens, keys, private exports, or credentials.
- Review network access requests.
- Treat web pages, GitHub issues, Slack threads, docs, and browser content as untrusted input.
- Use read-only mode for unfamiliar repositories.
- Use full access only in trusted and controlled environments.
- Review logs before sharing them.
- Keep MFA enabled on accounts connected to code.

### 6.11 `AGENTS.md`, Skills, Plugins, and MCP

Use the smallest durable surface that matches the job:

| Need | Use |
| --- | --- |
| One-off instruction | Prompt |
| Repo rule | `AGENTS.md` |
| Personal default | `~/.codex/AGENTS.md` |
| Reusable workflow | Skill |
| Installable workflow bundle | Plugin |
| External data or action | MCP server or app connector |
| Scheduled recurring task | Automation |
| Command enforcement | Rules or hooks |

### 6.12 Worktrees and Cloud Environments

Learn worktrees when you want parallel local work without disturbing your current checkout.

Learn cloud environments when you want Codex to work remotely on GitHub-backed repositories. A good cloud environment has:

- setup script
- package versions
- required tools
- environment variables
- secrets needed during setup
- internet access policy
- clear `AGENTS.md`

### 6.13 Automation and CI

Learn:

- `codex exec`
- JSONL output with `codex exec --json`
- GitHub Actions basics
- secret scoping
- patch artifacts
- PR creation workflows
- least privilege permissions

Use the official Codex GitHub Action for GitHub workflows instead of hand-rolling API key exposure in shell steps.

## 7. Daily Codex Workflows

### 7.1 Understand a New Codebase

Prompt:

```text
Inspect this repository and explain:
1. What it does.
2. How the main modules fit together.
3. How to run it locally.
4. How to test it.
5. What files I should read first.

Do not edit files.
```

Follow-up:

```text
Create or update `AGENTS.md` with the verified run/test/lint commands and the main repo layout. Keep it concise.
```

### 7.2 Make a Small Feature

Prompt:

```text
Implement [feature].

Use existing patterns in this repo. Keep the diff small. Add or update tests if behavior changes. Run the relevant checks and summarize what changed.
```

Human review:

```bash
git diff
git status
```

### 7.3 Fix a Bug

Prompt:

```text
Reproduce this bug using the steps below, identify the root cause, and make the smallest safe fix. Start by explaining the likely area to inspect. After editing, rerun the failing case and any related tests.
```

Add:

- reproduction steps
- expected behavior
- actual behavior
- logs
- screenshots if useful

### 7.4 Review Before Commit

Prompt:

```text
/review
```

Or:

```text
Review the uncommitted changes for bugs, regressions, missing tests, and risky assumptions. Prioritize findings by severity with file references. Do not edit files.
```

### 7.5 Prepare a Pull Request

Prompt:

```text
Review the current diff, run the relevant checks, then draft a concise PR description with summary, tests, and risks. Do not commit until I confirm.
```

### 7.6 Use Codex Cloud

Use cloud when:

- the repo is pushed to GitHub
- the task can run in a configured environment
- you want parallel attempts
- you want Codex to open a PR
- you are away from your local machine

Avoid cloud when:

- the task depends on unpushed local files
- local secrets are required during agent execution
- the environment is not set up
- you need desktop app or signed-in local browser state

### 7.7 Use Browser Verification

Prompt:

```text
Start the dev server, open the page in the in-app browser, verify the bug visually at desktop and mobile widths, fix it, and re-check the same route.
```

Use the in-app browser for local development servers and public pages without login. Use Chrome extension for signed-in sites.

### 7.8 Use Computer Use

Prompt:

```text
Use Computer Use to open the desktop app, reproduce the onboarding bug, and note the exact UI state. Then inspect the code, make the smallest fix, and repeat the same UI flow.
```

Keep Computer Use tasks narrow. Stay present for sensitive account, payment, credential, privacy, or security flows.

## 8. Command Cheat Sheet

### 8.1 Codex CLI

```bash
codex
codex "Explain this codebase"
codex --version
codex login
codex logout
codex doctor
codex resume
codex resume --last
codex -m gpt-5.5
codex --sandbox workspace-write --ask-for-approval on-request
codex --sandbox read-only --ask-for-approval on-request
codex completion zsh
codex features list
codex mcp --help
codex app
```

### 8.2 Non-interactive Codex

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

### 8.3 Git

```bash
git status
git diff
git diff --staged
git add path/to/file
git commit -m "Message"
git switch -c feature/name
git pull --rebase
git push -u origin feature/name
```

### 8.4 GitHub CLI

```bash
gh auth login
gh pr status
gh pr view --web
gh pr checks
gh run list
gh run view --log
gh issue view 123
```

### 8.5 Useful Search

```bash
rg "functionName"
rg --files
rg -n "TODO|FIXME"
```

## 9. Safety Checklist

Before letting Codex edit:

- The project is in Git.
- You know the current branch.
- You know whether there are unrelated local changes.
- You have a clear prompt and done criteria.
- You selected the right mode: Local, Worktree, or Cloud.
- You selected the right permission level.

Before approving a command:

- Read what command will run.
- Check whether it touches files outside the project.
- Check whether it uses network access.
- Check whether it can delete, overwrite, upload, or expose data.
- Prefer approving once over always approving if unsure.

Before committing:

- Inspect `git diff`.
- Run relevant checks.
- Confirm no secrets are included.
- Confirm generated files are intentional.
- Confirm docs/help changed if behavior changed.
- Use a clear commit message.

Before sharing logs or transcripts:

- Search for secrets, tokens, private URLs, email addresses, customer data, and internal names.
- Remove sensitive material.
- Prefer minimal excerpts over full logs.

## 10. Troubleshooting

| Problem | What to check |
| --- | --- |
| Codex edited files you did not expect | Check Git diff. Ask Codex for last-turn changes. Revert only the unwanted hunks. |
| Codex cannot run tests | Confirm dependencies are installed, the working directory is correct, and the test command is documented. |
| Worktree code does not run | Add setup scripts in local environments, or use `.worktreeinclude` for required ignored local files. |
| Cloud task fails during setup | Check setup script, package versions, environment variables, and secrets. Reset the environment cache after config changes. |
| Login fails | Run `codex login`, try device auth on headless machines, inspect login logs, check corporate CA settings. |
| CLI works but app behaves differently | Compare bundled versions with `codex --version` and the app's bundled Codex version. Experimental features may appear first in one surface. |
| Browser task cannot access signed-in page | Use Chrome extension instead of the in-app browser. |
| Codex cannot use Chrome | Confirm Chrome plugin is installed and enabled, extension shows Connected, correct Chrome profile is active, and site is not blocked. |
| Computer Use cannot see or click | On macOS, check Screen Recording and Accessibility permissions. On Windows, keep the target app visible. |
| Thread feels stuck | Check for approval prompts, open terminal, run `git status`, or start a smaller new thread. |
| Context is too large | Ask Codex to summarize, split the task, use subagents for read-heavy work, or start a fresh focused thread. |

## 11. Learning Plan

### Week 1: Local Confidence

- Install Codex app and CLI.
- Open one Git-backed project.
- Ask Codex to explain the repo.
- Create `AGENTS.md`.
- Run one small read-only review.
- Make one small change and inspect the diff manually.

### Week 2: Verification

- Learn project test/lint/build commands.
- Ask Codex to fix a small bug.
- Ask Codex to add or update a test.
- Use `/review` before committing.
- Practice reverting a hunk you do not want.

### Week 3: Better Context

- Add better `AGENTS.md` instructions.
- Configure `~/.codex/config.toml`.
- Try worktrees in the Codex app.
- Try the in-app browser on a local route.
- Use images or screenshots as prompt context.

### Week 4: Automation and Integrations

- Install `gh` and authenticate.
- Try `codex exec` for a read-only task.
- Configure one MCP server if useful.
- Create or install one skill.
- Set up one small automation or CI experiment.
- Try Codex cloud on a pushed GitHub repo.

## 12. Good Prompt Templates

### Explain

```text
Explain this codebase/module for a new maintainer. Focus on architecture, data flow, important files, and how to run tests. Do not edit files.
```

### Plan

```text
Plan the smallest safe implementation for [task]. Inspect the repo first, identify affected files, note risks, and ask questions if anything is ambiguous. Do not edit files until the plan is clear.
```

### Implement

```text
Implement [task]. Follow existing patterns, keep the diff scoped, update tests/docs if behavior changes, run relevant checks, and summarize the result.
```

### Debug

```text
Reproduce the failure from the logs below, identify the root cause, make the smallest fix, rerun the failing check, and explain why the fix works.
```

### Review

```text
Review the current diff for bugs, regressions, security issues, missing tests, and unclear behavior. Findings first, ordered by severity. Do not edit files.
```

### Docs

```text
Update the user-facing docs for this behavior change. Keep wording concise, include commands users need, and make sure examples match the implementation.
```

### PR Prep

```text
Inspect the final diff, run the relevant checks, then draft a PR description with summary, test results, risk, and rollout notes.
```

## 13. When To Use Each Codex Surface

| Task | Best surface |
| --- | --- |
| Explore a repo locally | App, CLI, or IDE |
| Make a focused code change | App, CLI, or IDE |
| Work beside editor context | IDE extension |
| Run multiple local attempts safely | Codex app worktrees |
| Review a visual web page | Codex app in-app browser |
| Use signed-in websites | Chrome extension |
| Operate a desktop app | Computer Use |
| Run a task from another device | Codex web/cloud |
| Review GitHub PRs | GitHub integration or `/review` locally |
| Schedule recurring checks | Automations |
| Script a repeatable prompt | `codex exec` |
| Build an internal tool | Codex SDK or app-server |
| Connect external systems | MCP, app connectors, plugins |

## 14. Official References

Use these as the source of truth when details drift:

- [Codex overview](https://developers.openai.com/codex/overview)
- [Codex quickstart](https://developers.openai.com/codex/quickstart)
- [Codex app](https://developers.openai.com/codex/app)
- [Codex CLI](https://developers.openai.com/codex/cli)
- [Codex IDE extension](https://developers.openai.com/codex/ide)
- [Codex cloud](https://developers.openai.com/codex/cloud)
- [Authentication](https://developers.openai.com/codex/auth)
- [Config basics](https://developers.openai.com/codex/config-basic)
- [Models](https://developers.openai.com/codex/models)
- [Approvals and security](https://developers.openai.com/codex/agent-approvals-security)
- [Sandboxing](https://developers.openai.com/codex/concepts/sandboxing)
- [Prompting](https://developers.openai.com/codex/prompting)
- [Best practices](https://developers.openai.com/codex/learn/best-practices)
- [AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [Skills](https://developers.openai.com/codex/skills)
- [Plugins](https://developers.openai.com/codex/plugins)
- [MCP](https://developers.openai.com/codex/mcp)
- [Automations](https://developers.openai.com/codex/app/automations)
- [Worktrees](https://developers.openai.com/codex/app/worktrees)
- [In-app browser](https://developers.openai.com/codex/app/browser)
- [Chrome extension](https://developers.openai.com/codex/app/chrome-extension)
- [Computer Use](https://developers.openai.com/codex/app/computer-use)
- [GitHub Action](https://developers.openai.com/codex/github-action)
- [SDK](https://developers.openai.com/codex/sdk)
- [Non-interactive mode](https://developers.openai.com/codex/noninteractive)
- [Windows](https://developers.openai.com/codex/windows)
- [Open source Codex CLI](https://github.com/openai/codex)

## 15. Final Beginner Advice

Start small. Ask Codex to explain before you ask it to edit. Keep every project in Git. Write down the real commands in `AGENTS.md`. Give clear done criteria. Review diffs. Let Codex run tests, but learn to understand the output yourself.

The goal is not to make Codex do mysterious magic. The goal is to build a working loop where you can describe intent, Codex can act, your tools can verify, and you can confidently accept, steer, or reject the result.
