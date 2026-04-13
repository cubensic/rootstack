# Setup Skill: Personality
*One-time skill. Fills in `About [You]/personality.md` through a guided conversation, then self-deletes.*

---

## Trigger

- "Set up my personality"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Helps the user describe how they think, work, and communicate. Captures cognitive style, energy patterns, and preferences. Drafts `About [You]/personality.md` from their answers.

---

## Before Starting

Tell the user:

> "This will take about **10 minutes**. I'll ask you about how you think, what gives you energy, how you prefer to work and communicate. If you've taken any personality assessments (MBTI, Big Five, etc.), have those results handy. I'll draft your personality file from your answers. Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `About [You]/personality.md`. Note the section structure — you'll draft into this format.

### Step 2 — Have a conversation

Ask these questions one at a time. Build on their answers.

- How do you think through problems — big picture first, or details first? Do you think in systems, stories, lists, visuals?
- How do you prefer to work — long deep focus blocks, or short bursts? Do you work better alone or with others?
- What energizes you? What drains you?
- How do you prefer to communicate? How do you like to receive feedback?
- Have you taken any personality assessments (MBTI, Big Five, Enneagram, DISC, etc.)? If so, what were the results?

### Step 3 — Draft the file

Write `About [You]/personality.md` using the template structure. If they shared assessment results, include them in the formal assessments table. Keep the descriptions concrete and specific — "needs 2 hours of uninterrupted morning time" is better than "likes deep work."

### Step 4 — Show and approve

Show the full draft. Ask: "How does this look? Ready to write it, or want changes?"

Only write the file after the user approves.

### Step 5 — Self-delete

After writing the approved file, delete this entire folder (`Skills/setup-personality/`).

Confirm: "Personality is set up. This setup skill has been removed — [N] setup sections remaining."

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
