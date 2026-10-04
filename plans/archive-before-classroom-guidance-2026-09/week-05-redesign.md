> Historical v2 plan, preserved before the September 27 classroom-guidance revision. See the [current version](../week-05-redesign.md) and [revision record](../fall-weeks-02-10-classroom-guidance-review.md). Preparation is not evidence of classroom use.

# Week 5: How much information determines a city?

Prepared September 19, 2026. Replaces the earlier depth of F05, retaining the common hands-on theme. Grade bands are entry points. The one-page grades 6–7 extra is optional.

## The mathematical work

Permutations, Latin-square completion, uniqueness, minimal versus minimum clue sets, and Latin trades.

| Entry level | Investigation |
| --- | --- |
| K–1 · F05-K-v2 | Enumerate all six skylines, distinguish viewpoints, and prove why one visible tower from each end is impossible. |
| 2–3 · F05-M-v2 | Classify all cities with a top clue of three, add a second clue for uniqueness, and prove one visibility clue never determines a 3-by-3 city. |
| 4–5 · F05-U-v2 | Give a complete case proof for a five-clue 4-by-4 city; optionally check five deletion certificates and prove a different three-clue set determines the same target. |
| Extra 6–7 · F05-X-v2 | Use four disjoint Latin trades to prove an entry-clue lower bound, then explain why touching those four trades is not sufficient. |

## Prerequisites and preparation

K–1: count to 3 and compare heights, no reading; distinguish arrangements and viewpoints. Middle: row/column exclusion and counts to 3, adult reading available; exhaustive two-case argument. Upper: counts to 4 and managing constraints, no advanced arithmetic; uniqueness and lower/upper bounds. Extra: row/column coordinates and four-block pigeonhole argument; no algebra required.

112 snap cubes plus a few for demonstration: 6 per K–1 child, 18 per middle child, 40 for the upper child. Height slips record further solutions; use cubes first. Build on the table or draw scrap-paper grids with one-inch cells; printed smaller grids record solutions rather than holding every brand of cube. Preparation: about 15 minutes to prebuild towers and print.

Current roster: K,K,1 / 3,3,3 / 5. Print three K–1 packets (two pages each), three middle (two each), one upper (three): 15 student sheets; add one extra if needed. Facilitator prints separately. US Letter, single-sided, 100%; grids are workspaces rather than calibrated physical templates.

## Default 60-minute flow, adjusted to the children

0–10: Free tower building and arranging; let children explore heights and viewpoints before adding rules.

10–15: Brief launch with heights 2,1,3. Ask what a tiny person sees from each end and touch the visible towers. Introduce the row/column rule separately.

15–35: K tries visibility challenges and records orders; middle constructs both top-clue cities and adds the second clue; upper solves the opening puzzle and starts the five-clue cases.

35–40: Movement/reset. Leave cities or records intact and step away from the tables.

40–55: Continue the current investigation or take its optional proof continuation below. Give one page at a time; the upper certificate page and extra are reserves.

55–60: Share one concrete result and reason, then tidy.

| Group | Satisfying stopping point | Optional proof continuation |
| --- | --- | --- |
| K–1 | Build the six skylines and describe their two viewpoints. | Organize them by first tower to prove none is missing; explain why one visible tower at each end is impossible. |
| 2–3 | Construct both cities for the top clue and show which survives the second clue. | Prove the two-case list is complete, then use an unseen-row/column swap to show no single visibility clue can suffice. |
| 4–5 | Complete the five-clue case table and explain why it gives one city. | Check all five deletion certificates and prove the different left-clue set 4,3,2 forces the same target; separate “three works” from the computer-certified global minimum. |

One adult stays primarily with K,K,1. The organizer starts the upper child on a clear next attempt, helps the middle group, and returns for a proof conversation. Middle children can compare built cities while the organizer works with the upper child; the upper child can check individual certificates between visits. Choose one proof conversation at a time, rather than expecting both groups to finish their continuations. Children may keep building at a satisfying stop.

**Hints:** Fix the first tower before varying the last two. For the middle, the first column is forced. For the upper, bottom-left clue 1 puts 4 first and right clue 2 puts 3 last; classify only 4123 and 4213. A failed search is not a uniqueness proof.

The facilitator packet gives exact checked solutions, prompts, and optional reasoning. Children can point, build, dictate, or draw.

## Checked mathematics and boundaries

The facilitator gives all six skyline counts, both middle completions, and a human three-case proof of upper uniqueness. Deletion counts are 2,2,6,12,20 for L3,L4,R2,R3,R4. The minimal five-clue set is not minimum: L1=4,L2=3,L3=2 forces the same cyclic city. Exhaustive search certifies three is minimum for this target among subsets of its 16 perimeter clues, not a universal result for every 4-by-4 city. No single 3-by-3 visibility clue determines a city: the two unseen rows or columns can be swapped. Extra entry clues use a different model: an untouched 2-by-2 trade gives an alternative, and at most three clues leave one of four disjoint trades untouched.

Run **python3 plans/verify-week-05.py**. Computation verifies finite instances; the facilitator supplies explanatory proofs of general claims.

## Sources and lineage

- Downloaded JRMF *Skyscrapers Teaching Guide*, PDF pp. 1–4 and 13–14: rules, physical viewpoint, explanation prompts, blank grids; exact clue sets here are project instances.
- Joy Morris, [*Combinatorics*, Chapter 16: Latin squares](https://opentext.uleth.ca/Combinatorics/ch_Latin-squares.html): undergraduate Latin-square structure.
- Hatami–Qian, [*Teaching dimension, VC dimension and critical sets for Latin squares*](https://arxiv.org/html/1606.00032), §1, Theorem 1.2: entry-based determining sets and an asymptotic quadratic lower bound. Our small trade proof is not that theorem. Visibility clues and fixed entries are distinct. No current open-status claim about the paper's conjecture.

**Teaching lessons actually read:** *Math Circle by the Bay*, preface printed pp. ix–x/PDF pp. 10–11 recommends manipulatives, varying pace, extras, practice explaining, and themes at different depths. JRMF pages above provide physical launches and explanation prompts. Staffing, timetable, and new proof scaffolds are our adaptations. See [lesson-format source notes](../lesson-format-source-notes.md).

## Returning children and records

Related Lowell material: Handout 2.1–2.2 seating constraints. Proposed S1/S3/S4 clues are reused and substantially deepened; this does not establish that those instances were taught. Reserve larger skyline-count recurrences, Latin transversals, and full trade classification for later.

Status: **prepared, not taught**. Record exact instances, claims proved, hints, and extra branches in the shared use log. Untouched reserves remain available. [Print/source index](../../lowell-math-circle-year-2/source/week-05/README.md) and [review](../../lowell-math-circle-year-2/source/week-05/REVIEW.md).
