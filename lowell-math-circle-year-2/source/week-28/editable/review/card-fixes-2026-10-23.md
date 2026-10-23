# Week 28: printable kit and guide fixes from the review card, October 23, 2026

The review card is `plans/review/week-28.md` in the project, with its math check `plans/review/week-28-math.md` and checks in `plans/review/checks/week-28/`.

## What changed

- **Must (card fix 1): a printable kit.** New `materials.pdf` (print copy `week-28-materials.pdf`, 15 pages, US Letter at 100%, built by `materials-src/build_materials.py`). Page 1 is the print plan for eleven children (K–1 4, grades 2–3 4, grades 4–5 3) and three adults: 42 sheets of copy paper and 7 of card stock. Pages 2–10 print one 18 cm folding disk each, with centre dot, tinted front and rays numbered clockwise from ray 1 at the top: the four-right-angle disk, disks B (45, 90, 90, 135), C (60, 120, 120, 60) and D (30, 60, 150, 120), the four grades 2–3 Problem 4 starts with 30° rim ticks, and a blank disk with 15° ticks. Pages 11–13 print the three wedge sets (seven lettered wedges; sixteen matching wedges with two half-turn boards; six repeated-letter wedges with three start disks), each set touching along shared straight cuts. Page 14 prints the K–1 Problem 4 M and V tabs (27 of each), page 15 the K–1 Problem 6 route cards A–H. Each page carries a 10 cm check line, what the sheet is and how many to print per table, and the mark "physically unrehearsed".
- **Guide p. 1 (should 2), launch:** after the legal refold, show how to record a fold: unfold with the tinted front up and ray 1 at the top, and write M or V beside each ray number on a spare uncut disk sheet.
- **Guide p. 2, preparation:** rewritten around the kit, with counts for eleven children (could 10, first part), the measurement sets keyed to kit pages, how to cut and precrease the disks (press only along each ray from the centre out: a crease carried through the centre adds a ray), that K–1 Problem 3 prints six disks for four answers so two are spare (the guide half of should 3), and about two and a quarter hours of preparation.

Only PDF pages 2 and 3 of `facilitator-guide.pdf` (guide pages 1 and 2) changed; the other 16 pages are pixel-identical at 100 dpi, and the three student packets rebuild with exact reference pixels.

Deferred: should 3's student half (print four marked K–1 Problem 3 disks and two blank ones) and shoulds 4–6 change student pages and wait for a problem-file conversion; coulds 7–9 likewise; could 10's page-17 and p. 8 drafting-note items are not done.

## Verification

- `materials-src/check_materials.py` reads only the finished kit PDF: 333 checks, 0 failures. It checks headers, footers, the 100 mm scale line on every page, the 180 mm disk diameter, every ray angle against what each problem needs, rim numbers and ticks, and the folding conditions on the printed angles with two independent methods (crimp reduction and a layer-order brute force): the right-angle disk folds in exactly 8 mountain-valley words, B in none, C in six, D in four (MVMM, MVVV, VMMM, VMVV; VVVM fails), and each add-a-ray start has exactly one fourth ray that folds flat, 360° minus its first angle (scanned every 0.5°). It also checks wedge angles, radii, labels and shading, the ten half-turn groups of the sixteen-wedge set, the 36 orders of the six-wedge set, the 54 tabs (27 M, 27 V) and the 16 route cards.
- `plans/review/checks/week-28/kit_crosscheck.py` in the project compares the kit's disks with the student PDFs' disks and runs the review's own folding oracle on them; all agree.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` and the strict `verify_rebuild.py` on all five PDFs (51 pages). Every kit page and both changed guide pages were rendered and inspected.
- Digital checks do not make the kit ready: no disk from it has been folded and no piece cut. The adult pretest on guide pages 2–3 comes first. The theme remains unpiloted.
