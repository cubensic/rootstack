# Setup Skill: Goals
*One-time skill. Fills in `About [You]/goals/1-year.md` through a guided conversation, then self-deletes.*

---

## Trigger

- "Set up my goals"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Helps the user define specific, measurable targets for the current year. Drafts `About [You]/goals/1-year.md` from their answers. Optionally does `5-year.md` as well.

---

## Before Starting

Tell the user:

> "This will take about **10 minutes**. I'll ask you about what you're trying to achieve this year — work, personal, health, learning. We'll make them specific and measurable so you can actually track progress. Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `About [You]/goals/1-year.md`. Note the section structure — you'll draft into this format.

### Step 2 — Have a conversation

Ask these questions one at a time. Build on their answers.

- What are you trying to achieve this year? Be as specific as you can — numbers, milestones, outcomes.
- Break it down: what are your goals for work/business? Personal growth? Health? Relationships? Learning?
- For each major goal: how will you know if you're on track? What are the leading indicators?
- Are there any constraints or boundaries you're setting? (e.g., "no more than X hours/week", "not taking on clients", etc.)

### Step 3 — Draft the file

Write `About [You]/goals/1-year.md` using the template structure. Goals should be specific and measurable — "grow revenue to $X/month" not "grow the business." Include leading indicators for each goal.

### Step 4 — Show and approve

Show the full draft. Ask: "How does this look? Ready to write it, or want changes?"

Only write the file after the user approves.

### Step 5 — Offer 5-year goals

Ask: "Want to also do your 5-year vision while we're here? It's optional — we can skip it."

If yes, read `About [You]/goals/5-year.md`, ask about their medium-range vision (work, lifestyle, financial, personal growth), draft, show, approve, write.

### Step 6 — Self-delete

After writing the approved file(s), delete this entire folder (`Skills/setup-goals/`).

Confirm: "Goals are set up. This setup skill has been removed — [N] setup sections remaining."

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
