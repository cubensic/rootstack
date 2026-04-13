# Skills
*AI maintenance skills that keep this vault alive.*

Skills are reusable, AI-executable workflows stored as markdown files. They can be run on demand or on a schedule.

---

## Setup Skills (one-time)

These skills guide you through filling in your vault profile. Each one is a short conversation that drafts one section. **They self-delete when complete** — their absence means that section is done.

Run them in any order. Recommended order: background → values → personality → writing → goals → now.

| Skill | What it fills in | Trigger |
|---|---|---|
| `setup-background` | `About [You]/background.md` | "Set up my background" |
| `setup-values` | `About [You]/values.md` | "Set up my values" |
| `setup-personality` | `About [You]/personality.md` | "Set up my personality" |
| `setup-writing` | `Content/Style/writing-style.md` | "Set up my writing style" |
| `setup-goals` | `About [You]/goals/1-year.md` | "Set up my goals" |
| `setup-now` | `About [You]/now.md` | "Set up my now page" |

Or say **"continue setup"** and the AI will show you what's remaining.

---

## Core Skills (permanent)

### `readme-updater`
**What it does:** Scans the vault structure and rewrites README.md to reflect current files and folders.
**When to run:** Weekly, or after adding/removing major folders.
**Trigger:** "Update my README" or scheduled weekly.
**Skill file:** `Skills/readme-updater/SKILL.md`

### `digest`
**What it does:** Reads recent journal entries and session notes, then:
- Rewrites `About [You]/now.md` with current focus and state
- Appends new entries to `patterns/behavioral-patterns.md` if patterns are detected
- Appends new entries to `patterns/lessons-learned.md` if key lessons emerged
**When to run:** Monthly, or after a significant period of journaling.
**Trigger:** "Run my digest" or scheduled monthly.
**Skill file:** `Skills/digest/SKILL.md`

---

## How to Add Skills

Create a subfolder for each skill with at minimum:
- `SKILL.md` — instructions for the AI on how to execute this skill
- Optionally: supporting scripts or templates

Skills should be platform-agnostic — written so they work in Claude, Codex, or any AI tool that can read files.
