# CoExplore benchmark

[简体中文](README.zh-CN.md)

The benchmark asks a narrow question:

> Does human–AI co-exploration reach justified information paths that human-only and AI-only exploration both miss?

## Three-arm design

Run three independent sessions with the same seed, budget, tool access and source restrictions:

1. **Human only**
2. **AI only**
3. **Human + AI with CoExplore**

Do not share trails between arms until all sessions end.

## Minimum record

Each arm must preserve:

- seed and seed-selection method;
- time or hop budget;
- every meaningful hop and its causal bridge;
- source title, URL and type;
- human interventions;
- abandoned branches;
- end-of-run retrospective.

Use [`trajectory.schema.json`](trajectory.schema.json) for machine-readable records.

## Evaluation dimensions

- information-environment breadth;
- path coherence;
- semantic displacement;
- question emergence;
- explanation revision;
- joint discovery gain;
- provenance coverage;
- cross-run repetition.

Use the rubric in each skill's `references/evaluation.md`.

## What not to claim

This benchmark does not prove that a user has permanently escaped an information bubble. It measures one session's route, novelty relative to comparison arms, and whether the movement was grounded rather than random.

## Suggested experiment report

```text
Seed:
Budget and tools:
Participants / model:
Arm summaries:
Route overlap:
Unique sources by arm:
Question changes:
Human interventions with measurable route effects:
Failure modes:
Joint discovery gain:
Limitations:
```
