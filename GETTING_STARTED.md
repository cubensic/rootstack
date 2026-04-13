# Getting Started with Rootstack

Rootstack is a portable, AI-readable personal context layer. It lives on your computer as a folder of markdown files, works with Claude Code out of the box, and opens in Obsidian for visual browsing and journaling.

Once set up, your AI always knows who you are, what you're working on, and how you think — across every session.

---

## What you need

- **Git** — to clone the repo
- **Python 3** — for the automation hooks (session harvesting, maintenance checks)
- **Claude Code** — for the full experience (hooks, auto-harvesting, scheduled maintenance)
- **Obsidian** *(optional but recommended)* — for browsing your vault visually and writing journal entries

---

## Setup (5 minutes)

### 1. Get the repo

Click **Use this template** on GitHub to create your own copy, then clone it:

```bash
git clone https://github.com/YOUR_USERNAME/rootstack.git
cd rootstack
```

Or clone this repo directly if you just want to try it:

```bash
git clone https://github.com/cubensic/rootstack.git
cd rootstack
```

### 2. Open in Claude Code

```bash
claude
```

Claude Code reads `CLAUDE.md` automatically. On the first session it will:
- Detect that the vault is unconfigured
- Explain what Rootstack is
- Ask your name and one sentence about what you're building
- Initialize your vault in under 2 minutes

That's your starting point. Everything else is optional and can happen whenever.

### 3. Open in Obsidian *(optional)*

Open Obsidian → **Open folder as vault** → select the `rootstack` folder.

This gives you a visual interface for browsing your files, writing journal entries, and seeing how everything connects. Obsidian's graph view shows the relationships between your KB pages over time.

**Journals plugin:** The vault is pre-configured for the **Journals** plugin by Sergii Kostyrko. To install: Settings → Community plugins → Browse → search "Journals" → Install → Enable. Once enabled, it automatically creates dated journal files in the right folders.

---

## What happens next

**Each session:** Claude Code automatically harvests your previous session transcripts and checks if any maintenance is due (digest, readme updater, KB lint).

**Setup conversations:** You have 5 optional setup conversations that fill in your profile — background, values, personality, writing style, and goals. Each one is a short chat that runs a framework-driven assessment and drafts a section of your vault. Say **"continue setup"** anytime to see what's remaining.

**Weekly:** The digest skill synthesizes your journals and sessions into `now.md` (current focus) and lessons learned. The style-analyzer updates your writing style guide if you've added new samples.

**Monthly:** The digest produces behavioral patterns from 30 days of data. The goal-review skill checks progress against your 1-year goals with evidence from actual behavior.

---

## Folder overview

```
About [You]/       ← Who you are: background, values, personality, goals, patterns
Journal/           ← Daily personal and work entries
Knowledge Base/    ← Three-layer KB: raw sources, wiki pages, index
Projects/          ← Active projects and businesses
Content/           ← Writing style, samples, platform strategy, schedule
Skills/            ← AI maintenance skills (digest, goal-review, kb-ingest, etc.)
```

---

## Using with other AI tools

**Codex / OpenAI tools:** The vault folder contains `AGENTS.md` which is auto-detected.

**Cursor or other tools:** Point your AI at `README.md` as the entry point.

Note: The automation hooks (session harvesting, maintenance scheduling) are Claude Code-specific. With other tools, you can still use all the skills manually — just trigger them by name.
