# Skill routing

Which skill to reach for at each phase of ouvrance, and what to feed it.

Two invocation modes, and the difference decides who starts the skill:

- **Auto** — the skill fires on its own when the request matches its description. Nothing to do.
- **`/name`** — the skill never fires on its own. Propose it by name when the phase calls for it.

## 0. Chart — decide before building

The current phase. No code, no spec: a map of open decisions.

| Skill | When | Mode |
| --- | --- | --- |
| `/wayfinder` | Work larger than one session: build the decision map and its tickets on GitHub Issues (see `issue-tracker.md`) | `/` |
| `/grill-with-docs` | Sharpen one decision under interview, emitting ADRs and glossary entries as it resolves | `/` |
| `grilling` | Stress-test a plan with no doc output | auto |
| `research` | Settle a factual question against primary sources — fal.ai, Gemini, Stripe, R2, GDPR on likeness — landing as a Markdown file in the repo | auto |
| `domain-modeling` | A term or a decision hardens: write it into `CONTEXT.md` or `docs/adr/` (see `domain.md`) | auto |
| `/to-spec` | A conversation already holds the answer: publish it as a spec | `/` |
| `/to-tickets` | Break a spec into tracer-bullet tickets with their blocking edges | `/` |
| `/ask-matt` | Unsure which engineering skill fits | `/` |

## 1. Direct — voice and foundations

Runs once, before any screen exists. Its output is what every later phase consumes.

| Skill | When | Mode |
| --- | --- | --- |
| `brand` | ouvrance's voice: site copy, transactional emails, the tone a gift deserves | auto |
| `ui-ux-pro-max` | Palettes, type pairings, cinematic styles, UX guidelines — **before** the first line of CSS, not as a fix afterwards | auto |
| `design-system` | Turn that direction into three-layer tokens and component specs | auto |

## 2. Draw — screens and flows

| Skill | When | Mode |
| --- | --- | --- |
| `design` | Mockups and screen flows on a pan/zoom canvas, before committing to code | auto |
| `mobile-app-ui-design` | Every recipient-facing screen. The recipient opens the link on a phone, one-handed: thumb zone, 48 px targets, iOS/Android safe areas | auto |
| `impeccable` | Polish an existing interface: hierarchy, motion, accessibility, stripping AI-slop | auto |

## 3. Build

| Skill | When | Mode |
| --- | --- | --- |
| `prototype` | Throwaway code to answer a design question — does this state model for the 3D game or the personalisation flow hold up? Reach for it before committing to a shape | auto |
| `codebase-design` | Deep modules and where the seams go | auto |
| `tdd` | Feature or bugfix test-first | auto |
| `/implement` | Work off an existing spec or ticket set | `/` |
| `ui-styling` | shadcn/Tailwind implementation | auto |
| `run` | Launch the app and see the change working | auto |

## 4. Diagnose

| Skill | When | Mode |
| --- | --- | --- |
| `diagnosing-bugs` | The debug loop. Anything broken, throwing, flaky, or slow | auto |
| `gemini-video-understanding` | Hand a recording to Gemini: Playwright captures, cinematics, perceived framerate, animation timing | auto |
| `claude-in-chrome` | Drive the browser: console logs, screenshots, reproducing a report | auto |

## 5. Review

| Skill | When | Mode |
| --- | --- | --- |
| `/code-review` (mattpocock) | A branch or PR against repo standards **and** against what the originating issue asked for | `/` |
| `/code-review` (built-in) | Correctness bugs and cleanups in the current diff | `/` |
| `simplify` | Quality-only pass: reuse, altitude, dead weight | `/` |
| `security-review` | Anything touching uploads, payment links, or recipient data | `/` |
| `resolving-merge-conflicts` | A merge or rebase is mid-conflict | auto |

## 6. Ship and operate

| Skill | When | Mode |
| --- | --- | --- |
| `banner-design` | Site hero, ads, campaign visuals | auto |
| `slides` | A deck to present or pitch | auto |
| `dataviz` | Any chart or dashboard — production tracking, order funnel | auto |
| `wizard` | Steps only a human can perform: Stripe dashboard, DNS, CI secrets, a one-off cutover | auto |
| `/triage` | Move issues through the triage roles (see `triage-labels.md`) | `/` |
| `writing-for-agents` | Editing `AGENTS.md`, this file, or any skill | auto |

## The LLM-provider rule

`claude-api` covers Claude and the Anthropic SDK only. ouvrance generates through Gemini and fal.ai, so on generation work the applicable reference is `gemini-video-understanding` and the providers' own docs. `claude-api` applies only where the code actually calls Claude.
