# Week 94 adversarial student-packet review

Reviewed the exact writer brief and its authorized short K–1 exception, all eleven draft PDF pages (K–1: 2; grades 2–3: 4; grades 4–5: 5), the LaTeX sources, the preparation README, and `check_math.py`. I independently rendered the PDFs into `review-renders/` and inspected every page. The mathematical check script passes. No student file was edited.

**Disposition: revise the specific issues below; retain the investigations and mathematical depth.** The pages are legible, comfortably spaced, and free of visible clipping or overlapping text. The short K–1 entry is authorized and honestly described as short in the source README. The upper continuation should remain available as a return visit; its difficulty alone is not a reason to delete it.

## Findings requiring revision

### 1. K–1 placement rules and first worked example do not establish the broken-ruler action

**Location:** K–1 p. 1 shared example and Problem 1, p. 2 Problem 2; `k-1.tex` lines 3–12 and 20–25.

The visual demonstrates putting a one-unit strip on a square, but never places that strip against the numbered ruler, shows which edges line up with which ticks, or shows how the visible endpoints are recorded. Problem 2 then asks for “every place” with one end at 7. Its verified answer excludes D extending left from 7 to the unprinted location 1, although the printed problem never says both ends must land on the printed ruler. More literally, it does not establish that strips lie parallel to the ruler rather than turning around the given end. These are essential legal-placement conventions, not solution hints.

**Required change:** Add one brief shared rule establishing alignment and the requirement that both ends are on the printed scale. Replace or extend the one-unit non-task visual with the same strip visibly aligned to two neighboring numbered ticks, with readable endpoint marks and its one-unit result. Show where a strip sits so that its opaque paper does not conceal the ticks or labels being used. Do not demonstrate any A–D task solution or teach endpoint subtraction as a prescribed method. The current 12 mm units in the cutouts, unit row, and rulers are mutually consistent; retain that consistency.

**Why it matters:** As written, the finite catalog depends on rules known to the checking script but not to the child. With the intended rule, the seven placements are A: 5–7, 7–9; B: 4–7, 7–10; C: 3–7, 7–11; D: 7–13. Without the printed-boundary requirement, D: 1–7 is a legitimate counteranswer.

### 2. The precision-design question needs a worst-case objective

**Location:** grades 4–5 p. 5, Problem 7; `grades-4-5.tex` line 65; corresponding final assertion in `check_math.py`.

“Pin down the stretch most tightly” does not specify whether the choice is judged by the largest possible remaining range before seeing reports, or by the range after particular reports. The intended choice, 1 and 10, minimizes the worst-case width. It does not promise a narrower realized positive-slope range than every closer pair under every set of admissible errors.

If the displayed difference is Δ over separation D, the feasible stretch set is `[(Δ−2)/D, (Δ+2)/D] ∩ (0,∞)`. Its untruncated width is `4/D`; positivity can shorten the range. For example, for the same true rule `y=0.1x`, observations at lengths 1 and 2 with errors +1 and −1 give Δ=−1.9 and feasible stretches `(0,0.1]`. Exact displayed values at lengths 1 and 10 give Δ=0.9 and feasible stretches `(0,29/90]`, a wider realized range despite greater separation. Both situations satisfy the stated error bound.

**Required change:** State briefly that children choose before seeing any reports and want the smallest guaranteed bound on the range of possible stretches, even for the least helpful allowed errors. Keep the bound discovery in the problem, not a supplied formula. Preserve the repeated-one-reference question: with unrestricted shift, even exact repeated observations at one input cannot determine stretch. In adult mathematical documentation distinguish width from attained extrema when positivity truncates at zero. Problem 6's actual examples stay strictly positive and have attained extrema, so they need no numeric replacement.

### 3. Add a concrete bridge for the newly introduced reading error

**Location:** grades 4–5 p. 5, before Problem 6; `grades-4-5.tex` lines 59–63.

The packet has good worked visuals for addition, copying then adding, and fractional stretch then negative shift. At the next new operation, however, “true report” and “displayed report” arrive together in prose immediately before a two-reference comparison. No worked input goes through the fixed machine and then the allowed display error. It is easy to mistake ±1 for an error in the reference length or a change of machine between readings.

**Required change:** Supply one small non-task example showing a known input, the same fixed rule's true report, then one allowed displayed report (or a short indicated permitted display interval). Use the same input throughout and label the transition where the reading error occurs. Do not reveal the endpoint strategy for Problems 6–7. If necessary redistribute space or add a continuation page; do not remove the extrema investigation. The existing fractional stretch/negative-shift example on p. 3 already satisfies this bridge for that earlier operation and should be retained.

### 4. Hidden-strip names collide with known physical-strip names

**Location:** grades 2–3 pp. 1–2, supplied A/B cutouts and Problems 2–3; `grades-2-3.tex` lines 14–23.

Children have just handled the supplied strip A of length 2 and strip B of length 3. The next page calls two hidden strips A and B, with reports 7 and 10. If children carry over the material labels, these cannot come from one machine (their inferred extras would be 5 and 7). The intended six-solution catalog instead treats these as entirely new unknown objects. The word “hidden” does not clearly reset identity.

**Required change:** Give the unknown strips fresh names or symbols, consistently through the report boxes, table, and Problem 3. This removes a needless identity puzzle while preserving the shared-offset investigation.

## Smaller improvements

- **Grades 2–3 p. 4, Problem 7:** Say to supply three *length-and-report pairs*. The existing phrase “a set of three reports” permits giving only three numbers, which a partner cannot repair without their inputs. This is an essential output specification, not extra scaffolding.
- **K–1 p. 2, Problem 3:** The available single copies make the intended answer A+C=D clear enough after setup. Preserve “two strips” as two available physical pieces; do not silently allow duplicated B pieces, which would introduce B+B=D. A preparation note can settle inventory without expanding the student text.
- **Grades 4–5 pp. 2–3:** The finite-rule game correctly allows a lucky single report to identify a rule. When a future adult guide explains the mathematical overview, explicitly contrast that finite prior with the unrestricted positive affine model, where one exact reference leaves infinitely many rules. Do not claim that the finite game's one-reference question has answer “never.” No extra generalized algebra is needed on the student page.

## Mathematical checks and features to retain

- Middle Problems 2–3 have six intended unknown-length pairs: `(6,9), (5,8), (4,7), (3,6), (2,5), (1,4)`; the second strip is always three units longer. One shared unknown extra is the mathematical substance.
- Middle Problem 4 gives `(5,8), (7,10), (3,6)`. Problem 6 repairs are I: final report 10→9; II already consistent; III: middle report 6→5.
- Upper Problem 2 has `(copies,extra)=(1,4),(2,2),(3,0)`; any distinct second reference separates these. A 6-unit first input reporting 24 uniquely identifies `(3,6)` in the stated finite model.
- Upper Problem 3 identifies `y=2x+4` and `y=x+6`. Distinct inputs determine the affine rule; preserve the uniqueness question.
- Upper Problem 4 has exactly three repairs: first report 7→6, middle 11→11½, or last 16→15. All three repaired slopes are positive.
- Upper Problem 5 correctly removes the affine assumption before asking for disagreeing tables; no number of tests strictly below 8 constrains the value at 8 without additional structure. Preserve this distinction between a promised model and testing a claim.
- Upper Problem 6 gives pair A stretches `[1,3]`, attained by `y=x+7` and `y=3x+1`; pair B gives `[7/4,9/4]`, attained by `y=(7/4)x+11/2` and `y=(9/4)x+5/2`. These are correctly chosen concrete cases for the later design question.

## Coverage and limits

| Packet | Pages visually inspected | Result |
|---|---|---|
| K–1 | 1–2 | Consistent scale and readable cutouts; placement/recording convention needs revision. |
| Grades 2–3 | 1–4 | Good concrete-to-identification sequence; relabel unknown strips and clarify constructed puzzle inputs. |
| Grades 4–5 | 1–5 | Strong substantive progression; add error bridge and state worst-case design objective. |

This is a review of the writer-stage PDFs, not final-revision acceptance. I did not alter the draft, perform physical printing/cutting or classroom rehearsal, or claim that the present files are release-ready. Source-package reconstruction and final rendered-page verification should be performed after revision, when the deliverable is fixed. No downloaded reference was needed to verify these independently derived finite and affine examples.
