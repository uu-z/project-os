---
name: project-os
description: Build or refactor a project into a document-first operating system with one source-of-truth document per layer and per dimension. Use when the user wants to stop "thinking while doing", freeze unique truth docs for strategy, architecture, engineering, project management, blockers, and harness protocol, and make daily agent loops align only against those documents plus the machine truth artifacts.
---

# Project OS

## Overview

Use this skill to turn a messy project into a layered control plane. The goal is not "more docs"; the goal is one unique truth document for each important question, plus one harness protocol so humans and agents loop against the same operating system every day.

Think about it as a `0-90 / 90-100` split:

- `project-os` should solve the first `0-90` by moving most ambiguity, ownership, scope, and stage problems into a stable document operating system
- the implementation loop should solve only the last `90-100` by executing against that frozen control plane

If the docs are right, the project should mostly already be right. Daily execution should be a narrow loop, not a daily redesign exercise.

If the repo does not already have adequate owner docs, create them.
If the repo already has docs, audit them before trusting them.

When terminology, boundaries, stage labels, or ownership are unclear, use a `grill-with-docs` style pass first: inspect code and docs, resolve what can be resolved from source, then ask only the smallest missing questions.

Also separate three different kinds of truth before writing anything:

- domain truth
- local project operating truth
- global `project-os` operating truth

## Core Model

Treat project truth as three layers:

| Layer | Purpose | Change Rate | Truth Form |
|---|---|---:|---|
| Decision layer | Define why the project exists and what "correct" means | Slow | Top-level docs |
| Execution layer | Define stage, blockers, owners, milestones, and loop cadence | Medium / fast | Top-level docs |
| Machine layer | Define actual runtime and artifact truth | High | Structured artifacts |

The rule is simple:

- one important question
- one owner document
- one update protocol
- no duplicated definitions

The intent is also simple:

- solve most project problems at the doc layer first
- leave only the final implementation and verification gap to the execution loop

Before those three layers, some repos also need two deeper bases:

| Layer | Purpose | Change Rate | Truth Form |
|---|---|---:|---|
| `L0 domain kernel` | Define the canonical domain vocabulary and concept boundaries | Very slow | `CONTEXT.md` or equivalent glossary/kernel doc |
| `L0.5 project kernel` | Define repo-specific operating patterns and local evolution candidates | Slow | `KERNEL.md` |

Use `CONTEXT.md` when the project keeps losing time to terminology drift, synonym drift, or architecture arguments caused by fuzzy language.
Use repo `KERNEL.md` when the project keeps rediscovering the same operating lesson during loops.

## Standard Doc Stack

Default to a `6 + 1` stack:

| File | Layer | Answers |
|---|---|---|
| `STRATEGY.md` | Decision | Why this project exists, what this release is, what is explicitly out |
| `ARCHITECTURE.md` | Decision | What the single-track system is, what the boundaries are, where truth lives |
| `ENGINEERING.md` | Decision | What counts as the official engineering interface, verification path, and artifact contract |
| `PROJECT.md` | Execution | What stage the project is in, what milestones exist, who owns what |
| `BLOCKERS.md` | Execution | What currently blocks progress, why, who owns it, what evidence clears it |
| `HARNESS.md` | Execution | How agents and humans read, write, delegate, update, and escalate |
| `machine truth` | Machine | The active structured runtime truth such as `manifest.json` or release snapshots |

If the repo already has near-equivalent docs, reuse and rename only when the duplication cost is lower than preserving drift.

## Optional `L0` Domain Kernel

When the repo has meaningful domain complexity, add or preserve one `L0` doc:

| File | Layer | Answers |
|---|---|---|
| `CONTEXT.md` | `L0 domain kernel` | What the important domain terms mean, which synonyms to avoid, and where semantic boundaries sit |

Rules:

- `CONTEXT.md` is repo-level language truth, not daily status truth
- `CONTEXT.md` should not become a launch tracker, blocker board, or implementation diary
- daily loops should not reread the whole `CONTEXT.md` by default
- agents should reread `CONTEXT.md` only when terminology, ownership, boundary, or protocol meaning is unclear

## Optional Repo `KERNEL.md`

When the repo has repeated execution patterns worth preserving, add or preserve one local `KERNEL.md`:

| File | Layer | Answers |
|---|---|---|
| `KERNEL.md` | `L0.5 project kernel` | What repo-specific operating patterns are stable, which local patterns are still candidates, and what may later promote into `project-os` itself |

Rules:

- repo `KERNEL.md` is local operating truth, not global skill truth
- repo `KERNEL.md` is short enough to stay in the hot loop when present
- only the candidate section should be auto-edited by ordinary project loops
- repo `KERNEL.md` may feed `project-os/KERNEL.md`, but should not bypass it

## Missing-Docs Mode

When the repo does not already have the required owner docs:

1. inspect existing code, artifacts, and hot docs
2. infer as much as possible from source
3. use a `grill-with-docs` style pass to resolve ambiguous terms and boundaries
4. create the minimum owner docs needed for the standard stack
5. freeze the read/write protocol in `HARNESS.md`
6. create `KERNEL.md` if the repo already shows repeated local operating lessons

Do not wait for perfect documentation before creating the control plane. The first correct version should be small, table-first, and explicit about assumptions.

## Existing-Docs Audit Mode

When the repo already has documentation:

1. inventory the hot-path docs
2. map each doc to the question it claims to answer
3. detect duplicated truths and conflicting definitions
4. decide which doc should own each question
5. demote, merge, or replace the rest

Run this audit table:

| Check | Question |
|---|---|
| Ownership | Does this doc own one clear question? |
| Duplication | Is the same fact defined elsewhere? |
| Layer fit | Is this decision, execution, or machine truth? |
| Freshness | Is the truth stable enough to live here? |
| Structure | Should this be a table instead of prose? |
| Loop fitness | Should the daily loop read this, write this, or ignore this? |

## Ownership Rules

Enforce these rules:

1. `STRATEGY.md` owns goals, scope, success, and non-goals.
2. `ARCHITECTURE.md` owns system shape, boundaries, truth source, and anti-dual-track rules.
3. `ENGINEERING.md` owns official commands, verification standards, artifact meanings, and implementation constraints.
4. `PROJECT.md` owns stage, milestones, owners, and deadlines.
5. `BLOCKERS.md` owns current blockers and risk movement.
6. `HARNESS.md` owns the daily loop protocol and agent behavior.
7. Machine artifacts own current runtime facts.
8. `CONTEXT.md`, when present, owns canonical domain language and anti-synonym rules.
9. Repo `KERNEL.md`, when present, owns repo-specific operating patterns and promotion candidates.

If a fact already has an owner document, all other docs must reference it rather than redefining it.

## Table-First Rule

Prefer structured tables over prose.

Use prose only for:

- one-sentence definitions
- irreversible constraints
- short interpretation notes

Everything else should default to a table:

- goals
- scope
- stages
- milestones
- boundaries
- blockers
- owners
- evidence
- escalation rules
- read/write rules
- promotion rules

For ready-made table shapes, read:

- [references/doc-templates.md](references/doc-templates.md)
- [references/harness-protocol.md](references/harness-protocol.md)
- [references/kernel-protocol.md](references/kernel-protocol.md)
- [references/doc-audit.md](references/doc-audit.md)

## Write Rules

Default write policy:

| File | Typical write frequency |
|---|---:|
| `STRATEGY.md` | Rare |
| `ARCHITECTURE.md` | Rare |
| `ENGINEERING.md` | Low |
| `PROJECT.md` | Daily / milestone-based |
| `BLOCKERS.md` | Every meaningful loop |
| `KERNEL.md` candidate section | On repeated local learning only |
| `HARNESS.md` | Rare |
| Machine artifacts | Automated |

Agents should not casually rewrite decision-layer docs during daily execution.

## Daily Harness Protocol

Default read order:

1. `KERNEL.md` when present
2. `STRATEGY.md`
3. `ARCHITECTURE.md`
4. `ENGINEERING.md`
5. `PROJECT.md`
6. `BLOCKERS.md`
7. `HARNESS.md`
8. active machine truth

Default write-back order:

1. update machine truth through the normal system path
2. update `BLOCKERS.md`
3. update `PROJECT.md`
4. update repo `KERNEL.md` candidate section only when the same local lesson has repeated
5. update `HARNESS.md` only if the protocol itself changed

Do not rewrite `STRATEGY.md`, `ARCHITECTURE.md`, or `ENGINEERING.md` unless a real decision changed.

`CONTEXT.md` is not in the default hot read loop. Read it on demand when the loop hits a language or boundary ambiguity.
Repo `KERNEL.md`, when present, is part of the default hot read loop because it carries local operating lessons.

## 0-90 / 90-100 Rule

Use this rule aggressively:

| Range | Meaning | Default owner |
|---|---|---|
| `0-90` | scope, goals, architecture, stage, blockers, operating protocol, truth ownership | `project-os` doc stack |
| `90-100` | bounded implementation, verification, evidence refresh, blocker clearing | execution loop |

If the team is still arguing daily about stage, scope, ownership, or what "done" means, the project is not in the `90-100` zone yet.

Do not spend implementation effort to compensate for missing control-plane clarity when that clarity should live in the docs.

## Evolution Pipeline

Use this pipeline:

```text
repo loop
-> repo KERNEL.md
-> project-os KERNEL.md
-> SKILL.md / references
```

Do not allow:

```text
repo loop -> direct SKILL.md growth
```

## Adoption Workflow

When applying this skill to a repo:

1. Determine whether the repo is in Missing-Docs Mode or Existing-Docs Audit Mode.
2. Inventory existing hot-path docs, code truth, and machine artifacts.
3. Map each existing doc to one owner question.
4. Identify duplicated truths and missing owner docs.
5. Use a `grill-with-docs` style pass to resolve ambiguous language and boundaries.
6. Collapse the control plane into the standard doc stack.
7. Move unstable operational status into execution-layer docs or machine artifacts.
8. Freeze read/write rules in `HARNESS.md`.
9. Add `KERNEL.md` if local operating patterns need a stable evolution layer.
10. Make daily loops read only the hot owner docs, local kernel, and machine truth.

## Anti-Patterns

Do not:

- create multiple docs that answer the same question
- let project status live inside strategy docs
- let machine truth be explained only in prose
- turn daily loops into free-form exploration
- keep adding narrative docs when tables would be clearer
- allow agents to "figure it out live" every day instead of following the harness
- trust existing docs without auditing whether they fit the protocol
- refuse to create docs until all ambiguities are solved

## Output Pattern

When using this skill, prefer output in this order:

- Current doc stack
- Duplicated truths
- Proposed owner docs
- Read/write protocol
- Migration sequence
- Remaining ambiguities
