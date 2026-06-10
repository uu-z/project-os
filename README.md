# project-os

`project-os` is a document-first operating system for projects.

Its job is to solve the first `0-90` in documents so the last `90-100` can be executed by workers without reopening strategy every day.

## One sentence

One project, one control plane, one harness loop.

## Philosophy

`project-os` exists to reduce entropy with elegant minimalism.

That means:

- fewer surfaces, not more surfaces
- stronger owner docs, not more explanatory docs
- one clear rule that explains many cases
- direct movement toward the end state, not transitional complexity

Failure tests:

- if a change increases explanation cost, it is probably not elegant
- if a change adds a new layer without deleting an old one, it is probably not minimal
- if a change hides entropy instead of removing it, it is probably not progress

## What it is

| Layer | Truth |
|---|---|
| Domain | `CONTEXT.md` |
| Local operating kernel | repo `KERNEL.md` |
| Decision layer | `STRATEGY.md`, `ARCHITECTURE.md`, `ENGINEERING.md` |
| Execution layer | `PROJECT.md`, `BLOCKERS.md`, `HARNESS.md` |
| Machine layer | runtime-owned manifests and artifacts |

## What it is not

- not a script framework
- not a repo-owned PM bot
- not a second machine-truth system
- not a replacement for the main agent's stage judgment

## Default operating model

| Role | Default responsibility |
|---|---|
| Main agent | PM + Architect + Control Tower |
| Worker subagent | bounded implementation |
| Explorer subagent | targeted fact finding |
| Verifier subagent | acceptance and regression |

Core rule:

- main agent stays in `0-90` and control-tower work
- subagents handle `90-100`
- main agent codes only when local implementation is obviously faster and does not damage project-level attention

The control-tower loop means the main agent keeps locking five things:

1. stage: what is shipping now
2. boundary: single-track architecture, single entrypoint, single truth source
3. blocker: exactly one primary blocker
4. cadence: implement, verify, write back, upgrade
5. deadline: whether the action directly moves the current milestone

If the main agent codes too often, the first things usually lost are stage judgment, scope control, and deadline control.

## Standard doc stack

| File | Owns |
|---|---|
| `STRATEGY.md` | why this project exists now, scope, success, non-goals |
| `ARCHITECTURE.md` | single-track shape, boundaries, truth sources |
| `ENGINEERING.md` | official commands, evidence rules, artifact meanings |
| `PROJECT.md` | stage, milestones, owners, deadlines |
| `BLOCKERS.md` | primary blocker, supporting blockers, evidence needed |
| `HARNESS.md` | read order, write order, delegation, escalation |

Optional base docs:

| File | Owns |
|---|---|
| `CONTEXT.md` | domain language and anti-synonym rules |
| `KERNEL.md` | local operating patterns and promotion candidates |

## Harness loop

Read order:

1. `KERNEL.md`
2. `STRATEGY.md`
3. `ARCHITECTURE.md`
4. `ENGINEERING.md`
5. `PROJECT.md`
6. `BLOCKERS.md`
7. `HARNESS.md`
8. machine truth

Write-back order:

1. refresh machine truth through the real system path
2. update `BLOCKERS.md`
3. update `PROJECT.md`
4. update repo `KERNEL.md` only when a lesson repeats
5. touch decision docs only when a real decision changed

## Align surface

When the project feels noisy or drifted, stop implementation and collapse status into one align sheet:

1. `Ship now`
2. `Stage`
3. `Milestone`
4. `Progress`
5. `One blocker`
6. `Do now`

This is the human alignment surface for strategy, project state, progress, and execution.
If a task does not clearly attach to that chain, it is probably noise.

## Autopilot meaning

`autopilot` here is a protocol, not a script.

It means the main agent should normally:

1. derive one active goal from the truth stack
2. keep exactly one primary blocker
3. decide whether the blocker is `0-90` or `90-100`
4. repair the control plane first if the problem is still `0-90`
5. delegate the last-mile implementation if the problem is `90-100`
6. write reality back into the owner docs

The active loop should always answer one question before acting:

- does this directly move the current milestone or deadline

## Evolution model

```text
repo loop
-> repo KERNEL.md
-> project-os KERNEL.md
-> SKILL.md / references
```

Rules:

- local learnings do not jump straight into `SKILL.md`
- only repeated cross-project patterns reach the global kernel
- `SKILL.md` is a compiled operating surface, not an auto-growth target
- if a new surface appears, some older surface should usually disappear

## Repository layout

```text
.
├── KERNEL.md
├── README.md
├── SKILL.md
├── references/
│   ├── doc-audit.md
│   ├── doc-templates.md
│   ├── goal-protocol.md
│   ├── harness-protocol.md
│   └── kernel-protocol.md
└── agents/
    └── openai.yaml
```

## Use project-os when

- the team keeps thinking while doing
- stage and milestone language drift every day
- blockers are plural and vague
- multiple docs answer the same question
- the main agent needs to stay in PM and architecture mode instead of coding-first mode
