# Emoji Legend

Canonical emoji vocabulary for agent reports and summaries, across every project. The core legend is 10 emojis in three tiers; dev repos add 2 more. Referenced from [AGENTS.md](../AGENTS.md) and the output style rules in [agents_notes.md](../notes/agents_notes.md).

## Core legend (10)

### Item status — starts a checklist row or table cell

Answers: what happened to this item?

| Emoji | Meaning |
|-------|---------|
| ✅ | Done / success / verified |
| ❌ | Failed / missing / not done |
| ⚠️ | Warning — done but with caveats, or a non-blocking issue |
| ⏳ | Pending / in progress / waiting on something |
| 📥 | New / incoming / not yet triaged |

### Rollup health — one per project, area, or section heading

Answers: how is this area overall?

| Emoji | Meaning |
|-------|---------|
| 🟢 | On track / healthy |
| 🟡 | Needs attention / at risk |
| 🔴 | Blocked / critical |

### Markers — communication flags

| Emoji | Meaning |
|-------|---------|
| ❓ | Needs Raveen's input — a decision or answer only he can give |
| 💡 | Idea / suggestion / optional improvement |

## Code-project extension (+2)

For dev repos only:

| Emoji | Meaning |
|-------|---------|
| 🐛 | Bug / defect found |
| 🚀 | Shipped / deployed / released |

## Usage rules

- The emoji starts the line or cell; one status emoji per item.
- Item emojis (✅ ❌ ⚠️ ⏳ 📥) mark single items; health emojis (🟢 🟡 🔴) summarize areas — don't mix tiers. ⚠️ flags an item, 🟡 flags an area; ❌ fails an item, 🔴 blocks an area.
- Group ❓ items together (top or bottom of the report) so "what do you need from me" is scannable at a glance.
- Emojis are status markers, not prose decoration — don't sprinkle them into sentences.
- A doc may define its own local legend for other purposes (e.g. the guide legend in [claude_starter_pack_2026.md](claude_starter_pack_2026.md)); reports and summaries always use the meanings on this page.

## Example

### Statement import 🟡

- [x] ✅ hdfc credit card — 42 transactions imported
- [x] ⚠️ icici savings — imported; 3 duplicates skipped
- [ ] ⏳ axis credit card — waiting on locked PDF
- [ ] 📥 sbi savings — new statement, not yet triaged
- [ ] ❌ kotak — download failed (site error)

❓ Axis PDF is password-protected — share the password or an unlocked copy?

💡 A pre-parse dedupe step would remove the icici duplicates automatically.

## Using from other repos

Reference this file — do not copy it. In the target repo's `AGENTS.md` / `CLAUDE.md`, add an import line:

```markdown
@~/repos/ai/docs/emoji_legend.md
```
