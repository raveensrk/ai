# Claude Starter Pack — 2026 Edition

*A practical user guide to everything you need to start building with Claude and working independently on your projects.*

---

## How to use this guide

This guide is organized as a path, not a reference dump. If you read it top to bottom you'll go from "nothing installed" to "comfortable shipping work with Claude." If you already have the basics, jump to the section you need using the table of contents.

- **Sections 1–2** — orientation: what Claude is, which surface to use, which model to pick.
- **Sections 3–4** — the toolkit: every tool/app to install, and how to set up Claude Code.
- **Sections 5–7** — the concepts and workflows you need to work independently.
- **Sections 8–12** — leveling up: prompting, customization, cost, security, troubleshooting.
- **Sections 13–16** — a learning roadmap, cheat sheet, glossary, and links.

> **Legend:** 🟢 = do this first · ⚙️ = configuration · 💡 = tip · ⚠️ = watch out

---

## Table of contents

1. [What is Claude (and what's in the box)](#1-what-is-claude-and-whats-in-the-box)
2. [Choosing your model](#2-choosing-your-model)
3. [The toolkit — what to install](#3-the-toolkit--what-to-install)
4. [Setting up Claude Code](#4-setting-up-claude-code)
5. [Core concepts you must know](#5-core-concepts-you-must-know)
6. [Essential workflows](#6-essential-workflows)
7. [Working effectively (prompting)](#7-working-effectively-prompting)
8. [Configuration & customization](#8-configuration--customization)
9. [Plans, pricing & cost control](#9-plans-pricing--cost-control)
10. [Security & safety](#10-security--safety)
11. [Troubleshooting & getting help](#11-troubleshooting--getting-help)
12. [Your 2-week learning roadmap](#12-your-2-week-learning-roadmap)
13. [Cheat sheet](#13-cheat-sheet)
14. [Glossary](#14-glossary)
15. [Resources & links](#15-resources--links)

---

## 1. What is Claude (and what's in the box)

**Claude** is Anthropic's family of AI models. You don't interact with the model directly — you use a **surface** (an app or interface) that talks to it. Picking the right surface for the job is the single most important orientation decision.

| Surface | What it is | Best for | Where |
|---|---|---|---|
| **Claude apps** (web / desktop / mobile) | Chat interface with file uploads, projects, web search, connectors | Everyday Q&A, writing, research, brainstorming, document analysis | [claude.ai](https://claude.ai), Mac/Windows desktop apps, iOS/Android |
| **Claude Code** | An agentic coding assistant that runs in your terminal, IDE, or browser and can read/write files and run commands | Building software, automating repo work, multi-step tasks on real projects | CLI, VS Code/JetBrains extensions, [claude.ai/code](https://claude.ai/code) |
| **Claude Developer Platform (API)** | Programmatic access to the models for your own apps | Building AI features into your own product | [platform.claude.com](https://platform.claude.com) (the Console) |
| **Claude in Chrome** | A browser extension that lets Claude see and act in your browser | Web tasks, navigating and filling web apps | Chrome extension |
| **Claude Agent SDK** | A toolkit for building your own custom agents on the same harness Claude Code uses | Custom autonomous agents and workflows | npm / PyPI packages |

> 💡 **Mental model:** The *apps* are for thinking and writing. *Claude Code* is for doing work on your computer/projects. The *API* is for putting Claude inside something you build. Most people developing a project live primarily in **Claude Code** and reach for the apps and API as needed.

### Where this guide focuses

Since you're working on a project, this guide centers on **Claude Code** — the surface that can actually read your files, run your tests, and make changes — while pointing you to the apps and API where they fit.

---

## 2. Choosing your model

Each surface lets you choose a model. They trade off intelligence, speed, and cost. As of mid‑2026 these are the current models:

| Model | Model ID | Tier | Context window | Relative cost | Use it for |
|---|---|---|---|---|---|
| **Claude Fable 5** | `claude-fable-5` | Most capable | 1M tokens | Highest | The hardest reasoning and long‑horizon agentic work |
| **Claude Opus 4.8** | `claude-opus-4-8` | Flagship (default) | 1M tokens | High | Most coding, agentic work, and complex reasoning |
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | Balanced | 1M tokens | Medium | High‑volume work where speed/cost matter |
| **Claude Haiku 4.5** | `claude-haiku-4-5` | Fast & cheap | 200K tokens | Lowest | Simple, latency‑sensitive, or high‑frequency tasks |

**How to choose, in one line:** default to **Opus 4.8**. Drop to **Sonnet 4.6** when you're doing lots of straightforward work and want it cheaper/faster. Use **Haiku 4.5** for simple, repetitive tasks. Reach for **Fable 5** only when a task is genuinely at the frontier of difficulty (it costs more than Opus).

> ⚠️ **Pricing changes.** Always confirm current numbers at [platform.claude.com/pricing](https://platform.claude.com/docs/en/pricing). As a snapshot (per million tokens, input/output): Fable 5 ≈ $10/$50, Opus 4.8 ≈ $5/$25, Sonnet 4.6 ≈ $3/$15, Haiku 4.5 ≈ $1/$5.

### A word on "effort" and "thinking"

Modern Claude models *think* before answering and you can tune how hard.

- **Adaptive thinking** is the default — Claude decides when and how much to reason.
- **Effort** (`low` / `medium` / `high` / `xhigh` / `max`) controls depth and token spend. Claude Code defaults to a high setting for coding. Higher effort = smarter but slower and more expensive. `high` is the usual sweet spot; `max` for "correctness matters more than cost."
- **Fast mode** (toggle with `/fast` in Claude Code, on Opus 4.8/4.7) runs the *same* model with faster output at premium pricing — it does **not** downgrade you to a smaller model.

---

## 3. The toolkit — what to install

This is the "starter pack" itself. Here's everything you need, grouped by how essential it is.

### 3.1 Essentials (🟢 install these first)

| Tool | What it's for | How to get it |
|---|---|---|
| **A terminal** | Where Claude Code runs | Built in: macOS *Terminal*/[iTerm2](https://iterm2.com), Windows *Windows Terminal*/WSL, Linux your shell |
| **Node.js (LTS)** | Runtime for the Claude Code CLI and many MCP servers | [nodejs.org](https://nodejs.org) — install the LTS (v20+). Tip: use [nvm](https://github.com/nvm-sh/nvm) to manage versions |
| **Git** | Version control — Claude Code is built around it | [git-scm.com](https://git-scm.com) (preinstalled on most Macs) |
| **Claude Code** | The agentic coding tool | `npm install -g @anthropic-ai/claude-code` (see §4) |
| **A Claude account** | Authentication | Sign up at [claude.ai](https://claude.ai); a Pro/Max plan or API credits unlocks Claude Code |
| **A code editor** | Editing, and the IDE integration | [VS Code](https://code.visualstudio.com), [Cursor](https://cursor.com), or [JetBrains](https://www.jetbrains.com) IDEs |

### 3.2 Strongly recommended

| Tool | What it's for | How to get it |
|---|---|---|
| **GitHub account** | Hosting code, pull requests, collaboration | [github.com](https://github.com) |
| **GitHub CLI (`gh`)** | Lets Claude Code create PRs/issues and run GitHub ops for you | [cli.github.com](https://cli.github.com) — then `gh auth login` |
| **Claude desktop app** | Chat + connectors + (on Mac/Windows) a home for Claude Code | [claude.ai/download](https://claude.ai/download) |
| **Claude mobile app** | Claude on the go; review and kick off work from your phone | App Store / Google Play |
| **A package manager** | Installing the above cleanly | macOS: [Homebrew](https://brew.sh); Windows: [winget](https://learn.microsoft.com/windows/package-manager/)/[Scoop](https://scoop.sh) |

### 3.3 Optional / situational

| Tool | When you need it |
|---|---|
| **Python + pip/uv** | Python projects, or Python‑based MCP servers ([uv](https://github.com/astral-sh/uv) is a fast modern installer) |
| **Docker** | Running services/databases locally, or sandboxing agent work |
| **MCP servers** | Connecting Claude to external tools/data — GitHub, Figma, databases, Slack, etc. (see §5.7) |
| **Claude in Chrome extension** | Letting Claude operate inside your browser |
| **IDE extension** (VS Code/JetBrains) | Inline diffs, in‑editor Claude Code, and "@‑mention" of selections |
| **Claude Agent SDK** | Building your own agents (`@anthropic-ai/claude-agent-sdk` / `claude-agent-sdk` on PyPI) |
| **Anthropic SDKs** | Calling the API from code: `anthropic` (Python), `@anthropic-ai/sdk` (TS), plus Java/Go/Ruby/C#/PHP |

### 3.4 The 5‑minute setup checklist

```text
[ ] Install Node.js LTS         → node --version   (expect v20+)
[ ] Install Git                 → git --version
[ ] Install Claude Code         → npm install -g @anthropic-ai/claude-code
[ ] (Recommended) Install gh    → gh auth login
[ ] Open your project           → cd ~/path/to/project
[ ] Start Claude Code           → claude
[ ] Authenticate                → follow the /login browser prompt
[ ] Generate project memory     → /init
[ ] Ask something small         → "explain what this repo does"
```

---

## 4. Setting up Claude Code

### 4.1 Install

```bash
# Recommended: npm (cross-platform)
npm install -g @anthropic-ai/claude-code

# Then launch from any project directory
cd your-project
claude
```

Alternatives: a **native installer** (`curl -fsSL https://claude.ai/install.sh | bash` on macOS/Linux) and platform package managers. The native install auto‑updates itself. Use whichever you prefer — npm is the most portable.

### 4.2 Authenticate

On first run, Claude Code prompts you to log in. You have two options:

1. **Subscription (Pro or Max)** — log in with your Claude account via the browser. Usage counts against your plan. Best for individuals doing regular interactive work.
2. **API key (pay‑as‑you‑go)** — create a key in the [Console](https://platform.claude.com) and use it. You pay per token. Best for teams, automation, and predictable billing.

Switch later with `/login` and `/logout`.

### 4.3 First commands

| Command | Does |
|---|---|
| `/init` | Scans the repo and writes a `CLAUDE.md` describing it (do this once per project) |
| `/model` | Pick which model to use |
| `/help` | List commands |
| `/status` | Show account, model, and session info |
| `/clear` | Start a fresh conversation (clears context) |

### 4.4 How a session works

- Type a request in plain English. Claude reads files, runs commands, and edits code to accomplish it.
- It asks permission before doing anything consequential (writing files, running commands) unless you've allowed that action.
- `@` mentions a file (`@src/app.ts`), `#` saves something to memory, and a leading `!` runs a raw shell command.
- Press **Esc** to interrupt; press **Esc twice** to rewind to an earlier point in the conversation.
- **Shift+Tab** cycles permission modes (normal → auto‑accept edits → plan mode).

---

## 5. Core concepts you must know

These are the topics that take you from "typing prompts" to *working independently*. Learn these and you can drive Claude Code confidently on a real project.

### 5.1 The agentic loop

Claude Code isn't a chatbot that returns text — it's an **agent**. Given a goal, it plans, takes actions (read, search, edit, run), observes the results, and repeats until the task is done. Your job shifts from "writing code" to **specifying intent, reviewing, and steering.** Give it a clear goal and the context it needs, then verify the result.

### 5.2 Context & context management

Claude can only "see" what's in its **context window** (its working memory for the session). Big takeaways:

- More relevant context = better results. Point Claude at the right files (`@`), paste error messages, describe the goal.
- Context is finite. Long sessions fill up. Use **`/clear`** to start fresh between unrelated tasks, and **`/compact`** to summarize a long session and keep going.
- Don't dump your whole codebase in — relevance beats volume.

### 5.3 `CLAUDE.md` — project memory

`CLAUDE.md` is a file Claude Code automatically reads at the start of every session. Put durable project knowledge here: how to build/test, conventions, architecture notes, "always do X / never do Y." There are three levels:

| Location | Scope |
|---|---|
| `./CLAUDE.md` (project root) | This project; commit it so your team shares it |
| `~/.claude/CLAUDE.md` | You, across all projects (personal preferences) |
| `./CLAUDE.local.md` | This project, just you (gitignored) |

Generate the first one with `/init`, then edit it as you learn what Claude keeps getting wrong.

### 5.4 Permissions & safety modes

Claude Code asks before doing risky things. You control how much it asks:

| Mode | Behavior |
|---|---|
| **Normal** (default) | Asks before edits and commands |
| **Auto‑accept edits** | Applies file edits without asking (still asks for commands) |
| **Plan mode** | Read‑only: Claude investigates and proposes a plan but changes nothing until you approve |
| **Bypass** (`--dangerously-skip-permissions`) | No prompts — ⚠️ only in a sandbox/throwaway environment |

You can also pre‑approve specific commands (an *allowlist*) so you stop getting prompted for safe, routine ones.

### 5.5 Slash commands

Built‑in shortcuts typed as `/name`. The essentials:

`/init` · `/clear` · `/compact` · `/model` · `/config` · `/login` · `/logout` · `/cost` · `/resume` · `/agents` · `/mcp` · `/hooks` · `/review` · `/help`

You can also write **custom slash commands** — see §8.

### 5.6 Skills

**Skills** are reusable packets of instructions and scripts that Claude loads *on demand* when relevant — turning a general assistant into a specialist (e.g. a "create a PowerPoint" skill, or your team's "deploy" procedure). They keep expertise out of your way until it's needed. You invoke a skill with its `/name`, and Claude can auto‑load one when a task matches. As you mature, packaging your repeated workflows as skills is one of the highest‑leverage things you can do.

### 5.7 MCP (Model Context Protocol)

**MCP** is the standard way to connect Claude to external tools and data — GitHub, Figma, databases, Slack, your file storage, calendars, and hundreds more. An **MCP server** exposes a capability; Claude Code connects to it and gains new tools.

```bash
# Add an MCP server to Claude Code
claude mcp add <name> -- <command to start the server>

# Manage them in a session
/mcp
```

Think of MCP as Claude's "USB ports" for the outside world. Start without any; add them when a task needs Claude to reach a system it can't otherwise touch.

### 5.8 Subagents

A **subagent** is a separate Claude instance Claude Code spins up to handle a focused sub‑task (e.g. "explore the codebase and report back," or several independent jobs in parallel). They keep the main conversation clean and let work happen concurrently. You can define **custom subagents** (with their own instructions and tool access) in `.claude/agents/`. Manage them with `/agents`.

### 5.9 Hooks

**Hooks** are shell commands the harness runs automatically at lifecycle events — e.g. "run the formatter after every edit," "block edits to this file," "notify me when the task finishes." Hooks are how you encode *automatic* behavior ("whenever X, do Y") because they're executed by the harness, not left to Claude's discretion. Configured in `settings.json`.

### 5.10 Plan mode

For anything non‑trivial, start in **plan mode** (Shift+Tab to it). Claude investigates read‑only and produces a step‑by‑step plan you approve before any change is made. This catches misunderstandings *before* code is touched and is one of the best habits to build.

### 5.11 Git worktrees & background tasks

- **Git worktrees** let Claude work on an isolated copy of your repo so parallel or risky work doesn't disturb your main checkout.
- **Background tasks** let long‑running processes (a dev server, a test watcher) run while you keep working; Claude is notified when they finish.

You don't need these on day one, but knowing they exist saves you later.

---

## 6. Essential workflows

Concrete recipes you'll use constantly.

### 6.1 Starting on a new (to you) codebase

```text
1. cd into the repo, run `claude`
2. /init  → generates CLAUDE.md
3. Ask: "Give me a tour of this codebase: entry points, main modules, how to run it."
4. Ask: "How do I run the tests? Run them and tell me what passes."
```

### 6.2 Making a change (the safe loop)

```text
1. Enter plan mode (Shift+Tab).
2. Describe the goal precisely + point at relevant files with @.
3. Review the plan; refine it.
4. Approve → let Claude implement.
5. Ask it to run tests / the app to verify.
6. Review the diff yourself before committing.
```

### 6.3 Debugging

```text
1. Paste the full error + how to reproduce.
2. Ask Claude to find the root cause BEFORE proposing a fix.
3. Have it write a failing test that reproduces the bug.
4. Then fix, and confirm the test passes.
```

> 💡 Insisting on "diagnose first, fix second" prevents the classic failure mode of patching symptoms.

### 6.4 Committing & pull requests

Claude Code can stage, commit (with a sensible message), push a branch, and open a PR with `gh`. Ask it to — but it will only commit/push when you tell it to. Always review the diff first. (It will branch off `main` rather than committing directly to it.)

### 6.5 Code review

Use `/review`, or ask Claude to review a diff/PR for bugs and improvements before you merge. Treat its review as a sharp second pair of eyes, not gospel — verify its claims.

### 6.6 One‑off / scripted runs (headless)

For automation and CI, run Claude Code non‑interactively:

```bash
claude -p "summarize today's changes and update the CHANGELOG"
```

This "print mode" runs the task and exits — handy for scripts, cron jobs, and pipelines.

---

## 7. Working effectively (prompting)

The difference between frustration and flow is mostly how you communicate. The core skills:

1. **State the goal and the *why*.** "I'm refactoring auth so we can add SSO next sprint. With that in mind, …" Claude uses intent to make better choices.
2. **Give context, not the whole repo.** Point at the 2–3 relevant files. Paste the actual error. Relevance > volume.
3. **Be specific about done.** "It works" is vague. "All tests pass and the `/login` page renders without console errors" is checkable.
4. **Let it plan first** for anything non‑trivial (plan mode).
5. **Iterate in small steps.** One coherent change at a time beats a giant ambiguous ask.
6. **Correct, don't restart.** If it goes wrong, tell it what's wrong and why — it adjusts. Esc‑Esc to rewind if needed.
7. **Ask for a recommendation, not options.** "Which approach should we use and why?" gets you unstuck faster than a survey.
8. **Make rules durable.** If you find yourself repeating an instruction, put it in `CLAUDE.md` (or a hook/skill) so you never repeat it again.

> 💡 **The feedback flywheel:** every time Claude does something you didn't want, ask *why it thought that was right*, then encode the correction in `CLAUDE.md`. Your setup gets sharper every week.

---

## 8. Configuration & customization

As you grow, you'll tailor Claude Code to your workflow. Here's the map of what's customizable and where it lives.

| What | Where | Use it to |
|---|---|---|
| **Settings** | `~/.claude/settings.json` (global) and `./.claude/settings.json` (project) | Permissions/allowlists, env vars, model, hooks |
| **Project memory** | `CLAUDE.md` | Conventions, build/test commands, do's & don'ts |
| **Custom slash commands** | `./.claude/commands/*.md` | Reusable prompts you invoke as `/name` |
| **Custom subagents** | `./.claude/agents/*.md` | Specialized agents with their own tools/instructions |
| **Hooks** | `settings.json` | Automatic actions on events (format on save, notify on done) |
| **MCP servers** | `claude mcp add` / config | Connect external tools and data |
| **Status line** | `settings.json` | Customize the info bar (model, branch, cost, etc.) |
| **Output style / theme** | `/config` | Appearance and verbosity preferences |

> ⚙️ Interactive setup panels like `/permissions`, `/config`, `/agents`, and `/hooks` open in the terminal app. Start with `CLAUDE.md` and an allowlist of safe commands — that alone removes most day‑to‑day friction.

**A good first customization:** create a `CLAUDE.md` with your build/test commands and conventions, then add 2–3 commands to a permission allowlist (e.g. your test runner, your linter) so you stop getting prompted for them.

---

## 9. Plans, pricing & cost control

### 9.1 Ways to pay

| Option | What you get | Good for |
|---|---|---|
| **Free** | The Claude apps with limits | Trying Claude out |
| **Pro** | More usage; Claude Code access | Individuals, light coding |
| **Max (5×/20×)** | Much higher limits; best for heavy Claude Code use | Daily/heavy builders |
| **API (pay‑as‑you‑go)** | Per‑token billing via the Console | Automation, teams, building products |
| **Team / Enterprise** | Seats, admin, higher limits, security controls | Organizations |

> Subscriptions (Pro/Max) and the API are billed separately. Heavy interactive coders usually find a **Max** plan more economical than metered API usage; automation and product work usually want the **API**.

### 9.2 Keeping costs (and context) under control

- `/cost` — see what the current session has used.
- Use **`/clear`** between unrelated tasks so you're not paying to re‑process stale context.
- **`/compact`** long sessions instead of letting context balloon.
- Pick the **right model** — don't run Opus/Fable for tasks Sonnet or Haiku handle fine.
- Tune **effort** down for routine work.
- For repeated large context (the API), learn **prompt caching** — it can cut input costs dramatically.

---

## 10. Security & safety

Working with an agent that can run commands and reach the internet means a few habits matter.

- **Review before you trust.** Read diffs before committing; sanity‑check commands before approving. Auto‑accept and bypass modes are conveniences, not defaults to leave on everywhere.
- **Never paste secrets** into prompts, `CLAUDE.md`, or memory files. Use environment variables and secret managers. Don't commit `.env` files.
- **Treat links and content from email/messages/web as untrusted.** Don't let an agent act on instructions embedded in fetched content without your judgment (this is "prompt injection" — malicious instructions hidden in data).
- **Sandbox risky work.** Use a container, VM, or a throwaway git worktree when letting Claude run with fewer guardrails.
- **Be deliberate about external actions.** Sending messages, posting data, deleting things, and pushing to shared branches are hard to undo — confirm first.
- **Scope MCP and API credentials minimally.** Give connectors only the access the task needs.
- **Mind your data.** Understand your plan's data‑retention settings; use zero/limited‑retention options if you have sensitive code (note some frontier features require standard retention).

---

## 11. Troubleshooting & getting help

| Symptom | Try this |
|---|---|
| Claude seems "lost" or off‑track | `/clear` and restart the task with tighter context |
| Session feels sluggish / huge | `/compact` to summarize and continue |
| It keeps making the same mistake | Add a rule to `CLAUDE.md` (or a hook) |
| Permission prompts are constant | Add the safe commands to an allowlist in `settings.json` |
| A tool/MCP isn't working | `/mcp` to check connection status |
| Wrong or pricey model | `/model` to switch |
| Something's broken in the install | run `claude doctor` (diagnostics) |
| Want to report a bug | `/bug` from inside Claude Code |

**Where to learn more:**
- **In‑product:** `/help`, and ask Claude Code itself "how do I …?" — it knows its own features.
- **Docs:** [docs.claude.com](https://docs.claude.com) (Claude Code, API, Agent SDK).
- **Status:** [status.anthropic.com](https://status.anthropic.com) when something seems down.

---

## 12. Your 2‑week learning roadmap

A realistic path from zero to independent.

**Days 1–2 — Get running.**
Install the essentials (§3.4). Start Claude Code in a real (small) project, run `/init`, and ask it to explain the code and run the tests. Goal: comfortable starting a session and reading its output.

**Days 3–4 — Make changes safely.**
Practice the plan → approve → implement → verify loop (§6.2). Make small, real changes. Learn `@`, `#`, Esc/Esc‑Esc, and Shift+Tab modes. Goal: ship a small change you trust.

**Days 5–7 — Context & memory.**
Write a real `CLAUDE.md`. Learn `/clear` vs `/compact`. Practice giving good context and correcting course. Goal: sessions that stay on track.

**Days 8–10 — Customize.**
Add a permission allowlist. Write one custom slash command. Connect one MCP server you'd actually use (e.g. GitHub). Goal: less friction, more leverage.

**Days 11–14 — Go deeper.**
Try plan‑heavy work on a bigger task. Use subagents for exploration. Experiment with a skill. If you're building a product, make your first API call with an SDK. Goal: independent on day‑to‑day work, and you know where to reach when you need more.

---

## 13. Cheat sheet

**Launch**
```bash
claude                      # interactive session in the current directory
claude "do X"               # start with an initial prompt
claude -p "do X"            # headless / print mode (scripts, CI)
claude -c                   # continue the most recent conversation
claude mcp add <name> -- …  # add an MCP server
claude doctor               # diagnose the install
```

**In‑session keys**
```text
@path        mention a file            Shift+Tab   cycle permission/plan modes
#text        save to memory            Esc         interrupt
!cmd         run a raw shell command   Esc Esc     rewind to an earlier point
/command     run a slash command       Ctrl+C/D    cancel / exit
↑            previous input
```

**Most‑used slash commands**
```text
/init      /clear     /compact   /model    /cost
/login     /logout    /resume    /review   /status
/agents    /mcp       /hooks     /config   /help
```

**The safe change loop**
```text
plan → review plan → approve → implement → verify (tests/app) → review diff → commit
```

---

## 14. Glossary

- **Agent** — software that pursues a goal by taking actions in a loop, not just returning text.
- **Agentic loop** — plan → act → observe → repeat until done.
- **Context window** — the model's working memory for a session; everything it can "see" at once.
- **Token** — the unit models read/write in (~¾ of a word); pricing and limits are in tokens.
- **`CLAUDE.md`** — a file of durable project/personal instructions Claude Code auto‑reads.
- **Effort** — a dial (`low`…`max`) for how hard the model thinks.
- **Hook** — a shell command the harness runs automatically at a lifecycle event.
- **MCP (Model Context Protocol)** — the open standard for connecting Claude to external tools/data.
- **MCP server** — a program exposing a capability (GitHub, DB, Figma…) over MCP.
- **Plan mode** — read‑only mode where Claude proposes a plan before changing anything.
- **Permission mode** — how much Claude asks before acting (normal / auto‑accept / plan / bypass).
- **Prompt injection** — malicious instructions hidden in data/content an agent processes.
- **Skill** — an on‑demand packet of instructions/scripts that specializes Claude for a task.
- **Subagent** — a separate Claude instance handling a focused sub‑task, often in parallel.
- **Surface** — an app/interface to a model (apps, Claude Code, API, etc.).
- **Worktree** — an isolated copy of a git repo for parallel/risky work.

---

## 15. Resources & links

**Get started**
- Claude apps: [claude.ai](https://claude.ai) · Download: [claude.ai/download](https://claude.ai/download)
- Claude Code in the browser: [claude.ai/code](https://claude.ai/code)
- Developer Console: [platform.claude.com](https://platform.claude.com)

**Docs**
- All docs: [docs.claude.com](https://docs.claude.com)
- Claude Code, API reference, Agent SDK, MCP, pricing — all under the docs site.
- Pricing: [platform.claude.com/pricing](https://platform.claude.com/docs/en/pricing)

**Tools to install**
- Node.js: [nodejs.org](https://nodejs.org) · Git: [git-scm.com](https://git-scm.com) · GitHub CLI: [cli.github.com](https://cli.github.com)
- VS Code: [code.visualstudio.com](https://code.visualstudio.com) · Homebrew: [brew.sh](https://brew.sh)

**Ecosystem**
- Model Context Protocol: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- Status: [status.anthropic.com](https://status.anthropic.com)

---

*Built for getting started in 2026. Models, prices, and features evolve quickly — when in doubt, check the official docs above or just ask Claude Code "what's the current way to do X?"*
