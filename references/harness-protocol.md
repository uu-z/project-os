# Harness Protocol

Use this as the standard execution protocol after the doc stack is frozen.

The harness starts only after the document operating system has solved most of the project's ambiguity. In shorthand:

- `project-os` handles `0-90`
- the loop handles `90-100`

## Read Order

| Step | Source | Why |
|---|---|---|
| 1 | `STRATEGY.md` | confirm target and scope |
| 2 | `ARCHITECTURE.md` | confirm single-track system shape |
| 3 | `ENGINEERING.md` | confirm official commands and evidence rules |
| 4 | `PROJECT.md` | confirm stage and milestone context |
| 5 | `BLOCKERS.md` | confirm current priority |
| 6 | `HARNESS.md` | confirm loop protocol |
| 7 | machine truth | confirm real runtime state |

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
| Machine truth | never hand-edit; refresh through system actions |

Do not use the loop to rediscover missing strategy, ownership, or architecture. Fix those in the owner docs first.

## Main Agent Role

| Responsibility | Default owner |
|---|---|
| stage judgment | main agent |
| blocker prioritization | main agent |
| delegation | main agent |
| evidence collection integration | main agent |
| scope control | main agent |

## Subagent Role

| Responsibility | Default owner |
|---|---|
| bounded implementation | worker |
| targeted repo fact finding | explorer |
| validation and acceptance | verifier |

## Doctor

Run `doctor` when:

- the team sounds busy but progress is unclear
- more than one blocker is competing for attention
- current work no longer obviously moves the milestone
- execution has drifted back into strategy, naming, or side-quest work
- human and machine truth seem to be telling different stories

`doctor` should answer only:

1. what are we shipping now
2. what stage are we actually in
3. what milestone or deadline matters now
4. what is the one blocker
5. should current work continue or stop

## Align Sheet

If `doctor` finds drift, stop implementation and emit one align sheet before doing anything else.

Use this exact compact shape:

| Field | Meaning |
|---|---|
| Ship now | what this version is actually shipping now |
| Stage | current stage, not hoped-for stage |
| Milestone | current milestone and deadline lens |
| Progress | current red/yellow/green judgment |
| One blocker | the only blocker that matters right now |
| Do now | the one action that directly moves the milestone |

Alignment chain:

`strategy -> stage -> milestone -> progress -> blocker -> current action`

Only after the align sheet is clear should the team produce delegation, implementation, or verification detail.
