# Kernel Protocol

Use this reference when adding or maintaining local project kernels and the global `project-os` kernel.

## Two kernels

| Kernel | Scope | Default owner | Auto-edit policy |
|---|---|---|---|
| Repo `KERNEL.md` | One project | Project loop / project lead | Candidate section only |
| `project-os/KERNEL.md` | Cross-project | `project-os` maintainer or promotion pass | Candidate section only, and only by cross-project synthesis |

## Repo `KERNEL.md` schema

| Section | Purpose |
|---|---|
| Stable patterns | Local rules that have already repeated enough inside the repo |
| Candidate patterns | New local lessons not yet promoted |
| Promotion upstream | Which local lessons may feed `project-os` |
| Rejected patterns | Local false friends |
| Update protocol | What the loop may and may not edit |

## Global `project-os` kernel schema

| Section | Purpose |
|---|---|
| Stable kernel | Cross-project rules that shape the skill |
| Candidate patterns | Cross-project rules not yet promoted |
| Promotion decisions | Accepted or rejected promotions |
| Rejected patterns | False universalizations |
| Update protocol | Guardrails against self-corruption |

## Promotion ladder

```text
single observation
-> repo candidate pattern
-> repo stable pattern
-> cross-project candidate
-> global stable kernel
-> SKILL.md / references
```

## Candidate updates

Default mutation path is protocol-first, not tool-first.

That means:

- update only `## Candidate Patterns`
- never let routine loops rewrite stable kernel sections
- if automation exists in a consuming repo, treat it as an implementation detail rather than part of the public `project-os` surface

## Promotion gate

Promote only when the pattern is:

- repeated
- entropy-reducing
- not repo-private language
- small enough to become a stable rule
- useful across more than one project before entering the global kernel
