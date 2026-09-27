# Geometry Analysis - investigation families

Facilitator planning cards. These are proposed investigations, not classroom-piloted student packets. The JSON alongside this file is the editable source; this Markdown is generated.

<a id="ga-01"></a>
## GA-01 - Can the order of two turns change the result?

Primary field: 22. Related: 20, 53. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does continuous rotational symmetry differ from simply permuting labels, and where does noncommutativity first appear?

**Anchor.** Rotations of the plane about one center commute. In three dimensions, rotations about different fixed axes need not commute. Rotation through any real angle is allowed; quarter-turns supply an exactly checkable witness.

**Bridge (exact-special-case).** A marked rigid box carries the usual rotation action of SO(3); arrows record images of an initial direction. Limits: The quarter-turn subgroup alone does not exhibit Lie algebra, covering-space theory, or all continuous rotations.

**Prerequisite gates.**

- **Entry:** O: follow a spoken turn instruction and distinguish three fixed room directions.
- **Explore:** V: record an arrow as right, forward, or up; optionally use signed coordinates.
- **Explain:** P: show different final arrows under two orders, which is a complete counterexample.
- **Prove:** L/D: rotation matrices and matrix exponentials for continuous generators.
- **Reading:** Oral launch; a partner may record turn words.
- **Arithmetic:** None for manipulation; signed unit vectors for checking.
- **Reasoning:** Hold axes fixed in the room, not attached to the moving box; spatial memory is the main demand.
- **Hard Stop:** Stop before Lie brackets unless matrix multiplication and derivatives are available.

**Materials and preparation (10 minutes).** A box marked with one large arrow, a paper compass showing fixed x,y,z axes, and two turn cards.

**Launch.** Start with the arrow pointing along positive z. Turn a quarter-turn about x, then about y. Reset completely and reverse the order. Can both results be right? Invent another pair of turns and predict before moving.

**Learner choices.** Learners choose turn pairs, starting arrows, and a recording method; they may ask a partner to execute their prediction.

**Hour menu.** 0–10 freely rotate and describe the box; 10–15 establish right-hand positive turns with a demonstration; 15–35 compare chosen orders; 35–40 movement reset; 40–55 build a repeatable witness or compare planar turns; 55–60 share one checked sequence.

**Explore.**

- Which turns seem interchangeable?
- Does starting with a different arrow conceal the difference between the transformations?

**Hint ladder.**

1. Keep the axis card on the table.
2. Track only the marked arrow before attempting all faces.

**Checked instance.** Use right-hand positive 90° rotations Rx and Ry on the starting vector (0,0,1).

**Reasoning.** Rx first sends z to −y; Ry then leaves −y fixed, so the result is (0,−1,0). Ry first sends z to x; Rx leaves x fixed, giving (1,0,0). The different arrows prove RxRy≠RyRx, with composition order explained verbally. Plane rotations through a then b both add a+b to the initial angle, so they commute.

**Boundary.** Two turns about the same axis do commute. Also, testing just one vector can miss a difference: equality of a single image does not establish equality of transformations.

**Extensions.**

- Find a three-turn sequence that returns the arrow but not the whole box.
- For matrix-ready learners, vary a small angle and compare the commutator with the identity; the limiting Lie bracket needs calculus.

**Satisfying stop.** A reproducible pair of order-sensitive turns and an explanation using the final arrow.

**Prior use.** Week 3 explored permutation composition; this uses continuous physical rotations and fixed axes. Actual use of related instances remains unknown.

**Sources.**

- [Peter Woit, Quantum Theory, Groups and Representations](https://www.math.columbia.edu/~woit/QMbook/qmbook-latest.pdf), Chapters 4–6; orthogonal groups and rotations. Inspection: Relevant text and definitions inspected; box example derived directly.

<a id="ga-02"></a>
## GA-02 - Can opposite fence heights always be different?

Primary field: 26. Related: 55. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can continuity guarantee an exact equality when no formula for the shape is known?

**Anchor.** For every continuous real-valued function h on a circle, some antipodal points have equal values: g(t)=h(t)−h(t+1/2) is continuous and g(1/2)=−g(0).

**Bridge (exact-special-case).** Sliding opposite markers samples a continuous periodic function; exchanging their roles reverses the sign of the difference. Limits: A finite list of isolated posts does not satisfy the continuous-domain hypothesis, and a model cannot resolve tiny physical height differences exactly.

**Prerequisite gates.**

- **Entry:** O: compare which of two markers is higher and follow opposite positions.
- **Explore:** V: read a closed profile represented on a strip with joined ends.
- **Explain:** P: argue that the higher marker must become lower after half a turn.
- **Prove:** P/X: intermediate value reasoning or its real-analysis proof.
- **Reading:** Oral; no numerical labels needed initially.
- **Arithmetic:** None for comparison; fractions only for the optional half-turn parameter.
- **Reasoning:** Track two points simultaneously and distinguish observed equality from an existence argument.
- **Hard Stop:** Higher-dimensional Borsuk–Ulam is not proved by this circle argument.

**Materials and preparation (12 minutes).** A paper strip with a continuous wavy line whose end heights agree; a duplicated strip and two linked markers half a period apart.

**Launch.** Draw a fence top that meets at its seam without a jump; corners are allowed, jumps are not. Try to keep the red marker higher than the blue one through half a turn, with the markers always opposite.

**Learner choices.** Choose the profile, starting position, direction of motion, and an attempted escape from equality.

**Hour menu.** 0–10 compare moving marker heights freely; 10–15 establish the continuous seam and opposition; 15–35 try to defeat equality; 35–40 stand and exchange places; 40–55 explain the exchange argument or test missing assumptions; 55–60 share a conjecture and its reason.

**Explore.**

- What has swapped after half a turn?
- Can six separate posts avoid matching opposite heights?

**Hint ladder.**

1. Ignore the exact heights and record only higher, same, lower.
2. Start and finish with the markers at each other's initial positions.

**Checked instance.** Use six post heights 0,4,1,3,0,2 in circular order, with straight ramps joining neighbors. Find one matching pair.

**Reasoning.** At the start the difference between opposite points is 0−3=−3. One sixth of a turn later it is 4−0=4. On these straight ramps the difference is linear, so equality occurs 3/7 of the way along that first sixth, at t=1/14 of a turn. The shared height is 12/7. More generally a sign reversal and continuity guarantee some equality without calculating it.

**Boundary.** With only the six isolated posts available, opposite differences are −3,4,−1 and their negatives: none is zero. Continuous ramps are essential.

**Extensions.**

- Bracket the crossing and halve the bracket, separating guaranteed location error from measurement error.
- Ask about matching two continuous measurements on a sphere; state the higher theorem as a continuation, not a proved result.

**Satisfying stop.** The half-turn argument that defeats every continuous attempted fence.

**Prior use.** New continuous strand; no matching worksheet in Weeks 1–10. The advisory atlas example suggested this mechanism; this exact ramp instance is separately checked.

**Sources.**

- [Jiří Lebl, Basic Analysis I](https://www.jirka.org/ra/realanal.pdf), §3.3, intermediate value theorem; circle deduction supplied here. Inspection: Theorem inspected; complete special-case argument supplied.

<a id="ga-03"></a>
## GA-03 - Can infinitely many points fit under very short covers?

Primary field: 28. Related: 03, 40. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why is counting points different from measuring length, and what does a countable covering argument actually prove?

**Anchor.** A countable set {p1,p2,…} in R has outer measure zero: for every ε>0, cover pn by an open interval of length ε/2^(n+1); the sum of lengths is ε/2<ε.

**Bridge (exact-special-case).** Each chosen point is assigned a genuine interval; a rule, rather than an impossible completed physical construction, specifies all intervals. Limits: Finite paper strips only illustrate initial stages. Zero outer measure does not assert that the set is empty or countable.

**Prerequisite gates.**

- **Entry:** O/C: cover named dots and compare total used strip lengths.
- **Explore:** F: repeatedly halve a length budget and discuss a listed infinity.
- **Explain:** P: explain why the nth listed point is covered and why the total stays below the requested budget.
- **Prove:** X: definition of outer measure; geometric-series bound suffices for this theorem.
- **Reading:** Short numbered labels; oral explanation with an adult recorder works.
- **Arithmetic:** Halves and geometric sums; optional enumeration of rational pairs.
- **Reasoning:** Separate every individual point receiving a cover from finitely many observed covers.
- **Hard Stop:** Uncountability and nonmeasurability require new arguments; do not infer either from a sparse-looking picture.

**Materials and preparation (10 minutes).** A number line, named point cards, paper strips of halving widths, and a visible total-length budget.

**Launch.** Your opponent names a first, second, third, and later point. Before hearing later points, promise a covering rule that spends less than one unit of total length, even if the list never ends.

**Learner choices.** Learners allocate the budget, place covers, allow overlaps, and choose adversarial point lists.

**Hour menu.** 0–10 cover five chosen points using little paper; 10–15 state the never-ending challenge; 15–35 invent and test budget rules; 35–40 reset; 40–55 explain one rule for all numbered positions or list rational numbers; 55–60 report precisely what was proved.

**Explore.**

- Must each interval have the same width?
- Could the points be dense and still admit your rule?

**Hint ladder.**

1. Reserve some budget for later points.
2. Give each new point half as much as the previous point.

**Checked instance.** Cover p_n=1/n, n≥1, using total length below 1/100.

**Reasoning.** Center an open interval of length (1/100)/2^(n+1) at each 1/n. Every listed point lies inside its assigned interval. The total interval length is (1/100)(1/4+1/8+…)=1/200, below the requested budget. Overlaps only reduce union length. Replace 1/100 by any positive ε to establish zero outer measure for this listed set.

**Boundary.** Assigning every listed point its own interval of one fixed positive width makes the sum of assigned lengths diverge. This particular budget proof therefore uses shrinking widths, despite possible overlaps. It does not exclude other finite covers of special sets such as {1/n}.

**Extensions.**

- Enumerate rational numbers by numerator-denominator diagonals and apply the same rule, despite density.
- Contrast with the uncountable Cantor set in GA-29; a small cover does not establish countability.

**Satisfying stop.** A budget rule that covers every numbered point and an exact total-length bound.

**Prior use.** No direct prior-week instance; connects to infinite-series reasoning rather than routine counting. Actual use is unrecorded.

**Sources.**

- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/MIRA.pdf), §2A, outer measure and countable sets. Inspection: Relevant definitions and countable-cover argument inspected.

<a id="ga-04"></a>
## GA-04 - Follow a square root around a circle

Primary field: 30. Related: 22, 55. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Can a locally consistent choice of root fail to return to its starting value after a closed journey?

**Anchor.** Along z=e^(it), 0≤t≤2π, the continuous root starting at w=1 is w=e^(it/2), so it ends at −1. A continuous single-valued square root cannot be defined on the entire unit circle.

**Bridge (exact-special-case).** Moving arrows realize complex squaring: double the angle and square the length. Tracking one root preserves continuity along a path. Limits: The construction proves a circle obstruction, not all monodromy theory or the general existence theorem for holomorphic roots.

**Prerequisite gates.**

- **Entry:** O/V: track angles and paired opposite arrows on a circle.
- **Explore:** F/A: half angles and complex multiplication, or a supplied double-angle rule.
- **Explain:** P: explain why a chosen root cannot jump between opposite alternatives.
- **Prove:** A/P: express w(t)/e^(it/2) as a continuous value in {1,−1}.
- **Reading:** Short labels; proof extension uses function notation.
- **Arithmetic:** Halving angles; optional multiplication with i.
- **Reasoning:** Distinguish the moving target, both candidate roots, and the tracked choice.
- **Hard Stop:** Holomorphic continuation on general domains requires complex analysis; angle tracking alone does not establish it.

**Materials and preparation (8 minutes).** Two circle diagrams, a target arrow, red and blue root arrows, and four quarter-turn cards.

**Launch.** Move the target once around its circle. Keep a root arrow whose doubled angle always points at the target, and never jump your root. Where does it finish? Choose a different route or starting root and try again.

**Learner choices.** Choose direction, number of target circuits, intermediate checkpoints, and whether to display both roots.

**Hour menu.** 0–10 learn the squaring action with free arrow play; 10–15 state the no-jump rule; 15–35 follow and record routes; 35–40 movement reset; 40–55 explain one-turn failure and two-turn recovery; 55–60 share a route certificate.

**Explore.**

- Why are there two roots at every target point?
- Could you exchange roots halfway without breaking continuity?

**Hint ladder.**

1. Start at target 1 with roots 1 and −1.
2. Each quarter-turn of the target advances the tracked root by an eighth-turn.

**Checked instance.** Start the target at 1 and the chosen root at 1. Follow the target through 1,i,−1,−i,1 counterclockwise.

**Reasoning.** The tracked roots have arguments 0°,45°,90°,135°,180°; their squares have exactly the target arguments. The ending root is −1. Any continuous competing choice differs from this one by a sign, and that sign cannot change continuously while restricted to {1,−1}. Thus one circuit cannot yield a continuous periodic root choice. Two target circuits advance the root 360° and restore it.

**Boundary.** Allow a jump from one root to the other and a single-valued rule such as a principal branch becomes possible on a cut diagram, but it is discontinuous at the cut.

**Extensions.**

- For cube roots, one target circuit cyclically permutes three choices; three circuits restore them.
- Investigate a loop that does not wind around zero; label general winding results as later topology.

**Satisfying stop.** Explain why a no-jump root needs two target turns to return.

**Prior use.** Week 3 cycles are an algebraic comparison; the new obstruction concerns continuous root selection around a loop.

**Sources.**

- [Jiří Lebl, Guide to Cultivating Complex Analysis](https://www.jirka.org/ca/ca.pdf), Example 10.2.6, continuation of a square root; §1.2 polar multiplication. Inspection: Relevant example inspected; elementary circle proof supplied.

<a id="ga-05"></a>
## GA-05 - Can an averaging landscape hide a peak?

Primary field: 31. Related: 05, 35. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a local averaging rule force a global maximum principle and uniqueness?

**Anchor.** On a finite connected graph with a nonempty fixed boundary, each interior value equals the arithmetic mean of its neighbors. Any strict excess over all boundary values would propagate through equal maximal neighbors to the boundary, a contradiction.

**Bridge (shared-mechanism).** The learner solves an exact discrete Dirichlet problem and uses maximum propagation. Limits: This is a discrete counterpart to classical potential theory; no convergence to a harmonic function on a continuum domain is claimed.

**Prerequisite gates.**

- **Entry:** C/F: add small values and divide by two; colors can first compare heights.
- **Explore:** A: solve two simultaneous linear equations or use balancing.
- **Explain:** P: chase an assumed interior maximum along neighbors to a fixed boundary.
- **Prove:** P/L: connected-graph argument; continuous mean-value proof needs analysis.
- **Reading:** One short averaging rule; adult can record equations.
- **Arithmetic:** Whole numbers and halves; selected example uses integers.
- **Reasoning:** Track fixed versus changeable vertices and apply the rule simultaneously.
- **Hard Stop:** Continuum harmonicity and Green functions require calculus and limits.

**Materials and preparation (8 minutes).** Four dots joined in a path, endpoint cards 0 and 9, movable interior number cards, and optional extra graph templates.

**Launch.** Keep the end dots at 0 and 9. Choose the two middle heights so each equals the average of its neighbors. Then invent a connected landscape with fixed boundary and try to hide a height above every boundary value.

**Learner choices.** Choose a graph, boundary values, and proposed solution; exchange designs to seek a hidden peak.

**Hour menu.** 0–10 play with averaging pairs; 10–15 distinguish fixed and interior dots; 15–35 solve and invent landscapes; 35–40 reset; 40–55 chase maxima or compare two solutions; 55–60 present one impossibility argument.

**Explore.**

- If a highest interior dot equals its neighbors' average, what must those neighbors be?
- What happens if a component has no fixed boundary?

**Hint ladder.**

1. An average cannot exceed every number being averaged.
2. Subtract two proposed solutions and inspect the biggest difference.

**Checked instance.** Solve the path 0—a—b—9 with averaging at a and b.

**Reasoning.** The equations 2a=b and 2b=a+9 give a=3 and b=6. They can also be found by equal spacing along the path. For uniqueness, subtract any two solutions: boundary differences are zero and interior differences still average neighbors. A positive maximum forces every neighbor equal; connectedness propagates it to a zero boundary, impossible. Apply the same argument to a negative minimum.

**Boundary.** A disconnected component with no boundary can have any constant value. It therefore defeats uniqueness and can support a peak above the boundary elsewhere.

**Extensions.**

- Give three unequal boundary values and compare how changing one influences interiors.
- Compare the discrete proof with mean values on every circle for a true harmonic function; use GA-35 for continuous polynomial examples.

**Satisfying stop.** A solved landscape and the reason a connected averaging graph cannot hide a new highest value.

**Prior use.** Week 10 networks supply graph familiarity; here edges constrain values rather than routes. This instance is new and unpiloted.

**Sources.**

- [John Hunter, Notes on Partial Differential Equations](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), §§2.1 and 2.3, harmonic mean-value and maximum principles. Inspection: Continuous statements inspected; finite graph proof supplied independently.

<a id="ga-06"></a>
## GA-06 - When two complex branches meet

Primary field: 32. Related: 14, 30. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does a zero set in two complex variables develop a singularity, and why can a real slice hide most of it?

**Anchor.** For the polynomial F(z,w)=z²+w² on C², F=0 is the union of two complex lines w=iz and w=−iz. They meet only at the origin. In contrast its real slice consists only of (0,0).

**Bridge (exact-special-case).** Actual complex polynomial equations and their solution branches are investigated; this is a genuine analytic variety. Limits: Factoring this example does not prove Hartogs extension, general singularity classification, or that all scalar holomorphic zero sets behave the same way.

**Prerequisite gates.**

- **Entry:** A/X: complex numbers, i²=−1, and factoring a quadratic; elementary age access is not claimed.
- **Explore:** V/A: use two complex-coordinate diagrams and parameterize solution pairs.
- **Explain:** P: verify factorization and prove that the two branches meet only at zero.
- **Prove:** X: complex manifolds and the local graph definition for a full singularity proof.
- **Reading:** Symbolic text; a facilitator may separate algebra from geometric interpretation.
- **Arithmetic:** Signed numbers and complex multiplication; no calculus for the factorization.
- **Reasoning:** Remember that each complex coordinate has two real coordinates.
- **Hard Stop:** Stop before claiming the origin is singular solely because one gradient vanishes; use the explicit two-branch local structure.

**Materials and preparation (10 minutes).** Two Argand diagrams labeled z and w, paired colored markers, and a table for recording solution pairs.

**Launch.** Choose any complex z and find every w satisfying z²+w²=0. Can your partner move continuously through solutions? What changes if both coordinates must be real? Try changing the equation to z²+w²=1.

**Learner choices.** Choose parameter paths, real or complex restrictions, and a branch to track; design a slice that conceals or reveals solutions.

**Hour menu.** 0–10 play with multiplication by i; 10–15 introduce the equation and paired diagrams; 15–35 parameterize branches and compare slices; 35–40 reset; 40–55 study the constant-one equation or discuss local structure; 55–60 state a proved algebraic fact.

**Explore.**

- What does multiplication by i do geometrically?
- Does a drawing containing one isolated real point establish an isolated complex zero?

**Hint ladder.**

1. Factor z²+w² over C.
2. For nonzero z, divide by z² and solve for w/z.

**Checked instance.** Describe all solutions of z²+w²=0 and test z=1+i.

**Reasoning.** Factor as (w−iz)(w+iz)=0. Since complex numbers have no zero divisors, w=iz or w=−iz. For z=1+i the roots are −1+i and 1−i. Their squares are −2i, while z²=2i. The branches coincide only when iz=−iz, hence z=w=0. For real coordinates, both squares are nonnegative, so their sum vanishes only at the origin.

**Boundary.** The real slice is just one point, yet every neighborhood of the complex origin contains infinitely many nonzero solutions. Real pictures cannot certify complex isolation.

**Extensions.**

- Replace zero by one: at any solution the complex gradient (2z,2w) is nonzero, so the holomorphic implicit-function theorem gives a smooth complex curve; this last step needs that theorem.
- Compare z²−w³=0 using z=t³,w=t²; parameterization alone is not a proof of local nonsingularity.

**Satisfying stop.** An exhaustive parameterization and a clear explanation of why the real and complex pictures differ.

**Prior use.** No existing week supplies this complex-variable content; this deliberately keeps a substantial algebra prerequisite.

**Sources.**

- [Jiří Lebl, Tasty Bits of Several Complex Variables](https://www.jirka.org/scv/scv.pdf), §6.5, Definition 6.5.5 and Example 6.5.6, intersecting complex manifolds. Inspection: Relevant definition and example inspected; plus-sign variant factored directly.

<a id="ga-07"></a>
## GA-07 - Invent a polynomial that triples an angle

Primary field: 33. Related: 30, 41. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can the same family of functions be generated by a geometric action and by an algebraic recurrence?

**Anchor.** Chebyshev polynomials satisfy T_n(cos θ)=cos(nθ), T_0=1, T_1=x, and T_(n+1)=2xT_n−T_(n−1) for n≥1. These identities define genuine polynomial angle multipliers.

**Bridge (exact-special-case).** Circle projections and polynomial substitution represent the same exact function on −1≤x≤1. Limits: A measured projection is approximate; the recurrence and trig identity establish equality. This does not cover all special functions.

**Prerequisite gates.**

- **Entry:** V/F: read horizontal coordinates on a unit circle and multiply an angle.
- **Explore:** A: expand simple polynomials and substitute fractions.
- **Explain:** P/A: derive T_2 and T_3 from recurrence and check a trigonometric derivation.
- **Prove:** A/P: induction with the cosine addition identity.
- **Reading:** Short symbolic instructions; graphing labels can be read aloud.
- **Arithmetic:** Signed fractions, multiplication, and cubic expressions.
- **Reasoning:** Distinguish the angle from its horizontal coordinate; multiple angles may share a cosine.
- **Hard Stop:** Bessel functions, gamma integrals, and approximation theory need additional calculus or analysis.

**Materials and preparation (8 minutes).** Unit-circle sheet, angle marker, graph paper, and recurrence cards T_0=1 and T_1=x.

**Launch.** An angle machine receives only x=cos θ, not θ itself. Build a polynomial that outputs cos(3θ). Can different angles with the same input demand different outputs? Choose checks that might expose an error.

**Learner choices.** Choose test angles, expand through the recurrence, or derive with angle formulas; compare independently obtained answers.

**Hour menu.** 0–10 explore projections while turning arrows; 10–15 state the polynomial-machine task; 15–35 derive and challenge candidates; 35–40 reset; 40–55 graph the machine or compose multipliers; 55–60 share a derivation rather than only a table.

**Explore.**

- Why does squaring x help double an angle?
- What happens when one angle multiplier feeds another?

**Hint ladder.**

1. First build T_2 from 2x·x−1.
2. Use T_3=2xT_2−T_1.

**Checked instance.** Find T_3 and compute its output at x=1/2.

**Reasoning.** The recurrence gives T_2=2x²−1 and T_3=2x(2x²−1)−x=4x³−3x. At x=1/2 the output is 1/2−3/2=−1, matching cos(3·60°). To see why the same x is enough, cosine addition gives cos((n+1)θ)+cos((n−1)θ)=2cos θ cos(nθ), so induction constructs a polynomial in x alone.

**Boundary.** Do not identify T_3(x) with cos(3x). The input is the cosine of an angle, not the angle itself; at x=0 the two expressions are 0 and 1.

**Extensions.**

- Prove T_m(T_n(x))=T_(mn)(x) first on [−1,1], then as polynomials.
- Study how T_n oscillates with equal extreme heights; connect to minimax approximation only after defining the error criterion.

**Satisfying stop.** A correct triple-angle polynomial with one explanation and one adversarial check.

**Prior use.** Week 3 repeated actions is a conceptual comparison; polynomial functions and projections create new substance.

**Sources.**

- [NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/18.5), Equation 18.5.1; recurrence relations in §18.9. Inspection: Displayed identities inspected; n=2,3 examples expanded directly.

<a id="ga-08"></a>
## GA-08 - Can a motion wait and still obey its rate law?

Primary field: 34. Related: 26. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** When does a differential equation determine a unique future, and how can a plausible rate rule fail?

**Anchor.** For nonnegative y and t≥0, the initial-value problem y'=2√y, y(0)=0 has y_c(t)=0 for t≤c and (t−c)² for t≥c, for every c≥0. The right side is not locally Lipschitz at y=0.

**Bridge (exact-special-case).** Learners choose and verify actual differentiable solutions of an initial-value problem. Limits: An arrow picture suggests motion but does not verify the equation. This counterexample does not say all non-Lipschitz equations are nonunique.

**Prerequisite gates.**

- **Entry:** A/D: functions, square roots, and derivatives of quadratics.
- **Explore:** V: draw a function with a chosen waiting time and inspect the join.
- **Explain:** D/P: check both pieces, the initial condition, and the derivative at the join.
- **Prove:** X: local Lipschitz condition and a uniqueness theorem.
- **Reading:** Symbolic task; oral discussion can support interpretation.
- **Arithmetic:** Squares, square roots, and nonnegative differences.
- **Reasoning:** Distinguish a rate law from a step-by-step update rule and check the exceptional join.
- **Hard Stop:** Do not lower this to a coin-moving game and call it an ODE proof; derivatives are central.

**Materials and preparation (5 minutes).** Graph paper, pencils, and three blank time-height axes; optional graphing tool.

**Launch.** Start at height zero and obey speed=2√height at every time. Can you stay still for a while and then leave? Choose your own waiting time and defend the complete motion, including the moment you start.

**Learner choices.** Learners select waiting times, propose other departures, and try to disprove each other's solution at the join.

**Hour menu.** 0–10 sketch possible height-time motions; 10–15 clarify that slope is the required speed; 15–35 test formulas and join points; 35–40 reset; 40–55 compare with y'=y or inspect Lipschitz ratios; 55–60 explain the failure of uniqueness.

**Explore.**

- What slope does the equation demand at zero?
- Why does knowing the slope at one instant not settle the whole future?

**Hint ladder.**

1. After leaving at time c, try a translated square.
2. Compute the derivative at c from both sides, not just away from c.

**Checked instance.** Check the motion that waits until c=2 and then follows y=(t−2)².

**Reasoning.** For t<2 both y' and 2√y are zero. For t>2, y'=2(t−2), and nonnegativity of t−2 gives 2√((t−2)²)=2(t−2). At t=2, the right difference quotient is h²/h=h→0 and the left quotient is zero, so the derivative exists and equals zero. The initial height is zero. Waiting forever is another solution with exactly the same initial condition.

**Boundary.** For y'=y, y(0)=0, the analogous delayed exponential cannot leave zero while remaining differentiable and satisfying the equation; local Lipschitz uniqueness applies. Failure of one hypothesis permits, but does not force, nonuniqueness.

**Extensions.**

- Calculate [2√h−0]/h=2/√h to see why no uniform local Lipschitz constant exists.
- Compare finite-time blow-up in GA-34: uniqueness and existence for all time are separate properties.

**Satisfying stop.** Two fully checked different futures for the same initial data.

**Prior use.** No existing worksheet covers rate-law uniqueness; this is intentionally a calculus-gated extension upward.

**Sources.**

- [Gerald Teschl, Ordinary Differential Equations and Dynamical Systems](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf), §2.2, Theorem 2.2 and Problem 2.6 on local Lipschitz continuity. Inspection: Existence/uniqueness hypotheses inspected; waiting solutions checked directly.

<a id="ga-09"></a>
## GA-09 - A wave that travels and a shape that fades

Primary field: 35. Related: 42. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What differences between partial differential equations can be discovered from exact solutions before learning a general solution method?

**Anchor.** On the whole line, u(x,t)=sin(x−t) solves u_tt=u_xx. On [0,π] with zero endpoint values, v(x,t)=e^(−t)sin x solves v_t=v_xx. Partial differentiation verifies both.

**Bridge (exact-special-case).** Learners manipulate exact continuum solution profiles and distinguish translation from amplitude decay. Limits: Sliding paper is a representation, not a physical heat experiment; arbitrary token-spreading rules are not claimed to converge to these PDEs.

**Prerequisite gates.**

- **Entry:** V/A: read graphs and understand a formula depending on space and time.
- **Explore:** D: differentiate sine and exponential while holding the other variable fixed.
- **Explain:** D/P: substitute into each PDE and check initial/boundary conditions.
- **Prove:** X: general existence or convergence requires PDE analysis.
- **Reading:** Symbolic formulas; a partner can manage the graph while another differentiates.
- **Arithmetic:** Coordinates and trigonometric values; exponentials for the fading profile.
- **Reasoning:** Separate position x from time t and distinguish time derivative orders.
- **Hard Stop:** Without derivatives, stop at comparing graphs and label the PDE connection as supplied information.

**Materials and preparation (10 minutes).** A sine-wave transparency that can slide, fixed axes, and three printed or sketched fading profiles.

**Launch.** Here are two shape rules: slide sin x to the right, or keep it in place while multiplying its height by e^(−t). Choose times to compare. Which differential equation does each obey, and can either obey the other's equation?

**Learner choices.** Choose time slices, derivative order, and a point where a proposed equation is likely to fail.

**Hour menu.** 0–10 slide and resize profiles; 10–15 distinguish x and t; 15–35 verify the two rules and boundary data; 35–40 reset; 40–55 superpose solutions or test a wrong equation; 55–60 share a diagnostic calculation.

**Explore.**

- Does a peak move or only shrink?
- Why does a wave need an initial velocity as well as an initial shape?

**Hint ladder.**

1. For u, compute u_t first, then u_tt.
2. Check equality symbolically before substituting one convenient point.

**Checked instance.** Verify both formulas and test whether sin(x−t) solves the heat equation.

**Reasoning.** For u, u_t=−cos(x−t), u_tt=−sin(x−t), and u_xx=−sin(x−t), so the wave equation holds. The heat equation would require −cos(x−t)=−sin(x−t), which fails, for example at x=t=0. For v, both v_t and v_xx equal −e^(−t)sin x. Also v(0,t)=v(π,t)=0 and v(x,0)=sin x. Equal initial shapes therefore do not imply equal evolution under different laws.

**Boundary.** The traveling wave on the whole line does not satisfy fixed zero boundary conditions at 0 and π for every t. Changing the domain and boundary data changes the problem.

**Extensions.**

- Show that sin x cos t is a standing wave with zero endpoint displacement and zero initial velocity.
- Add two exact solutions of the same linear PDE and explain why addition works; it generally fails for nonlinear equations.

**Satisfying stop.** One complete PDE substitution and a clear graph-based distinction between motion and decay.

**Prior use.** Week 9 billiards involves trajectories; this concerns functions spread over space, so it is not a renamed orbit activity.

**Sources.**

- [John Hunter, Notes on Partial Differential Equations](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), §5.1 and §7.1; heat and wave solutions compared. Inspection: Relevant equations and d'Alembert discussion inspected; selected formulas differentiated directly.

<a id="ga-10"></a>
## GA-10 - Program a repeating orbit by choosing its itinerary

Primary field: 37. Related: 39. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Can we design periodic behavior in a nonlinear system by solving backward rather than guessing starting points?

**Anchor.** The tent map on [0,1] is T(x)=2x for x≤1/2 and T(x)=2−2x for x≥1/2. Its inverse branches are L(y)=y/2 and R(y)=1−y/2; branch words can specify exact periodic orbits.

**Bridge (exact-special-case).** A number-line point is the actual state of a continuous interval map; legal moves are evaluations of T. Limits: Three observed steps do not prove chaotic dynamics. Finite decimal arithmetic can manufacture periodic orbits.

**Prerequisite gates.**

- **Entry:** F/A: double fractions, subtract from two, and follow a two-piece rule.
- **Explore:** A: compose affine inverse branches and solve one linear equation.
- **Explain:** P: verify a complete orbit and exclude smaller periods.
- **Prove:** P/X: general symbolic coding and chaos require precise dynamical definitions.
- **Reading:** Short symbolic rules; two colored interval halves support reading.
- **Arithmetic:** Signed fractions; denominators seven in the checked example.
- **Reasoning:** Track whether a letter names the current half or an inverse branch; use one convention consistently.
- **Hard Stop:** No assertion of randomness or chaos follows merely from an irregular plot.

**Materials and preparation (8 minutes).** Number line [0,1], two branch cards, fraction markers, and graph paper; no computer required.

**Launch.** Choose a three-letter pattern of left and right halves. Find a point that repeats that itinerary forever under T. Work backward if forward guessing stalls. Avoid landing exactly at the midpoint while coding the halves.

**Learner choices.** Choose itineraries, forward or backward reasoning, and a candidate starting point to challenge.

**Hour menu.** 0–10 iterate easy fractions; 10–15 fix the itinerary convention; 15–35 engineer periodic points; 35–40 reset; 40–55 compare periods or nearby starts; 55–60 present an exact orbit rather than a decimal trace.

**Explore.**

- How can one target value have two possible previous values?
- Does a word of length three always force least period three?

**Hint ladder.**

1. Solve x=L(R(R(x))) for the word LRR.
2. Verify which half contains each intermediate value after solving.

**Checked instance.** Find a point with repeating current-half itinerary LRR.

**Reasoning.** Writing the three-step return using inverses gives x=(1−(1−x/2)/2)/2=1/4+x/8, hence x=2/7. Forward verification gives 2/7→4/7→6/7→2/7; the halves are left,right,right. The three values are distinct, so the least period is three. Inverse algebra found a candidate; checking the branch inequalities made it a valid solution.

**Boundary.** The word LLL yields the fixed point zero rather than least period three. Points landing at 1/2 have a coding ambiguity unless a convention is imposed, so our core avoids them.

**Extensions.**

- Find the starting point for RRL. Answer: 4/7→6/7→2/7→4/7, the same orbit as LRR with a different starting point. Verify the half labels at each step.
- Compare nearby rational starts for several steps; distinguish finite sensitivity evidence from a theorem about chaos.

**Satisfying stop.** Construct and verify one prescribed repeating orbit.

**Prior use.** Week 4 modular orbits were finite cyclic dynamics; here the state interval is continuous and the map folds it.

**Sources.**

- [Gerald Teschl, Ordinary Differential Equations and Dynamical Systems](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf), §§11.3–11.5, tent map and symbolic dynamics. Inspection: Tent-map definition and symbolic mechanism inspected; itinerary solved directly.

<a id="ga-11"></a>
## GA-11 - How much does an addition machine have to reveal?

Primary field: 39. Related: 26. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Does a rule about combining inputs determine an entire function, or do hidden domain assumptions matter?

**Anchor.** If f:Q→R is additive, then f(q)=qf(1). On R, continuity at one point forces the same form; additivity alone allows nonstandard functions. The core proves only the rational statement.

**Bridge (exact-special-case).** An actual function obeys f(x+y)=f(x)+f(y); learners infer values from the equation rather than from a finite pattern table. Limits: The elementary core does not construct a pathological additive function on all of R or prove the general regularity theorem.

**Prerequisite gates.**

- **Entry:** C: combine whole-number inputs under one stated rule.
- **Explore:** F/A: use negatives and fractions and name an unknown output.
- **Explain:** P: force integer and rational values using repeated addition.
- **Prove:** P/X: extending the rational linearity conclusion to all real inputs uses a stated regularity assumption, such as continuity; constructing nonstandard additive extensions is a separate algebraic task. The restricted irrational domain here uses Q-linear independence.
- **Reading:** Short rules; symbolic follow-up can be adult recorded.
- **Arithmetic:** Addition, division, signed fractions.
- **Reasoning:** Distinguish values forced by a universal rule from guesses suggested by examples.
- **Hard Stop:** Do not claim the rational proof covers arbitrary real inputs without a continuity argument.

**Materials and preparation (5 minutes).** Input-output cards, blank cards for learner-selected inputs, and a rule card.

**Launch.** The machine always obeys f(x+y)=f(x)+f(y), and f(1)=3. Choose an input whose output you think is forced. Convince a skeptical partner using only the rule. Then try an input your argument cannot reach.

**Learner choices.** Choose inputs, chains of decompositions, and adversarial output proposals; decide which domain the machine accepts.

**Hour menu.** 0–10 invent whole-number machines; 10–15 impose the addition rule; 15–35 force zero, negative, and fractional outputs; 35–40 reset; 40–55 examine irrational inputs or prove the rational theorem; 55–60 classify forced and unproved claims.

**Explore.**

- What must f(0) be?
- Why does a repeated-addition proof reach 2/3 but not √2?

**Hint ladder.**

1. Use f(0)=f(0)+f(0).
2. Three copies of the input 2/3 add to two.

**Checked instance.** Determine f(2/3) and decide whether f(√2)=5 is already impossible from the rational argument.

**Reasoning.** Additivity gives f(2)=6 and 3f(2/3)=f(2)=6, so f(2/3)=2. On the restricted domain D={a+b√2:a,b rational}, define f(a+b√2)=3a+5b. Representation is unique because √2 is irrational, and coordinatewise addition verifies additivity. Thus f(1)=3 and f(√2)=5 coexist on D. This is an exact counterexample to extending the rational conclusion by algebra alone.

**Boundary.** If continuity is additionally required on D, rational numbers approaching √2 force f(√2)=3√2, contradicting 5. Continuity is a mathematical condition, not a property established by a smooth-looking sketch.

**Extensions.**

- For arbitrary f(1)=c, prove f(m/n)=cm/n with n positive.
- Replace additivity by positive multiplicativity f(x+y)=f(x)f(y); logarithms turn it into an additive equation when those tools are available.

**Satisfying stop.** One forced fractional output and a correct statement of the domain on which the proof works.

**Prior use.** No prior-week equivalent; differs from guessing patterns because the universal functional equation is the evidence.

**Sources.**

- [Daniel Reem, Remarks on the Cauchy functional equation and variations of it](https://arxiv.org/pdf/1002.3721), Introduction and §2, regularity assumptions for additive functions. Inspection: Relevant discussion inspected; rational proof and restricted-domain counterexample supplied.

<a id="ga-12"></a>
## GA-12 - Smaller pieces: a finite total or an endless climb?

Primary field: 40. Related: 26, 28. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can terms become tiny while their accumulated sum still exceeds every bound?

**Anchor.** Geometric partial sums have explicit shrinking remainders. Harmonic partial sums are unbounded: each block from 2^(k−1)+1 through 2^k contains 2^(k−1) terms at least 1/2^k, contributing at least 1/2.

**Bridge (exact-special-case).** Lengths and grouped fractions are actual partial sums; the infinite claim is supported by a rule producing arbitrarily many blocks. Limits: Physical strip width limits terminate a demonstration, not the mathematical sequence. Nothing here licenses rearranging a conditionally convergent series.

**Prerequisite gates.**

- **Entry:** O/F: compare halves and collect successive pieces.
- **Explore:** F/M: use reciprocals, powers of two, and equal-size blocks.
- **Explain:** P: give a construction exceeding a chosen target.
- **Prove:** P: quantified unboundedness, contrasting a geometric remainder bound.
- **Reading:** Fraction labels; oral grouping with an adult recorder is possible.
- **Arithmetic:** Unit fractions, doubling, and simple lower bounds.
- **Reasoning:** Track a bound for a whole block without needing its exact sum.
- **Hard Stop:** A graph leveling off over finitely many terms is not evidence sufficient for convergence.

**Materials and preparation (10 minutes).** Fraction strips or drawn rectangles, cards 1/n, and blank target cards.

**Launch.** Two machines pay 1,1/2,1/4,… or 1,1/2,1/3,…. Choose a target total. Can you guarantee that either machine will pass it, without adding every term individually?

**Learner choices.** Choose targets, grouping schemes, and an opponent's proposed upper bound.

**Hour menu.** 0–10 assemble early payments; 10–15 compare the two rules; 15–35 search for bounds and blocks; 35–40 reset; 40–55 prove one general claim or estimate a target-crossing index; 55–60 distinguish experiment from guarantee.

**Explore.**

- Could a million tiny payments still contribute a substantial amount?
- What feature gives the geometric machine an exact remaining debt?

**Hint ladder.**

1. Group harmonic terms by doubling the final denominator.
2. Replace every term in a block by its smallest term to get a lower bound.

**Checked instance.** Prove that the first 16 harmonic terms exceed 3, without computing their exact sum.

**Reasoning.** Separate 1; then blocks {1/2}, {1/3,1/4}, {1/5,…,1/8}, and {1/9,…,1/16}. Each block after the initial 1 contributes at least 1/2, so the sum is at least 3. The second block contributes strictly more than 1/2, hence the total exceeds 3. Continuing gives H_(2^k)≥1+k/2, exceeding any fixed target for sufficiently large k. In contrast the geometric sum through 1/2^k is 2−1/2^k, always below 2.

**Boundary.** Both sequences of payments tend to zero. That necessary condition for series convergence therefore cannot decide which total converges.

**Extensions.**

- Give a guaranteed, deliberately loose index that exceeds 10: k=19 and N=2^19 suffice.
- Average the partial sums of 1−1+1−…; explain why their limit 1/2 is a summability convention rather than ordinary convergence.

**Satisfying stop.** A grouping argument that defeats every proposed finite harmonic bound.

**Prior use.** Year-1 figurate and fraction work may support entry; exact prior use of infinite series is unrecorded. GA-03 uses a geometric cover for a different question.

**Sources.**

- [Jiří Lebl, Basic Analysis I](https://www.jirka.org/ra/realanal.pdf), §§2.5–2.6, geometric and harmonic series. Inspection: Relevant series statements inspected; block proof supplied.

<a id="ga-13"></a>
## GA-13 - Fit a curve inside the narrowest error band

Primary field: 41. Related: 49. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a few unavoidable errors certify the best approximation everywhere on an interval?

**Anchor.** For f(x)=x² on [−1,1], the unique affine function minimizing maximum absolute error is p(x)=1/2, with error 1/2. Three alternating extreme errors certify the optimum; the card supplies a direct proof.

**Bridge (exact-special-case).** Moving a line and its uniform-width error band is precisely a best-uniform approximation problem. Limits: Measured fit suggests a candidate; endpoint and center inequalities establish optimality over all affine competitors, not just sampled lines.

**Prerequisite gates.**

- **Entry:** O/V: compare a line's vertical discrepancy from a supplied parabola.
- **Explore:** F/A: use y=ax+b and absolute errors at three x-values.
- **Explain:** P: combine inequalities to force a lower bound and verify attainment.
- **Prove:** A/P: direct proof suffices here; general equioscillation requires approximation theory.
- **Reading:** Short graph labels; symbolic proof can follow an oral search.
- **Arithmetic:** Halves, signed values, linear equations.
- **Reasoning:** Distinguish vertical error from perpendicular distance and worst error from average error.
- **Hard Stop:** Calculus is not needed for this instance; least-squares extensions require a new objective and possibly integration.

**Materials and preparation (10 minutes).** Graph of x² on [−1,1], transparent movable lines, and an adjustable vertical-width band.

**Launch.** Choose any straight line and try to keep its vertical error from the parabola as small as possible at every x. Tilting is allowed. Can your opponent prove you cannot beat their band width?

**Learner choices.** Choose slope and intercept, diagnostic points, and a proposed certificate of optimality.

**Hour menu.** 0–10 experiment with lines; 10–15 define maximum vertical error; 15–35 optimize and challenge candidates; 35–40 reset; 40–55 build a three-point proof or change the objective; 55–60 report the best value and its certificate.

**Explore.**

- Why might a tilted line help one endpoint but hurt the other?
- Which three locations are enough to force a lower bound?

**Hint ladder.**

1. Inspect x=−1,0,1.
2. Average the two endpoint residuals before comparing with the center.

**Checked instance.** Prove that no affine line beats the constant 1/2.

**Reasoning.** Suppose p=ax+b has error at most E. At zero, |b|≤E. At the endpoints, |1−b−a|≤E and |1−b+a|≤E, implying |1−b|≤E by averaging. Thus 1≤|b|+|1−b|≤2E, so E≥1/2. The constant 1/2 attains this bound because 0≤x²≤1. Equality forces b=1/2; endpoint inequalities then force a=0, proving uniqueness.

**Boundary.** Passing through more selected points need not improve worst error between them. Also a least-squares best constant for x² on this interval is 1/3, so a different error criterion gives a different answer.

**Extensions.**

- Repeat on [0,1]: p=x−1/8 has maximum error 1/8, certified at 0,1/2,1; verify by completing the square.
- Let students choose a continuous polygonal target and derive the best constant from its maximum and minimum.

**Satisfying stop.** A complete lower bound plus an attaining line, not just the prettiest fit.

**Prior use.** New approximation family; related to optimization in Week 1 but the domain is a continuous interval.

**Sources.**

- [NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/3.11), §3.11(i), minimax approximation and alternating extrema. Inspection: Relevant criterion inspected; affine example proved independently.

<a id="ga-14"></a>
## GA-14 - Two different motions with the same snapshots

Primary field: 42. Related: 65. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What information is lost by sampling, and why can exact agreement at every recorded time still conceal different signals?

**Anchor.** The signals f(t)=sin(2πt) and g(t)=sin(10πt) agree at t=n/4 for every integer n, since their angles differ by 2πn. They differ between those sample times.

**Bridge (exact-special-case).** Rotating arrows represent continuous sinusoidal signals; sampling is an exact restriction of those functions to specified times. Limits: This does not prove a general sampling theorem, and four values never determine an unrestricted continuous function.

**Prerequisite gates.**

- **Entry:** O/V: compare arrow heights at regularly spaced snapshots.
- **Explore:** F: quarter-turn timing and integer extra rotations.
- **Explain:** A/P: use trigonometric periodicity to prove equality at all sample times.
- **Prove:** X: band-limited reconstruction requires Fourier analysis and precise hypotheses.
- **Reading:** Short time labels; formulas optional until explanation.
- **Arithmetic:** Integer turns, quarters, and optional exact sine values.
- **Reasoning:** Separate actual motion from its sampled record and allow multiple compatible explanations.
- **Hard Stop:** Do not promise reconstruction without an explicit frequency restriction.

**Materials and preparation (8 minutes).** Two clock-face arrows, four snapshot cards, and a strip of equally spaced time marks.

**Launch.** One arrow completes one turn per second; another completes five. Photograph their heights four times per second. Can you tell which motion produced the photographs? Choose one extra photograph that would help.

**Learner choices.** Choose starting phases, sample schedules, alternative speeds, and a diagnostic extra time.

**Hour menu.** 0–10 compare free rotations; 10–15 fix sample times and equal initial phase; 15–35 build identical records from different motions; 35–40 movement reset; 40–55 prove the ambiguity or redesign sampling; 55–60 share both explanations of one record.

**Explore.**

- How many extra complete turns occur between photographs?
- Would photographing only the height lose more information than recording the whole arrow?

**Hint ladder.**

1. Compare angles modulo one full turn at each sampling time.
2. Look halfway between two adjacent sample times.

**Checked instance.** List samples at t=0,1/4,1/2,3/4, and distinguish the signals at t=1/8.

**Reasoning.** Both sample lists are 0,1,0,−1. More generally, 10π(n/4)−2π(n/4)=2πn, so equality persists for every integer snapshot index. At t=1/8, f=sin(π/4)=√2/2 and g=sin(5π/4)=−√2/2, so one extra height observation separates these two candidates. A physical device adds measurement uncertainty; the mathematical result uses exact times.

**Boundary.** That extra sample only distinguishes the two proposed signals. It does not determine the correct signal among every continuous function; infinitely many can fit any finite record.

**Extensions.**

- Find all integer frequencies giving the same samples as frequency one at rate four.
- Record both horizontal and vertical coordinates, then compare the remaining ambiguity with height-only sampling.

**Satisfying stop.** Two different exact motions that produce the same entire regular snapshot record.

**Prior use.** Week 4 periodicity is a prerequisite comparison; the new question concerns information lost by observing continuous motion discretely.

**Sources.**

- [Daniel Stroock, Topics in Fourier Analysis](https://ocw.mit.edu/courses/res-18-015-topics-in-fourier-analysis-spring-2024/mitres_18_015_s24_full_lec.pdf), §§1–2, periodic exponentials and Fourier representation. Inspection: Periodic-frequency framework inspected; aliasing example checked directly.

<a id="ga-15"></a>
## GA-15 - Four brightnesses, four hidden patterns

Primary field: 43. Related: 15, 42. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why do a group's symmetries supply the right coordinates for decomposing a pattern?

**Anchor.** On G=(Z/2Z)², the four character patterns (1,1,1,1), (1,1,−1,−1), (1,−1,1,−1), and (1,−1,−1,1) are mutually orthogonal. Coefficients of any real four-entry pattern are one quarter of its dot products with these patterns.

**Bridge (exact-special-case).** A two-by-two brightness array is a function on an actual finite group, and the sign cards are its characters. Limits: The finite transform is exact but does not establish Haar integration or harmonic analysis on infinite groups.

**Prerequisite gates.**

- **Entry:** C/F: add brightness values and signed contributions; halves may occur.
- **Explore:** L: treat four-entry lists as vectors and use dot products.
- **Explain:** P: verify orthogonality and reconstruct the original pattern.
- **Prove:** L/X: group characters for the general finite-abelian theorem.
- **Reading:** Four short pattern cards; negative contributions should be explained orally.
- **Arithmetic:** Signed addition, multiplication, and division by four.
- **Reasoning:** Keep one ordering: 00,01,10,11; negative coefficients are corrections, not negative physical light.
- **Hard Stop:** Stop before nonabelian or continuous transforms without representation theory or integration.

**Materials and preparation (10 minutes).** Four sign-pattern cards, counters for positive brightness, red counters for negative corrections, and a two-by-two grid.

**Launch.** Make a four-square brightness picture. Rebuild it using only scaled copies of these four sign patterns. Can a partner recover your hidden coefficients? Then swap the two columns and predict which coefficients change sign.

**Learner choices.** Choose target arrays, coefficients, reconstruction order, and a translation of the square labels.

**Hour menu.** 0–10 combine sign patterns freely; 10–15 fix coordinates and scaling; 15–35 encode and decode pictures; 35–40 reset; 40–55 predict column swaps or justify the formula; 55–60 share a reconstructed pattern.

**Explore.**

- Why does each nonconstant sign card have average zero?
- What happens when two different sign cards are multiplied entry by entry and summed?

**Hint ladder.**

1. Add all four brightnesses to find the constant contribution.
2. A sign card cancels every other sign card under a dot product.

**Checked instance.** Decompose (4,2,0,2) in the displayed basis.

**Reasoning.** The dot products are 8,4,0,4, so the coefficients are 2,1,0,1. Reconstruction gives (2,2,2,2)+(1,1,−1,−1)+(1,−1,−1,1)=(4,2,0,2). Each basis vector has squared length four, and distinct ones have dot product zero, explaining the division by four. Swapping columns translates by 01; it changes the signs of the third and fourth coefficients, giving (2,4,2,0).

**Boundary.** Brightness data need not give nonnegative coefficients. Requiring only positive pattern weights would forbid many valid reconstructions and change the mathematical problem.

**Extensions.**

- Construct an array requiring four nonzero coefficients.
- Use three binary coordinates to build eight Walsh patterns; explain why the signs multiply according to parity.

**Satisfying stop.** Encode and decode one picture, then predict a symmetry without recomputing everything.

**Prior use.** Week 2 used binary toggles; this uses real brightness, orthogonal decomposition, and translation. The object and question are different.

**Sources.**

- [Rohan Dandavati, The Fourier Transform on Finite Groups: Theory and Computation](https://math.uchicago.edu/~may/REU2018/REUPapers/Dandavati.pdf), §3, Theorems 3.5–3.8. Inspection: Finite-character basis argument inspected; four-entry arithmetic checked directly.

<a id="ga-16"></a>
## GA-16 - Slide two windows and predict their overlap graph

Primary field: 44. Related: 26, 42. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does convolution turn two shapes into a third, and how can geometry reveal the formula before integration?

**Anchor.** For interval indicators f=1_[0,2] and g=1_[0,1], (f*g)(t) is the length of [0,2]∩[t−1,t]. It rises linearly, has a plateau, and falls linearly.

**Bridge (exact-special-case).** Sliding a reflected-and-shifted interval computes the actual continuum convolution integral of two indicator functions. Limits: A sampled overlap table is only partial evidence; interval endpoints give the exact piecewise formula. This is not merely finite multiplication.

**Prerequisite gates.**

- **Entry:** O: slide strips and compare overlap lengths.
- **Explore:** F/V: read positions, lengths, and a graph against displacement.
- **Explain:** A/P: locate each change in the endpoint formula and explain every interval.
- **Prove:** I: integrate indicator products, or accept length as their integral.
- **Reading:** Minimal reading; endpoint labels 0,1,2,3.
- **Arithmetic:** Subtraction of lengths and optional halves.
- **Reasoning:** The moving interval is [t−1,t], so its right endpoint, not its center, is t.
- **Hard Stop:** General convolution and Laplace identities require integrability and convergence conditions.

**Materials and preparation (8 minutes).** One fixed strip of length two, one transparent strip of length one, ruler, and blank t-versus-overlap axes.

**Launch.** Slide the short window [t−1,t] across the long window [0,2]. Before tracing the answer, predict its entire overlap-length graph. Choose lengths that make the graph a triangle, a trapezoid, or something else.

**Learner choices.** Choose strip lengths, direction, observation points, and a claimed graph to challenge.

**Hour menu.** 0–10 play with sliding overlaps; 10–15 define t precisely; 15–35 draw and justify graphs; 35–40 reset; 40–55 reverse roles or stack two-window operations; 55–60 explain a corner or plateau.

**Explore.**

- At what t does overlap begin and end?
- Why does unequal window length create a flat top?

**Hint ladder.**

1. The overlap starts at the larger left endpoint.
2. The overlap ends at the smaller right endpoint; subtract only when the result is positive.

**Checked instance.** Find the full convolution of the length-two and length-one indicators.

**Reasoning.** The overlap length is max(0,min(2,t)−max(0,t−1)). Therefore it is zero for t≤0, t for 0≤t≤1, one for 1≤t≤2, 3−t for 2≤t≤3, and zero for t≥3. At t=1/2,3/2,5/2 the values are 1/2,1,1/2. These cases cover every real displacement, so they prove the whole graph. Single endpoints have zero length and do not change the values.

**Boundary.** Simply sliding [t,t+1] instead changes the parameter and shifts the graph. Forgetting the reflection/shift convention can produce a correct-looking but incorrectly positioned convolution.

**Extensions.**

- For lengths a≥b>0, derive a plateau of height b and support [0,a+b].
- Integrate the overlap graph: its area is two, the product of the original interval lengths; then ask why this extends to nonnegative integrable functions.

**Satisfying stop.** A complete overlap graph justified by endpoint cases.

**Prior use.** No current-week equivalent; connects continuous geometry to transforms with inexpensive reusable materials.

**Sources.**

- [Stephen Boyd, EE102 Lecture 3: The Laplace Transform](https://web.stanford.edu/class/ee102k/laplace.pdf), Slides 3–27 through 3–29, convolution and its transform. Inspection: Convolution definition inspected; overlap integral derived directly.

<a id="ga-17"></a>
## GA-17 - An equation that listens to its own average

Primary field: 45. Related: 47. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** When does feedback through an integral produce one solution, no solution, or infinitely many?

**Anchor.** On [0,1], solve u(x)=f(x)+λm where m=∫_0^1u(t)dt. Integrating gives (1−λ)m=∫f. This rank-one integral equation is exactly reducible to one scalar compatibility condition.

**Bridge (exact-special-case).** The unknown is an actual function and its continuum mean is part of its defining equation. Limits: The simple kernel is a genuine special case; it does not prove the Fredholm alternative for arbitrary compact operators.

**Prerequisite gates.**

- **Entry:** A/I: functions, definite integrals, and the mean over a unit interval.
- **Explore:** A: introduce m as an unknown number and solve a linear equation.
- **Explain:** P/I: integrate both sides, then substitute the resulting function back.
- **Prove:** L/X: compact operators for general Fredholm theory.
- **Reading:** Symbolic text; graphs support the meaning of an average.
- **Arithmetic:** Fractions and linear equations; ∫_0^1x dx=1/2.
- **Reasoning:** Separate necessary compatibility from sufficient construction; verify both.
- **Hard Stop:** A finite-group averaging puzzle is an analogy unless the integral formulation is actually used.

**Materials and preparation (5 minutes).** Graph paper and cards selecting f(x)=x or x−1/2 and λ=0,1/2,1,2.

**Launch.** Choose f and λ. Find a graph whose height is f(x) plus λ times its own average height. Can turning the feedback dial destroy all solutions, or create infinitely many?

**Learner choices.** Choose feedback values and forcing functions; predict the number of solutions before calculating.

**Hour menu.** 0–10 compare means of simple lines; 10–15 state the feedback equation; 15–35 solve selected pairs; 35–40 reset; 40–55 investigate λ=1 and compatibility; 55–60 explain one transition in the number of solutions.

**Explore.**

- What equation must the unknown mean satisfy?
- If the mean equation works, how do you recover the whole graph?

**Hint ladder.**

1. Name the mean m before trying to solve for every u(x).
2. At λ=1, inspect the mean of f rather than dividing by zero.

**Checked instance.** Solve first f=x, λ=1/2, then compare λ=1 for f=x and f=x−1/2.

**Reasoning.** For λ=1/2, m=1/2+m/2 gives m=1 and u=x+1/2; its integral is indeed one. With f=x and λ=1, integration demands 0=1/2, so no solution exists. With f=x−1/2 and λ=1, the forcing has zero mean. Every u=x−1/2+C has mean C and satisfies the equation; conversely every solution must have this form, giving exactly a one-parameter family.

**Boundary.** The singular dial value does not always mean no solution. It means the forcing must satisfy a compatibility condition; when it does, uniqueness fails.

**Extensions.**

- Choose f=x² and compute the compatibility using its mean 1/3.
- Replace the constant kernel by x·t, so the unknown moment is ∫t u(t)dt; derive another scalar condition.

**Satisfying stop.** Three fully verified examples showing unique, absent, and infinitely many solutions.

**Prior use.** New calculus-level family; graph averaging in GA-05 introduces a related mechanism but has different unknowns and solvability conditions.

**Sources.**

- [Michael O'Neil, Integral Equations and Fast Algorithms](https://cims.nyu.edu/~oneil/courses/fa17-math2011/int_eq_notes_2017.pdf), Fredholm Alternative, Theorem 3, printed p.54. Inspection: Theorem statement inspected; rank-one examples solved independently.

<a id="ga-18"></a>
## GA-18 - Which constant best represents a whole landscape?

Primary field: 46. Related: 41, 49. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does a choice of distance between functions change the meaning of best approximation?

**Anchor.** For f=0 on [0,3/4) and f=4 on [3/4,1], its squared L² distance to constant c is (3/4)c²+(1/4)(4−c)²=(c−1)²+3. Thus c=1 uniquely minimizes this distance.

**Bridge (exact-special-case).** A step-function space with weighted squared distance is an exact finite-dimensional subspace of L²[0,1]; constant approximation is orthogonal projection. Limits: This example does not prove infinite-dimensional projection existence, completeness, or general Banach-space behavior.

**Prerequisite gates.**

- **Entry:** F/V: compare the widths and heights of two rectangular pieces.
- **Explore:** A: square discrepancies and combine weighted costs.
- **Explain:** P/A: complete the square to prove global optimality.
- **Prove:** I/X: interpret the cost as an L² integral and extend to Hilbert spaces.
- **Reading:** Short labels and a cost rule; a recorder can handle algebra.
- **Arithmetic:** Quarters, squares, signed differences.
- **Reasoning:** Keep width weights: a small high region must not count equally with a wide low region.
- **Hard Stop:** General function-space conclusions require norms, integrals, and completeness.

**Materials and preparation (8 minutes).** A unit-width profile with height zero over three quarters and height four over one quarter; movable horizontal line.

**Launch.** Replace this two-level landscape by one flat height. Each part charges its width times the square of its vertical error. Choose a replacement that costs least. Then change the rule to charge only the largest error.

**Learner choices.** Choose candidate heights, compare cost rules, and redesign the widths to favor a different answer.

**Hour menu.** 0–10 inspect and approximate the landscape; 10–15 define the weighted squared cost; 15–35 optimize by trials and algebra; 35–40 reset; 40–55 compare maximum error or derive a general weighted mean; 55–60 state which definition of best was used.

**Explore.**

- Why should the wide low region matter more?
- Can the same constant win under two different error rules?

**Hint ladder.**

1. Write the two rectangular contributions separately.
2. Expand the total and try to complete one square.

**Checked instance.** Find the squared-error best constant and the maximum-error best constant.

**Reasoning.** The squared-error cost is c²−2c+4=(c−1)²+3, so c=1 uniquely gives the minimum three. Under maximum error, the cost is max(|c|,|4−c|), at least two by the triangle inequality 4≤|c|+|4−c|. Height c=2 attains two and is the unique minimizer. Thus different legitimate distances select different flat representatives.

**Boundary.** Using the unweighted average of the two displayed heights gives two, which ignores their unequal widths and fails for squared error. Requiring exact equality to the profile has no constant solution.

**Extensions.**

- For heights a,b occupying proportions p and 1−p, derive c=pa+(1−p)b.
- Explain orthogonality: the residual f−1 has integral zero, so its inner product with every constant vanishes.

**Satisfying stop.** An optimal constant with a completed-square certificate and a second optimum under another distance.

**Prior use.** GA-13 minimizes uniform error for a parabola; this changes both the space and the error geometry rather than repeating the same fit.

**Sources.**

- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/MIRA.pdf), §8B, orthogonal projection; 8.34 and 8.43. Inspection: Projection definitions and characterization inspected; step-function calculation supplied.

<a id="ga-19"></a>
## GA-19 - A tiny graph with a large derivative

Primary field: 47. Related: 26, 65. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Can a transformation amplify arbitrarily small input errors, and why does the chosen norm matter?

**Anchor.** Differentiation D:C¹[0,1]→C[0,1] is unbounded when both spaces use the supremum norm. The polynomials f_n(x)=x^n/n have norm 1/n while Df_n=x^(n−1) has norm one.

**Bridge (exact-special-case).** The input objects are actual functions and differentiation is a linear operator; supremum discrepancy measures their size. Limits: This establishes one unbounded operator between specified normed spaces, not a general theorem about spectra or numerical differentiation.

**Prerequisite gates.**

- **Entry:** A/D: polynomial functions and the power rule.
- **Explore:** V: compare graphs on one fixed scale and inspect endpoint slopes.
- **Explain:** P: use a parameter n to defeat any proposed amplification bound.
- **Prove:** P/L: definition of a bounded linear operator.
- **Reading:** Symbolic formulas; graph explanations can precede notation.
- **Arithmetic:** Powers, reciprocals, and inequalities.
- **Reasoning:** Do not change the graph scale secretly; separate visual height from derivative height.
- **Hard Stop:** Without derivatives, observations remain motivation. Infinite-dimensional spectral theory is a separate hard stop.

**Materials and preparation (5 minutes).** Graph paper with a fixed vertical scale, polynomial cards n=1,2,5,10, and optional plotting software.

**Launch.** Design a function that stays extremely close to zero but whose derivative is at least one somewhere. Your opponent proposes a universal multiplier C between graph size and derivative size. Can your function break that promise?

**Learner choices.** Choose n, an error budget, and a claimed bound; test alternative function families.

**Hour menu.** 0–10 compare low-degree graphs; 10–15 define both supremum sizes; 15–35 challenge bounds using polynomials; 35–40 reset; 40–55 prove unboundedness or change the norm; 55–60 state exactly what failed.

**Explore.**

- Where is x^n largest on [0,1]?
- What happens if we measure the derivative as part of input size?

**Hint ladder.**

1. Divide x^n by n.
2. Choose n larger than the opponent's proposed constant.

**Checked instance.** Find a polynomial with maximum height at most 1/100 and derivative equal to one at x=1.

**Reasoning.** Take f(x)=x^100/100. For 0≤x≤1, its height is between zero and 1/100. Its derivative is x^99, equaling one at x=1. More generally ||Df_n||∞/||f_n||∞=n, so for any fixed C choose an integer n>C and the inequality ||Df||∞≤C||f||∞ fails. The sequence f_n tends uniformly to zero while its derivatives do not tend uniformly to zero.

**Boundary.** With input norm ||f||∞+||f'||∞, differentiation has bound one by definition. The operator did not change; the topology used to judge small input changed.

**Extensions.**

- Compare f_n=x^n with f_n=x^n/n and explain why only the second tends uniformly to zero.
- Explore finite differences on a noisy table, clearly separating an error-amplification model from a proved algorithmic bound.

**Satisfying stop.** One exact tiny-input witness and a parameter argument defeating every fixed bound.

**Prior use.** New operator-theory family. GA-18 compares norms for optimization; here the question is continuity of a transformation.

**Sources.**

- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/MIRA.pdf), Chapter 10, bounded linear maps and operator norms. Inspection: Definitions inspected; unbounded-differentiation witness supplied.

<a id="ga-20"></a>
## GA-20 - Save quadratic effort with a steady journey

Primary field: 49. Related: 26. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why can local changes to a whole trajectory prove that one motion minimizes a functional?

**Anchor.** Among continuous piecewise-C¹ paths y:[0,1]→R with y(0)=0 and y(1)=1, the cost E=∫_0^1(y′)²dt is at least one, with equality only for y(t)=t. Use a finite partition into C¹ pieces and expand ∫(y′−1)²=E−1; values of the derivative at joins do not affect the integral.

**Bridge (exact-special-case).** A chosen time-position curve is the actual competitor in a variational problem; its velocity determines the defined cost. Limits: Quadratic effort is a mathematical objective, not a claim about human metabolic energy. This proof uses more than merely stationarity.

**Prerequisite gates.**

- **Entry:** F/V: compare journeys using constant speeds on two equal time intervals.
- **Explore:** A: square speeds and calculate weighted cost.
- **Explain:** P/A: prove the two-speed optimum by completing a square.
- **Prove:** D/I/P: the general continuous piecewise-C¹ path proof applies the fundamental theorem of calculus on each piece and adds.
- **Reading:** Short schedule labels initially; symbolic integral extension.
- **Arithmetic:** Halves, signed speeds, and squares.
- **Reasoning:** Distinguish fixed duration, endpoint displacement, and total traveled distance; reversing is allowed.
- **Hard Stop:** The universal result for continuous piecewise-C¹ paths needs calculus; checking finitely many schedules alone does not prove it.

**Materials and preparation (8 minutes).** A unit time-position diagram, two half-time cards, speed cards, and optional string curves.

**Launch.** Reach position one from zero in one time unit. Each time segment charges its duration times speed squared. Choose your speeds and see whether rushing early and resting later can cost less than moving steadily.

**Learner choices.** Choose two-speed schedules, permit backward motion, and invent smooth challengers.

**Hour menu.** 0–10 act or draw varied journeys; 10–15 define the artificial cost; 15–35 optimize two-speed schedules; 35–40 reset; 40–55 prove the smooth theorem or design another objective; 55–60 share an optimality certificate.

**Explore.**

- If the first-half speed rises, what must the second-half speed do?
- Why is finding a stationary trajectory insufficient by itself?

**Hint ladder.**

1. Write the two speeds as 1+a and 1−a.
2. Subtract the constant speed one and square the difference.

**Checked instance.** Optimize two half-time speeds and then verify y=t+a t(1−t).

**Reasoning.** The endpoint condition forces speeds 1+a and 1−a. Their cost is [(1+a)²+(1−a)²]/2=1+a², minimized only at a=0. The resulting journeys are continuous piecewise-C¹ competitors. For the smooth family y=t+a t(1−t), derivative is 1+a(1−2t); integrating its square gives 1+a²/3. For every permitted path, apply the fundamental theorem on each piece to get ∫y′=1. Thus E=1+∫(y′−1)²≥1. Equality makes the continuous squared integrand zero on each piece, so the derivative is one there. Continuity at joins and y(0)=0 then give y=t throughout.

**Boundary.** Minimizing total distance ∫|y'| gives many minimizers: every nondecreasing path with these endpoints has distance one. Uniqueness depends on the squared-speed objective.

**Extensions.**

- Use three unequal time intervals and derive a weighted variance identity.
- Change endpoints to a,b over duration T>0: the minimum is (b−a)²/T, attained by constant speed.

**Satisfying stop.** A complete best-two-speed argument; calculus-ready learners may finish the global proof.

**Prior use.** Week 1 optimized discrete packing; this optimizes a continuous function. It is new even though both use lower-bound-plus-construction reasoning.

**Sources.**

- [UCL MATH0043, Calculus of Variations](https://www.homepages.ucl.ac.uk/~ucahmto/latex_html/pandoc_chapter2.html), §2, functional viewpoint and Euler–Lagrange setup. Inspection: Functional setup inspected; global squared-cost proof supplied independently.

<a id="ga-21"></a>
## GA-21 - The shortest route that touches a mirror

Primary field: 51. Related: 49. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a geometric transformation turn a constrained broken path into an unconstrained straight one?

**Anchor.** For A and B in the same open half-plane of a mirror line, reflecting B to B' makes |AM|+|MB|=|AM|+|MB'|. The straight crossing gives the minimum whenever it lies in the allowed mirror segment.

**Bridge (exact-special-case).** A chosen contact point determines a real Euclidean broken path; unfolding preserves its length. Limits: The minimum for an infinite mirror need not be legal for a finite mirror. Physical light behavior is motivation, not needed for the proof.

**Prerequisite gates.**

- **Entry:** O/V: move a contact point and compare string lengths.
- **Explore:** V/F: reflect a point and use equal triangles.
- **Explain:** P: apply the triangle inequality to every possible contact point.
- **Prove:** A: optional coordinate solution; calculus only for certain constrained extensions.
- **Reading:** Oral launch; coordinate labels for exact computation.
- **Arithmetic:** None for geometric proof; fractions and square roots for exact length.
- **Reasoning:** Track the reflected endpoint while preserving original path lengths.
- **Hard Stop:** Multiple obstacles or curved mirrors require new arguments; do not reuse the straight-mirror theorem blindly.

**Materials and preparation (10 minutes).** Paper with A=(1,2), B=(5,4), mirror y=0 from x=0 to 4; ruler, string, and tracing paper.

**Launch.** Travel from A to B while touching the marked mirror segment exactly once at M. Choose M to make the total route shortest. Your partner may challenge your choice with any other point on the segment.

**Learner choices.** Choose and adjust M, use measurement or reflection, and shorten the mirror to test the solution.

**Hour menu.** 0–10 compare candidate string routes; 10–15 fix legal contact points; 15–35 discover reflection; 35–40 reset; 40–55 produce a universal proof or change the segment; 55–60 explain a certificate.

**Explore.**

- What stays equal when B is reflected?
- Could the best infinite-mirror route miss the permitted segment?

**Hint ladder.**

1. Draw B' below the mirror at the same perpendicular distance as B.
2. A bent path from A to B' cannot beat their straight-line distance.

**Checked instance.** Find the optimal M on the specified segment and its exact route length.

**Reasoning.** B'=(5,−4). The segment from A to B' has parametrization (1+4t,2−6t), meeting y=0 at t=1/3 and M=(7/3,0), which lies in [0,4]. Its length is √(4²+6²)=2√13. Every legal route unfolds to A→M→B' and has length at least |AB'| by the triangle inequality. The exhibited crossing attains the bound, so it is globally optimal.

**Boundary.** If the allowed mirror ends at x=2, M=7/3 is illegal. The previous lower bound still holds, but its equality construction is unavailable; a new constrained optimization is required.

**Extensions.**

- Vary A and B and express M as a weighted average of their horizontal coordinates using their heights.
- For the shortened mirror, calculus or convexity proves the minimum occurs at x=2; the route then has length √5+5.

**Satisfying stop.** A shortest route certified without testing every mirror point.

**Prior use.** Week 9 used billiard unfolding and periodicity; this adds a continuous optimization and a finite-mirror obstruction. Avoid reusing the earlier trajectory instance.

**Sources.**

- [Anton Petrunin, Euclidean Plane and Its Relatives](https://arxiv.org/pdf/1302.1630), §5D–F, reflection and distance; triangle-inequality framework. Inspection: Reflection facts inspected; constrained instance derived directly.

<a id="ga-22"></a>
## GA-22 - Split four pegs so their hulls meet

Primary field: 52. Related: 15. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What tiny configuration forces an intersection between two independently chosen convex hulls?

**Anchor.** Any four points in R² can be partitioned into two nonempty groups whose convex hulls intersect. The core uses distinct points and analyzes convex quadrilaterals, a point inside a triangle, and collinear degeneracy.

**Bridge (exact-special-case).** Peg subsets and stretched outlines are literal convex hulls; choosing a partition asks the exact planar Radon question. Limits: Rubber bands show an idealized hull approximately. Four pegs do not prove the higher-dimensional theorem by experiment.

**Prerequisite gates.**

- **Entry:** O: sort four pegs into two colors and draw segments or triangular hulls.
- **Explore:** V: recognize inside a triangle versus four convex corners.
- **Explain:** P: explain the complete geometric case split, including collinearity.
- **Prove:** L/P: linear dependence gives the general R^d theorem.
- **Reading:** Oral; a partner may trace boundaries.
- **Arithmetic:** None for the first cases; fractions for a coordinate certificate.
- **Reasoning:** A hull of one point is that point; hulls include their boundaries.
- **Hard Stop:** Do not assume every four-point arrangement is a convex quadrilateral.

**Materials and preparation (8 minutes).** Four movable pegs or dots, two colors, thread, and a transparent grid.

**Launch.** Choose four distinct positions. Color each red or blue, using both colors, so the red convex hull and blue convex hull share a point. Challenge another group with an arrangement that seems hard.

**Learner choices.** Choose positions, partition, intersection witness, and a case missed by a proposed universal explanation.

**Hour menu.** 0–10 make and discuss hulls; 10–15 establish the intersection task; 15–35 challenge arrangements; 35–40 reset; 40–55 organize a proof or try three points; 55–60 explain one difficult case.

**Explore.**

- What if one peg is inside the triangle of the others?
- Can three corners of a triangle always be split successfully?

**Hint ladder.**

1. For four convex corners, try opposite corners together.
2. A one-peg hull is allowed.

**Checked instance.** Use (0,0),(4,0),(0,4),(1,1). Find a partition and certify the intersection.

**Reasoning.** Put (1,1) alone and the other three together. Since (1,1)=1/2(0,0)+1/4(4,0)+1/4(0,4), with nonnegative coefficients totaling one, it lies in the triangular hull. More generally, if one point lies in or on the triangle of the other three, put it alone. This includes three collinear points plus one off their line: choose the middle collinear point alone. Otherwise four distinct noncollinear points form a convex quadrilateral, whose diagonal segments intersect, giving two pairs. If all four are collinear, choose an inner point alone; it lies between the extreme points in the other group. These cases cover every arrangement of four distinct points.

**Boundary.** For three noncollinear points, every nonempty partition is one vertex versus the opposite edge, and those hulls are disjoint. The number four is therefore necessary in the plane.

**Extensions.**

- Choose five points in three dimensions and seek a partition using a tetrahedron and an interior point.
- Translate intersection witnesses into two convex combinations and relate them to affine dependence.

**Satisfying stop.** A successful partition for an adversarial arrangement and a proof that handles its geometric type.

**Prior use.** Week 1 tilings are different convex/discrete geometry. No identical existing task was found.

**Sources.**

- [Daniel Hug and Wolfgang Weil, A Course on Convex Geometry](https://users.fmf.uni-lj.si/lavric/hug%26weil.pdf), §1.2, Theorem 1.2.1, Radon's theorem. Inspection: Statement and proof framework inspected; planar cases supplied.

<a id="ga-23"></a>
## GA-23 - Return home with your arrow pointing somewhere new

Primary field: 53. Related: 58. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can locally straight transport around a curved surface retain a record of the route?

**Anchor.** On the unit sphere, parallel transport along a great-circle arc keeps the angle to its forward tangent constant. Around the positively oriented octant triangle A=(1,0,0), B=(0,1,0), C=(0,0,1), the transported tangent arrow rotates by π/2.

**Bridge (exact-special-case).** A tangent arrow follows an explicitly defined connection along actual spherical great-circle arcs. Limits: A hand-held arrow is approximate. General holonomy/curvature theorems need differential geometry; an arbitrary 'keep pointing north' rule is different transport.

**Prerequisite gates.**

- **Entry:** O/V: follow three great-circle arcs and keep a chosen angle to forward travel.
- **Explore:** V: identify tangent directions along equator and meridians.
- **Explain:** P/V: track exact coordinate directions leg by leg.
- **Prove:** D/X: parallel transport equations and general Gauss–Bonnet.
- **Reading:** Oral route with labeled landmarks; coordinates optional.
- **Arithmetic:** Right angles; no length calculations in the octant proof.
- **Reasoning:** Separate the sphere's tangent plane from surrounding three-dimensional space.
- **Hard Stop:** Do not infer transport from compass direction alone; the legal rule must be demonstrated.

**Materials and preparation (15 minutes).** A ball marked with equator, north pole, and two meridians 90° apart; a tangent arrow and route diagram. Mark A,B,C and use different colors for the forward tangent and transported arrow. Keep the arrow fixed at each corner before starting the next arc.

**Launch.** Start at A with your arrow pointing toward B. Follow the shortest arc A→B→C→A. Along each leg keep the arrow's angle to the forward tangent unchanged. When you return, compare with the original arrow without resetting it at the corners.

**Learner choices.** Choose an initial tangent direction, reverse the route, or compare a retraced route; predict before carrying the arrow.

**Hour menu.** 0–10 explore tangent directions on the ball; 10–15 demonstrate transport on one arc; 15–35 complete and record routes; 35–40 reset; 40–55 verify exact vectors or relate angle excess; 55–60 share the route-dependent result.

**Explore.**

- Can an arrow remain tangent while staying fixed in ordinary space?
- Why is retracing an arc different from completing a triangle?

**Hint ladder.**

1. On the equator, track the arrow that points along travel.
2. On B→C the x-direction stays tangent and perpendicular to travel.

**Checked instance.** Transport initial vector +y from A around the specified octant.

**Reasoning.** Along A→B, the forward tangent rotates from +y to −x, so the arrow reaches B as −x. Along B→C the vector −x is constant, tangent to the sphere, and perpendicular to the great-circle plane, hence parallel. At C it is opposite the forward tangent +x for C→A. Keeping that opposite relation makes the ending arrow +z at A. Thus +y has become +z, a +90° rotation in A's tangent plane. The octant area is 4π/8=π/2, matching spherical holonomy.

**Boundary.** Walking out and exactly retracing the same arc restores the arrow. Curvature does not make every closed itinerary produce nonzero rotation.

**Extensions.**

- Reverse the triangle and predict −90°.
- Use a different longitude separation α with two meridians and an equator arc; the spherical lune argument predicts transport angle α.

**Satisfying stop.** One precisely described route and a verified changed arrow.

**Prior use.** New curved-geometry strand; plane billiards from Week 9 cannot exhibit this transport effect.

**Sources.**

- [Anton Petrunin and Sergio Zamora Barrera, What Is Differential Geometry?](https://arxiv.org/pdf/2012.11814), Chapters 16–17; Proposition 17.10 and octant transport example in semisolutions. Inspection: Relevant transport and spherical-area discussion inspected; vector tracking supplied.

<a id="ga-24"></a>
## GA-24 - Can a loop be reshaped into a segment?

Primary field: 54. Related: 55. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What property survives every homeomorphism even when lengths and angles are discarded?

**Anchor.** Deleting a point from a circle leaves a connected space, while deleting an interior point from a closed interval disconnects it. A homeomorphism restricts to a homeomorphism of the corresponding punctured spaces.

**Bridge (exact-special-case).** Idealized strings represent a circle and interval as topological spaces, and deleting a point tests an invariant. Limits: Physical cutting removes a short length; the proof concerns deleting one mathematical point. No general classification of topological spaces is claimed.

**Prerequisite gates.**

- **Entry:** O: trace a loop and segment and compare pieces after a marked cut.
- **Explore:** P: reason about all possible images of an interior point.
- **Explain:** P: formulate the puncture contradiction using preservation of connectedness.
- **Prove:** X: definitions of homeomorphism and connectedness for a formal proof.
- **Reading:** Oral launch with pictures.
- **Arithmetic:** None; counting one or two components.
- **Reasoning:** Separate allowable continuous reversible deformation from cutting, gluing, or identifying points.
- **Hard Stop:** A drawing with crossings needs explicit decisions about which strands are joined.

**Materials and preparation (5 minutes).** One closed string loop and one open string segment, paper diagrams, and removable dot markers.

**Launch.** Can you continuously reshape a loop into a segment without cutting, gluing, or making different points become the same point? Invent a test that every successful reshaping would have to pass.

**Learner choices.** Choose where to puncture each shape, propose candidate reshaping rules, and challenge a test using endpoints.

**Hour menu.** 0–10 freely bend strings; 10–15 specify reversible no-identification moves; 15–35 invent invariants; 35–40 reset; 40–55 explain the puncture test or compare another pair; 55–60 state an impossibility with its legal-move assumptions.

**Explore.**

- Does an endpoint behave like a middle point?
- If a map is reversible, can two different string points merge?

**Hint ladder.**

1. Mark a point in the interior of the segment.
2. Its corresponding point on a loop would have to behave the same after deletion.

**Checked instance.** Prove that [0,1] is not homeomorphic to the unit circle.

**Reasoning.** Suppose a homeomorphism existed. Take the point 1/2 in the interval and its image p on the circle. Removing them preserves the homeomorphism. But [0,1] without 1/2 separates into two nonempty relatively open pieces [0,1/2) and (1/2,1]. A circle without p is connected: rotating p to (1,0), the remaining circle is the continuous image of the interval 0<t<2π under t↦(cos t,sin t). This contradicts preservation of connectedness.

**Boundary.** Deleting an endpoint of [0,1] leaves it connected, so one careless cut does not distinguish the spaces. The argument deliberately chooses an interior point and uses the circle's every-point property.

**Extensions.**

- Compare a Y-shaped graph with a segment by deleting the branch point; three components appear.
- Investigate a figure-eight, specifying that its crossing is one joined point, and compare it with two disjoint circles.

**Satisfying stop.** A complete impossibility argument that does not rely on visual resemblance.

**Prior use.** Week 1 reconfiguration involved legal moves on discrete states; this introduces reversible continuous maps of spaces.

**Sources.**

- [Romyar Sharifi, Point-Set Topology](https://www.math.ucla.edu/~sharifi/notes/topology-ch03.html), §3.1, connectedness and Proposition 3.1.8. Inspection: Continuous-image principle inspected; puncture argument supplied.

<a id="ga-25"></a>
## GA-25 - How many corridors must close to erase every loop?

Primary field: 55. Related: 05. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why does a connected graph have an invariant number of independent cycles even when it has many visible loop routes?

**Anchor.** For a finite connected graph with V vertices and E edges, every spanning tree has V−1 edges. Therefore exactly E−V+1 edges must be removed to leave a connected graph with no cycles.

**Bridge (exact-special-case).** Rooms and corridors form the actual one-dimensional cell complex; deleting selected edges asks for its cycle rank. Limits: This computes a graph invariant, not higher-dimensional homology. Crossing corridors are joined only when a vertex is explicitly marked.

**Prerequisite gates.**

- **Entry:** O/C: trace routes and count rooms and corridors.
- **Explore:** P: delete a cycle edge without disconnecting the graph.
- **Explain:** P: combine a termination algorithm with the tree-edge count.
- **Prove:** X: fundamental groups or homology for the algebraic interpretation.
- **Reading:** Oral; vertex labels help record chosen deletions.
- **Arithmetic:** Counting and E−V+1.
- **Reasoning:** Distinguish a cycle from a backtracking walk and preserve all vertices.
- **Hard Stop:** Cycle rank does not count every simple cycle; avoid calling both quantities 'number of loops'.

**Materials and preparation (8 minutes).** Four room dots A,B,C,D in a square, corridors AB,BC,CD,DA,AC, and removable edge strips.

**Launch.** Close as few corridors as possible so every room remains reachable but no cycle survives. Choose your closures. Can a partner prove that using fewer closures could never work?

**Learner choices.** Choose the spanning tree, a deletion algorithm, and a graph that seems to have more cycles than the formula predicts.

**Hour menu.** 0–10 explore routes and cycles; 10–15 define connected and cycle-free; 15–35 optimize closures; 35–40 reset; 40–55 prove the edge count or change the graph; 55–60 share two different optimal closure sets.

**Explore.**

- Can removing an edge on a cycle disconnect the graph?
- Why are the two small triangles and the outside square not three independent cycles?

**Hint ladder.**

1. Keep deleting one cycle edge until no cycle remains.
2. A tree can be built by attaching one new vertex with one new edge.

**Checked instance.** Solve the four-room square with diagonal AC.

**Reasoning.** Here V=4 and E=5, so two deletions are required. Delete DA and AC, leaving the path A−B−C−D. One deletion would leave four edges on four vertices; a connected acyclic graph on four vertices has only three edges, so one cannot suffice. To prove the general procedure, an edge on a cycle has an alternate route around that cycle, so deleting it preserves connectivity. Repetition ends at a spanning tree. Removing a leaf inductively proves every finite tree has V−1 edges.

**Boundary.** The original graph has three simple cycles: ABC, ACD, and the outer square. Its independent cycle count is only two; listing cycles and finding a cycle basis are different questions.

**Extensions.**

- Allow several connected components: the cycle rank becomes E−V+c, where c is the component count.
- Fill one triangle with a two-dimensional face; ask why its boundary loop is now contractible, introducing a new dimension.

**Satisfying stop.** A minimal closure plan and an explanation of why all optimal plans remove the same number.

**Prior use.** Week 10 studied Euler/postman routes. This asks about spanning trees and independent cycles, not traversing all corridors.

**Sources.**

- [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Chapter 0, graphs and homotopy type; §1.1 fundamental group of graphs. Inspection: Graph discussion inspected; elementary spanning-tree proof supplied.

<a id="ga-26"></a>
## GA-26 - Can a coloring prove a knot cannot untie?

Primary field: 57. Related: 20, 55. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a local diagram rule provide a global obstruction to deformation?

**Anchor.** Fox 3-coloring assigns residues 0,1,2 to diagram arcs so that 2·over=under1+under2 mod 3 at each crossing. Equivalently, all three colors agree or all differ. Reidemeister moves preserve colorings bijectively.

**Bridge (exact-special-case).** Arcs and crossings are those of genuine knot diagrams; allowed Reidemeister moves preserve the embedded-knot type. Limits: The invariant can prove two knots different but matching colorability does not prove sameness. Diagrams need unambiguous over/under data.

**Prerequisite gates.**

- **Entry:** O/C: follow an arc through crossings and use three colors.
- **Explore:** P: check local color completion under moves; modular arithmetic is optional.
- **Explain:** P: distinguish a nonconstant coloring from the single-arc unknot.
- **Prove:** M/P: the formula supplies a compact proof of all three move identities.
- **Reading:** Oral rule; short crossing labels.
- **Arithmetic:** None for coloring; remainders modulo three for the algebraic extension.
- **Reasoning:** An arc stops at undercrossings, not at every crossing; tracing deserves time.
- **Hard Stop:** General knot equivalence requires Reidemeister's theorem; do not present local checks alone as its proof.

**Materials and preparation (15 minutes).** A clearly drawn standard trefoil with three arcs labeled A,B,C, an unknot, three pencils, and local move sketches. Mark an explicit overpass at every crossing and stop each arc only at undercrossings. Future student sheets need independently checked trefoil and local-move drawings.

**Launch.** Color the trefoil's arcs so each crossing has either one color or three, and use more than one color overall. Can the same kind of coloring survive every legal diagram move? Could the knot then become a plain circle?

**Learner choices.** Choose colorings, local moves to test, and a proposed invariant-breaking move.

**Hour menu.** 0–10 trace knot arcs and manipulate a closed cord; 10–15 learn the crossing rule; 15–35 color and test moves; 35–40 reset; 40–55 explain the obstruction or check algebraic identities; 55–60 separate proof from failed untying attempts.

**Explore.**

- Why must a nonconstant coloring be required?
- What changes if a strand is allowed to pass through another?

**Hint ladder.**

1. Give the trefoil arcs three different colors.
2. For a crossing with overcolor b and incoming undercolor a, the outgoing undercolor must be 2b−a modulo three.

**Checked instance.** Color the standard three-crossing trefoil and explain why the unknot is excluded.

**Reasoning.** Assign A=0,B=1,C=2. At every crossing the three colors are distinct, satisfying 2b=a+c modulo three. The unknot has only one arc, so every coloring is constant. For move invariance define a*b=2b−a: a*a=a, (a*b)*b=a, and (a*b)*c=(a*c)*(b*c), since both sides are a−2b+2c. These are the type I, II, and III local color-completion identities. The induced bijections preserve constant colorings and hence nonconstant ones. Together with Reidemeister's theorem this obstructs unknotting.

**Boundary.** Every diagram admits constant colorings, so allowing those alone proves nothing. Changing a crossing is not a Reidemeister move and can alter knot type.

**Extensions.**

- Count all trefoil colorings: choose two arc colors freely and the third is forced, giving nine total and six nonconstant.
- Find a nontrivial knot with no nonconstant 3-coloring; treat an example as a new sourced investigation rather than assuming the test is complete.

**Satisfying stop.** A nonconstant trefoil coloring and one checked local reason it survives legal moves.

**Prior use.** New knot-theory content; Week 2 parity invariants offer a reasoning comparison but not the same object or obstruction.

**Sources.**

- [Louis Kauffman, Knots](https://homepages.math.uic.edu/~kauffman/Tots/Knots), Three Colored Trefoil, Figures 12–14 and theorem. Inspection: Coloring rule and move-invariance argument inspected.

<a id="ga-27"></a>
## GA-27 - What happens when a lake rises through a saddle?

Primary field: 58. Related: 53, 54. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a local critical point change the topology of an entire sublevel set?

**Anchor.** The quadratic f(x,y)=x²−y² has a nondegenerate critical point of index one at the origin. Within [−1,1]², its sublevel sets at c=−1/4,0,1/4 exhibit two components, a point connection, and a connected region.

**Bridge (exact-special-case).** Flooding means the precise inequality f≤c, and the quadratic is the actual local Morse saddle model. Limits: A clay landscape is a representation. The square has corners, so we do not apply the compact smooth-manifold slab theorem to its boundary.

**Prerequisite gates.**

- **Entry:** V/A: plot inequalities or test coordinates in a supplied contour map.
- **Explore:** A: rewrite the inequality and use symmetry.
- **Explain:** P: prove disconnectedness by the sign of y and connectedness by explicit paths.
- **Prove:** D/L/X: gradient, Hessian signature, and Morse theory for the general theorem.
- **Reading:** Coordinate labels; oral flooded/not-flooded decisions before symbolic proof.
- **Arithmetic:** Squares and signed quarters.
- **Reasoning:** Track connected regions rather than just the number of contour curves.
- **Hard Stop:** A sampled height map cannot certify that no hidden critical point exists.

**Materials and preparation (12 minutes).** Graph paper showing [−1,1]², transparent shaded sublevels, and optional clay saddle for comparison.

**Launch.** Raise the water level c. A point floods exactly when x²−y²≤c. Choose test points and sketch the flooded regions at −1/4,0,1/4. At which height can the upper and lower lakes first meet?

**Learner choices.** Choose test points, routes through flooded ground, and candidate levels where the topology changes.

**Hour menu.** 0–10 explore a saddle or its contours; 10–15 define sublevel flooding; 15–35 map the three levels; 35–40 reset; 40–55 prove the connection change or classify derivatives; 55–60 report one topological event.

**Explore.**

- Can a flooded path cross y=0 when c is negative?
- What makes radial travel toward the origin safe when c≥0?

**Hint ladder.**

1. At y=0, f=x² cannot be negative.
2. Use f(tx,ty)=t²f(x,y) for 0≤t≤1.

**Checked instance.** Explain the component change for the three stated levels.

**Reasoning.** For c=−1/4, every flooded point satisfies y²≥x²+1/4, so y cannot be zero. The upper and lower regions are separated. Each is connected: move vertically toward y=1 or y=−1, which only decreases f, then travel along that boundary within |x|≤√3/2. At c=0 the two wedges |y|≥|x| meet at the origin. For c=1/4, every flooded point can connect radially to the origin because multiplying f by t² keeps it ≤1/4, so the set is connected. Gradient (2x,−2y) vanishes only at zero; Hessian diag(2,−2) has one negative direction.

**Boundary.** A function such as x⁴−y⁴ has a similar-looking drawing but a degenerate Hessian at zero. The Morse lemma cannot be invoked just from visual resemblance.

**Extensions.**

- Compare a bowl x²+y², where a component is born as c crosses zero.
- Build a piecewise-linear landscape and track component mergers, labeling it a different model before connecting it to persistence.

**Satisfying stop.** An exact reason the two regions cannot join below zero and do join at zero.

**Prior use.** New global-analysis entry; no prior week studies critical points or sublevel topology.

**Sources.**

- [Patrick Gillespie, Morse Theory Notes](https://web.math.utk.edu/~afreire/teaching/m663f21/Morse_Theory_Notes.pdf), Lemma 1.12; Theorem 2.9; §3 passing critical levels. Inspection: Relevant local normal form and topology-change statements inspected; square-domain instance proved directly.

<a id="ga-28"></a>
## GA-28 - A bracket or a tangent: which promise survives?

Primary field: 26. Related: 65, 37. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a root-finding method certify an answer, and why can a fast local method fail?

**Anchor.** For continuous f on [a,b] with opposite endpoint signs, bisection preserves a root-containing interval and halves its width each step. Newton iteration has no corresponding unconditional convergence guarantee; for f(x)=x³−2x+2 it cycles 0→1→0.

**Bridge (exact-special-case).** Learners execute genuine algorithms on real continuous functions, with a maintained existence certificate. Limits: A graph that appears to cross an axis supplies intuition; the sign condition plus continuity supplies the mathematical existence argument.

**Prerequisite gates.**

- **Entry:** F: halve rational intervals and compare squares.
- **Explore:** A: evaluate polynomial signs; D is required only for Newton slopes.
- **Explain:** P: explain why the selected half still contains some root.
- **Prove:** P/A: inductive interval bound using the intermediate value theorem; D for the Newton counterexample.
- **Reading:** Short numeric records; a facilitator may read procedural instructions.
- **Arithmetic:** Fractions and squares; cubic values and signed division in the extension.
- **Reasoning:** Keep an invariant rather than merely collecting plausible decimal digits.
- **Hard Stop:** Do not introduce tangent iteration without derivatives, or claim continuity from a finite plot.

**Materials and preparation (8 minutes).** Number lines, blank bracket records, fraction cards, optional calculator and graphing tool.

**Launch.** Find a number whose square is two, using questions that answer only “too large” or “too small.” Decide what information to keep after every question.

**Learner choices.** Choose test points, compare equal-halving with other choices, and set a target interval width before computing.

**Hour menu.** 0–10 guess and square; 10–15 agree on a certificate; 15–35 maintain brackets; 35–40 reset; 40–55 investigate the Newton cycle if derivative-ready, otherwise prove the halving bound; 55–60 compare promises.

**Explore.**

- Can a good-looking guess lack a proved error bound?
- Does an endpoint sign change prove a root if the function jumps?

**Hint ladder.**

1. Keep both a lower and an upper witness.
2. For the Newton example, calculate the next value from zero and then from one.

**Checked instance.** Start with [1,2] for x²−2 and perform four bisections. Compare with Newton on x³−2x+2 from zero.

**Reasoning.** The tested midpoints are 3/2,5/4,11/8,23/16; their square-minus-two signs are +,−,−,+. The remaining interval is [11/8,23/16], width 1/16. Its midpoint 45/32 is within 1/32 of √2. Generally the width after n bisections is 2^−n. For the cubic, Newton gives x−(x³−2x+2)/(3x²−2): at zero it gives one, and at one it gives zero. Both derivative denominators are nonzero, yet iteration never reaches a root.

**Boundary.** The discontinuous function equal to −1 for x<0 and +1 for x≥0 changes sign across [−1,1] without any zero. Continuity is essential to the bracket certificate.

**Extensions.**

- Bracket a root of the cubic on [−2,−1] and compare its reliable progress with the cycle.
- Design a hybrid that accepts a Newton step only when it preserves a maintained bracket; specify fallback rules.

**Satisfying stop.** A root-containing interval of chosen width and an explanation of why it is trustworthy.

**Prior use.** Comparison and extension of AP-06: the Newton cubic x³−2x+2 and its 0↔1 cycle are deliberate cross-volume reuse. Here the main additional work is a bisection invariant and explicit error certificate. GA-02 supplies the underlying continuity principle.

**Sources.**

- [MIT 2.086, Numerical Computation for Mechanical Engineers, Unit VI](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-spring-2013/60af88c658ba3e83cdf7c43289aeb5b4_MIT2_086S13_Unit6_Textbook.pdf), §29, bisection discussion and §29.2.5 Newton pathologies, printed pp.432–435. Inspection: Both methods and their differing guarantees inspected; chosen arithmetic verified independently.

<a id="ga-29"></a>
## GA-29 - Remove almost all the length; keep uncountably many points

Primary field: 28. Related: 03, 40. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a set have zero length and still contain more points than any list?

**Anchor.** The middle-thirds Cantor set C is the intersection of its closed construction stages. Stage n has 2^n intervals of length 3^−n, so outer measure(C)=0. Infinite addresses using ternary digits 0 and 2 give an injection from all binary sequences into C.

**Bridge (exact-special-case).** Finite stages supply actual covers of the limiting set; nested interval addresses specify actual real points. Limits: A finite paper model always retains positive total length and cannot display all points or prove an infinite statement by itself.

**Prerequisite gates.**

- **Entry:** O/C: cut or shade the open middle third repeatedly, keeping endpoints.
- **Explore:** F: compute interval counts, lengths, and a shrinking total budget.
- **Explain:** P: distinguish number of pieces, length, and number of points.
- **Prove:** P/F: use geometric limits and diagonalization; no derivatives are needed.
- **Reading:** Facilitator can narrate the cut rule; address strings must be tracked accurately.
- **Arithmetic:** Powers of two and three, fractions, and a geometric sum.
- **Reasoning:** Coordinate a nested construction with two different quantifiers: every length budget and every proposed list.
- **Hard Stop:** Uncountability needs an infinite-sequence argument. “Too many dots to count” is only an observation.

**Materials and preparation (10 minutes).** Long paper strips, three-color pencils, interval templates, and 0/2 address cards.

**Launch.** Repeatedly remove the open middle third of every surviving interval. Before cutting, predict which endpoints survive and whether all the length can disappear while points remain.

**Learner choices.** Choose addresses for surviving points, invent a proposed list of addresses, and challenge another group to find an omitted address.

**Hour menu.** 0–10 explore cutting; 10–15 state endpoint and nesting rules; 15–35 compute covers and encode locations; 35–40 reset; 40–55 compare length with listing and diagonalize; 55–60 share separate certificates.

**Explore.**

- Why does zero total length not mean the empty set?
- Where does the argument use infinitely many stages?

**Hint ladder.**

1. At stage n multiply the number of intervals by their individual length.
2. Against a list of infinite addresses, change the nth digit of the nth address.

**Checked instance.** Compute the stage-four cover, locate 1/4 in C, and explain why no list exhausts C.

**Reasoning.** Stage four has 16 closed intervals of length 1/81, total 16/81. At stage n the cover total is (2/3)^n, below every positive budget for sufficiently large n; hence outer measure is zero. If using open covers, enlarge the finitely many stage-n closed intervals slightly, adding arbitrarily little total length. The repeating ternary address 0.020202… has value (2/9)/(1−1/9)=1/4 and avoids every deleted middle third. Every infinite 0/2 address determines a point by nested intervals. Two such addresses differing first at digit k give values separated by at least 1/3^k, so they cannot coincide. If all such addresses were listed, changing the diagonal digits produces another address missing from the list.

**Boundary.** After any finite number of stages the retained length is positive. Endpoints such as 1/3 survive because the removed middle thirds are open; using closed deletions changes the construction.

**Extensions.**

- Find surviving rational points from repeating 0/2 addresses.
- Compare GA-03: countable sets have zero outer measure, but the converse fails by this example.

**Satisfying stop.** A small-length cover and an independently explained missed-address argument.

**Prior use.** New measure/cardinality synthesis. Paper cutting resembles earlier hands-on work, but the infinite limiting object and two distinct proofs are new.

**Sources.**

- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/MIRA.pdf), §2D, Cantor set construction and results 2.76–2.79. Inspection: Construction, zero outer measure, and uncountability inspected; stage counts and chosen address checked.

<a id="ga-30"></a>
## GA-30 - Two shortest routes around a cylinder

Primary field: 53. Related: 55, 51. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does a surface’s global topology affect shortest paths even when its local geometry is flat?

**Anchor.** On the lateral surface of a circular cylinder of circumference six and height four, A and B lie on opposite generators at opposite rims. Unrolling lifts B to (3+6k,4), k∈Z, from A=(0,0). Straight segments give candidates of length √((3+6k)²+16); the minimum is five, attained twice.

**Bridge (exact-special-case).** Paper unrolling preserves intrinsic lengths on the actual cylinder surface, giving a continuous geometric proof. Limits: Routes must stay on the lateral surface. Travel through the solid cylinder or across end caps is a different optimization problem.

**Prerequisite gates.**

- **Entry:** O: trace alternative routes around a rolled paper surface.
- **Explore:** V: unroll and compare straight segments to translated copies.
- **Explain:** P/V: explain why every winding choice has a straight lower bound.
- **Prove:** A/P: minimize over integer lifts with the distance formula.
- **Reading:** Labels and short diagrams suffice; no calculus reading.
- **Arithmetic:** Squares, square roots, integer multiples, and comparison of absolute values.
- **Reasoning:** Separate local straightness from being globally shortest.
- **Hard Stop:** The informal paper argument proves this developable case; arbitrary curved-surface geodesics need further differential geometry.

**Materials and preparation (10 minutes).** A 6-by-4 rectangle, tape, ruler, string, and a tiled strip of three or more copied rectangles.

**Launch.** Join the short edges into a cylinder. Connect a bottom-rim point to the top point halfway around. Find two visibly different routes and decide whether one can be shortened.

**Learner choices.** Choose a cut line, a winding direction, and extra windings; use another cut if a promising path crosses the first seam.

**Hour menu.** 0–10 explore string routes; 10–15 fix the surface-only rule; 15–35 unroll and measure; 35–40 reset; 40–55 compare lifted routes and prove the minimum; 55–60 show two equal winners.

**Explore.**

- Why might one unrolled rectangle hide a shortest route?
- Can a locally straight route lose to another route with different winding?

**Hint ladder.**

1. Repeat the rectangle sideways before drawing.
2. A path ending at B can lift to any copy of B, but its endpoint height is always four.

**Checked instance.** Use circumference six, height four, and a half-circumference displacement. Find all shortest routes.

**Reasoning.** In the unrolled strip, B has copies (3+6k,4). A path with that lift has length at least the straight segment distance √((3+6k)²+16). Each straight segment lies between heights zero and four and rolls to an allowed path, so the bound is attained for each winding choice. The smallest possible |3+6k| is three, attained only at k=0 and k=−1. Both routes therefore have length √25=5. The next candidates have horizontal displacement nine and length √97>5.

**Boundary.** A straight line to a distant lift is locally a geodesic but is not globally shortest. A chord through the cylinder’s interior does not compete under the stated rules.

**Extensions.**

- Move B to horizontal offset two; show that the unique shortest lift has displacement two.
- Vary the offset continuously and locate exactly where two shortest routes exchange priority.

**Satisfying stop.** Two constructions of length five and a lower-bound argument excluding every shorter surface route.

**Prior use.** New continuous geometry. GA-23 studies curvature on a sphere; this cylinder is locally flat while its global wrapping still matters.

**Sources.**

- [Anton Petrunin and Sergio Zamora Barrera, What Is Differential Geometry?](https://arxiv.org/pdf/2012.11814), Chapters 14–15 on length and shortest paths; §18G cylinder as a length-preserving image of a plane domain. Inspection: Unrolling/length-preserving cylinder model inspected; lift minimization checked independently.

<a id="ga-31"></a>
## GA-31 - Everybody agrees in pairs: is there a common choice?

Primary field: 52. Related: 54, 90. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** When can small groups of convex constraints certify simultaneous feasibility?

**Anchor.** For a finite family of nonempty closed bounded intervals, pairwise intersection implies a common point. In R² pairwise intersection of convex sets is insufficient; finite Helly requires every triple to intersect, for families with at least three members.

**Bridge (exact-special-case).** Interval choices are actual one-dimensional convex sets, and their shared feasibility is exactly the dimension-one Helly theorem. Limits: The planar triple theorem is a further theorem. Pairwise classroom trials do not prove it, and arbitrary nonconvex sets need not obey the interval result.

**Prerequisite gates.**

- **Entry:** O/C: overlap strips representing allowed locations on a common line.
- **Explore:** V: draw intervals or clipped half-planes on a coordinate grid.
- **Explain:** P: identify the latest left endpoint and earliest right endpoint.
- **Prove:** P: complete the finite interval proof and construct a planar counterexample.
- **Reading:** Read short endpoint labels; symbols for inequalities are needed only in the planar extension.
- **Arithmetic:** Ordering integers; signed coordinates for the counterexample.
- **Reasoning:** Distinguish one common witness from a different witness for every pair.
- **Hard Stop:** A general proof of planar Helly needs additional convexity reasoning, such as Radon; do not present the interval proof as that proof.

**Materials and preparation (10 minutes).** Transparent strips on a number line, endpoint clips, grid paper, and optional three translucent half-plane sheets.

**Launch.** Each person marks an allowed interval for a meeting location. Every pair can agree somewhere. Can the entire group agree? Try hard to produce a failure before making a rule.

**Learner choices.** Choose interval endpoints, choose which pairs to test, then change the space from a line to a plane or remove the no-gaps rule.

**Hour menu.** 0–10 free overlap play; 10–15 state the pairwise condition; 15–35 search and prove on a line; 35–40 reset; 40–55 build planar or nonconvex failures; 55–60 identify the hypothesis doing the work.

**Explore.**

- Why is checking that every interval overlaps one favorite interval insufficient?
- What changes when allowed regions have holes or live in a plane?

**Hint ladder.**

1. Which interval starts furthest right? Which ends furthest left?
2. In the plane try three constraints that each prohibit a different direction.

**Checked instance.** Find the common part of [0,4],[2,6],[3,5],[1,7]. Then give three planar convex sets intersecting pairwise but not all together.

**Reasoning.** The largest left endpoint is three and the smallest right endpoint is four, so the common interval is [3,4]. In general, let L be the largest left endpoint and U the smallest right endpoint. The two intervals attaining them intersect by hypothesis, forcing L≤U; every interval contains [L,U]. For the plane use A={x≥0}, B={y≥0}, C={x+y≤−1}. Pair witnesses are (0,0) for A,B; (0,−1) for A,C; and (−1,0) for B,C. A common point would have x+y≥0 and ≤−1, impossible. Intersect each set with [−2,2]² if bounded physical windows are preferred.

**Boundary.** The nonconvex sets {0,1},{1,2},{0,2} intersect pairwise but have empty triple intersection even on a line. Convexity, not merely dimension, matters.

**Extensions.**

- Use GA-22 Radon partitions to investigate a proof of planar Helly.
- Design a three-window puzzle where pair witnesses misleadingly suggest global agreement.

**Satisfying stop.** A complete interval proof and a counterexample showing precisely why its scope matters.

**Prior use.** New convex-feasibility family. GA-22 supplies a possible later proof tool; no prior worksheet is assumed.

**Sources.**

- [Daniel Hug and Wolfgang Weil, A Course on Convex Geometry](https://users.fmf.uni-lj.si/lavric/hug%26weil.pdf), §1.2, Theorems 1.2.1–1.2.3 on Radon and Helly. Inspection: Finite-dimensional convex intersection statements inspected; interval proof and planar counterexample checked independently.

<a id="ga-32"></a>
## GA-32 - Cut a Möbius band and follow the seam

Primary field: 57. Related: 54. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can gluing rules determine connectedness, boundary, and orientability before a surface is physically built?

**Anchor.** Compare the annulus quotient (0,s)~(1,s) with the Möbius quotient (0,s)~(1,−s) of [0,1]×[−1,1]. The Möbius band has one boundary component. Cutting along s=0 produces one annulus; the corresponding annulus cut produces two annuli.

**Bridge (exact-special-case).** Paper represents these exact quotient surfaces. Tracking glued edges proves connectedness beyond the empirical surprise of one cut. Limits: The embedding in three-dimensional space may be twisted or linked. This activity classifies the resulting surfaces, not their knotting or a numerical twist count.

**Prerequisite gates.**

- **Entry:** O: trace an edge and make a prediction before cutting.
- **Explore:** C: label upper/lower halves and follow paired seam labels.
- **Explain:** P: explain why crosswise gluing connects the two halves.
- **Prove:** P: use the quotient diagram to prove boundary counts and the cut surface type.
- **Reading:** Colored arrows can replace written labels; oral reasoning is sufficient at entry.
- **Arithmetic:** Counting one or two circuits; no algebra is required for the physical proof.
- **Reasoning:** Distinguish a connected strip from the number of boundary loops and from orientability.
- **Hard Stop:** General surface classification is beyond a single band. A dramatic cutting demonstration alone is not a classification proof.

**Materials and preparation (12 minutes).** Long paper strips, tape, two marker colors, scissors or precut strips, and large matching seam diagrams.

**Launch.** Build one band with matching ends and one with a half-turn. Trace an edge all the way back to your start. Predict what will happen if each band is cut exactly along its middle.

**Learner choices.** Choose tracking colors, draw a prediction diagram, and decide which observations would distinguish one component from two.

**Hour menu.** 0–10 handle and trace both bands; 10–15 record predictions; 15–35 cut and follow seams; 35–40 reset; 40–55 rebuild the explanation on flat diagrams; 55–60 present a proof another group can check without cutting.

**Explore.**

- Does one connected object necessarily have one boundary loop?
- Which part of the seam rule changes the result of the center cut?

**Hint ladder.**

1. Name the upper half U and lower half L before attaching the seam.
2. After a half-turn, the end of U attaches to L. Follow one more seam crossing.

**Checked instance.** Predict boundary loops and connected pieces before and after a center cut, using the two seam rules.

**Reasoning.** In the annulus, the top edge returns to the top and the bottom to the bottom, giving two boundary loops. Cutting the center leaves U glued to U and L to L, so there are two separate annuli. In the Möbius band, following the top edge crosses to the bottom and only then returns, giving one boundary loop. After the center cut, U joins L and L joins U: the two rectangular pieces form one cyclic strip. Traversing both pieces reverses the transverse coordinate twice, so the combined strip has matching ends and is an annulus. It is connected but has two boundary loops.

**Boundary.** Do not infer “two pieces” from two visible edges after cutting. Connected components and boundary components count different objects; the cut Möbius example separates them.

**Extensions.**

- Replace the half-turn by several half-turns and predict seam behavior from parity, keeping knotting questions separate.
- Draw the center circle and explain why flattening a band onto it forgets boundary and orientability information.

**Satisfying stop.** A seam diagram that correctly predicts the outcome of the cut and distinguishes two kinds of counting.

**Prior use.** New surface investigation. Week 5 used geometric transformations; here identification of whole edges creates a space rather than moving a planar figure.

**Sources.**

- [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Chapter 0, opening deformation-retraction examples, printed p.2; Möbius band and core circle. Inspection: Core-circle surface model inspected; boundary and cutting conclusions derived independently by the explicit seam tracking below.

<a id="ga-33"></a>
## GA-33 - The transform must remember how the system started

Primary field: 44. Related: 34, 93. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does an integral transform convert a differential equation into algebra without losing initial data?

**Anchor.** For the one-sided Laplace transform Y(s)=∫_0^∞e^−st y(t)dt, integration by parts gives L(y′)=sY−y(0) under convergence and vanishing-boundary hypotheses. Applied to y′+y=1, the initial value selects y(t)=1+(y(0)−1)e^−t.

**Bridge (exact-special-case).** The transformed equation and recovered continuous trajectory solve exactly the same initial-value problem. Limits: This is a calculus-gated activity. The algebraic table game alone does not establish the transform identity or convergence.

**Prerequisite gates.**

- **Entry:** D/A: read a rate equation and compare initial slopes.
- **Explore:** I/A: use the definition, integration by parts, and a short transform table.
- **Explain:** P/D: substitute the recovered trajectory into the original equation and initial condition.
- **Prove:** I/P: justify the derivative rule, including the boundary term at infinity.
- **Reading:** Symbolic mathematical reading; a shared table reduces memory demand.
- **Arithmetic:** Partial fractions and exponential algebra.
- **Reasoning:** Track the same initial datum through time-domain and transformed descriptions.
- **Hard Stop:** Stop before this family unless derivatives and improper integrals are meaningful; forcing an elementary version would lose the central mechanism.

**Materials and preparation (8 minutes).** Graph paper or plotting tool, a table with transforms of 1,e^−t,t e^−t, and equation cards with different initial values.

**Launch.** A system moves toward level one according to y′=1−y. Predict its behavior when it starts empty and when it starts at level two. Can an algebraic shortcut preserve that difference?

**Learner choices.** Choose starting levels, sketch predictions, and choose a constant or fading input before calculating.

**Hour menu.** 0–10 sketch initial slopes and qualitative paths; 10–15 establish the transform definition; 15–35 solve and compare initial conditions; 35–40 reset; 40–55 investigate a fading input and verify by differentiation; 55–60 explain the indispensable boundary term.

**Explore.**

- Where exactly is the starting value stored in the transformed equation?
- Can two solutions have the same forcing but different trajectories?

**Hint ladder.**

1. Keep −y(0) attached to the transformed derivative.
2. After inversion, check both the differential equation and the initial value.

**Checked instance.** Solve y′+y=1 first with y(0)=0, then with y(0)=2; finally change the forcing to e^−t and start at zero.

**Reasoning.** For the constant forcing and initial value a, sY−a+Y=1/s, so Y=1/[s(s+1)]+a/(s+1). Inversion gives y=1−e^−t+a e^−t. Thus the first two trajectories are 1−e^−t and 1+e^−t: both approach one, from opposite sides. For forcing e^−t and zero initial value, (s+1)Y=1/(s+1), hence Y=1/(s+1)² and y=t e^−t. Differentiating gives y′=(1−t)e^−t, so y′+y=e^−t and y(0)=0. These transforms converge for real s>0.

**Boundary.** Omitting −y(0) incorrectly assigns the zero-start trajectory to every initial condition. A transform expression without its domain of convergence is also incomplete.

**Extensions.**

- Find when t e^−t reaches its maximum, and relate that time to input versus decay.
- Replace the decay coefficient one by k>0 and determine the steady level for constant input.

**Satisfying stop.** Two correctly distinguished initial-value solutions and one direct time-domain verification.

**Prior use.** New transform family. GA-16 develops convolution geometrically; this offers a later route to transformed differential equations and system response.

**Sources.**

- [Stephen Boyd, EE102 Laplace Transform](https://web.stanford.edu/class/ee102k/laplace.pdf), Slides 3–19 and 3–20, differentiation and initial-condition example; transform table. Inspection: Derivative transform and role of initial conditions inspected; selected equations and inverses verified directly.

<a id="ga-34"></a>
## GA-34 - A well-behaved rate law can still explode

Primary field: 34. Related: 26. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why does local existence and uniqueness not guarantee that a trajectory exists for all future time?

**Anchor.** For y′=y² with y(0)=a>0, y(t)=a/(1−at) is the unique solution on its maximal forward interval 0≤t<1/a and diverges as t approaches 1/a. The polynomial rate law is locally Lipschitz, so this is finite-time blow-up without a local uniqueness failure.

**Bridge (exact-special-case).** The algebraic trajectory is an exact solution of a genuinely continuous differential equation; finite doubling times reveal its limiting behavior. Limits: A step-by-step numerical table can suggest growth, but cannot establish either finite-time divergence or the exact differential law.

**Prerequisite gates.**

- **Entry:** A/F: compare values of a supplied rational trajectory and mark doubling times.
- **Explore:** D/A: interpret the rate equation and differentiate the proposed solution.
- **Explain:** P: explain why an infinite value cannot be inserted as a real-valued continuation.
- **Prove:** D/P: verify the solution and use local uniqueness to establish its maximal interval.
- **Reading:** Symbolic fractions and rate notation; discussion can precede formal theorem reading.
- **Arithmetic:** Rational expressions, signed values, and geometric time intervals.
- **Reasoning:** Separate uniqueness, boundedness, and duration of existence.
- **Hard Stop:** Without derivatives, stop at the exact rational-function investigation; identifying it as the solution of the rate equation requires calculus.

**Materials and preparation (8 minutes).** Time-number lines, value cards, graph paper or plotting software, and optional slope-field images.

**Launch.** A quantity grows at a rate equal to its square. Starting at one, could it double over and over before time one? Predict the times before looking at the candidate formula.

**Learner choices.** Choose positive, zero, or negative starting values; choose target heights and compare their arrival times.

**Hour menu.** 0–10 predict growth and inspect candidate curves; 10–15 define the rate equation; 15–35 verify and find doubling times; 35–40 reset; 40–55 vary initial values and discuss continuation; 55–60 distinguish the three existence questions.

**Explore.**

- Does a finite rate at every finite y prevent the solution from escaping to infinity?
- Why can a formula valid beyond a vertical asymptote fail to continue the original trajectory?

**Hint ladder.**

1. Differentiate a/(1−at) before trying to solve the equation from scratch.
2. For a=1, solve 1/(1−t)=2^n for the arrival time.

**Checked instance.** Verify the solution for a=1, calculate repeated doubling times, and compare a=1/2,0,−1.

**Reasoning.** Differentiating y=a/(1−at) gives y′=a²/(1−at)²=y², with y(0)=a. For a=1, height 2^n is reached at t=1−2^−n, so all finite doublings occur before one. The solution tends to +∞ as t→1 from below and cannot extend continuously as a real-valued solution through that time. For a=1/2 the blow-up time is two. For a=0 the solution is constantly zero. For a=−1 it is −1/(1+t), defined for all t≥0 and approaching zero from below.

**Boundary.** The expression 1/(1−t) also satisfies the equation on t>1, but that disconnected branch does not pass through the initial point and is not a continuation across t=1. Local uniqueness remains valid.

**Extensions.**

- Compare y′=y, whose exponential solution grows without finite-time blow-up.
- For y′=y^p with positive initial data and p>1, investigate how the blow-up time depends on p.

**Satisfying stop.** A directly verified solution, an exact finite blow-up time, and a clear reason continuation fails.

**Prior use.** New counterpart to GA-08: the waiting-time example loses uniqueness at zero, whereas this smooth rate law retains local uniqueness but loses global existence.

**Sources.**

- [Gerald Teschl, Ordinary Differential Equations and Dynamical Systems](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf), §2.2, local existence/uniqueness and Problem 2.9 on finite-time existence. Inspection: Local theorem and blow-up exercise inspected; explicit solution and maximal forward intervals checked.

<a id="ga-35"></a>
## GA-35 - A circle’s average can equal its center exactly

Primary field: 31. Related: 35, 26. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What makes harmonic functions obey exact averaging laws on a continuum of surrounding points?

**Anchor.** The harmonic polynomial h(x,y)=x²−y² equals its mean over every circle centered at (a,b). More generally a quadratic Ax²+Bxy+Cy²+Dx+Ey+K has this property exactly when A+C=0, equivalently its Laplacian is zero.

**Bridge (exact-special-case).** The activity investigates actual functions on the plane and their actual circle integrals. Symmetric point groups expose why exact cancellation occurs. Limits: Four successful sample values do not establish an integral identity for an arbitrary function. The continuous mean and the discrete test must remain distinct.

**Prerequisite gates.**

- **Entry:** F/V: evaluate a supplied quadratic at four marked circle points.
- **Explore:** A: move the center, change the radius, and pair opposite points.
- **Explain:** P/A: prove the four-point cancellation and propose a general coefficient condition.
- **Prove:** I: integrate the trigonometric parametrization; D for the Laplacian connection.
- **Reading:** Coordinates and short formulas; calculus notation only at the advanced gate.
- **Arithmetic:** Signed squares and averages; trigonometric identities for the continuous calculation.
- **Reasoning:** Turn sampled evidence into a structural identity with stated scope.
- **Hard Stop:** General mean-value and maximum principles for arbitrary harmonic functions need analysis; a finite sampling experiment is not their proof.

**Materials and preparation (8 minutes).** Coordinate grids, circle templates, value tables, and optional plotting software.

**Launch.** Place four equally spaced points on a circle and evaluate x²−y² at each. Does their average know the value at the center? Move the circle and try to break your guess.

**Learner choices.** Choose center, radius, and starting angle; then choose altered quadratics and design a sampling test likely to expose failure.

**Hour menu.** 0–10 evaluate and compare circles; 10–15 distinguish samples from a continuous average; 15–35 find symmetry cancellations; 35–40 reset; 40–55 integrate if ready or classify four-point identities; 55–60 state exactly what was proved.

**Explore.**

- What cancels between opposite points?
- Could a different function pass our four-point test but fail the full circle-average test?

**Hint ladder.**

1. Use x=a+r cos θ and y=b+r sin θ.
2. The full-circle means of cos θ and sin θ vanish; the means of their squares both equal one-half.

**Checked instance.** Test center (1,2), radius two, then prove the mean identity and find a misleading four-point test.

**Reasoning.** The cardinal points (3,2),(−1,2),(1,4),(1,0) have h-values 5,−3,−15,1, averaging −3=h(1,2). Parametrization gives h=a²−b²+2r(a cos θ−b sin θ)+r²(cos² θ−sin² θ). Every extra term has circle mean zero, proving the identity for all centers and radii. For a general quadratic the circle mean is its center value plus (A+C)r²/2; hence the stated criterion. But q=x²y² on a circle centered at zero has value zero at all four cardinal points while its actual circle mean is r^4/8>0 for r>0.

**Boundary.** The four cardinal samples for q falsely suggest the mean-value identity. Changing the starting angle can expose the failure; a universal proof still needs an exact argument.

**Extensions.**

- Use the Laplacian to classify more harmonic polynomials and then test their mean values.
- Explain directly why x²−y² has no interior local maximum, and compare with −x²−y².

**Satisfying stop.** A proved symmetry identity; calculus-ready learners additionally prove the actual continuous mean formula.

**Prior use.** GA-05 introduced a finite network averaging mechanism. This is the deliberately separate continuous family and does not claim that network experiments prove harmonic-function theorems.

**Sources.**

- [John K. Hunter, Notes on Partial Differential Equations](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), §2.1, Theorems 2.1–2.2 on mean values; §2.3 maximum principle. Inspection: Mean-value statements and smoothness/domain hypotheses inspected; quadratic classification derived independently.

<a id="ga-36"></a>
## GA-36 - A fixed point exists—but will repeated feedback find it?

Primary field: 54. Related: 26, 37. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What separates a topological existence theorem from a convergent algorithm?

**Anchor.** Every continuous f:[0,1]→[0,1] has a fixed point because f(x)−x changes from nonnegative to nonpositive. Iterating f need not converge: f(x)=1−x has fixed point 1/2 but cycles from zero. A contraction adds a quantitative convergence mechanism.

**Bridge (exact-special-case).** The learner’s feedback map is an actual continuous interval self-map. Its fixed point and iterates are exact mathematical objects. Limits: A crossing in a coarse sketch is evidence, while continuity and endpoint inequalities prove existence. Existence by itself supplies no universal iteration guarantee.

**Prerequisite gates.**

- **Entry:** O/V: match a curve with the diagonal and follow feedback arrows.
- **Explore:** F/A: iterate simple affine maps and compare errors.
- **Explain:** P: explain the endpoint sign argument without differentiating.
- **Prove:** P/A: prove the interval theorem by continuity and derive geometric error decay in the chosen contraction.
- **Reading:** Graph labels and a short iteration rule; no derivative notation is necessary.
- **Arithmetic:** Fractions, signed differences, powers of three.
- **Reasoning:** Distinguish an object’s existence, uniqueness, and accessibility by a chosen process.
- **Hard Stop:** A general contraction theorem needs completeness and a sequence-limit proof; the finite computation alone establishes neither.

**Materials and preparation (7 minutes).** Unit-square grids, diagonal lines, arrow cards, and a table for iterates and errors.

**Launch.** A machine turns a number between zero and one into another number in that interval. Can some input come out unchanged? If you repeatedly feed the output back in, must you find it?

**Learner choices.** Choose a continuous graph inside the square, choose a starting value, and try to create settling, alternating, and cycling behavior.

**Hour menu.** 0–10 graph and arrow play; 10–15 define fixed points; 15–35 compare two machines; 35–40 reset; 40–55 prove existence and investigate error decay; 55–60 separate the conclusions.

**Explore.**

- Why does staying inside the unit interval force an intersection with the diagonal?
- What property prevents two different fixed points in the shrinking-distance example?

**Hint ladder.**

1. Compare f(x) with x at the two endpoints.
2. For f(x)=(x+1)/3, subtract 1/2 from both sides of the iteration equation.

**Checked instance.** Start at zero and compare f(x)=(x+1)/3 with g(x)=1−x. Prove that every continuous self-map of the closed interval [0,1] has some fixed point.

**Reasoning.** For f, solving x=(x+1)/3 gives x=1/2. The iterates from zero are 1/3,4/9,13/27,40/81. Their errors satisfy x_n−1/2=(x_0−1/2)/3^n, so after four steps the error is 1/162 and tends to zero. For g, the only fixed point is also 1/2, but zero and one alternate forever. For any continuous interval self-map, d(x)=f(x)−x is continuous, d(0)≥0, and d(1)≤0. An endpoint zero is already a fixed point; otherwise the intermediate value theorem gives an interior zero.

**Boundary.** On the incomplete space (0,1), f(x)=x/2 shrinks distances but has no fixed point in that space: iteration approaches the omitted endpoint zero. The domain hypotheses cannot be discarded.

**Extensions.**

- Use f_q(x)=1/2+q(x−1/2) with −1<q<1. It maps [0,1] into [0,1] and has error multiplier q about its fixed point 1/2. Compare the bound |x_n−1/2|=|q|^n|x_0−1/2|, including alternating errors when q<0.
- Find continuous self-maps with an interval of fixed points, then examine which uniqueness hypothesis fails.

**Satisfying stop.** An existence argument and two exact iterations proving that existence and convergence are different claims.

**Prior use.** New fixed-point synthesis. GA-02 and GA-28 also use continuity; GA-10 studies iteration through symbolic orbits. Return visits should foreground a different question, not repeat the same calculation.

**Sources.**

- [Jiří Lebl, Basic Analysis I](https://www.jirka.org/ra/realanal.pdf), §3.3 intermediate value theorem; §7.6, Theorem 7.6.2 and Exercise 7.6.4 on contractions and completeness. Inspection: Existence and contraction hypotheses inspected; both explicit iterations and the omitted-endpoint example checked.

