# project-os

`project-os` is a document-first project operating system for AI agents and human teams.

It pushes most project ambiguity into a small source-of-truth doc stack first, then lets the implementation loop focus only on the last mile.

## Core idea

- `0-90`: solve scope, goals, architecture, stage, blockers, and operating protocol in docs
- `90-100`: solve only bounded implementation, verification, and blocker clearing in the loop

If the docs are right, the project should mostly already be right.

## Default autopilot

`project-os` should normally run in autopilot.

That means:

- if the user gives a clear top-level outcome, use it
- if the user does not give a narrower sub-goal, derive the next active goal automatically
- do not wait for the user to manually pick every loop step

Autopilot reads:

```text
KERNEL.md
-> STRATEGY.md
-> PROJECT.md
-> BLOCKERS.md
-> machine truth
```

Then it picks one active goal, usually the highest-value blocker-moving step.

## Evolution model

`project-os` now uses a two-kernel model:

- repo `KERNEL.md`: local self-evolution layer for one project
- `project-os/KERNEL.md`: cross-project self-evolution layer for the operating system itself

Evolution pipeline:

```text
repo loop
-> repo KERNEL.md
-> project-os/KERNEL.md
-> SKILL.md / references
```

This means the skill does not grow directly from one project's noise.

## Thin kernel writer

Use the thin writer when a loop needs to record one repeated candidate pattern without touching stable kernel sections:

```bash
python3 scripts/kernel_writer.py upsert \
  --kernel /path/to/KERNEL.md \
  --pattern-id repo-cand-001 \
  --set "symptom=The same blocker keeps being rediscovered" \
  --set "proposed_rule=Freeze one blocker owner doc first" \
  --set "evidence=loop-3 in repo-x" \
  --set "status=candidate"
```

This command edits only the `## Candidate Patterns` table.

## What it creates

Default owner-doc stack:

- `STRATEGY.md`
- `ARCHITECTURE.md`
- `ENGINEERING.md`
- `PROJECT.md`
- `BLOCKERS.md`
- `HARNESS.md`
- machine truth such as `manifest.json`

Optional base layer:

- `CONTEXT.md` for domain language, terminology boundaries, and anti-synonym drift
- `KERNEL.md` for repo-specific operating patterns and promotion candidates

## Repository layout

```text
.
├── KERNEL.md
├── SKILL.md
├── scripts/
│   ├── kernel_writer.py
│   └── tests/
│       └── test_kernel_writer.py
├── agents/
│   └── openai.yaml
└── references/
    ├── doc-audit.md
    ├── doc-templates.md
    ├── harness-protocol.md
    └── kernel-protocol.md
```

## Usage

Install or copy this skill into your Codex skills directory as `project-os`, then invoke it when a repo needs:

- one owner doc per important question
- one repo-level self-evolution layer
- a stable read/write protocol
- less “thinking while doing”
- a narrow execution loop against frozen project truth
- default autopilot loop execution without requiring manual sub-goal selection

## Design rules

- one important question
- one owner document
- one update protocol
- no duplicated definitions
- table-first by default
- no daily free-form rediscovery
