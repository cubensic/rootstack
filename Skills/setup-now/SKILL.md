# Setup Skill: Now
*One-time skill. Fills in `About [You]/now.md` through a guided conversation, then self-deletes.*

---

## Trigger

- "Set up my now page"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Captures a snapshot of what the user is focused on right now — active projects, current challenges, and state of mind. Drafts `About [You]/now.md`. After setup, this file is maintained by the `digest` skill.

---

## Before Starting

Tell the user:

> "This will take about **10 minutes**. I'll ask you about what you're focused on right now — active projects, what's hard, how you're feeling about the work. This becomes your 'now page' that every AI session reads first. After this, the digest skill keeps it current from your journal entries. Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `About [You]/now.md`. Note the section structure — you'll draft into this format.

### Step 2 — Have a conversation

Ask these questions one at a time. Build on their answers.

- What are you most focused on right now? (1–3 things)
- What projects are actively in progress? What's the status of each?
- What's hard right now? What are you stuck on or struggling with?
- How are you feeling about the work overall? What's your energy and motivation like?
- Any open questions you're sitting with — things you haven't decided yet?

### Step 3 — Draft the file

Write `About [You]/now.md` using the template structure. This should reflect current reality, not aspirations. Be honest and specific — "struggling with outreach consistency" is more useful than "working on marketing."

### Step 4 — Show and approve

Show the full draft. Ask: "How does this look? Ready to write it, or want changes?"

Only write the file after the user approves.

### Step 5 — Self-delete

After writing the approved file, delete this entire folder (`Skills/setup-now/`).

Confirm: "Now page is set up. This setup skill has been removed — [N] setup sections remaining. Going forward, the digest skill will keep this file current from your journal entries."

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
