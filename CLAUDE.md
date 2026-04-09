# Rootstack — Project Instructions

## What This Is

Rootstack is an open source personal context layer for AI builders. It is a folder-and-file system — designed to live on your computer, open in Obsidian, and be readable by any AI tool (Claude, Codex, Cursor, etc.).

The core idea: most AI tools have their own memory systems, but those are platform-locked, abstract, and hard for humans to review. Rootstack is the alternative — a portable, human-readable model of a person that any AI can consume without re-training. Lightweight markdown files are the primary "language."

**Creator:** Ante Peovic (antepeovic@gmail.com)
**Goal:** Publish as an open source GitHub template repo that AI builders can fork, fill in, and use immediately.
**Target user:** Solo AI builders who use Obsidian, build with AI tools daily, and create content as part of their personal brand.

---

## Architecture Decisions (Already Made)

Do not relitigate these — they are settled:

1. **Markdown-first.** All human-readable content is in `.md` files. Non-markdown files (SQLite databases, scripts) are optional add-ons for power users and are invisible in Obsidian by default.

2. **Dual format is optional, not required.** Markdown is the source of truth. SQLite/JSON companions (for semantic search) are an advanced layer in Knowledge Base only.

3. **README.md is the AI navigator.** Every folder that needs AI navigation has its own README.md. The root README is the entry point for every AI session. It is updated weekly by the readme-updater skill.

4. **Platform-agnostic via stub files.** CLAUDE.md routes Claude to README.md. AGENTS.md routes Codex/OpenAI tools. Both are thin stubs — README.md holds the real context.

5. **Three update tiers:**
   - **Foundation** (background, values, personality) — user provides input, AI writes and formats, rarely changes
   - **Accumulator** (patterns, lessons, skills, people) — AI appends new entries over time, history is preserved
   - **Scratchpad** (now.md) — AI rewrites completely on a schedule, reflects current state only

6. **Content Creation is a core folder, not optional.** The target user is a solo builder with a personal brand. Content creation is part of their operating system.

7. **gitignore defaults to private.** Personal content is excluded by default. Template structure and skills are what get pushed.

---

## Current State of the Build

The full template structure is complete. Every folder exists with README files, template files, and placeholder content. What is NOT yet built:

### Skills (Priority — Build These Next)

Skills live in `/Skills/` and are AI-executable workflows in markdown format. Three core skills need to be built:

#### 1. `readme-updater`
- **What:** Scans the vault structure and rewrites the root README.md to reflect current files and folders.
- **When:** Weekly (or manually triggered).
- **Key behavior:** Should preserve the "How to Find What You Need" section format. Should update folder tables to reflect actual current files. Should not hallucinate files that don't exist.

#### 2. `digest`
- **What:** Reads recent journal entries (last 30 days) and session notes, then:
  - Rewrites `About [You]/now.md` to reflect current focus, projects, challenges, and state of mind
  - Appends new behavioral patterns to `About [You]/patterns/behavioral-patterns.md` (if patterns detected with 3+ evidence points)
  - Appends new lessons to `About [You]/patterns/lessons-learned.md` (if clear lessons surfaced)
- **When:** Monthly (or manually triggered).
- **Key behavior:** Should propose updates and ask for approval before writing. Should not overwrite or delete existing pattern/lesson entries.

#### 3. `people-nudge`
- **What:** Scans `About [You]/people/` for contact files where the most recent "Recent Interactions" entry is 60+ days old. Surfaces a list and prompts the user to add a note.
- **When:** Monthly (or manually triggered).
- **Key behavior:** Read-only scan — never writes to contact files without user input.

---

## Folder Structure

```
README.md                    ← AI navigator (entry point for every session)
CLAUDE.md                    ← You are here — project instructions for Claude
AGENTS.md                    ← Same for Codex/OpenAI tools
tools.md                     ← User's tools and integrations

About [You]/                 ← Identity core
  README.md
  background.md              ← Foundation
  values.md                  ← Foundation
  personality.md             ← Foundation
  operating-manual.md        ← Accumulator (AI refines)
  skills.md                  ← Accumulator
  now.md                     ← Scratchpad (AI rewrites monthly)
  goals/                     ← 1-year, 5-year, 10-year + monthly reviews
  stories/                   ← Personal narratives
  patterns/                  ← behavioral-patterns.md + lessons-learned.md (AI-maintained)
  people/                    ← Lightweight CRM (contact per file)
  learning/                  ← books.md + resources.md

Journal/
  Personal/                  ← DD-MM-YYYY.md
  Work/                      ← DD-MM-YYYY.md

Knowledge Base/
  Notes/work/
  Notes/personal/
  Notes/my-content/

Projects/                    ← One subfolder per project

Content/
  Style/writing-style.md
  Pillars/
  Schedule/LinkedIn|Newsletter|YouTube|X (Twitter)/

Prompts/                     ← Reusable prompts; onboarding.md ships by default

Skills/                      ← Core maintenance skills (to be built — see above)
```

---

## Design Principles

When building or modifying anything in this project, follow these rules:

- **No IDE required.** Everything should work for a user who never opens a terminal. Markdown files are the interface.
- **Obsidian-friendly.** Non-markdown files should not clutter the Obsidian view. Keep scripts and databases in clearly named subfolders.
- **Platform-agnostic skills.** Skills should be written so they work in Claude, Codex, and Cursor. Avoid tool-specific syntax.
- **Propose before writing.** Skills that modify files should show the user what they're about to write and ask for approval. Never silently overwrite.
- **Template files use `[brackets]` for placeholders.** Consistent convention throughout.
- **Keep it lean.** If a feature adds complexity without clear value for the target user, don't add it.

---

## What To Do When Opening This Project

1. Read this file (done).
2. Read `README.md` for the full vault overview.
3. Check `/Skills/README.md` for the current skill build status.
4. Ask Ante what he wants to work on — likely one of the three core skills above.
