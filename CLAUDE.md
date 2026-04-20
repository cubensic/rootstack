<!-- Keep in sync with AGENTS.md -->
# Rootstack — Instructions for Claude

---

## What This Is

This is a Rootstack vault — a portable, AI-readable personal context layer. It is a folder of markdown files that gives you a complete model of the person you're working with: their background, values, goals, projects, writing voice, and current focus.

Read this file first, then follow the instructions below.

---

## First: Detect the vault state

Check `README.md`. Look for the text `[Your Name]` anywhere in the file.

- **If found → this is a fresh, unconfigured vault.** Follow the Quick Start below.
- **If not found → this vault has been configured.** Follow the Normal Session flow below.

---

## Quick Start (fresh vault)

This should take under 2 minutes. Do not run the full setup — just initialize the vault and give the user context.

**First, explain what this is:**

> "Welcome to Rootstack — your personal context layer for AI.
>
> This vault is a structured folder of markdown files that gives any AI tool you use a complete picture of who you are — your background, how you think, what you're building, how you write, and what you're focused on right now. It means every AI session starts with context instead of from scratch.
>
> You can view and edit everything in Obsidian. The AI keeps it maintained over time through skills that run on a schedule.
>
> Let's get you started — I just need two things."

**Ask only these two things:**
1. What's your name?
2. One sentence about who you are and what you're building.

**Then do this:**
- Replace every instance of `[Your Name]` in `README.md` with their actual name
- Fill in the one-sentence description in `README.md`
- Update `*Last updated:*` to today's date
- Write the file

**Then explain the setup skills:**

> "Your vault is initialized. There are 6 optional setup conversations available that fill in your profile. Each one is a short chat where I ask you questions and draft a section from your answers. You don't have to do any of them right now — or ever. But the more you fill in, the better every AI session becomes.
>
> Here's what's available:
>
> | Setup | What it fills in | Time |
> |---|---|---|
> | **Background** | Your origin story and turning points | ~10–15 min |
> | **Values** | Your value hierarchy (Schwartz framework) | ~10–15 min |
> | **Personality** | Big Five personality profile + work style | ~10–15 min |
> | **Writing style** | Your voice and tone (bring 5–10 writing samples) | ~10–20 min |
> | **Goals** | 10-year direction → 5-year vision → 1-year targets | ~15–20 min |
> | **Me** | Synthesizes the above into `me.md` — the always-loaded identity file | ~5 min (run last) |
>
> Say **'continue setup'** anytime to pick one, or just start working — I'll gently remind you they're there."

Do not start any setup skill automatically. Let the user decide.

---

## Normal Session (configured vault)

### Step 1 — Load context

Read these three files before responding to anything. They're small and always in context:

1. `me.md` — portable identity: who the user is, current focus, how to work with them
2. `vault-map.md` — navigation manual for the vault
3. `README.md` — vault overview (GitHub-facing doc; read for additional context)

Everything else (`About [You]/background.md`, `values.md`, `personality.md`, `goals/`, `patterns/`, KB pages, skill files) is loaded **on-demand** — read only when the task requires it. `me.md` has pointers; follow them when depth is needed.

### Step 2 — Check for remaining setup

Check if any `Skills/setup-*/SKILL.md` files exist.

- **If setup skills exist:** Include one line in your greeting: *"(You have [N] setup sections remaining — say 'continue setup' anytime.)"*
- **If no setup skills exist:** Say nothing about setup. It's complete.

### Step 3 — Ready

Confirm you're ready and ask what they want to work on today.

Do not summarize what you read back to them unless they ask. Just be ready.

---

## Handling "continue setup"

When the user says "continue setup", "what setup is left", or similar:

1. Check which `Skills/setup-*/SKILL.md` files still exist
2. List the remaining ones with a one-line description of each
3. Suggest a recommended order (background → values → personality → writing → goals → me) but let them choose. `setup-me` synthesizes from the others, so it should run last.
4. When they pick one, read that skill's `SKILL.md` and follow its instructions exactly

---

## Rules That Always Apply

- **Propose before writing.** Any file you modify must be shown to the user first. Get a "yes" before writing.
- **Never delete existing content.** If a file has entries (patterns, lessons, people), only append — never remove.
- **Markdown only.** All user-facing content is `.md`. Don't create other file types unless asked.
- **Keep it honest.** Don't invent content for the user's files. Draft from what they tell you, not from assumptions.
- **Sessions are captured automatically.** The session-harvest skill (`Skills/session-harvest/`) copies raw Claude Code session transcripts and processes them into summaries. This runs as part of the digest flow. You do not need to manually log sessions — the raw transcripts are the source of truth.
- **Knowledge base is three layers.** Raw sources (`Knowledge Base/Raw/Sources/`) are immutable — never modify them after ingest. Wiki pages (`Knowledge Base/Notes/`) are LLM-maintained and updated whenever new sources connect to existing pages. `Knowledge Base/index.md` tracks everything. When ingesting sources, follow the kb-ingest skill.
- **Setup skills self-delete.** When a setup skill completes, it deletes its own folder. Never recreate a deleted setup skill.
- **`me.md` is the portable identity layer.** It's always loaded. The `digest` skill updates its `## Current Focus` section weekly. Deeper identity details live in `About [You]/`.
- **`vault-map.md` is the navigation map.** Always loaded. Replaces the need for folder-level READMEs. The `vault-map-updater` skill proposes updates when the vault structure changes.
