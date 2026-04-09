# Getting Started with Rootstack

Rootstack is a portable, AI-readable personal context layer. It lives on your computer as a folder of markdown files, opens in Obsidian, and works with any AI tool — Claude, Codex, Cursor, or others.

Once set up, your AI always knows who you are, what you're working on, and how you think — across every session and every tool.

---

## Setup (5 minutes)

### 1. Fork and clone this repo

Click **Use this template** on GitHub, then clone your fork to your computer.

```
git clone https://github.com/YOUR_USERNAME/rootstack.git
```

### 2. Open the folder in Obsidian

Open Obsidian → **Open folder as vault** → select the `rootstack` folder.

Obsidian will detect the included configuration and prompt you to install community plugins. Allow it.

### 3. Install the Journals plugin

The vault is pre-configured to use the **Journals** plugin by [Sergii Kostyrko](https://github.com/srg-kostyrko). It handles your daily journal entries and content schedule files automatically.

To install: **Settings → Community plugins → Browse** → search "Journals" → Install → Enable.

Once installed, the plugin is already configured for the Rootstack folder structure — no additional setup needed.

### 4. Connect your AI tool

**Claude Code:** Open the vault folder in Claude Code. It will read `CLAUDE.md` automatically.

**Codex / OpenAI tools:** Open the vault folder. It will read `AGENTS.md` automatically.

**Cursor:** Open the vault folder. Point your `.cursorrules` file at `README.md`.

**Any other tool:** Open the vault folder and point your AI at `README.md`.

### 5. Run the setup prompt

Open `Prompts/setup.md`. Copy the prompt inside and paste it into your AI tool.

The AI will guide you through filling in your vault — your background, values, goals, and writing style. It takes about 1–2 hours and you can stop and resume at any time.

---

## What gets tracked in git

By default, **your personal content is not committed** — only the vault structure, templates, and skills are pushed. This means you can fork the public template repo and use it privately without worrying about accidentally publishing your journals or personal notes.

If you want to back up your personal content, push to a **private** repo and uncomment the relevant sections in `.gitignore`.

---

## Folder overview

```
README.md              ← AI navigator (entry point for every AI session)
CLAUDE.md              ← Claude-specific stub
AGENTS.md              ← Codex/OpenAI stub
tools.md               ← Your tools and integrations

About [You]/           ← Who you are: background, values, goals, patterns
Journal/               ← Daily entries (Personal + Work), managed by Journals plugin
Knowledge Base/        ← Saved notes, articles, research
Projects/              ← Active projects and businesses
Content/               ← Writing style, platform strategy, content schedule
Prompts/               ← Reusable AI prompts
Skills/                ← Maintenance skills that keep the vault alive
```

Full documentation in `README.md`.
