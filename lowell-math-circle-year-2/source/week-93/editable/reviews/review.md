# Week 93 adversarial review

## Verdict

Revise the exact-versus-approximate transition on page 3 before delivering this draft. The five-page packet has correct mathematics, a useful concrete opening, substantial continuation questions, and clean rendering. Its largest usability risk is that children are asked to produce a guaranteed range using a repeating-decimal calculation before the warning about rounded bounds appears. The supplied fraction cards also need to be genuinely movable without destroying the page on which children must explain their answer.

This review follows the consolidated-PDF override: no K–1 packet or fixed three-band quota is required. I inspected every page of a fresh render of `draft/students.pdf`, read `draft/src/students.tex`, and checked the numerical claims with exact rational arithmetic. No student files were edited. Physical cutting rehearsal and classroom piloting remain untested. Age-fit judgments below are hypotheses, not classroom findings.

## Priority revisions

### 1. Put exact-number support before the first repeating quotient (page 3, Problem 3)

The third input, 2 by 10, produces sides 6 and 10/3. A four-function calculator displays a rounded value for 20 divided by 6. Yet the page asks for the “tightest range you can guarantee” and provides blanks that look equally suitable for exact values and calculator displays. The distinction between exact fractions and estimates first appears on page 4. This is too late for the first certificate-producing task and falls directly under the brief's prohibition against silently treating rounded decimals as exact certificates.

The particular usual downward rounding of 10/3 would still give a valid, slightly looser lower bound; the issue is not that this example necessarily creates a false inequality. It teaches no defensible rule for deciding whether a rounded value remains a bound and can make an approximate rectangle look area-preserving when it is not.

Move the concise exact/rounded convention before Problem 3 and provide the exact quotient needed here, or choose an initial terminating quotient and introduce the supplied exact fractions on page 4. Keep the children's choice of comparisons and justification open. A calculator estimate can locate an exact fraction approximately on the line, but the interval endpoints should remain exact labels. Fraction comparison is in the stated prerequisite route; generating and simplifying fractions should not quietly become a new prerequisite.

### 2. Clarify the finite choice in “tightest range” (page 3, Problem 3)

“Which two lengths give the tightest range you can guarantee” presumably means among the old and new lengths just marked. Taken literally, it has no tightest answer: a child may use further calculations to narrow the interval indefinitely, and the square-root endpoint itself would give a degenerate interval. Make the selection domain explicit with a small edit such as “Which two of these lengths…”. This preserves the intended comparison without revealing the answer or adding procedural scaffolding.

### 3. Make the card sort physically usable (page 4, Problem 4)

The prompt says to put the cards in order, but they are fixed boxes on the same sheet that contains the explanation space and Problem 5. Children can infer that they should copy letters, or an adult can supply another printout, but neither is specified. Sorting is the mathematical action here; the project guidance specifically favors movable cards over transcription.

Give an explicit cut instruction and a usable arrangement, or supply a separate card copy as part of the printable materials. A second copy of page 4 could work with a minimal preparation note in the eventual package; do not force a child to remove the middle of their only working page. Keep the exact fractions and shuffled order.

## Mathematical and instructional concerns to test, rather than automatic redesigns

### The geometric reason for a bracket has little concrete work before Problem 3

Problem 1 finds equal-area integer rectangles; Problem 2 packs a rectangle into a larger average-side square. Neither explicitly has children locate an equal-area square between the original short and long sides. Page 3 then asks for guaranteed intervals, and page 4 asks for an explanation of the certificate. This is a meaningful reasoning demand, but it is a second new idea arriving alongside the reshaping algorithm and number-line representation.

A child could complete the procedural parts of Problem 3 by copying the two new side lengths into the bounds blanks without understanding why either is a bound. Test whether the normal launch makes the comparison accessible: a square built on the short side has too little area, and a square built on the long side has too much. If adult rescue is needed throughout, give this comparison a concrete task before asking for several guarantees. Do not print the theorem as a recipe or append explanations to every row merely to address this concern.

### The card values reduce iteration arithmetic, but do not eliminate it

Checking that A leads to C requires averaging 24/7 and 7/2 to get 97/28, then dividing 12 by that fraction. Checking the exact lower certificate by squaring C directly involves 336 squared and 97 squared. Those are substantial fraction demands for the main Grades 3–5 route. The task has a lighter route: use the equal-area rectangle relationship to reason about bounding squares, and order the supplied cards using side lengths. However, “so each card follows from one reshaping move” can reasonably be read as requiring all the fraction arithmetic.

Retain the substantive proof opportunity. In later facilitator work, explicitly distinguish the children’s comparison/reasoning from arithmetic the adult or calculator may handle. If revisions add support, make it exact-value support, not instructions that solve the ordering or the enclosure argument. Do not require tiny physical fraction strips.

### Page 5 is an advanced continuation, not a general expectation for every fourth grader

Problem 6 asks for a general geometric identity; Problem 7 asks for arbitrary precision and impossibility of finite termination for every unequal-sided rectangle. These are worthwhile mathematical destinations. They are also a sharp jump from the preceding numerical cases, especially the universal convergence claim. The outline expressly makes the general algebraic gap proof adult material unless children are ready.

Keep these questions available rather than deleting the depth. Treat page 5 as readiness-dependent in the eventual route description; consider a header that reflects readiness as well as grade if needed. Do not assume that a standard launch alone makes the universal explanation an independent task for all children. General reasoning can be done geometrically; algebra is not intrinsically required.

## Page-by-page audit

- **Page 1, Problem 1:** Clear, concrete entry. The 24-by-20 grid can contain the 1-by-24 rectangle and the other factor-pair rectangles. All four cases are 1×24, 2×12, 3×8, and 4×6; 4×6 is closest to square. Rotation convention is stated once. Consider whether grid-aligned arrays are established in the launch, since “every rectangle” relies on the ordinary tile-array interpretation.
- **Page 2, Problem 2:** Two useful cutting cases, large enough for handling. Source scale is equally 1.5 cm per unit in both axes. Case A is a 9×3 cm rectangle and 6×6 cm target; case B is 6×3 cm and 4.5×4.5 cm. All four shapes use the same physical unit. Labels match the geometry. The missing squares have sides 2 and 1 units. Each has a simple one-cut construction: remove the excess strip beyond the target width and reposition it. The B piece must be turned. The page itself does not give these solutions, appropriately. Cutting fit is digitally checked, not physically rehearsed.
- **Page 3, Problem 3:** The non-task worked example is a strong feature: 1×3 input, joined lengths and halving as an intermediate, then 2×(3/2) output. All dimensions and areas are correct. It precedes first use and does not reveal the main gap identity. Three rows give useful contrasting results, but exactness support and the comparison domain need the edits above. Number lines are readable and give ample space for these first-round values.
- **Page 4, Problems 4–5:** Fraction cards are correct, large, and legible. The task leaves ample explanation space. Problem 5 meaningfully connects bounds to exact square checks. Its endpoints may be 3.46 and 3.47; their exact squares are 11.9716 and 12.0409. Neither is the square side. This does not prove that no terminating decimal could be the side, and the prompt does not ask for that stronger claim. Do not broaden the expected answer inadvertently.
- **Page 5, Problems 6–7:** Diagrams are legible, square axes have equal scale, and “not to scale” protects the generic illustration from a measurement interpretation. There is room to draw and argue. No universal claim is printed as a fact for children to copy. The readiness concern above is the main issue, not layout.

## Exact mathematical audit

For positive a≤b and m=(a+b)/2, the other new side h=ab/m satisfies a≤h≤sqrt(ab)≤m≤b. For unequal sides, all the relevant endpoint improvements are strict. The extra area is m²−ab=((b−a)/2)². The new gap is (b−a)²/[2(a+b)], strictly smaller than half the old gap, so repeated bounds shrink to zero. Equality h=m would imply (a−b)²=0; hence no move starting from unequal positive sides produces the exact square, even when the target square side is rational.

Problem 3 outputs are (3,4), (4,9/2), and (10/3,6). All preserve their stated areas and bound the corresponding square side.

Problem 4 order is B→D→A→C. Every card has exact area 12. Gaps are 4, 1, 1/14, and 1/2716. Card C gives the tightest displayed interval, [336/97,97/28]. Its lower square is 112896/9409<12 and its upper square is 9409/784>12. No numerical correction is needed.

## Format and completion evidence

All five rendered pages have consistent headers, footers, and page numbers, continuous Problem 1–7 numbering, no Name/Date fields, no decorative titles, and no clipping or overlapping elements. Body text and fractions are readable. The packet has enough potential work for the intended hour, especially with cutting and explanation; four or more pages per generic band are superseded by the authorized consolidated-packet override. No facilitator guide was requested for this stage. Remaining verification limits are physical rehearsal, classroom piloting, and readiness-dependent adult support; the visual and exact numerical checks do not establish those.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.
