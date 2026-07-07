# AI Agents

Notes on working effectively with AI coding agents.

## Working style

- Use agile work. Tight scope.
- Nothing vague — precise goal / result.
- Use a second AI model to critique the output.

## Defining a great result (before you start)

- Define the precise criteria for a great result up front.
- Use a past example as the format to match.
- Have a second AI check the final output.

## A workspace that improves over time

1. Set up a proper `CLAUDE.md` file.
2. Build your LLM knowledge base.
3. Start building out your skill set.
4. Create rules for what the AI can and can't work on.

## Guardrails — a rule the AI can't bypass

Bucket things into three groups:

- **Always do** — the defaults the agent runs on autopilot.
- **Ask first** — anything with consequences: destructive actions, costs, one-way decisions.
- **Never do** — the lines that don't get crossed: touching production, sending real
  emails, exposing secrets. Enforce these with hooks so they can't be bypassed.

## Useful prompt — audit your setup

> Check my CLAUDE.md, my knowledge base, my skills, and my guardrails. For each of the
> top 5 gaps, name the file, the problem, and the exact fix — and flag which risky
> actions need a hook so I can't bypass them.

## Source

- [Stop Prompting Claude. Use Karpathy's Method Instead.](https://youtu.be/7zZy1QTvokM)
