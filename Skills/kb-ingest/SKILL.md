# Skill: kb-ingest
*Ingest a source into the knowledge base — snapshot it, generate wiki pages, update the index.*

---

## When to Run

- Whenever the user wants to save external knowledge to their KB
- Trigger phrases: "Ingest this", "Add to my KB", "Save this to knowledge base", "KB ingest [URL or content]"

---

## What This Skill Does

Takes a single source (URL, pasted text, or file) and processes it through the three-layer knowledge base:

1. **Snapshots** the raw source (immutable, never modified after creation)
2. **Generates wiki pages** — a summary page plus entity and concept pages
3. **Updates the index and log** — so the KB stays navigable

A single source typically creates or updates 5–15 pages. This is by design — cross-referencing is what makes a knowledge base compound over time.

**Rule:** Always propose all changes and ask for approval before writing anything.

---

## Step-by-Step Instructions

### Step 1 — Receive and classify the source

The user provides one of:
- A **URL** — fetch and convert to markdown
- **Pasted text** — use as-is
- A **file path** — read the file

Determine the category by asking if not obvious:
- **work** — professional, industry, or career-related
- **personal** — personal interests, hobbies, general learning
- **my-content** — something the user themselves wrote or published

If the source is very short (< 100 words), ask if it's a complete source or if more context is needed.

---

### Step 2 — Snapshot the raw source

Save an immutable copy to `Knowledge Base/Raw/Sources/`.

**Filename:** `YYYY-MM-DD [source-title].md`

**Format:**
```markdown
---
source: [URL or "pasted text" or "file: path"]
date_ingested: YYYY-MM-DD
author: [original author if known, or "Unknown"]
type: [article|paper|thread|video-transcript|book-excerpt|other]
category: [work|personal|my-content]
---

# [Source Title]

[Full content in markdown]
```

This file is never modified after creation.

---

### Step 3 — Generate the summary page

Create a wiki page in the appropriate `Notes/` subfolder.

**Location:** `Knowledge Base/Notes/[category]/[title].md`

**Format:**
```markdown
# [Title]
*Source: [URL or origin]*
*Ingested: [date]*
*Category: [work|personal|my-content]*

## Summary
[2–3 paragraph summary of the source. Be specific — names, numbers, claims.]

## Key Concepts
- [[Concept Name]] — one-line explanation of the concept as used in this source
- [[Another Concept]] — explanation

## Key Entities
- [[Person or Org Name]] — their role or relevance in this source

## Quotes / Key Excerpts
> [Notable quote with enough context to be useful standalone]

> [Another quote if relevant]

## Takeaways
[How this connects to the user's current work and goals. Reference `me.md` (Current Focus) and `About [You]/goals/1-year.md` for context. If no connection is obvious, say so — don't force it.]

## Related
- [[Other existing wiki page]] — if any existing pages are related
```

**Wikilinks:** Use `[[double brackets]]` for all entity and concept references. These create navigable links in Obsidian and make cross-references explicit.

---

### Step 4 — Update or create entity and concept pages

For each entity and concept mentioned in the summary page's Key Concepts and Key Entities sections:

**Check if a page already exists** in any `Notes/` subfolder. Search by name.

**If the page exists** — append a new reference section:
```markdown

### From: [Source Title] (YYYY-MM-DD)
- [What this source says about the entity/concept]
- [Any new information not already captured]
```

Update the `*Last updated:*` date.

**If the page doesn't exist** — create it in the same category folder as the source:

**Entity page format:**
```markdown
# [Entity Name]
*Type: [person|company|organization|product|project]*
*Last updated: [date]*

## Overview
[Synthesized description from all sources that mention this entity.]

## Mentions
### From: [Source Title] (YYYY-MM-DD)
- [What this source says]
```

**Concept page format:**
```markdown
# [Concept Name]
*Type: [concept|technology|framework|method|theory]*
*Last updated: [date]*

## Overview
[Clear explanation of the concept, synthesized from all sources.]

## Mentions
### From: [Source Title] (YYYY-MM-DD)
- [How this source explains or uses this concept]

## Related Concepts
- [[Related Concept]] — how they connect
```

**Judgment call:** Not every mentioned name needs its own page. Create pages for entities and concepts that are:
- Central to the source (not just mentioned in passing)
- Likely to appear in future sources
- Useful as standalone reference

A good rule: if you'd want to look it up later, it deserves a page.

---

### Step 5 — Update index.md

Open `Knowledge Base/index.md` and:

1. Add a row to the appropriate category table:
   ```
   | YYYY-MM-DD | [Title] | [source URL or type] | [[Notes/category/title]] |
   ```

2. Add new entities to the Entity Index:
   ```
   | [Entity] | [type] | [[Notes/category/title]] |
   ```
   If the entity already exists in the index, append the new page to its "Mentioned In" column.

3. Add new concepts to the Concept Index (same pattern).

4. Update the Summary line at the top with new counts.

5. Update the `*Last updated:*` date.

---

### Step 6 — Append to log.md

Add an entry to the end of `Knowledge Base/log.md`:

```markdown
## YYYY-MM-DD — Ingested: [Source Title]
**Source:** [URL or origin]
**Category:** [work|personal|my-content]
**Raw snapshot:** Raw/Sources/YYYY-MM-DD [title].md
**Pages created:** [list of new pages]
**Pages updated:** [list of updated pages]

---
```

---

### Step 7 — Propose all changes

Before writing anything, present the complete list of changes:

```
## KB Ingest — [Source Title]

### Raw snapshot
[filename and location]

### Summary page (new)
[full proposed content]

### Entity/concept pages
- [Page name] — NEW / UPDATED (what was added)
- [...]

### Index updates
[what rows were added]

### Log entry
[the log entry]

---

Ready to write? Reply "yes" to apply all, or tell me which parts to skip or change.
```

---

## Tips

- **Batch ingesting:** If the user wants to ingest multiple sources, process them one at a time. Each source gets its own full pass. Entity/concept pages will naturally accumulate references across sources.
- **Re-ingesting:** If a source was already ingested (check log.md), tell the user and ask if they want to update the existing pages or skip.
- **Large sources:** For very long articles or papers, focus the summary on the most important 20%. Include the full text in the raw snapshot but be selective in the wiki page.
- **No forced connections:** If a source has nothing to do with the user's goals or current work, the Takeaways section should say so honestly. Don't manufacture relevance.
