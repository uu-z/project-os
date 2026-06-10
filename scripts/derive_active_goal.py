#!/usr/bin/env python3
"""
Derive one active goal from a repo's project-os truth stack.

The heuristic is intentionally narrow:
- prefer the first concrete P0 blocker
- otherwise prefer finishing an obviously incomplete control plane
- otherwise prefer establishing machine-truth ownership
- otherwise suggest the next verification / rehearsal step
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Table:
    header: list[str]
    rows: list[dict[str, str]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Derive one active goal from a project-os repo.")
    parser.add_argument("--root", required=True, help="Target repo root")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of a human-readable summary",
    )
    return parser.parse_args()


def read_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def resolve_doc_path(root: Path, filename: str) -> Path:
    primary = root / filename
    if primary.exists():
        return primary
    nested = root / "docs" / "actum" / filename
    if nested.exists():
        return nested
    return primary


def unwrap(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value.startswith("`") and value.endswith("`"):
        return value[1:-1]
    return value


def is_pending(value: str | None) -> bool:
    if value is None:
        return True
    stripped = value.strip()
    return stripped in {"", "-", "pending", "`pending`", "`-`", "empty", "`empty`"}


def parse_row(line: str) -> list[str]:
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        raise ValueError(f"not a table row: {line!r}")
    return [unwrap(cell) for cell in stripped[1:-1].split("|")]


def find_section(lines: list[str], heading: str) -> tuple[int, int] | None:
    for idx, line in enumerate(lines):
        if line.strip() == heading:
            end = len(lines)
            for j in range(idx + 1, len(lines)):
                if lines[j].startswith("## "):
                    end = j
                    break
            return idx, end
    return None


def find_first_table(lines: list[str], start: int, end: int) -> Table | None:
    table_start = None
    for idx in range(start, end):
        if lines[idx].lstrip().startswith("|"):
            table_start = idx
            break
    if table_start is None or table_start + 1 >= end:
        return None

    header = parse_row(lines[table_start])
    rows: list[dict[str, str]] = []
    idx = table_start + 2
    while idx < end and lines[idx].lstrip().startswith("|"):
        cells = parse_row(lines[idx])
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
        idx += 1
    return Table(header=header, rows=rows)


def find_table_by_heading(path: Path, heading: str) -> Table | None:
    lines = read_lines(path)
    section = find_section(lines, heading)
    if section is None:
        return None
    start, end = section
    return find_first_table(lines, start + 1, end)


def first_concrete_row(table: Table | None, key_column: str) -> dict[str, str] | None:
    if table is None:
        return None
    for row in table.rows:
        key_value = row.get(key_column)
        if is_pending(key_value):
            continue
        return row
    return None


def file_has_pending_markers(path: Path) -> bool:
    if not path.exists():
        return True
    content = path.read_text(encoding="utf-8")
    return "`pending`" in content or "| `pending` |" in content or "Fill with" in content


def derive_goal(root: Path) -> dict[str, object]:
    blockers_path = resolve_doc_path(root, "BLOCKERS.md")
    project_path = resolve_doc_path(root, "PROJECT.md")
    strategy_path = resolve_doc_path(root, "STRATEGY.md")
    kernel_path = root / "KERNEL.md"
    harness_path = resolve_doc_path(root, "HARNESS.md")
    manifest_path = root / "artifacts" / "current" / "manifest.json"

    p0_table = find_table_by_heading(blockers_path, "## P0 Blockers")
    p0_row = first_concrete_row(p0_table, "Blocker")
    if p0_row:
        blocker = p0_row.get("Blocker", "").strip()
        next_action = p0_row.get("Next action", "").strip() or p0_row.get("Next Action", "").strip()
        owner = p0_row.get("Owner", "").strip()
        return {
            "mode": "blocker-driven",
            "primary_blocker": blocker,
            "active_goal": f"Move the top P0 blocker: {blocker}",
            "suggested_next_action": next_action or f"Produce the next evidence needed to move blocker: {blocker}",
            "owner": owner or "main agent",
            "source": str(blockers_path),
        }

    control_plane_files = [kernel_path, strategy_path, project_path, blockers_path, harness_path]
    pending_files = [path.name for path in control_plane_files if file_has_pending_markers(path)]
    if pending_files:
        return {
            "mode": "control-plane-freeze",
            "primary_blocker": "incomplete control plane",
            "active_goal": "Freeze the missing 0-90 control-plane truth before broad execution.",
            "suggested_next_action": f"Replace placeholder content in: {', '.join(pending_files)}",
            "owner": "main agent",
            "source": ", ".join(str(path) for path in control_plane_files if path.name in pending_files),
        }

    if not manifest_path.exists():
        return {
            "mode": "machine-truth-missing",
            "primary_blocker": "missing machine truth",
            "active_goal": "Establish the repo's runtime-owned machine-truth path.",
            "suggested_next_action": "Create or wire the real artifacts/current/manifest.json path through the runtime, not by hand.",
            "owner": "main agent",
            "source": str(manifest_path),
        }

    stage_table = find_table_by_heading(project_path, "## Current Stage")
    stage_row = first_concrete_row(stage_table, "Field")
    stage_value = stage_row.get("Value", "").strip() if stage_row else ""

    return {
        "mode": "verification-or-rehearsal",
        "primary_blocker": "no explicit P0 blocker found",
        "active_goal": "Run the next highest-value verification or rehearsal against the current truth stack.",
        "suggested_next_action": "Verify machine truth freshness, then run the smallest rehearsal or validation step that tests the current stage claim.",
        "owner": "main agent",
        "source": str(manifest_path),
        "stage_hint": stage_value or None,
    }


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    goal = derive_goal(root)
    if args.json:
        print(json.dumps(goal, indent=2, ensure_ascii=False))
    else:
        print(f"Mode: {goal['mode']}")
        print(f"Active goal: {goal['active_goal']}")
        print(f"Primary blocker: {goal['primary_blocker']}")
        print(f"Next action: {goal['suggested_next_action']}")
        print(f"Owner: {goal['owner']}")
        print(f"Source: {goal['source']}")
        if goal.get("stage_hint"):
            print(f"Stage hint: {goal['stage_hint']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
