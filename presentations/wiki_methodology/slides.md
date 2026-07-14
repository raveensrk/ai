<!-- .slide: data-auto-animate -->

# Your Wiki Is the Product

### A methodology for structuring shared knowledge between you and your LLM

<span class="sol-muted">Raveen · 2026</span>

Note: Welcome. This talk is about a simple idea with big consequences: if you structure your notes and documentation the right way, they stop being passive text — they become the operating system for an AI agent. And that structured system itself is a product you can sell.

---

<!-- .slide: data-auto-animate -->

## Your Wiki Is the Product

<div class="cols">
<div>

**Part 1 — The idea**
1. The problem
2. The concept
3. The methodology

</div>
<div>

**Part 2 — In practice**
4. The workflow
5. Demos & use cases
6. Agent roles & behaviors
7. The pitch

</div>
</div>

---

## 1. The Problem

--

<!-- .slide: data-auto-animate -->

### Where does your knowledge live today?

- Buried in chat histories <!-- .element: class="fragment fade-up" -->
- Scattered across docs, files, and tools <!-- .element: class="fragment fade-up" -->
- In your head <!-- .element: class="fragment fade-up" -->
- Nowhere — re-derived every time <!-- .element: class="fragment fade-up sol-red" -->

<p class="cite">Knowledge workers spend roughly a fifth of their week just searching for and gathering information — McKinsey Global Institute, <a href="https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-social-economy">The social economy</a></p>

Note: Before we talk about AI at all: this is already a human problem. The knowledge that runs your work is fragmented. McKinsey's classic estimate is ~19% of the workweek spent searching and gathering information.

--

### And the LLM makes it worse before it makes it better

- Every session starts from **zero** — the model remembers nothing about you <!-- .element: class="fragment" -->
- So you re-explain your project, your conventions, your vocabulary… <!-- .element: class="fragment" -->
- …every. single. time. <!-- .element: class="fragment sol-orange" -->
- The model's answers are only as good as the **context** you hand it <!-- .element: class="fragment sol-yellow" -->

Note: LLMs are stateless. Without deliberate context, you pay an explanation tax at the start of every conversation, and quality drifts because each session gets a slightly different briefing.

--

<!-- .slide: data-auto-animate -->

### The real bottleneck isn't the model

# It's the context

<!-- .element: class="fragment sol-cyan" -->

<p class="cite">"Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy, June 2025 (via <a href="https://simonwillison.net/2025/Jun/27/context-engineering/">Simon Willison</a>); see also Anthropic, <a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents</a></p>

Note: The industry converged on a name for this: context engineering. Models are commoditizing; curated context is the differentiator. That's exactly what a well-structured wiki is.

---

## 2. The Concept

--

### Shared knowledge is a **contract**

The wiki is the single source of truth that **both parties read and write**

| The human agrees to… | The agent agrees to… |
|---|---|
| Keep knowledge in predictable places | Read the rules before acting |
| Use the shared vocabulary | Use the shared vocabulary |
| Capture decisions in the wiki | Cite sources, write results back |

Note: The key mental shift: docs are not for humans OR for machines — they are a contract between them. Both sides read it, both sides write it, and the conventions file (AGENTS.md) is the contract's terms.

--

### One wiki, two readers

<div class="mermaid">
<pre>
flowchart LR
  U["👤 User"] -- "writes & reads" --> W
  subgraph W["📚 The Wiki — shared knowledge"]
    R["📜 AGENTS.md<br/>rules & conventions"] ~~~ N["🗂 docs/<br/>content & task prompts"] ~~~ T["🔤 terminologies & aliases<br/>shared vocabulary"]
  end
  W -- "reads & writes" --> A["🤖 LLM Agent"]
  U -. "task prompt" .-> A
  A -. "results + citations" .-> U
</pre>
</div>

Note: This is the whole architecture on one slide. The user and the agent never rely on memory or chat history — everything durable flows through the wiki. Rules at the top, content below, vocabulary binding it together.

---

## 3. The Methodology

--

### Five principles

1. **Single source of truth** — one repo, everything in it <!-- .element: class="fragment" -->
2. **Predictable places** — every kind of content has one home <!-- .element: class="fragment" -->
3. **Shared vocabulary** — terminologies and aliases both sides use <!-- .element: class="fragment" -->
4. **Executable prompts** — tasks stored as callable documents <!-- .element: class="fragment" -->
5. **Citations everywhere** — claims link to sources, work links back <!-- .element: class="fragment" -->

Note: Everything that follows is one of these five principles applied. None of them require special tooling — just discipline encoded as files.

--

<!-- .slide: data-auto-animate -->

### Predictable places

```text
ai/
├── AGENTS.md        ← the contract: rules & conventions
└── docs/            ← the wiki: knowledge & inbox
```

--

<!-- .slide: data-auto-animate -->

### Predictable places

```text
ai/
├── AGENTS.md        ← the contract: rules & conventions
├── docs/            ← the wiki: knowledge & inbox
│   ├── inbox.md     ← capture point: todos land here first
│   ├── tasks.md     ← callable task prompts
│   ├── terminologies.md
│   └── write_docs.md ← reusable documentation prompt
├── scripts/         ← automation the agent may run
└── tmp/             ← scratch space (never knowledge)
```

Note: Auto-animate grows the tree — the point being: start tiny, the structure scales without reorganizing. An agent that knows this map never has to guess where something belongs.

--

### Rules the agent can rely on

- Naming: `snake_case` for files and directories
- Links: always markdown links, always relative paths
- Aliases: `y` = yes, `n` = no, `<` = previous, `>` = next
- Behavior: *interview me first, one question at a time*
- Scope: *minimal fix — smallest change that solves the problem*

<p class="cite">Convention files for agents are an open standard adopted by 60,000+ open-source projects: <a href="https://agents.md">AGENTS.md</a> (<a href="https://openai.com/index/agentic-ai-foundation/">Agentic AI Foundation, Dec 2025</a>); see also Anthropic's <a href="https://www.anthropic.com/engineering/claude-code-best-practices">Claude Code best practices</a> on CLAUDE.md memory files.</p>

Note: These are real rules from this repo's AGENTS.md. Small, checkable, boring — and that's why they work. The agent reads them at session start, so behavior is consistent without re-prompting.

--

### Structure the docs themselves: Diátaxis

<div class="mermaid">
<pre>
block-beta
  columns 2
  block:learn["&nbsp;"]:2
    columns 2
    T["📘 Tutorials<br/><i>learning-oriented</i>"]
    H["🛠 How-to guides<br/><i>task-oriented</i>"]
    E["💡 Explanation<br/><i>understanding-oriented</i>"]
    R["📖 Reference<br/><i>information-oriented</i>"]
  end
</pre>
</div>

Four kinds of documentation — never mix them in one page

<p class="cite">Daniele Procida, <a href="https://diataxis.fr">Diátaxis</a>; the <a href="https://docs.divio.com">Divio documentation system</a></p>

Note: For the docs/ directory we adopt Diátaxis: tutorials, how-to guides, reference, explanation. The quadrant split matters for agents too — a how-to and a reference answer different questions, and the agent can pick the right kind of page for the right job.

---

## 4. The Workflow

--

### From loose thought to executed task

<div class="mermaid">
<pre>
flowchart TD
  C["💭 Capture<br/>any thought, any time"] --> I["docs/inbox.md"]
  I --> TR{"Triage"}
  TR -- "knowledge" --> N["docs/<br/>structured pages"]
  TR -- "repeatable task" --> TP["docs/tasks.md<br/>task-calling prompt"]
  TR -- "new term" --> V["terminologies & aliases"]
  TP --> AG["🤖 Agent executes"]
  N --> AG
  V --> AG
  AG --> OUT["Results + citations"]
  OUT --> N
</pre>
</div>

Note: The loop: capture into the inbox with zero friction, triage into structure, and everything structured becomes fuel for the agent. Crucially the arrow comes back — results are written into the wiki with citations, so the system compounds.

--

### A session under the contract

<div class="mermaid">
<pre>
sequenceDiagram
  participant U as 👤 User
  participant A as 🤖 Agent
  participant W as 📚 Wiki
  U->>A: "Do maintenance" (task alias)
  A->>W: read AGENTS.md — rules & conventions
  A->>W: read docs/tasks.md → maintenance.md
  A->>U: clarifying question (one at a time)
  U->>A: answer ("y")
  A->>A: execute task
  A->>W: write results + citations back
  A->>U: report with links
</pre>
</div>

Note: This is what a single session looks like. The user speaks in shared vocabulary — a task name and the alias "y". The agent front-loads reading the contract, interviews before acting, and closes the loop by writing back.

---

## 5. Demos & Use Cases

--

### Demo 1 — Tasks as callable prompts

`docs/tasks.md`:

> Following are tasks that the AI/llm will perform for me.
> **The heading will be the task calling prompt.**

- Saying **"Maintenance"** invokes the whole documented procedure <!-- .element: class="fragment" -->
- The prompt *is* documentation; the documentation *is* the prompt <!-- .element: class="fragment sol-cyan" -->

Note: Demo this live: type the single word "Maintenance" and watch the agent open docs/maintenance.md and follow it. New team members and new agents get identical behavior because the procedure lives in the wiki, not in anyone's head.

--

### Demo 2 — Shared vocabulary

| You type | Both of you mean |
|---|---|
| `y` | yes |
| `n` | no |
| `<` | previous |
| `>` | next |
| "Maintenance" | the entire maintenance procedure |

Vocabulary compresses communication — like jargon between colleagues <!-- .element: class="fragment" -->

Note: Aliases look trivial but they are the seed of something bigger: a controlled vocabulary. Every term you both agree on removes a round of clarification forever.

--

### Demo 3 — Documentation on demand

- `docs/write_docs.md` encodes the **Divio/Diátaxis** method
- Point the agent at any project → it writes docs *in your structure*
- Consistency without style guides or review cycles <!-- .element: class="fragment" -->

Note: Because the documentation methodology itself lives in the wiki as a prompt, "write the docs" is a one-liner. The output lands in docs/ following Diátaxis, with citations, matching every other page.

--

### Demo 4 — This deck built itself 🤯

1. A voice note became a TODO in `docs/inbox.md`
2. The agent read the TODO, interviewed the user, researched sources
3. …and produced **this presentation**, in the wiki, with citations

The methodology you're looking at **produced the artifact you're looking at** <!-- .element: class="fragment sol-green" -->

Note: The meta-demo is the strongest one: this very deck started as a rambling voice memo captured into inbox.md. The agent asked clarifying questions per the contract, did the research, cited it, and committed the result back into the repo. Workflow, demonstrated by existing.

---

## 6. Agent Roles & Behaviors

--

### An agent = model + context + role + behavior

- **Role** — who the agent is: *librarian, researcher, reviewer…* <!-- .element: class="fragment" -->
- **Behavior** — how it acts: *interview first, minimal fix, cite sources* <!-- .element: class="fragment" -->
- **Skills** — what it can do: packaged, reusable capabilities <!-- .element: class="fragment" -->
- **Tools** — what it can touch: files, APIs, connectors (MCP) <!-- .element: class="fragment" -->

<p class="cite">Role prompting: <a href="https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/system-prompts">Anthropic system-prompt docs</a> · Skills: <a href="https://agentskills.io">Agent Skills protocol</a> · Tools: <a href="https://modelcontextprotocol.io">Model Context Protocol</a></p>

Note: Four dials you can turn independently. The wiki sets all four declaratively: roles and behaviors in AGENTS.md, skills in .agents/skills/, tools via MCP config. Change the files, change the agent.

--

### One wiki, a team of roles

<div class="mermaid">
<pre>
flowchart TB
  subgraph W["📚 Shared wiki — one source of truth"]
    K["knowledge · rules · vocabulary · task prompts"]
  end
  L["🗂 Librarian<br/><i>triage inbox, keep structure</i>"] --> W
  R["🔎 Researcher<br/><i>gather & cite sources</i>"] --> W
  S["✍️ Scribe<br/><i>write docs in Diátaxis form</i>"] --> W
  V["✅ Reviewer<br/><i>check rules & citations</i>"] --> W
  W --> OUT["Consistent, auditable output"]
</pre>
</div>

<p class="cite">Anthropic's orchestrator + specialist-subagent system outperformed single-agent Claude Opus 4 by 90.2% on research evals — <a href="https://www.anthropic.com/engineering/multi-agent-research-system">How we built our multi-agent research system</a></p>

Note: Once knowledge is structured, you don't need one do-everything agent — you can run specialists that share the same contract. Anthropic's multi-agent research system showed specialist subagents outperform a single generalist by 90.2% on their internal evals; the wiki is what keeps a team of them coherent.

---

## 7. The Pitch

--

<!-- .slide: data-auto-animate -->

### What are we actually selling?

Not a model. Not a chatbot.

# The methodology **is** the product

<!-- .element: class="fragment sol-yellow" -->

Note: Now the sales pitch. Models are rented and commoditized — anyone can call the same API. What can't be copied overnight is an organization's structured, living knowledge and the workflow that maintains it. That is the sellable asset.

--

<!-- .slide: data-auto-animate -->

### The methodology **is** the product

**The package:**

1. The **structure** — wiki template, naming rules, directory contract
2. The **workflow** — capture → triage → task prompts → cited results
3. The **agent** — pre-configured roles, behaviors, and skills on top

Install it in a company and their wiki **becomes their agent** <!-- .element: class="fragment sol-cyan" -->

Note: Concretely the product has three layers: a structure you can install in a day, a workflow the team adopts, and the agent layer that makes it come alive. The tagline: your wiki becomes your agent.

--

### Why now — the market already agrees

- **Notion AI, Atlassian Rovo, Glean, Microsoft Copilot** — every major player is racing to turn company knowledge into an AI assistant <!-- .element: class="fragment" -->
- But they bolt AI onto **messy** knowledge — garbage in, garbage out <!-- .element: class="fragment" -->
- **Our edge:** we sell the methodology that makes knowledge *agent-ready first* <!-- .element: class="fragment sol-green" -->

<p class="cite"><a href="https://techcrunch.com/2024/05/01/atlassian-launches-rovo-its-new-ai-teammate/">Atlassian Rovo</a> turns Confluence wikis into AI agents · <a href="https://www.glean.com/press/glean-raises-150m-series-f-at-7-2b-valuation-to-accelerate-enterprise-ai-agent-innovation-globally">Glean valued at $7.2B</a> for enterprise-knowledge agents · <a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture">Microsoft 365 Copilot</a> grounds every answer in company content</p>

Note: The market validation: enterprise knowledge + AI is one of the hottest categories — Atlassian built Rovo on Confluence wikis, Glean is a $7.2B company whose entire product is "knowledge graph + agents", and Copilot's architecture is grounding answers in org content. The incumbents index whatever mess exists. We differentiate by fixing the knowledge first — the methodology — so the agent on top is actually reliable.

--

### Value proposition

| Pain | With the methodology |
|---|---|
| Onboarding takes months | New hire (or new agent) reads the wiki |
| Knowledge walks out the door | Knowledge lives in the contract |
| AI answers you can't trust | Every claim carries a **citation** |
| Every AI session starts from zero | Context **compounds** over time |

Note: Four pains, four direct answers. The citation rule matters for enterprise buyers: auditability is what makes AI output usable in regulated or high-stakes settings.

--

### Roadmap

1. **v1 — Method**: wiki template + AGENTS.md contract + training <!-- .element: class="fragment" -->
2. **v2 — Agent**: packaged roles, behaviors, and skills, installed on the customer's wiki <!-- .element: class="fragment" -->
3. **v3 — Platform**: marketplace of task prompts & skills; the wiki as the company's agent OS <!-- .element: class="fragment" -->

Note: The wedge is consulting-shaped (v1), the product is the packaged agent (v2), and the moat is the ecosystem (v3). Each stage is sellable on its own.

--

<!-- .slide: data-auto-animate -->

# Your Wiki Is the Product

### Structure your knowledge — and it starts working for you

<span class="sol-muted">Thank you · questions?</span>

Note: Callback to the title: it reads differently now. The wiki is not documentation about the work — structured correctly, it IS the work, and it's for sale.

---

## References

--

### Documentation methodology

<small>

- Daniele Procida — [Diátaxis: a systematic approach to technical documentation](https://diataxis.fr) · [in five minutes](https://diataxis.fr/start-here/)
- Daniele Procida / Divio — [The documentation system](https://documentation.divio.com/) (2017, the original four-quadrant write-up)
- Daniele Procida — [What nobody tells you about documentation](https://www.youtube.com/watch?v=t4vKPhjcMZg) (PyCon AU 2017 talk)
- Tom Johnson — [What is Diátaxis and should you be using it?](https://idratherbewriting.com/blog/what-is-diataxis-documentation-framework) (I'd Rather Be Writing)
- kapa.ai — [Writing documentation for AI: best practices](https://docs.kapa.ai/improving/writing-best-practices)
- Jeremy Howard, Answer.AI — [/llms.txt: helping LLMs use your content](https://www.answer.ai/posts/2024-09-03-llmstxt.html) · [spec](https://llmstxt.org/)

</small>

--

### Context engineering & shared knowledge

<small>

- Anthropic — [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Sep 2025)
- Simon Willison — [Context engineering](https://simonwillison.net/2025/Jun/27/context-engineering/) (Jun 2025, quotes Karpathy's coinage)
- Philipp Schmid — [The new skill in AI is not prompting, it's context engineering](https://www.philschmid.de/context-engineering) (Jun 2025)
- Anthropic — [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices) (Apr 2025, the CLAUDE.md convention)
- Anthropic — [Claude Code memory documentation](https://code.claude.com/docs/en/memory)
- [AGENTS.md — a README for agents](https://agents.md/) (Aug 2025) · [InfoQ coverage](https://www.infoq.com/news/2025/08/agents-md/) · [Agentic AI Foundation: 60k+ adopting projects](https://openai.com/index/agentic-ai-foundation/) (Dec 2025)

</small>

--

### Agent roles, behaviors & skills

<small>

- Anthropic — [Giving Claude a role with a system prompt](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
- OpenAI — [Prompt engineering guide (personas)](https://platform.openai.com/docs/guides/prompt-engineering)
- Anthropic — [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) (Jun 2025)
- Anthropic — [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- Anthropic — [Introducing Agent Skills](https://www.anthropic.com/news/skills) (Oct 2025) · [Agent Skills open standard](https://agentskills.io) (Dec 2025)
- Anthropic — [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) (Nov 2024)

</small>

--

### Market validation

<small>

- McKinsey Global Institute — [The social economy](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-social-economy) (2012 — 19% of the workweek spent searching for information)
- TechCrunch — [Atlassian launches Rovo, its new AI teammate](https://techcrunch.com/2024/05/01/atlassian-launches-rovo-its-new-ai-teammate/) (May 2024)
- SiliconANGLE — [Atlassian opens Teamwork Graph, pushes Rovo into agentic execution](https://siliconangle.com/2026/05/06/atlassian-opens-teamwork-graph-pushes-rovo-agentic-execution-team-26/) (May 2026)
- Glean — [Series F at $7.2B valuation for enterprise AI agents](https://www.glean.com/press/glean-raises-150m-series-f-at-7-2b-valuation-to-accelerate-enterprise-ai-agent-innovation-globally) (Jun 2025)
- Microsoft — [Microsoft 365 Copilot architecture (Graph grounding)](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture)
- Mintlify — [Simplifying docs for AI with /llms.txt](https://www.mintlify.com/blog/simplifying-docs-with-llms-txt)

</small>

Note: References are split into four vertical slides — navigate down. The same links appear inline on the slides where each claim is made.
