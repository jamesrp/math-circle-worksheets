# Week 35: three coulds from an independent review, October 23, 2026 (Critic L)

An independent review of the day's revisions found no must or should in Week 35 and three clear coulds, made here. The packets are W35-k-1-v5 and W35-grades-4-5-v5; Grades 2–3 stays W35-grades-2-3-v4 and did not change, and neither did the kit page.

## Made

- **Could 6, Grades 4–5 Problem 3.** "A border matches after a 3 cm glide" now reads "A border matches after a flip over the middle line and a 3 cm slide along it." Problem 3 is on the return route and opens the published return view (`week-35-grades-4-5-return.pdf`) without Problem 2, the only place a glide is defined. The new wording names the move itself and still names the middle line, which the card's should 6 asked for (a flip over a perpendicular line would change the answer).
- **Could 7, K–1 Problem 4.** "Make another border like Problem 3's, with a longer slide." now ends "where the shortest slide is longer." Problem 3's own border G already matches after the flip and a 9 cm slide, so "a longer slide" asked for nothing new; the key wants a longer shortest slide (G8: 4 cm after the flip, where G uses 3 cm). Read either way, as the slide after the flip or the plain slide (8 cm against 6 cm), the answer is a border with a longer repeat, as the key says.
- **Could 8, guide p. 2.** The preparation estimate said "about 20 minutes to cut four sets (96 cards)". The group has five working groups (two K–1 pairs, two Grades 2–3 pairs, one Grades 4–5 trio), as the guide's pre-kit text budgeted ("five pair-sized material sets"), so it now says "about 25 minutes to cut five sets with scissors (120 cards ...): both sets on the K–1 and Grades 2–3 sheets, for two pairs each, and Set 1 for the Grades 4–5 trio." The print note (one sheet per table, a set for each pair or trio) was already right, and the kit page's "A table with one group can start with Set 1 only" fits the trio. The kit checker's console note for K–1 Problem 6 said the K–1 table "has one group, so Set 2 on the same sheet covers it"; it now says that both Problem 6 borders repeat every 6 cm and so go in the printed boxes, where two borders use at most 10 cards of one kind.
- The guide names the new packets (status line on p. 1, packet basis on p. 7) and its footer reads "Revised October 23 2026 (K-1 and 4-5 v5)", so a printed page shows which packets it goes with. `review/verify_card_fixes_2026_10_23.py` accepts the new wording, footers and guide lines as well as the old ones.

## Left

Grades 4–5 Problem 6, also on the return route, lists "slide, glide, flip and turn" without a definition of a glide; it asks about the child's own border from an earlier visit, so it was left. The return views still open with a rules-only page and keep each problem at its full-packet position on the page (the tools' behaviour).

## Verification

- `review/verify_critic_coulds_2026_10_23.py [build] [views]` tests borders G and G8 exactly with the package's motif (G matches after the flip and 3 or 9 cm; shortest slide after the flip 3 and 4 cm, plain 6 and 8 cm; every flip-and-slide d done twice is a slide 2d; G's 3 cm slide fails), counts the sets (5 groups, 120 cards, 25 minutes at the old rate, three sheets of two sets) and checks every changed sentence, the footers of all three packets, the guide's packet lines and footer, and the return view's Problem 3 page. It passes (29 checks with the views); `verify_card_fixes_2026_10_23.py` still passes (186 checks).
- K–1 p. 3, Grades 4–5 p. 2, the Grades 4–5 return view's Problem 3 page and guide pp. 1–2 were rendered at 80 dpi and inspected. Against the previous PDFs, K–1 differs only in Problem 4 and the footers, Grades 4–5 only in Problem 3 and the footers, the guide only in the status line, the preparation estimate, the packet basis and the footers; Grades 2–3 and the kit are pixel-identical.
- `verify_revision.py` passes against the new references, and a clean rebuild from the extracted ZIP passes it and both verifiers.
- The replaced PDFs are in the project's `week-35/archive-before-critic-coulds-2026-10-23/`, and the replaced ZIP in `source/week-35/archive-before-critic-coulds-2026-10-23/`.

All of this is digital checking. The week remains unpiloted and the kit physically unrehearsed.
