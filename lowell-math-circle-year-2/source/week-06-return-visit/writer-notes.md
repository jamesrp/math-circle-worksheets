# Week 6 return visits: writer notes

Student draft: `return-visit.pdf`, 3 US Letter pages, Problems 1--3. Source: `src/return-visit.tex`; portable builder: `src/build.sh`; writer checks: `src/check_answers.py`. The page headers identify actual entry bands: Grades 2--5, Grades 4--5, Grades 2--5. No independent K--1 version is claimed. Adult-supported play with a three-card weighing subcase remains possible outside this shared packet.

These are three different investigations, not three variants of one search puzzle. Problem 1 uses ternary measurements; Problem 2 changes the optimization objective through frequencies; Problem 3 changes fixed words into joined variable-length words and asks about segmentation. Current base content and novelty boundaries were supplied in the Week 6 outline; the writer did not import or alter base pages.

## Problem 1: guarantee through three outcomes

Exact printed objects: cards 1--9. A keeper chooses exactly one secret heavy label and keeps it fixed throughout a game. An attempt puts equal numbers on two pans, and the outcome is LEFT, RIGHT or BALANCED according to whether the heavy label is on the left pan, right pan or neither. All other cards are treated as equal weight. No actual weighing or unknown-heavy-versus-light model is used.

Optimal guarantee: **2 weighings**. Put 1,2,3 on LEFT, 4,5,6 on RIGHT, leaving 7,8,9 off the pans. LEFT leaves candidates 1,2,3; RIGHT leaves 4,5,6; BALANCED leaves 7,8,9. Put the first candidate on LEFT and second on RIGHT. LEFT names the first, RIGHT the second and BALANCED the third. One weighing has at most three outcomes and therefore cannot identify one of nine arbitrary secrets. This is a guarantee under truthful fixed-secret responses, not an average-cost statement. Other partitions/strategies can be valid; do not demand these exact labels.

Worked non-task visual: cards 10,11,12; keeper's secret 12; LEFT contains 10 and RIGHT contains 12; output RIGHT. It illustrates input, pan placement and report without giving the main 3+3+3 strategy. The keeper, rather than the printed page, enforces the outcome rule.

Diagram parameters: nine outline cards each 0.52 by 0.52 inches, with 0.73-inch pitch. Main grouping pans each 3.05 by 1.35 inches, separated by 0.58 inch. The blank lower record area is 6.68 by 2.25 inches. These are not calibrated physical-fit claims.

## Problem 2: total cost across an unequal batch

Exact printed batch: **A, A, A, A, B, B, C, D**. A plan can ask whether the hidden letter belongs to any selected subset, and later questions can depend on earlier responses. Every search begins with A, B, C, D possible; the same plan is reused. Earlier batch outcomes must not remove letters from later searches. A singleton needs no confirming question. This convention is printed explicitly so depletion of known batch counts does not change the optimization problem.

An optimal plan asks `Is it A?`; if no, `Is it B?`; if no, `Is it C?`. The terminal depths are A:1, B:2, C:3, D:3, and the batch total is **4x1 + 2x2 + 1x3 + 1x3 = 14**. Its largest individual cost is **3**. A balanced two-question plan costs 16 and has maximum 2; total-cost optimization and worst-case optimization differ.

For completeness: remove questions that do not split the current possibilities. A remaining full binary tree with four terminal letters has depths either (2,2,2,2) or (1,2,3,3). In the second shape place the most frequent letter at depth 1 and the next most frequent at depth 2: swapping a larger frequency deeper than a smaller frequency can only increase total cost. Thus no valid plan beats 14. The check script enumerates both shapes and every distinct depth assignment.

This page requires counting repeated cards and tracking conditional questions; its genuine independent entry is Grades 4--5. An adult may physically lay out the eight cards and count questions after completing each message. Recording the plan once and four terminal depths is enough; children need not maintain concurrent query tallies and frequency tallies. The one-message depths and batch total have printed recording lines.

Diagram parameters: 8 cards each 1.08 by 0.77 inches, four columns with 1.38-inch pitch and two rows with 1-inch pitch. Blank plan area 6.68 by 3.02 inches. No sorting/transcription task is added.

## Problem 3: joined counter words

Counter convention: R = red, Y = yellow. Repetition of message letters is allowed. Messages have finite length; no spaces or word separators are transmitted. Only rows made by concatenating a book's words count as transmitted rows.

Exact books:

| Book | A | B | C |
|---|---|---|---|
| 1 | R | RY | Y |
| 2 | R | YR | YY |
| 3 | R | RY | absent |

**Book 1 is ambiguous**: B and AC both yield RY. Another collision: AB and AAC both yield RRY. Finite enumeration confirms collisions.

**Book 2 is uniquely decodable for every finite message.** If the next counter is R, it must be A. If it is Y, a second counter is required: YR is B, YY is C. None of these three words begins another, so that first letter is determined; repeat on the remaining suffix. This is the prefix-free sufficient condition. The example row RYRYY decodes ABC.

**Book 3 is also uniquely decodable for every finite message**, even though A's word R is a prefix of B's word RY. Every Y must attach to the R immediately before it, forming B; an R not followed by Y forms A. Equivalently, decode from the right: final Y forces a final RY/B, while final R forces A. Remove that forced word and repeat. This shows that the prefix-free condition is sufficient but not necessary. Rows such as Y or RYY are invalid rather than ambiguous. Example row RRYRY decodes ABB; RYRR decodes BAA.

Worked non-task visual: M = YR, N = R; input MN; intermediate YR | R; output YRR. The intermediate separation line shows what disappears during concatenation. It does not expose a main-book collision. Red/yellow counter circles carry R/Y text for grayscale readability.

Diagram parameters: three codebook cards each 2.05 by 2.03 inches, with 2.30-inch pitch. The non-task conversion counter circles are 0.27-inch diameter, 0.37-inch pitch; the separator stays only in the intermediate. Blank record area 6.65 by 3.50 inches. It is for drawing/recording, not a counter mat.

## Writer-stage verification and limits

- `check_answers.py` passed: two-weighing response pairs distinguish all nine labels; optimal batch cost is 14; Book 1 collides; Books 2 and 3 have no collision among messages of 1--6 letters; the MN conversion gives YRR. The two arbitrary-length uniqueness arguments above are required in addition to the finite check.
- pdfLaTeX compiled three pages with no overfull or underfull boxes reported.
- Every page was rendered with PyMuPDF and visually inspected: headers, footer ids, consecutive problem numbers, cards, pans, codebooks and worked conversion are legible; no clipping or overlaps were observed. Rendered PNGs are in `render/`.
- The sources have been rebuilt from a clean extracted source archive within this draft run; page count and content match.
- These are writer-stage **unpiloted** drafts. No physical balance, material-fit rehearsal or classroom use is claimed. The independent critic/math/reviser stages remain outstanding.
