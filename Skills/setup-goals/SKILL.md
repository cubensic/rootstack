# Setup Skill: Goals
*One-time skill. Fills in all three goal files (10-year, 5-year, 1-year) through a top-down conversation, then self-deletes.*

---

## Trigger

- "Set up my goals"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Guides the user through defining their goals top-down: long-range direction → medium-range vision → this year's specific targets. Most people set goals bottom-up (tasks first), which produces disconnected targets. Starting from purpose and working down makes goals coherent and meaningful.

Fills in three files:
- `About [You]/goals/10-year.md` — direction and purpose
- `About [You]/goals/5-year.md` — concrete vision
- `About [You]/goals/1-year.md` — specific, measurable targets with key results

---

## Before Starting

Tell the user:

> "This will take about **15–20 minutes**. We're going to work top-down — starting from the big picture (where you're heading long-term) and zooming in to this year's specific goals.
>
> Most people set goals from the bottom up — tasks and targets without a clear 'why.' We'll do it the other way around: direction first, then vision, then targets. That way your yearly goals actually connect to something meaningful.
>
> You don't need to have it all figured out. Uncertainty is fine — we'll capture what you know and what you're still figuring out. This document evolves over time as the system learns from your journals and sessions.
>
> Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read templates and context

Read:
- `About [You]/goals/10-year.md` — note the structure
- `About [You]/goals/5-year.md` — note the structure
- `About [You]/goals/1-year.md` — note the structure
- `About [You]/values.md` — if it exists, read it for context. Goals should align with values.
- `About [You]/background.md` — if it exists, check the Identity Threads and Current Chapter. Goals often extend these threads.

### Step 2 — 10-year direction (the long view)

Start here. Keep it light — 2-3 minutes. This isn't about specifics, it's about direction and identity.

> "Let's start big. Forget about what's realistic for a moment. Ten years from now — who do you want to be? Not what job title or how much money, but what kind of person, what kind of life, what kind of impact?"

Follow up based on their response:
- "What do you want to be known for?"
- "What would you want to have contributed — to your field, your community, the world?"

If they struggle with 10 years: "Okay, think of it as a compass direction, not a destination. Even 'I want to be free to work on whatever interests me' is a direction."

**Don't push for precision here.** A few sentences about direction and purpose is enough.

### Step 3 — 5-year vision (the concrete picture)

Now zoom in. This should feel more tangible.

> "Okay, now let's make it more concrete. Five years from now — what does your life and work actually look like? Walk me through a normal week."

Probe specific areas:
- "What are you working on? What does your professional life look like?"
- "Where are you living? What does your day-to-day lifestyle look like?"
- "What's your financial situation? Not exact numbers necessarily, but what does freedom look like at that point?"
- "What have you gotten better at? What have you figured out that you haven't yet?"

Then the bridge question:
> "What has to be true in the next 1-2 years to make this 5-year picture possible? What are the bridge steps?"

### Step 4 — 1-year goals (specific targets)

Now derive this year's goals from the vision.

> "Alright, let's zoom into this year. Given where you want to be in 5 years, what are the most important things to accomplish in the next 12 months?"

For each goal they mention, push for specificity:
- "How will you know you've hit this? What's the measurable outcome?"
- "What are the key results — the 2-3 things that would have to be true for this goal to be done?"
- "What does progress look like before you hit the goal? What's the leading indicator?"

Cover multiple areas — but don't force categories. Ask:
> "Those are your work goals. Is there anything on the personal side — health, relationships, learning, lifestyle — that matters this year?"

Then constraints:
> "What are you protecting this year? Any boundaries or non-negotiables — things you won't sacrifice for the goals?"

If values.md exists, check alignment:
> "Looking at your values, [top value] and [second value] come up strongest. Do these goals feel aligned with those? Is there anything you value highly that none of these goals serve?"

### Step 5 — Draft all three files

Draft all three goal files:

**10-year.md** — Keep it short. North star, impact, identity. 100-200 words max. This should feel like a compass, not a plan.

**5-year.md** — More concrete. Vision, work/business, lifestyle, financial, personal growth, plus the bridge steps that connect to 1-year goals. 200-400 words.

**1-year.md** — The most detailed. Structure each goal as:
```
### [Goal Name]
**Target:** [Specific, measurable outcome]
**Key Results:**
- [ ] [Measurable result 1]
- [ ] [Measurable result 2]
- [ ] [Measurable result 3]
**Leading indicator:** [What progress looks like week to week]
```

Include the Headline ("If this year goes well, what is true by December 31st?"), constraints, and leading indicators.

### Step 6 — Show and approve

Show all three drafts together. Ask: "Here's the full picture — 10-year direction, 5-year vision, and this year's targets. How does this feel? Anything off or missing?"

Only write after approval. The user can approve all three or pick which ones to write.

### Step 7 — Self-delete

After writing the approved files, delete this entire folder (`Skills/setup-goals/`).

Confirm: "Goals are set up. This setup skill has been removed — [N] setup sections remaining."

---

## Important Notes

- **Top-down is the key insight.** If the user wants to jump straight to 1-year goals, let them — but then work backwards: "Great, those are your targets. Now let me ask — what's the bigger picture these are serving? Where are you heading in 5-10 years?" The hierarchy should exist even if you build it out of order.
- **Uncertainty is valid.** If someone says "I have no idea where I'll be in 10 years," that's honest and useful. Write it: "Direction not yet clear — exploring." The digest skill will surface themes from their actual behavior over time.
- **Goals should be theirs, not yours.** Don't suggest goals. Don't push them to be more ambitious or more modest. Reflect what they actually want, even if it seems small or unrealistic.
- **The self-evolution angle.** The digest skill reads 1-year.md when synthesizing now.md, and can surface gaps between stated goals and actual behavior: "You say growing revenue is a priority, but your last 3 weeks of sessions were all about product features." This is where Rootstack adds real value over a static goal doc.
- **Monthly reviews.** A review template exists at `About [You]/goals/reviews/(Template) Monthly Review.md`. Mention it: "There's a monthly review template in your goals folder. Using it once a month keeps your goals alive instead of forgotten."

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
