# Contributing

[简体中文](CONTRIBUTING.zh-CN.md)

Contributions are welcome when they make open-ended exploration more observable, reproducible or genuinely less repetitive.

## Useful contributions

- A real exploration trajectory with private data removed.
- A failure case that the current protocol does not capture.
- A cross-model or human/AI/co-exploration comparison.
- A language adaptation that preserves the method rather than translating words mechanically.
- A small tool that improves trail capture, provenance or post-run evaluation.

## Before opening a pull request

1. Keep the main `SKILL.md` concise; move detail into `references/`.
2. Do not add a fixed topic-discovery template or force every session to produce a publishable result.
3. Mark synthetic examples clearly.
4. Remove credentials, private browsing history and personally identifying information.
5. Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_trajectory.py benchmark/sample-trajectory.json --strict
```

## Trajectory submissions

Use the exploration-case issue template first. Explain the seed, budget, checkpoint cadence, human interventions, unexpected transitions and where the run repeated or converged too early.

## Pull requests

Prefer one conceptual change per pull request. State what behavior changes, what failure mode it addresses and how you tested it.
