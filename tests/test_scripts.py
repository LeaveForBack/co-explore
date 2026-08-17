from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class CoExploreScriptsTest(unittest.TestCase):
    def test_sample_trajectory_validates_strictly(self) -> None:
        result = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "validate_trajectory.py"),
             str(REPO / "benchmark" / "sample-trajectory.json"), "--strict"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OK:", result.stdout)

    def test_new_session_creates_expected_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO / "scripts" / "new_session.py"),
                    "--lang", "zh-CN",
                    "--seed", "测试入口",
                    "--mode", "guided",
                    "--budget-type", "steps",
                    "--budget-value", "5",
                    "--output", tmp,
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            session_dir = Path(result.stdout.strip())
            for name in ("trajectory.json", "trail.md", "materials.csv", "retrospective.md"):
                self.assertTrue((session_dir / name).exists(), name)
            data = json.loads((session_dir / "trajectory.json").read_text(encoding="utf-8"))
            self.assertEqual(data["language"], "zh-CN")
            self.assertEqual(data["budget"], {"type": "steps", "value": 5})


if __name__ == "__main__":
    unittest.main()
