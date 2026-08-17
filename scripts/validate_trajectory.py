#!/usr/bin/env python3
"""Validate core CoExplore trajectory invariants without external packages."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

VALID_LANGUAGES = {"en", "zh-CN"}
VALID_MODES = {"guided", "relay", "timed", "comparison"}
VALID_ACTORS = {"human", "ai"}
VALID_LABELS = {"observation", "inference", "speculation"}


def parse_iso8601(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except (TypeError, ValueError):
        return False


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(data: Any, strict: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["top level must be a JSON object"]

    required = ["session_id", "language", "mode", "seed", "started_at", "budget", "participants", "steps", "checkpoints"]
    for key in required:
        if key not in data:
            errors.append(f"missing top-level field: {key}")

    if not nonempty_string(data.get("session_id")):
        errors.append("session_id must be a non-empty string")
    if data.get("language") not in VALID_LANGUAGES:
        errors.append(f"language must be one of {sorted(VALID_LANGUAGES)}")
    if data.get("mode") not in VALID_MODES:
        errors.append(f"mode must be one of {sorted(VALID_MODES)}")
    if not parse_iso8601(data.get("started_at")):
        errors.append("started_at must be an ISO-8601 datetime")
    if data.get("ended_at") is not None and not parse_iso8601(data.get("ended_at")):
        errors.append("ended_at must be null or an ISO-8601 datetime")

    seed = data.get("seed")
    if not isinstance(seed, dict):
        errors.append("seed must be an object")
    else:
        if not nonempty_string(seed.get("description")):
            errors.append("seed.description must be non-empty")
        if not nonempty_string(seed.get("selection_method")):
            errors.append("seed.selection_method must be non-empty")

    budget = data.get("budget")
    if not isinstance(budget, dict):
        errors.append("budget must be an object")
    else:
        if budget.get("type") not in {"steps", "minutes"}:
            errors.append("budget.type must be steps or minutes")
        if not isinstance(budget.get("value"), int) or budget.get("value", 0) < 1:
            errors.append("budget.value must be an integer >= 1")

    participants = data.get("participants")
    if not isinstance(participants, list) or not participants or any(p not in VALID_ACTORS for p in participants):
        errors.append("participants must be a non-empty list containing only human and/or ai")

    steps = data.get("steps")
    if not isinstance(steps, list):
        errors.append("steps must be a list")
        steps = []

    ids: list[int] = []
    for index, step in enumerate(steps, start=1):
        prefix = f"steps[{index - 1}]"
        if not isinstance(step, dict):
            errors.append(f"{prefix} must be an object")
            continue
        step_id = step.get("id")
        if not isinstance(step_id, int) or step_id < 1:
            errors.append(f"{prefix}.id must be an integer >= 1")
        else:
            ids.append(step_id)
        if not parse_iso8601(step.get("timestamp")):
            errors.append(f"{prefix}.timestamp must be ISO-8601")
        if step.get("actor") not in VALID_ACTORS:
            errors.append(f"{prefix}.actor must be human or ai")
        if step.get("label") not in VALID_LABELS:
            errors.append(f"{prefix}.label must be observation, inference or speculation")
        for field in ("source_type", "source_title", "observation"):
            if not nonempty_string(step.get(field)):
                errors.append(f"{prefix}.{field} must be non-empty")
        if not isinstance(step.get("uncertainty"), str):
            errors.append(f"{prefix}.uncertainty must be a string")
        if not isinstance(step.get("next_hop_reason"), str):
            errors.append(f"{prefix}.next_hop_reason must be a string")

        url = step.get("source_url")
        if url is not None:
            if not nonempty_string(url):
                errors.append(f"{prefix}.source_url must be null or non-empty")
            else:
                parsed = urlparse(url)
                if parsed.scheme not in {"http", "https", "file"}:
                    errors.append(f"{prefix}.source_url has unsupported scheme")
        if strict and url is None:
            errors.append(f"{prefix}.source_url is required in strict mode")
        if strict and not step.get("next_hop_reason", "").strip():
            errors.append(f"{prefix}.next_hop_reason is required in strict mode")

    if len(ids) != len(set(ids)):
        errors.append("step ids must be unique")
    if ids and ids != list(range(1, len(ids) + 1)):
        errors.append("step ids must be sequential starting at 1")

    checkpoints = data.get("checkpoints")
    if not isinstance(checkpoints, list):
        errors.append("checkpoints must be a list")
    else:
        for index, checkpoint in enumerate(checkpoints):
            prefix = f"checkpoints[{index}]"
            if not isinstance(checkpoint, dict):
                errors.append(f"{prefix} must be an object")
                continue
            if not isinstance(checkpoint.get("after_step"), int) or checkpoint.get("after_step", 0) < 1:
                errors.append(f"{prefix}.after_step must be an integer >= 1")
            for field in ("unfamiliar_observations", "warnings", "open_routes"):
                if not isinstance(checkpoint.get(field), list):
                    errors.append(f"{prefix}.{field} must be a list")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a CoExplore trajectory JSON file")
    parser.add_argument("path", type=Path)
    parser.add_argument("--strict", action="store_true", help="Require URL and next-hop reason for every step")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2

    errors = validate(data, strict=args.strict)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
