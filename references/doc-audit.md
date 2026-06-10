# Doc Audit

Use this reference when a repo already has documentation and you need to decide whether it can be reused or must be restructured.

## Audit Questions

| Dimension | Audit question | Action if failed |
|---|---|---|
| Owner question | Does this doc answer one clear question? | split, merge, or demote |
| Layer | Is this doc clearly decision, execution, or machine-adjacent? | move or relabel |
| Duplication | Is the same fact defined elsewhere? | pick one owner doc and reference it |
| Stability | Is the truth stable enough for this layer? | move unstable truth downward |
| Structure | Is prose hiding what should be a table? | convert to structured format |
| Loop fit | Should daily loops read it, write it, or ignore it? | assign explicit loop role |

## `KERNEL.md` Test

When a repo has a `KERNEL.md`, ask:

| Question | Good sign | Bad sign |
|---|---|---|
| Is it storing repo-specific operating lessons instead of generic strategy prose? | repeated local rules, promotion candidates, write protocol | duplicate goals, duplicate milestones, duplicate blocker board |
| Is only the candidate section auto-growable? | yes | no; the whole doc mutates freely |
| Does it feed the global skill through promotion instead of bypassing it? | yes | repo loop edits `SKILL.md` directly |

## 0-90 Test

Use this forcing question during audits:

| Question | If yes | If no |
|---|---|---|
| Should this ambiguity be solved before implementation starts? | move it into the owner docs and treat it as `0-90` work | keep it in the execution loop as `90-100` work |

If the team is repeatedly re-deciding the same scope, stage, blocker, or ownership question during implementation, the document operating system is still incomplete.

## Reuse Rule

Reuse an existing doc only when:

- it already owns the right question
- it does not duplicate another owner doc
- it is mostly structurally compatible

Otherwise:

- rename
- split
- merge
- or demote it to a cold reference

## `CONTEXT.md` Test

When a repo has a `CONTEXT.md`, ask:

| Question | Good sign | Bad sign |
|---|---|---|
| Is it acting as a domain kernel instead of a project tracker? | glossary, boundaries, invariants, avoid-language | milestones, blockers, day-by-day execution notes |
| Does the daily loop need it every time? | no; read on ambiguity | yes; because other owner docs are underspecified |

## Grill-With-Docs Use

Use a `grill-with-docs` style pass when:

- terminology conflicts across docs
- stage names mean different things in different places
- code disagrees with docs
- ownership of a fact is unclear
- the right owner doc cannot be chosen from source alone
