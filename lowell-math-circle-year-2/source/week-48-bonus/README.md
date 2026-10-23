# Week 48 bonus: Inside and outside covers

**Guide v3, October 23, 2026.** The adult guide printed the roster code "KK11 / 3333 / 445" (K, K, 1, 1 / four third graders / 4, 4, 5); it now prints the band labels "K–1 / 2–3 / 4–5", and a lone "KK11", "3333" or "445" as the table it names. Footer W48-BONUS-FAC-v3; the student companion is unchanged. The previous guide and source ZIP are in the `archive-before-bonus-label-fix-2026-10-23/` folders beside the print copies and the ZIPs.

Local v1, October 4, 2026; v2, October 23, 2026, from the Week 48 review card's should 11: page 2's card pairs are numbered 1-3 and its witness grids are captioned "Pair: ____" instead of "First pair" and "Third pair", which answered "Which pair cannot be true?"; the adult guide says so (footers F48B-S-v2, W48-BONUS-FAC-v2). **Unpiloted. Physical fit and procedures untested.**

Three or more distinct investigations use selected bands by prerequisites. They complement, rather than replace, the base Week 48 packet. The student companion and adult mathematical guide are separate. Suitable routes, materials, launch, hints, precise solutions and extensions are in `guide.md`; investigation metadata is in `investigations.json`.

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

The coordinator verified an extracted-ZIP rebuild against the released PDFs by page text and rendered pixel hashes; check evidence and workflow review records are in `../../../plans/bonus-weeks-35-51/` in the repository. Writer, fresh adversarial/math review, and fresh revision stages are in `tmp/worksheet-runs/week-48-bonus-v1/`. The tested workflow is for student pages; the guide is a separate, untested authoring step. These sources are current locally only; no remote upload or publication is claimed.
