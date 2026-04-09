# Rootstack — Product Requirements Document

**Version:** 0.1
**Author:** Ante Peovic
**Status:** Draft
**Last updated:** April 2026

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Product Vision](#3-product-vision)
4. [Target User](#4-target-user)
5. [Core Design Principles](#5-core-design-principles)
6. [Architecture Overview](#6-architecture-overview)
7. [Product Requirements](#7-product-requirements)
   - 7.1 Root Level
   - 7.2 About [You]
   - 7.3 Journal
   - 7.4 Knowledge Base
   - 7.5 Projects
   - 7.6 Content
   - 7.7 Prompts
   - 7.8 Skills
8. [Memory & Synthesis System](#8-memory--synthesis-system)
9. [Core Maintenance Skills](#9-core-maintenance-skills)
10. [Non-Functional Requirements](#10-non-functional-requirements)
11. [Out of Scope](#11-out-of-scope)
12. [Phases & Roadmap](#12-phases--roadmap)
13. [Success Metrics](#13-success-metrics)
14. [Open Questions](#14-open-questions)

---

## 1. Executive Summary

Rootstack is an open source, file-based personal context layer for AI builders. It is a structured folder system — designed to live on the user's computer, be viewed in Obsidian, and be read by any AI tool (Claude, Codex, Cursor, or others). It gives AI systems a rich, portable, human-readable model of the person they are working with, without locking that model into any single platform.

The core insight: AI tools are increasingly capable, but they lose context between sessions and across platforms. Existing solutions (platform-native memory, second-brain tools, knowledge bases) are either platform-locked, too abstract for humans to review, or too narrow in scope. Rootstack is a complete personal operating layer — identity, goals, journal, projects, knowledge, and content — structured so that both humans and AI agents can navigate it efficiently.

The project is:
- **Open source** — published as a GitHub template repository
- **Markdown-first** — all content is in plain `.md` files, viewable in Obsidian without any technical setup
- **AI-agnostic** — works with any AI tool that can read files
- **Maintained by AI** — comes with skills that keep the vault alive automatically

---

## 2. Problem Statement

### 2.1 The Memory Problem

Every major AI tool has its own memory system. Claude has memory. ChatGPT has memory. Cursor has rules files. Codex has AGENTS.md. The result is that a person's context is fragmented across platforms — and the memory within each platform is typically stored as JSON blobs or hidden files that the user cannot easily read, review, or correct.

When you switch AI tools or start a new session, you lose context. When you want to check what your AI "knows" about you, you can't. When the AI gets something wrong about your preferences or history, you have no easy way to fix it.

### 2.2 The Second Brain Gap

The second brain movement (Obsidian, Notion, Roam, etc.) has given many people a place to collect and organize knowledge. But a knowledge base alone is not a model of a person. It captures what you've consumed, not who you are, what you're working toward, how you think, or what you're doing right now.

An AI working from a knowledge base knows what you've saved. An AI working from a Rootstack vault knows *you* — your background, values, patterns, current focus, goals, and operating style. That is a fundamentally different level of context.

### 2.3 The Maintenance Problem

Personal knowledge systems go stale. Users fill them in at setup and never update them. The deeper problem is that meaningful updates require self-reflection and effort — two things that are hard to sustain as a habit.

Rootstack solves the maintenance problem by giving AI the responsibility of keeping the vault current. Scheduled skills synthesize recent journals and sessions, update the "current state" file, append new behavioral patterns, and flag stale relationship notes. The human reviews and approves changes but doesn't have to initiate them.

---

## 3. Product Vision

**Rootstack is the foundation layer that every AI system runs on.**

A person builds their Rootstack vault once and then connects every AI tool they use to it. The vault becomes their persistent, portable identity across sessions, platforms, and tools. As they grow and evolve, the vault evolves with them — maintained partly by themselves and partly by AI.

For AI builders specifically, Rootstack is the infrastructure beneath their entire setup. Their automations know who they are. Their content tools know their voice. Their business tools know their strategy. Their research tools know their knowledge base. All of it runs on Rootstack.

---

## 4. Target User

### Primary User: The Solo AI Builder

Rootstack is designed for people who:

- Use AI tools daily as part of their work (Claude, Codex, Cursor, Perplexity, etc.)
- Have adopted or are adopting Obsidian as a personal knowledge system
- Are building solo businesses, side projects, or personal brands — often as "solo builders" augmented by AI
- Create content as part of their marketing or distribution strategy
- Are comfortable with file systems and markdown, but don't want to use a terminal for everyday tasks
- Value portability and ownership of their data

**Profile:** Technically adjacent but not necessarily developers. Think: the Karpathy knowledge base audience, indie hackers, creator-builders, AI consultants, freelancers building AI-augmented practices. The wave of solo builders emerging from the AI transition.

### Secondary Users

- **Developers** who want a more structured personal context layer than a single `.cursorrules` or `CLAUDE.md` file
- **Knowledge workers** who use AI heavily and want persistent context across sessions
- **Teams** in early stages where each founder/operator maintains their own Rootstack vault

### Who This Is NOT For

- Absolute beginners to AI tools or Obsidian
- Users who want a hosted/SaaS solution
- Users who need multi-user collaboration features
- Enterprises with compliance requirements around personal data

---

## 5. Core Design Principles

These are settled decisions. They should not be relitigated without strong evidence.

### 5.1 Markdown-First
All human-facing content is in `.md` files. Non-markdown files (SQLite databases, Python scripts, JSON) are optional power-user add-ons and are invisible in the default Obsidian view. Markdown is the primary "language" of the person using this system.

### 5.2 No Terminal Required
Everything a user needs to do in their day-to-day use of Rootstack should be possible without opening a terminal or IDE. Setup may require minimal command-line work (git clone, npm install), but ongoing use should be entirely file-based.

### 5.3 Platform-Agnostic
Rootstack must work with Claude, Codex, Cursor, and any future AI tool that can read files. There is no tool-specific logic in the core vault structure. Platform-specific files (CLAUDE.md, AGENTS.md) are thin stubs that route to the universal README.md.

### 5.4 README.md as the Nervous System
Every folder with AI-navigable content has a README.md that describes what's inside and where to look. The root README.md is the entry point for every AI session. It is kept current by the readme-updater skill.

### 5.5 Propose Before Writing
Any skill that modifies files must show the user what it is about to write and ask for approval before making changes. The user is always in control. Silent overwrites are not permitted.

### 5.6 Three Update Tiers
Files are categorized by how they change, and skills respect this categorization:

| Tier | Description | Examples | Updated by |
|---|---|---|---|
| Foundation | Stable. Reflects who you are. | background.md, values.md | Human provides input, AI writes |
| Accumulator | Grows over time. History preserved. | patterns, lessons, skills, people | AI appends; never overwrites |
| Scratchpad | Current state only. Fully rewritten on schedule. | now.md | AI rewrites; old version replaced |

### 5.7 Lean by Default
The base template ships with the minimum structure needed to be useful. Optional add-ons (SQLite, scripts, advanced skills) are documented but not bundled. Users extend as needed.

---

## 6. Architecture Overview

```
rootstack/
  README.md                    ← Root AI navigator (updated weekly by skill)
  CLAUDE.md                    ← Stub for Claude Code / Claude Desktop
  AGENTS.md                    ← Stub for Codex / OpenAI tools
  tools.md                     ← User's active tools and integrations
  .gitignore                   ← Personal content excluded by default
  PRD.md                       ← This document

  About [You]/                 ← Identity core
  Journal/                     ← Daily reflection (personal + work)
  Knowledge Base/              ← Ingested notes and resources
  Projects/                    ← Active projects and businesses
  Content/                     ← Content strategy, voice, schedule
  Prompts/                     ← Reusable AI prompts
  Skills/                      ← Maintenance automation skills
```

### Platform Adapter Pattern

AI tools find their entry point via a tool-specific stub file, which routes them to README.md:

```
Claude reads CLAUDE.md → "Read README.md for context"
Codex reads AGENTS.md → "Read README.md for context"
Cursor reads .cursorrules → "Read README.md for context"
```

The root README.md is the single source of truth. All platform-specific files are generated stubs.

### Dual Format (Optional)

For users who want semantic search over their Knowledge Base, a companion SQLite vector database can be maintained alongside the markdown notes. This is opt-in. The markdown files remain the source of truth — the database is a derived layer. This pattern may be extended to other folders (People, Projects) in future versions.

---

## 7. Product Requirements

### 7.1 Root Level

**Files that ship with the template:**

| File | Purpose | Required |
|---|---|---|
| README.md | AI navigator and vault overview | Yes |
| CLAUDE.md | Claude-specific stub | Yes |
| AGENTS.md | Codex/OpenAI stub | Yes |
| tools.md | User's tools and integrations | Yes |
| .gitignore | Excludes personal content by default | Yes |
| PRD.md | This document | Yes |

**README.md requirements:**
- Must include a one-sentence description of the vault owner (filled in at setup)
- Must include the full folder structure with one-line descriptions
- Must include a "How to Find What You Need" section with common query patterns
- Must include a timestamp for when it was last updated
- Must be maintainable by the readme-updater skill without human editing

**tools.md requirements:**
- Lists active AI tools the user has access to
- Lists key apps and services in the user's stack
- Lists active automations and integrations (including Rootstack skills)
- Includes a "Notes for AI Agents" section for any tool-specific context

**.gitignore defaults:**
- Excludes all personal content: About [You]/ (except README), Journal/, Projects/, Content/Schedule/
- Includes: folder structure, template files, README files, Skills/, Content/Style/, Content/Pillars/, Prompts/

---

### 7.2 About [You]

The identity core of the vault. Contains everything about who the person is.

**Folder structure:**
```
About [You]/
  README.md
  background.md         ← Foundation
  values.md             ← Foundation
  personality.md        ← Foundation
  operating-manual.md   ← Accumulator
  skills.md             ← Accumulator
  now.md                ← Scratchpad
  goals/
    1-year.md
    5-year.md
    10-year.md
    reviews/
      (Template) Monthly Review.md
  stories/
    (Template) Story.md
  patterns/
    behavioral-patterns.md   ← Accumulator (AI-maintained)
    lessons-learned.md       ← Accumulator (AI-maintained)
  people/
    README.md
    (Template) Contact.md
  learning/
    books.md
    resources.md
```

**background.md requirements:**
- Covers origin, education/career history, and current chapter
- Written by AI from a guided conversation with the user
- Updated when the user's life chapter changes significantly
- Should be readable as a narrative, not a resume

**values.md requirements:**
- Documents core values ranked by dominance
- Covers where values conflict (useful for AI decision support)
- Covers non-negotiables
- Should include the source/method (e.g., Schwartz Values Assessment) and date

**personality.md requirements:**
- Covers cognitive style, work style, and communication preferences
- Covers what energizes and what drains
- Can reference formal assessments (MBTI, Big Five, etc.) with results and dates
- Written by AI from user input; refined over time

**operating-manual.md requirements:**
- Written as instructions for AI agents and collaborators
- Covers working hours/energy patterns, how to support them best, decision-making style
- Covers known blind spots and things to avoid
- Covers preferred output formats
- Maintained as an accumulator: AI refines specific sections as it learns new preferences

**skills.md requirements:**
- One section per skill domain (Coding, Marketing, Design, Communication, etc.)
- Each section includes level (Beginner/Intermediate/Advanced), current application, tools used, and gaps
- Languages section with proficiency levels
- Maintained as an accumulator: AI appends new skills or updates proficiency levels as they develop

**now.md requirements:**
- Answers: what is this person currently focused on, what are their active projects, what is hard right now, what is their state of mind
- Rewritten completely by the digest skill (monthly or on demand)
- Sourced from recent journal entries, active Projects folder, and goals
- Should reflect current reality, not aspirations

**goals/ requirements:**
- 1-year.md: specific and measurable targets for the current year, plus leading indicators
- 5-year.md: medium-range vision covering work, lifestyle, financial, and personal growth
- 10-year.md: long-range direction covering impact, identity, and legacy
- Monthly review template: wins, misses, lessons, patterns noticed, focus for next month
- Monthly reviews are written collaboratively: user provides input, AI structures

**stories/ requirements:**
- Each story is a standalone markdown file
- Stories include the narrative, core message, where to use it, and topic tags
- Used by content tools to pull relevant personal narratives
- Added by user over time; AI can help structure and polish

**patterns/behavioral-patterns.md requirements:**
- Each entry: pattern name, one-sentence description, evidence (with dates), why it matters
- AI-maintained: new entries appended from journal/session synthesis
- Newest entries at top
- Human review required before new entries are written
- Entries are never deleted by AI — only humans remove patterns

**patterns/lessons-learned.md requirements:**
- Each entry: lesson title + date, one-sentence lesson, context, how to apply it
- AI-maintained: appended from journal/session synthesis
- Newest entries at top
- Same human review requirement as behavioral-patterns.md

**people/ requirements:**
- One markdown file per contact
- Template includes: name, role/context, location, relationship type, what matters to them, recent interactions (append-only log), notes
- "Recent interactions" section is append-only — new entries at top with date
- AI can suggest updates when a person is mentioned in journals or sessions
- people-nudge skill flags contacts not updated in 60+ days
- Contacts can be organized flat or in subfolders (Family/, Friends/, Professional/, Clients/)

**learning/ requirements:**
- books.md: currently reading, read (with key takeaway), to read
- resources.md: courses/programs, creators followed (with reason), reference tools
- Both are accumulators: new entries added over time

---

### 7.3 Journal

Daily reflection, kept separate for personal and work contexts.

**Folder structure:**
```
Journal/
  Personal/    ← Personal daily entries
  Work/        ← Work daily entries
```

**File naming convention:** `DD-MM-YYYY.md` (e.g., `09-04-2026.md`)

**Integration with Obsidian:** The Obsidian Daily Notes plugin (or Templater) can be configured to create journal entries automatically in the correct folders with the correct naming convention. This should be documented in the getting started guide.

**Integration with AI:** The digest skill reads journal entries from the last 30 days as its primary input. Journal entries are the raw material for synthesizing now.md, behavioral patterns, and lessons learned.

**Requirements:**
- No enforced template for journal entries — freeform writing is the point
- Folder structure allows AI to query by date range (e.g., "last 30 days") efficiently
- Older entries can be archived in year/month subfolders without breaking any skill

---

### 7.4 Knowledge Base

The user's personal library: ingested notes, articles, and resources.

**Folder structure:**
```
Knowledge Base/
  README.md
  Notes/
    work/        ← Work-related articles, threads, resources
    personal/    ← Personal interest notes
    my-content/  ← Copies of own published content
  databases/     ← Optional: SQLite vector databases (advanced)
  scripts/       ← Optional: ingestion and query scripts (advanced)
```

**Note file requirements:**
- Each note is a markdown file with: source (URL or origin), date ingested, 1–2 sentence summary, full content or key excerpts
- File names should be dated and descriptive (e.g., `2026-04-09 How to build a personal AI stack.md`)

**Semantic search (optional, advanced):**
- SQLite vector databases can be maintained alongside markdown notes
- Three databases: kb-work.db, kb-personal.db, kb-my-content.db
- The kb-ingest skill handles ingestion into both markdown and database
- The kb-query skill handles semantic search across databases
- Markdown remains the source of truth; databases are derived

**kb-ingest skill requirements:**
- Accepts a URL or pasted content
- Fetches and cleans the content
- Saves as a structured markdown note in the correct Notes/ subfolder
- Optionally embeds and stores in SQLite (if database is configured)
- Always fetches the real title — never infers it

**kb-query skill requirements:**
- Accepts a natural language query
- Returns relevant notes with source, date, and key excerpt
- Searches across all three databases (or markdown files if no databases)

---

### 7.5 Projects

Active projects, businesses, and initiatives.

**Folder structure:**
```
Projects/
  README.md
  (Template) Project.md
  [Project Name]/
    README.md
    [project files]
```

**Project folder requirements:**
- Each project has its own subfolder
- Each project subfolder has a README.md covering: what it is, current status, goal/deadline, key files, and next action
- Project files can include: strategy docs, SOPs, playbooks, client files, research notes — anything relevant to that project
- No enforced structure within a project folder beyond the README

**Projects/README.md requirements:**
- Lists all active projects with one-line descriptions and current status
- Updated by the readme-updater skill to reflect actual project folders
- Maintained as an accumulator: new projects added; completed projects moved to an Archive/ subfolder

---

### 7.6 Content

Everything related to creating and publishing content.

**Folder structure:**
```
Content/
  README.md
  Style/
    writing-style.md
  Pillars/
    README.md
    [Platform].md      ← One file per platform
  Schedule/
    LinkedIn/
    Newsletter/
    YouTube/
    X (Twitter)/
```

**Rationale for inclusion:** The target user (solo AI builder) uses content creation as their primary distribution and marketing channel. Content infrastructure is a core part of their operating system, not an optional add-on.

**writing-style.md requirements:**
- Captures the user's voice in one sentence
- Documents tone (formality, energy, POV)
- Lists what the user consistently does in their best writing
- Lists what the user does not do (things to avoid)
- Documents per-platform tone adaptations
- References writing samples for AI calibration
- Written by AI from user input and writing samples; refined over time
- This is the most important file for any AI-assisted content creation

**Platform pillar files requirements:**
- One file per platform the user publishes on
- Each covers: goal (what this platform does for them), audience, content format, posting rhythm, tone adaptation, what works, what doesn't
- Written by user with AI assistance; reviewed quarterly

**Schedule/ requirements:**
- Platform subfolders mirror the Pillars/ structure
- Each content piece is a markdown file named by date: `DD-MM-YYYY [Title].md`
- Recent files live in the platform root; older files can be archived in month subfolders
- Default platforms: LinkedIn, Newsletter, YouTube, X (Twitter) — users add/remove as needed

---

### 7.7 Prompts

Reusable AI prompts for recurring workflows.

**Folder structure:**
```
Prompts/
  README.md
  onboarding.md     ← Ships with template
  [workflow].md
```

**Requirements:**
- Each prompt is a standalone markdown file, named by the workflow it serves
- Prompts use `[brackets]` for context-specific fill-ins
- Prompts must be platform-agnostic — they should work in Claude, Codex, or any tool
- onboarding.md ships with the template: instructs AI to read README.md, now.md, and operating-manual.md before beginning work

**Recommended prompts to build (not shipped, documented as suggestions):**
- `background-builder.md` — guided conversation to fill out background.md
- `weekly-review.md` — structured weekly reflection
- `content-brainstorm.md` — generate content ideas from KB and recent activity
- `goal-setting.md` — annual or quarterly goal-setting session
- `discovery-call-prep.md` — research and brief for a sales call

---

### 7.8 Skills

AI-executable maintenance workflows that keep the vault alive.

**Folder structure:**
```
Skills/
  README.md
  readme-updater/
    SKILL.md
  digest/
    SKILL.md
  people-nudge/
    SKILL.md
```

**General skill requirements:**
- Each skill lives in its own subfolder with a SKILL.md file
- SKILL.md contains step-by-step instructions for an AI agent to execute the skill
- Skills must be platform-agnostic (work in Claude, Codex, Cursor)
- Skills that modify files must follow the "propose before writing" principle
- Skills should be triggerable manually or on a schedule

---

## 8. Memory & Synthesis System

The memory system is the mechanism by which Rootstack learns and evolves over time. It is the core differentiator from static personal knowledge systems.

### 8.1 How It Works

The system has three inputs and three outputs:

**Inputs:**
- Daily journal entries (Personal/ and Work/)
- AI session notes or summaries (if the user logs them)
- Goals and project status (from Projects/ and goals/)

**Outputs:**
- `now.md` — current state (scratchpad, rewritten)
- `behavioral-patterns.md` — repeating behaviors (accumulator, appended)
- `lessons-learned.md` — extracted insights (accumulator, appended)

**The digest skill** is the mechanism that transforms inputs into outputs. It runs monthly (or on demand) and handles all three outputs in a single pass.

### 8.2 Human Oversight

The system is designed so that humans remain in control:

- The digest skill always shows proposed changes before writing
- Users can accept, reject, or edit each proposed update
- No file is ever silently overwritten
- Users can manually edit any file at any time — the skill respects existing content
- The vault is git-backed (recommended), so any AI change can be rolled back

### 8.3 Pattern Detection Threshold

A behavioral pattern is only added to behavioral-patterns.md if it has been observed in at least 3 separate journal entries or sessions. Single occurrences are not patterns. This prevents noise and ensures entries are meaningful.

### 8.4 Memory vs. Journal

The journal is the raw record — freeform, daily, unfiltered. The patterns and lessons files are the synthesis — structured, reviewed, AI-maintained. Users should not manually edit the patterns files except to remove incorrect entries. The journal is the source of truth; the synthesis files are derived.

---

## 9. Core Maintenance Skills

Three skills ship with the Rootstack template. These are the minimum required to keep the vault functional over time.

### 9.1 readme-updater

**Purpose:** Keep the root README.md accurate as the vault grows and changes.

**Trigger:** Weekly (scheduled) or manual ("update my README").

**Process:**
1. Scan the vault folder structure (2 levels deep)
2. Compare to the current README.md table of contents
3. Identify new folders/files not in README, and listed entries that no longer exist
4. Propose updated README.md content (preserving "How to Find What You Need" section format)
5. Show diff to user and ask for approval
6. Write approved changes

**Constraints:**
- Must not hallucinate file descriptions — only describe files that exist
- Must preserve the vault owner's one-sentence description at the top
- Must preserve any custom notes in the "How to Find What You Need" section

### 9.2 digest

**Purpose:** Synthesize recent journal entries and sessions into the three AI-maintained files.

**Trigger:** Monthly (scheduled) or manual ("run my digest").

**Process:**
1. Read all journal entries from the last 30 days (Personal/ and Work/)
2. Read current now.md, behavioral-patterns.md, and lessons-learned.md for context
3. Read current goals and active projects
4. Generate:
   - Draft rewrite of now.md (current focus, projects, challenges, state of mind)
   - List of detected behavioral patterns with 3+ evidence points (not already in the file)
   - List of distinct lessons extracted (not already in the file)
5. Present each proposed change separately, ask for approval before writing
6. Write only approved changes

**Constraints:**
- Must not delete or overwrite existing entries in behavioral-patterns.md or lessons-learned.md
- Must flag if no new patterns or lessons were detected (rather than inventing content)
- Patterns require 3+ evidence points from distinct dates
- now.md rewrite replaces the file entirely; user approves the full new version

### 9.3 people-nudge

**Purpose:** Prevent the People folder from going stale.

**Trigger:** Monthly (scheduled) or manual ("check my contacts").

**Process:**
1. Scan all files in About [You]/people/ (excluding README.md and template files)
2. For each contact file, find the most recent date in the "Recent Interactions" section
3. Identify contacts with no interaction logged in the last 60 days
4. Present the list to the user with the last interaction date for each
5. For each flagged contact, ask if there's anything worth noting
6. Write user-provided notes to the contact file (append to Recent Interactions)

**Constraints:**
- Read-only scan — never writes to contact files without explicit user input
- Does not flag contacts where the "Recent Interactions" section is empty (new contacts)

---

## 10. Non-Functional Requirements

### 10.1 Compatibility

- **Obsidian:** All markdown files must render correctly in Obsidian. Non-markdown files must not clutter the Obsidian vault view.
- **Git:** The folder structure must be git-compatible. The default .gitignore must protect personal content from accidental public commits.
- **AI tools:** The vault must be readable by Claude, Codex, Cursor, and any tool that can access a filesystem or folder. No proprietary formats.
- **Operating systems:** Must work on macOS and Windows at minimum. File naming must avoid OS-reserved characters.

### 10.2 Performance

- The root README.md must load quickly and give an AI sufficient context without reading every file. It is the performance optimization — the AI should need to read fewer files, not more.
- Individual folder README files serve the same function at the subfolder level.

### 10.3 Privacy & Security

- Personal content is excluded from git by default via .gitignore
- Users who choose to push personal content (e.g., to a private repo) do so explicitly
- No external API calls are required for basic vault use
- Skills that require external APIs (e.g., embedding for KB semantic search) are opt-in add-ons

### 10.4 Maintainability

- All core files use consistent template structures with `[bracket]` placeholders
- Template files are clearly marked so users know what to fill in
- Folder README files document the update type (Foundation / Accumulator / Scratchpad) for each file
- The PRD and CLAUDE.md provide enough context for any contributor to understand the project without prior conversation

---

## 11. Out of Scope

The following are explicitly not part of Rootstack v1:

- **Hosted/cloud version** — Rootstack is local-first. No SaaS, no server, no sync service.
- **Mobile app or interface** — Obsidian has a mobile app; that is sufficient for now.
- **Multi-user collaboration** — One vault per person. Shared vaults are not a v1 use case.
- **Real-time AI integration** — Skills are run on demand or on a schedule; Rootstack is not a real-time AI layer.
- **Built-in LLM** — Rootstack has no bundled AI. It works with whatever AI tool the user already has.
- **Visual dashboards** — Everything is markdown. No charts, graphs, or UI.
- **Automated vault backup** — Recommended via git, but not built in.
- **Paid tier or monetization** — This is an open source project. Monetization (if any) happens separately.

---

## 12. Phases & Roadmap

### Phase 1 — Template (Current)

**Goal:** Publish a complete, usable template repository that someone can fork and start using today.

**Deliverables:**
- Complete folder structure with all template files
- Root README.md with full navigation
- CLAUDE.md, AGENTS.md platform stubs
- About [You]/ with all core files and subfolders
- Journal/, Knowledge Base/, Projects/, Content/, Prompts/ with templates
- Skills/README.md documenting the three core skills to build
- PRD.md (this document)
- CLAUDE.md as a developer brief for Claude Code
- .gitignore with sensible defaults
- Getting started guide (README in repo root, separate from vault README)

**Success:** Someone can fork the repo, open it in Obsidian, and know exactly what to do to get started.

### Phase 2 — Core Skills

**Goal:** Build and publish the three maintenance skills so the vault stays alive automatically.

**Deliverables:**
- `Skills/readme-updater/SKILL.md` — fully working skill
- `Skills/digest/SKILL.md` — fully working skill
- `Skills/people-nudge/SKILL.md` — fully working skill
- Documentation for how to schedule skills with Claude Code, Codex, or other tools
- Testing with real vault data (Ante's vault as the test case)

**Success:** A user can run all three skills and the vault updates correctly without breaking existing content.

### Phase 3 — Getting Started Experience

**Goal:** Make it easy for a new user to fill in their vault from scratch.

**Deliverables:**
- `Prompts/background-builder.md` — guided conversation to complete background.md
- `Prompts/values-builder.md` — guided conversation to complete values.md
- `Prompts/style-extractor.md` — prompt that takes writing samples and produces writing-style.md
- A getting-started checklist: what to fill in first, in what order
- Video walkthrough (optional, for distribution)

**Success:** A new user can go from empty vault to meaningfully filled in the first two sections (About [You] + Content/Style) in under 2 hours with AI assistance.

### Phase 4 — Ecosystem

**Goal:** Build out the ecosystem of optional add-ons and community contributions.

**Potential deliverables:**
- KB semantic search (kb-ingest + kb-query skills with SQLite)
- Additional skill packs (content brainstorm, discovery call prep, goal-setting)
- Community contributions: starter platform pillar templates, story templates, prompt library
- Integration guides for specific tools (Claude Desktop, Cursor, OpenClaw)
- `.cursorrules` adapter file for Cursor users

---

## 13. Success Metrics

### Phase 1 Success
- GitHub repo is publicly available and forkable
- At least one person other than the creator successfully sets up the vault from the template
- The CLAUDE.md brief is sufficient for a new AI session to understand the project and continue building without re-explanation

### Phase 2 Success
- All three core skills run without errors on a real vault
- The digest skill correctly identifies behavioral patterns from journal data
- Skills follow the "propose before writing" principle — no silent overwrites

### Phase 3 Success
- A new user can complete the About [You] core files (background, values, personality, skills) within a 2-hour guided session using the builder prompts
- The writing-style.md output from the style-extractor prompt matches the user's voice well enough to use for content without heavy editing

### Long-Term Success
- GitHub stars / forks as a proxy for adoption
- Number of community-contributed skills or prompt packs
- Mention in the AI builder community (Karpathy adjacent, indie hackers, AI builder Twitter/LinkedIn)
- Ante's ability to use it to drive B2C revenue (courses, premium skill packs, community)

---

## 14. Open Questions

The following decisions have not yet been finalized:

1. **Versioning strategy for vault content** — How should users handle the risk of AI skills corrupting content when git is not configured? Should the template ship with a built-in "backup before run" step in each skill?

2. **People folder — flat vs. organized** — Should the default template organize contacts into subfolders (Family, Friends, Professional, Clients) or keep it flat? Flat is simpler; organized is easier to navigate at scale.

3. **Content platforms default** — LinkedIn, Newsletter, YouTube, and X are the default platforms. Should the template ship with pre-written pillar files for these, or leave them blank? Pre-written reduces setup friction but may not match all users.

4. **Skill format standardization** — Should SKILL.md files follow a strict schema (with sections like Trigger, Process, Constraints, Examples) or be freeform instructions? Strict schema is easier for AI to parse; freeform is easier to write.

5. **GitHub repo name** — rootstack, rootstack.fyi, or rootstak.com as the primary domain/handle. Final decision pending domain availability check.

6. **Community contribution model** — Should skills and prompts contributed by the community ship in the main repo or in a separate community repo? This affects maintenance burden and quality control.

7. **Dream log** — The creator's vault includes a dream log (Journal/Dreams/). Should this be included in the template as an optional section, or excluded to keep scope focused?

---

*This PRD reflects decisions made through April 2026. It should be updated as the project evolves. Architecture decisions marked "settled" in Section 5 require strong evidence to reverse.*
