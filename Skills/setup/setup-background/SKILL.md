# Setup Skill: Background
*One-time skill. Captures your origin story through a turning-points conversation, then drafts `About [You]/background.md`. Self-deletes when complete.*

---

## Trigger

- "Set up my background"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Guides the user through telling their story — not as a chronological resume, but through the pivotal moments that shaped who they are. Based on Narrative Identity Theory (Dan McAdams), which finds that identity is built from a handful of key episodes: breakthroughs, struggles, and turning points.

The output is a background document organized around identity threads and turning points — much more useful for AI context than a timeline.

**For best results:** This is a good first setup skill to run. The background you capture here gives context to every other section.

---

## Before Starting

Tell the user:

> "This will take about **10–15 minutes**. I'm going to ask you about the moments that shaped who you are — not a full biography, just the turning points, breakthroughs, and struggles that explain how you got here.
>
> You don't need to be comprehensive. This document grows over time — as you journal and work with AI, the system will notice details about your past and suggest adding them here. So just share what comes to mind naturally.
>
> Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `About [You]/background.md`. Note the section structure — you'll draft into this format.

### Step 2 — The turning points conversation

Ask these questions one at a time. Build on their answers — this should feel like a real conversation, not an interview.

**Start broad:**
> "Give me the 2-minute version: who are you and how did you get to where you are now?"

This gets the basic arc. Then go deeper:

**Turning points (the core):**
> "What are the 2–3 moments that actually changed your direction? The decisions or events where your path forked and you went one way instead of another."

Follow up on each one naturally. Ask *why* it mattered, not just *what* happened.

**Formative struggle:**
> "What's the hardest thing you've gone through that shaped how you think or work today?"

This often reveals values and operating principles that show up nowhere else.

**The thread:**
> "Looking at all of that — is there a recurring theme? Something that keeps showing up across these different chapters of your life?"

Many people haven't articulated this before. If they struggle, offer an observation based on what they've told you: "It sounds like [autonomy / building things / proving something / reinvention] keeps coming up — does that feel right?"

**Current chapter:**
> "So what's the chapter you're in right now? What are you building or working toward?"

### Step 3 — Draft the file

Write `About [You]/background.md` using the template structure:

1. **The Short Version** — 2–3 sentences. Who they are and what they're about. This is the "if you read nothing else" section.

2. **Turning Points** — the pivotal moments, in rough chronological order. Each one gets a brief description of what happened and *why it mattered*. Write these as narrative, not bullet points.

3. **Identity Threads** — the recurring themes across their story. These are the deep patterns that explain their motivations and choices. Usually 2–3 threads.

4. **Current Chapter** — where they are now and what they're building toward.

**Voice:** Keep it in their voice. This should read as a person telling their story, not a third-party biography. First person.

**Length:** Aim for 300–600 words total. Enough to be useful, short enough to read in 2 minutes.

### Step 4 — Show and approve

Show the full draft. Ask: "How does this feel? Anything missing, or anything you'd rather leave out?"

Only write the file after the user approves.

### Step 5 — Self-delete

After writing the approved file, delete this entire folder (`Skills/setup-background/`).

Confirm: "Background is set up. This setup skill has been removed — [N] setup sections remaining."

If the only remaining setup is `setup-me`, add: "You're one step from a fully configured vault — `setup-me` synthesizes everything into your always-loaded identity file at the root. Run it whenever you're ready."

---

## Important Notes

- **Low friction is the goal.** If someone gives short answers, work with what you get. A 200-word background is infinitely better than an empty file. The digest skill will suggest additions over time as it picks up details from journals and sessions.
- **Don't push for vulnerability.** The "formative struggle" question is optional. If someone deflects or keeps it surface-level, that's fine — move on.
- **First person, their voice.** Don't over-formalize. If they're casual, write casually. If they're precise, write precisely.
- **This document evolves.** The digest skill checks for identity-relevant material in journals and sessions and can suggest appending to background.md over time. Make this clear so users don't feel pressure to "get it right" on the first pass.

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
