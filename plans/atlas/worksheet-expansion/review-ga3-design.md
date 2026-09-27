# GA3 independent design review — closed

Reviewer: expand_ad1. September 26, 2026. Reviewed `ga3-data.json` (SHA-256 `d1f20b3d652c9e76ecbdb998369a574d787cd11e4d8b6906d8a4e4858f52cb53`), `ga3-design.md`, and the complete author checker. Coverage: **all eight families, all 50 student prompts, all eight guide extensions, and all 25 planned student pages**. I independently derived the instances and general arguments below and compared every keyed answer. The author's checker was also read and run successfully. Its finite checks are supporting evidence, not the proof of universal assertions.

**Result: design review closed, approved for production. No mathematical or design repair is required.** This does not approve unrendered PDFs. The maker and independent PDF reviews must still inspect actual diagrams, supplied objects, workspace, answer timing and typography.

## GA-18 — prompts 1–6 and extension

The learner's freely selected candidate and loss in prompt 1 are testable with the printed exact width ratio. Independently, the squared loss is `(2/3)c²+(1/3)(6−c)²=(c−2)²+8`, so prompt 2 has unique minimizer 2. For prompt 3 the absolute loss is `2−c` below 0, `2+c/3` on [0,6], and `c−2` above 6; its unique minimizer is 0. The maximum error is at least 3 because the two endpoint errors sum to at least 6, and equality forces c=3. Thus the ambiguous claim in prompt 4 really does depend on the cost definition.

For prompts 5–6 and low-height width p, completion of the square gives mean `6(1−p)` and residual cost `36p(1−p)`. The absolute-loss slope inside [0,6] is `2p−1`, with outer slopes −1 and +1. Consequently its minimizer is 0 when p>1/2, 6 when p<1/2, and all of [0,6] when p=1/2. The maximum minimizer stays 3 for 0<p<1. Prescribing an interior squared-loss optimizer h uniquely sets p=1−h/6; no such h can be a unique absolute-loss optimizer. The excluded zero-width cases are genuinely excluded, preventing an endpoint-value convention from changing the maximum problem.

For the extension, μ=Σwᵢaᵢ gives Σwᵢ(aᵢ−μ)=0 and the exact variance decomposition `Σwᵢ(aᵢ−c)²=Σwᵢ(aᵢ−μ)²+(c−μ)²`. This proves uniqueness without importing a Hilbert-space existence theorem. The concrete rectangle model supports the abstraction, and fractions, absolute values and algebra are accurately gated. The specified 2:1 diagram and movable line are sufficient; no optimum is supplied prematurely. GA-13's affine minimax task is explicitly distinguished.

## GA-19 — prompts 1–6 and extension

For any ε,M>0, choose `a=ε` and an integer `n≥M/ε`, n≥1. Then axⁿ on [0,1] has norm ε and endpoint derivative εn≥M. The required ε=1/1000, M=7 works with n=7000 exactly. For fₙ=xⁿ/n, the norms in prompt 2 are 1/n and 1; n=1 is included. Choosing n>C proves prompt 3 against every proposed finite nonnegative bound C, not merely against a sampled list.

In prompt 4, fₙ tends uniformly to zero while its derivatives do not: their endpoint value stays 1. The tempting xⁿ family has input norm 1 and therefore fails the required premise. For prompt 5, the changed input norm gives derivative ratio at most 1 and strictly less than 1 for each nonzero function, since its function norm is positive. The fₙ ratios n/(n+1) approach 1, proving sharpness without attainment. Prompt 6's integration map has norm ≤1 from `|∫₀ˣf|≤x||f||∞`; f=1 attains the bound at x=1.

The extension's error is `(e₁−e₀)/h`, hence exact worst magnitude 2ε/h, attained by opposite extreme errors. This bounds the measurement contribution relative to the true finite difference; it does not supply a derivative truncation model or an optimal h. Calculus, supremum norms and quantified counterexamples are honest core prerequisites. Fixed-scale axes and a blank ledger support the task without pretending a plot is the norm proof.

## GA-20 — prompts 1–6 and extension

For prompt 1, legal two-speed schedules satisfy v+2w=6; (0,3) costs 18 and (−2,4) costs 36, confirming that backward travel is permitted but charged. Writing v=2+2a, w=2−a gives prompt 2's exact cost 12+6a². For any positive-duration finite partition totaling 3, expansion using ΣΔtᵢvᵢ=6 gives `E=12+ΣΔtᵢ(vᵢ−2)²`. Equality forces every speed 2. Different subdivisions do not produce different minimizing motions.

The waypoint in prompt 4 forces displacement 4 in time 1 and displacement 2 in time 2. Applying the same identity separately yields unique speeds 4 then 1 and bill 18, including schedules with additional subdivisions. For prompt 5, FTC applies on the explicitly stated finite C¹ pieces and telescopes across their continuous joins. Thus `E[y]=12+∫(y′−2)²`. If equality holds, the continuous nonnegative integrand vanishes on each piece, giving the unique y=2t everywhere.

For prompt 6, y=2t+a t(3−t) has derivative 2+a(3−2t) and squared integral 12+9a². Total distance instead has lower bound 6; equality is equivalent to nonnegative derivative on the pieces, or to a nondecreasing path. In this family that is exactly |a|≤2/3. For the extension, the same expansion gives minimum `(B−A)²/T`; applying it between strictly ordered waypoints yields the sum of interval costs and unique piecewise-linear interpolation. Reversals between prescribed waypoints remain legal.

The diagrams state time and position, the quadratic bill is declared rather than presented as physical energy, and the finite algebraic core is separated from the calculus class. Endpoints and later waypoint are sufficient supplied objects; optimal paths remain learner constructions.

## GA-21 — prompts 1–6 and extension

The admissible variable in prompt 1 is contact m in the printed mirror interval. The cost in prompt 2 is `F(m)=√((m+2)²+9)+√((m−6)²+1)`. The mirror midpoint m=1 has squared cost `44+12√13>80`; m=4 costs 4√5, so midpoint symmetry is false for these endpoints.

Reflection in prompts 3–4 sends B to (6,−1); the segment from (−2,3) reaches y=0 at parameter 3/4, hence contact (4,0). Triangle inequality yields lower bound √80 and its equality condition gives this unique contact, which is initially legal. After shortening the interval, prompt 5's old lower bound is unattained. Prompt 6 correctly supplies the extra strict-convexity fact needed: vectors (m−a,−h) at distinct m cannot be parallel when h>0. If x<y<m*, write y as a strict convex combination of x and the unique minimum m*. Strict convexity then gives F(y)<F(x). The symmetric argument applies on the right. Therefore m=2 is the unique shortened-mirror optimizer, cost 5+√17.

The extension crossing is `(ka+hb)/(h+k)` and clipping it to [s,t] gives the complete unique constrained optimizer. Positive heights ensure strictness; equality with either endpoint is included. Ruler trials are not sold as proof. Equal coordinate scales, legal-contact intervals, and undrawn reflected point/contact are adequate design specifications. The prior billiards use is candidly cross-linked.

## GA-22 — prompts 1–6 and extension

Prompts 1–2 allow genuine adversarial arrangements and provide all four labeled points, with boundaries and singleton hulls legal. Independently, the first coordinate board is a convex quadrilateral and AC meets BD. The second has P inside ABC. For prompt 3, the supplied planar hull alternative reduces noncollinear boards to an isolated point in/on the other triangle or crossing diagonals. If all points are collinear, either middle point can be isolated. If exactly three are collinear, their middle point lies on the opposite triangle edge. These cases include the degeneracies rather than relying on a generic drawing.

For prompt 4, coincident labels give a shared point when one is isolated and the rest form the second group. A noncollinear triple defeats every partition because its singleton vertex is outside the opposite edge. For prompt 5, solving `(5r,4r)=(6−6s,3s)` gives r=6/13, s=8/13 and intersection (30/13,24/13). Both coefficient pairs are positive and sum to one. Prompt 6 gives P=(1/2)A+(1/3)B+(1/6)C; moving P across gives a zero-sum signed affine relation. The negative-weight example 2B−A lies outside AB, so the convex/affine distinction is substantive.

The extension's nonzero dependence among lifted (pᵢ,1) forces positive and negative coefficients since their sum is zero. Their equal positive total normalizes two convex combinations. Zero-coefficient labels may be added to either group without destroying the witness; coincidences cause no failure. The general-dimensional linear-dependence fact is explicitly supplied and separately gated. Initial boards must retain their specified absence of hull edges and diagonals. No repetition or preparation issue was found.

## GA-23 — prompts 1–8 and extension

I checked the frame values and actual corner vectors independently. For +y, AB sends it to −x at B, BC holds it as −N through C, and CA sends −T to +z. For +z, AB holds it, BC sends T to −y, and CA holds −N. These give the prompt 1 experiments and prompt 3 certificate. Prompt 2's out-and-back restores every vector, whereas reverse triangular transport is the inverse quarter-turn. Prompt 4's map `(a,b)↦(−b,a)` is linear, preserves a²+b² and has the stated positive orientation from +y toward +z. Reversing a leg changes both oriented frame vectors' signs and exactly undoes it.

For prompts 5–6, write c=cos α, s=sin α. Initial +y reaches C as (−s,c,0), hence becomes c·y+s·z at A. Initial +z reaches C as (−c,−s,0), hence returns as −s·y+c·z. Thus the complete map is `(a,b)↦(ac−bs,as+bc)`. Its norm identity follows by expansion, and the fixed-vector equations have determinant 2(1−c)>0 for 0<α<π. The α=π/3 unit-arrow instance is therefore (1/2,√3/2).

For prompt 7 the lune is fraction α/(2π) of area 4π, and its northern half has area α. This agrees with the independently derived rotation for precisely the stated route family. Prompt 8's ambient fixed +y has dot product sin t with equatorial radius and generally fails tangency. Retracing is a valid zero-holonomy closed route, so curvature alone does not force every itinerary to rotate. The extension composes the proved rotations: return for a nonzero vector iff kα∈2πZ, first k=6 for π/3, and no positive finite return for irrational α/(2π).

The model's rule genuinely agrees with parallel transport: for a unit-speed great circle, T′=−r and fixed N′=0, so the derivative of aT+bN is normal to the tangent plane. Learners can use the supplied rule without proving that differential-geometric equivalence. Spatial signed-vector and later trig gates are explicit. The four-page allocation is warranted. Physical carried and forward arrows must remain visually distinct, and no returned arrow may appear on the initial picture; the specification says so.

## GA-24 — prompts 1–6 and extension

For prompts 1–2 the possible one-point deletion counts are circle {1}, segment {1,2}, Y {1,2,3}, joined eight {1,2}, separate loops {2}. These are counts for geometric strands with retained edge interiors. In particular, a punctured non-junction point of one lobe of the eight does not disconnect the whole space. The endpoint trap on the interval is real.

For prompt 3, remove the midpoint of [0,1] and its matching image. The punctured interval has a separation, whereas every punctured circle is a continuous image of an open interval of angles, after a rotation. The inverse restricted homeomorphism would contradict connected-image preservation. In prompt 4 the Y center's three components cannot correspond to any interval point, and the eight's join cannot correspond to any circle point. Whole-space connectedness already separates the eight from two disjoint loops. Homeomorphisms induce component bijections by applying connected-image preservation to map and inverse.

Prompt 5's projection identifies (0,±1), and its parametrization identifies endpoints 0 and 1; neither is injective. Prompt 6's coordinate scaling and inverse map exactly between the stated circle and ellipse, are continuous, and compose to identities. Length and angle preservation are unnecessary.

The extension is correct for a closed nondegenerate disk including boundary punctures. For retained p,q choose interior z outside the finitely many lines through either endpoint and either deleted point. Convexity keeps pz and zq inside the disk; the line exclusions keep them away from both punctures. Thus the disk minus either one or two points is path-connected, while the twice-punctured circle has two open arcs. The supplied finite-line fact makes the existence step explicit. The entry's informal tracing statement is limited to these examples; the formal page supplies the correct homeomorphism and connectedness facts. Joined and disjoint diagram conventions are sufficient.

## GA-27 — prompts 1–6 and extension

For prompt 1, at levels −1/4, 0, 1/4 the exact inequalities are respectively `y²≥x²+1/4`, `|y|≥|x|`, and `x²≤y²+1/4`, always clipped to the square. Equality matters at the zero joining point. Prompt 2's negative-level obstruction follows from the intermediate value property of the y-coordinate and f(x,0)=x²≥0. The axis route attains the threshold 0.

For prompt 3, the range on the square is [−1,1]. Below −1 the wet set is empty; at −1 it is the two points (0,±1). Every negative wet upper point connects first vertically to (x,1) and then to (0,1); the admissible top interval is |x|≤√(1+c). The analogous lower route and the y-sign separation give exactly two components for −1≤c<0. For c≥0, radial scaling stays wet: if f≥0 it lowers f, and if f<0 the scaled value remains ≤0≤c. Thus there is one component, and the entire square appears exactly at c≥1.

Prompt 4's mandatory point has height a², giving the lower bound. The three-segment top/vertical/bottom route attains it inside the square, including a=0 and a=±1. Prompt 5's gradient and Hessian are (2x,−2y) and diag(2,−2), hence one index-one critical point; the bowl instead has an index-zero birth. Prompt 6's quartic has the same zero sublevel but zero Hessian at the origin, so the Morse lemma cannot be invoked.

For the extension, the allowed x obey `max(0,1−√c)≤x²≤1+√c` when c≥0. Fibers contract vertically to the wet axis. There are two singleton points at zero, two axis intervals/components for 0<c<1, and one for c≥1, first joined at the origin. Critical points are (±1,0),(0,0) with Hessians diag(8,2), diag(−4,2); the saddle level is 1. Empty c<0 is included. These are direct global proofs on the actual domains, not misapplications of a smooth-boundary theorem. Signed inequalities and paths are the core; derivatives/Hessians have a separate gate.

## Source and check-code audit

I independently reopened the primary sources on September 26, 2026. Axler's current [MIRA](https://measure.axler.net/MIRA.pdf) has the cited bounded-map definition in §6C and projection definition/residual characterization in §8B; the data accurately distinguish the worksheet's own witnesses. [UCL §2](https://www.homepages.ucl.ac.uk/~ucahmto/latex_html/pandoc_chapter2.html) supplies the functional framework, not a global-minimum certificate. [Petrunin's Euclidean text](https://arxiv.org/pdf/1302.1630) supplies reflection's distance preservation. [Hug–Weil](https://users.fmf.uni-lj.si/lavric/hug%26weil.pdf), printed/PDF p.22, supplies the actual positive/negative affine-dependence normalization. [Petrunin–Zamora](https://arxiv.org/pdf/2012.11814) Chapter 16 supplies the normal-derivative tangent-field definition and transport; the stated special-family calculation has the correct sign convention. [Gillespie](https://web.math.utk.edu/~afreire/teaching/m663f21/Morse_Theory_Notes.pdf) states nondegeneracy in the Morse lemma and explicit admissibility/boundary hypotheses later, which are not silently applied to the square.

Direct opens of Sharifi's two HTML chapters failed for this reviewer too. Indexed primary-page text did expose and was read for [Definition 2.1.13](https://www.math.ucla.edu/~sharifi/notes/topology-ch02.html) and [Definition 3.1.1 / Proposition 3.1.8](https://www.math.ucla.edu/~sharifi/notes/topology-ch03.html). The author's source record accurately discloses that access limitation. No uninspected topology source pages are claimed.

The complete author check code has substantive exact algebra, derivative identities, finite schedules, crossings, convex-hull and affine-dependence certificates, frame reversals, geometric puncture models and wet-path checks. Its rational frame tests supplement the symbolic all-angle proof; its graph subdivisions retain edge interiors; floating mirror checks are explicitly only supplemental. I found no implementation defect in those audits. Running it passed all eight groups and confirmed 25 pages, 50 keyed prompts and eight solved extensions. The independently derived proofs recorded above remain the release evidence for universal claims.

No open findings. Preserve explicit gates, answer timing and the exact figure conventions through production. Classroom outcomes remain unpiloted.
