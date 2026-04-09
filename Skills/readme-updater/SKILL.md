# Skill: readme-updater
*Keeps the root README.md accurate as the vault grows and changes.*

---

## When to Run

- Weekly (or after adding/removing major folders or files)
- Trigger phrases: "Update my README", "Refresh my README", "Sync my README"

---

## What This Skill Does

Scans the vault folder structure, compares it against the current README.md, and proposes an updated version that reflects reality. Preserves everything the user has written — only updates the structural navigation tables and file listings.

**Rule:** Always show the full proposed README and ask for approval before writing. Never silently overwrite.

---

## Step-by-Step Instructions

### Step 1 — Read the current README

Read `README.md` in full. Note:
- The vault owner's one-sentence description (`**[Name] in one sentence:**`)
- The current folder-by-folder tables and listings
- The "How to Find What You Need" section and any custom entries there
- The `*Last updated:*` date

These must all be preserved or updated — never deleted.

---

### Step 2 — Scan the vault structure

Scan the vault **2 levels deep**. For each folder, list:
- The folder name
- All `.md` files directly inside it (level 1)
- All subfolders and their `.md` files (level 2)

**Skip these entirely — do not include in the README:**
- `.git/`
- `.obsidian/`
- Any folder or file listed in `.gitignore` that is personal content (Journal entries, Projects subfolders, Content/Schedule files, etc.)
- `desktop.ini`, `.DS_Store`, `.gitkeep`, and other system files
- Template files named `(Template) *.md` — these exist but don't need individual README entries

**What to include:**
- All top-level folders
- README.md files in subfolders (these are navigable)
- Template files — mention the folder contains a template, but don't list each one individually
- Skills (each skill subfolder with its SKILL.md)
- Prompts (each .md file)

---

### Step 3 — Compare and identify changes

Compare the scanned structure against the current README. Flag:

**Additions** — folders or files that exist in the vault but are not mentioned in README
**Removals** — folders or files mentioned in README that no longer exist in the vault
**No change** — structure matches README (still update the date)

If there are no structural additions or removals, note that and still propose a version with the updated date.

---

### Step 4 — Draft the updated README

Write the full updated README.md. Follow these rules exactly:

**Preserve unchanged:**
- The `# Rootstack — [Name]'s Personal Context Layer` title
- The `*Last updated: [date]*` line — update it to today's date
- The vault owner's one-sentence description
- The "How to Find What You Need" section — preserve all existing entries; only add new ones if new major content areas were added
- The closing italicized note at the bottom

**Update as needed:**
- Folder-by-folder tables — add rows for new files, remove rows for deleted files
- Vault Structure at a Glance — update to reflect actual top-level folders
- Any folder that now has a README.md should be linked

**Do not:**
- Invent descriptions for files you haven't read — if a new file has no obvious description from its name, read the first few lines to understand it
- Remove or rewrite custom descriptions the user has written
- Add folders or files that don't exist
- Change the tone or structure of sections you're not updating

---

### Step 5 — Propose and get approval

Present the proposed README to the user using this structure:

```
## README Updater — [today's date]

**Changes detected:**
- Added: [list any new folders/files found]
- Removed: [list any entries that no longer exist]
- Updated: Last updated date

**Proposed README.md:**

[Full proposed README content]

---
Ready to write? Reply "yes" to apply, or tell me what to change.
```

If no structural changes were found (only date update), say so clearly:
```
No structural changes detected. Only the "Last updated" date will change.
```

---

### Step 6 — Write on approval

Once the user approves, overwrite `README.md` with the proposed content. No partial writes — replace the whole file.

Confirm after writing: "README.md updated."

---

## What a Good README Looks Like

The README has five sections in this order:

1. **Title + date** — `# Rootstack — [Name]'s Personal Context Layer` + `*Last updated: [date]*`
2. **What This Is** — one paragraph + the owner's one-sentence description
3. **Vault Structure at a Glance** — code block showing top-level folder tree
4. **Folder-by-Folder Guide** — one subsection per top-level folder, with a table of key files
5. **How to Find What You Need** — quick-reference index of common query patterns

The skill must not add, remove, or reorder these sections. It only updates the content within sections 3 and 4 to match the actual vault.
