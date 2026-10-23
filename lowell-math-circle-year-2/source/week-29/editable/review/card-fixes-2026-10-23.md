# Week 29: guide corrections from the review card, October 23, 2026

Only the adult guide changed: pages 1, 2 and 3 of `facilitator-guide.pdf`. The student packets, their sources and their reference copies are unchanged. The review card is `plans/review/week-29.md` in the project, with its math check `plans/review/week-29-math.md`.

## What changed

- **Must (card fix 1), p. 2, K–1 Problem 6 key.** With 2- and 4-rods, 7, 9 and 11 all fail in 6–12; the key listed only 7. It now reads "{2,4}: 7,9,11". Every other K–1 key entry was rechecked by enumeration.
- **Should (fix 6), p. 3, Grades 4–5 Problem 5 key.** With 4- and 6-rods, 2 also fails: "odd targets and 2".
- **Should (fix 4 and the guide half of fix 5), p. 1, materials.** Rods at 1 cm per unit (Cuisenaire scale), print at 100%, since every printed strip and ruler is 1 cm per unit and the K–1 strips are outlines the rods must fill; a few 6-rods or 6 cm paper strips for 4–5 P5 (3/6 and 4/6).
- **Should (fix 10), p. 2, timing.** The hour now follows the group's shape: launch after the opening run-around, K P1–3 (adding the 3/5 contrast), 2–3 P1–3 or 4–5 P1–2 to about minute 20, continuations to about 38, then sharing; the tables have about 35–40 minutes.

Deferred: fixes 2, 3, 7, 8, 9, 11 and 12 change student pages and wait for a problem-file conversion (fix 2 also changes the 4–5 P2 key); the printable rod sheet in fix 5 is a new materials page for a later pass. The coulds (13–17) are not done.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` recomputes every K–1 key entry (P1–P6, all six pairs and every target 6–12), the 4–5 P5 gap sets of 2/4, 3/6 and 4/6 up to 300 and the last gaps of 3/5 and 4/7, and measures the reference K–1 strips (1, 2, 5, 6, 8, 9, 10 cm in 1 cm cells) and the printed rulers (1 cm ticks).
- The rebuilt guide differs from the October 4 guide only on pages 1–3; pages 4 and 5 are pixel-identical at 100 dpi. All three student PDFs rebuild with exact reference pixels. Each changed page was rendered and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` with exact 100-dpi pixels on all 21 pages.
- The previous guide and ZIP are archived in the project in `week-29/archive-before-card-fixes-2026-10-23/` and `source/week-29/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted; rod fit and timing are unrehearsed.

## Part 2: student-page fixes and the rod sheet, after the problem-file conversion

The student pages are now `problems/*.md` and `figures.py` beside `week.toml` (in the ZIP, `problem-files/`). The conversion itself changed nothing: the rebuilt LaTeX was the old builder's byte for byte and the packets matched the print PDFs in pages, text and 100-dpi pixels. Then, as v3 packets (F29-K-v3, F29-23-v3, F29-45-v3):

- **Should 2, Grades 4–5 Problem 2.** It asks for 3 and 5, and 4 and 5, only, with more room for each; 4 and 7 is left to Problems 3 and 4, which it used to answer. Guide p. 3's P2 key drops 4/7 and "18,19,20,21 as above"; its P3–4 key now lists the builds 18–21 and the three cases for 17 itself.
- **Should 3, K–1 Problem 2.** Three strips under 12 and three under 15; each has exactly two ways, so one strip per target stays empty (guide p. 2 says so).
- **Should 7, Grades 4–5 Problem 7.** "propose a rule that gives the last impossible length from the two rod lengths", so the comparison leads to ab − a − b rather than restating Problem 5's divisor rule.
- **Should 8, K–1 Problem 6.** Six rows, one per pair, each with two boxes for the pair's rod lengths and the targets 6–12, replacing one target row and ruled lines.
- **Should 9, K–1 Problem 4 and Grades 2–3 Problem 1.** "Mark a target on a ruler and build from 0 to the mark." is gone; the guide's launch (p. 2) builds the 3 + 4 train from 0 on a printed ruler instead.
- **Should 11, Grades 2–3 Problem 4.** "Can 3-rods and 4-rods build every length after 16? Can 3-rods and 5-rods build every length after 20? Explain how you know." Guide p. 3's key answers yes to both.
- **Should 12, Grades 2–3 Problem 6.** "Is the claim true? Use rods 2, 3, 4, 5 and 7 to decide." The page no longer names the counterexample; the key adds that 2/4 is the only one of the ten pairs with gaps forever.
- **Coulds 13–17.** The labels of 2- and 4-rods have the rod's colour behind them, so the cell line no longer runs through the numeral (13); Grades 2–3 Problem 2 no longer repeats "Rod order does not count." (14); Grades 4–5 Problem 6 reads "Find every way to build 24 with 3-rods and 4-rods. How can you change one way into another?" (15); Grades 4–5 Problem 8 says "every length from some point on" (16); guide p. 1 plans for the eleven children, with the five kits named (17).
- **Should 5, the rod sheet.** `week-29-materials.pdf`, built by `materials/build_materials.py`: one pair-kit per sheet of card stock, ten rods each of 2, 3, 4, 5 and 7 units and three 6-rods at 1 cm per unit, in twelve abutting 19 cm rows, with a 10 cm scale check. Guide p. 1 points to it.

### Verification

- `python3 review/verify_student_fixes_2026_10_23.py` reads the printed pages and checks each fix and its mathematics: v3 footers; no ruler sentence; three 12 cm and three 15 cm strips, with exactly two builds each; six pair rows of targets 6–12, with exactly {2,3}, {2,5}, {3,4} covering them; last gaps 5 and 7 for 3/4 and 3/5, and the certificates 17–19 and 21–23; of the ten pairs from 2, 3, 4, 5, 7 only 2/4 has gaps forever and the other nine have last gap ab − a − b; the 4–5 P2 pairs and the 4/7 builds; the five last gaps 5, 7, 11, 17, 23; the three builds of 24; the label patches.
- `python3 materials/verify_materials.py` measures the rod sheet from the PDF: 53 rods, each 10.00 mm wide and n × 10.00 mm long with its numeral, rows of 190.00 mm that abut, one 100.00 mm scale line; the K–1 strips they fill measure n cm by 1 cm. Every buildable target the problems print or the keys use has a build from one kit, and the certificate runs 6–8, 8–10, 12–15 and 18–21 fit one kit side by side; the 5/7 run 24–28 needs twelve 5-rods at once, so it is built in turns, as the guide's "large targets can be represented by counts" allows.
- `python3 problem-files/check_guide_copy.py` confirms the key view's copy of the guide. Guide pages 4 and 5 are pixel-identical to the previous release; pages 1–3 changed. Every student page changed (the footer is v3). Each changed page and the rod sheet were rendered and inspected.
- A clean rebuild from the extracted ZIP passes `verify_revision.py` with exact 100-dpi reference pixels on all pages, and both verifiers pass there.
- The replaced v2 packets and guide are archived in the project in `week-29/archive-before-card-fixes-2026-10-23/`, and the conversion's ZIP in `source/week-29/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted; the rod sheet is physically unrehearsed (nobody has cut or used it), and rod fit and timing are untested.
