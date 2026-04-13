# Sessions
*Auto-captured AI session summaries.*

This folder holds session logs written automatically at the end of every AI working session (Claude Code, Codex, Cowork, Cursor, etc.). These are raw input for the **digest skill**, which synthesizes them into `now.md`, behavioral patterns, and lessons learned.

## File Format

One file per session: `YYYY-MM-DD [topic].md`

```
# Session Log — [date]
**Tool:** [Claude Code / Codex / Cowork / Cursor]
**Duration:** [approximate]

## What was done
- [bullets]

## Decisions made
- [key decisions with reasoning]

## What was learned
- [new knowledge, patterns, skills developed]

## What was hard
- [blockers, confusion, things that took longer than expected]

## Next steps
- [what to pick up next time]
```

## How It Works

You don't need to do anything. The AI is instructed to draft a session log when a working session wraps up. It will show you the draft and write it on approval.

The digest skill reads these alongside your journal entries to keep your vault evolving.
