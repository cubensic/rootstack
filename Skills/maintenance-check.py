"""
Maintenance Check — Run at session start to detect overdue vault maintenance.

Checks timestamps in .rootstack/ to determine if any maintenance skills
are due. Outputs JSON that Claude Code reads via the SessionStart hook.

If maintenance is due, returns additionalContext telling Claude what to run.
If nothing is due, returns silently.

Maintenance schedule:
- Session harvest: every session (always run)
- Digest: every 7 days
- README updater: every 7 days
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
            "description": "Synthesize recent journals and sessions into now.md, patterns, and lessons"
        })

    # Check readme-updater (every 7 days)
    last_readme = read_timestamp(state_dir, "readme-updater")
    if last_readme is None or (now - last_readme) > timedelta(days=7):
        days_ago = "never" if last_readme is None else f"{(now - last_readme).days} days ago"
        due.append({
            "task": "readme-updater",
            "last_run": days_ago,
            "description": "Update README.md to reflect current vault structure"
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
