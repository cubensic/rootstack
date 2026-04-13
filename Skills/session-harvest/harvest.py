"""
Session Harvest — Copy raw Claude Code session transcripts to the vault.

Finds recent .jsonl session files from ~/.claude/projects/ and copies them
to Knowledge Base/Raw/Sessions/. Only copies files not already present.

Usage:
    python harvest.py [--days 7] [--vault-root /path/to/vault]

If --vault-root is not specified, assumes the vault root is two directories
up from this script (Skills/session-harvest/ → vault root).
"""

import argparse
import json
import os
import shutil
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path


def find_claude_projects_dir():
    """Find the .claude/projects/ directory."""
    home = Path.home()
    claude_dir = home / ".claude" / "projects"
    if claude_dir.exists():
        return claude_dir
    return None


def encode_path(path):
    """
    Encode a filesystem path the way Claude Code does it.
    Path separators and colons become dashes.
    E.g. C:\\Users\\john\\projects\\Rootstack → C--Users-john-projects-Rootstack
         /Users/john/projects/Rootstack → -Users-john-projects-Rootstack
    """
    # Normalize to forward slashes first
    path_str = str(path).replace("\\", "/")
    # Remove trailing slash
    path_str = path_str.rstrip("/")
    # Replace / with -
    encoded = path_str.replace("/", "-")
    # Replace : with -
    encoded = encoded.replace(":", "-")
    return encoded


def find_vault_root(script_path):
    """Find the vault root (two levels up from this script)."""
    return script_path.parent.parent.parent


def get_session_metadata(jsonl_path):
    """Extract basic metadata from a session file (first few lines)."""
    metadata = {
        "session_id": jsonl_path.stem,
        "file_size": jsonl_path.stat().st_size,
        "modified": datetime.fromtimestamp(jsonl_path.stat().st_mtime),
    }

    # Try to get the first timestamp from the file
    try:
        with open(jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    if "timestamp" in entry:
                        metadata["started"] = entry["timestamp"]
                        break
                except (json.JSONDecodeError, KeyError):
                    continue
    except Exception:
        pass

    return metadata


def harvest(vault_root, days=7, dry_run=False):
    """
    Copy recent Claude Code session files to the vault's Raw/Sessions folder.

    Returns a list of copied files.
    """
    claude_projects = find_claude_projects_dir()
    if not claude_projects:
        print("ERROR: Could not find ~/.claude/projects/")
        return []

    # Encode the vault path to find the matching Claude project folder
    vault_encoded = encode_path(vault_root.resolve())

    # Find matching project directories (exact match and worktree variants)
    matching_dirs = []
    for d in claude_projects.iterdir():
        if d.is_dir() and d.name.startswith(vault_encoded):
            matching_dirs.append(d)

    if not matching_dirs:
        # Also try matching against all project dirs for any vault-related sessions
        print(f"No Claude project directory found for: {vault_encoded}")
        print(f"Available directories:")
        for d in sorted(claude_projects.iterdir()):
            if d.is_dir():
                print(f"  {d.name}")
        return []

    # Target directory for raw session files
    raw_sessions = vault_root / "Knowledge Base" / "Raw" / "Sessions"
    raw_sessions.mkdir(parents=True, exist_ok=True)

    cutoff = datetime.now() - timedelta(days=days)
    copied = []

    for project_dir in matching_dirs:
        for jsonl_file in project_dir.glob("*.jsonl"):
            # Skip if older than cutoff
            modified = datetime.fromtimestamp(jsonl_file.stat().st_mtime)
            if modified < cutoff:
                continue

            # Skip if already copied
            target = raw_sessions / jsonl_file.name
            if target.exists():
                # Check if source is newer (session continued)
                if jsonl_file.stat().st_mtime <= target.stat().st_mtime:
                    continue

            # Copy
            if dry_run:
                print(f"  [DRY RUN] Would copy: {jsonl_file.name} ({jsonl_file.stat().st_size:,} bytes)")
            else:
                shutil.copy2(jsonl_file, target)
                print(f"  Copied: {jsonl_file.name} ({jsonl_file.stat().st_size:,} bytes)")

            copied.append({
                "file": jsonl_file.name,
                "target": str(target),
                "size": jsonl_file.stat().st_size,
                "modified": modified.isoformat(),
                "source_dir": project_dir.name,
            })

    return copied


def main():
    parser = argparse.ArgumentParser(description="Harvest Claude Code sessions into Rootstack vault")
    parser.add_argument("--days", type=int, default=7, help="How many days back to look (default: 7)")
    parser.add_argument("--vault-root", type=str, help="Path to vault root (default: auto-detect)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be copied without copying")
    parser.add_argument("--all-projects", action="store_true", help="Search all Claude project directories, not just the vault's")
    args = parser.parse_args()

    if args.vault_root:
        vault_root = Path(args.vault_root)
    else:
        vault_root = find_vault_root(Path(__file__).resolve())

    if not (vault_root / "README.md").exists():
        print(f"ERROR: {vault_root} does not look like a Rootstack vault (no README.md)")
        sys.exit(1)

    print(f"Vault root: {vault_root}")
    print(f"Looking back: {args.days} days")
    if args.dry_run:
        print("Mode: DRY RUN")
    print()

    copied = harvest(vault_root, days=args.days, dry_run=args.dry_run)

    if copied:
        print(f"\n{len(copied)} session(s) {'would be ' if args.dry_run else ''}copied.")
    else:
        print("\nNo new sessions to copy.")


if __name__ == "__main__":
    main()
