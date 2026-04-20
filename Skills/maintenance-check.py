"""
Maintenance Check — Run at session start to detect overdue vault maintenance.

Checks timestamps in .rootstack/ to determine if any maintenance skills
are due. Outputs JSON that Claude Code reads via the SessionStart hook.

If maintenance is due, returns additionalContext telling Claude what to run.
If nothing is due, returns silently.

Maintenance schedule:
- Session harvest: every session (always run)
- Digest: every 7 days
- Vault-map updater: every 7 days
- Style analyzer: every 7 days (only if samples exist)
- KB lint: every 14 days
- Goal review: every 30 days (only after setup-goals completes)
- Setup-me: checked only after all other setup-* skills complete
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path


def find_vault_root():
    """Find the vault root from cwd or script location."""
    # Try cwd first (Claude Code runs from project root)
    cwd = Path.cwd()
    if (cwd / "README.md").exists() and (cwd / "CLAUDE.md").exists():
        return cwd
    # Fall back to script location
    script_dir = Path(__file__).resolve().parent
    vault_root = script_dir.parent  # Skills/ -> vault root
    if (vault_root / "README.md").exists():
        return vault_root
    return None


def get_state_dir(vault_root):
    """Get or create the .rootstack/ state directory."""
    state_dir = vault_root / ".rootstack"
    state_dir.mkdir(exist_ok=True)
    return state_dir


def read_timestamp(state_dir, name):
    """Read a timestamp file. Returns None if not found."""
    ts_file = state_dir / f"last-{name}"
    if ts_file.exists():
        try:
            return datetime.fromisoformat(ts_file.read_text().strip())
        except (ValueError, OSError):
            return None
    return None


def write_timestamp(state_dir, name):
    """Write current timestamp to a state file."""
    ts_file = state_dir / f"last-{name}"
    ts_file.write_text(datetime.now().isoformat())


def check_maintenance(vault_root):
    """Check what maintenance is due. Returns list of due tasks."""
    state_dir = get_state_dir(vault_root)
    now = datetime.now()
    due = []

    # Check digest (every 7 days)
    last_digest = read_timestamp(state_dir, "digest")
    if last_digest is None or (now - last_digest) > timedelta(days=7):
        days_ago = "never" if last_digest is None else f"{(now - last_digest).days} days ago"
        due.append({
            "task": "digest",
            "last_run": days_ago,
            "description": "Synthesize recent journals and sessions into me.md Current Focus, patterns, and lessons"
        })

    # Check vault-map-updater (every 7 days)
    last_map = read_timestamp(state_dir, "vault-map-updater")
    if last_map is None or (now - last_map) > timedelta(days=7):
        days_ago = "never" if last_map is None else f"{(now - last_map).days} days ago"
        due.append({
            "task": "vault-map-updater",
            "last_run": days_ago,
            "description": "Update vault-map.md to reflect current vault structure"
        })

    # Check style-analyzer (every 7 days)
    last_style = read_timestamp(state_dir, "style-analyzer")
    if last_style is None or (now - last_style) > timedelta(days=7):
        # Only flag if samples folder exists and has content
        samples_dir = vault_root / "Content" / "Style" / "Samples"
        has_samples = samples_dir.exists() and any(
            f.suffix == ".md" and f.name != "README.md"
            for f in samples_dir.iterdir()
        ) if samples_dir.exists() else False
        if has_samples:
            days_ago = "never" if last_style is None else f"{(now - last_style).days} days ago"
            due.append({
                "task": "style-analyzer",
                "last_run": days_ago,
                "description": "Re-analyze writing samples and update the writing style guide"
            })

    # Check goal-review (every 30 days, only if goals are set up)
    setup_goals_exists = (vault_root / "Skills" / "setup-goals").exists()
    goals_file = vault_root / "About [You]" / "goals" / "1-year.md"
    if not setup_goals_exists and goals_file.exists():
        last_review = read_timestamp(state_dir, "goal-review")
        if last_review is None or (now - last_review) > timedelta(days=30):
            days_ago = "never" if last_review is None else f"{(now - last_review).days} days ago"
            due.append({
                "task": "goal-review",
                "last_run": days_ago,
                "description": "Monthly review of progress against 1-year goals"
            })

    # Check setup-me (surfaces once the other 5 setup-* skills have self-deleted
    # and setup-me itself still exists — prompts user to run it as the final step)
    setup_me_exists = (vault_root / "Skills" / "setup-me").exists()
    other_setups = [
        "setup-background",
        "setup-values",
        "setup-personality",
        "setup-writing",
        "setup-goals",
    ]
    other_setups_done = all(
        not (vault_root / "Skills" / name).exists() for name in other_setups
    )
    if setup_me_exists and other_setups_done:
        due.append({
            "task": "setup-me",
            "last_run": "never",
            "description": "Synthesize me.md from your completed setup files (final setup step, ~5 min)"
        })

    # Check kb-lint (every 14 days)
    last_kb_lint = read_timestamp(state_dir, "kb-lint")
    if last_kb_lint is None or (now - last_kb_lint) > timedelta(days=14):
        days_ago = "never" if last_kb_lint is None else f"{(now - last_kb_lint).days} days ago"
        due.append({
            "task": "kb-lint",
            "last_run": days_ago,
            "description": "Health check the knowledge base for orphan pages, broken links, and inconsistencies"
        })

    return due


def main():
    vault_root = find_vault_root()
    if not vault_root:
        # Not in a vault — exit silently
        sys.exit(0)

    # Handle --stamp flag: mark a task as completed
    if len(sys.argv) >= 3 and sys.argv[1] == "--stamp":
        task_name = sys.argv[2]
        state_dir = get_state_dir(vault_root)
        write_timestamp(state_dir, task_name)
        print(json.dumps({"suppressOutput": True}))
        sys.exit(0)

    due_tasks = check_maintenance(vault_root)

    if not due_tasks:
        # Nothing due — exit silently (no output = no context injected)
        sys.exit(0)

    # Build context message for Claude
    lines = ["Rootstack maintenance check: the following skills are overdue:\n"]
    for task in due_tasks:
        lines.append(f"- **{task['task']}** (last run: {task['last_run']}): {task['description']}")

    lines.append("\nAfter greeting the user, briefly mention that vault maintenance is due and offer to run it.")
    lines.append("If the user agrees, run each skill by reading its SKILL.md and following the instructions.")
    lines.append("After each skill completes successfully, stamp it as done by running:")
    lines.append("  python Skills/maintenance-check.py --stamp <task_name>")
    lines.append("This prevents the same task from being flagged again until the next cycle.")

    context = "\n".join(lines)

    # Output JSON that the hook system reads
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context
        }
    }

    print(json.dumps(output))


if __name__ == "__main__":
    main()
