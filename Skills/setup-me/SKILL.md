# Setup Skill: Me
*One-time skill. Synthesizes `me.md` from the other setup files (background, values, personality, goals, writing-style), asks a few targeted questions to fill gaps, then self-deletes.*

---

## Trigger

- "Set up my me.md"
- "Set up my identity file"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

`me.md` is the always-loaded portable identity file at the root of the vault. Every AI tool — Claude Code, Cursor, Codex, Gemini, anything — reads it at session start. It needs to be **tight** (50–80 lines filled) and **self-sufficient** (enough for a tool loading only one file).

This skill runs *after* the other five setup skills because it synthesizes from them. It should not be the first setup anyone does.

Fills in `me.md` at the repo root.

---

## Before Starting

Check which other setup skills have completed (folder deleted = done):
- `Skills/setup-background/` → if gone, read `About [You]/background.md`
- `Skills/setup-values/` → if gone, read `About [You]/values.md`
- `Skills/setup-personality/` → if gone, read `About [You]/personality.md`
- `Skills/setup-goals/` → if gone, read `About [You]/goals/1-year.md`
- `Skills/setup-writing/` → if gone, read `Content/Style/writing-style.md`

If **none or only one** of the above is done, tell the user:

> "This skill synthesizes your `me.md` from your other setup files. Right now only [N] of the 5 other setup skills are complete, so there's not much for me to draw from. I can still do it — we'll use what's there and leave placeholders — or you can come back after finishing a few more setups. Which do you prefer?"

If the user wants to proceed anyway, continue. Otherwise, exit cleanly.

Otherwise, tell the user:

> "This will take about **5 minutes**. I'll read your other setup files, draft a tight `me.md` that any AI tool can use, and ask you a few quick questions to fill gaps. This file gets loaded at the start of every session, so we're keeping it short and high-signal.
>
> Ready?"

Wait for confirmation.

---

## Steps

### Step 1 — Read all available source files

Read everything that exists:
- `me.md` — the current template/state
- `About [You]/background.md`
- `About [You]/values.md`
- `About [You]/personality.md`
- `About [You]/goals/1-year.md`
- `Content/Style/writing-style.md`
- `README.md` — for the one-sentence bio

### Step 2 — Draft each section from source material

Synthesize each section of `me.md`:

**Quick Bio** — Pull from `README.md`'s one-sentence description, expand using `background.md` (current chapter, identity threads). Keep to 3–5 sentences. Must answer: who they are, what they're building, where they are in life.

**Current Focus** — Leave as a 3-line placeholder with `[To be updated by digest]`. Digest will fill this weekly. Do not invent priorities.

**How to Work With Me** — Pull from `personality.md`'s "How to Work With Me" section if it exists. Condense to 3–4 bullets: communication style, decision-making style, what they want from AI, work rhythm. Strip anything verbose.

**Core Values** — Pull top 3–5 from `values.md`. One line each — the value name + one line on what it means in practice for this person. Not textbook definitions.

**Key Frameworks I Think Through** — This usually isn't in any setup file. Ask the user directly:

> "One quick question — what are 2 to 4 mental models, frameworks, or thinkers that shape how you reason? Things like 'first principles', 'second-order effects', 'Taleb on fragility', 'Bezos's regret minimization', 'OODA loops', etc. Skip any that feel like name-dropping — only list ones you actually use."

If they don't have any in mind, leave the section with a placeholder comment and move on.

**Pointers** — Keep the full table from the template. Only remove rows for files that don't exist yet.

### Step 3 — Show the draft

Show the full `me.md` draft. Ask:

> "Here's the draft. It's meant to be tight — this gets loaded at the start of every AI session, so every line should earn its place. Anything to cut, expand, or change?"

Iterate until the user approves.

### Step 4 — Write the file

Write `me.md` at the repo root. Update `*Last updated:*` to today's date.

### Step 5 — Self-delete

After writing:
1. Delete the `Skills/setup-me/` folder entirely.
2. Confirm: "`me.md` is set up. Setup skill removed. [N] setup sections remaining."

If this was the last setup skill, say instead: "`me.md` is set up. All setup is complete — your vault is fully configured."

---

## Important Notes

- **Tight is the whole point.** If a section is bloated, cut it. Target: 50–80 lines of filled content, not 200. Every line should give an AI something actionable.
- **Don't invent.** If a source file is a template/placeholder, leave that section of `me.md` as a placeholder too. Do not make up values, frameworks, or priorities.
- **Current Focus is always a digest placeholder.** This skill never fills it. The first `digest` run after setup-me will populate it.
- **Pointers table is the escape hatch.** If an AI needs more than what `me.md` contains, it has clear pointers to the deeper files. Don't try to cram depth into `me.md`.

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
