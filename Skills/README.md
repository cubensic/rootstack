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

Or say **"continue setup"** and the AI will show you what's remaining.

*Note: `now.md` doesn't have a setup skill — it's generated automatically by the digest skill from your journals and sessions.*

---

## Core Skills (permanent)

### `readme-updater`
**What it does:** Scans the vault structure and rewrites README.md to reflect current files and folders.
**When to run:** Weekly, or after adding/removing major folders.
**Trigger:** "Update my README" or scheduled weekly.
**Skill file:** `Skills/readme-updater/SKILL.md`

### `digest`
**What it does:** Reads recent journal entries and session notes, with outputs on different cadences:
- *Weekly:* Rewrites `About [You]/now.md`, appends lessons learned, appends to background if identity-relevant material surfaces
- *Monthly:* Appends behavioral patterns (needs 3+ evidence points across 30 days)
**When to run:** Weekly (automated via maintenance check), or manually.
**Trigger:** "Run my digest", "Update my now.md"
**Skill file:** `Skills/digest/SKILL.md`

### `session-harvest`
**What it does:** Harvests raw Claude Code session transcripts from `~/.claude/projects/` and generates processed markdown summaries in `Knowledge Base/Sessions/`. These summaries are the primary input for the digest skill.
**When to run:** Weekly (runs automatically as part of the digest flow), or manually.
**Trigger:** "Harvest my sessions", "Process my sessions"
**Skill file:** `Skills/session-harvest/SKILL.md`

### `goal-review`
**What it does:** Monthly review of progress against 1-year goals. Reads journals and session summaries to assess actual behavior vs. stated goals, generates a review file, and proposes goal updates if priorities have shifted.
**When to run:** Monthly (automated via maintenance check, only activates after goals are set up), or manually.
**Trigger:** "Review my goals", "Monthly review"
**Skill file:** `Skills/goal-review/SKILL.md`

### `kb-ingest`
**What it does:** Ingests a source (URL, text, or file) into the knowledge base:
- Snapshots the raw source to `Knowledge Base/Raw/Sources/`
- Generates a summary page with key concepts and entities in `Knowledge Base/Notes/`
- Creates or updates entity and concept pages (one source touches 5–15 pages)
- Updates `Knowledge Base/index.md` and `Knowledge Base/log.md`
**When to run:** Whenever you want to save external knowledge.
**Trigger:** "Ingest this", "Add to my KB", "Save this to knowledge base"
**Skill file:** `Skills/kb-ingest/SKILL.md`

### `kb-lint`
**What it does:** Health check for the knowledge base — finds orphan pages, broken wikilinks, unindexed sources, stale pages, and missing cross-references.
**When to run:** Every 14 days (automated via maintenance check), or manually.
**Trigger:** "Lint my KB", "KB health check"
**Skill file:** `Skills/kb-lint/SKILL.md`

### `style-analyzer`
**What it does:** Reads writing samples from `Content/Style/Samples/` and generates a comprehensive writing style guide at `Content/Style/writing-style.md`. Detects tone, sentence patterns, vocabulary, signature moves, and anti-patterns.
**When to run:** Weekly (automated via maintenance check), or after adding new writing samples.
**Trigger:** "Update my writing style", "Analyze my writing"
**Skill file:** `Skills/style-analyzer/SKILL.md`

---

## How to Add Skills

Create a subfolder for each skill with at minimum:
- `SKILL.md` — instructions for the AI on how to execute this skill
- Optionally: supporting scripts or templates

Skills should be platform-agnostic — written so they work in Claude, Codex, or any AI tool that can read files.
