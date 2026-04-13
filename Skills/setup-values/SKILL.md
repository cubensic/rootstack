# Setup Skill: Values
*One-time skill. Fills in `About [You]/values.md` through a guided conversation, then self-deletes.*

---

## Trigger

- "Set up my values"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Helps the user articulate their core values — what drives their decisions, what they won't compromise on, and where their values conflict with each other. Drafts `About [You]/values.md` from their answers.

---

## Before Starting

Tell the user:

> "This will take about **10 minutes**. I'll ask you about the values that drive your decisions — what matters most, what you won't compromise on, and where your values sometimes pull in different directions. I'll draft your values file from your answers. Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `About [You]/values.md`. Note the section structure — you'll draft into this format.

### Step 2 — Have a conversation

Ask these questions one at a time. Build on their answers.

- What are the 3–5 things that matter most to you when making decisions? (These can be words or phrases — autonomy, honesty, impact, family, craft, etc.)
- For each value: why does this one matter? Can you give an example of when it shaped a decision?
- What are your non-negotiables — the things you won't compromise on no matter what?
- Do any of your values ever conflict with each other? (e.g., freedom vs. security, ambition vs. presence)

If they've taken a formal values assessment (Schwartz, VIA, etc.), ask about the results and include them.

### Step 3 — Draft the file

Write `About [You]/values.md` using the template structure. Rank values by dominance based on how the user talked about them. Include the tension/conflict section — this is the most useful part for AI decision support.

### Step 4 — Show and approve

Show the full draft. Ask: "How does this look? Ready to write it, or want changes?"

Only write the file after the user approves.

### Step 5 — Self-delete

After writing the approved file, delete this entire folder (`Skills/setup-values/`).

Confirm: "Values are set up. This setup skill has been removed — [N] setup sections remaining."

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
