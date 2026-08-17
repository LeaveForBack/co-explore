.PHONY: test validate-sample

test:
	python3 -m unittest discover -s tests -v

validate-sample:
	python3 scripts/validate_trajectory.py benchmark/sample-trajectory.json --strict
