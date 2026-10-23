# Week 5 return-visit companion — review draft, unpiloted

These are **three new investigations**, separate from the base Week 5 packets and existing extras. No physical rehearsal or classroom piloting is claimed. The student packet is shared Grades 2–5, with genuine younger entries/readiness limits described in the adult guide.

**Check-sweep fix, October 23, 2026 (F05-RV-FAC-v2).** One sentence of the adult guide's order-3 impossibility argument (page 3) said the bottom corners are forced to be "b, a"; with the top corners a, b, the diagonals force the bottom corners to be a, b. It now says so and ends at the contradiction this gives at once (the left column holds a twice), as the math check suggested; the longer middle-column step is gone. The student PDF is unchanged. The previous guide and ZIP are in the `archive-before-check-sweep-fix-2026-10-23/` folders beside the current copies. Checked by `plans/review/checks/week-05/check_return_visit.py`. Unpiloted.

- Current student PDF: `../../week-05/week-05-return-visit.pdf`.
- Adult guide: `../../week-05/week-05-return-visit-facilitator.pdf`.
- Reference PDFs: `reference-pdfs/` (the same local deliverables for comparing a rebuild).
- Student editable source: `student-src/return-visit.tex`.
- Adult editable source: `guide-src/facilitator.tex` and any included vector diagrams.

Print Letter, single-sided at 100% scale. Follow the guide's material/preparation instructions; printed compact sketches are records unless a page explicitly provides a working board. Choose one investigation for a visit and continue later according to interest/readiness.

## Portable build

Requires Python 3 for checks and pdfLaTeX with TikZ, Helvetica and Latin Modern (standard TeX Live/MacTeX). From any extracted directory:

```sh
sh build.sh /absolute/path/to/output-directory
```

The build writes only to the named output directory. With no argument it creates a temporary output directory and prints its path. `PDFLATEX` may name a compiler explicitly. Builds use a fixed PDF timestamp to support comparison. Source paths do not refer to this repository.

Optional independent checks, using only Python's standard library:

```sh
python3 verification/verify_kernels.py
python3 verification/verify_triangles.py
```

These finite checks cover the mathematical kernels of the five-week range and an independent Week 1 triangle-board enumeration. If present, `verification/verify_weekNN.py` checks the represented cases of this week and can be run with Python 3 in the same way. The student's own stage checks in `student-src/` check its actual examples. Review records and inventory are stored locally in `plans/encore-01-05/` and `plans/bonus-weeks-01-05.md`; those are not required to build.

Creation followed the worksheet writer → fresh adversarial critic → fresh independent math critic → fresh reviser workflow. The adult guide was a separate coordinator step and the workflow has not been validated with children. Local source package only; no remote upload/publication.
