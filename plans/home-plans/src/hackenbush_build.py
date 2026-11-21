#!/usr/bin/env python3
"""Rebuild plans/home-plans/2026-11-21-hackenbush.pdf: the plan's pages, then the positions page.

    python3 plans/home-plans/src/hackenbush_build.py

Runs the checker, draws the positions page (reportlab), builds the plan with the
room plans' builder (pandoc and LibreOffice), and appends the positions page with
pdfunite (poppler). Run from the repository root.
"""
import pathlib, shutil, subprocess, sys, tempfile

SRC = pathlib.Path(__file__).resolve().parent
HOME = SRC.parent
ROOT = HOME.parent.parent
plan = HOME / "2026-11-21-hackenbush.md"
subprocess.run([sys.executable, str(SRC / "hackenbush_check.py")], check=True, stdout=subprocess.DEVNULL)
subprocess.run([sys.executable, str(SRC / "hackenbush_positions.py")], check=True)
subprocess.run([sys.executable, str(ROOT / "plans/room-plans/build/build.py"), str(plan)], check=True)
with tempfile.TemporaryDirectory() as tmp:
    joined = pathlib.Path(tmp) / "joined.pdf"
    subprocess.run(["pdfunite", str(plan.with_suffix(".pdf")),
                    str(HOME / "2026-11-21-hackenbush-positions.pdf"), str(joined)], check=True)
    shutil.copy(joined, plan.with_suffix(".pdf"))
print("appended the positions page to", plan.with_suffix(".pdf"))
