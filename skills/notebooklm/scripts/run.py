#!/usr/bin/env python3
"""
Lightweight runner for NotebookLM scripts.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/run.py <script.py> [args...]")
        sys.exit(1)

    scripts_dir = Path(__file__).resolve().parent
    target_script = scripts_dir / sys.argv[1]
    if not target_script.exists():
        print(f"Script not found: {target_script}")
        sys.exit(1)

    cmd = [sys.executable, str(target_script), *sys.argv[2:]]
    env = dict(os.environ)
    env["PYTHONUNBUFFERED"] = "1"
    result = subprocess.run(cmd, env=env, check=False)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
