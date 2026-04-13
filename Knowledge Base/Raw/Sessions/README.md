# Raw Sessions
*Unprocessed Claude Code session transcripts.*

This folder holds raw `.jsonl` files copied from `~/.claude/projects/` by the `session-harvest` skill. These are complete conversation transcripts — every message, tool use, and response from a Claude Code session.

**Do not edit these files.** They are raw input. The session-harvest skill reads them and generates processed markdown summaries in `Knowledge Base/Sessions/`.

## How files get here

Run the harvest script:
```bash
python Skills/session-harvest/harvest.py
```

Or trigger the session-harvest skill: "Harvest my sessions"

The script copies `.jsonl` files from the last 7 days that haven't already been copied.
