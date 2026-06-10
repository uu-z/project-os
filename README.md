# project-os

`project-os` is a document-first project operating system for AI agents and human teams.

It pushes most project ambiguity into a small source-of-truth doc stack first, then lets the implementation loop focus only on the last mile.

## Core idea

- `0-90`: solve scope, goals, architecture, stage, blockers, and operating protocol in docs
- `90-100`: solve only bounded implementation, verification, and blocker clearing in the loop

If the docs are right, the project should mostly already be right.

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

## Repository layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── doc-audit.md
    ├── doc-templates.md
    └── harness-protocol.md
```

## Usage

Install or copy this skill into your Codex skills directory as `project-os`, then invoke it when a repo needs:

- one owner doc per important question
- a stable read/write protocol
- less “thinking while doing”
- a narrow execution loop against frozen project truth

## Design rules

- one important question
- one owner document
- one update protocol
- no duplicated definitions
- table-first by default
- no daily free-form rediscovery
