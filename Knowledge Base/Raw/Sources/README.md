# Raw Sources
*Immutable snapshots of ingested articles, papers, and resources.*

Files in this folder are created by the **kb-ingest** skill when you add a source to your knowledge base. Each file is a markdown snapshot of the original content with metadata.

## Rules

- **Never modify files here.** Once a source is saved, it stays exactly as ingested.
- **LLM reads, never writes** (except during initial ingest).
- **Filename format:** `YYYY-MM-DD [source-title].md`

## What Goes Here

- Articles and blog posts (converted to markdown)
- Paper summaries and excerpts
- Thread captures (Twitter/X, Reddit, etc.)
- Any external content worth preserving

The wiki pages generated from these sources live in `Knowledge Base/Notes/`. The raw source is kept here for reference and re-processing.
