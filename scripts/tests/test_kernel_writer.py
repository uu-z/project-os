#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "kernel_writer.py"


SAMPLE_KERNEL = textwrap.dedent(
    """\
    # Sample Kernel

    ## Candidate Patterns

    Only this table is auto-editable.

    | pattern_id | first_seen | last_seen | loop_count | symptom | proposed_rule | evidence | status |
    |---|---|---|---:|---|---|---|---|
    | `pending` | `-` | `-` | `0` | `-` | `-` | `-` | `empty` |

    ## Next Section

    Keep me untouched.
    """
)


class KernelWriterTest(unittest.TestCase):
    def run_writer(self, kernel_path: Path, *args: str) -> str:
        completed = subprocess.run(
            ["python3", str(SCRIPT), "upsert", "--kernel", str(kernel_path), *args],
            check=True,
            text=True,
            capture_output=True,
        )
        return completed.stdout

    def test_upsert_replaces_placeholder_and_creates_row(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            kernel_path = Path(tmpdir) / "KERNEL.md"
            kernel_path.write_text(SAMPLE_KERNEL, encoding="utf-8")

            self.run_writer(
                kernel_path,
                "--pattern-id",
                "cand-001",
                "--date",
                "2026-06-10",
                "--set",
                "symptom=Team keeps recreating the same blocker board",
                "--set",
                "proposed_rule=Create one owner blocker document first",
                "--set",
                "evidence=repo-a",
                "--set",
                "status=candidate",
            )

            content = kernel_path.read_text(encoding="utf-8")
            self.assertIn("cand-001", content)
            self.assertNotIn("`pending`", content)
            self.assertIn("`2026-06-10`", content)
            self.assertIn("`1`", content)
            self.assertIn("## Next Section", content)

    def test_upsert_existing_row_increments_loop_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            kernel_path = Path(tmpdir) / "KERNEL.md"
            kernel_path.write_text(SAMPLE_KERNEL, encoding="utf-8")

            self.run_writer(
                kernel_path,
                "--pattern-id",
                "cand-001",
                "--date",
                "2026-06-10",
                "--set",
                "status=candidate",
            )
            self.run_writer(
                kernel_path,
                "--pattern-id",
                "cand-001",
                "--date",
                "2026-06-11",
                "--set",
                "evidence=repo-a loop-2",
            )

            content = kernel_path.read_text(encoding="utf-8")
            self.assertIn("| `cand-001` | `2026-06-10` | `2026-06-11` | `2` |", content)
            self.assertIn("repo-a loop-2", content)


if __name__ == "__main__":
    unittest.main()
