# ouvrance

## Agent skills

### Issue tracker

Issues are tracked as GitHub issues, managed via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

The five canonical triage roles, used verbatim as label strings. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.

### Skill routing

Which skill to reach for at each phase, and whether it fires on its own or waits to be named. See `docs/agents/skills.md`.

| Phase | Reach for |
| --- | --- |
| **Chart** — decide before building | `/wayfinder`, `/grill-with-docs`, `grilling`, `research`, `domain-modeling`, `/to-spec`, `/to-tickets` |
| **Direct** — voice and foundations | `brand`, `ui-ux-pro-max`, `design-system` |
| **Draw** — screens and flows | `design`, `mobile-app-ui-design`, `impeccable` |
| **Build** | `prototype`, `codebase-design`, `tdd`, `/implement`, `ui-styling`, `run` |
| **Diagnose** | `diagnosing-bugs`, `gemini-video-understanding`, `claude-in-chrome` |
| **Review** | `/code-review`, `simplify`, `security-review`, `resolving-merge-conflicts` |
| **Ship and operate** | `banner-design`, `slides`, `dataviz`, `wizard`, `/triage`, `writing-for-agents` |

A `/name` entry never fires on its own — propose it by name when its phase comes up.
