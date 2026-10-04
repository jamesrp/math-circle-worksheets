# Independent review of the Week 21 draft

## Verdict

The packet is mathematically coherent, unusually faithful to the requested student-page register, and physically usable at 100% scale. It needs a small wording revision, principally to K–1 Problem 2, rather than a rebuild. I found no incorrect constructed optimum, illegal intended contact point, clipped element, overlapping text, or undersized working board. The older-band sequence reaches the intended reflection argument, restricted-contact issue, and uniqueness without printing the solution method.

Two wording issues deserve attention before printing. The first changes the possible answer to a K–1 question; the second leaves the grades 2–3 optimality explanation less definite than the central mathematical purpose requires. A further K–1 workload concern is a judgment call, not an established mathematical or production failure.

## Review performed

I read `PROMPT.md`, independently rendered all three delivered PDFs at 80 dpi, and visually inspected every page: seven pages each in `k-1.pdf`, `grades-2-3.pdf`, and `grades-4-5.pdf`. I inspected `draft/src/build_packets.py` for exact geometry and recomputed reflected crossings and relevant lengths separately rather than accepting the author's assertions or `geometry-checks.json` as verification. No draft file was changed. Review renderings are in `review-render/`.

## Findings, in priority order

### 1. Revise the ambiguous comparison in K–1 Problem 2 (page 2)

The task says:

> Make routes from A to B and A to C that touch at the same spot. Can either use less string?

There are two reasonable interpretations:

- Can one of these two routes use less string **than the other**, while they share the contact point? No: B and C are reflected partners, so the two routes have equal length at every common contact point.
- Can either route use less string **than it currently uses**, by moving the contact point? Usually yes: unless the selected point is already optimal, moving it toward the straight A–C crossing shortens both routes.

This matters especially for a problem meant to make sense to a nonreader after one hearing. The adult should not have to repair the question or decide which true answer counts. A minimal correction is “Can one use less string than the other?” Keep the shared-contact condition in the first sentence. No hint or extra explanation is needed on the student page.

### 2. Make the universal target explicit in grades 2–3 Problem 3 (page 3)

The explanation request is:

> Explain how you can tell whether a different contact point could make a shorter route.

A child can reasonably answer this as a procedure for checking another trial: make that route and compare the two pieces of string. That answers how to test a different point, but does not establish that the chosen route is shortest against all allowed points. The opening instruction does ask for the shortest route, and Problem 2 supplies an appropriate equality observation, so this is a weakness in the requested explanation rather than an erroneous problem.

Prefer a goal such as “Explain why no other contact point gives a shorter route.” This makes the necessary conclusion clear without supplying reflection, straightening, a diagram of the answer, or any other method. The corresponding grades 4–5 problem already explicitly includes routes not drawn and avoids this finite-testing loophole. Its phrase “no longer than every other allowed route” could also be made more natural as “no other allowed route is shorter,” but its intended quantifier is sufficiently explicit in context.

### 3. Reconsider the depth of late K–1 Problem 6 (page 6)

After Problem 3 has asked for a shortest route, Problem 4 for two shortest routes, and Problem 5 for three shortest routes with a vertical boundary, Problem 6 returns to one ordinary two-endpoint minimization. Its two pre-drawn guesses supply a concrete comparison, but once the child has the construction, beating them and drawing the optimum add little new thinking. This is the clearest risk against the organizer's requirement that each numbered problem sustain about five minutes, rather than a claim that seven pages automatically provide too little work.

The page would have more value as an earlier concrete entry into optimization, or if the author chose a genuinely contrasting mathematical demand for this late slot. Do not address this by adding routine “explain,” “notice,” or “compare with a partner” follow-ups. K–1 Problem 7 is a meaningful inverse problem and should remain available to quick children. The current K–1 packet has real mathematics and the same page count as the older packets; there is no basis for calling the entire band trivial or severely under-supplied.

## Mathematical audit

All coordinates below are independent review checks in the source drawing's centimetres, not proposed student-facing notation. Horizontal coordinates are local to the board; the common horizontal line is at y = 8.7. Vertical-board contacts are given by their y coordinate.

| Configuration and use | Check |
|---|---|
| Equal-height board, K–1 P1 | The optimum is x = 8.4. Contacts equally spaced on either side have equal route lengths, so the requested two distinct equal-length routes exist within the permitted segment. |
| Reflected B/C board, every band P2 | B is at (13.5, 13.1) and C at (13.5, 4.3), exactly opposite across y = 8.7. At every common contact M, MB = MC and therefore AM + MB = AM + MC. The straight A–C crossing is x ≈ 8.66436, within the permitted segment. |
| Unequal-height board, every band P3 | The reflected optimum is x = 6.3, not the midpoint 8.3 of the perpendicular feet. The minimum is about 15.7493 cm. This is a useful configuration for defeating a midpoint guess. |
| Comparison board, K–1 P4 and older bands P1 | AB is shorter: minima are about 13.2608 cm for AB and 14.2562 cm for AC. Both reflected crossings are interior. |
| Vertical board, K–1 P5 and grades 2–3 P4 | The three contacts are y ≈ 6.88395, 8.67565, and 11.28444 for AB, AC, and BC respectively. All are inside the drawn segment from 0.6 to 17.6. All needed reflections fit on the page. |
| Pre-drawn guesses, K–1 P6 | Their lengths are about 16.8107 cm and 17.3471 cm; the true minimum is about 16.0963 cm at x ≈ 6.61524. Thus a route shorter than both genuinely exists. |
| Prescribed-contact inverse board | There are infinitely many valid start points on the ray extending from P away from the reflection of B, in the upper half-plane. Plenty of this ray lies on the supplied sheet, so two distinct drawable answers exist. “All the places” in grades 4–5 P5 properly leads to that ray. |
| Equal-minimum comparison, grades 2–3 P6 | The two squared minima are both 164; the common length is about 12.8062 cm. Their contacts differ (x = 8 and x = 6.2). The “same amount” option is necessary and is present. |
| Shared-contact board, grades 4–5 P4 | AB and CD both attain their minima at x = 6.2, even though the respective minimum lengths differ. The intended common-contact answer is correct. |
| Restricted-contact board, grades 2–3 P7 and grades 4–5 P6 | The unrestricted contact is x = 6.5. It is inside C–D = [4.5, 8.2] and C–F = [4.5, 14.9], and outside E–F = [10.2, 14.9]. The tasks ask whether the original optimum remains allowed/optimal; they do not claim an unproved endpoint solution for E–F. |
| Uniqueness board, grades 4–5 P7 | The optimum is an interior contact at x ≈ 10.51818. Equality in the straightened triangle inequality permits only this crossing, so two distinct optimal contacts are impossible. |

The opposite-side A–C route on Problem 2 is a valid auxiliary comparison under the printed two-straight-segment rules. It should not be mistaken for applying the same-side theorem to opposite-side endpoints. There is no printed claim about curved boundaries, multiple reflections, angles of light, calculus, or strict convexity.

## Page design and production

- All 21 pages are US Letter, with the expected one-line header, numbered “Problem N:” label, one-line packet footer, and correct page number. There are no extra activity headings, captions, cheerleading, characters, worked answers, or lettered solution steps.
- Every page has the board needed for its task. The nominal working region is 16.8 × 18.2 cm, satisfying the minimum 15 × 18 cm requirement. The large white areas are useful space for string, drawing, reflection, and explanations; they are not a layout defect.
- The horizontal boundary is 15.6 cm long; the vertical one is 17 cm. The horizontal fold line leaves enough paper below it for every required reflected point, even the high point on the restricted board. The vertical line leaves usable paper on both sides.
- The current renders have readable point labels, distinct line-end marks, clear solid/dashed trial routes, and no text/diagram/footer collisions. Small filled dots provide unambiguous centers, as the rules require.
- All fixed-board routes fit comfortably within the supplied 60 cm string lengths. No extra tools, measured angles, numerical student calculations, elastic, pegs, cutting, or oversized print scale are required.
- The rules explicitly require two straight legs, contact between the end marks, no travel along the line, and use of dot centers. They are stated once, as requested.
- The K–1 problems themselves stay within one or two sentences. The older packets' explanation requests are attached to actual mathematical claims: invariance, optimality, inverse characterization, legality, or uniqueness.

## Recommended disposition

Correct K–1 Problem 2, tighten the grades 2–3 optimality question, and consider whether the late K–1 repeated minimization earns its own five-minute slot. Preserve the clean full-size layouts and the existing geometry. Do not add a facilitator guide or put the reflection construction on the student pages; neither is part of the requested deliverable.
