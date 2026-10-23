# Week 14: student-page and guide fixes from the review card, October 23, 2026

The review card is `plans/review/week-14.md` in the project (verdict keep, no must), with its math check `plans/review/week-14-math.md` and checks in `plans/review/checks/week-14/`.

The student pages first became problem files with no wording change (`../../README.md`). The fixes below were then made in the problem files and the guide source, with the footer ids raised to F14-K-v3, F14-23-v3 and F14-45-v3.

## What changed

- **One line per change (should 1).** K–1 Problem 5's eight small copies now print their start's lines in light gray (35% black), so a child records a result by crossing out one gray line and drawing one new line; the large boards stay black. The guide's launch (p. 2) adds a referee check for every table and every change: a partner lays the new drawing on the old one and points to the one line that moved, and a drawing with two changed lines, or redrawn two changes away, does not count. The K–1 Problem 5 key (p. 5) says how to use the gray copies and that four copies for three results keep the count open. This replaces the menu's one-time standing pause.
- **Tracing paper (should 2).** Guide p. 2: about 28 tracing sheets cut into quarters (4¼ × 5½ in, which covers the largest board, 3.8 × 4.4 in), about ten quarters per child, for eleven children with eleven pencils and straightedges. The route note (p. 14) gives the same numbers in place of "twenty-two tracing sheets".
- **Route note (should 3).** Guide p. 14: "Grades 2-3 can use their pentagon gallery for the flip map and odd return (P4-5), with the hexagon one-flip and shortest-route problems (P3, P6), leaving the full hexagon collection (P7) for a separate investigation." (the math check's item 2 wording).
- **Grades 2–3 p. 8 (should 4).** The page is headed "Problem 7 (continued)" only; "Extra hexagons for your collection. Use these to continue Problem 7 on the previous page." is gone. The guide's Problem 7 key (p. 8) quotes the new heading.
- **K–1 Problem 3 (could 5).** "Explain why any impossible case cannot work." now reads "If one cannot be done, explain why."
- **K–1 Problem 6 (could 6).** "Can you visit every other filling once" now reads "Can you visit each of the other fillings once".
- **K–1 Problem 4 key (could 7).** Guide p. 4: "Only two pentagon completions exist, so two of the four pre-lined pentagon copies stay empty; the spares keep the copies from giving the count away." The copies are unchanged.
- **Grades 4–5 Problem 4 (could 9).** Three arrows run from the three starts to the fourth filling, as in grades 2–3 Problem 6; the starts move up 0.10 in and the target down 0.08 in to make room. The guide's key (p. 9) says "where the arrows point".
- **Grades 4–5 Problem 7 hint (could 10).** Guide p. 12: a route can be recorded on the one working board as a list of changes, such as "erase AC, draw BD" from Problem 3's example, with only the final filling drawn.
- **Grades 2–3 p. 6 (could 11, in part).** The eight copies move up 0.13 in, so the bottom row's labels clear the footer by about 0.17 in instead of 0.04 in.
- **Grades 2–3 Problems 2 and 7 (could 12).** "Organize your drawings so that you can explain why none are missing." and "Organize your drawings so you can tell whether any are missing or repeated." now read "How do you know none are missing?" and "How do you know none are missing or repeated?"
- **Guide p. 2 menu (could 13).** 0–5 run around (the children arrive from school), 5–9 launch, then handling tracing paper and straightedges, 9–28 and 28–50 table work, 50–60 share, matching `worksheet-workflow/context.md`, for eleven children.

Every page of the three packets changed (the footer id); in content, K–1 pages 3, 5 and 6, grades 2–3 pages 2, 6, 7 and 8 and grades 4–5 page 4. Guide pages 2, 4, 5, 8, 9, 12 and 14 changed in content; the guide keeps 14 pages and every heading stays on its page, so its page references still hold.

## Not done

- **Could 8** (grades 2–3 Problem 5: ask "Which numbers of flips can bring you back?" instead of an odd return): it changes the problem's question and answer (every number but 1 and 3), so it is left for the organizer. The guide's key already says why no odd return is shorter than five.
- **Could 11, the copy sizes** (0.82–0.92 in copies on K–1 p. 4, grades 2–3 p. 6 and grades 4–5 pp. 4–5): larger copies would take room from the working boards or the copy count; only the footer clearance was fixed. Organizer's call after a trial.
- **The return visit** (its Problem 2 circles corners already printed as circles; the math check's items 3 and 4): a separate package (`week-14-return-visit.pdf`) that the card noticed but did not review; it is unchanged.

## Verification

- `src/student_checks.py` keeps the old builder's enumeration checks (all fillings of 3 to 8 corners, the pentagon map, the K–1 kept-line counts, the grades 4–5 distances 3, 1, 2 and 3, 5, the fan rule on all 132 × 8 octagon cases; `mathematical-checks.json` is unchanged) and adds checks on the drawings the revised pages print: K–1 Problem 5's copies carry their start in gray, four per start against three results; K–1 Problem 4's pentagon has four copies for two completions; the three grades 4–5 Problem 4 arrows each run from a start towards the A fan, more than 0.1 in from both and crossing no drawing; the lowest grades 2–3 Problem 6 label stays 0.1 in above the footer; the largest working board is 3.81 × 4.40 in, inside a quarter sheet; 11 children × 10 quarters is 28 sheets; grades 2–3 Problems 4–5 are pentagon pages and Problems 3 and 6 hexagon pages; "erase AC, draw BD" is on grades 4–5 Problem 3. Changing the copy grid, an arrow or the gray makes it fail.
- The review's own extractor, `plans/review/checks/week-14/extract_figures.py`, run on the new print PDFs (outputs kept outside the project), reads every polygon and diagonal in the packets and guide as its October 5 transcription has them, except K–1 page 5, whose eight copies now carry their start's three diagonals in gray (0.65), as intended; the new arrows are plain strokes.
- `verify_geometry.py` still finds the same regular polygon counts and side checks in every source.
- `check_guide_copy.py` confirms that every key and hint sentence and route table in the problem files appears in the regenerated guide, and that the guide pages the keys cite carry their headings.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` and the strict `verify_rebuild.py` on all four PDFs (35 pages), and the problem-file tools give the same student LaTeX. K–1 pages 3, 5 and 6, grades 2–3 pages 2, 6, 7 and 8, grades 4–5 page 4 and guide pages 2, 4, 5, 8, 9, 12 and 14 were rendered and inspected.
- The references are now built with TeX Live 2023 (pdfTeX 1.40.25), so the audited pixel alternates for unchanged pages are no longer needed.
- These are digital checks. Whether light gray survives the copier, the quarter tracing sheets, the referee check and K–1 straightedge drawing are unrehearsed, and the theme remains unpiloted.
