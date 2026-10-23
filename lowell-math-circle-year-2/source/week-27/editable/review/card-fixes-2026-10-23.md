# Week 27: the review card's shoulds and coulds, October 23, 2026

The review card (`plans/review/week-27.md` in the project) had one must, the table kit, fixed earlier the same day with should 2 (the launch profile), and deferred the rest. A second card run (`plans/review/checks/week-27/card-second-run.md`) added a should for Grades 2–3 Problem 1. These are now made in the problem files (converted first with no wording change) and the guide source. Grades 2–3 is W27-23-v4 and Grades 4–5 W27-45-v3; K–1 (W27-K-v3), the table kit and the bonus did not change. The guide keeps its overview, 17 numbered pages and route note.

## Made

- **Should 3, guide p. 6.** "the checker records all blockers" is now "Each row shows one blocker; a child may find another." (BZ, CX and CY also block AX / BY / CZ, for example.)
- **Should 4, guide p. 13.** "Exact expected answer: 16" is retitled "A sufficient answer", says any bound from 13 up with a reason is right, and adds the sharper count: when an asker asks its last choice, every other receiver holds someone, so that receiver is free and the run ends; at most 4 × 3 + 1 = 13 requests (91 for ten), with a printed profile that takes 13.
- **Should 5.** Grades 2–3 Problem 4 prints six boards instead of four, so the page no longer shows the number of answers, and the guide says the boards are workspace. For K–1 Problem 6 the guide asks "Is there another way?" before confirming the first answer.
- **Should 6, guide p. 2.** "Two voices for one check": each child of a pair speaks for one side, reading only its own strip; the pair blocks only when both say yes.
- **Should 7, overview and guide p. 1.** The gate ("only after the child can check that both sides prefer a switch"; "Participation requires understanding why only the first is a blocking pair") is now "Start in P1; ask each piece in turn, as in the P1 held hint." The section is headed "Where to start, especially for K-1", and the overview's last line says "The starting route and longer proof keys follow."
- **Could 8, guide p. 2.** The launch says that a case's four strips serve both of its pairings, since K–1 and Grades 2–3 Problem 1 print the circles' strips on the left and the squares' on the right, above both boards.
- **Could 9, Grades 4–5 Problem 2.** The two record boxes are labelled "A, B, C, D asking" and "W, X, Y, Z asking".
- **Could 10, guide p. 14.** Before the Problem 5 proof, run the rules on Problem 1's bottom lists: either side asking gives AY / BZ / CX.
- **Could 11, guide pp. 1, 11, 17.** Cut: "a library label, not a booked meeting", the "instance-specific count" hedge, and the "Fidelity" and "Checks packaged" sections (p. 17 is now "Sources and local evidence"). Page 1 instead names the packets it keys.
- **Second run's should 4, Grades 2–3 Problem 1.** "join two letters that both want to change" is now "join a circle and a square that would both rather be together": in the bottom case both circles want to change in AY / BX, yet it stays.

## Left

- The second run's other items that the first card does not list are not made: a separate K–1 Problem 6 workspace page (the card chose the guide question instead), moving Grades 4–5 Problem 2's rules above "Use these rules", a different first-come example order for the guide's Problem 3, numbering the route note 18, and changing one strip in K–1 Problem 4's top case so it is not also a Problem 6 answer. The last changes a printed case, which the organizer would see as a different K–1 problem.

## Verification

- `review/verify_card_fixes_2026_10_23.py [build]` checks every change in the built PDFs and recomputes each changed claim: the two P1 cases' blockers and the one-sided wishes in the bottom case, four stable pairings of 24 in 2–3 P4 with six boards printed, both asking runs of 4–5 P2 (8 and 7 requests), the multiple-blocker rows, the request bound (only the final request can be a last choice, checked over all 46,656 three-pair profiles, where the most is 7 = 3 × 2 + 1, and 3,000 random four-pair runs), the printed 13-request profile under 500 random asking orders, AY / BZ / CX from either side, and every new or cut guide sentence. It passes (50,193 checks).
- `src/check_math.py`, `src/check_examples.py`, `facilitator-src/check_math.py` and `facilitator-src/verify_pdf.py` pass; `facilitator-src/source-manifest.json` now names W27-23-v4 and W27-45-v3 with their hashes.
- Changed pages were rendered and inspected: Grades 2–3 pp. 2 and 5, Grades 4–5 p. 2, guide overview and pp. 1, 2, 13, 14 and 17.
- `verify_revision.py` passes: every changed PDF and the kit reproduce exact 100-dpi pixels. The unchanged K–1 packet rebuilds here with identical text and vector geometry and glyphs moved under 0.06 pt on pages 2–7 (pdfTeX 1.40.25, TeX Live 2023); those six pages are now recorded in `review/rebuild-pixel-allowances.json`, whose old Grades 4–5 entries were dropped because that packet was revised. The K–1 print copy is unchanged.
- A clean rebuild from the extracted ZIP passes `verify_revision.py` and the card-fix verifier.
- The replaced PDFs are in the project's `week-27/archive-before-card-shoulds-2026-10-23/`, and the replaced ZIP in `source/week-27/archive-before-card-shoulds-2026-10-23/`.

All of this is digital checking. The week, the two-voice check and the kit remain unpiloted and physically unrehearsed.
