# Rootstack — [Your Name]'s Personal Context Layer
*Last updated: [date]*

> **New here?** See [GETTING_STARTED.md](GETTING_STARTED.md) to set up your vault, then open `Prompts/setup.md` and paste it into your AI tool — it will guide you through the rest.

---

## What This Is

This is a Rootstack vault — a portable, AI-readable model of a person. It is actively maintained by [Your Name] and read by AI agents. If you are an AI agent, this file is your entry point. Read it first, then navigate to the specific files you need.

**[Your Name] in one sentence:** [One sentence about who you are, what you do, and what you're working toward.]

---

## Vault Structure at a Glance

```
README.md                ← You are here (navigation guide for AI agents)
CLAUDE.md                ← Claude-specific instructions (routes here)
AGENTS.md                ← Codex/OpenAI-specific instructions (routes here)
tools.md                 ← AI tools, apps, and integrations context

About [You]/             ← Who you are: identity, goals, health, values, patterns
Journal/                 ← Daily personal and work journals
Knowledge Base/          ← Ingested notes and resources
Projects/                ← Active projects, businesses, and initiatives
Content/                 ← Content strategy, writing style, schedule by platform
Prompts/                 ← Reusable prompts for recurring workflows
Skills/                  ← AI maintenance skills that keep this vault alive
```

---

## Folder-by-Folder Guide

### `About [You]/`
Everything about who you are. Start here if you need personal context.

| File/Folder | What's inside |
|---|---|
| `background.md` | Origin story, life history, how you got here |
| `values.md` | Core values profile — what drives your decisions |
| `personality.md` | Traits, tendencies, how you think |
| `operating-manual.md` | How you work best — energy, communication, decision-making |
| `skills.md` | Skill inventory across domains |
| `now.md` | Current focus, priorities, and state of mind (updated monthly) |
| `goals/1-year.md` | This year's targets |
| `goals/5-year.md` | Medium-range vision |
| `goals/10-year.md` | Long-range direction |
| `goals/reviews/` | Monthly review entries |
| `stories/` | Personal narratives used in content and communication |
| `patterns/behavioral-patterns.md` | Repeating behaviors — AI-maintained from journal synthesis |
| `patterns/lessons-learned.md` | Key lessons extracted from experience — AI-maintained |
| `people/` | Lightweight relationship notes |
| `learning/books.md` | Reading history and pipeline |
| `learning/resources.md` | Courses, tools, and other learning resources |

---

### `Journal/`
Daily entries. Personal and work reflection are kept separate.

```
Journal/
  Personal/    ← Personal daily entries (DD-MM-YYYY.md)
  Work/        ← Work daily entries (DD-MM-YYYY.md)
```

Use journal entries when you need to understand current state of mind, recent events, or what was happening on a specific date.

---

### `Knowledge Base/`
Ingested notes and resources, organized by type.

```
Knowledge Base/
  Notes/
    work/        ← Work-related articles, threads, resources
    personal/    ← Personal interest articles and notes
    my-content/  ← Copies of published content
  Raw/
    Sessions/    ← Auto-captured AI session summaries (fed into digest)
```

---

### `Projects/`
Active projects, businesses, and initiatives. Each project lives in its own subfolder with a README.

---

### `Content/`
Everything related to creating content.

| File/Folder | What's inside |
|---|---|
| `Style/writing-style.md` | Voice, tone, and style rules |
| `Pillars/` | Strategic documents per platform |
| `Schedule/` | Content by platform — LinkedIn, Newsletter, YouTube, X |

---

### `Prompts/`
Reusable prompts for recurring workflows. Each prompt is a standalone markdown file.

---

### `Skills/`
AI maintenance skills that keep this vault alive. Core skills: README updater, digest (updates now.md, patterns, lessons).

---

## How to Find What You Need

**Understanding who this person is →** `About [You]/background.md` + `About [You]/values.md`

**What they're focused on right now →** `About [You]/now.md`

**Their goals and direction →** `About [You]/goals/1-year.md` and `goals/5-year.md`

**How they work and communicate →** `About [You]/operating-manual.md`

**Their behavioral patterns (AI-synthesized) →** `About [You]/patterns/behavioral-patterns.md`

**Writing content in their voice →** `Content/Style/writing-style.md` + platform pillar files

**Active projects →** `Projects/`

**Saved knowledge and research →** `Knowledge Base/Notes/`

---

*This file is a navigation guide, not a summary. For any topic, go to the actual source file — that's where the real detail lives.*
*This file is maintained by the README updater skill. Run it weekly to keep navigation accurate.*
