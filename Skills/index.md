<!-- Skill catalog. One entry per skill with trigger phrase and cadence. -->
# Skills Index
*Reusable AI workflows. Each skill lives in its own folder with a `SKILL.md` the AI reads to execute it.*

---

## Setup Skills — One-Time

Short conversations that fill in your vault profile. **These self-delete when complete** — absence means that section is done. Run them in any order. Recommended order: background → values → personality → writing → goals → me.

| Skill | Fills in | Trigger | Time |
|---|---|---|---|
| `setup-background` | `About [You]/background.md` | "Set up my background" | 10–15 min |
| `setup-values` | `About [You]/values.md` | "Set up my values" | 10–15 min |
| `setup-personality` | `About [You]/personality.md` | "Set up my personality" | 10–15 min |
| `setup-writing` | `Content/Style/writing-style.md` | "Set up my writing style" | 10–20 min |
| `setup-goals` | `About [You]/goals/1-year.md` (+ 5-year, 10-year) | "Set up my goals" | 15–20 min |
| `setup-me` | `me.md` (runs last — synthesizes from above) | "Set up my me.md" | ~5 min |

Or say **"continue setup"** to see what's remaining.

---

## Core Skills — Permanent

### `digest`
**What:** Reads recent journals + session summaries. Writes the `## Current Focus` section of `me.md`, appends lessons, appends behavioral patterns (monthly, needs 3+ evidence points), appends identity-relevant material to `background.md`.
**Cadence:** Weekly (automated) — monthly patterns window.
**Trigger:** "Run my digest", "Update me.md"

### `session-harvest`
**What:** Copies raw Claude Code `.jsonl` transcripts from `~/.claude/projects/` and generates processed markdown summaries in `Knowledge Base/Sessions/`. Feeds `digest`.
**Cadence:** Weekly (runs as part of digest flow).
**Trigger:** "Harvest my sessions"

### `goal-review`
**What:** Monthly evidence-based review of 1-year goals. Reads journals + sessions, assesses actual behavior vs. stated goals, generates a review file, proposes goal updates.
**Cadence:** Monthly (automated after `setup-goals` completes).
**Trigger:** "Review my goals", "Monthly review"

### `kb-ingest`
**What:** Ingests a source (URL/text/file) into the three-layer KB. Snapshots raw source → generates summary wiki page → creates/updates entity + concept pages → updates `index.md` + `log.md`. One source touches 5–15 pages.
**Cadence:** On-demand.
**Trigger:** "Ingest this", "Add to my KB"

### `kb-lint`
**What:** KB health check — orphan pages, broken wikilinks, unindexed sources, stale pages, missing cross-references. Outputs a report with proposed fixes.
**Cadence:** Every 14 days (automated).
**Trigger:** "Lint my KB", "KB health check"

### `style-analyzer`
**What:** Reads writing samples in `Content/Style/Samples/` and generates `Content/Style/writing-style.md`. Detects tone, sentence patterns, vocabulary, signature moves, anti-patterns.
**Cadence:** Weekly (automated, only if samples exist).
**Trigger:** "Update my writing style", "Analyze my writing"

### `vault-map-updater`
**What:** Scans the vault structure and proposes updates to `vault-map.md` (never writes without approval).
**Cadence:** Weekly (automated).
**Trigger:** "Update my vault map"

---

## Adding New Skills

Create a folder under `Skills/` with at minimum a `SKILL.md` describing the workflow. Keep skills platform-agnostic — written so they work in Claude Code, Codex, Cursor, or any AI that can read files. Add an entry to this index.
