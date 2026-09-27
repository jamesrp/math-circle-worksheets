# GA4 independent mathematical and design review

Reviewer: expand_ga1. Date: 2026-09-25. **Closed: no outstanding design findings.** PDF production may proceed; this report does not certify PDFs that have not yet been produced.

I read every student prompt before comparing its solution, independently solved all 48 prompts and eight guide extensions, then reviewed all keys, hints, gates, source records, figure data and the author's checker. The batch contains GA-28, GA-30–36: eight families and 24 student body pages. The instances and general arguments agree with the keys, including the difficult calculus continuations. I reopened all eight primary references at the locators recorded below.

The independent `review-ga4-checks.py` and its results file supplement this proof review. They prove the entire quadratic four-sample identity by formal polynomial arithmetic in four indeterminates, trace actual strip-edge boundary circuits independently for 1–64 lanes, verify the batch counts and wording repairs, and rerun the author's finite audits with author-file writes suppressed. All pass. Finite checks do not replace the general arguments summarized here.

## Findings and closure

1. **GA-28, page 1 comparison game.** “Secret number” could suggest commitment before a partner is required to choose the longer side. The revised introduction explicitly allows delaying the choice of r while requiring all replies to remain jointly consistent. Reread the actual revised field. Closed: every finite retained interval has an interior r realizing the complete history, exactly as the lower-bound proof requires.
2. **GA-32, prompts 4–5 terminology.** The tracing/counting entry gate did not support an unexplained surface-type request or “transverse direction.” Prompt 4 now defines annulus as an ordinary band with matching ends, and prompt 5 explicitly names the ordinary-band/Möbius alternatives and describes an arrow across the strip's width. Reread both prompts. Closed.
3. **GA-30 preparation clarification.** The author added edge-to-edge joining without paper overlap to the materials and first introduction. Reread both. This makes the circumference of the 6-by-4-inch model genuinely 6 inches; actual-size printing remains explicit. Closed.

There are no remaining mathematical corrections or source-locator repairs. References to already delivered activities correctly distinguish a new investigation from prior warm-ups: notably AP-06 versus GA-28's cycling cubic, discrete harmonic work versus GA-35's circle/quadratic classification, and the Week 1 tiling ribbon versus GA-32's surface identifications.

## Family-by-family independent derivations and usability

### GA-28 — comparisons, root brackets and a cycling tangent rule

Prompts 1–2: after any comparison in an interval of width W, one side has width at least W/2. An adversary can retain that side and still choose a consistent interior target after any finite history. Thus four tests cannot guarantee less than 1/16; midpoints attain it. Exact-hit histories do not invalidate this worst-case argument.

Prompts 3–4: the successive midpoints for the positive square root of 2 are 3/2, 5/4, 11/8 and 23/16, with squares 9/4, 25/16, 121/64 and 529/256. The final bracket is [11/8,23/16]; 45/32 has error at most 1/32. Seven tests first give width below 1/100. The jump function taking −1 below zero and +1 at/above zero has opposite endpoint signs but no root, proving why the supplied continuity hypothesis matters.

Prompts 5–6: for f(x)=x³−2x+2, f′(x)=3x²−2 and Newton sends 0 to 1 to 0. Both denominators and both function values are nonzero. Bisection on [−2,−1] tests −3/2 and −7/4, giving 13/8 and 9/64; the certified bracket is [−2,−7/4]. The extension's fixed-fraction strategy has worst-case width max(q,1−q)^n, uniquely minimized by q=1/2.

The interval records leave actual test choices to students and support the adversarial proof; the nonlinear continuation is explicitly gated by derivatives. The payoff is a guarantee and a lower bound, followed by a genuine failure of another method.

### GA-30 — all routes on a cylinder

Prompts 1–4: unrolling preserves length and a lifted path ends at (3+6k,4) for some integer k. Its length is at least √((3+6k)²+16). All integers satisfy |3+6k|≥3, with equality exactly at k=0 and −1. Straight segments to these two endpoints attain 5 and stay within the strip. Equality in the plane excludes other geometric minimizers, up to reparametrization. Nonrectifiable paths cannot improve the answer. The next endpoints, with horizontal displacement ±9, give √97.

Prompts 5–6: for 0≤d<6 the minimum is √(16+min(d,6−d)²), with k=0 winning below d=3, k=−1 above it, and exactly those two tying at d=3. At d=0 the vertical route is unique. The locally straight path lifting to (9,4) is globally longer than 5, so local straightness alone is insufficient. The extension follows verbatim with circumference C>0 and height H>0: √(H²+min(d,C−d)²), a two-route tie only at d=C/2.

The edge-to-edge 6-by-4 model and repeated strip have sufficient dimensions, destination copies and legal-surface restrictions. The key explicitly covers copies beyond those printed. Spatial unrolling and Pythagoras are honest prerequisites; no calculus is smuggled into the core.

### GA-31 — what makes pairwise intersections sufficient?

Prompts 1–4: the supplied four intervals have intersection [3,4]. For any finite nonempty family of nonempty closed intervals, let L be the largest left endpoint and U the smallest right endpoint. The intersection is [L,U] when L≤U. If L>U, the intervals attaining these extrema are disjoint, contradicting pairwise intersection. If one interval attains both extrema, its nonemptiness already gives L≤U. Checking only against a favorite interval fails for [0,6], [0,1], [5,6]. The intervals [0,3], [3,6], [2,4] have singleton intersection {3}.

Prompts 5–6: within the stated square, the regions x≥0, y≥0 and x+y≤−1 have pairwise witnesses (0,0), (0,−1), (−1,0), but no triple intersection. They remain convex: dimension changed. The disconnected sets {0,1}, {1,2}, {0,2} give the second failure through gaps. The extension's rays [n,∞) have all finite intersections nonempty but empty total intersection; for a pairwise-intersecting family of closed bounded intervals, fixing one compact member and using the finite intersection property proves the supplied compactness extension.

The endpoint strips, chosen examples and bounded planar diagrams are adequate. Ordering endpoints supports the core; signed inequalities and compactness are distinctly gated. The investigation develops a certificate, then tests its hypotheses rather than presenting a string of unrelated counterexamples.

### GA-32 — count paper components and boundary circuits separately

Prompts 1–4: the plain band has two boundary loops and its center cut yields two annuli. The Möbius band has one boundary loop; after its center cut the lane journey U→L→U gives one connected piece. Two seam reversals restore an across-width arrow, so that piece is an annulus with two boundary loops. Intact lane interiors connect to their seams, making the lane-component argument complete.

Prompts 5–6: the three-lane reversal has cycles (U L) and (C). The former has two reversing seams and is an annulus; the latter has one and is Möbius. There are two surface components and three boundary loops regardless of physical linking. This supplies valid corrections to both “one piece has one boundary” and “linked means connected.” The extension's reversal i↦m+1−i gives floor(m/2) annuli plus a middle Möbius band when m is odd: ceil(m/2) components and m boundary loops. My independent check traces the long-edge identifications themselves, rather than merely recomputing 2×annuli+Möbius.

The specified seam rule is sufficient to prove the result without a successful physical cut. The claim is intrinsic surface type, not an assertion that the embedding can be untwisted or unlinked. Preparation is ordinary strips/tape/scissors; corrected vocabulary fits the accessible tracing gate.

### GA-33 — the boundary term remembers the initial state

Prompts 1–2: for y′=1−y, y(0)=a, the candidate is 1+(a−1)e^(−t). The chosen starts −1 and 0 increase to 1; 2 decreases to 1. The initial slope is 1−a. A transform computation giving the same 1/[s(s+1)] for every start has lost the initial condition and only describes a=0.

Prompts 3–4: integration by parts over [0,T] gives e^(−sT)y(T)−a+s∫₀ᵀe^(−st)y(t)dt. For these bounded candidates and s>0 the boundary term vanishes and the relevant integrals converge. Thus L(y′)=sY−a and Y=1/s+(a−1)/(s+1). Direct substitution verifies the candidate. If two solutions exist, their difference z obeys (e^t z)′=0 and z(0)=0, proving uniqueness without assuming transform injectivity.

Prompts 5–6: forcing e^(−t) and initial zero give Y=1/(s+1)² and y=te^(−t). Its derivative is (1−t)e^(−t), so the unique peak is at t=1, height 1/e, precisely where the input equals the loss. The extension y′+ky=c with k>0 gives c/k+(a−c/k)e^(−kt), with the same direct verification and integrating-factor uniqueness.

The course-level calculus gate is explicit, including improper integrals and integration by parts. The trajectory and transform records are usable and do not substitute guesswork for the boundary-term derivation. The investigation connects a concrete family of initial states to why the transform formula must contain a.

### GA-34 — locally valid dynamics need not continue forever

Prompts 1–2: from y(0)=1, y=1/(1−t), and reaching H>1 takes 1−1/H. Doubling times t_n=1−2^(−n) have gaps 2^(−n), whose total approaches 1. The rational derivative is the square of the function.

Prompts 3–4: the expression on t>1 is a negative solution on a different interval, not a continuation across t=1. Any differentiable continuation would need a finite continuous value there, impossible because the left-hand values diverge. Smoothness at each finite state and local uniqueness do not impose a bound on growth over an unbounded range of states.

Prompts 5–6: y=a/(1−at) has maximal forward interval [0,1/a) for a>0; a=0 is forever zero; a<0 exists for every forward time and increases to zero from below. For nonzero solutions, z=1/y gives z′=−1, explaining the pole. Exponential growth ae^t has no finite-time divergence. In the extension p>1, positive initial value a gives y=[a^(1−p)−(p−1)t]^(−1/(p−1)) and blow-up time a^(1−p)/(p−1); local uniqueness on positive states and the divergent endpoint justify the maximal forward interval.

Calculus remains the core, and the doubling work is honestly labeled a warm-up. Tables and graph space support exploring the approach to the pole without suggesting the disconnected negative branch repairs it.

### GA-35 — sampling a circle versus averaging the circle

Prompts 1–2: for x²−y² around (1,2) at radius 2, cardinal sample values are 5, −3, −15, 1, with mean −3 equal to the center. For a general rotated cross with displacement vectors (u,v), (−v,u), (−u,−v), (v,−u), first moments and the mixed moment vanish; both squared-coordinate moments are (u²+v²)/2.

Prompts 3–4: the mean shift of q=Ax²+Bxy+Cy²+Dx+Ey+K is (A+C)r²/2. Consequently the every-center/every-radius quadratic classification is exactly A+C=0. My formal polynomial checker proves this for all coefficients by checking a basis symbolically. For x²y² on the unit circle, the cardinal samples are zero while the rotated diagonal samples are all 1/4; the actual circle mean is 1/8. Thus a finite sampling rule is not automatically the full mean-value property.

Prompts 5–6: integrating a quadratic over the circle gives the same classification and Δq=2(A+C). The cited general harmonic theorem has further hypotheses and is not proved by four-point sampling. The saddle x²−y² has no local extrema: at a center with x≠0 vary x slightly in both directions; at x=0,y≠0 vary y; at the origin compare the axes. The extension −x²−y² has a strict global maximum at the origin and Laplacian −4, as required by the contrast.

Coordinates, signed squares and algebra suffice for the finite core. The continuous integral and general PDE theorem are explicitly more advanced. Rotatable sample diagrams and circle data permit genuine learner choices without claiming four samples settle all functions.

### GA-36 — existence, uniqueness and iteration are different claims

Prompts 1–2: f(x)=(x+1)/3 has fixed point 1/2 and error e_n=e_0/3^n. On [0,1], the worst error is 1/(2·3^n), so four iterations first guarantee error below .01. From zero the four values are 1/3, 4/9, 13/27 and 40/81. The reflection 1−x has the same unique fixed point but alternates unless it starts there.

Prompts 3–4: for a continuous self-map of [0,1], d(x)=f(x)−x has d(0)≥0 and d(1)≤0. An endpoint zero or the supplied IVT produces a fixed point. The identity and reflection distinguish existence from uniqueness and convergence. For f_q(x)=1/2+q(x−1/2), −1≤q≤1, every q≠1 has the unique fixed point 1/2, while q=1 fixes every point. If |q|<1, e_n=q^n e_0 converges to zero, alternately when q<0; q=0 reaches it in one update; q=−1 gives a two-cycle away from it.

Prompts 5–6 and extension: x/2 maps (0,1) into itself and is contracting, but the only possible fixed point is the excluded endpoint zero. The missing closed/complete domain matters. The discontinuous map that is 1 below 1/2 and 0 at/above 1/2 has no fixed point on [0,1], demonstrating why continuity cannot be deleted from the interval existence proof.

The number-line/iteration scaffolds and allowed q-range support the full classification. Affine algebra is the core and the IVT is explicitly supplied. The resulting distinction among existence, uniqueness and algorithmic convergence is substantive.

## Source verification

All links below were reopened on the review date. The stated scope is source background; the instances and elementary arguments above were independently checked.

- [MIT Unit VI](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-spring-2013/60af88c658ba3e83cdf7c43289aeb5b4_MIT2_086S13_Unit6_Textbook.pdf): bisection paragraph in §29.2.3 on printed p.432, and §29.2.5 describing cycling Newton trajectories. The locators are correct even though §29.2.3 begins with Newton's algorithm.
- [Petrunin and Zamora Barrera](https://arxiv.org/pdf/2012.11814): §18G, printed p.160, explicitly gives the plane-to-cylinder length-preserving map. The worksheet's discrete lift minimization is independently derived.
- [Hug and Weil](https://users.fmf.uni-lj.si/lavric/hug%26weil.pdf): finite Helly in §1.2, Theorem 1.2.2, p.22, and compact-family Theorem 1.2.3, p.23. The infinite extension retains the needed compactness premise.
- [Hatcher](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf): Chapter 0, printed p.2, contains the Möbius-band/core-circle model. The author correctly does not attribute the lane-cut puzzle or its counts to this passage.
- [Boyd](https://web.stanford.edu/class/ee102k/laplace.pdf): slides 3–19 through 3–21 give the derivative transform and integration-by-parts boundary term; slide 3–32 supplies the basic table. The worksheet specializes to ordinary smooth bounded candidates and checks convergence.
- [Teschl](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf): §2.2 and Problem 2.9 on printed p.42/PDF p.53 support the local-uniqueness and finite-time blow-up context. The signed-start and power-law classifications were checked independently.
- [Hunter](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf): Theorems 2.1–2.2 on printed pp.20–21 state the harmonic mean-value context with the domain and regularity hypotheses. The worksheet limits its elementary classification to quadratics.
- [Lebl](https://www.jirka.org/ra/realanal.pdf): §3.3 and §7.6, Theorem 7.6.2 on printed p.296, plus Exercises 7.6.4/7.6.6 on pp.299–300 in version 6.3. Completeness is present in the contraction theorem; the open-interval example deliberately lacks it.

## Production handoff

The proposed diagrams, boards, tables and legal moves are sufficient on paper. The renderer must still preserve exact dimensions and seam conventions for GA-30/32 and must not reveal classifications through a fixed number of answer slots. Every student page needs full-size independent PDF review; guide pages need the contract's contact-sheet and dense-page inspection. Timing and facilitator suggestions are unpiloted. No classroom-pilot or further approval gate is imposed by this review.
