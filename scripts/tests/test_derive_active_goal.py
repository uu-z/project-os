#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BOOTSTRAP = ROOT / "scripts" / "bootstrap_project_os.py"
DERIVE = ROOT / "scripts" / "derive_active_goal.py"


class DeriveActiveGoalTest(unittest.TestCase):
    def bootstrap_repo(self, root: Path) -> None:
        subprocess.run(
            ["python3", str(BOOTSTRAP), "--root", str(root), "--project-name", "Sample Repo"],
            check=True,
            text=True,
            capture_output=True,
        )

    def derive_json(self, root: Path) -> dict[str, object]:
        completed = subprocess.run(
            ["python3", str(DERIVE), "--root", str(root), "--json"],
            check=True,
            text=True,
            capture_output=True,
        )
        return json.loads(completed.stdout)

    def test_prefers_concrete_p0_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            self.bootstrap_repo(root)
            blockers = root / "BLOCKERS.md"
            blockers.write_text(
                blockers.read_text(encoding="utf-8").replace(
                    "| `pending` | Fill with the first real blocker. | `pending` | `pending` | `pending` | `pending` |",
                    "| Real launch blocker | Launch still fails on wallet proof. | main agent | browser proof | produce browser proof | open |",
                ),
                encoding="utf-8",
            )

            payload = self.derive_json(root)
            self.assertEqual(payload["mode"], "blocker-driven")
            self.assertIn("Real launch blocker", payload["active_goal"])

    def test_falls_back_to_control_plane_freeze(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            self.bootstrap_repo(root)

            payload = self.derive_json(root)
            self.assertEqual(payload["mode"], "control-plane-freeze")
            self.assertIn("Freeze the missing 0-90 control-plane truth", payload["active_goal"])

    def test_supports_nested_docs_actum_layout(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            self.bootstrap_repo(root)
            actum_dir = root / "docs" / "actum"
            actum_dir.mkdir(parents=True, exist_ok=True)
            for name in ["STRATEGY.md", "PROJECT.md", "BLOCKERS.md", "HARNESS.md"]:
                source = root / name
                target = actum_dir / name
                target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
                source.unlink()

            blockers = actum_dir / "BLOCKERS.md"
            blockers.write_text(
                blockers.read_text(encoding="utf-8").replace(
                    "| `pending` | Fill with the first real blocker. | `pending` | `pending` | `pending` | `pending` |",
                    "| Real nested blocker | Launch still fails on wallet proof. | main agent | browser proof | produce browser proof | open |",
                ),
                encoding="utf-8",
            )

            payload = self.derive_json(root)
            self.assertEqual(payload["mode"], "blocker-driven")
            self.assertIn("Real nested blocker", payload["active_goal"])


if __name__ == "__main__":
    unittest.main()
