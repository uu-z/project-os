# project-os Kernel

`KERNEL.md` is the global evolution source of truth behind `project-os`.

It is not the same as:

- a repo's local `KERNEL.md`
- a repo's domain `CONTEXT.md`
- a repo's live owner-doc stack

## Layer model

| Layer | File | Owns |
|---|---|---|
| Global kernel | `project-os/KERNEL.md` | Cross-project operating rules that are stable enough to shape the skill |
| Project kernel | `<repo>/KERNEL.md` | Repo-specific operating patterns and local evolution candidates |
| Domain kernel | `<repo>/CONTEXT.md` | Canonical language, terms, boundaries, anti-synonym rules |
| Control plane | `STRATEGY / ARCHITECTURE / ENGINEERING / PROJECT / BLOCKERS / HARNESS` | The repo's `0-90` source of truth |
| Machine truth | `manifest.json` and similar artifacts | The repo's live runtime truth |

## Stable Kernel

| kernel_id | Rule | Why it is stable |
|---|---|---|
| `os-001` | Solve `0-90` in docs before spending loop effort on `90-100` implementation. | This is the main entropy-reduction law behind the system. |
| `os-002` | One important question should have one owner document and one update protocol. | Duplicate truth is the default source of drift. |
| `os-003` | `CONTEXT.md` and `KERNEL.md` are different things. | Language drift and operating drift are different failure classes. |
| `os-004` | Repo `KERNEL.md` is the local self-evolution layer; `project-os/KERNEL.md` is the cross-project self-evolution layer. | Local patterns should not jump straight into the global skill surface. |
| `os-005` | `SKILL.md` and `references/` are compiled execution surfaces, not direct auto-growth targets. | Direct self-editing of the skill causes self-corruption. |
| `os-006` | Only candidate sections are auto-editable by loops. Stable sections require promotion. | This keeps learning possible without destabilizing truth. |
| `os-007` | The main agent is not the default implementer. | Project-level attention is usually scarcer than coding capacity. |
| `os-008` | The main agent should code only when doing it locally is obviously faster and does not damage project-level attention. | This preserves throughput without losing command focus. |
| `os-009` | The main agent should fix the document control plane before delegating the final implementation loop. | Most recurring execution waste comes from unresolved `0-90` ambiguity, not missing code. |
| `os-010` | `project-os` should default to autopilot when the user does not supply a narrower sub-goal. | The user should not need to micromanage the next obvious loop step. |
| `os-011` | In autopilot, the system should derive one active goal from `KERNEL -> STRATEGY -> PROJECT -> BLOCKERS -> machine truth`. | This keeps execution aligned to frozen truth instead of chat drift. |

## Candidate Patterns

Use this section for cross-project candidates that have not yet earned promotion.

| pattern_id | source_repos | repeated_count | symptom | proposed_rule | evidence | status |
|---|---:|---:|---|---|---|---|
| `pending` | `0` | `0` | `-` | `-` | `-` | `empty` |

## Promotion Decisions

Use this section to record when a candidate becomes stable enough to shape the skill.

| promotion_id | promoted_from | decision | target_surface | note |
|---|---|---|---|---|
| `boot-001` | bootstrap | accepted | `KERNEL.md` | Initial project-os operating model established. |

## Rejected Patterns

Use this section to record tempting but false patterns.

| rejection_id | rejected_pattern | why rejected |
|---|---|---|
| `rej-001` | Let every project loop edit `SKILL.md` directly. | This destroys the boundary between local learning and global truth. |
| `rej-002` | Merge `CONTEXT.md` and `KERNEL.md` into one doc by default. | Language truth and operating truth drift at different rates. |

## Update Protocol

| Surface | Default write rule |
|---|---|
| Repo `KERNEL.md` candidate section | May be updated by repo loops when a repeated local pattern is observed. |
| `project-os/KERNEL.md` candidate section | May be updated only by cross-project synthesis or a promotion pass. |
| `project-os/KERNEL.md` stable section | Manual promotion only. |
| `SKILL.md` and `references/` | Change only after a promoted kernel rule is accepted. |
| Active goal selection | In autopilot mode, derive it from the hot truth stack rather than asking the user to choose every time. |

Writer:

```bash
python3 scripts/kernel_writer.py upsert --kernel /path/to/KERNEL.md --pattern-id <id> ...
```

## Evolution Pipeline

```text
repo execution loop
-> repo KERNEL.md
-> project-os KERNEL.md
-> SKILL.md / references
```
