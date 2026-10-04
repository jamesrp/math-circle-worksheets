# Polygon triangulations facilitator guide

Draft and unpiloted. Week 14 is an unscheduled library slot.

- Output: `../facilitator-guide.pdf` (12 US Letter pages).
- Editable content: `build_guide.py`, generated `facilitator-guide.tex`.
- Rebuild: `bash build.sh` from this directory or by full path.
- Independent mathematics: `verify.py`, `checks.json`, `verification.log`. Root-edge recursion independently enumerates all triangulations through 8 corners; BFS checks all final route instances and all fan distances through 8 corners. The code does not import worksheet builders or previous checks.
- Coverage: all 20 final numbered problems. The final middle packet has 8 pages, with Problem 7 continued on page 8; routes are Problem 6, not the draft Problem 7.
- Catalogs: five pentagon fillings, all fourteen hexagon fillings grouped by the root-edge triangle, all six one-flip results of the two printed hexagon starts, and every fixed-line completion.
- Visual QA: all 12 pages rendered at 90 dpi and inspected individually on 2026-10-03. Pages 6 and 12 re-inspected after final edits. No clipping, overlap, missing glyph, or overflow found. Build log has no overfull/underfull/missing-character warnings.
- Source fidelity and mathematical restrictions are printed on pages 10 and 12. Student PDFs and their sources were not edited.

Final student PDF SHA256 values used for this guide:
- k-1.pdf: 592ca60f337bbd64b4b8511f4e519b9a5035c4830400413deac9dadd1f7a2872
- grades-2-3.pdf: f7cf7b5a98514af768618920625903edda6b890ced4413fddb29437e15a03a71
- grades-4-5.pdf: 1c455abd493248984efc019dd326633e0e02f04aab8a2ac4e1ef095464699637
