# Week 49: fixes from the review card, October 23, 2026

The review card is `plans/review/week-49.md` in the project, with its math check `plans/review/week-49-math.md`. The week was first stored as problem files with no wording change; these fixes were then made in the problem files (`problem-files/problems/*.md`, `problem-files/figures.py`, `problem-files/week.toml`) and the guide in `facilitator-src/content.json` and `facilitator-src/route-note.json`.

## What changed

- **Should 1, K–1 Problem 6 and Grades 2–3 Problem 5.** The first printed ring is (0,2,1,4), which lasts 4 moves, beside (0,1,4,2), which also lasts 4, so the page no longer shows a longest order. The guide's key gives the (0,2,1,4) run and keeps (0,1,2,4) as the 7-move order.
- **Should 2, Grades 2–3 Problem 6.** Both rings are blank. The guide keeps the example (0,1,2,4) → (1,1,2,4).
- **Should 3, pages 2 and 4, all bands.** The mats' stations are 36 mm instead of 40 mm, centres still 52 mm apart, and each mat moved 2 mm outward, so the old and new mats are 9 mm apart. The page-1 arrow from old to new is drawn between them. The guide says 36 mm.
- **Should 4, guide page 1.** Materials are 40 linking cubes per pair (the most an old and a new ring need with heights up to 5; the Grades 4–5 doubled run needs 36), with no number cards. The launch says "clear the old mat and move each new tower to the same letter on it" instead of swapping roles, and so does the route note. The hour starts after the run and drops the undescribed gap-card slot.
- **Should 5, recording space.** The three-station page in every band has six numbered A-B-C rows in two blocks under the mats. Each older Problem 3 target has a four-box "old" row under it. Grades 4–5 Problem 5 has four columns of letter boxes, each a start (move 0) and four moves, in place of two blank rings; the guide mentions them.
- **Should 6, pages 1 and 2, all bands.** "Use these big mats for all four-station starts." is deleted, and "An all-zero start takes 0 moves." moves from page 2 to the page-1 rules. That also settles K–1 Problem 3, whose key excludes (0,0,0,0); the guide's key now points to the rule.
- **Could 7, page 1.** The caption keeps "Edge A to B has gap 3, so new A is 3." and drops "All four gaps use the old ring.", which repeated the rule.
- **Could 8, Grades 2–3 Problem 5.** "Two rings count as different here only when…" is deleted, with the guide's matching sentence.
- **Could 9, Grades 4–5 Problem 6.** The starts are (2,5,1,0) and (4,10,2,0), 6 moves each, instead of the page-1 example (1,4,2,0) and its double. The guide's runs match.
- **Could 10, the theme name.** Pages, guide, route page and catalog now say "Four towers and differences", as the index does. The ZIP's file name is unchanged.

Deferred: could 11 (the bonus companion's "Grades 2-5" label and "within five rounds" wording). The bonus is built by its own ReportLab builder in `source/week-49-bonus/`, which the problem-file tools cannot store.

## Pages

Every page of every packet changed, at least in its header (could 10). Beyond the header:

- K–1: pp. 1 (rules, caption), 2 (mats, deleted sentence), 4 (mats, record rows) and 5 (the orders); p. 3 header only.
- Grades 2–3: pp. 1, 2, 3 (old rows), 4 and 5 (orders, blank rings).
- Grades 4–5: pp. 1, 2, 3, 4, 5 (letter boxes, the rule as a small table) and 6 (new starts).
- Adult guide: all four pages (title, materials, launch and hour on p. 1, keys on pp. 2–3, the route page).

## Verification

- `python3 src/check.py` checks every changed claim: the 24 orders (eight last 7 moves, sixteen 4) and the printed (0,2,1,4) and (0,1,4,2); the new scaling runs (6 moves each, every state doubled, tripling too); 40 cubes for an old and a new ring in every case used; the three-station repeat within the six rows; the predecessors; the one-move starts and the all-zero rule; the bound and the guide's example.
- `python3 review/verify_card_fixes_2026_10_23.py` reads the reference PDFs: the headers and rules, the deleted sentences, the printed ring values from their page positions, 36 mm stations with a 9 mm gap on pages 2 and 4 of every band, the numbered record rows, the old rows, the 80 letter boxes, and the guide's changed text. Run on the earlier PDFs, it fails at the first check.
- `facilitator-src/verify_pdfs.py` expected 40 mm stations and three guide pages, but the build appends the route page, so `verify_math.py` failed on every clean build; it now measures 36 mm stations, expects four pages and allows the route page's own right margin.
- The student packets built by the package match the problem-file tools' build in pages, text and 100-dpi pixels. Every changed page was rendered at 80 dpi and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify.py`, `verify_revision.py`, `verify_math.py` and this verifier. The student pixel allowances in `rebuild-pixel-allowances.json` are removed, since all three packets were rebuilt here.

The theme remains unpiloted. The respaced mats and record rows have not been tried with cubes.

## Footer ids, later on October 23

These changes reached the printed packets while their footers still carried the v2 ids of the earlier printings, so two printings shared each id. A footer-version sweep the same day raised `version` in `week.toml` to v3, so every packet, route packet and the key view now print v3 ids. The rebuilt packets differ from the previous ones only in the footer: the extracted text is identical after the id swap, and the differing pixels lie in the footer row. The guide's subtitle now reads "Final student packets v3"; no other guide text changed.
