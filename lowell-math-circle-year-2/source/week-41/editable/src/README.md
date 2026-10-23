# Week 41 revised student source

The student pages' source is the Week 41 problem files: `week.toml`, `figures.py` and `problems/*.md`, in `../problem-files/` inside the portable ZIP and in `lowell-math-circle-year-2/source/week-41/` in the repository. Edit a problem there, not here. `regenerate.py` writes `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` from them; the builder they replaced, `make_packets.py` with `common.py`, is archived in the repository's `source/week-41/archive-before-problem-files-2026-10-23/`.

Revised and unpiloted. Student pages only. Every packet includes a 180 mm square, three-by-three portal mat for 100% Letter printing. Smaller repeated maps are recording diagrams; the table's 90 mm copied-map array and spare extension copies remain separate materials specified by the activity outline. Opposite edges use matching shape marks and arrow orientation. No edge reversals are used.

The two-right-step input/process/output example uses identical H, E, and D labels on the quotient map and its consecutive copies. Middle and upper grades distinguish reaching H from returning to the original copy. Upper-grade square slides keep endpoints fixed and permit face motion and self-overlap; grid edges do not become permanent barriers. A visit to H alone is never equated with contracting the whole journey. K–1 tasks do not claim homotopy classification.

`check_math.py` checks the printed route endpoints, the two-step reachability set, and the two-pawn swap obstruction on this finite model. These are mathematical checks, not classroom testing.

Run `bash build.sh` with Python 3.11+, pdfLaTeX, TikZ, Latin Modern, AMS fonts, and Poppler installed. It runs `regenerate.py` and `check_math.py`, uses the caller's TeX environment, resolves page anchors with two passes, writes PDFs to `../`, and writes page renders and logs to `../qa/`.

The revised K–1 packet is four pages; the older packets are five pages. All locations are small-cell centers, marked with a dot. The square-slide example uses the actual lower-left 2-by-2 block D,H/F,G of the same map, comparing F→G→H with F→D→H. Both directions and all rotations of a square slide are allowed, as are insertion and deletion of an immediate same-edge backtrack. These moves preserve the lifted endpoints, and generate their equality classification. The new concrete RRRUUU→UUURRR task precedes the general question without printing a solution algorithm.

The middle band's small final recording array was replaced by a full-page 180 mm repeated map. This remains a 60 mm-per-copy printed recording map, not a claim that the separate 90 mm-per-copy table array and extension tiles have been physically prepared. Their real tabletop check, pawn handling, and tracing-paper workflow remain unperformed. Copies extend indefinitely; the printed border is not a wall or another wraparound. No physical torus construction is required, and no full homotopy classification is claimed for K–1.
