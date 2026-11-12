"""news-summary-01 entry: write the bundled summary to the output file.

Standard library only, no network. The summary is fixed text, so every run
writes the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
# Byte-exact copy: the output is identical on every run by construction.
(OUT_DIR / "entry.txt").write_bytes((HERE / "summary.txt").read_bytes())
