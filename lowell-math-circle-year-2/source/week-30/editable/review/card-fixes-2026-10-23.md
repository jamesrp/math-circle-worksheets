# Week 30: fixes from the review card, October 23, 2026

The review card is `plans/review/week-30.md` in the project, with its math check `plans/review/week-30-math.md`. Its verdict was keep; it listed seven shoulds and five coulds, and all twelve are done. The student pages were first stored as problem files with no wording change (the rebuilt LaTeX was the old builder's byte for byte), and that conversion was committed alone. Then, as v3 packets (F30-K-v3, F30-23-v3, F30-45-v3):

## Student pages

- **Should 1, Grades 2–3 Problem 4.** Three small boards under each of "1, 3, 8" and "1, 3, 9", with no ruled lines, so the page no longer shows that there are two ways and one. Knowing you have them all stays the problem.
- **Should 2, Grades 4–5 Problem 5.** "What is the most any three-weight kit can balance, even with gaps? Explain why none can do better." replaces "Can another kit balance more, even if there are gaps?"
- **Should 3, K–1 Problem 3.** Two labelled rows of boxes 1–6, "1 and 4" and "1 and 3", in place of one strip and ruled lines, so the two kits' results can be compared.
- **Should 4, Grades 2–3 Problem 3.** Target boxes 1–14 under each kit in place of ruled lines; the first misses (13, 14, 5) all fall in that range.
- **Should 6 and could 10, Grades 2–3 Problem 2.** The three boards have blank target boxes (they printed 5, 8 and 13, the guide's hint), and "Test your choice." is gone.
- **Could 8, K–1 Problem 5.** The weight cards' dot rows are .33 cm apart instead of .38, so the 10 card's tenth dot clears the border (by about 4.5 pt).
- **Could 9, every band's first page.** The shared rules' worked example is target 5 with weights 2 and 7 ("put 2 beside the target", 5 + 2 = 7), which no task uses; the arrow that pointed at text is gone.

## Adult guide (pages 1, 2 and 4)

- **Should 5, materials.** Linking-cube sticks (or Week 29's Cuisenaire rods) of 1, 2, 3, 4, 7, 8, 9 and 10 units, 44 cubes a kit, target sticks in another colour and a two-pan mat on which each pan's sticks lie end to end, so equal row lengths balance. New sticks are snapped when a child chooses 5, 6, 7, 11 and so on; paper cards stay for 27, 81 and big targets, with blanks. Preparation: about 15 minutes to snap five kits (about 220 cubes). The launch's 2 and 7 are in the kit. This kit has not been rehearsed.
- **Could 11, timeline.** About 35–40 minutes at tables after a 5-minute launch: a first 15–20 minutes, then pairs pose targets for the other pair at their table (at the 4–5 table two build and the third checks, rotating), then sharing.
- **Launch (could 9).** The board demonstration uses the new example.
- **Should 2's key.** The 4–5 P5 key now says why no three-weight kit does better than 13: of the 27 placements, all-off gives zero and the rest pair into opposites by swapping the pans.

## Bonus companion guide (W30-BON-FAC-v2)

Should 7 and could 12 are wording fixes on pages 1 and 2 of the bonus guide; see `source/week-30-bonus/review/card-fixes-2026-10-23.md`. The bonus student packet is unchanged.

Nothing on the card is deferred. The cube-stick kit and its fit on the mat are untested, as the card says.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py [folder]` reads the built PDFs and checks each fix and its mathematics: v3 footers; the launch example on every first page, used by no task, balancing only with 2 beside the target; K–1 P3 rows (1 and 4 reach 1, 3, 4, 5; 1 and 3 reach 1–4); the 10 card's dot clearance; 2–3 P2's three blank boards, the removed sentence and 9 as the only third weight up to 199; 2–3 P3's boxes 1–14 under each kit and first misses 13, 14, 5; 2–3 P4's three boards per kit against 2 and 1 ways; the 4–5 P5 question and the bound 13 (search of all kits up to 40, reached by 1, 3, 9, and (3³ − 1)/2); the guide's materials, 44 and 220 cubes, launch and timing. It passes with no failures.
- Page by page against v2 at 100 dpi: K–1 pages 1, 3 and 5 changed, page 4 only in the shared 10 card's dots, page 2 only in the footer; Grades 2–3 pages 1–4 changed, page 5 only in the footer; Grades 4–5 pages 1 and 4 changed, the rest only in the footer; guide pages 1, 2 and 4 changed, pages 3 and 5 unchanged. Each changed page was rendered and inspected.
- Every student and guide reference changed, so `rebuild-pixel-allowances.json` no longer lists unchanged-packet alternates, and `reference-manifest.json` has the new hashes. A clean rebuild from the extracted ZIP passes `verify_revision.py` with exact 100-dpi reference pixels on all 20 pages, and the card-fix verifier passes there.
- The replaced v2 packets and guides are archived in the project in `week-30/archive-before-card-fixes-2026-10-23/`, and the conversion's ZIP and the previous bonus ZIP in `source/week-30/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted; the cube-stick kit, the mat and the timing are unrehearsed.
