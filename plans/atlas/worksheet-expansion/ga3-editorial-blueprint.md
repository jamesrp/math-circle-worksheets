# GA3 editorial blueprint for the final geometry batch

Editor-developed suggestions and exact derivations, not approved worksheet data. The eventual author should improve the prompts and independently verify every claim/source. A different agent must review the final data. Use `ga3-originals.json`, `AUTHOR-BRIEF.md`, and `NEXT-BATCH-NOTES.md`. Suggested scope: three student pages with two substantial prompts each, eight optional guide extensions. Avoid copying supplied answers into student scaffolds.

## GA-18: choose what “best flat height” means

Use height 0 on [0,2/3) and height 6 on [2/3,1], rather than the original 3/4-versus-1/4 instance. Let learners move a horizontal line, choose a loss rule and challenge a candidate.

- Page 1: weighted squared cost. Choose several c; derive Q(c)=(2/3)c²+(1/3)(6-c)²=(c-2)²+8. The unique optimum is c=2, not the unweighted midpoint 3. The complete-square certificate covers every real competitor.
- Page 2: compare absolute and maximum loss. A(c)=(2/3)|c|+(1/3)|6-c| has unique minimizer c=0: outside [0,6] moving toward the interval reduces it, and inside A=2+c/3. Maximum loss max(|c|,|6-c|) has unique minimizer 3 with value 3 by endpoint triangle inequality. Ask learners to invent a wrong “one best average” statement and repair it with the specified objective.
- Page 3: vary the low-region width p∈[0,1]. Q_p=(c-6(1-p))²+36p(1-p), unique mean for every p. Absolute minimizer is 0 for p>1/2, 6 for p<1/2, and every c∈[0,6] for p=1/2. At p=0 or1 the absent-height value has no measure, so integral-based L∞ essential supremum must not be confused with a stray endpoint value. Easiest student core restricts 0<p<1 and addresses endpoints separately in key. Ask to design widths making squared optimum a chosen interior h; p=1-h/6.
- Extension: squared-loss residual has weighted integral zero. For arbitrary step heights a_i and positive widths w_i summing to1, mean μ=Σw_i a_i and Σw_i(a_i-c)²=Σw_i(a_i-μ)²+(c-μ)². This is exact L² projection on constants; general Hilbert-space existence is not proved.
- Gate: fractions, squares, signed algebra/absolute values; integrals are interpreted as rectangle sums. Sources: Axler projection context, exact sections recheck. Diagram must preserve2:1 widths.

## GA-19: defeat every claimed derivative-error bound

Actual calculus is essential. Keep [0,1] and fixed graph scales; no optical rescaling trick.

- Page 1: learner chooses ε>0 and desired slope magnitude M>0. Seek f(x)=a x^n with ||f||∞≤ε and f′(1)≥M; choose a=ε,n≥M/ε. Or use f_n=x^n/n for a uniform-output-one family. A practical exact target ε=1/1000 is different from the original1/100.
- Page 2: prove the general unbounded-operator claim, defining ||f||∞ and the requested inequality. For f_n, norms are1/n and1, ratio n. For any C choose n>C. Uniform convergence f_n→0 does not imply uniform convergence of derivatives to0; their endpoint values stay1. Contrast x^n, whose sup norm stays1, so it does not give the needed small-input sequence.
- Page 3: change the input norm to ||f||∞+||f′||∞. Prove D has bound1, optimal operator norm1 but no nonzero function attains ratio1 (input includes strictly positive ||f||∞). f_n gives ratios n/(n+1)→1. Then compare integration I f(x)=∫₀ˣf(t)dt on continuous functions with sup norms: ||If||∞≤||f||∞, exact operator norm1 attained by f=1. The same derivative operator under a stronger input norm is distinct from changing the operator to integration.
- Extension: noisy forward difference [z(x+h)-z(x)]/h with two independent bounded measurement errors ≤ε has worst error2ε/h; opposite-sign errors attain it. This is the measurement contribution only, not a derivative approximation error theorem or a justified optimal h without a truncation model.
- Gate: derivatives, supremum reasoning, integrals on the last comparison. Parent note: advanced/specialist. Check whether three pages need split gates or fourth page for space; keep each payoff usable.

## GA-20: pay for changes of speed

New physical schedule: start at position0, finish at6 in duration3. Quadratic effort is an invented objective, not metabolic energy.

- Page 1: choose constant speed v for duration1 and w for duration2, allowing negative speeds. Endpoint condition v+2w=6. Write v=2+2a,w=2-a; E=v²+2w²=12+6a². Steady2 uniquely wins; make a rival rush/rest schedule and compare exact costs.
- Page 2: allow any finite partition with durations Δt_i>0 summing3 and displacement ΣΔt_i v_i=6. Identity E=12+ΣΔt_i(v_i-2)² proves the complete finite-schedule optimum. Add a mandatory waypoint y(1)=4: optimize each interval separately to get speeds4 then1, total effort16+2=18. This is an extra constraint with a new attaining path, not a counterexample.
- Page 3: calculus continuation for continuous piecewise-C¹ paths on a finite partition. FTC on pieces yields ∫y′=6 and E=12+∫₀³(y′-2)²≥12. Equality plus continuous derivative on pieces and continuity at joins forces y=2t. Check y=2t+a t(3-t): E=12+9a². Under total distance ∫|y′| the minimum6 has many minimizers: every nondecreasing path, e.g. this family for |a|≤2/3. Show uniqueness depends on the objective.
- Extension: endpoints A,B over durationT>0 give min(B-A)²/T; mandatory time-position waypoints give sum of each Δy²/Δt, attained by the unique piecewise-linear interpolation, by applying the same certificate interval by interval.
- Core finite schedule proof uses algebra; the universal function-space claim needs calculus. Source UCL functional/Euler–Lagrange setup; the global square identity is independent and stronger than mere stationarity.

## GA-21: a mirror that is too short

New instance A=(-2,3), B=(6,1), legal contact M=(m,0) with -3≤m≤5. Straight segment legs A→M→B only, touching the mirror at M.

- Page 1: learner chooses/compares contact points with string; try a construction that could exclude every rival. Do not print the optimal m on the diagram.
- Page 2: reflect B to B′=(6,-1). The crossing of AB′ has parameter3/4 and m=4. It is legal. Global lower bound |AB′|=sqrt(8²+4²)=4sqrt5, attained only by the straight unfolded segment. Thus unique optimum.
- Page 3: shorten legal mirror to [-3,2]. The old equality point is illegal; the original lower bound is unattainable. Prove the new optimum at2 with length5+sqrt17. A calculus-free proof is available using strict convexity: for m≠n and0<t<1, the triangle inequality for the two displacement vectors is strict because positive endpoint height prevents parallel vectors at different contact positions. Hence F((1-t)m+tn)<(1-t)F(m)+tF(n). Since F has global min at4, F strictly decreases up to4 and increases after4 (compare a point between another point and4); the constrained optimum is the nearest legal endpoint in the ordering. Supply the convex-combination inequality as a tool if deriving it would overwhelm the sheet; state the abstraction gate.
- Extension: A=(a,h),B=(b,k),h,k>0. Infinite-mirror crossing m*=(ka+hb)/(h+k), minimum sqrt((b-a)²+(h+k)²). On any closed nondegenerate segment [s,t], clamp m* to[s,t]; strict convexity proves uniqueness. No curved/multiple-mirror claim.
- Respect Week9 overlap by centering optimization and finite-mirror obstruction. Diagram must use equal axes and distinguish actual B from reflected B′.

## GA-22: the adversarial four-peg partition

Allow four distinct points for core, coincidences as explicitly labeled continuation. Both groups nonempty, every label assigned exactly once; hulls include boundaries and one-point hulls.

- Page1: child chooses a challenging arrangement; partner partitions it. Use a new irregular convex quadrilateral A=(0,0),B=(6,0),C=(5,4),D=(0,3) and a separate interior-point configuration A=(0,0),B=(6,0),C=(0,6),P=(2,1), but do not give the winning partition before exploration.
- Page2: prove the complete four-distinct-point theorem by hull cases. If one lies in/on the triangle of the others, isolate it. If not and noncollinear, four convex corners have crossing diagonals. Three collinear plus an off-line point is covered by isolating the middle collinear point. All four collinear: isolate a nonextreme point. For coincident labels, isolate one and put the matching label in the other group. Show why three noncollinear pegs can fail: every partition is one vertex versus the opposite segment.
- Page3: give exact convex-combination certificates. Irregular quad AC and BD intersect at (30/13,24/13), with AC parameter6/13 and BD parameter8/13. Interior point P=(1/2)A+(1/3)B+(1/6)C. Compare geometric proof with signed affine relation; keep signed coefficients distinct from nonnegative convex coefficients.
- Extension: supply linear dependence of d+2 vectors (p_i,1) in R^(d+1). A nontrivial relation Σα_i p_i=0,Σα_i=0 has both positive and negative coefficients. Normalize their common positive sum to get two equal convex combinations. Zero-coefficient labels can be assigned arbitrarily to a nonempty side. This proves the general Radon partition from the supplied linear-algebra fact, including coincidences. Gate clearly linear algebra.
- Source Hug–Weil Theorem1.2.1. Rubber-band drawings are representations, not the completeness proof.

## GA-23: a route turns the tangent arrow

Core exact transport rule: on a great-circle leg, resolve a tangent vector as aT+bN, where T is the forward unit tangent and N is the fixed normal to the leg's oriented plane. Preserve a,b along the leg. At a corner keep the actual vector fixed, then decompose using the NEXT leg's frame; do not rotate it along with the walker. This supplied rule defines the model; general parallel-transport equivalence is background.

- Page1: ball exploration around A=(1,0,0),B=(0,1,0),C=(0,0,1), route A→B→C→A. Choose initial+y,+z or a mixture. Compare reverse route and an out-and-back route. Clear tangent arrow, different-colored forward tangent.
- Page2 exact proof: for AB use r=(cos t,sin t,0),T=(-sin t,cos t,0),N=+z; BC use r=(0,cos t,sin t),T=(0,-sin t,cos t),N=+x; CA use r=(sin t,0,cos t),T=(cos t,0,-sin t),N=+y;0≤t≤π/2. T can be supplied as a verified unit forward tangent so calculus is not necessary for component tracking. Initial+y becomes -x atB, stays-x toC, ends+z atA. Initial+z stays+z toB, becomes-y atC, stays-y toA. Therefore a y+b z maps to -b y+a z: positive90° in the outward-oriented tangent plane atA. Reverse is the inverse rotation; retracing a leg cancels its transport.
- Page3 vary longitude: B=(cosα,sinα,0),0<α<π, use equator arc A→B and shortest meridians B→C→A. Initial+y maps to cosα y+sinα z; initial+z maps to -sinα y+cosα z. Derive by the same two-component rule, not a general curvature theorem. Check a learner-selectedα, e.g.π/3. The spherical lune between the two meridians has area2α on the unit sphere; its northern half triangle has areaα. Explain this matching angle/area only for this proved family.
- Extension: repeat route k times. A nonzero vector returns iff kα is an integer multiple of2π. For α=π/3 first return6; if α/(2π) is irrational it never returns at a positive integer repetition. This is algebra on the proved rotation.
- Gate spatial tangent-vector reasoning; trigonometric components for variedα. No claim a compass or fixed3Darrow implements transport. Parent prep ball15minutes realistic. Source Petrunin–Zamora transport chapters/Prop17.10 recheck actual locator.

## GA-24: test a proposed reversible reshaping

Start with strings/shapes; then define a homeomorphism as continuous bijection with continuous inverse. Physical cutting removes a short interval; the proof deletes one mathematical point. Crossings must say whether joined.

- Page1: choose punctures on a loop, closed interval, joinedY, joinedfigure-eight and two disjoint loops. Record the number of remaining connected pieces; include endpoint versus interior choices. Predictions and examples precede an impossibility claim.
- Page2: supply connectedness of an interval and preservation under a continuous image, and explain restriction of a homeomorphism after deleting matching points. Prove circle not closed interval by choosing interior1/2; every punctured circle is connected (parameterized by an open angle interval), while the punctured interval has two components. Use Y's branch-point deletion (three components) to distinguish it from the interval. Joinedfigure-eight loses its joined point to leave two components, unlike a circle; it is originally connected, unlike two disjoint loops.
- Page3: diagnose continuous but non-homeomorphic maps: projection (x,y)↦x maps circle onto[-1,1] but identifies upper/lower points; t↦(cos2πt,sin2πt) maps[0,1] onto circle but identifies endpoints. Construct a positive homeomorphism from circle to ellipse(x/2)²+y²=1: (x,y)↦(2x,y), inverse(X,Y)↦(X/2,Y). These concrete maps make the no-identification/reversibility condition substantive.
- Extension: one-point tests do not classify all spaces. Both circle and closed disk stay connected after deleting one point. Circle minus two distinct points has two arcs; closed disk minus any two distinct points remains path-connected. For any retainedp,q choose an interior z avoiding the finitely many lines through p or q and a deleted point; the polygonal path p→z→q stays in convex disk and avoids deletions. Such z exists because a finite union of lines cannot cover an open disk. Thus no homeomorphism exists despite identical one-point component counts. Gate basic planar paths and the supplied finite-line fact.
- Source Sharifi connected-image proposition; proof/particular comparisons independent. Avoid treating mere bending in ambient3-space as a full definition of abstract homeomorphism.

## GA-27: find the flood's exact joining height

Use f=x²-y² on the actual clipped square[-1,1]². Flood means f≤c, including equality. All-domain classification is possible with elementary inequalities.

- Page1 choose negative and positive levels and classify testpoints before sketching. Retain levels-1/4,0,1/4 as a useful common comparison; ask for a wet path or an impossibility certificate between(0,1) and(0,-1).
- Page2 complete classification: c<-1 empty; c=-1 exactly(0,±1); -1<c<0 exactly two components. Negative-level upper/lower pieces cannot meet because y never0; each joins vertically to its top/bottom boundary, then along that boundary within |x|≤sqrt(1+c). At c=0 two wedges meet at origin; c≥0 is nonempty and star-shaped about0 since f(tx,ty)=t²f(x,y)≤c. For c≥1 the entire square is flooded. At0 the only flooded point on y=0 is origin. A path between the two given endpoints must cross y=0, hence max f along path≥0, attained on x=0. If the crossing is forced to be(a,0),|a|≤1, the exact minimum possible maximal height is a²; attain by going along top to(a,1), vertically to(a,-1), then along bottom. This connects chosen path design with the barrier proof.
- Page3 calculus interpretation: gradient(2x,-2y), onlycriticalpoint0; Hessian diag(2,-2), index1. Bowl x²+y² has positive Hessian and a component born at0. The graph of x⁴-y⁴ has the same sign-pattern/zero wedges but zero Hessian at0, so appearance alone cannot authorize Morse lemma. Keep the square-boundary events separate from smooth compact-manifold theorems.
- Extension: whole-plane doublewell F=(x²-1)²+y². c<0 empty;c=0 two minima;0<c<1 two components;c≥1 connected, meeting through saddle0 atc1. Allowed x satisfy |x²-1|≤sqrt(c): two intervals when c<1 and one when c≥1. Every vertical fiber joins its x-axis point, proving component counts from those intervals. Gradient gives minima(±1,0) with Hessian diag(8,2), saddle(0,0) with diag(-4,2). This is an explicit new model, not an inferred general topology theorem.
- Source Gillespie local Morse lemma and critical-level context. Core finite-square connectivity uses paths and inequalities; derivatives are only on the later interpretation.
