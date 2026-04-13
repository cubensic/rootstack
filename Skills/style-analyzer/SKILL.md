# Skill: style-analyzer
*Reads writing samples and generates a comprehensive writing style guide.*

---

## When to Run

- Weekly (checked by maintenance-check.py)
- Manually: "Update my writing style", "Analyze my writing", "Regenerate my style guide"
- After setup-writing completes (first run)

---

## What This Skill Does

Reads all writing samples in `Content/Style/Samples/`, analyzes them for patterns, and generates (or regenerates) `Content/Style/writing-style.md` — a single comprehensive style guide that any AI can use to write in the user's voice.

On subsequent runs, it checks if new samples have been added since the last analysis. If the samples haven't changed, it skips the regeneration.

**Rule:** Always propose the style guide and ask for approval before writing.

---

## Step-by-Step Instructions

### Step 1 — Check for samples

Read all `.md` files in `Content/Style/Samples/` (excluding README.md).

If no samples exist, tell the user:
> "No writing samples found in `Content/Style/Samples/`. Drop 5–10 pieces of your best writing there (as .md files) and run this again. See the README in that folder for guidance."

Exit the skill.

### Step 2 — Check if update is needed

Read the current `Content/Style/writing-style.md`. Check the `*Last analyzed:*` date and the `*Samples analyzed:*` count.

Compare against the actual samples in the folder. If the count matches and no files have been modified since the last analysis date, tell the user: "Style guide is up to date — no new samples detected." and exit.

If this is the first run or samples have changed, continue.

### Step 3 — Analyze all samples

Read every sample file. For each one, extract:

**Sentence structure:**
- Average sentence length (short/medium/long)
- Sentence length variation (monotone vs. deliberately varied)
- Use of fragments for emphasis
- Paragraph length patterns

**Tone and register:**
- Formality level (casual, conversational, professional, academic)
- Energy (calm, intense, measured, enthusiastic)
- Confidence level (assertive, hedging, exploratory)
- Humor usage (none, dry, frequent, self-deprecating)
- Emotional register (detached, warm, vulnerable, matter-of-fact)

**Vocabulary:**
- Simple vs. complex word preference
- Jargon and technical language usage
- Distinctive words or phrases that recur
- Cliches or filler they avoid

**Structure and rhythm:**
- How they open pieces (story, observation, question, statement, provocation)
- How they close pieces (takeaway, question, call to action, trailing thought)
- Transition patterns between ideas
- Use of lists, headers, whitespace
- Paragraph-level rhythm (short-long patterns, builds, punchlines)

**Rhetorical patterns:**
- Teaching through experience vs. theory
- Use of stories and anecdotes
- Use of data and evidence
- Use of metaphor and analogy
- Direct address to reader
- First person vs. third person vs. second person

**What they consistently DON'T do:**
- This is as important as what they do. Look for patterns of absence — things that never appear across multiple samples.

### Step 4 — Synthesize into style guide

Draft `Content/Style/writing-style.md` as a single comprehensive document. Structure:

```markdown
# Writing Style
*AI-generated style guide based on [N] writing samples.*
*Read this before writing any content for this person.*
*Last analyzed: [date]*
*Samples analyzed: [N]*

---

## Voice in One Sentence
[One sentence that captures the overall voice — written as if describing to someone who's never read their work]

---

## Tone
- **Formality:** [with specific evidence from samples]
- **Energy:** [with evidence]
- **Confidence:** [with evidence]
- **Humor:** [with evidence]
- **Emotional register:** [with evidence]

---

## Sentence Patterns
[Specific observations about sentence structure, length, variation, use of fragments. Include real examples from their samples.]

---

## What You Always Do
[Patterns that appear consistently across samples. Each point should cite a real example.]

- [Pattern] — e.g., "Opens with a concrete observation, never a rhetorical question"
- [Pattern] — e.g., "Uses single-sentence paragraphs for emphasis after a longer paragraph"
- [...]

---

## What You Never Do
[Patterns of absence. Things that never appear.]

- [Anti-pattern] — e.g., "Never uses motivational language ('crush it', 'level up', 'game-changing')"
- [Anti-pattern] — e.g., "Never hedges with 'I think' or 'in my opinion' — states things directly"
- [...]

---

## Vocabulary
[Distinctive word choices, preferred terms, technical language usage, words they avoid]

---

## Structure
[How they build pieces — openings, closings, transitions, paragraph rhythm. Include examples.]

---

## Signature Moves
[2–3 distinctive things that make their writing recognizably theirs. The things a reader would notice.]

---

## Example Excerpts
[3–4 short excerpts from their samples that best represent their voice. These serve as calibration anchors for AI generation.]

> [Excerpt 1 — with brief note on what it demonstrates]

> [Excerpt 2]

> [Excerpt 3]
```

### Step 5 — Propose and approve

Show the full draft. Ask: "Here's your updated style guide based on [N] samples. How does this look? Anything I'm getting wrong about your voice?"

Only write after approval.

### Step 6 — Write

Write `Content/Style/writing-style.md`. Overwrite the entire file — this is a regenerated document, not an append.

---

## Tips

- **More samples = better accuracy.** 5 samples give a rough sketch. 10+ give a reliable profile. Tell the user if their sample count is low: "This is based on [N] samples — the style guide will get more accurate as you add more."
- **Conflicting styles across samples** are fine. If someone writes differently for LinkedIn vs. newsletters, note it: "Your tone shifts from [X] in shorter pieces to [Y] in long-form." This is valuable information.
- **Don't invent patterns.** If something only appears once, it's not a pattern. Only include observations supported by multiple samples.
- **The "What You Never Do" section is crucial.** AI models default to generic patterns. Knowing what to *avoid* is often more useful than knowing what to do.

---

*This is a permanent skill. It runs on a schedule and should not be deleted.*
