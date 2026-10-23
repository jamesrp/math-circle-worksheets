# Week 49 bonus: Four-tower differences

Local v1, October 4, 2026; v2, October 23, 2026, from the Week 49 review card's could 11: page 3's Problem 3 asks about "by round 5" instead of "within five rounds", which a child filling rows 0-4 could read as excluding round 5, and the adult guide matches (footers F49B-S-v2, W49-BONUS-FAC-v2). The page headers keep their per-page levels (Grades 2-5, then 4-5), as `investigations.json` and the guide assign them. **Unpiloted. Physical fit and procedures untested.**

Three or more distinct investigations use selected bands by prerequisites. They complement, rather than replace, the base Week 49 packet. The student companion and adult mathematical guide are separate. Suitable routes, materials, launch, hints, precise solutions and extensions are in `guide.md`; investigation metadata is in `investigations.json`.

Print PDFs at 100% / Actual Size on US Letter, single-sided. Use only pages appropriate to the group's readiness and return for further work; finishing a packet in one hour is not expected.

## Clean standalone rebuild

Extract the source ZIP into any new directory, enter this folder, and run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build.py --out output
.venv/bin/python student/verify.py
```

Python3 and ReportLab are required. Fonts and their license are bundled. No repository checkout, external paths, network content fetch, or images generated elsewhere are required after dependency installation. `student/` contains editable page text, diagrams and the student builder. `guide.md` and `guide_renderer.py` contain the editable adult guide and its builder. `build.py` generates both PDFs in the chosen output directory and leaves all base packets untouched.

The coordinator verified an extracted-ZIP rebuild against the released PDFs by page text and rendered pixel hashes; check evidence and workflow review records are in `../../../plans/bonus-weeks-35-51/` in the repository. Writer, fresh adversarial/math review, and fresh revision stages are in `tmp/worksheet-runs/week-49-bonus-v1/`. The tested workflow is for student pages; the guide is a separate, untested authoring step. These sources are current locally only; no remote upload or publication is claimed.
