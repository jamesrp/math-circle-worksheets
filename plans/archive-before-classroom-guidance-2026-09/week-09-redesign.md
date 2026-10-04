> Historical v2 plan, preserved before the September 27 classroom-guidance revision. See the [current version](../week-09-redesign.md) and [revision record](../fall-weeks-02-10-classroom-guidance-review.md). Preparation is not evidence of classroom use.

# Week 9: Unfolding billiards: corners, gcd, and dynamics

Redesigned September 19, 2026; review revisions September 20, 2026. Prepared, not taught. Use Week 1’s standard of an approachable experiment leading to a theorem, obstruction, optimization, or controlled mathematical question. Three core entry levels plus **one optional grades 6–7 page**. Full launch prompts, hints, checked solutions, and the 60-minute operating plan are in the [four-page facilitator guide](../../lowell-math-circle-year-2/week-09/week-09-facilitator.pdf) and its [editable source](../../lowell-math-circle-year-2/source/week-09/week-09-facilitator.tex).

## What changed

Unfolding becomes the main representation instead of a brief optional preview. Middle children coordinate two lists of wall locations and design corners; upper children prove the gcd/parity classification, derive an exact bounce formula, and solve inverse existence/impossibility problems. The extra changes slope and distinguishes avoiding corners from being dense.

## Entry points and mathematical work

Grade labels are approximate. Reading can always be supported by adult scribing/read-aloud; moving objects and giving an oral explanation count as mathematical work.

| ID suffix | Investigation | Student pages | Prerequisites: reading/arithmetic/reasoning | Main work |
| --- | --- | --- | --- | --- |
| K | Bounce to a corner / See a straight path | 2 | No reading/arithmetic; follow a diagonal, distinguish side from corner, and reverse only the blocked direction. | Compare 2×2,2×4,4×2, then fold mirrored rooms around a straight line. |
| M | Unbounce the ball / When do walls meet? | 2 | Count lengths and multiples through 12; coordinate two repeating lists and use odd/even whole-room counts. | Trace 2×3, unfold to (6,6), classify 2×3,3×6,3×9,4×6 and make target tables. |
| U | A straight line in many rooms / Every corner / Bounce design | 3 | Multiples, parity, and division; gcd/lcm follow a picture. The optional general lemma adds adult-supported subtraction of multiples and Euclid’s argument. Coordinate geometry and necessity/sufficiency reasoning. | Prove first-corner LCM and reduced-parity rules, show no return to start at first corner, count a+b−2 bounces, design exactly four and rule out three at top-right. |
| X | Change the slope | 1 | Positive fractions, coordinate pairs, and the supplied irrationality fact for √2. Distinguish rational-direction proof from a deeper density theorem. | In a unit square, derive the first lattice point for p/q, prove √2 never reaches a corner, and find a periodic no-corner diamond from a different start. |

The complete IDs are **F09-K/M/U/X-v2**. There is no extra packet for the lower groups; offer the next entry level when appropriate.

## Materials, launch, and hour

Seven counters, rulers, pencils, scrap square-grid paper, and two spare copies of the K1 folding page. An adult may trace while a child chooses bounces. No real ball or precision construction is required. Print three K1 packets, three middle packets, and one upper packet: **15 core student sheets**, plus the single extra sheet if wanted. Print single-sided, US Letter; actual size is recommended but no physical fitting depends on calibration. Introduce one page at a time.

**Launch:** Which part of the direction must change at this wall? Show two proposed arrows at the right wall, then let a child choose. Later ask what happens if the wall opens into a mirror copy and the path keeps going straight.

**Proposed hour:** 0–10 explore counters and mirrored grid rooms; 10–15 brief reflection launch; 15–35 main investigation: trace, fold, and predict corners; 35–40 movement/reset; 40–55 continue with inverse design or an optional proof; 55–60 share a prediction with its reason and tidy.

One parent stays mainly with K,K,1; the organizer alternates between 3,3,3 and the fifth grader, aiming for a return within five minutes and leaving a concrete next attempt. Roles rotate within triplets, preserving two opposing sides for games. The fifth grader needs actual adult mathematical conversation. The exact timetable and staffing are this project’s proposal, not a documented arrangement from the books.

**Hints and pacing:** first ask a child to demonstrate the rule and show their current attempt; next ask for a smaller example or counterexample; only then offer the organizing representation on the next page. The facilitator gives specific hint ladders. A corrected conjecture is valuable. Do not fill time with copying or require finishing every task.

## Stopping points and optional proof continuations

| Group | Satisfying stopping point | Optional proof continuation |
| --- | --- | --- |
| K–1 | Predict a corner and show how folding turns a straight path into its bounces. | Explain why the 2×4 and 4×2 paths end at different corners using the reflected rooms. |
| 2–3 | Make a target table and explain its endpoint with whole-room counts. | Show why the first shared wall multiple gives the first corner, then justify a new target design. |
| 4–5 | Use an earlier-corner argument to rule out bottom-left and explain the bounce count in whole-room counts. | With adult support, prove the coprime-divisibility lemma and reduced-side formula, then classify every four-bounce top-right design. |

The [shared coprime-divisibility scaffold](../coprime-divisibility-scaffold.md) supplies the additional arithmetic reasoning also used in Week 4. The general lemma requires adult-supported subtraction of multiples and following Euclid’s repeated-subtraction argument; it is not implied by being able to count multiples. If supplied rather than explained, record it as **given as a theorem**.

## Verified mathematical backbone

Assume positive integer width w and height h, launch from bottom-left with physical slope 1, and stop at the first corner. Unfolding gives y=x. A corner needs a simultaneous multiple of w and h; the first is L=lcm(w,h). First write m=L/w, n=L/h. If m,n shared d>1, the path at L/d would already have crossed m/d whole widths and n/d whole heights, giving an earlier corner. Thus m,n are coprime; both cannot be even, so bottom-left is impossible without the gcd formula.

For the optional arithmetic continuation, write w=ga, h=gb with gcd(a,b)=1. Every common multiple has form ga·t with b dividing at. The [shared scaffold](../coprime-divisibility-scaffold.md) proves that b must divide t, by subtracting shorter strips from longer ones in parallel pairs (a,b) and (at,bt). The base pair reaches (1,1); the scaled pair reaches (t,t) while remaining multiples of b. Hence the least t is b and L=gab, so the trajectory travels b whole widths and a whole heights. Its horizontal side is right iff b is odd, and its vertical side top iff a is odd. Since a,b cannot both be even, it cannot first end bottom-left. Do not apply raw side-length parity before removing gcd.

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

For pedagogy, re-read *Math Circle by the Bay*, preface printed pp. viii–x (PDF 9–11): common themes with varying depth, manipulatives, explanations, and reserve challenges. Also re-read Rozhkovskaya, Lesson 3 “At the lesson” (`part0013.xhtml`) for attempts before an organizing display; Lesson 7 (`part0017.xhtml`) for verifying legal-move understanding; and Lesson 8 (`part0018.xhtml`) for unequal copying pace. Our preprinted material, adult rotations, and particular task sequence are adaptations, not arrangements reported by those sources. See [lesson-format-source-notes.md](../lesson-format-source-notes.md).

## Returning children and future branches

Lowell has 7×5, 4×3, 8×10, consecutive sides, 1×n, 2×odd, scaling, and height-five families. Do not promise that small tables or scaling are new. The new emphasis is proof through unfolding, exact first-corner classification, bounce count, and inverse design. For a returner, take one remembered corner prediction straight to mirrored rooms and ask why it is right; skip familiar traces and redundant table rows. Move to the forbidden corner or inverse-design questions once the unfolding is understood. Physical unfolding was formerly reserved for summer and is intentionally promoted here. Keep plus-shaped tables and additional nonrectangular tables as future branches. Update the [use log](fall-k-5-year-a-use-log.md) after teaching, recording exactly which packet pages and instances each child encountered; prepared reserves stay untaught. Preserve an oral explanation as a brief adult note when writing is a barrier.

## Verification and outputs

An independent unit-step reflection tracer verifies all 900 rectangles of side lengths 1–30 against the formulas, plus the complete four-bounce top-right reduced-pair list and several rational-slope event counts.

Run `python3 lowell-math-circle-year-2/source/week-09/verify.py`, then `sh lowell-math-circle-year-2/source/week-09/build.sh`. Builds write five PDFs in `lowell-math-circle-year-2/combined/`; LaTeX is editable in the week folder. The [print index](../../lowell-math-circle-year-2/source/week-09/README.md) and [review record](../../lowell-math-circle-year-2/source/week-09/REVIEW.md) describe the delivered files and visual checks.
