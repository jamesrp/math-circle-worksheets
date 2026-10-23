#!/usr/bin/env python3
"""Rebuild Week 93 from its sources into a temporary folder and confirm the
delivered PDFs carry the same text (so the reviewed sources are the printed ones).

Run: python3 rebuild_compare.py > rebuild_compare.out
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from repo_path import SRC, WEEK  # noqa: E402

fail = 0
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    r = subprocess.run([sys.executable, str(SRC / "build.py"), "--out", str(tmp / "out"), "--work", str(tmp / "work")],
                       capture_output=True, text=True)
    print("build exit", r.returncode, r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-500:])
    fail |= r.returncode != 0
    for stem in ("students", "facilitator"):
        texts = []
        for pdf in (tmp / "out" / f"week-93-{stem}.pdf", WEEK / f"week-93-{stem}.pdf"):
            texts.append(subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout)
        same = texts[0] == texts[1] and texts[0].strip() != ""
        print(("PASS " if same else "FAIL ") + f"{stem}: rebuilt text identical to delivered PDF text")
        fail |= not same
print("FAILURES:", int(fail))
sys.exit(1 if fail else 0)
