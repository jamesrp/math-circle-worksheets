# Week 22: fixes from the review card, October 23, 2026

The review card is `plans/review/week-22.md` in the project, with its math check `plans/review/week-22-math.md`. Its verdict was keep; it listed four shoulds and six coulds. All four shoulds and coulds 5 and 7–10 are done; could 6 says to leave K–1 page 3 as it is, and it is unchanged. The student pages were first stored as problem files with no wording change (the rebuilt LaTeX was the old builder's apart from blank lines, and the packets matched its rebuild in pixels), and that conversion was committed alone. Then, as v5 packets (F22-K-v5, F22-23-v5, F22-45-v5; 9, 9 and 12 pages):

## Student pages

- **Should 1, all bands, Problem 1.** A new page 2 continues Problem 1 with one small board per cross, D printed at that cross (three boards for K–1, four for Grades 2–3 and 4–5), so each placement is drawn on its own board and no earlier triangle or segment judges a later one. Page 1 keeps the large board with its crosses for moving the D marker; page 2 restates the task ("For each place of D, make two regions that meet and mark a point they share." for K–1).
- **Should 2, all bands, p. 1, the key.** The location inside triangle HIJ is a small dot instead of a × that looked like the boards' crosses for D.
- **Could 9, Grades 4–5 Problem 6.** Ends "Give an explanation that covers all arrangements."; the named cases (dots in a straight line, labels at the same point) were already raised by Problems 2 and 4.

Every later page moves back one; apart from the footer they are unchanged.

## Adult guide (overview unchanged; printed pp. 1–2, 5–19, 21 and the route page)

- **Should 1.** P. 2 says P1's record page has one small board per cross with D printed; the K–1, Grades 2–3 and Grades 4–5 Problem 1 gates (pp. 5, 10, 14) say to move the D marker on the large board and draw each placement on its own record board.
- **Should 2.** The launch describes "the small unlabelled interior dot".
- **Should 3, p. 2.** "Say explicitly" adds "On a line, draw one group just above the dots and the other just below.", and each pair gets two colors of pencil or crayon, one per group (also in the table list), so overlapping segments on K–1 P3, Grades 2–3 P2 and Grades 4–5 P2 stay visible.
- **Could 5, p. 8.** For K–1 Problem 6: "Taking turns means one child places all four markers and the partner splits them; then they swap."
- **Could 7, route page.** It says "guide p. 3" (it said "guide p4") and is numbered 22, following p. 21 (`route-note.json` sets `unnumbered_pages` for the overview, and this package's `add_route_note.py` subtracts it).
- **Could 8, p. 2.** The current eleven-child group (four K–1, four Grades 2–3, three Grades 4–5): 4 × 9 + 4 × 9 + 3 × 12 = 108 sheets for a packet each, or 2 × (9 + 9 + 12) = 60 for a packet per pair.
- **Could 10, p. 2.** The launch says "Split the four labels into two groups", the word every problem uses, and an adult once stretches a real rubber band around three upright markers and lifts it away.
- The page map (p. 1), every page reference to student pages, the verification page and the footer name the v5 packets and their 9, 9 and 12 pages; the kicker reads "revised 23 October 2026".

## Bonus companion (W22-BON-v2, W22-BON-FAC-v2)

**Should 4.** T in the bonus Problem 1 moved from (4, 3.2), 1.3 mm from segment BE, to (3.2, 3.4), about 12.9 mm from every joining segment and inside the same eight triangles; the bonus guide's coordinates and containment certificate follow. See `source/week-22-bonus/review/card-fixes-2026-10-23.md`.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py [folder]` reads the built PDFs, the problem files and `figures.py`, and checks: v5 footers and 9, 9, 12 pages; that each record page has one board per cross with D at the cross positions and the same A, B, C, D printed once per board and not on page 1; with exact rational geometry, the splits whose regions meet for every placement (K–1: AD | BC, ABC | D, AC | BD; Grades 2–3: AD | BC, ABC | D, both ABC | D and AB | CD on side AB, AB | CD; Grades 4–5: AD | BC, ABC | D, both on side AB, AC | BD), each named in the guide's Problem 1 key; the key's dot strictly inside HIJ and, from the page drawings, crosses only on the boards; the Grades 4–5 Problem 6 wording; and every guide fix above, including the sheet arithmetic from the actual page counts and the route page's reference and number. `src/check_examples.py` (now asserting the dot), `src/check_geometry.py` and `facilitator-src/check_math.py` (now expecting 9, 9 and 12 pages) pass in the build.
- Page by page against the v4 rebuild at 100 dpi: in every band page 1 changed (the key's dot), page 2 is new, Grades 4–5 page 11 (Problem 6) changed, and every other page is the old one moved back a page with only the footer changed. Guide: the overview is unchanged; printed pages 1–2, 5–19, 21 and the route page changed in content (most only in a student page reference), pages 3, 4 and 20 only in the footer. The changed pages were rendered and inspected.
- `review/reference-manifest.json` has the new hashes and page counts, and `facilitator-src/student-input-manifest.json` the new student hashes. A clean rebuild from the extracted ZIP passes `verify_revision.py` and `verify_rebuild.py` with exact 100-dpi pixels on all 53 pages, and the card-fix verifier passes there.
- The replaced v4 packets and guide, and the bonus v1 files, are archived in the project in `week-22/archive-before-card-fixes-2026-10-23/`; the conversion's ZIP and the bonus v1 ZIP in `source/week-22/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted; tracing, two-color drawing on a line and the timing are unrehearsed.
