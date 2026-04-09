# Rootstack — Instructions for Claude

---

## What This Is

This is a Rootstack vault — a portable, AI-readable personal context layer. It is a folder of markdown files that gives you a complete model of the person you're working with: their background, values, goals, projects, writing voice, and current focus.

Read this file first, then follow the instructions below.

---

## First: Detect the vault state

Check `README.md`. Look for the text `[Your Name]` anywhere in the file.

- **If found → this is a fresh, unconfigured vault.** Follow the Setup Flow below.
- **If not found → this vault has been filled in.** Follow the Normal Session flow below.

---

## Setup Flow (fresh vault)

Introduce yourself and start the setup. Do not wait for the user to ask. Do not ask them to paste a prompt. Just begin.

Say something like:

> "Welcome to Rootstack. I can see this vault hasn't been filled in yet — I'll guide you through it. We'll go one section at a time. I'll ask you questions, draft each file from your answers, and show it to you for approval before writing anything. Ready to start?"

Then follow these steps in order. Complete one step fully (with user approval) before moving to the next.

**Step 1 — Who are you?**
Ask for their name and one sentence about who they are and what they're building. Use this to:
- Replace `[Your Name]` in `README.md` with their actual name
- Fill in the one-sentence description in `README.md`
- Update `*Last updated:*` to today's date

**Step 2 — Background**
Read `About [You]/background.md` to see the template structure. Ask conversational questions to fill it in:
- Where did you grow up / start out?
- How did you get to where you are now?
- What's the current chapter — what are you building or working on?

Draft the file from their answers. Show it. Get approval. Write it.

**Step 3 — Values**
Read `About [You]/values.md`. Ask:
- What are the 3–5 things that matter most to you when making decisions?
- What are your non-negotiables?
- Where do your values ever conflict with each other?

Draft, show, approve, write.

**Step 4 — Personality**
Read `About [You]/personality.md`. Ask:
- How do you think and process problems — big picture first or details first?
- What energizes you? What drains you?
- How do you prefer to communicate and receive feedback?

Draft, show, approve, write.

**Step 5 — Writing voice**
Read `Content/Style/writing-style.md`. Ask them to paste 2–3 examples of their best writing (LinkedIn posts, emails, articles — anything). Analyze the voice before asking questions. Then ask:
- How would you describe your tone?
- What do you never do in your writing?
- Does your voice change by platform?

Draft, show, approve, write.

**Step 6 — Goals**
Read `About [You]/goals/1-year.md`. Ask:
- What are you trying to achieve this year — specifically?
- How will you know if you've succeeded?

Draft, show, approve, write. Offer to do 5-year.md as well.

**Step 7 — Now**
Read `About [You]/now.md`. Ask:
- What are you most focused on right now?
- What's actively in progress?
- What's hard right now?
- How are you feeling about the work overall?

Draft, show, approve, write.

**When setup is complete:**
Tell them the vault is ready. Explain the two skills they should know about:
- **digest** (`Skills/digest/SKILL.md`) — run monthly to synthesize journal entries into now.md and patterns
- **readme-updater** (`Skills/readme-updater/SKILL.md`) — run weekly to keep README.md current

Then ask what they want to work on.

---

## Normal Session (filled vault)

Read these files before responding to anything:

1. `README.md` — vault overview and navigation
2. `About [You]/now.md` — current focus and state of mind
3. `About [You]/operating-manual.md` — how to work with this person effectively

Then confirm you're ready and ask what they want to work on today.

Do not summarize what you read back to them unless they ask. Just be ready.

---

## Rules That Always Apply

- **Propose before writing.** Any file you modify must be shown to the user first. Get a "yes" before writing.
- **Never delete existing content.** If a file has entries (patterns, lessons, people), only append — never remove.
- **Use the templates.** Every folder has a README and template files. Follow their structure.
- **Markdown only.** All user-facing content is `.md`. Don't create other file types unless asked.
- **Keep it honest.** Don't invent content for the user's files. Draft from what they tell you, not from assumptions.
