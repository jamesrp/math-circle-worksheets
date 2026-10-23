# Week 11: student-page and guide fixes from the review card, October 23, 2026

The review card is `plans/review/week-11.md` in the project (verdict keep, no must), with its math check `plans/review/week-11-math.md` and checks in `plans/review/checks/week-11/`.

The student pages first became problem files with no wording change (`../../README.md`). The fixes below were then made in the problem files and the guide source, with the footer ids raised to F11-K-v4, F11-23-v4 and F11-45-v4.

## What changed

- **K–1 Problems 1 and 3 (should 1).** Each start is printed on two rows, as in grades 2–3 Problem 1, so a child compares two orders of one start rather than four different starts. To fit eight rows, Problem 1's statement, board and word example move up 14–16 mm and Problem 3's board 7 mm; rows are 7 mm (Problem 1) and 7.7 mm (Problem 3).
- **K–1 Problem 4 (should 2).** Ten answer rows for the eight stable placements, so the rows no longer give the count away. Guide p. 7 hint: "If a child stops at seven, ask whether a board with no chips counts; the eighth way is (0,0,0). The page has ten rows so that it does not give the count away."
- **K–1 Problem 6 (should 3).** "Can you ever get empty circles again?" now reads "Can both circles ever be empty again?"
- **Grades 2–3 Problem 4 (should 4).** Ends with grades 4–5 Problem 4's question, "Does the extra line change your conclusion about order?"
- **Grades 2–3 Problem 5 (should 5).** A Timing column: "together", "2 at A first", "4 at B first", one row each.
- **Guide p. 4 launch (should 6).** A table routine for every band: one child moves the chips; the partner touches each line from the sharing circle, checks that one chip went along it and says the circle's letter for the sharing word (an adult scribes for K–1); swap roles at each new start. The grades 2–3 Problem 1 hint (p. 8) now points to it, and the K–1 Problem 1 answer (p. 6) says why each start has two rows.
- **Guide p. 8, grades 2–3 Problem 3 invariant (could 7).** "A start with chips never finishes empty, because the last share always leaves a chip on the other circle." before "The three nonempty stable pairs have different remainders."
- **Row heights (could 8).** Grades 2–3 Problem 4 rows 6 → 7.1 mm, Problem 6 rows 5.4 → 6 mm, grades 4–5 Problem 1 rows 5.5 → 7.2 mm, taken from the space around the boards. Board geometry is unchanged: 44 mm circles, 60 mm sinks, the same lines.
- **Headers (could 11).** "End A/B/C" in grades 2–3 Problems 2 and 4 and grades 4–5 Problem 4 now read "Finish A/B/C", as elsewhere.

Every page of the three packets changed (the footer id); in content, K–1 pages 1, 3, 4, 6, grades 2–3 pages 2, 4, 5, 6 and grades 4–5 pages 1, 4. Guide pages 4, 6, 7 and 8 changed in content and p. 4 names the v4 packets; the guide keeps 12 pages and its page references (pp. 4, 7, 9).

## Not done

- **Could 9** (replace "A → AB → ABA" with the return visit's Before / A fires / After panel): a new figure on every band's first page that would drop the sharing-word example the record depends on; the launch already shows a move. Left for the organizer.
- **Could 10** (replace grades 2–3 Problem 4's order question with the extra-line capacity question): it changes the problem's substance, and should 4 makes the order question explicit instead. The capacity question stays in the guide (p. 12). Organizer's call.
- **Could 12** ("fire" in the return visit against "share" in the base pages): the return visit is a separate package (`source/week-11-return-visit/`) that the card did not review; changing its student page needs its own conversion.

## Verification

- `src/student_checks.py` keeps the old builder's checks (every printed start stabilised in 20 random orders and by a memoised search over all legal choices; repeated additions; staged batches) and adds checks that read the printed starts and row counts from the problem files' `figures.py`: every start printed twice in K–1 Problems 1 and 3 and grades 2–3 Problems 2 and 4 and grades 4–5 Problem 4 has at least two complete legal words; (4,0) has only AAB, so "if possible" stays in grades 2–3 and 4–5 Problem 1; the four-cycle has 8 stable placements, 7 with chips, none with 4 chips, fewer than the 10 rows; after 1 to 11 additions at A both triangle circles are never empty, while one circle is empty in 8 rows; the three grades 2–3 Problem 5 timings all finish at (1,1,1). Changing a row count or a start to (4,0) makes it fail.
- `facilitator-src/verify.py` and the guide's tables are unchanged; `check_guide_copy.py` confirms that every key and hint sentence in the problem files appears in the regenerated guide and that the guide's pages 4, 7 and 9 carry the labelled headings.
- The review's own extractor, `plans/review/checks/week-11/extract_pdf.py`, run on the new print PDFs (outputs kept outside the project): every board is still the intended graph with 44.0 mm circles and a 60.0 mm square sink, and every changed table has the intended rows, starts (K–1 dot counts) and headers.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` and the strict `verify_rebuild.py` on all four PDFs (30 pages), and the problem-file tools give the same student LaTeX. Every changed student page and guide pages 4, 6, 7 and 8 were rendered and inspected.
- The references are now built with TeX Live 2023 (pdfTeX 1.40.25); the October 4 references used pdfTeX 1.40.27, which renders glyphs very slightly differently.
- These are digital checks. Counter fit on the 44 mm circles and the table routine are unrehearsed, and the theme remains unpiloted.
