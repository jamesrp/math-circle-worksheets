# GA3 design handoff

September 26, 2026. All eight assigned families—GA-18 through GA-24 and GA-27—are complete in `ga3-data.json`: **25 staged student pages, 50 keyed prompts and eight fully solved guide extensions**. Author checks pass in `ga3-checks.py` and `ga3-checks-results.json`. Independent design review is assigned to expand_ad1. No renderer or preview PDF has been created for this batch.

I used the editor's detailed `ga3-editorial-blueprint.md` as a head start, independently derived its calculations, developed full prompt/solution/hint sequences, specified exact diagram data and reopened the relevant primary sources. Since the editor contributed that blueprint, the final data have a different independent reviewer. The original atlas, accepted random ten and closed batch files remain unchanged.

The design follows the author/review contracts, NEXT-BATCH-NOTES and the trial review/assessment. I reread *Math Circle by the Bay*, printed preface pp.viii–x (PDF pp.9–11), as well as the source-supported lesson-format notes. Those passages support deep connected themes, manipulatives, independent attempts, repeated explanations and flexible pace. The particular diagrams, prompts, proof stages and suggested timings here are editorial choices. No proposed pacing or classroom outcome is presented as tested.

## GA-18 — choosing the loss changes the winner

The landscape now has height 0 for width 2/3 and height 6 for width 1/3. The learner chooses both a loss rule and candidate lines before solving an optimization problem. This is a new exact instance rather than the original 3/4 versus 1/4 calculation. Unequal widths matter: square loss selects 2, absolute loss selects 0 and maximum loss selects 3. Every claim has a bound and complete equality argument over all real constants, including heights outside the landscape range.

Changing the low width p introduces a genuine classification: mean 6(1−p); median 0 or 6 according to the majority, with the entire interval [0,6] tied at p=1/2; and unchanged midrange 3. The core explicitly assumes 0<p<1 so both heights occur on positive-width regions, avoiding a silent essential-supremum versus isolated-endpoint convention. The inverse task lets the learner choose a desired mean h and construct its unique width, then proves no interior h is a unique absolute-loss optimum. The extension gives the exact general weighted-variance identity and residual orthogonality.

Fractions, absolute values and completing the square are real gates. Integrals are defined as rectangle sums for these step functions. Axler's MIRA §8B provides the projection context; the direct finite proof does not rely on a general existence theorem. GA-13's minimax parabola is explicitly distinguished. Preserve 2:1 widths in the picture and leave all candidate lines undrawn. **Promising with algebra gates.**

## GA-19 — a counterexample against every bound

Calculus remains essential. A learner chooses an amplitude allowance ε and endpoint-slope target M, then constructs εx^n with n≥M/ε. The supplied new target 1/1000 and 7 is met exactly at n=7000; hand-plot resolution is irrelevant. The retained x^n/n family now drives a quantified opponent game: every proposed finite C loses to some n>C. Norms are defined on a fixed interval and fixed scales, so the effect is not graphical magnification.

The uniform-convergence question separates small inputs from their derivatives and correctly rejects x^n as a uniformly small input sequence. Changing the input norm to ||f||∞+||f′||∞ makes D bounded with exact norm one but no nonzero maximizing input. Integration has norm one under the original supremum norms and does attain it at f=1. These are different changes, not an ambiguous “repair” of one equation. The noise extension establishes only the exact measurement contribution 2ε/h; no unstated truncation model chooses an optimal h.

I corrected the original broad Axler Chapter10 locator to **MIRA §6C Definition6.43 and Examples6.44–6.45, pp.167–168**. The derivative witnesses and norm arguments are independently supplied. Graph play is not marketed as a substitute for derivatives and quantifiers. **Advanced/specialist.**

## GA-20 — schedule choice grows into a variational proof

The new endpoint data are displacement6 in time3, with initial durations1 and2. Signed speeds permit pausing and reversal. The complete two-speed parameterization (2+2a,2−a) gives E=12+6a², and the finite-partition identity E=12+ΣΔt_i(v_i−2)² defeats every schedule. Different subdivisions of the same constant-speed path are explicitly not different minimizing motions.

The waypoint y(1)=4 changes the legal set and gives the unique winning speeds4 then1, cost18. It is not mislabeled a counterexample to the original theorem. The calculus page defines continuous piecewise-C¹ paths on finitely many closed pieces, telescopes FTC and explains why a zero integral of a nonnegative continuous piecewise integrand forces the unique path through every join. The family y=2t+a t(3−t) has E=12+9a². Replacing the bill with distance produces many minimizers, precisely nondecreasing admissible paths; this family wins for |a|≤2/3.

The extension solves arbitrary endpoints and waypoints by intervalwise certificates. UCL's functional viewpoint is source context, while the global square proof supplies sufficiency and uniqueness without confusing Euler–Lagrange stationarity with optimality. Finite schedules are algebraic; the full class needs calculus. The quadratic bill is explicitly an invented objective, not metabolic energy. **Promising finite core; advanced calculus continuation.**

## GA-21 — reflection is only half the constrained problem

The new endpoints are A=(−2,3), B=(6,1), with the initial legal mirror [−3,5]. Learners place contacts and test a midpoint guess before receiving the reflection tool. Unfolding gives contact4 and exact length4√5, with the equality condition proving uniqueness. Shortening the mirror to [−3,2] removes that contact: the old lower bound survives but is unattainable.

The last page supplies strict convexity with a vector-triangle justification using positive endpoint heights. Learners still have to derive monotonicity on each side of the known global minimum and then prove the constrained endpoint2 has length5+√17 and is unique. The extension derives m*=(ka+hb)/(h+k) and the complete clamping rule for every nondegenerate closed mirror segment. No curved or multiple-mirror extension is implied.

Petrunin's line-reflection/distance and triangle-inequality arguments were reopened. Week9's billiard unfolding is cross-linked; the new destination is continuous optimization with a missing equality case. Diagrams need equal axis scales and must leave B′ and optimal contact for construction. **Promising with geometric proof and an explicit convexity gate.**

## GA-22 — an adversarial arrangement still admits a split

The opening lets learners place four challenging pegs, followed by an irregular quadrilateral and a point-inside-triangle board. Groups must be nonempty, use every label once and include hull boundaries; a singleton hull is explicitly allowed. The proof states the planar hull alternative as a supplied fact, then covers all-collinear and three-collinear cases as well as four corners and interior/edge points. Coincident labels have their own direct witness. Three noncollinear points show the worst-case four-point threshold is necessary.

The continuation verifies the new diagonal crossing (30/13,24/13), with weights7/13,6/13 and5/13,8/13. The interior point (2,1) has weights1/2,1/3,1/6 in the triangle with vertices(0,0),(6,0),(0,6). A signed affine relation is distinguished from a single convex combination; negative coefficients alone cannot certify hull membership. The higher-dimensional extension openly supplies linear dependence of d+2 lifted vectors, then proves the positive/negative normalization, nonempty groups and treatment of zero coefficients.

Hug–Weil Theorem1.2.1 was reopened with its actual normalization proof. Exact hull checking verifies every four-point subset of a4×4 lattice but is not the general theorem. Initial student boards have no hulls or diagonals drawn. **First-pilot candidate for the planar core; fractions and linear algebra are distinct continuations.**

## GA-23 — the tangent plane moves

This family uses four student pages to leave adequate room for its real spatial reasoning. The supplied rule preserves coefficients in a leg's orthonormal frame (forward tangent T, fixed plane normal N). The actual vector remains fixed at each corner before decomposition in the next frame. Neither a compass bearing nor a vector fixed in ambient space defines the same operation.

Learners choose an initial direction, compare a triangle with reverse and retraced routes, then track both basis arrows exactly. The octant map is (a,b)↦(−b,a), positive from+y toward+z at A. The variable-longitude route uses explicit endpoint frames and derives (a,b)↦(a cosα−b sinα,a sinα+b cosα) for every0<α<π. The α=π/3 check, length preservation and absence of nonzero fixed vectors follow directly. The northern half-lune has areaα; equality with the already proved rotation is asserted only for this route family. The final model test proves a fixed+y arrow fails tangency along the equator. The extension classifies repeated returns.

Petrunin–Zamora Chapter16 definitions, octant semisolution and Proposition17.10 were reopened. The supplied frame rule really is parallel transport: on a unit-speed great circle T′=−r and N′=0, so aT+bN has derivative normal to the surface. Calculus explains that background equivalence; signed vector tracking alone proves the supplied-rule instance. Exact diagram data were checked against the frames, including the BC endpoint tangent−y. The renderer must make actual and forward arrows visually distinct and avoid printing returned arrows on the opening diagram. **Promising with spatial-vector readiness; trigonometric continuation advanced.**

## GA-24 — a precise reversible map must preserve punctures

The learner chooses points on five explicit spaces before making an impossibility claim. A puncture deletes a single geometric point, and joined versus disjoint crossings are stated. Endpoint versus interior interval choices, Y center versus arm choices and the figure-eight join all matter. A careless single sample is not a proof.

The formal page supplies interval connectedness, continuous-image preservation and the full homeomorphism definition. The circle/segment contradiction deliberately chooses1/2 in the interval and proves every punctured circle connected through an open-angle parametrization. Y/segment and figure-eight/circle comparisons use the corresponding point, and whole-space connectedness already separates joined and disjoint loops. Explicit continuous surjections fail injectivity, while (x,y)↦(2x,y) and its continuous inverse give a successful circle/ellipse homeomorphism.

The extension shows one-point counts do not classify spaces: disk and circle match there, but two punctures differ. The disk argument constructs a polygonal detour through an interior point avoiding finitely many lines; it is a proof of path connectivity, not a finite grid experiment. Sharifi direct page opens failed, but indexed primary-page text provided the actual definition and connected-image proposition/proof, recorded candidly in sources. **First-pilot candidate for tracing; explicit topology facts gate the proof.**

## GA-27 — exact threshold, actual clipped domain

The landscape remains x²−y² on[−1,1]², with equality included in flooding. Learners choose levels and test points, then sketch the common levels−1/4,0,1/4. A continuous path from top to bottom must cross y=0, proving the zero barrier. At zero the two closed wedges really connect at one point.

The new core classifies every real level: empty below−1; two singleton components at−1; two connected pieces through every negative level below0; one component for every nonnegative level; the whole square at1 and above. Negative pieces connect via the actual top/bottom edges within |x|≤√(1+c), and nonnegative sublevels connect radially. A learner-selected forced crossing(a,0) has exact optimal barriera², with an explicit three-segment attaining route even at a=0 or±1.

Only the final page uses calculus. The saddle's index-one Hessian is contrasted with a bowl's birth event and the degenerate quartic's identical zero wedges. The whole-plane double-well extension is independently classified by vertical fibers and x intervals, with its two minima and level-one saddle calculated. Gillespie's Morse lemma and boundary hypotheses were reopened; the smooth compact-manifold theorem is not applied to the clipped square. **Promising inequality/path core; advanced Morse interpretation.**

## Verification and production constraints

The standard-library checker passes all eight mathematical groups. It includes a formal two-variable weighted-square identity;1,083 exact loss cases and125 weighted residual arrays;100 formal derivatives and exact threshold/noise checks;136 exact finite schedules plus the symbolic effort integral;108 reflection/clamp instances with exact crossings and strictness determinants; all1,820 distinct4×4-grid peg boards plus120 higher-dimensional affine relations;1,225 exact rational transport-frame roundtrips; geometric point-deletion models that retain edge interiors and90 exact disk detours; and1,060 exact wet-point path certificates plus gradient/Hessian identities. The machine-generated results are authoritative for counts if these figures change.

Each result states scope. In particular, floating mirror distance samples supplement the exact geometric proof; finite grid hulls do not replace Radon's proof; finite graph deletions do not classify arbitrary spaces; and sampled wet points do not certify all-point connectivity. The general proofs are fully written in the keys, with supplied facts identified.

No initial diagram should print optimal constants, mirror contacts, hull diagonals, returned tangent vectors, puncture counts or shaded flood answers. Invented arrangements and records use open workspace rather than exactly as many slots as the eventual number of solutions. The source and guide-only data are separate from student scaffolds. Independent design findings must close before rendering; maker and independent visual reviews remain later gates. No extra PDF operation marker will be run.
