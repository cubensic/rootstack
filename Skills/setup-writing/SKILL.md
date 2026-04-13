# Setup Skill: Writing Style
*One-time skill. Fills in `Content/Style/writing-style.md` through analysis and conversation, then self-deletes.*

---

## Trigger

- "Set up my writing style"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Captures the user's writing voice by analyzing real samples first, then asking targeted questions. This is the most important file for AI-assisted content creation. Drafts `Content/Style/writing-style.md`.

---

## Before Starting

Tell the user:

> "This will take about **20 minutes**. I'll need you to paste 2–3 examples of your best writing — LinkedIn posts, emails, articles, tweets, anything that sounds like you. I'll analyze your voice first, then ask a few follow-up questions. Have those samples ready before we start. Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Read the template

Read `Content/Style/writing-style.md`. Note the section structure — you'll draft into this format.

### Step 2 — Ask for writing samples

Ask the user to paste 2–3 examples of their best writing. These can be LinkedIn posts, emails, articles, tweets, newsletter issues — anything that represents their real voice.

**Important:** Analyze the samples BEFORE asking questions. Extract:
- Sentence length and structure patterns
- Tone (formal/casual, energetic/measured, direct/nuanced)
- Vocabulary tendencies (simple vs. technical, jargon usage)
- How they open and close pieces
- Use of stories, data, humor, metaphor
- What they consistently do and don't do

Share your analysis with the user: "Here's what I see in your writing..." This gives them something to react to rather than describe from scratch.

### Step 3 — Ask targeted questions

Based on your analysis, ask:

- Does this analysis match how you see your own voice? Anything I'm missing or getting wrong?
- What do you never do in your writing? (e.g., never use emojis, never write clickbait, never hedge)
- Does your voice change by platform? (e.g., more casual on X, more structured on LinkedIn)
- Is there a writer or creator whose style you admire or want to move toward?

### Step 4 — Draft the file

Write `Content/Style/writing-style.md` using the template structure. Include specific examples from their samples to anchor each point. The platform adaptation table should reflect what they told you about voice shifts.

### Step 5 — Show and approve

Show the full draft. Ask: "How does this look? Ready to write it, or want changes?"

Only write the file after the user approves.

### Step 6 — Self-delete

After writing the approved file, delete this entire folder (`Skills/setup-writing/`).

Confirm: "Writing style is set up. This setup skill has been removed — [N] setup sections remaining."

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
