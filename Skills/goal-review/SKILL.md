# Skill: goal-review
*Monthly review of progress against your 1-year goals. Generates a review file and optionally updates goals.*

---

## When to Run

- Monthly (checked by maintenance-check.py — only activates after goals are set up)
- Manually: "Review my goals", "Monthly review", "How am I doing on my goals?"

---

## What This Skill Does

Walks through each goal in `About [You]/goals/1-year.md`, assesses progress using evidence from recent journals and sessions, and generates a monthly review file. Also surfaces misalignments between stated goals and actual behavior.

This is where the self-evolution loop proves its value — the system can show you what you've *actually* been working on vs. what you *said* you'd work on.

**Rule:** Always propose the review and ask for approval before writing.

---

## Step-by-Step Instructions

### Step 1 — Gather context

Read:
- `About [You]/goals/1-year.md` — the goals and key results
- `About [You]/now.md` — current state
- Recent journal entries from `Journal/Personal/` and `Journal/Work/` (last 30 days)
- Recent session summaries from `Knowledge Base/Sessions/` (last 30 days)
- The previous month's review (if any) from `About [You]/goals/reviews/`

### Step 2 — Assess each goal

For each goal in 1-year.md:

1. **Check key results** — which ones show progress based on journal/session evidence? Which ones have been neglected?
2. **Look for behavioral evidence** — did the user actually work on this goal? How much time/energy went toward it?
3. **Assess trajectory** — on track, behind, ahead, or stalled?
4. **Note surprises** — goals that progressed without conscious effort, or goals that got zero attention despite being "priorities"

### Step 3 — Surface misalignments

This is the most valuable part. Compare:
- **Stated priorities** (goals) vs. **actual behavior** (what journals and sessions show they spent time on)
- **What they said they'd focus on** (previous month's review) vs. **what actually happened**

Don't judge — just surface it clearly: "You listed X as a top goal, but your last 4 weeks of sessions were entirely focused on Y. That might be intentional — or it might mean your goals need updating."

### Step 4 — Ask the user

Walk through your findings conversationally. For each goal:
> "**[Goal Name]** — here's what I see: [evidence summary]. How does that feel — on track, behind, or has the goal itself changed?"

Then the bigger questions:
- "Is there anything you've been working on that *isn't* in your goals but probably should be?"
- "Any goals that feel dead — things you listed but don't actually care about anymore?"
- "What's your top priority for the next month?"

### Step 5 — Draft the review

Generate a monthly review file. Use the template structure but make it evidence-based:

**Filename:** `About [You]/goals/reviews/[Month] [Year].md`

```markdown
# [Month] [Year] — Monthly Review
*Date: [date]*

---

## Goal Progress

### [Goal Name]
**Status:** [On track / Behind / Ahead / Stalled / Revised]
**Key Results:**
- [ ] [KR1] — [progress note]
- [ ] [KR2] — [progress note]
**Evidence:** [What journals/sessions show about actual effort toward this goal]

### [Goal Name]
**Status:** [...]
**Key Results:**
- [...]
**Evidence:** [...]

---

## Wins
*What went well this month.*

- [Win — tied to specific goal where possible]
- [Win]

---

## What Didn't Work
- [Struggle or miss — with context]
- [...]

---

## Alignment Check
*How well did actual behavior match stated goals?*

[Honest assessment. What got attention? What got neglected? Any emerging priorities not yet captured in goals?]

---

## Key Lessons
- [Lesson from this month]
- [Lesson]

---

## Focus for Next Month
*Top 3 priorities going into next month.*

1. [Priority — tied to which goal it serves]
2. [Priority]
3. [Priority]

---

## State of Mind
[Brief honest snapshot — how are they feeling about their trajectory?]
```

### Step 6 — Propose goal updates (if needed)

If the review revealed:
- **Dead goals** — goals they no longer care about → propose removing or replacing
- **New priorities** — things they're working on that aren't in goals → propose adding
- **Shifted targets** — key results that need adjusting → propose updates

Draft the updates to `1-year.md` separately: "Based on this review, I'd suggest these changes to your goals: [changes]. Want me to update your goals file too?"

### Step 7 — Write on approval

Write the review file. If the user approved goal updates, also update `1-year.md`.

---

## Tips

- **The first review is the most valuable.** It's the first time the system compares stated goals to actual behavior. Expect surprises.
- **Don't guilt-trip.** Behind on a goal isn't failure — it's information. Maybe the goal needs revising, maybe it just wasn't the right month.
- **Let goals die gracefully.** If something doesn't matter anymore, removing it is better than carrying dead weight. Fewer, real goals beat a long list of aspirations.
- **Reviews compound.** The second review can reference the first. By month 3-4, patterns become clear: which goals get consistent attention, which get ignored, which are seasonal.
- **Connect to other documents.** If a review reveals a new pattern, suggest appending to `behavioral-patterns.md`. If a lesson emerges, suggest appending to `lessons-learned.md`. The review is a rich input for the whole vault.

---

*This is a permanent skill. It runs monthly and should not be deleted.*
