# Week 9: Unfolding billiards: corners, gcd, and dynamics

Revised September 27, 2026 in response to the [Week 1 classroom review](week-01-classroom-review.md) and the adopted AGENTS.md guidance. **F09-K/M/U/X-v3 are prepared, unpiloted revisions.** No observations about a Week 9 session have been supplied. The previous v2 source and PDFs are preserved separately in the weekly `archive-before-classroom-guidance-2026-09/` directories.

## What changed, and why

Several contrasting bounce traces now precede mirrored rooms. Original and unfolded paths are paired with numbered crossings; two more concrete room pictures and endpoint-count records support folding before multiples are used to predict. Upper tasks separate scaled copies, first-corner failure, wall-count work and inverse design. The extra now has five rational-slope trials and a visible midpoint diamond before discussing irrational direction and density.

These changes infer what may help from the organizer's reported Week 1 experience: sufficient contrasting work, explicit actions, and records introduced for a purpose. They are proposals, not claims that these new sequences succeeded with children. Formal generalizations, hints and discretionary proof follow-ups are in the [six-page facilitator guide](../lowell-math-circle-year-2/week-09/week-09-facilitator.pdf); numbered student problems state concrete actions with the space/diagrams needed to perform them.

## Entry points and mathematical work

Grades are approximate. Choose by prerequisites; read aloud, scribe and accept oral or drawn explanations. The additional pages provide flexible continuations, not a one-hour completion quota.

| ID | Pages | Prerequisites | Concrete sequence |
| --- | --- | --- | --- |
| F09-K-v3 | 3 | Adult reads/draws as needed; track diagonals and change only the blocked direction; no independent arithmetic. | Square, tall, wide and taller traces; two separate folding panels after comparisons. |
| F09-M-v3 | 4 | Counts and multiples through 12; coordinate two room counts and alternate sides. | Three traces; bounce/crossing correspondence; two additional unfolding pictures; endpoint strip/table; target designs on supplied grids. |
| F09-U-v3 | 5 | Multiples, division and parity; optional gcd/coprime proof needs adult-supported subtraction of multiples. | Contrasting traces; paired original/copied rooms; scaling and raw-parity counterexample; first-corner check; separate wall counts; three inverse candidates. |
| F09-X-v3 | 3 | Positive fractions and coordinates; irrationality of square root of 2 may be supplied. | Five rational traces including an unreduced slope; corner design; irrationality argument; offset diamond distinguishes no-corner from density. |

## Materials, launch, and flexible hour

Counters, rulers, pencils, scrap square-grid paper and adult scissors. Copy K page 3 separately and cut between the two panels before folding; keep traced earlier pages available for comparison. An adult may draw while a child chooses each direction.

**Print a starting set:** page 1 of the appropriate level for each child (3 K–1 + 3 middle + 1 upper = **7 starting sheets**), with one master of each continuation and the optional three-page extra. Copy additional pages as needed and offer one at a time. The complete core packet lengths are 3/4/5 pages; the full roster set would be 26 sheets, but is not the default print instruction. Use US Letter, single-sided, actual size. No activity depends on physical scale calibration.

**Whole-group launch:** After handling counters and tracing grid diagonals, gather at a visible 2×4 table. Move to its right wall, ask a child for the legal next direction, dot the bounce, and circle the ending corner. Show that interior path crossings are not walls. Only then give separate starting tasks. Delay mirror rooms until children have actual paths to compare.

**Proposed hour:** 0–10 handle materials; 10–15 short common action-and-record demonstration; 15–35 concrete attempts; 35–40 movement/reset; 40–55 revisit, compare or continue at the child's current stage; 55–60 share one result and tidy. Change this rhythm to fit actual exploration. Parent mainly supports K–1; organizer alternates middle/upper about every five minutes and leaves a specific next attempt. The upper child receives actual adult mathematical conversation. Roles rotate so each child acts.

## Stopping points and proof continuations

| Group | Satisfying stop | Optional facilitator continuation |
| --- | --- | --- |
| K–1 | Predict and show contrasting corners; one physical fold if ready. | Explain the tall/wide corner difference through the reflected panels. |
| 2–3 | Match bounce numbers to unfolded crossings, or explain a target rectangle. | Why the first common wall distance is the first corner; verify a new target design. |
| 4–5 | Use room-count parity and verify a bounce-count rule from separate wall lists. | Earlier-corner obstruction; adult-supported coprime lemma; full reduced-side and inverse-design classification. |

Do not require every table cell, map or page. Demonstrate each unfamiliar record once with the real objects. When a representation is causing copying rather than helping compare attempts, scribe or return to objects. Preserve both construction and explanation; the guide keeps complete arguments so they are available when children are ready.

## Observation plan and reuse

After the session record which exact pages/instances children attempted, what they tried, what needed adult rescue, what they explained and what they wanted to continue. Label adult hypotheses separately from observed behavior. Distinguish a child's explanation from a supplied theorem. Unused stages remain prepared reserves; do not mark a whole printed packet as taught. The existing use log records actual use; this revision makes no new teaching claims.

## Verified mathematical backbone

Assume positive integer width w and height h, launch from bottom-left with physical slope 1, and stop at the first corner. Unfolding gives y=x. A corner needs a simultaneous multiple of w and h; the first is L=lcm(w,h). First write m=L/w, n=L/h. If m,n shared d>1, the path at L/d would already have crossed m/d whole widths and n/d whole heights, giving an earlier corner. Thus m,n are coprime; both cannot be even, so bottom-left is impossible without the gcd formula.

For the optional arithmetic continuation, write w=ga, h=gb with gcd(a,b)=1. Every common multiple has form ga·t with b dividing at. The [shared scaffold](coprime-divisibility-scaffold.md) proves that b must divide t, by subtracting shorter strips from longer ones in parallel pairs (a,b) and (at,bt). The base pair reaches (1,1); the scaled pair reaches (t,t) while remaining multiples of b. Hence the least t is b and L=gab, so the trajectory travels b whole widths and a whole heights. Its horizontal side is right iff b is odd, and its vertical side top iff a is odd. Since a,b cannot both be even, it cannot first end bottom-left. Do not apply raw side-length parity before removing gcd.

Before the final corner, m−1 vertical walls and n−1 horizontal walls are crossed; after the optional lemma these counts are b−1 and a−1. None coincide (else that would be an earlier corner), hence bounce count a+b−2. L is coordinate distance, while geometric path length is √2L.

Middle (L,widths,heights,corner): 2×3→(6,3,2,BR);3×6→(6,2,1,TL);3×9→(9,3,1,TR);4×6→(12,3,2,BR). Upper additional tables:6×9→(18,3,2,BR);6×10→(30,5,3,TR);8×14→(56,7,4,BR).

Top-right with four bounces requires positive coprime odd a,b with a+b=6: only (1,5),(5,1), since (3,3) is not reduced. Any positive integer scaling works. Top-right with three bounces is impossible because the sum of two odd numbers minus two is even.

Extra: only for the **unit square**, coprime slope p/q first reaches the lattice point (q,p); the horizontal side is right iff q odd, vertical top iff p odd, and the bounce count is p+q−2. Slopes 2/3 and 3/2 give BR and TL with three bounces each. A √2 slope cannot meet a positive integer point since that would make √2 rational. An offset rational path from (0,1/2), slope 1, follows the mid-edge diamond and avoids corners without being dense. Density is supplied specifically for the √2-slope path launched from (0,0), not proved by the no-corner argument. The origin matters under the stop-at-a-corner convention: from (0, 2−√2), slope √2 reaches unfolded (1,2), folds to bottom-right, and stops.

For a general rectangle with physical slope s, the normalized-square slope is sw/h. The worksheet fixes the unit square to avoid confusion. “Rational polygon” in the research refers to angles that are rational multiples of π, not to launch slope. Corner-start paths stopped at their first corner are not called periodic orbits.

## Sources and boundary between class and research

- JRMF, *Billiards Geometry*, PDF p.2, asks general corner, bounce-count, and path-length questions. The stages, selected tables, fold sheet, and inverse-design briefs are our adaptation.
- Lowell *Handout 10*, problems 10.2–10.7; *Handout 11*, problems 11.4–11.5: rectangle families, scaling, height-five tables, plus-shaped tables. See prior-use note below.
- Howard Masur and Serge Tabachnikov, *Rational billiards and flat structures*, *Handbook of Dynamical Systems* 1A (2002), pp. 1015–1089. [Author manuscript](https://math.uchicago.edu/~masur/handbook1.pdf): §1.3 unfolding; §1.4 unit-square/torus model and rational/irrational slope distinction; §1.5 flat surfaces; §4 periodic orbits. The linked manuscript’s pagination differs from the published chapter. The elementary reflection construction is genuinely the first step of that research framework; the children do not prove its ergodicity results.

Undergraduate homes: gcd/lcm, divisibility, lattice geometry, rational/irrational numbers, torus flows and dynamical systems. The extension contrasts two precise statements; it does not label an unproved classroom conjecture a current research open problem.

For pedagogy, re-read *Math Circle by the Bay*, preface printed pp. viii–x (PDF 9–11): common themes with varying depth, manipulatives, explanations, and reserve challenges. Also re-read Rozhkovskaya, Lesson 3 “At the lesson” (`part0013.xhtml`) for attempts before an organizing display; Lesson 7 (`part0017.xhtml`) for verifying legal-move understanding; and Lesson 8 (`part0018.xhtml`) for unequal copying pace. Our preprinted material, adult rotations, and particular task sequence are adaptations, not arrangements reported by those sources. See [lesson-format-source-notes.md](lesson-format-source-notes.md).

## Returning children and future branches

Lowell has 7×5, 4×3, 8×10, consecutive sides, 1×n, 2×odd, scaling, and height-five families. Do not promise that small tables or scaling are new. The new emphasis is proof through unfolding, exact first-corner classification, bounce count, and inverse design. For a returner, take one remembered corner prediction straight to mirrored rooms and ask why it is right; skip familiar traces and redundant table rows. Move to the forbidden corner or inverse-design questions once the unfolding is understood. Physical unfolding was formerly reserved for summer and is intentionally promoted here. Keep plus-shaped tables and additional nonrectangular tables as future branches. Update the [use log](fall-k-5-year-a-use-log.md) after teaching, recording exactly which packet pages and instances each child encountered; prepared reserves stay untaught. Preserve an oral explanation as a brief adult note when writing is a barrier.

## Verification and outputs

An independent unit-step reflection tracer checks all 900 rectangles with sides 1–30. Added assertions cover the height-6, swapped/square, scaled and inverse-design examples, and first vertices for 1/2, 2/4, 2/3, 3/2 and 3/4. Origin-start and normalized-slope qualifications remain in the guide; density is supplied as a separate theorem. Finite checks support the printed cases; general proofs remain in the facilitator guide.

Run `python3 lowell-math-circle-year-2/source/week-09/verify.py`, then `sh lowell-math-circle-year-2/source/week-09/build.sh`. The five PDFs are written to `lowell-math-circle-year-2/week-09/`; editable TeX sources remain in the weekly source folder and intermediates in `tmp/pdfs/`. The [print index](../lowell-math-circle-year-2/source/week-09/README.md) and [review record](../lowell-math-circle-year-2/source/week-09/REVIEW.md) record final page counts and checks.
