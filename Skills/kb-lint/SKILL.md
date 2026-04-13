# Skill: kb-lint
*Health check for the knowledge base — find orphans, broken links, stale pages, and inconsistencies.*

---

## When to Run

- Every 14 days (checked by maintenance-check.py)
- Manually: "Lint my KB", "KB health check", "Check my knowledge base"

---

## What This Skill Does

Scans the knowledge base for structural issues and proposes fixes. This is housekeeping — it keeps the KB navigable and trustworthy as it grows.

**Rule:** Report findings and propose fixes. Never write changes without approval.

---

## Step-by-Step Instructions

### Step 1 — Scan the knowledge base

Read:
- `Knowledge Base/index.md` — the master catalog
- `Knowledge Base/log.md` — the operation log
- All `.md` files in `Knowledge Base/Notes/` (all subfolders)
- All `.md` files in `Knowledge Base/Raw/Sources/`

Build a mental map of: all pages, all `[[wikilinks]]`, all index entries, all raw sources.

---

### Step 2 — Check for issues

Run through each check:

**Orphan pages** — wiki pages in `Notes/` that are not referenced in `index.md`.
- Severity: Medium
- Fix: Add to index, or delete if the page is empty/useless.

**Unindexed sources** — files in `Raw/Sources/` with no matching entry in `index.md`.
- Severity: High (means a source was added but never properly ingested)
- Fix: Run kb-ingest on the source, or add to index manually.

**Broken wikilinks** — `[[links]]` in wiki pages that point to pages that don't exist.
- Severity: Low (Obsidian shows these as unresolved — they're prompts to create the page)
- Fix: Create the missing page, or remove the link if it's not worth a page.

**Stale pages** — wiki pages with a `*Last updated:*` date older than 90 days that cover fast-moving topics (technology, current events, active projects).
- Severity: Low
- Fix: Flag for review. The user decides if the content is still accurate.

**Missing cross-references** — entity or concept names that appear in page text but aren't linked with `[[brackets]]`.
- Severity: Low
- Fix: Add the wikilink.

**Empty pages** — pages with only a header and metadata but no real content.
- Severity: Medium
- Fix: Fill in content from available sources, or delete.

**Index inconsistencies** — counts in the Summary line that don't match actual content.
- Severity: Low
- Fix: Recalculate and update.

---

### Step 3 — Generate report

Present findings grouped by severity:

```
## KB Lint Report — [date]

### High Severity
- [issue description and proposed fix]

### Medium Severity
- [issue description and proposed fix]

### Low Severity
- [issue description and proposed fix]

### Stats
- Total wiki pages: [N]
- Total raw sources: [N]
- Total entities: [N]
- Total concepts: [N]
- Issues found: [N]

---

Want me to fix these? Reply "yes" to apply all fixes, or pick specific ones.
```

---

### Step 4 — Apply fixes on approval

For each approved fix:
- Update the relevant files
- Update index.md if pages were added/removed
- Append a lint entry to log.md:

```markdown
## YYYY-MM-DD — Lint pass
**Issues found:** [N]
**Issues fixed:** [N]
**Details:** [brief summary of what was fixed]

---
```

---

## Edge Cases

- **Empty KB:** If no sources have been ingested yet, report "Knowledge base is empty — nothing to lint. Use 'ingest this' to add your first source." and exit.
- **Very large KB (100+ pages):** Focus on High and Medium severity issues first. List Low severity as a count only ("12 missing cross-references — run again with 'show all' to see details").
