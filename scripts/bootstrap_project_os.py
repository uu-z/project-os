#!/usr/bin/env python3
"""
Bootstrap a repo with the minimal project-os control plane.

This script is intentionally narrow:
- it creates only the minimum control-plane docs
- it does not overwrite existing files unless asked
- it creates a placeholder machine-truth directory, not a real runtime manifest
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap a repo with project-os docs.")
    parser.add_argument("--root", required=True, help="Target repo root")
    parser.add_argument(
        "--project-name",
        help="Human-friendly project name used in generated docs",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing project-os files",
    )
    return parser.parse_args()


def write_file(path: Path, content: str, overwrite: bool) -> str:
    existed = path.exists()
    if existed and not overwrite:
        return "skipped"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "overwritten" if existed else "created"


def file_content_map(project_name: str) -> dict[str, str]:
    return {
        "CONTEXT.md": f"""# {project_name} Context

`CONTEXT.md` is the repo's language kernel.

## One sentence

Define what this project is in one sentence.

## Core Terms

| Term | Meaning | Avoid |
|---|---|---|
| `pending` | Fill with the canonical domain term. | drifting synonyms |

## Boundaries

| Boundary | Rule |
|---|---|
| `pending` | Fill with one canonical boundary rule. |

## Stable Invariants

| Invariant | Why |
|---|---|
| `pending` | Fill with one stable invariant. |
""",
        "KERNEL.md": f"""# {project_name} Project Kernel

`KERNEL.md` is the repo's local self-evolution layer.

## Stable Patterns

| kernel_id | Rule | Why it is stable |
|---|---|---|
| `pending` | Fill with the first stable repo operating rule. | Explain why it repeats. |

## Candidate Patterns

Only this section should be auto-edited by loops.

| pattern_id | first_seen | last_seen | loop_count | symptom | proposed_rule | evidence | status |
|---|---|---|---:|---|---|---|---|
| `pending` | `-` | `-` | `0` | `-` | `-` | `-` | `empty` |

## Promotion Upstream

| promotion_id | local_pattern | promotion_gate | current_status |
|---|---|---|---|
| `pending` | `-` | Fill when a local pattern may promote into project-os. | `pending` |

## Rejected Patterns

| rejection_id | rejected_pattern | why rejected |
|---|---|---|
| `pending` | `-` | Fill when a tempting false pattern appears. |

## Update Protocol

| Surface | Default rule |
|---|---|
| `Stable Patterns` | manual promotion only |
| `Candidate Patterns` | loop may append or merge repeated local lessons |
| `Promotion Upstream` | update when a local lesson may become global |
| `Rejected Patterns` | manual only |
""",
        "STRATEGY.md": f"""# {project_name} Strategy

## One sentence

Define what this project exists to deliver right now.

## Current Strategy

| Question | Answer |
|---|---|
| What is this release trying to achieve? | `pending` |
| What is explicitly out of scope? | `pending` |
| What does success mean? | `pending` |

## Scope

| Item | In scope | Why |
|---|---|---|
| `pending` | yes | Fill with the first scope item. |

## Non-goals

| Item | Why not now |
|---|---|
| `pending` | Fill with the first non-goal. |
""",
        "ARCHITECTURE.md": f"""# {project_name} Architecture

## Mainline

```text
pending -> pending -> pending
```

## Boundaries

| Boundary | Rule |
|---|---|
| `pending` | Fill with one boundary rule. |

## Truth Sources

| Question | Source |
|---|---|
| Current machine truth | `artifacts/current/manifest.json` |
| Current project state | `PROJECT.md` |
| Current blockers | `BLOCKERS.md` |
""",
        "ENGINEERING.md": f"""# {project_name} Engineering

## Official Commands

| Command | Use | Green signal |
|---|---|---|
| `pending` | Fill with the first official command. | Fill with the expected green signal. |

## Artifact Meanings

| Artifact | Role |
|---|---|
| `artifacts/current/manifest.json` | expected machine-truth path once the runtime owns it |

## Constraints

| Constraint | Meaning |
|---|---|
| `pending` | Fill with one engineering constraint. |
""",
        "PROJECT.md": f"""# {project_name} Project

## Current Stage

| Field | Value |
|---|---|
| Stage | `pending` |
| Current objective | `pending` |
| Current focus | `pending` |

## Milestones

| Milestone | Goal | Status |
|---|---|---|
| `M1` | Freeze the first correct control plane. | `pending` |

## Owners

| Area | Owner |
|---|---|
| Control plane | `main agent / project lead` |
| Implementation | `workers` |
| Verification | `verifiers` |
""",
        "BLOCKERS.md": f"""# {project_name} Blockers

## P0 Blockers

| Blocker | Why it blocks | Owner | Evidence needed | Next action | Status |
|---|---|---|---|---|---|
| `pending` | Fill with the first real blocker. | `pending` | `pending` | `pending` | `pending` |

## P1 Blockers

| Blocker | Why it matters later | Owner | Evidence needed | Next action | Status |
|---|---|---|---|---|---|
| `pending` | Fill with the first secondary blocker. | `pending` | `pending` | `pending` | `pending` |
""",
        "HARNESS.md": f"""# {project_name} Harness

## Read Order

| Step | Source | Why |
|---|---|---|
| 1 | `KERNEL.md` | local operating lessons |
| 2 | `STRATEGY.md` | target and scope |
| 3 | `ARCHITECTURE.md` | system shape |
| 4 | `ENGINEERING.md` | command and evidence rules |
| 5 | `PROJECT.md` | stage and milestone context |
| 6 | `BLOCKERS.md` | current priority |
| 7 | `artifacts/current/manifest.json` | machine truth once runtime owns it |

## Main Agent Rules

- main agent is not the default implementer
- main agent codes only when it is obviously faster and does not damage project-level attention
- main agent fixes the control plane first, then delegates the final `90-100` loop

## Autopilot Loop

1. read the hot truth stack
2. derive one active goal
3. choose one primary blocker
4. decide whether it is a `0-90` or `90-100` problem
5. write back to `BLOCKERS.md`, `PROJECT.md`, and `KERNEL.md` when reality changes
""",
        "artifacts/current/README.md": f"""# {project_name} Machine Truth Placeholder

This directory is reserved for runtime-owned machine truth, usually:

```text
artifacts/current/manifest.json
```

Do not hand-edit a real manifest once the runtime starts owning it.
""",
    }


def write_summary(root: Path, results: list[dict[str, str]]) -> None:
    summary_path = root / ".project-os-bootstrap.json"
    payload = {
        "artifact_kind": "project-os-bootstrap-summary",
        "artifact_version": 1,
        "results": results,
    }
    summary_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    project_name = args.project_name or root.name

    results: list[dict[str, str]] = []
    for relative_path, content in file_content_map(project_name).items():
        target = root / relative_path
        existed = target.exists()
        status = write_file(target, content, args.overwrite)
        results.append(
            {
                "path": relative_path,
                "status": "overwritten" if existed and args.overwrite else status,
            }
        )

    write_summary(root, results)

    for item in results:
        print(f"{item['status']}: {item['path']}")
    print("created: .project-os-bootstrap.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
