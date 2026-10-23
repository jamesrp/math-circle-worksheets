# Week 50: fixes from the review card, October 23, 2026

The review card is `plans/review/week-50.md` in the project, with its math check `plans/review/week-50-math.md`. The week was first stored as problem files with no wording change; these fixes were then made in the problem files (`problem-files/problems/*.md`, `problem-files/figures.py`) and the guide in `facilitator-src/content.json` and `facilitator-src/route-note.json`.

## What changed

- **Should 1, p. 1 in every band, and older Problem 2.** The worked example's pieces are lettered in path order (A right 10, B up 20, C right 30, D up 10), and one 70 mm bar holds them end to end in that order, captioned "the pieces in a row", in place of a 40 mm "right pieces" bar and a 30 mm "up pieces" bar. Grades 2–3 and 4–5 Problem 2 ends "Find the exact length of each staircase." Collecting the right and up pieces stays a hint in the guide (p. 3), which no longer says the opening diagram does it.
- **Should 2, Grades 4–5 Problem 5.** The strip is 7.5 mm above and below the diagonal, half of Problem 4's, and the problem reads "Make a staircase inside this narrower strip with as few turns as you can. Is it shorter than your staircase in the wider strip? Explain your answer." Key: 16 turns, by U7.5, eight R20 with U15 between them, U7.5; with 15 or fewer turns there are at most 8 horizontal pieces of at most 20 mm, one of them an end piece of at most 10 mm, so they cover at most 150 mm. The card's note that 15 turns suffice applies to an 8 mm strip, not to this one.
- **Should 3, Grades 4–5 Problem 7.** It ends "Explain your answer."
- **Should 4, Grades 2–3 Problem 5.** "Could a path with leftward pieces be shorter than 280 mm?"
- **Should 5, p. 1 in every band.** B's label (the up piece of 20, "C: 20" before) is at (31,46), beside its piece, instead of on the gray outline.
- **Should 6, guide p. 1, launch.** With fix 1's single bar, the launch follows the example piece by piece, A to D, and straightens the string beside the 70 mm bar.
- **Should 7, guide pp. 1 and 4.** One first-visit plan: 0-5 running around, 5-9 launch, 9-48 Problems 1-3 and then Problem 4 for any pair that finishes, 48-55 share, 55-60 reset. The route page says the same, and Problem 4 is in the first-route packets as well as the return ones.
- **Could 8, Problem 3.** K–1: "Make a staircase inside the gray strip. Compare its length with this one using string." Older bands: "Make a staircase inside the gray strip. Compare the two staircase lengths with the diagonal's length." The guide's key adds that the printed staircase leaves the strip, so any staircase inside it is closer.
- **Could 9.** "clipped by the rectangle" (older p. 4, 4–5 p. 5), "It goes left once" (4–5 Problem 6) and "A straight diagonal is 200 mm long." (2–3 p. 5) are deleted.
- **Could 10, guide materials.** K–1 may use a 30 cm pipe cleaner instead of string; it holds its corners and leaves about a 2 cm tail past F. Untried.
- **Could 11, guide overview.** A "Fewest turns" paragraph states the eight-turn optimum and its bound, that 9 turns are needed if pieces may not touch the boundary, and the 16 turns of the 7.5 mm strip.

Nothing on the card was left. The bonus companion was not reviewed by the card and did not change.

## Pages

- K–1: pp. 1 (example) and 3 (Problem 3) changed; pp. 2, 4 and 5 unchanged.
- Grades 2–3: all five pages changed (p. 1 example, pp. 2–5 wording; p. 5 also loses its caption).
- Grades 4–5: all six pages changed (p. 1 example, pp. 2–4 and 6 wording, p. 5 the 7.5 mm strip and its problem).
- Adult guide: pp. 1 (overview, materials, launch, hour), 2 (Problem 3 key), 3 (Problem 5 key, hint) and the route page; still four pages.

Unchanged pages match the previous print PDFs in text and 100-dpi pixels.

## Verification

- `python3 src/check.py` checks every changed claim: the example's four pieces in path order and the 70 mm bar; B's label 6 mm from B and at least 10 mm from any other piece; the printed four-step staircase's 30 mm gap; fewest turns 8 in the 15 mm strip and 16 in the 7.5 mm strip, each by the counting bound, an exact witness and lattice searches; 9 turns without the boundary (bound and witness); Routes A and B at 280 + 2 × 40 = 360 mm; the pipe cleaner's 2 cm tail; and the contiguous hour.
- `python3 review/verify_card_fixes_2026_10_23.py` reads the reference PDFs: the page-1 bar (10, 20, 30 and 10 mm end to end) and labels in every band, the new and deleted wording in every band, the 7.5 mm strip's vertices on Grades 4–5 p. 5, and the guide's changed text. Run on the earlier PDFs, it fails at the first check.
- `facilitator-src/verify_pdfs.py` expected three guide pages, but the build appends the route page, so `verify_math.py` failed on every clean build; it now expects four pages and allows the route page's own right margin. `facilitator-src/verify_math.py` checks the narrow witness against 7.5 mm and the 16-turn bound.
- The student packets built by the package match the problem-file tools' build in pages, text and 100-dpi pixels. Every changed page was rendered at 80 dpi and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify.py`, `verify_revision.py`, `verify_math.py` and this verifier. The student pixel allowances in `rebuild-pixel-allowances.json` are removed, since all three packets were rebuilt here.

The theme remains unpiloted. The pipe cleaner and the relettered example have not been tried with children.

## Critic follow-up, later on October 23, 2026 (v3)

An independent critic (Critic C) read the card-fix release and found two shoulds, now made:

- **Grades 4–5 Problem 5.** It asked for the fewest turns "inside this narrower strip" without Problem 4's "Its pieces may follow the strip's boundary." The 16-turn witness (U7.5, then R20 pieces with U15 between, then U7.5) has every corner on the boundary; strictly inside, a horizontal piece spans less than 20 mm (an end piece less than 10 mm), so 16 turns fall short and the minimum is 17. Problem 5 now carries the same sentence as Problem 4, so the key's 16 holds, and the guide's overview and Problem 5 key add "(17 if no piece may touch the boundary)".
- **Version.** The footers were still F50-K/23/45-v2, the ids of the October 4 packets, though every older-band page had changed. `week.toml` now says v3 and the guide's header "Final student packets v3".

To keep the guide at four pages, its materials paragraph now says "The guide's own diagram is deliberately smaller" (it was "The diagram on the next guide page is deliberately smaller").

Checks: `review/verify_card_fixes_2026_10_23.py` reads the new Problem 5 and the overview's 17; `plans/review/checks/week-50/check_critic_fixes.py` (repository) checks both minima exactly (16 with the boundary, 17 strictly inside, with fraction witnesses and the counting bound), the v3 footers, and that only the footers and 4–5 Problem 5 changed on the student pages. The previous PDFs and ZIP are in the week's `archive-before-critic-fixes-2026-10-23/` folders.
