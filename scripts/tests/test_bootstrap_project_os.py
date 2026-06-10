#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "bootstrap_project_os.py"


class BootstrapProjectOsTest(unittest.TestCase):
    def run_bootstrap(self, target_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(SCRIPT), "--root", str(target_root), *args],
            check=True,
            text=True,
            capture_output=True,
        )

    def test_bootstrap_creates_minimal_stack(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "sample-repo"
            result = self.run_bootstrap(root, "--project-name", "Sample Project")

            expected_files = [
                "CONTEXT.md",
                "KERNEL.md",
                "STRATEGY.md",
                "ARCHITECTURE.md",
                "ENGINEERING.md",
                "PROJECT.md",
                "BLOCKERS.md",
                "HARNESS.md",
                "artifacts/current/README.md",
                ".project-os-bootstrap.json",
            ]
            for relative_path in expected_files:
                self.assertTrue((root / relative_path).exists(), relative_path)

            payload = json.loads((root / ".project-os-bootstrap.json").read_text(encoding="utf-8"))
            self.assertEqual(payload["artifact_kind"], "project-os-bootstrap-summary")
            self.assertIn("created: CONTEXT.md", result.stdout)

    def test_bootstrap_does_not_overwrite_without_flag(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "sample-repo"
            root.mkdir(parents=True, exist_ok=True)
            strategy = root / "STRATEGY.md"
            strategy.write_text("KEEP ME\n", encoding="utf-8")

            self.run_bootstrap(root, "--project-name", "Sample Project")
            self.assertEqual(strategy.read_text(encoding="utf-8"), "KEEP ME\n")


if __name__ == "__main__":
    unittest.main()
