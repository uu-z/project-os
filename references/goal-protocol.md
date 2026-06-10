# Goal Protocol

Use this reference when coupling `project-os` to an active goal and a repeating execution loop.

## Model

| Layer | Purpose |
|---|---|
| `project-os` control plane | Defines what is correct and where truth lives |
| Active goal | Defines what this loop is trying to finish next |
| Execution loop | Moves one blocker or closes one control-plane gap |
| Write-back | Strengthens the repo control plane and kernels |

## Core rule

The active goal is a fast-variable execution contract derived from a slow-variable control plane.

That means:

- goals should be derived from frozen truth
- goals should not redefine frozen truth mid-loop
- goal runs should strengthen the repo truth stack
- repeated repo learnings may later strengthen `project-os`

## Goal derivation order

1. explicit user outcome
2. repo `KERNEL.md`
3. `STRATEGY.md`
4. `PROJECT.md`
5. `BLOCKERS.md`
6. machine truth

## Goal quality bar

A good active goal is:

- singular
- blocker-shaped
- traceable to the truth stack
- small enough to finish or decisively move in one loop
- strong enough to improve project reality, not just chat clarity

## One-goal rule

Default to one active goal and one primary blocker.

Only break this when:

- the work naturally splits into disjoint subagent slices
- one local step can proceed while another verifies in parallel
- the main agent still preserves a single integrated objective

## Goal write-back

If a goal loop changes reality, it should normally write back to:

- `BLOCKERS.md`
- `PROJECT.md`
- repo `KERNEL.md` candidate section when the same lesson repeated

If a goal loop reveals a cross-project pattern:

- promote first to `project-os/KERNEL.md`
- only later, if stable enough, to `SKILL.md` or `references/`

## Anti-patterns

Do not:

- let the goal drift away from the truth stack
- let the goal expand scope because the loop found something interesting
- let the goal bypass repo `KERNEL.md` and edit global skill truth directly
- let a finished goal disappear without write-back
