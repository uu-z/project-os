# Harness Protocol

Use this as the standard execution protocol after the doc stack is frozen.

The harness starts only after the document operating system has solved most of the project's ambiguity. In shorthand:

- `project-os` handles `0-90`
- the loop handles `90-100`

Default loop mode is autopilot. The user should not have to manually nominate the next obvious step.

## Read Order

| Step | Source | Why |
|---|---|---|
| 1 | repo `KERNEL.md` when present | confirm local operating lessons |
| 2 | `STRATEGY.md` | confirm target and scope |
| 3 | `ARCHITECTURE.md` | confirm single-track system shape |
| 4 | `ENGINEERING.md` | confirm official commands and evidence rules |
| 5 | `PROJECT.md` | confirm stage and milestone context |
| 6 | `BLOCKERS.md` | confirm current priority |
| 7 | `HARNESS.md` | confirm loop protocol |
| 8 | machine truth | confirm real runtime state |

`CONTEXT.md` is not part of the default hot loop. Re-read it only when:

- terminology is ambiguous
- a boundary or ownership question is fuzzy
- a protocol term is being used inconsistently
- an agent is likely to invent synonyms or drift from canonical language

## Write Rules

| Target | Default behavior |
|---|---|
| Decision-layer docs | change rarely |
| Execution-layer docs | update during loops |
| Repo `KERNEL.md` stable sections | change rarely |
| Repo `KERNEL.md` candidate section | update only on repeated local learning |
| Machine truth | never hand-edit; refresh through system actions |

Do not use the loop to rediscover missing strategy, ownership, or architecture. Fix those in the owner docs first.
Do not use the loop to write directly into the global skill surface. Promote through kernels.

## Main Agent Role

| Responsibility | Default owner |
|---|---|
| stage judgment | main agent |
| blocker prioritization | main agent |
| delegation | main agent |
| evidence collection integration | main agent |
| scope control | main agent |

Default rules:

- the main agent is not the default implementer
- the main agent should code only when doing it locally is obviously faster and does not damage project-level attention
- the main agent should repair the document control plane first, then delegate the final `90-100` implementation loop
- the main agent should keep the autopilot loop advancing unless a real decision fork requires escalation

## Subagent Role

| Responsibility | Default owner |
|---|---|
| bounded implementation | worker |
| targeted repo fact finding | explorer |
| validation and acceptance | verifier |

## Loop Output

Use this exact compact shape:

| Field | Meaning |
|---|---|
| Objective | current one-sentence goal |
| Stage | current stage |
| Primary blocker | top blocker for this cycle |
| Delegation plan | who does what |
| Evidence collected | what changed reality |
| Decision needed | what needs escalation |
| Next 24h | single primary outcome |

## Autopilot Goal Selection

Choose the active goal in this order:

1. explicit user outcome
2. highest-priority unresolved blocker
3. highest-value missing `0-90` control-plane gap
4. smallest credible `90-100` blocker-clearing action

The loop should not ask the user to choose among these unless there is a material tradeoff.
