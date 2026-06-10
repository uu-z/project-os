#!/usr/bin/env python3
"""
Thin kernel writer for project-os.

This tool only edits the markdown table under `## Candidate Patterns`.
It is intentionally narrow so project loops can record local or global
kernel candidates without mutating stable kernel sections.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SECTION_HEADING = "## Candidate Patterns"
PLACEHOLDER_PATTERN_ID = "pending"
SIMPLE_TOKEN_RE = re.compile(r"^[A-Za-z0-9._:/<>-]+$")


@dataclass
class TableBlock:
    start: int
    end: int
    header: list[str]
    separator: str
    rows: list[dict[str, str]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upsert a row in the Candidate Patterns table of a KERNEL.md file."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    upsert = subparsers.add_parser("upsert", help="Upsert one candidate pattern row")
    upsert.add_argument("--kernel", required=True, help="Path to KERNEL.md")
    upsert.add_argument("--pattern-id", required=True, help="Candidate pattern identifier")
    upsert.add_argument(
        "--set",
        action="append",
        default=[],
        metavar="COLUMN=VALUE",
        help="Set or overwrite a column value",
    )
    upsert.add_argument(
        "--inc",
        action="append",
        default=[],
        metavar="COLUMN=DELTA",
        help="Increment a numeric column by DELTA",
    )
    upsert.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Date used for first_seen / last_seen defaults (default: today)",
    )
    upsert.add_argument(
        "--dry-run",
        action="store_true",
        help="Print updated file to stdout instead of writing back",
    )
    return parser.parse_args()


def split_row(line: str) -> list[str]:
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        raise ValueError(f"not a markdown table row: {line!r}")
    cells = [cell.strip() for cell in stripped[1:-1].split("|")]
    return [unwrap(cell) for cell in cells]


def unwrap(value: str) -> str:
    if len(value) >= 2 and value.startswith("`") and value.endswith("`"):
        return value[1:-1]
    return value


def is_missing(value: str | None) -> bool:
    return value is None or value == "" or value == "-"


def wrap(value: str) -> str:
    escaped = value.replace("|", "\\|")
    if escaped == "":
        return "`-`"
    if SIMPLE_TOKEN_RE.fullmatch(escaped):
        return f"`{escaped}`"
    return escaped


def parse_assignments(values: list[str], label: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            raise ValueError(f"invalid {label} assignment: {item!r}")
        key, value = item.split("=", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"empty column in {label} assignment: {item!r}")
        result[key] = value.strip()
    return result


def find_candidate_table(lines: list[str]) -> TableBlock:
    try:
        section_index = next(i for i, line in enumerate(lines) if line.strip() == SECTION_HEADING)
    except StopIteration as exc:
        raise ValueError(f"missing section heading: {SECTION_HEADING}") from exc

    next_heading_index = len(lines)
    for idx in range(section_index + 1, len(lines)):
        if lines[idx].startswith("## "):
            next_heading_index = idx
            break

    table_start = None
    for idx in range(section_index + 1, next_heading_index):
        if lines[idx].lstrip().startswith("|"):
            table_start = idx
            break
    if table_start is None or table_start + 1 >= next_heading_index:
        raise ValueError("missing Candidate Patterns table")

    table_end = table_start
    while table_end < next_heading_index and lines[table_end].lstrip().startswith("|"):
        table_end += 1

    header = split_row(lines[table_start])
    separator = lines[table_start + 1]
    row_lines = lines[table_start + 2 : table_end]
    rows: list[dict[str, str]] = []
    for row_line in row_lines:
        cells = split_row(row_line)
        if len(cells) != len(header):
            raise ValueError("row/header width mismatch in Candidate Patterns table")
        rows.append(dict(zip(header, cells)))

    if "pattern_id" not in header:
        raise ValueError("Candidate Patterns table must contain a pattern_id column")

    return TableBlock(
        start=table_start,
        end=table_end,
        header=header,
        separator=separator,
        rows=rows,
    )


def apply_defaults(row: dict[str, str], header: list[str], current_date: str, is_new: bool) -> None:
    if "first_seen" in header and is_new and is_missing(row.get("first_seen")):
        row["first_seen"] = current_date
    if "last_seen" in header and is_missing(row.get("last_seen")):
        row["last_seen"] = current_date
    if "loop_count" in header and is_missing(row.get("loop_count")):
        row["loop_count"] = "1" if is_new else row.get("loop_count", "1")


def apply_increments(row: dict[str, str], increments: dict[str, str]) -> None:
    for column, delta_text in increments.items():
        if column not in row:
            raise ValueError(f"cannot increment missing column: {column}")
        try:
            base = int(row[column] or "0")
            delta = int(delta_text)
        except ValueError as exc:
            raise ValueError(f"increment requires integer values: {column}={delta_text}") from exc
        row[column] = str(base + delta)


def normalize_placeholder(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [row for row in rows if row.get("pattern_id") != PLACEHOLDER_PATTERN_ID]


def render_rows(header: list[str], rows: list[dict[str, str]]) -> list[str]:
    rendered: list[str] = []
    for row in rows:
        cells = [wrap(row.get(column, "-") or "-") for column in header]
        rendered.append("| " + " | ".join(cells) + " |")
    return rendered


def upsert(kernel_path: Path, pattern_id: str, set_values: dict[str, str], inc_values: dict[str, str], current_date: str) -> str:
    lines = kernel_path.read_text(encoding="utf-8").splitlines()
    table = find_candidate_table(lines)
    rows = normalize_placeholder(table.rows)

    existing = next((row for row in rows if row.get("pattern_id") == pattern_id), None)
    is_new = existing is None
    row = existing.copy() if existing else {column: "" for column in table.header}
    row["pattern_id"] = pattern_id

    apply_defaults(row, table.header, current_date, is_new)
    for column, value in set_values.items():
        if column not in table.header:
            raise ValueError(f"unknown Candidate Patterns column: {column}")
        row[column] = value
    if "last_seen" in table.header and "last_seen" not in set_values:
        row["last_seen"] = current_date
    if "loop_count" in table.header and "loop_count" not in set_values and "loop_count" not in inc_values:
        base = int(existing["loop_count"]) if existing and existing.get("loop_count", "").isdigit() else 0
        row["loop_count"] = str(base + 1 if existing else 1)
    apply_increments(row, inc_values)

    if existing:
        rows = [row if item.get("pattern_id") == pattern_id else item for item in rows]
    else:
        rows.append(row)

    updated_table_lines = [lines[table.start], table.separator, *render_rows(table.header, rows)]
    new_lines = lines[: table.start] + updated_table_lines + lines[table.end :]
    return "\n".join(new_lines) + "\n"


def main() -> int:
    args = parse_args()
    if args.command != "upsert":
        raise AssertionError(f"unsupported command: {args.command}")

    kernel_path = Path(args.kernel)
    if not kernel_path.exists():
        print(f"error: kernel file not found: {kernel_path}", file=sys.stderr)
        return 1

    try:
        set_values = parse_assignments(args.set, "--set")
        inc_values = parse_assignments(args.inc, "--inc")
        updated = upsert(kernel_path, args.pattern_id, set_values, inc_values, args.date)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.dry_run:
        sys.stdout.write(updated)
    else:
        kernel_path.write_text(updated, encoding="utf-8")
        print(f"updated {kernel_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
