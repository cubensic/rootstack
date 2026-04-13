# Setup Skill: Values
*One-time skill. Maps your values using the Schwartz framework, then drafts `About [You]/values.md`. Self-deletes when complete.*

---

## Trigger

- "Set up my values"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Guides the user through a conversational values assessment based on the Schwartz Theory of Basic Human Values — the most validated cross-cultural values framework in psychology. Instead of asking "what do you value?", it uses portrait-based scenarios (adapted from the Portrait Values Questionnaire) to surface genuine priorities.

The output is a structured values profile showing their value hierarchy, where they sit on two fundamental dimensions, their natural value tensions, and their non-negotiables.

---

## Before Starting

Tell the user:

> "This will take about **10–15 minutes**. Instead of asking you to list your values (which tends to produce generic answers), I'm going to walk you through a series of scenarios based on the Schwartz values framework — the most validated values model in psychology.
>
> I'll describe different people and you tell me how much each one sounds like you. From your responses, I'll map your actual value hierarchy and the tensions between your values — which is the most useful part for decision-making.
>
> Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `About [You]/values.md`. Note the section structure — you'll draft into this format.

### Step 2 — Portrait scenarios (the core assessment)

Present these scenarios **one at a time** or in small groups of 2–3. For each, ask: *"How much does this sound like you? A lot, somewhat, a little, or not at all?"*

Adapt the language to feel natural in conversation — these are starting points, not scripts to read verbatim. Use "they" or match the user's apparent gender. The key is that each portrait targets a specific Schwartz value.

**The 10 portraits (one per value type):**

1. **Self-Direction** — "This person thinks it's important to come up with their own ideas and figure things out for themselves. They like to be free to plan their own path rather than follow someone else's."

2. **Stimulation** — "This person is always looking for new experiences. They want a life full of challenge and novelty — routine bores them."

3. **Hedonism** — "This person prioritizes enjoying life. Having a good time and treating themselves well is important to them."

4. **Achievement** — "This person wants to be really good at what they do. Showing their competence and being recognized for their abilities matters a lot to them."

5. **Power** — "This person wants to be in charge and have influence. Being a leader, making decisions that affect others, and having resources at their disposal is important to them."

6. **Security** — "This person values safety and stability above most things. They avoid unnecessary risks and want their environment to be predictable and secure."

7. **Conformity** — "This person believes in following rules and meeting expectations. They try not to do anything that would upset others or go against social norms."

8. **Tradition** — "This person thinks it's important to follow the customs and practices they were raised with. Respecting tradition and maintaining continuity matters to them."

9. **Benevolence** — "This person goes out of their way to help the people close to them. Being loyal, dependable, and caring for their inner circle is central to who they are."

10. **Universalism** — "This person cares deeply about fairness and the welfare of all people — not just their own group. They want equality, justice, and to protect the world around them."

**After each response**, briefly acknowledge and move to the next. Don't analyze yet — just note their self-ratings mentally.

### Step 3 — Follow-up on strong responses

For the 3–4 values where the user said "a lot" or gave a strong reaction, ask one follow-up each:

- "Can you give me an example of when [this value] actually shaped a decision you made?"
- "What does [this value] look like in your daily life — not in theory, but in practice?"

This grounds abstract values in real behavior and gives you material for the "what this means in practice" descriptions.

### Step 4 — Explore the two dimensions

Now explicitly explore where they sit on Schwartz's two fundamental dimensions. Frame it as tensions:

**Dimension 1: Self-Enhancement vs. Self-Transcendence**
> "Here's a tension most people feel: On one side, there's ambition — wanting personal success, influence, and recognition. On the other side, there's service — wanting to help others, promote fairness, and contribute beyond yourself. Most people lean one way. Where do you fall? And has this changed over time?"

**Dimension 2: Openness to Change vs. Conservation**
> "Another one: On one side, there's independence and novelty — wanting to explore, take risks, and do things your own way. On the other side, there's stability and order — wanting predictability, respecting tradition, and keeping things running smoothly. Where do you land?"

Let them talk. These two questions often produce the richest material.

### Step 5 — Non-negotiables and real tensions

Ask:
- "What's something you absolutely will not compromise on, even when it costs you?"
- "When have your values actually conflicted with each other? Like, two things you care about pulled you in opposite directions — and you had to choose?"

If they can't think of a conflict, suggest one based on their portrait responses. The Schwartz circle predicts which values conflict:
- Self-Direction vs. Conformity/Tradition
- Stimulation vs. Security
- Achievement/Power vs. Benevolence/Universalism
- Hedonism vs. Conformity

### Step 6 — Draft the file

Using everything from the conversation, draft `About [You]/values.md` following the template structure:

1. **Value Hierarchy** — rank their values from the portrait responses + follow-ups. Use all 10 Schwartz values, grouped into tiers (dominant, important, moderate, low priority). For the top values, include a "what this means in practice" line drawn from their actual examples.

2. **The Two Dimensions** — map where they sit on both axes. Use their own words where possible.

3. **Values in Tension** — identify 2–3 real tensions. These should come from:
   - What they explicitly described as conflicts
   - What the Schwartz circle predicts based on their high-priority values (adjacent values are compatible, opposite values conflict)

4. **Non-Negotiables** — their stated hard lines.

5. **Framework Note** — brief note that this was derived from the Schwartz framework, with the date.

### Step 7 — Show and approve

Show the full draft. Ask: "How does this look? Anything feel off or missing?"

Only write the file after the user approves.

### Step 8 — Self-delete

After writing the approved file, delete this entire folder (`Skills/setup-values/`).

Confirm: "Values are set up. This setup skill has been removed — [N] setup sections remaining."

---

## Important Notes

- **Don't lecture about the framework.** The user doesn't need to know the academic details. Use the framework to structure the conversation, not to teach psychology.
- **Adapt the portraits.** If the user is clearly a technical founder, adjust the scenarios to be relevant (e.g., "This person wants to build something that works elegantly" for Achievement). The Schwartz values are universal — the examples should be contextual.
- **Trust behavioral evidence over self-report.** If someone says they don't care about Achievement but describes spending every weekend shipping side projects, note the discrepancy gently: "Interesting — from what you described, it sounds like competence and output actually matter quite a bit to you, even if you wouldn't call it 'achievement.' Fair?"
- **The tensions section is the most valuable part.** For AI decision support, knowing that someone values both Freedom and Security (and which one wins) is more useful than knowing they value Freedom alone.

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
