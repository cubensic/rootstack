# Rootstack — [Your Name]'s Personal Context Layer
*Last updated: [date]*

> **New here?** See [GETTING_STARTED.md](GETTING_STARTED.md) to set up your vault. Open it in Claude Code, Codex, or any AI tool — it auto-detects the vault and guides you through setup.

---

## What This Is

A Rootstack vault — a portable, AI-readable model of a person. Actively maintained by [Your Name] and read by AI agents.

If you are an AI agent, your entry points are:
- **`me.md`** — portable identity (who the user is, current focus, how to work with them). Always loaded.
- **`vault-map.md`** — navigation manual for the vault. Always loaded.
- This file — high-level overview.

For depth on any topic, follow the pointers in `me.md`.

**[Your Name] in one sentence:** [One sentence about who you are, what you do, and what you're working toward.]

---

## Top-Level Layout

```
me.md                    ← Always-loaded identity (start here)
vault-map.md             ← Always-loaded navigation manual
README.md                ← This file
CLAUDE.md / AGENTS.md    ← Tool-specific load instructions
GETTING_STARTED.md       ← First-time setup guide

About [You]/             ← Full identity: background, values, personality, goals, patterns
Content/                 ← Writing style, pillars, platform schedules
Journal/                 ← Personal and work daily entries
Knowledge Base/          ← Three-layer AI-maintained wiki
Projects/                ← Active projects and initiatives
Skills/                  ← AI maintenance skills (see Skills/index.md)
```

For anything more detailed, read `vault-map.md`.

---

## The Core Idea

Rootstack gives any AI tool — Claude Code, Cursor, Codex, anything — a persistent, portable context layer. You own the files. You take them with you when you switch tools. No lock-in.

Three things make it work:

1. **`me.md`** — a tight identity file always loaded by the AI. Who you are, what you're focused on, how to work with you. Updated weekly by the `digest` skill.
2. **`vault-map.md`** — a navigation manual so the AI knows where to go for depth. Always loaded.
3. **Skills** — AI-executable workflows (markdown files) that keep the vault alive over time. See `Skills/index.md`.

---

## Setup

See [GETTING_STARTED.md](GETTING_STARTED.md). The short version:

1. Clone this repo
2. Open the folder in Claude Code (or any AI tool)
3. The AI detects the vault, walks you through a 2-minute initialization
4. Run the 6 optional setup skills (background, values, personality, writing, goals, me) at your own pace — each is a short conversation

---

## Maintenance

The `maintenance-check.py` script runs at session start and flags overdue skills (digest, vault-map-updater, style-analyzer, goal-review, kb-lint). Claude Code reads the output via a SessionStart hook and offers to run what's due.

---

*This file is a stable, manually-maintained overview. For live vault structure, see `vault-map.md` (auto-updated by the `vault-map-updater` skill).*
