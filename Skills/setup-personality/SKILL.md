# Setup Skill: Personality
*One-time skill. Maps your personality using the Big Five framework through natural conversation, then drafts `About [You]/personality.md`. Self-deletes when complete.*

---

## Trigger

- "Set up my personality"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Guides the user through a conversational personality assessment grounded in the Big Five (OCEAN) model — the most validated personality framework in psychology. Instead of a questionnaire, it uses open-ended questions that naturally probe each trait, plus follow-ups based on responses.

The output combines a Big Five profile (where they sit on each dimension) with practical sections the AI uses daily (how they think, work, communicate).

---

## Before Starting

Tell the user:

> "This will take about **10–15 minutes**. I'll ask you questions about how you think, work, and handle different situations. Behind the scenes I'm mapping your personality against the Big Five model — but it'll feel like a conversation, not a test.
>
> Like everything in Rootstack, this evolves over time. The digest skill will refine your personality profile as it learns more about you from journals and sessions.
>
> Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `About [You]/personality.md`. Note the section structure — you'll draft into this format.

### Step 2 — The Big Five conversation

Ask these questions **one at a time**, with natural follow-ups. Each question targets one or two Big Five traits. Don't announce which trait you're probing — just have the conversation.

Pay attention to both **what they say** (direct content) and **how they say it** (linguistic patterns — hedging, certainty, detail level, emotional language, vocabulary complexity).

**Openness to Experience:**
> "What kinds of things grab your attention — even when they're completely unrelated to your work? What do you find yourself exploring just because it's interesting?"

Follow up: "When you're facing a problem, do you tend to reach for proven approaches or do you find yourself inventing new ones?"

**Conscientiousness:**
> "Walk me through how you approach a big project or goal. What does your process actually look like — from start to finish?"

Follow up: "When things get messy or chaotic around you — deadlines shifting, plans falling apart — how do you respond?"

**Extraversion:**
> "Think about your ideal day off with no obligations. What does it look like? And where do other people fit into that picture?"

Follow up: "In a group setting — a meeting, a dinner, a team — what role do you naturally fall into?"

**Agreeableness:**
> "When someone you're working with takes an approach you think is wrong, what do you typically do? Walk me through how that plays out."

Follow up: "Would people who know you well describe you as more of a peacemaker or more of a straight-shooter?"

**Neuroticism / Emotional Stability:**
> "When something goes wrong — a project fails, you get bad news, plans fall through — how do you typically process that? How long does it take you to bounce back?"

Follow up: "What kinds of situations create the most stress or anxiety for you?"

### Step 3 — Practical questions

After the Big Five probes, ask a few practical questions that map directly to the template's working sections:

- "How do you prefer to communicate? Written vs. verbal, direct vs. diplomatic, how do you like to receive feedback?"
- "What's your energy pattern like? Are you a morning person, a night owl? Do you work in long deep blocks or short bursts?"
- "What consistently energizes you? And what reliably drains you?"

### Step 4 — How to work with you

These questions fill the "How to Work With Me" section — instructions for AI and collaborators:

- "When you're working with an AI, what does good support look like? What should the AI do more of, or less of?"
- "How do you make decisions — fast and intuitive, or slow and deliberate? Does it depend on the stakes?"
- "What are your blind spots — things you know you tend to miss or avoid?"
- "What frustrates you? What should an AI never do when working with you?"
- "How do you like information delivered — bullet points, prose, short vs. detailed?"

### Step 5 — Existing assessment results

Ask: "Have you ever taken any formal personality assessments — MBTI, Big Five, Enneagram, DISC, StrengthsFinder, anything? If so, what were the results?"

If they have results, incorporate them. If the results align with your conversational assessment, note the consistency. If they conflict, gently explore why: "Interesting — your Big Five results say [X], but from our conversation it seems more like [Y]. Which feels more accurate to you now?"

### Step 6 — Draft the file

Write `About [You]/personality.md` using the template structure:

**Big Five Profile:** For each of the 5 traits, write where they fall (not as a number, but as a description — "high", "moderately high", "moderate", "moderately low", "low") with a one-line description of what that means for them specifically. Include facet-level detail where the conversation revealed it.

**How I Think / How I Work / How I Communicate:** Concrete, specific descriptions drawn from their actual answers. "Needs 2 hours of uninterrupted morning time" is better than "likes deep work."

**Energizers and Drains:** Specific, not generic.

**How to Work With Me:** Fill in from the Step 4 answers — support preferences, decision-making style, blind spots, frustrations, preferred output formats. These are the instructions AI agents use most frequently.

**Assessment Results:** Include any formal results they shared.

### Step 7 — Show and approve

Show the full draft. Ask: "How does this feel? Anything I'm getting wrong or missing?"

Only write the file after the user approves.

### Step 8 — Self-delete

After writing the approved file, delete this entire folder (`Skills/setup-personality/`).

Confirm: "Personality is set up. This setup skill has been removed — [N] setup sections remaining."

---

## Important Notes

- **Don't label the traits during conversation.** Never say "this next question is about conscientiousness." The assessment should feel like getting to know someone, not administering a test.
- **Trust behavioral evidence.** If someone says they're organized but describes a chaotic, improvised workflow — go with the behavior. Gently note the discrepancy: "You mentioned you value organization, but it sounds like your actual process is more intuitive and flexible — would you say that's accurate?"
- **Avoid pathologizing neuroticism.** Frame it as emotional sensitivity/resilience, not as a problem. High neuroticism isn't bad — it often comes with higher empathy and self-awareness.
- **The Big Five profile is descriptive, not prescriptive.** It maps where someone is, not where they should be. No trait is "better" at any level.
- **This document evolves.** The digest skill can suggest refinements to personality.md over time as patterns emerge from journals and sessions.

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
