# Knowledge Base
*Your personal library. Ingested notes and resources, organized by type.*

## Structure

```
Knowledge Base/
  Notes/
    work/        ← Work-related articles, threads, and resources
    personal/    ← Personal interest notes
    my-content/  ← Copies of your own published content
  Raw/
    Sessions/    ← Raw .jsonl session transcripts (copied from Claude Code)
  Sessions/      ← Processed session summaries (markdown, fed into digest)
```

## How to Use

Add notes by dropping markdown files into the appropriate `Notes/` subfolder, or use the kb-ingest skill to ingest URLs and automatically save them as structured notes.

Each note file should include at the top:
- **Source** (URL or origin)
- **Date ingested**
- **Summary** (1–2 sentences)
- **Full content or key excerpts**

## Optional: SQLite for Semantic Search

If you want AI to query your knowledge base semantically (find notes by meaning, not just keyword), you can add a `databases/` folder with SQLite vector databases. The kb-ingest and kb-query skills support this. Not required for basic use.
