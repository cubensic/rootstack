# Knowledge Base
*Your personal, AI-maintained knowledge base. Three layers: raw sources, wiki pages, and a schema that ties it together.*

---

## The Three-Layer Pattern

This knowledge base follows a three-layer architecture:

1. **Raw Sources** (`Raw/`) — immutable snapshots of ingested content. The AI reads these but never modifies them after creation.
2. **The Wiki** (`Notes/`) — AI-generated and AI-maintained markdown pages. Summaries, entity pages, concept pages, cross-references. The AI owns these entirely — creating, updating, and linking pages as new sources arrive.
3. **The Schema** — `CLAUDE.md`, `AGENTS.md`, and skill files define how the AI operates on the KB. Co-evolved by you and the AI.

A single ingested source typically creates or updates 5–15 pages. This cross-referencing is what makes the knowledge base compound over time.

---

## Structure

```
Knowledge Base/
  index.md       ← Master catalog of all KB content
  log.md         ← Append-only record of all operations
  Notes/
    work/        ← Wiki pages from work-related sources
    personal/    ← Wiki pages from personal interest sources
    my-content/  ← Copies of your own published content
  Raw/
    Sessions/    ← Raw .jsonl session transcripts (from Claude Code)
    Sources/     ← Immutable snapshots of ingested articles, papers, etc.
  Sessions/      ← Processed session summaries (markdown, fed into digest)
```

---

## How to Use

**Ingest a source:** Say "ingest this" and provide a URL, paste text, or point to a file. The AI will:
1. Snapshot the raw source (immutable)
2. Generate a summary page with key concepts and entities
3. Create or update entity and concept pages
4. Update the index and log

**Query:** Just ask questions. The AI reads `index.md` to find relevant pages and synthesizes answers from wiki content.

**Lint:** Say "lint my KB" to run a health check — finds orphan pages, broken links, stale content, and inconsistencies.

See `Skills/kb-ingest/SKILL.md` and `Skills/kb-lint/SKILL.md` for full details.

---

## Key Files

| File | Purpose | Who maintains it |
|------|---------|-----------------|
| `index.md` | Master catalog — all sources, entities, concepts | AI (updated on every ingest) |
| `log.md` | Chronological record of operations | AI (append-only) |
| `Notes/` | Wiki pages — the living knowledge | AI (creates, updates, cross-links) |
| `Raw/Sources/` | Immutable source snapshots | AI (write once, never modify) |
| `Raw/Sessions/` | Raw Claude Code transcripts | Automated (session-harvest script) |
| `Sessions/` | Processed session summaries | AI (session-harvest skill) |

---

## Optional: SQLite for Semantic Search

If you want AI to query your knowledge base semantically (find notes by meaning, not just keyword), you can add a `databases/` folder with SQLite vector databases. Not required for basic use.
