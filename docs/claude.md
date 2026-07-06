# Claude Notes

Personal notes / rules for working with Claude in this project.

## Rules

- Never use the brainstorm skill or plugin in Claude.

## Commands

### `/init`

Scans the codebase and generates a `CLAUDE.md` file documenting the project
(structure, commands, conventions). Claude Code loads this file as project
memory at the start of every session. Run it once per project, then edit the
generated file by hand as you learn what Claude gets wrong.

Source: [Claude Code slash commands](https://code.claude.com/docs/en/slash-commands)
