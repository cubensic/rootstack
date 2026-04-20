# Skill: vault-map-updater
*Keeps `vault-map.md` accurate as the vault grows and changes. Always proposes before writing.*

---

## When to Run

- Weekly (checked by maintenance-check.py)
- After adding/removing/renaming top-level folders
- Trigger phrases: "Update my vault map", "Refresh vault-map", "Sync vault-map"

---

## What This Skill Does

Scans the vault folder structure, compares it against `vault-map.md`, and proposes an updated version that reflects reality. `vault-map.md` is **always loaded** into every AI session, so it must stay tight and accurate — bloat wastes every session's context budget.

**Rule:** Always show the full proposed map and ask for approval before writing. Never silently overwrite.

---

## Step-by-Step Instructions

### Step 1 — Read the current vault-map.md

Read `vault-map.md` in full. Note:
- The table structure for each top-level folder
- Any custom descriptions the user has written
- The `*Last updated:*` date (if present)

Preserve custom wording — only update structure.

---

### Step 2 — Scan the vault structure

Scan **2 levels deep** from the repo root. For each top-level folder, list:
- The folder name
- All `.md` files directly inside it (level 1)
- All subfolders and their `.md` files (level 2)

**Skip entirely:**
- `.git/`, `.obsidian/`, `.claude/`, `.rootstack/`
- System files: `desktop.ini`, `.DS_Store`, `.gitkeep`, `*.tmp`
- `(Template) *.md` files — mention the folder has templates, don't list each one
- Personal content folders that are gitignored (journals, project subfolders, content drafts) — list the folder but not the individual files

**Include:**
- All top-level folders at the repo root
- Root-level files: `me.md`, `README.md`, `vault-map.md`, `CLAUDE.md`, `AGENTS.md`, `GETTING_STARTED.md`
- Key level-1 subfolders and the `.md` files inside them when structurally important
- Skill folders (each under `Skills/` with a `SKILL.md`)

---

### Step 3 — Compare and identify changes

Compare the scanned structure against the current `vault-map.md`. Flag:

**Additions** — folders or structural files that exist in the vault but aren't in the map
**Removals** — map entries for folders/files that no longer exist
**No structural change** — map matches reality (still update the date)

If there are no additions or removals, propose only a date update.

---

### Step 4 — Draft the updated vault-map.md

Write the updated `vault-map.md`. Follow these rules:

**Preserve:**
- The opening comment block and title
- Section ordering: Root Files → `About [You]/` → `Content/` → `Journal/` → `Knowledge Base/` → `Projects/` → `Skills/` → File Conventions
- Any custom wording the user added in descriptions
- The closing maintenance note

**Update:**
- Tables: add rows for new files/folders, remove rows for deleted ones
- `*Last updated:*` — set to today's date

**Stay tight:**
- Target: under 120 lines total.
- One line per file/folder in tables. No paragraphs of explanation.
- If you need more than a line, the detail belongs in a dedicated file (the pointer itself is the value).

**Do not:**
- Invent descriptions for files you haven't read — read the first few lines of unfamiliar files to derive a one-line purpose
- Add folder-level README entries (those have been retired)
- Reorder sections or change the file's structure

---

### Step 5 — Propose and get approval

Present using this structure:

```
## Vault Map Updater — [today's date]

**Changes detected:**
- Added: [list new entries]
- Removed: [list deleted entries]
- Updated: Last updated date

**Proposed vault-map.md:**

[Full proposed content]

---
Ready to write? Reply "yes" to apply, or tell me what to change.
```

If no structural changes:
```
No structural changes detected. Only the "Last updated" date will change.
```

---

### Step 6 — Write on approval

Overwrite `vault-map.md` with the proposed content. Confirm: "vault-map.md updated."

---

## Guardrails

- **Length budget.** If the map exceeds ~120 lines, flag it to the user and propose what to prune. `vault-map.md` loads every session — bloat is expensive.
- **Don't touch `README.md`.** That's the GitHub-facing doc, maintained manually. This skill only touches `vault-map.md`.
- **Don't duplicate `Skills/index.md`.** The map mentions `Skills/` briefly and points to the index — it doesn't re-list every skill.
