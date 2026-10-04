# Portable current bonus source (v1)

Requires Python 3.10+ and ReportLab (`python3 -m pip install reportlab`).

Run `python3 build.py --out /path/to/scratch-output` from any directory. It writes only `bonus.pdf` into that output directory; default is the parent of this source directory. `python3 verify.py` uses the standard library and recomputes the mathematical checks. The builder has no repository imports or required external fonts. ReportLab invariant output is enabled.

For digital rendering, optionally install PyMuPDF and run `python3 render.py --pdf /path/to/bonus.pdf --out /path/to/pngs`. Print at 100% on US Letter. The selected-band student companion has three pages, one investigation per page. All materials are unpiloted and physical pretests remain unperformed. Adult notes are separate from the tested student-generation workflow.

Optional physical-map preparation: `python3 materials.py --out /path/to/scratch` builds `portal-copies.pdf`, four separate 3-by-3 boards on one Letter sheet at 27.5 mm cells. Print three sheets per pair at 100%, cut the outer board borders, and tile aligned copies as needed. This is supporting material, not a fourth investigation. Cutting and seam handling remain physically untested.
