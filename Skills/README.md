# Skills
*AI maintenance skills that keep this vault alive.*

Skills are reusable, AI-executable workflows stored as markdown files. They can be run on demand or on a schedule.

## Core Skills (Build These First)

### `readme-updater` ✓
**What it does:** Scans the vault structure and rewrites README.md to reflect current files and folders.
**When to run:** Weekly, or after adding/removing major folders.
**Trigger:** "Update my README" or scheduled weekly.
**Skill file:** `Skills/readme-updater/SKILL.md`

### `digest` ✓
**What it does:** Reads recent journal entries and session notes, then:
- Rewrites `About [You]/now.md` with current focus and state
- Appends new entries to `patterns/behavioral-patterns.md` if patterns are detected
- Appends new entries to `patterns/lessons-learned.md` if key lessons emerged
**When to run:** Monthly, or after a significant period of journaling.
**Trigger:** "Run my digest" or scheduled monthly.
**Skill file:** `Skills/digest/SKILL.md`

### `people-nudge`
**What it does:** Scans `About [You]/people/` for contacts not updated in 60+ days and surfaces them for a quick update.
**When to run:** Monthly.
**Trigger:** "Check my contacts" or scheduled monthly.

## How to Add Skills

Create a subfolder for each skill with at minimum:
- `SKILL.md` — instructions for the AI on how to execute this skill
- Optionally: supporting scripts or templates

Skills should be platform-agnostic — written so they work in Claude, Codex, or any AI tool that can read files.
