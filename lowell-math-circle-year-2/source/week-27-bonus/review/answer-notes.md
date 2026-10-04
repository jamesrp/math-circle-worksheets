# Week 27 revised answers and assumptions

Three directions: aggregate rank score versus stability (P1), incomplete mutual choices and invariant unpaired objects (P2, P4), and one-group roommates (P3). The two omitted-choice problems are one investigation, not counted twice. One shared Grades 2–5 packet; no forced younger sheet. Strict lists, one unchanged reference matching and both preference checks are necessary. Reading support is routine, but the child must make the decisions. Artificial tokens, not real children. All work is unpiloted; practical independent retention of the two simultaneous checks is untested.

The non-task demonstration now supplies ordered strips V:P,Q and P:V,U, boxes the current partners Q and U, and keeps U–P and V–Q fixed, then compares V to current Q and P to current U. Both prefer V–P, so it blocks. This supplies an explicit input/current matching, intermediate two checks, and output. It does not update pairs during the check.

## Problem 1

Rank score is an invented puzzle objective, not a measurement of happiness. Complete list profile exactly as printed: A:Y,Z,X; B:Y,X,Z; C:X,Y,Z; X:B,A,C; Y:A,C,B; Z:B,A,C.

| Pairing | Total | All blocking pairs |
|---|---:|---|
| AX/BY/CZ | 15 | AY, AZ, CY |
| AX/BZ/CY | 13 | AY, BX |
| AY/BX/CZ | 11 | none |
| AY/BZ/CX | 10 | BX |
| AZ/BX/CY | 11 | AY |
| AZ/BY/CX | 12 | AY |

Unique lowest aggregate score is AY/BZ/CX (10). It is unstable: B prefers X (rank2) to Z (rank3), and X prefers B (rank1) to C (rank3). Unique stable pairing is AY/BX/CZ (11), so this is also the lowest stable total. Its pair scores are AY=2, BX=3, CZ=6. Listing all six certifies optimality and uniqueness, but the blank record table leaves ordering to children. This is aggregate optimization, not a repeat ordinary stable-catalog task.

## Problem 2

Only mutually listed pairs are allowed; omissions are unacceptable; acceptable partners beat being unpaired. A missing choice is not a tied last choice. Every acceptable strict preference ordering remains visible.

First profile has unique stable matching AX, leaving B and Y unpaired. Empty pairing is blocked by AX; BX leaves A unpaired and is blocked by AX because X ranks A before B; Y has no edge.

Second profile has exactly two stable matchings: AX/BY and AY/BX, both leaving C and Z unpaired. Z has no acceptable choices. C can only pair Y; if CY, one of A/B must be unpaired (both otherwise require the one X). Y ranks both A and B before C, so that unpaired object and Y block. Thus C cannot be matched stably. Neither A nor B can stay unpaired in a stable matching: if A unpaired then either an allowed X/Y is free or Y is with C and would prefer A; if B unpaired then either X is free or X is with A and would prefer B. Both displayed complete-on-A/B alternatives have no blocker: each unchosen A/B pair fails one of the two preference checks. Stable partners differ, unpaired objects do not.

## Problem 3

All objects are on one side, and pairs use every object once. There are exactly three perfect pairings. For the left profile:

- AB/CD is blocked by BC.
- AC/BD is blocked by AB.
- AD/BC is blocked by AC.

Therefore no stable pairing exists. Completeness of these three cases is the explanation, not merely failure of a procedure. The right profile has mutual first-choice pairs AB and CD; AB/CD is stable. AC/BD is blocked by AB and CD. AD/BC is blocked by AB, AC, CD. This contrast shows some one-group instances work and some do not. It does not apply the two-sided deferred-acceptance promise to roommates. All diagrams use identical token styles.

## Problem 4

No requested counterexample exists under strict mutual acceptable lists and acceptable-partner-above-unpaired assumptions. Stable matchings in this two-sided model match exactly the same objects. The students choose particular omitted lists and may find several stable partners; that supplies experiment, while the following explanation gives the general destination. Blank strips are one profile, not sequentially changed reference lists.

Suppose p0 is unmatched in stable M but matched to r0 in stable N. Stability of M forces r0 to have M-partner p1 preferred to p0, since p0 would accept r0. Stability of N then forces p1 to have N-partner r1 preferred to r0, since r0 would prefer p1 to current p0. Repeat: M-stability forces r1 to have M-partner p2 preferred to p1, and N-stability forces p2 to have N-partner r2 preferred to r1. Alternating M/N links form a path beginning at unmatched p0. It cannot repeat (a matching has degree at most one of each link type; a repeated component would be a cycle disconnected from the unmatched endpoint) and cannot end without the blocking pair just forced. Finiteness is a contradiction. Repeat after exchanging M/N and after exchanging sides to show equal matched sets on both sides. Strictness and the unpaired convention are essential; equal side sizes do not force perfect matching.

This proof is readiness-dependent adult reserve for a return visit. It is not needed to start P2's concrete finite profiles, and unsuccessful counterexample search alone is not proof.

## QA and sources

`src/check.py` enumerates all six score-profile perfect matchings, all valid partial matchings for both incomplete profiles, and every perfect roommate pairing for both lists. `writer-checks.json` contains full blockers/scores. Writer checks do not replace independent math review. Every draft page was rendered and inspected. Portable build accepts an output directory and uses PATH/PDFLATEX only. Background Pass–Halpern Chapter 14 is base-model context; new examples/invariant are supported here by exact enumeration/alternating paths, not attributed to that source. Week 13 allowed-edge capacity work is related but different.
