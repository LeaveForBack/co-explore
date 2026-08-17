# Utility scripts

Both scripts use only the Python standard library.

## Create a session

```bash
python3 scripts/new_session.py \
  --lang en \
  --seed "A concrete starting page or object" \
  --mode guided \
  --budget-type steps \
  --budget-value 12
```

The command creates a folder containing `trajectory.json`, `trail.md`, `materials.csv` and `retrospective.md`.

## Validate a trajectory

```bash
python3 scripts/validate_trajectory.py path/to/trajectory.json
python3 scripts/validate_trajectory.py path/to/trajectory.json --strict
```

Strict mode requires a source URL and non-empty next-hop reason for every step. Use non-strict mode for local or offline materials that do not have URLs.
