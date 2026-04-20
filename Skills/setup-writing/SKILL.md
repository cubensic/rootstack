# Setup Skill: Writing Style
*One-time skill. Helps you populate your writing samples and generates your first style guide, then self-deletes.*

---

## Trigger

- "Set up my writing style"
- "Continue setup" (when this is the next available setup skill)

---

## What This Skill Does

Gets the user's writing samples into `Content/Style/Samples/`, then runs the style-analyzer skill to generate the first version of `Content/Style/writing-style.md`.

After setup, the style-analyzer skill runs weekly and picks up new samples automatically — so the style guide evolves over time as the user adds more writing.

---

## Before Starting

Tell the user:

> "This will take about **10–20 minutes** depending on how many samples you have ready.
>
> I need **5–10 pieces of your best writing** — the stuff that sounds most like you. LinkedIn posts, newsletter issues, articles, tweets, emails — anything you're proud of.
>
> You can either:
> 1. **Paste them here** and I'll save each one as a file in `Content/Style/Samples/`
> 2. **Drop them directly** into `Content/Style/Samples/` as .md files (if you already have them as files)
>
> The more samples, the better the style guide. But even 3–4 is enough to start — you can always add more later and the system will update your style guide automatically.
>
> Ready?"

Wait for confirmation before proceeding.

---

## Steps

### Step 1 — Collect samples

If the user pastes writing samples in chat:
- Save each one to `Content/Style/Samples/` as a separate `.md` file
- Use a descriptive filename: `[platform or type] - [brief topic].md` (e.g., `LinkedIn - why I left my job.md`, `Newsletter - building in public.md`)
- Include a brief metadata line at the top of each file:
  ```
  *Source: [platform/context] | Date: [if known]*
  ```
- Confirm each one saved: "Got it — saved as `[filename]`"

If they've already dropped files in the folder:
- Read the folder and confirm what's there: "I see [N] samples in your folder: [list]. Ready to analyze?"

If they have fewer than 3 samples, mention it:
> "3 samples is enough to start, but the style guide will be more accurate with 5–10. You can always add more later — the system re-analyzes weekly."

### Step 2 — Run style-analyzer

Once samples are collected, run the style-analyzer skill (`Skills/style-analyzer/SKILL.md`) — follow its instructions from Step 3 onward (skip Steps 1–2 since we just verified the samples).

This generates the first version of `Content/Style/writing-style.md`.

### Step 3 — Ask targeted follow-up questions

After showing the generated style guide, ask:

- "Does this capture your voice? Anything feel off or missing?"
- "Is there anything you *never* want AI to do when writing as you — pet peeves, words you hate, patterns that feel wrong?"
- "Does your voice shift by platform, or is it pretty consistent everywhere?"

Incorporate their feedback into the style guide before final approval.

### Step 4 — Show and approve

Show the final draft. Get approval before writing.

### Step 5 — Write and confirm

Write the approved `Content/Style/writing-style.md`.

Tell the user:
> "Your writing style guide is set up. From now on, any AI that reads this file can write in your voice.
>
> To keep it accurate: **drop new writing samples into `Content/Style/Samples/` whenever you write something you're proud of.** The style-analyzer runs weekly and will update your style guide automatically."

### Step 6 — Self-delete

Delete this entire folder (`Skills/setup-writing/`).

Confirm: "Writing style is set up. This setup skill has been removed — [N] setup sections remaining."

If the only remaining setup is `setup-me`, add: "You're one step from a fully configured vault — `setup-me` synthesizes everything into your always-loaded identity file at the root. Run it whenever you're ready."

---

## Important Notes

- **The setup skill is one-time. The style-analyzer is permanent.** This skill gets the user started and then deletes itself. The ongoing maintenance is handled by `Skills/style-analyzer/` which runs weekly.
- **Don't over-analyze thin data.** With only 3–4 samples, keep the style guide modest. Flag uncertainty: "Based on limited samples — will sharpen as you add more."
- **Samples stay forever.** The `Content/Style/Samples/` folder is the source of truth. The style guide is always re-derivable from the samples.

---

*This is a one-time setup skill. Once deleted, it should not be recreated.*
