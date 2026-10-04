# Week 40 bonus: Loop colors

Local v1, October 4, 2026. **Unpiloted. Physical fit and procedures untested.**

Three or more distinct investigations use selected bands by prerequisites. They complement, rather than replace, the base Week 40 packet. The student companion and adult mathematical guide are separate. Suitable routes, materials, launch, hints, precise solutions and extensions are in `guide.md`; investigation metadata is in `investigations.json`.

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

The coordinator verified an extracted-ZIP rebuild against the released PDFs by page text and rendered pixel hashes; check evidence and workflow review records are in `../../../plans/bonus-weeks-35-51/` in the repository. Writer, fresh adversarial/math review, and fresh revision stages are in `tmp/worksheet-runs/week-40-bonus-v1/`. The tested workflow is for student pages; the guide is a separate, untested authoring step. These sources are current locally only; no remote upload or publication is claimed.
