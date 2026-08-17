#!/usr/bin/env python3
"""Create a CoExplore session workspace without third-party dependencies."""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Final

VALID_LANGUAGES: Final = ("en", "zh-CN")
VALID_MODES: Final = ("guided", "relay", "timed", "comparison")
VALID_BUDGET_TYPES: Final = ("steps", "minutes")


def slugify(value: str, limit: int = 48) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\u4e00-\u9fff]+", "-", value, flags=re.UNICODE)
    value = value.strip("-")
    return (value[:limit].rstrip("-") or "exploration")


def template_path(repo_root: Path, language: str, name: str) -> Path:
    skill = "co-explore" if language == "en" else "co-explore-zh"
    return repo_root / "skills" / skill / "templates" / name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a CoExplore session workspace")
    parser.add_argument("--lang", choices=VALID_LANGUAGES, default="en")
    parser.add_argument("--seed", required=True, help="Concrete starting material")
    parser.add_argument("--seed-url", default=None)
    parser.add_argument("--selection-method", default="Provided by the human")
    parser.add_argument("--mode", choices=VALID_MODES, default="guided")
    parser.add_argument("--budget-type", choices=VALID_BUDGET_TYPES, default="steps")
    parser.add_argument("--budget-value", type=int, default=12)
    parser.add_argument("--output", type=Path, default=Path("sessions"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.budget_value < 1:
        raise SystemExit("--budget-value must be at least 1")

    now = datetime.now(timezone.utc).replace(microsecond=0)
    session_id = f"{now.strftime('%Y%m%d-%H%M%S')}-{slugify(args.seed)}"
    session_dir = args.output / session_id
    session_dir.mkdir(parents=True, exist_ok=False)

    repo_root = Path(__file__).resolve().parents[1]
    metadata = {
        "session_id": session_id,
        "language": args.lang,
        "mode": args.mode,
        "seed": {
            "description": args.seed,
            "url": args.seed_url,
            "selection_method": args.selection_method,
        },
        "started_at": now.isoformat().replace("+00:00", "Z"),
        "ended_at": None,
        "budget": {"type": args.budget_type, "value": args.budget_value},
        "participants": ["human", "ai"],
        "non_goals": [],
        "steps": [],
        "checkpoints": [],
        "retrospective": None,
    }
    (session_dir / "trajectory.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    session_template = template_path(repo_root, args.lang, "session.md")
    retrospective_template = template_path(repo_root, args.lang, "retrospective.md")
    (session_dir / "trail.md").write_text(session_template.read_text(encoding="utf-8"), encoding="utf-8")
    (session_dir / "retrospective.md").write_text(
        retrospective_template.read_text(encoding="utf-8"), encoding="utf-8"
    )

    with (session_dir / "materials.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "step", "timestamp", "actor", "source_type", "source_title", "source_url",
            "observation", "unfamiliar_detail", "label", "uncertainty", "next_hop_reason"
        ])

    print(session_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
