# Week 70 math check: Four shields in a portal room

Scope: `lowell-math-circle-year-2/week-70/week-70-students.pdf` (GGT70-S-v1, one shared Grades 4–5 packet, 4 pages) and `week-70-facilitator.pdf` (GGT70-FAC-v1, 3 pages). Sources: `lowell-math-circle-year-2/source/week-70/`. All pages were rendered into `tmp/review-runs/week-70/render/`. Diagram data was read from `student/students.tex`.

Independent check: `plans/review/checks/week-70/check_week70.py`, with its output in `check_week70.out`. It uses exact rationals, finds the repository from its own location and imports none of the packet's checkers. The model is the torus R²/(4Z)², with S=(0,0), T=(2,2) and point shields that cannot sit at S or T.

## Result

**Student packet: no mathematical errors found.** **Adult guide: no mathematical errors found.** I found 0 problems in the packet. There is one minor note about a source-package checker, which is outside the packet (see the end).

## What was verified, problem by problem

- **Shared rules and launch picture (p.1).** The non-task shot starts at (3,1) with direction (2,1). It crosses x=4 at (4, 3/2) and ends at (5,2), which is a copy of P=(1,2). The one-room version leaves at (4,1.5), reappears at (0,1.5) and reaches P. The TikZ coordinates match: `(3,1)--(5,2)`, `(4,1.5)`, `(3,1)--(4,1.5)` and `(0,1.5)--(1,2)`. The S/X/Y labels match the stated gluing.
- **Problem 1 (fewest shields for the four diagonal shots; intended answer 4).** The four arrows start at the four distinct corners and each points along its corner-to-T diagonal; this was parsed from the source. I checked the four open diagonal shots exactly against translates and found them pairwise disjoint on the torus. Their only common points are S and T, and shields are not allowed there. So at least 4 shields are needed, and 4 are enough (one inside each diagonal). The rooms are 4×4 with T at (2,2), drawn with uniform scaling.
- **Problem 2 (first T reached for the shots aimed at (2,6), (6,2), (6,6), (10,6)).** The first hits are (2,6), (6,2), (2,2) and (10,6). The halfway points fold to (1,3), (3,1), (1,1) and (1,3). The seam crossings are: top only; right only; none; right, top, right. No shot passes an S copy before its first T. The 16 map T copies are exactly {−2,2,6,10}², and they all fold to T. The bold room is [0,4]².
- **Problem 3 (four shields that stop every shot on the map).** The 16 map targets reduce to 14 distinct first-hit segments. Each of them passes through a midpoint shield at t=½, before reaching T. Uniqueness: a 4-shield solution must put one shield on each diagonal. I enumerated every candidate position, and the map alone forces {(1,1),(1,3),(3,1),(3,3)} as the **only** 4-shield answer. For example, the shot to (2,6) meets the diagonals only at (1,3), and the shot to (6,2) only at (3,1). So the page's intended outcome is the only one possible.
- **Problem 4 (all shots; can three shields work?).** I checked 14,641 lifts (2+4m, 2+4n) with |m|,|n| ≤ 60. In every case the first T comes before any S copy, and the halfway point to the first hit folds into the four shields. A general argument confirms this: on the first-hit lift (2u′, 2v′) with u′, v′ odd, the lattice points are k(u′,v′). T first appears at k=2 and S first appears at k=4. The midpoint, k=1, is odd–odd. Three shields are impossible because of the disjoint diagonals above. The answer is unique, as in Problem 3.
- **Guide.** I checked each of the following and found it correct:
  - the overview theorem and its hypotheses (point shields, not S or T, first hit, rays that never reach T excluded);
  - the launch coordinates;
  - the Problem 1 answer and diagram;
  - the Problem 2 table, the folded path (0,0)→(4/3,4), then (4/3,0)→(2,2), and the "right, top, right" crossing order;
  - the remark that "(6,6) … too late" (the midpoint (3,3) comes after the first hit at t=⅓);
  - the Problem 3 claims;
  - the Problem 4 sufficiency proof, drawing-level explanation and necessity argument.

  The hint "equal fractions along the four short diagonals" narrows the search to one parameter, and only the fraction ½ blocks every map shot (checked for ¼, ⅓, ½, ⅔ and ¾). It is a valid hint. The guide's caution that other source/target positions "need their own argument" is careful wording, not a false statement.

Not verified: the citation's page and lemma numbers (Lelièvre–Monteil–Weiss, arXiv:1407.2975, Lemma 12). The proxy blocked arXiv, and there is no local copy.

## Note outside the packet (source checker, minor)

`source/week-70/checks/verify_kernels.py`, `check70()`. It asserts `midpoint = tuple(F(t,2)%4 for t in endpoint)` for each *aimed* lift (2+4m, 2+4n) with |m|,|n| ≤ 30, and `MATHEMATICS.md` describes this as "3,721 lift midpoints". That midpoint always folds into the shield set, because it is odd–odd. But for 685 of those 3,721 lifts, the shot reaches T before the aimed midpoint. An example is (6,6): T is reached at t=⅓ and the midpoint (3,3) at t=½. So this check does not test interception, and it does the very thing `MATHEMATICS.md` warns against ("must not treat a midpoint after a first hit as successful interception"). The packet's other checkers do reduce to the first hit (`checks/independent_check.py` `shield_checks`, `student/check_math.py`, `guide/check_math.py`), so no printed claim is affected. Smallest fix: divide the endpoint by `gcd(|x/2|, |y/2|)` before taking the midpoint in `check70()`.
