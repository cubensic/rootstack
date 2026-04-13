# Setup Skill: Background
*One-time skill. Fills in `About [You]/background.md` through a guided conversation, then self-deletes.*

---

## Trigger

- "Set up my background"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Guides the user through telling their story — where they come from, how they got here, and what they're building now. Drafts `About [You]/background.md` from their answers.

**For best results:** This is a good first setup skill to run. The background you capture here gives context to every other section.

---

## Before Starting

Tell the user:

> "This will take about **15 minutes**. I'll ask you about your story — where you grew up, how you got to where you are now, and what you're building. I'll draft your background file from your answers and show it to you before writing anything. Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `About [You]/background.md`. Note the section structure — you'll draft into this format.

### Step 2 — Have a conversation

Ask these questions one at a time. Build on their answers — this should feel like a conversation, not a form.

- Where did you grow up? What was your early life like?
- How did you get into what you do now? What's the path that brought you here?
- What's the current chapter — what are you building or working on right now?
- Is there anything else about your story that matters for understanding who you are?

### Step 3 — Draft the file

Write `About [You]/background.md` using the template structure. Keep the user's voice — don't over-formalize. This should read as a narrative, not a resume.

### Step 4 — Show and approve

Show the full draft. Ask: "How does this look? Ready to write it, or want changes?"

Only write the file after the user approves.

### Step 5 — Self-delete

After writing the approved file, delete this entire folder (`Skills/setup-background/`).

Confirm: "Background is set up. This setup skill has been removed — [N] setup sections remaining."

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
