# Week 33 independent mathematical review

**Pass.** The shared Grades 2–5 packet checks out completely: all seven tasks, every supplied necklace, every supplied code card, and the clockwise wraparound example are mathematically valid. All five rendered pages were inspected. No located mathematical correction is required.

`independent-check.py` enumerates actual words, exact rotation and reflection orbits, all proper colorings, all shortest universal rings, and every shorter binary ring. It writes `checks.json` and uses no writer checker or answer notes.

| Page / problem | Requested outcome independently verified |
|---|---|
| 1 / 1 | Reading clockwise from the top, the supplied rings are a=AABABBBB, b=ABBBBABA, c=BAABABBB, d=AABBABBB, e=ABBBABBA, f=BBAABBAB. Turns alone give **{a,c}, {b}, {d,f}, {e}**. Turns and flips give **{a,b,c}, {d,e,f}**. Both reflection mergers are real; fixed A/B names are preserved. |
| 2 / 2 | Four- and six-bead rings can be made, uniquely up to turn, by alternating A and B. Five cannot: alternation makes the closing neighbors equal. Full fixed-position enumeration gives 2,0,2 valid words respectively. |
| 3 / 3 | Exactly six rotation classes exist: **ABABC, ABACB, ABCAC, ABCBC, ACACB, ACBCB**. Exhausting all 3^5 fixed-position words gives 30 valid proper colorings, split into six five-member rotation orbits. Named colors are not permuted; reversals are not merged. The supplied eight recording rings leave sufficient room. |
| 4 / represented example | The example's clockwise word from the top is ABAAB. Starting at the upper-left B reads indices 4→0→1, hence B→A→B, across the closing gap. The output card BAB and arrow direction are correct. |
| 4 / 4 | Minimum length four, with exactly one rotation class **AABB**. Its four clockwise pair windows are AA,AB,BB,BA, each once. All four pair cards are supplied exactly once. |
| 4 / 5 | A ring with n beads starts n windows. Four different cards require at least four starts, so no shorter ring works. Exhaustion of all lengths 1–3 independently confirms the lower bound. |
| 5 / 6 | Minimum length eight. **AAABABBB** is a valid witness, with windows AAA,AAB,ABA,BAB,ABB,BBB,BBA,BAA. All eight triple cards are supplied exactly once. Eight distinct cards require eight starts. |
| 5 / 7 | Exactly two shortest rotation classes exist: **AAABABBB** and **AAABBBAB**. Exhaustion of all 256 eight-letter words gives 16 solutions, two eight-member orbits. The second has windows AAA,AAB,ABB,BBB,BBA,BAB,ABA,BAA. Reversal maps each class to the other; neither is its own flipped class. All binary lengths 1–7 were also checked and yield no solution. |

For window tasks, one start at every bead and cyclic wrapping are essential; both are printed. The worked example demonstrates wrapping before the first window task without giving a target solution. Keeping the ring face up and names fixed correctly distinguishes the two triple-window rotation classes. Problem 7 asks about the flipped copies after that collection is formed and does not silently change its equivalence convention.

Every supplied ring and recording ring has the correct number of spots. Source coordinates place spots at equal angular steps, with x=y scaling; adjacent working spots do not overlap and have 24 mm diameter for the requested ≥20 mm counters. Small rings are recording/reference diagrams. Mathematical geometry does not verify physical card, counter, tracing-overlay, or viewer fit; those procedures and classroom pacing remain untested.
