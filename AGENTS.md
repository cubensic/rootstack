# Rootstack — Instructions for AI Agents (Codex / OpenAI tools)

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

Introduce yourself and start the setup. Do not wait for the user to ask. Just begin.

Say something like:

> "Welcome to Rootstack. I can see this vault hasn't been filled in yet — I'll guide you through it. We'll go one section at a time. I'll ask you questions, draft each file from your answers, and show it to you for approval before writing anything. Ready to start?"

Then follow these steps in order. Complete one step fully (with user approval) before moving to the next.

**Step 1 — Who are you?**
Ask for their name and one sentence about who they are and what they're building. Use this to:
- Replace `[Your Name]` in `README.md` with their actual name
- Fill in the one-sentence description in `README.md`
- Update `*Last updated:*` to today's date

**Step 2 — Background**
Read `About [You]/background.md` to see the template structure. Ask conversational questions:
- Where did you grow up / start out?
- How did you get to where you are now?
- What's the current chapter — what are you building or working on?

Draft the file, show it, get approval, write it.

**Step 3 — Values**
Read `About [You]/values.md`. Ask:
- What are the 3–5 things that matter most to you when making decisions?
- What are your non-negotiables?

Draft, show, approve, write.

**Step 4 — Personality**
Read `About [You]/personality.md`. Ask:
- How do you think and process problems?
- What energizes you? What drains you?
- How do you prefer to communicate?

Draft, show, approve, write.

**Step 5 — Writing voice**
Read `Content/Style/writing-style.md`. Ask them to paste 2–3 examples of their best writing. Analyze the voice, then ask follow-up questions. Draft, show, approve, write.

**Step 6 — Goals**
Read `About [You]/goals/1-year.md`. Ask what they're trying to achieve this year. Draft, show, approve, write.

**Step 7 — Now**
Read `About [You]/now.md`. Ask about current focus, active projects, and state of mind. Draft, show, approve, write.

**When setup is complete:**
Tell them the vault is ready and explain the two core maintenance skills:
- **digest** (`Skills/digest/SKILL.md`) — run monthly
- **readme-updater** (`Skills/readme-updater/SKILL.md`) — run weekly

Then ask what they want to work on.

---

## Normal Session (filled vault)

Read these files before responding to anything:

1. `README.md` — vault overview and navigation
2. `About [You]/now.md` — current focus and state of mind
3. `About [You]/operating-manual.md` — how to work with this person effectively

Then confirm you're ready and ask what they want to work on.

---

## Rules That Always Apply

- **Propose before writing.** Show the user any file you plan to modify. Get approval before writing.
- **Never delete existing content.** Patterns, lessons, and people entries are append-only.
- **Use the templates.** Follow the structure in each folder's README and template files.
- **Markdown only.** All user-facing content is `.md`.
- **Keep it honest.** Draft from what the user tells you, not from assumptions.
