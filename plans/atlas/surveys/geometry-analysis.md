# Geometry, topology, and analysis: breadth survey

Prepared 25 September 2026. This is a **research-screening document**, not a collection of reviewed lessons. It covers the 27 assigned MSC2020 top-level fields individually. Three or four anchors per field establish useful starting territory; they do not exhaust the field or confer dispositions on its descendant codes. Proposed entrances are design inferences, with no classroom evidence claimed. The advisory `math_circle_atlas_plan.md`, project README, current fall plan, and Weeks 2–10 mathematical redesign were consulted.

The survey deliberately includes mathematics whose first satisfactory entrance requires calculus, linear algebra, or university analysis. Lowering every topic would damage the map. Conversely, continuous motion, comparison, and geometric arguments sometimes provide genuine access before numerical calculation does. **Physical measurement suggests a conjecture; an idealized model and argument establish a theorem.** An apparent crossing in a graph, a measured right angle, or one successful soap film does not resolve the corresponding universal claim.

Access descriptions below are capability gates, not age placement. “Entry” means meaningful work on the stated small world; it does not imply readiness to prove its adult generalization. Unless otherwise specified, materials are paper, string, movable markers, transparent overlays, or a simple graphing interface. Sources are authored mathematical texts, institutional lecture notes, or the NIST reference; locators identify what was inspected. Calculations explicitly called “small exact examples” are independently specified here, rather than borrowed lesson designs.

## 22 — Topological groups, Lie groups

**What distinguishes the field.** Symmetry has continuous parameters, local geometry, and infinitesimal generators. Classifying finite permutations alone misses this territory.

**Anchors.** (1) Plane rotations about one fixed center obey `R(a)R(b)=R(a+b)` for all real angles; the parameter is taken modulo a full turn. (2) Rotations about different axes in three dimensions generally do not commute: quarter-turns about the x- and y-axes already distinguish the two orders. (3) For real skew-symmetric matrices A, `exp(tA)` is orthogonal with determinant one; differentiation recovers the generator. (4) Unit quaternions act on imaginary quaternions by conjugation, giving the two-to-one map onto SO(3), with kernel `{1,−1}`. [Woit, *Quantum Theory, Groups and Representations*, chapters 4–6](https://www.math.columbia.edu/~woit/QMbook/qmbook-latest.pdf).

**Entrances and stops.** Rotate an arrow continuously, combine chosen turns, and ask whether order matters. Then manipulate a marked box using two specified axes. This is an exact action of rotations, requiring orientation tracking but no reading beyond instructions. Matrix exponentials stop at linear algebra plus convergent power series; the covering-space claim stops at topology. A belt demonstration is motivation until its allowed deformations are modeled precisely.

**Trap/frontier.** A finite set of quarter-turns does not exhibit Lie algebra or local topology. Retain representation theory, noncompact groups, and harmonic analysis on groups as separate later searches. Week 3 permutations are a useful contrast, not coverage of this field.

## 26 — Real functions

**Distinguishing mathematics.** Completeness, continuity, differentiability, and controlled limits turn pictures of change into existence and impossibility arguments.

**Anchors.** (1) A continuous real function on `[a,b]` assumes every value between its endpoint values. (2) Such a function attains its maximum and minimum. (3) If continuous on `[a,b]` and differentiable on `(a,b)`, it has a point where instantaneous slope equals the secant slope. (4) Continuous functions can converge pointwise to a discontinuous function: `x^n` on `[0,1]`; uniform convergence would preserve continuity. [Lebl, *Basic Analysis I*, §§3.3, 4.2, 6.1–6.2](https://www.jirka.org/ra/realanal.pdf).

**Entrances and stops.** Two markers exchange which is higher while moving without jumps; explain why equality is unavoidable. Give a continuous periodic fence profile and compare opposite points: after half a turn their height difference changes sign. This is an exact continuous special case, not an exercise about six isolated posts. Numerical bisection adds fractions and gives an interval-width guarantee. Moving averages and speed stories introduce slopes, but the mean-value theorem stops at a derivative concept.

**Trap/frontier.** “No pencil lifting” is an unreliable definition of continuity, and a steep continuous ramp is not a jump. Keep nowhere-differentiable functions, bounded variation, generalized derivatives, and multivariable inequalities on the frontier.

## 28 — Measure and integration

**Distinguishing mathematics.** Size is assigned consistently to sets, and integrals survive suitable limiting operations; counting points and measuring length can disagree spectacularly.

**Anchors.** (1) A countable subset of the real line has Lebesgue measure zero: cover its nth point by an interval of length at most `ε/2^n`. (2) The middle-thirds Cantor set is uncountable but has length zero; its nth cover has length `(2/3)^n`. (3) For measurable `0≤f_n↑f`, integrals increase to the integral of f, allowing infinity. (4) For measurable f_n with a fixed integrable bound `|f_n|≤g`, almost-everywhere convergence permits exchanging integral and limit. [Axler, *Measure, Integration & Real Analysis*, §§2A, 2D, 3A–3B](https://measure.axler.net/MIRA.pdf).

**Entrances and stops.** Cover finitely many named points with arbitrarily short paper strips, then design a rule covering a listed infinity. Repeated cutouts introduce nested sets; fractions and infinite series support the zero-length argument, while a separate binary-sequence argument establishes uncountability. This is a strong secondary-level entrance; younger finite constructions are preparation.

**Trap/frontier.** Finite dust still has positive paper area; small pixels are not points. A zero-area object need not be empty. No finite cutting activity proves nonmeasurability. Product measures, Hausdorff measure/dimension, differentiation of measures, and nonmeasurable sets need separate searches.

## 30 — Functions of a complex variable

**Distinguishing mathematics.** Complex differentiability imposes rigidity: local behavior can determine a whole function, while contour geometry controls zeros and integrals.

**Anchors.** (1) Multiplication by nonzero `re^{iθ}` scales all lengths by r and rotates all angles by θ. (2) A nonconstant holomorphic function on a connected open set has no interior local maximum of its modulus. (3) For a function holomorphic on a neighborhood of a closed Jordan region, with no zeros on its positively oriented boundary, the change in argument counts enclosed zeros with multiplicity. (4) `z↦z²` doubles argument and squares modulus, so a full target circuit exchanges the two square-root branches. [Lebl, *Guide to Cultivating Complex Analysis*, §§1.2, 3.3, 5.1 and chapter 10](https://www.jirka.org/ca/ca.pdf).

**Entrances and stops.** Rotating and stretching arrows gives an exact model of multiplication. Track a two-valued square root around a circle with two colored moving markers; algebra and angle doubling suffice for that special case. Contour integrals and the general argument principle stop at complex differentiation/integration.

**Trap/frontier.** Pretty complex-plane coloring does not establish holomorphicity, and angle preservation excludes points where the derivative vanishes. Riemann surfaces, analytic continuation, conformal mapping, and value distribution remain distinct territory.

## 31 — Potential theory

**Distinguishing mathematics.** Interior values are governed by boundary data and averaging, connecting equilibrium, harmonicity, and energy.

**Anchors.** (1) A C² harmonic function has its center value equal to its average over every contained sphere or ball. (2) A continuous function with this local mean-value property is smooth and harmonic. (3) On a bounded connected domain, a harmonic function continuous on the closure cannot exceed its boundary maximum; an interior maximum forces constancy. These hypotheses and the reverse direction are inspected in [Hunter, *Notes on PDE*, §§2.1 and 2.3, Theorems 2.1–2.2](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf). (4) A small exact discrete counterpart: on a finite connected graph with nonempty fixed boundary, interior vertices equal to their neighbor averages have at most one solution, because a positive difference maximum propagates to the boundary.

**Entrances and stops.** Invent number landscapes satisfying the averaging rule; ask whether an isolated peak is possible. Four-neighbor graph models require addition and division. A continuous rubber-sheet or temperature picture is an analogy unless the governing PDE and boundary assumptions are justified. Real harmonic examples `x`, `x²−y²`, and `log r` away from zero require elementary differentiation.

**Trap/frontier.** Graph harmonicity is exact mathematics but does not prove convergence to a continuum solution. Capacity, Green functions, fine topology, and nonlinear potential theory retain hard analysis gates.

## 32 — Several complex variables and analytic spaces

**Distinguishing mathematics.** Multiple complex coordinates produce phenomena absent in one variable; they are not just two simultaneous complex drawings.

**Anchors.** (1) For `n≥2`, if U is a domain in Cⁿ, K is compact in U, and `U\K` is connected, every holomorphic function on `U\K` extends holomorphically to U (Hartogs). (2) The unit ball and unit bidisc in C² are not biholomorphic. (3) A nonempty zero set of a holomorphic scalar function on a domain in Cⁿ, `n≥2`, cannot be compact. [Lebl, *Tasty Bits of Several Complex Variables*, Theorem 4.3.1, Corollary 4.3.2, §1.4/Theorem 1.4.4](https://www.jirka.org/scv/scv.pdf).

**Entrances and stops.** Compare `1/z` on a punctured plane with the impossibility of an isolated holomorphic pole in a punctured ball in C². A meaningful investigation can start with polynomial examples such as the zero set of `zw`, then ask which one-variable intuitions survive. Polynomial algebra permits examples, but these distinguishing extension results need one-variable complex analysis and multivariable reasoning. **No elementary bridge established.**

**Trap/frontier.** Filling a physical hole is not Hartogs extension. Slicing a four-real-dimensional space into pictures may hide compatibility conditions. Pseudoconvexity, the ∂̄ problem, sheaves, singularities, and analytic spaces deserve their own advanced dossiers.

## 33 — Special functions

**Distinguishing mathematics.** Recurrences, differential equations, integral representations, and symmetries organize functions that recur throughout mathematical physics and geometry.

**Anchors.** (1) Chebyshev polynomials satisfy `T_n(cos θ)=cos(nθ)`, with `T_0=1`, `T_1=x`, and `T_(n+1)=2xT_n−T_(n−1)`. (2) The gamma function extends factorial values: for positive real x, `Γ(x+1)=xΓ(x)` and `Γ(1)=1`. (3) Bessel's equation `x²y''+xy'+(x²−ν²)y=0` supplies radial modes for circular geometry, rather than ordinary sine waves. Exact references: [NIST DLMF 18.5.1 and §18.9](https://dlmf.nist.gov/18.5), [5.5.1](https://dlmf.nist.gov/5.5), [10.2.1](https://dlmf.nist.gov/10.2).

**Entrances and stops.** Use angle-doubling circles to discover `T_2=2x²−1`, then obtain higher polynomials in two ways. This requires coordinates/algebra; a gear drawing alone gives only motivation. Compare candidate “factorial between integers” rules to see why a recurrence does not determine a unique interpolation. Gamma's integral and Bessel's equation stop at calculus; drumhead mode proofs need PDE.

**Trap/frontier.** Naming a curve after a special function is not investigating its mechanism. Orthogonality, asymptotics, hypergeometric transformations, and elliptic functions remain separate families.

## 34 — Ordinary differential equations

**Distinguishing mathematics.** A local rate law can determine an entire trajectory, but existence, uniqueness, and long-time survival are different questions.

**Anchors.** (1) A continuous vector field locally Lipschitz in the dependent variable gives a unique local initial-value solution. [Teschl, *Ordinary Differential Equations and Dynamical Systems*, §2.2, Theorem 2.2](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf). Small exact examples: (2) `y'=y², y(0)=1` has `y=1/(1−t)` only up to its finite blow-up time. (3) `y'=2√y, y(0)=0`, restricted to nonnegative y and forward time, permits waiting until any c≥0 then taking `y=(t−c)²`. (4) `y'=y(1−y)` has equilibria 0 and 1, with upward motion between them and downward motion above 1.

**Entrances and stops.** Place direction arrows along a number line and predict trajectories before solving formulas. Rate comparisons and signed numbers support qualitative reasoning; checking formulas requires derivatives. The waiting solution provides a surprising calculus-level investigation with an explicit failure of the uniqueness hypothesis.

**Trap/frontier.** Connecting Euler-method dots gives an approximation, not the solution; small steps can still distort stability. Systems, bifurcation, Sturm–Liouville theory, boundary-value problems, and stiff equations require further work.

## 35 — Partial differential equations

**Distinguishing mathematics.** Change depends on several independent variables; different equations propagate information in fundamentally different ways.

**Anchors.** (1) For C² profiles F and G, `u(x,t)=F(x−ct)+G(x+ct)` solves the one-dimensional wave equation `u_tt=c²u_xx`. (2) On `[0,π]`, `u=e^(−t)sin x` solves `u_t=u_xx` with zero endpoint values, retaining its shape while decaying. (3) A small exact Burgers example: `u(x,t)=−x/(1−t)` solves `u_t+uu_x=0` for t<1 with initial profile `u(x,0)=−x`; characteristics `x(t)=ξ(1−t)` collide at t=1. (4) The harmonic maximum principle provides uniqueness for continuous Dirichlet data whenever a sufficiently regular solution exists. [Hunter, *Notes on PDE*, §§2.3, 5.1, and 7.1; the displayed Burgers example is checked directly by differentiation](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).

**Entrances and stops.** Slide two drawn wave profiles past one another and add heights; this preserves exact solutions when the profiles are smooth. Compare the wave and heat examples using calculus. Traffic trajectories introduce characteristic crossing with coordinate geometry, but choosing physically meaningful weak solutions needs additional analysis.

**Trap/frontier.** “Everything spreads out” conflates waves, diffusion, and transport. A classroom token-sharing rule is a discrete model, not automatically a heat equation. Nonlinear regularity, shocks, distributions, and multidimensional PDE remain large open design territory.

## 37 — Dynamical systems and ergodic theory

**Distinguishing mathematics.** Repeated evolution produces orbits, invariant sets, stability, recurrence, and statistical behavior; unpredictability can coexist with exact rules.

**Anchors.** (1) Circle rotation by a rational fraction of a turn is periodic; an irrational rotation has dense orbits. (2) For `f_r(x)=rx(1−x)`, the fixed point `1−1/r` is locally attracting for `1<r<3`, since its derivative is `2−r`. (3) The tent map `T(x)=2x` below 1/2 and `2−2x` above it stretches intervals and folds them; finite itineraries can be built by inverse branches. (4) A probability-preserving transformation on a finite measure space returns almost every point of a measurable set to it infinitely often. For iteration, symbolic dynamics, and attractors, see [Teschl, chapter 11, especially §§11.3–11.5](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf); recurrence is an advanced frontier anchor requiring a dedicated proof source before lesson production.

**Entrances and stops.** Iteration games and cobweb plots require following a rule; rational arithmetic supports exact orbit certificates. Irrational density needs an infinite argument. Ergodic conclusions stop at measure theory.

**Trap/frontier.** A long nonrepeating decimal simulation proves neither irrationality nor chaos. Do not label all nonlinear iteration chaotic. Week 4 modular orbits and Week 9 billiards are prior overlaps; invariant measures and continuous flows provide genuinely new questions.

## 39 — Difference and functional equations

**Distinguishing mathematics.** Global rules constrain sequences or entire functions, often leaving freedom that sample values conceal.

**Anchors.** Small exact examples: (1) Every solution on nonnegative integers of `a_(n+2)−2a_(n+1)+a_n=0` is `a_n=A+Bn`. (2) For `a_(n+1)=ra_n+b`, subtracting a fixed point reduces the problem to a geometric sequence when `r≠1`. (3) Additivity `f(x+y)=f(x)+f(y)` on Q forces `f(q)=qf(1)`. On R this conclusion follows with continuity at one point, but fails without suitable regularity. (4) A continuous positive function satisfying `f(x+y)=f(x)f(y)` on R is exponential. The regularity problem is discussed in [Reem, *Remarks on the Cauchy functional equation and variations of it*, introduction and §2](https://arxiv.org/pdf/1002.3721).

**Entrances and stops.** Let children invent machines obeying “combine inputs, add outputs,” then predict untested values and explain necessity. Whole-number versions need only addition; rational extension needs division. Distinguishing rational from real conclusions needs continuity and infinite reasoning.

**Trap/frontier.** Agreement on a finite table does not establish an equation for every input. Uniqueness requires a domain and regularity assumptions. Nonlinear recurrences, delay equations, and stability of approximate functional equations remain separate searches.

## 40 — Sequences, series, summability

**Distinguishing mathematics.** Infinite addition has rules that finite arithmetic cannot safely supply; summation procedures differ from ordinary convergence.

**Anchors.** Small exact examples: (1) `1+1/2+1/4+…=2`, because the partial-sum remainder is an explicit power of 1/2. (2) The harmonic series diverges by grouping blocks whose sum is at least 1/2. (3) The ordinary partial sums of `1−1+1−1+…` alternate, but their arithmetic means tend to 1/2. (4) Every convergent sequence has arithmetic means converging to the same limit; the converse fails. General series rules and convergence hypotheses: [Lebl, *Basic Analysis I*, §§2.5–2.6](https://www.jirka.org/ra/realanal.pdf). Fourier summability gives a distinct application in [Stroock, *Topics in Fourier Analysis*, §5](https://ocw.mit.edu/courses/res-18-015-topics-in-fourier-analysis-spring-2024/mitres_18_015_s24_full_lec.pdf).

**Entrances and stops.** Build area dissections, accumulate strips, and compete to exceed a target using harmonic terms. Fractions and grouping support exact proofs. Ask what an averaging rule measures before calling its output a “sum.”

**Trap/frontier.** A bounded sequence need not converge; terms tending to zero are necessary but insufficient for convergence of a series. Never use regularized sums as ordinary sums. Conditional rearrangements, Tauberian conditions, and summability matrices need dedicated later dossiers.

## 41 — Approximation and expansions

**Distinguishing mathematics.** An approximation is judged by a specified error, domain, and class of allowable approximants; matching many sample points is only one possible objective.

**Anchors.** (1) For continuous real f on a compact nondegenerate interval, there is a unique best uniform approximating polynomial of degree at most n. Alternating maximal error at n+2 ordered points certifies optimality. [NIST DLMF §3.11(i)](https://dlmf.nist.gov/3.11). Small exact examples: (2) The best constant approximation to `x²` on `[-1,1]` is 1/2, error 1/2: values at 0 and 1 force that lower bound. (3) The best uniform affine approximation to `x²` is also 1/2, by symmetry and the same bound. (4) Linear interpolation of a C² function on an interval of length h has error at most `h² sup|f''|/8`.

**Entrances and stops.** Move a horizontal strip until a drawn curve fits in the narrowest strip; then justify endpoints forcing the answer. This needs comparison before numbers. Secondary learners compare worst error with squared error, then build counterexamples where more interpolation points make behavior worse.

**Trap/frontier.** “Looks close” is not an error certificate. Numerical point samples can miss peaks between them. General interpolation bounds require calculus; approximation in function spaces, rational approximation, splines, and wavelets deserve distinct attention.

## 42 — Harmonic analysis on Euclidean spaces

**Distinguishing mathematics.** Decomposing functions into oscillations reveals scale, cancellation, regularity, and uncertainty.

**Anchors.** (1) Integer-frequency complex exponentials are orthogonal on a full unit period. (2) For integrable functions on the circle, Fourier coefficients of their circular convolution multiply. (3) Fejér means of a continuous periodic function converge uniformly to that function, even when ordinary partial sums are not the appropriate convergence method. (4) Two continuous oscillations whose frequencies differ by an integer multiple of the sampling rate give the same equally spaced samples. Orthogonality, convolution, and Fejér's positive averaging kernel: [Stroock, *Topics in Fourier Analysis*, §§1–5, especially formula (5.1)](https://ocw.mit.edu/courses/res-18-015-topics-in-fourier-analysis-spring-2024/mitres_18_015_s24_full_lec.pdf).

**Entrances and stops.** Combine rotating arrows and draw their height; change amplitude and phase to match a target. Sample a turning wheel with a fixed strobe and exhibit aliasing exactly through angle arithmetic. Trigonometry supports finite sums; infinite reconstruction and convergence require integration and analysis.

**Trap/frontier.** A finite DFT exactly recovers a finite vector, not every continuous signal compatible with it. Sound demonstrations motivate but do not prove Fourier completeness. Singular integrals, maximal functions, restriction, and time-frequency analysis must not disappear behind a music activity.

## 43 — Abstract harmonic analysis

**Distinguishing mathematics.** Frequencies are characters or representations of an underlying group; the group's structure determines the transform.

**Anchors.** (1) For a finite abelian group, its complex characters form an orthogonal basis of functions on the group, with normalized counting inner product. (2) Translation becomes multiplication by character values under Fourier transformation. (3) On `(Z/2Z)^n`, characters are sign patterns `(-1)^(a·x)`, producing the Walsh transform. (4) For the circle group, continuous characters are `z↦z^n`, indexed by integers, so the dual is discrete rather than another circle. [Dandavati, *The Fourier Transform on Finite Groups: Theory and Computation*, §3, Theorems 3.5–3.8 and Remark 3.7](https://math.uchicago.edu/~may/REU2018/REUPapers/Dandavati.pdf).

**Entrances and stops.** Four signed cards can encode a four-entry brightness pattern as average, left-right, top-bottom, and checkerboard components. Children choose a pattern to hide and reconstruct. Signed addition and halves give an exact finite case. Characters require groups and complex numbers; Haar integration and nonabelian representation theory are hard stops.

**Trap/frontier.** Fourier-on-four-cards overlaps linear algebra and Week 2 toggles but contributes a new question only if translation, decomposition, or reconstruction is investigated. It does not review locally compact groups, amenability, or noncommutative harmonic analysis.

## 44 — Integral transforms, operational calculus

**Distinguishing mathematics.** Transforming a function can turn evolution or convolution into algebra, but inversion depends on information and analytic conditions.

**Anchors.** (1) For piecewise continuous functions of exponential order, one-sided Laplace transforms exist in a suitable right half-plane. (2) With appropriate differentiability and exponential bounds, `L(f')=sL(f)−f(0)`. (3) Causal convolution transforms into multiplication where the integrals converge absolutely. These rules and regions of convergence are explicit in [Boyd, EE102 Lecture 3, slides 3–2 through 3–7 and 3–27 through 3–29](https://web.stanford.edu/class/ee102k/laplace.pdf). Small exact example: (4) Convolving two unit interval indicator functions produces a triangular tent supported on `[0,2]`.

**Entrances and stops.** Slide two paper intervals past one another and record overlap length against displacement. This is a literal convolution integral and needs only length comparison for entry; derive the piecewise formula with coordinates. An impulse-response “echo machine” with finite sums is a discrete analogue. Laplace solving of ODEs stops at integration plus algebra.

**Trap/frontier.** Transform tables hide domains; an algebraic formula without its region of convergence can be ambiguous. A finite collection of shadows does not automatically determine an object. Radon/Mellin transforms, inverse problems, and distributional operational calculus need further scouting.

## 45 — Integral equations

**Distinguishing mathematics.** The unknown function appears inside an averaging or accumulation operator; some kernels reduce an infinite-dimensional question to finitely many unknown moments.

**Anchors.** Small exact examples on `[0,1]`: (1) `u(x)=1+λ∫u(t)dt` has constant solution `1/(1−λ)` for λ≠1 and no solution for λ=1. (2) `u(x)=λ∫u(t)dt` has only zero for λ≠1 and every constant for λ=1. (3) `u(x)=1+∫_0^x u(t)dt` gives `u=e^x`; differentiating is justified once u is continuous. (4) For compact K on a Hilbert space, `I+K` is invertible exactly when its nullspace is zero; otherwise solvability requires orthogonality to the adjoint nullspace. [O'Neil, *Integral Equations and Fast Algorithms*, Fredholm Alternative, Theorem 3, printed p.54](https://cims.nyu.edu/~oneil/courses/fa17-math2011/int_eq_notes_2017.pdf).

**Entrances and stops.** Use “your value equals a gift plus a fraction of the group's mean” puzzles, then replace finitely many participants by a continuous interval. The first three examples remain genuine calculus-level tasks; the finite group version is explicitly a matrix model.

**Trap/frontier.** A Riemann sum creates an approximate equation, potentially with different stability. No elementary realization of general Fredholm theory is claimed. Singular kernels, ill-posed first-kind equations, and boundary integral methods remain open searches.

## 46 — Functional analysis

**Distinguishing mathematics.** Functions become points in spaces; geometry and completeness govern approximation, continuity, and existence.

**Anchors.** (1) A nonempty closed convex subset of a Hilbert space has a unique nearest point to each point of the ambient space. (2) Projection onto a closed linear subspace is characterized by orthogonality of the residual. (3) A contraction of a nonempty complete metric space has a unique fixed point; successive approximations converge geometrically. (4) A bounded linear functional on a Hilbert space is inner product with one unique vector. [Axler, *Measure, Integration & Real Analysis*, chapter 8, especially closed subspaces and Riesz representation](https://measure.axler.net/MIRA.pdf); [Lebl, *Basic Analysis I*, §7.6](https://www.jirka.org/ra/realanal.pdf).

**Entrances and stops.** Find a closest point on a line using string and a right-angle argument; then compare “distance between graphs” measured by maximum discrepancy or integrated squared discrepancy. The first is a finite-dimensional exact special case. Infinite-dimensional geometry needs norms, completeness, and often integration.

**Trap/frontier.** Changing the norm can change the best answer and destroy uniqueness. Closed bounded sets are not generally compact in infinite dimensions. Banach-space duality, weak topology, distributions, and locally convex spaces need separate mechanisms; one closest-point activity cannot represent them all.

## 47 — Operator theory

**Distinguishing mathematics.** Study transformations of whole function spaces, including spectra, invertibility, compactness, and long-term repeated action.

**Anchors.** (1) Compact normal operators on complex Hilbert spaces have orthonormal eigenvector bases. [Axler, *Measure, Integration & Real Analysis*, Theorem 10.107](https://measure.axler.net/MIRA.pdf). Small exact contrasts: (2) The right shift on `ℓ²`, `(a_0,a_1,…)↦(0,a_0,a_1,…)`, preserves norm but is not onto. (3) Differentiation on polynomials is linear but unbounded in the sup norm on `[0,1]`, since `||x^n||∞=1` and `||(x^n)'||∞=n`. (4) If bounded T has operator norm below one, the geometric operator series gives `(I−T)⁻¹=ΣT^n`.

**Entrances and stops.** Explore a finite “blur machine,” ask which brightness patterns keep their shape, then predict repeated blurring from eigenvectors. Signed arithmetic starts a matrix special case. The shift and unbounded-derivative contrasts need infinite sequences/calculus and should retain those gates.

**Trap/frontier.** Every finite matrix has finite-dimensional spectral behavior; it cannot demonstrate continuous spectrum. Not every operator is diagonalizable. Operator algebras, non-self-adjoint spectra, semigroups, and unbounded operator domains remain explicitly unbridged.

## 49 — Calculus of variations and optimal control

**Distinguishing mathematics.** The unknown is a curve, function, or control schedule, and stationarity is weaker than global optimality.

**Anchors.** (1) For a sufficiently smooth integrand L and C² extremizer with fixed endpoints, first variation yields `d/dx L_(y')=L_y`; this is necessary, not sufficient. (2) The shortest rectifiable Euclidean path between two points is the segment, by the triangle inequality. (3) A frictionless bead released from rest under uniform gravity leads to the brachistochrone time integral; its Euler–Lagrange extremals are cycloidal arcs with appropriate endpoints. [UCL MATH0043, §2, “The Brachistochrone”](https://www.homepages.ucl.ac.uk/~ucahmto/latex_html/pandoc_chapter2.html). (4) A small control problem: for `x'=u`, `|u|≤1`, moving from 0 to a>0 takes at least a time units, achieved by u=1 almost everywhere.

**Entrances and stops.** Design paths of string with specified obstacles; distinguish shortest, fastest, and least bending. Children can compare candidate tracks, but a race is experimental evidence under a physical model. The time-integral investigation begins at calculus; global sufficiency and general control theory require more.

**Trap/frontier.** Soap films can be trapped in local minima. Euler–Lagrange equations do not certify that any solution minimizes. Relaxation, existence of minimizers, constraints, and Pontryagin's principle require further advanced surveys.

## 51 — Geometry

**Distinguishing mathematics.** Axioms, distance, incidence, and transformations generate different geometries; a familiar drawing may support incompatible structures.

**Anchors.** (1) For endpoints in the same open half-plane, reflecting one endpoint across a straight mirror converts the shortest one-bounce Euclidean path to a straight segment, provided its crossing lies in the allowed mirror segment. (2) In a Euclidean triangle the angles sum to π; in a hyperbolic triangle the sum is strictly smaller. (3) Circle inversion sends circles or lines to circles or lines, with a circle through the inversion center becoming a line. (4) A Euclidean composition of two reflections in intersecting lines is a rotation by twice their directed angle. [Petrunin, *Euclidean Plane and Its Relatives*, §§5D, 7C, 10B, 11B–C, and 13D](https://arxiv.org/pdf/1302.1630).

**Entrances and stops.** Plan mirror routes, turn folded paper twice, or compare straight travel on several supplied geometric models. Reflection proofs use congruence; inversion needs ratios and coordinates. Hyperbolic-model claims need definitions of distance and straightness, not merely bowed grid lines.

**Trap/frontier.** Week 9 already uses billiard unfolding; new mirror work must introduce a new constraint or optimization question. Do not confuse projective incidence with Euclidean lengths. Finite geometries, projective duality, constructibility, and buildings warrant separate activity searches.

## 52 — Convex and discrete geometry

**Distinguishing mathematics.** Global shape and intersection structure can be forced by a few points or small subfamilies.

**Anchors.** (1) Any d+2 points in Rᵈ admit a partition into two nonempty parts with intersecting convex hulls (Radon). (2) If every d+1 members of a finite family of at least d+1 convex sets in Rᵈ intersect, all members intersect (Helly). (3) Every point in a convex hull in Rᵈ is a convex combination of at most d+1 original points (Carathéodory). (4) Disjoint compact convex sets can be strictly separated by a hyperplane. [Hug and Weil, *A Course on Convex Geometry*, §§1.2 and 1.4; Theorems 1.2.1–1.2.4](https://users.fmf.uni-lj.si/lavric/hug%26weil.pdf).

**Entrances and stops.** Place four pegs in the plane and split them into two colors so their stretched-rubber-band hulls meet. Collinear and interior-point cases must be included. A Helly puzzle can use transparent convex windows; deliberately allow a nonconvex window to test the assumption. Drawing and inclusion suffice to enter; general d-dimensional arguments need linear dependence.

**Trap/frontier.** Pairwise intersections do not suffice in the plane. Existing tilings cover a different part of discrete geometry. Packing density, polytopes, oriented matroids, rigidity, and geometric discrepancy remain substantial territory.

## 53 — Differential geometry

**Distinguishing mathematics.** Curvature, intrinsic distance, and transport connect local measurements to global shape without requiring an external view.

**Anchors.** (1) A circle of radius r has curvature `1/r`; bending a plane into a cylinder preserves intrinsic distances locally but changes its extrinsic appearance. (2) Nonantipodal points on a round sphere have a unique shortest great-circle arc. (3) A convex geodesic triangle on the unit sphere contained in an open hemisphere, has area equal to its angle sum minus π. (4) Parallel transport around such a triangle rotates a tangent direction by its signed spherical area modulo 2π. [Petrunin and Zamora Barrera, *What Is Differential Geometry?*, chapters 14–18, especially 16 and 17C](https://arxiv.org/pdf/2012.11814).

**Entrances and stops.** Carry an arrow north from the equator, turn along a second meridian, and return along the equator; the octant triangle supplies an exact right-angle example. Compare shortest paths on a cylinder by unrolling it. Movement and angle tracking provide access; general curvature and transport equations stop at multivariable calculus.

**Trap/frontier.** “Walk straight” needs a defined transport rule. Great circles are locally straight, but sufficiently long arcs are not globally shortest. General relativity, symplectic/contact geometry, and comparison geometry require further branches.

## 54 — General topology

**Distinguishing mathematics.** Continuity, convergence, separation, connectedness, and compactness are studied independently of a particular metric or embedding.

**Anchors.** (1) A continuous image of a connected space is connected. (2) A continuous image of a compact space is compact. (3) A continuous bijection from compact X to Hausdorff Y has continuous inverse. (4) The closure of `{(x,sin(1/x)):0<x≤1}` is connected but not path connected. [Sharifi, *Point-Set Topology*, chapter 3, especially Proposition 3.1.8 and connected/compact-space sections](https://www.math.ucla.edu/~sharifi/notes/topology-ch03.html).

**Entrances and stops.** Compare a loop and a segment by removing a chosen point and counting pieces; specify the objects as topological spaces, not pencil traces with accidental crossings. A coverage game on `[0,1]` can contrast finite subcovers with the family of intervals covering `(0,1)` but approaching an omitted endpoint. Elementary examples use continuous deformation and logic; general topology needs quantified definitions.

**Trap/frontier.** The phrase “rubber-sheet geometry” omits most topology. A continuously traced curve is path connected; that does not characterize connectedness. Finite grids cannot reproduce the sine-curve counterexample. Separation axioms, product topology, dimension, and nonmetrizable spaces remain advanced searches.

## 55 — Algebraic topology

**Distinguishing mathematics.** Algebraic invariants turn deformation and obstruction questions into computable evidence.

**Anchors.** (1) Loops in a circle based at one point have an integer winding number; concatenation adds it. (2) A connected finite graph with V vertices and E edges has E−V+1 independent cycles. (3) The alternating cell count of a finite CW complex equals the alternating ranks of its homology groups. (4) Every continuous map `S²→R²` identifies an antipodal pair; the `S¹→R` case follows from the intermediate value theorem. [Hatcher, *Algebraic Topology*, §1.1, Theorem 1.10, §2.2/Theorem 2.44, and §2.B](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).

**Entrances and stops.** Wind strings around a forbidden peg with a fixed basepoint, or add corridors to a connected network and predict independent loops. Removing edges of a spanning tree gives a concrete graph proof. The equal-height circle is a genuine continuous entrance. Homology groups and higher-dimensional obstructions need algebra and topology.

**Trap/frontier.** Counting visible holes is ambiguous unless dimension and space are fixed. Equal Euler characteristic does not imply homeomorphism. Week 1's configuration graph is an overlap, but its connectivity alone does not establish homology of a richer configuration space.

## 57 — Manifolds and cell complexes

**Distinguishing mathematics.** Local Euclidean structure coexists with global gluing, knots, orientation, and high-dimensional phenomena.

**Anchors.** (1) Connected compact surfaces without boundary are classified by orientability and genus: sphere with g handles, or sphere with k crosscaps. [Sahoo, *Surfaces*, §8, classification theorem/corollary, pp.17–19](https://e.math.cornell.edu/people/Nikhil_Sahoo/files/math-circles/surfaces.pdf). (2) Reidemeister moves preserve the number of Fox 3-colorings of a knot diagram; a nonconstant trefoil coloring distinguishes it from the unknot. (3) A Möbius band has one boundary component and reverses transverse orientation along its central loop; an annulus has two boundary components and preserves orientation. Knot invariance is developed in [Kauffman, *Knots*, “Three Colored Trefoil,” Figures 12–14 and accompanying theorem](https://homepages.math.uic.edu/~kauffman/Tots/Knots).

**Entrances and stops.** Glue marked strips, trace edges before cutting, and color knot diagrams while checking local moves. Reading can be minimal; consistency checking is substantive. Classification proofs require gluing words and systematic reduction. Smooth structures, surgery, and high-dimensional manifolds retain university prerequisites.

**Trap/frontier.** Cutting changes the space and is not a homeomorphism. A physical Klein-bottle model necessarily self-intersects in three-space; that crossing is not intrinsic. Failure of a chosen coloring test does not prove a knot unknotted.

## 58 — Global analysis, analysis on manifolds

**Distinguishing mathematics.** Differential equations, critical points, and differential operators interact with the global topology of a manifold.

**Anchors.** (1) Near a nondegenerate critical point of a smooth real function, local coordinates make the function a constant plus a sum of positive and negative squares (Morse lemma). (2) A smooth map from a compact manifold slab to `[a,b]`, with boundary at the endpoints and no critical points, has diffeomorphic level surfaces throughout. (3) Crossing one nondegenerate critical point of index k changes the sublevel homotopy type by attaching a k-cell, under compactness and isolated-critical-value hypotheses. [Gillespie, *Morse Theory Notes*, Lemma 1.12, Theorem 2.9, §3](https://web.math.utk.edu/~afreire/teaching/m663f21/Morse_Theory_Notes.pdf).

**Entrances and stops.** Raise an imaginary waterline through a clay landscape, recording component births, merges, and holes. For a deliberately specified smooth surface, this is a model of sublevel topology. Derive and classify critical points of `x²+y²` and `x²−y²` with calculus; the general Morse correspondence needs manifolds and topology. A triangulated landscape is a separate piecewise-linear model.

**Trap/frontier.** A contour drawing does not verify smoothness, nondegeneracy, or absence of hidden critical points. Morse theory is one entrance, not all global analysis. Elliptic operators, heat kernels, index theory, and infinite-dimensional manifolds remain prerequisite-blocked/unresolved.

## Editorial decisions and next survey frontier

The most promising new low-prerequisite work is concentrated in **continuous comparison, convexity, transformations, intrinsic geometry, and topological obstruction**. Prioritize the equal-height antipodes, four-point Radon split, one-bounce shortest path with a constrained mirror, cylinder routes, octant parallel transport, convolution overlap, and knot-coloring invariance. Each supplies choices, counterexamples, and a proof question rather than a famous-name demonstration. These are candidates for design/review, not approved worksheets.

A second tranche should retain secondary-school gates: minimax fitting, functional-equation machines over Q versus R, ODE uniqueness failure, geometric versus harmonic accumulation, finite Fourier reconstruction and aliasing, and separable-kernel integral equations. They extend the library upward by mathematical prerequisites, without forcing calculus vocabulary into younger sessions.

The hard choices were to leave SCV without an elementary bridge; keep spectral and global-analysis theorems behind their real prerequisites; and label graph averaging, finite matrices, and triangulated landscapes according to the structure they actually realize. These restrictions protect the atlas from letting one attractive activity silently “cover” half of analysis.

Current weeks already provide tiling/reconfiguration (Week 1), finite linear transformations (Week 2), compositions (Week 3), discrete orbits (Week 4), and unfolding/periodicity (Week 9), plus networks (Week 10). Those are useful prerequisites and comparison cases. Reuse should introduce an additional invariant, changed space, limiting issue, or genuinely new optimization question; merely changing the story would not expand the child's mathematical experience. The current use log must still distinguish planned from taught instances.

Before leaf-level coverage is claimed, commission protected searches in geometric measure theory, real-variable harmonic analysis, functional/operator algebras, complex geometry, nonlinear PDE, ergodic theory, symplectic/contact geometry, topology beyond surfaces, and index theory. Also inspect the primary source and proof of Poincaré recurrence before turning its screening anchor into a family. This file establishes **27 screened top-level dossiers, 104 anchors, and an explicit frontier**; it establishes no exhaustive leaf audit, independent bridge review, or classroom validation.
