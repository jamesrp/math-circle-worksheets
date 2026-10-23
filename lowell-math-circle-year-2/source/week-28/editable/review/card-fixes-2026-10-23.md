# Week 28: printable kit and guide fixes from the review card, October 23, 2026

The review card is `plans/review/week-28.md` in the project, with its math check `plans/review/week-28-math.md` and checks in `plans/review/checks/week-28/`.

## What changed

- **Must (card fix 1): a printable kit.** New `materials.pdf` (print copy `week-28-materials.pdf`, 15 pages, US Letter at 100%, built by `materials-src/build_materials.py`). Page 1 is the print plan for eleven children (K–1 4, grades 2–3 4, grades 4–5 3) and three adults: 42 sheets of copy paper and 7 of card stock. Pages 2–10 print one 18 cm folding disk each, with centre dot, tinted front and rays numbered clockwise from ray 1 at the top: the four-right-angle disk, disks B (45, 90, 90, 135), C (60, 120, 120, 60) and D (30, 60, 150, 120), the four grades 2–3 Problem 4 starts with 30° rim ticks, and a blank disk with 15° ticks. Pages 11–13 print the three wedge sets (seven lettered wedges; sixteen matching wedges with two half-turn boards; six repeated-letter wedges with three start disks), each set touching along shared straight cuts. Page 14 prints the K–1 Problem 4 M and V tabs (27 of each), page 15 the K–1 Problem 6 route cards A–H. Each page carries a 10 cm check line, what the sheet is and how many to print per table, and the mark "physically unrehearsed".
- **Guide p. 1 (should 2), launch:** after the legal refold, show how to record a fold: unfold with the tinted front up and ray 1 at the top, and write M or V beside each ray number on a spare uncut disk sheet.
- **Guide p. 2, preparation:** rewritten around the kit, with counts for eleven children (could 10, first part), the measurement sets keyed to kit pages, how to cut and precrease the disks (press only along each ray from the centre out: a crease carried through the centre adds a ray), that K–1 Problem 3 prints six disks for four answers so two are spare (the guide half of should 3), and about two and a quarter hours of preparation.

Only PDF pages 2 and 3 of `facilitator-guide.pdf` (guide pages 1 and 2) changed; the other 16 pages are pixel-identical at 100 dpi, and the three student packets rebuild with exact reference pixels.

Deferred: should 3's student half (print four marked K–1 Problem 3 disks and two blank ones) and shoulds 4–6 change student pages and wait for a problem-file conversion; coulds 7–9 likewise; could 10's page-17 and p. 8 drafting-note items are not done. The student-page items were made later the same day, after the conversion; see the next section.

## Verification

- `materials-src/check_materials.py` reads only the finished kit PDF: 333 checks, 0 failures. It checks headers, footers, the 100 mm scale line on every page, the 180 mm disk diameter, every ray angle against what each problem needs, rim numbers and ticks, and the folding conditions on the printed angles with two independent methods (crimp reduction and a layer-order brute force): the right-angle disk folds in exactly 8 mountain-valley words, B in none, C in six, D in four (MVMM, MVVV, VMMM, VMVV; VVVM fails), and each add-a-ray start has exactly one fourth ray that folds flat, 360° minus its first angle (scanned every 0.5°). It also checks wedge angles, radii, labels and shading, the ten half-turn groups of the sixteen-wedge set, the 36 orders of the six-wedge set, the 54 tabs (27 M, 27 V) and the 16 route cards.
- `plans/review/checks/week-28/kit_crosscheck.py` in the project compares the kit's disks with the student PDFs' disks and runs the review's own folding oracle on them; all agree.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` and the strict `verify_rebuild.py` on all five PDFs (51 pages). Every kit page and both changed guide pages were rendered and inspected.
- Digital checks do not make the kit ready: no disk from it has been folded and no piece cut. The adult pretest on guide pages 2–3 comes first. The theme remains unpiloted.

## Student-page fixes, after the problem-file conversion

The student pages became problem files first, with no wording change (`../../README.md`). Then, in the problem files, with the footer ids raised to F28-K-v3, F28-23-v3 and F28-45-v3:

- **K–1 Problem 3 (should 3):** four disks with ray 1 marked M for the four answers, then two blank disks under the label "Extra workspace".
- **Grades 4–5 Problem 6 (should 4):** 16 recording strips instead of 12, so the number of rows no longer gives away the answer, 12.
- **Grades 2–3 Problems 2–4 (should 5):** Problems 2 and 3 swapped, so children try to close disks A–D before measuring their alternating pairs. Problem 2 no longer asks to "explain any exact mismatch"; the measuring problem, now Problem 3, ends "For any disk that could not close, explain why." and has two lines for it. Problem 4 reads "Add one ray to each pattern so it can close flat along every ray. Make a flat fold of each completed pattern."
- **Grades 4–5 rules (should 6):** "A failed attempt alone does not establish impossibility." cut.
- **Grades 4–5 Problem 4 (could 8):** "Explain why each labeling on your list works." cut; a fold is its own witness.
- **Grades 2–3 rules (could 9):** "Loose wedges are for measuring." cut.

The guide follows: its grades 2–3 answers are reordered (guide p. 10: Problems 1 and 2, with the listening note; p. 11: Problems 3 and 4), the sixteen-wedge answer says that B is the disk that could not close in Problem 2, the hold for the closing problem points ahead to Problem 3's measuring, the grades 4–5 Problem 1 page references on p. 13 swap (totals p. 11, witnesses p. 10), p. 2 lists the K–1 Problem 3 extra-workspace disks and the sixteen wedges under grades 2–3 Problem 3, p. 14 drops the Problem 4 explanation request, and p. 1 and p. 16 name the v3 packets. The kit's print plan and disk and wedge captions (kit pp. 1–5, 12) swap grades 2–3 P2 and P3 in the same way. The problem files' keys follow the guide (`check_guide_copy.py`).

Not done: could 7 (ask 4–5 Problem 3 for "an angle rule that decides" instead of stating it). It is more than a one-line change: it turns an explanation of a stated rule into finding one, and "decides" asks for the converse, which the guide cites but does not prove. Could 10's page-17 and p. 8 drafting-note items remain undone.

Verification: `src/student_checks.py` still passes (10 half-turn groups, 8 right-angle labelings, 12 six-angle orders, tab and route checks); `materials-src/check_materials.py` 333 checks, 0 failures; `plans/review/checks/week-28/kit_crosscheck.py` 0 failures on the new kit. The package build from the extracted ZIP and the problem-file tools give the same student pages (identical LaTeX; `compare.py` finds identical text and pixels). Every page of the three packets, guide PDF pages 2, 3, 11, 12, 14, 15 and 17, and kit pages 1–5 and 12 were rendered and inspected; the other guide and kit pages are pixel-identical. The previous print PDFs are in `week-28/archive-before-student-page-fixes-2026-10-23/` beside the print copies, and the conversion's ZIP in `source/week-28/archive-before-student-page-fixes-2026-10-23/`. The pages are digitally checked only; the theme remains unpiloted and the kit physically unrehearsed.

## Kit footer id, later on October 23

The student-page fixes changed kit pages (the grades 2–3 numbering) while the kit's footer still read W28-M-v1, the id of its morning printing. A footer-version sweep the same day bumped it to W28-M-v2 (`ID` in `materials-src/build_materials.py`; `check_materials.py` expects it). The rebuilt kit differs from the previous one only in that id: the extracted text is identical after the id swap, and the differing pixels lie in the footer row.

## Critic follow-up, later on October 23

An independent critic reviewed the day's student-page changes (no arithmetic or key error found) and asked for three more:

- **K–1 Problem 3 (should):** four disks marked M matched the four answers, so the page told a child the list was complete. All six disks now carry M on ray 1, with no "Extra workspace" label; the guide (p. 2) says two are spare. The key is unchanged.
- **Grades 2–3 Problem 3 (could):** "For any disk that could not close in Problem 2, explain why."
- **Kit p. 14 (could):** a fourth K–1 tab stock, 36 M and 36 V tabs, one stock per child at a table of four; the kit's p. 1 and guide p. 2 say so.

Ids: F28-K-v4, F28-23-v4, kit W28-M-v3; grades 4–5 and the key view are unchanged. The rebuilt packets differ from v3 only on their p. 3 (and the footers); the kit only on pp. 1 and 14 (and the footers); the guide only on pp. 1, 2 and 16. `check_materials.py` now expects 72 tabs, four full stocks.
