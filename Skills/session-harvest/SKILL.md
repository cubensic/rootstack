# Skill: session-harvest
*Harvest raw Claude Code sessions and generate processed summaries for the digest.*

---

## When to Run

- Weekly (recommended: before running digest)
- Trigger phrases: "Harvest my sessions", "Process my sessions", "Run session harvest"
- This skill runs automatically as part of the digest flow — see digest SKILL.md

---

## What This Skill Does

Two-step process:

1. **Harvest** — Runs `harvest.py` to copy raw `.jsonl` session transcripts from `~/.claude/projects/` into `Knowledge Base/Raw/Sessions/`. Only copies new or updated files from the last 7 days.

2. **Summarize** — Reads each new raw session file and generates a structured markdown summary in `Knowledge Base/Sessions/`. These summaries are what the digest skill reads.

**Platform:** Claude Code only (for now). Codex and Cursor adapters can be added later.

---

## Step-by-Step Instructions

### Step 1 — Run the harvest script

Run the harvest script to copy raw session files:

```bash
python Skills/session-harvest/harvest.py
```

This copies recent `.jsonl` files from `~/.claude/projects/` into `Knowledge Base/Raw/Sessions/`. It skips files already copied. Note the output — it tells you how many sessions were found.

If no new sessions are found, stop here and tell the user.

---

### Step 2 — Identify unprocessed sessions

Compare the files in `Knowledge Base/Raw/Sessions/` against `Knowledge Base/Sessions/`.

For each `.jsonl` file in Raw/Sessions, check if a corresponding `.md` summary already exists in Sessions/ (matched by the session UUID in the filename). Collect the list of unprocessed sessions.

If all sessions are already processed, stop here and tell the user: "All sessions already have summaries. Nothing new to process."

---

### Step 3 — Read and summarize each new session

For each unprocessed `.jsonl` file:

1. Read the file. It contains JSON Lines — one JSON object per line. Each line is a message in the conversation (user messages, assistant responses, tool use, etc.).

2. Focus on extracting:
   - **What was worked on** — the main tasks, files modified, features built
   - **Decisions made** — architectural choices, design decisions, trade-offs discussed
   - **What was learned** — new knowledge, patterns noticed, skills developed
   - **What was hard** — blockers, confusion, things that took multiple attempts
   - **Next steps** — anything left unfinished or explicitly mentioned as "next"

3. Draft a summary using this format:

```markdown
# Session Log — [date of session]
**Tool:** Claude Code
**Session ID:** [UUID from filename]
**Duration:** [approximate, based on timestamps in the file]
**Project:** [working directory / project name from session metadata]

## What was done
- [bullets — concrete deliverables and actions taken]

## Decisions made
- [key decisions with reasoning]

## What was learned
- [new knowledge, patterns, skills developed]

## What was hard
- [blockers, confusion, things that took longer than expected]

## Next steps
- [what to pick up next time]
```

4. Name the file: `YYYY-MM-DD [brief topic].md` (use the session date and a 2-4 word topic summary)

---

### Step 4 — Show summaries and get approval

Present all drafted summaries to the user. For each one, show:
- The session date and topic
- The full summary

Ask for approval before writing. The user can approve all, edit individual summaries, or skip specific ones.

---

### Step 5 — Write approved summaries

Write each approved summary to `Knowledge Base/Sessions/`.

Confirm when complete: "Processed [N] session(s). Summaries saved to Knowledge Base/Sessions/."

---

## Notes

- **Raw files are never modified.** The script copies them; the skill only reads them. The originals in `~/.claude/projects/` are untouched.
- **Summaries are the processed output.** The digest skill reads from `Knowledge Base/Sessions/`, not from Raw.
- **Large sessions:** Some session files can be very large (1MB+). Focus on the user and assistant messages — skip tool result contents and file snapshots when summarizing.
- **Multiple projects:** The harvest script looks for sessions from the vault's own project directory. Sessions from other projects are not harvested unless explicitly requested.
