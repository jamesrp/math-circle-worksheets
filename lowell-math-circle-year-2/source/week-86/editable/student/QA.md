# Week 86 revision QA

Status: revised student packet, digitally checked; unpiloted. No facilitator guide edited.

## Review resolution

| Review item | Final resolution |
|---|---|
| Printed folds cannot be erased through a sleeve | Upper p4 now requires removable opaque covers; original remains visible. Materials p3 names opaque paper/card rectangles, narrow strips, scissors and removable tape, with trimming around surviving dots/roads. |
| Design roads pass through collinear dots | Upper p3 D1/D2 each use six regular-hexagon vertices, no three collinear; 22 mm dots, 32 mm nearest centers. Six-dot/six-road depth retained. |
| Q6 free placement gives immediate capture | Upper p5 starts both cops at a. Exact finite-horizon check gives three cop turns in the worst case. Q8/every-ring task retained. |
| Optimization measure | Both p1 tasks say fewest C turns. |
| Fold procedure duplication | Handling instruction integrated into Problem 4; current-map comparison rule stated once in opening fold guidance. |
| Cop co-location | Materials p3 says to stack cops sharing a dot. |

## Delivered-output evidence

Rendered and visually inspected all 13 final pages: shared 1–4, upper 1–6, materials 1–3. No clipped text, unwanted overlap, missing edges, or footer collisions found. The two non-task worked sequences remain intact. Upper fold comparison uses unchanged input; output removes exactly w and its road.

`../qa/check_pdf_graphs.py` extracts actual final PDF vectors and labels. It checks all 29 graph instances against expected vertices/roads; all working diameters; minimum center spacings; equal sides of regular polygons; no three D1/D2 centers collinear; four 18 mm counters and four 35 mm square tile faces. All pages are US Letter, 612 by 792 points. `../qa/pdf-graph-results.json` records board evidence. Individual PNGs and two-page inspection sheets remain in `../qa/`.

`verify.py` passes paths, both trees, C3/C4/C5/C6/C8, C4/C5 added-road minima, F1/F2 folds, two-cop C6/C8, and exact revised Q6 common-start optimum. General arguments are retained in the independent mathematical stage's review; enumeration checks finite examples rather than establishing the all-rings theorem by itself.

Built from a ZIP extracted into an empty directory, using only extracted sources and Python 3/TeX Live. All three reconstructed PDFs were byte-identical to delivered final PDFs:

- shared.pdf (4 pages): f20f41ba2817745e0c7821d63718122fb35b5ed9624e00324d13b6f4987c1fbd
- upper.pdf (6 pages): d98525f8fc2e7335e1ec4dea8d623d4d99ebcd0ac791e1f6c92273472d07a3bf
- materials.pdf (3 pages): 040cd4c03ceb15bdd957b2a6acdb0718612551842075f0854f2592f0cce9b96b

Remaining checks: printing at actual scale, counter fit/stacking, tile assembly, cover opacity/trim/removability, and the full physical fold procedure. None has been physically rehearsed or classroom piloted. No local-to-remote synchronization is claimed.

## Release evidence location

The `../qa/` paths above describe the isolated revision-stage run. Reproducible final vector checks and compact results are preserved in the repository production record, not bundled render intermediates. A later provisional clipping concern was independently cleared with high-resolution PyMuPDF crops and Ghostscript full-page renders of these same bytes; no geometry mutation was needed. The independent final pair report records the cleared concern.

## Card fixes, October 23, 2026

Student pages changed from the review card: shared pp. 1, 2, 4; upper pp. 1, 3, 4, 5; materials pp. 1–2 (wording, the T1 board, letter positions, the D2 board position and the materials header). Each changed page was rendered at 80 dpi and inspected; the unchanged pages (shared p. 3, upper pp. 2 and 6, materials p. 3) are pixel-identical to the previous build. `../review/check_pdf.py` reads all boards from the new PDFs (175 checks, 0 failures), including that no letter sits on a road and that D1's d clears the D2 heading. `../review/check_card_fixes_2026_10_23.py` checks the new T1 (five cop moves from h; walking toward R always catches), the odd-ring sentence and the two-chord test. The new layout, counters and covers remain physically unrehearsed.
