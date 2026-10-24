# New-theme drafts for the organizer's review

Student pages for the four recommended themes in [the scouting list](../README.md#recommended-top-four), drafted on October 24, 2026 with the [worksheet workflow](../../../worksheet-workflow/README.md). Each one went through the full workflow, with every stage run by a fresh agent: the writer stage, an adversarial review (`review.md`), an independent math check that re-solved every printed board with its own code (`review-math.md`), and a revision that addressed both reviews.

**Status.** These are drafts awaiting the organizer's review. They are unpiloted, and no kit has been rehearsed with real materials. The pages say "Week NN" and the packet ids use NN, because a week number is assigned only on approval. As with every output of the workflow, there are no facilitator guides yet.

| Draft | Header topic | K–1 | Grades 2–3 | Grades 4–5 | Materials | Not yet tried physically |
|---|---|---|---|---|---|---|
| [towers-from-either-end](towers-from-either-end/) | Towers from either end | 7 pp. | 7 pp. | 6 pp. | snap cubes, printed slot strips (plain, then red/blue) | towers standing in 25 mm slots |
| [games-decided-before-they-start](games-decided-before-they-start/) | Breaking and drawing games | 7 pp. | 7 pp. | 9 pp. | card "chocolate bars", token counters, pencils | 5–8 card bars per pair (the outline said 6); counters on the dot boards |
| [poisoned-cookie](poisoned-cookie/) | Poisoned cookie | 6 pp. | 5 pp. | 6 pp. | 25 mm counters, a 15 cm bite card | the bite card on neighbouring boards (the build checks the spacing) |
| [who-beat-whom](who-beat-whom/) | Who beat whom | 5 pp. | 6 pp. | 8 pp. | animal cards, 10 cm arrow cards, the K–1 big board | arrow cards in the big board's lanes |

What the reviews changed, in brief:

- **Towers from either end.** K–1 Problem 1 can now record a tie. "Play as well as they can" is defined where a page asks "by how many". The slot-number record has a worked example. Rows that invited a false rule ("always take the shorter end", "take the taller end") were replaced with checked rows. Problem 9 in grades 2–3 no longer has its answer printed in Problem 7. The red/blue strips begin on a later page, so children can be given them as a second set after playing on plain strips.
- **Breaking and drawing games** (outline: "Games decided before they start"). The header no longer announces the discovery. The token rule now says each end of a line needs its own token, so a loop needs two. Lines may not cross themselves or another line; both gaps had let game lengths vary and changed winners. Grades 2–3 now record line counts, and K–1 players swap who goes first. In grades 4–5 Problem 10, a line through a cross counts as two pieces.
- **Poisoned cookie.** "A position where the player whose turn it is cannot make sure to win" replaces "an L position", which a child could read as an L shape. The strategy-stealing question now asks which step of the argument breaks. Square boards are "bigger than one cookie". The make-a-board problems start from a full grid, so the answers are boards that can occur in a game. Full-size boards that share a page sit far enough apart for the bite card.
- **Who beat whom.** Every K–1 problem now says which board to use, and the big board's lanes hold the 10 cm arrow cards. Grades 2–3 Problem 3 has a recording diagram, the line-up answer gaps are wider, and grades 4–5 Problem 7 has larger diagrams and six blank pentagons for four possible answers, so the number of blanks no longer hints at the answer.

## Rebuilding

Each `src/` folder rebuilds its three PDFs into the draft folder with Python 3 and pdfLaTeX. The commands are `python3 gen.py` (towers), `sh build.sh` (breaking and drawing games; who beat whom, which writes into `src/`) and `python3 build.py` (poisoned cookie), each run inside `src/`. Each build also runs that draft's answer checker. On October 24 all four rebuilt from a clean copy, with text identical to the committed PDFs.

## After approval

Assign a week number. Store the week as [problem files](../../../lowell-math-circle-year-2/source/problem-files/README.md). Write a facilitator guide that opens with the theorem-first overview AGENTS.md asks for; the math reviews' answer keys are a starting point. Add a catalog record (`catalog/weeks/`) and run `python3 catalog/build.py`. Then record the week as unpiloted.
