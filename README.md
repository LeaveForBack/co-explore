# CoExplore

[简体中文](README.zh-CN.md)

**Human–AI co-exploration beyond familiar information paths.**

Most AI research tools begin with a question and optimize for relevance. CoExplore begins with a concrete seed, keeps the route open, and lets human and AI interrupt each other's habits until they reach materials and questions neither would likely find alone.

> Search answers what you already know how to ask. CoExplore helps you discover what you never thought to ask.

## Who it is for

| You are… | Use CoExplore to… |
|---|---|
| Creator or independent researcher | Find unfamiliar materials and original questions |
| Founder, product or strategy practitioner | Explore non-obvious needs, users and opportunities |
| Cross-disciplinary researcher or learner | Leave familiar terminology, sources and citation paths |
| Agent builder | Study and evaluate open-ended human–AI exploration |
| Curious internet user | Recover purposeful serendipity without pure randomness |

**Not for:** direct factual lookup, exhaustive literature review, urgent troubleshooting, or high-stakes decisions. Use a search or deep-research workflow for those tasks.

## Core idea

**Local causality, global non-predetermination.**

Every hop must follow a concrete detail from the current material, but the final destination must not be chosen in advance.

Human and AI have different jobs:

- **AI** expands reach: browsing, translation, cross-domain movement, memory and trail recording.
- **Human** detects anomalies: “this is unfamiliar,” “you are repeating yourself,” “follow that detail,” or “drop this explanation.”

## How it works

1. **Set a budget, not a conclusion.** Choose time, steps and checkpoint cadence.
2. **Start from a concrete seed.** A page, object, phrase, community, image or event is enough.
3. **Follow material, not a preset topic.** Each next hop must be justified by something actually observed.
4. **Delay synthesis.** Record first; explain later. Do not force a topic during the trail.
5. **Review together.** At checkpoints, inspect repetition and choose where to continue.
6. **Reflect only at the end.** Map the route, question changes, discarded explanations and cognitive shifts.

## Quick start

This repository contains two installable Agent Skills. Install **one** language version.

### English

```bash
mkdir -p ~/.claude/skills
cp -R skills/co-explore ~/.claude/skills/
```

Invoke it explicitly:

```text
/co-explore Start from this page. Explore for 12 meaningful hops, check in every 4 hops, and do not form a topic early.
```

### Chinese

```bash
mkdir -p ~/.claude/skills
cp -R skills/co-explore-zh ~/.claude/skills/
```

Invoke it explicitly:

```text
/co-explore-zh 从这个页面出发，探索 12 次有效跳转，每 4 次做一次检查，不要过早形成主题。
```

For a project-only installation, copy the selected folder into `.claude/skills/` inside the project.

The packages use the portable `SKILL.md` structure and avoid vendor-specific runtime features. An agent works best when it can browse the web, but it can also explore a supplied folder or document collection.

## Outputs

A session should leave four artifacts:

- **Trail:** what was visited and why each hop happened.
- **Unfamiliar materials:** concrete details worth preserving before interpretation.
- **Question evolution:** how the initial framing changed or disappeared.
- **Retrospective:** what neither side would likely have sought alone, plus unresolved routes.

## Repository layout

```text
skills/       English and Chinese Agent Skills
examples/     Short, synthetic example sessions
benchmark/    Comparison protocol, trajectory schema and sample data
scripts/      Dependency-free session and validation utilities
tests/        Basic utility tests
```

## Optional session utilities

Create a session workspace:

```bash
python3 scripts/new_session.py \
  --lang en \
  --seed "A neighborhood repair-café event page" \
  --mode guided \
  --budget-type steps \
  --budget-value 12
```

Validate a trajectory:

```bash
python3 scripts/validate_trajectory.py benchmark/sample-trajectory.json --strict
```

## Evaluation

Do not optimize scores during exploration. Evaluate only after the trail ends.

Suggested dimensions include information-environment breadth, path coherence, semantic displacement, question emergence, explanation revision, joint discovery gain, provenance coverage and cross-run repetition. See [`benchmark/README.md`](benchmark/README.md).

## Important limits

CoExplore is a discovery protocol, not a truth engine. Preserve provenance, distinguish observation from inference, and verify important claims before publication or action. Never commit private browsing histories, credentials or sensitive personal information.

## Contributing

New failure cases, multilingual adaptations, trajectories and benchmark proposals are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

[MIT](LICENSE)
