# Probability, computation, and applied mathematics: territory survey

Prepared 25 September 2026. Scope: MSC2020 fields **60, 62, 65, 68, 70, 74, 76, 78, 80, 81, 82, 83, 85, 86, 90, 91, 92, 93, 94, 97**: nineteen mathematical content fields and one education/support field. The pinned denominator is [taxonomy.json](../taxonomy.json), not a claim that the anchors below exhaust its descendants.

This is research screening with candidate bridges, before independent family review. Each numbered anchor is a distinct question worth designing around. The proposed entrances are our design inferences, not activities validated by their sources. The capability letters follow [DESIGN.md](../DESIGN.md); the prose specifies the actual requirement. “Stop” means retain the topic at that prerequisite, not replace its mathematics with a loosely related puzzle. Physical trials provide data; idealized models require separate arguments.

## 60 — Probability theory and stochastic processes

**Distinguishing questions.** What is predictable about an unpredictable path? How do conditioning, dependence, stopping, rare events, and scaling change an answer? Finite probability is a substantial entrance; it does not cover stochastic calculus or measure-theoretic probability.

1. **Conditioning changes the sample space.** In a finite model, conditional probabilities are ratios within the event learned. Compare drawing a colored counter, learning that it came from a particular bag, and learning information selected by a biased reporting rule. The information-generating procedure is part of the hypotheses.
2. **Gambler's ruin.** An independent fair nearest-neighbor walk on integers 0 through N, stopped at an endpoint, hits N with probability i/N from i. Harmonic averaging plus boundary values proves this; biased steps change the answer.
3. **Branching and extinction.** Independent identically distributed offspring counts give extinction probability equal to the smallest fixed point of their probability generating function on [0,1]. Mean offspring alone does not describe every generation; the deterministic one-child case is an important exception to careless critical-extinction slogans.
4. **Mixing versus cycling.** Finite irreducible aperiodic chains converge to their unique stationary distribution. Alternating deterministically between two states has a stationary distribution but no convergence from a single state.

**Entrance/gates.** O/C: walk counters and compare endpoint frequencies; F: probability trees and exact proportions; A/P: solve the averaging recurrence; L: transition matrices; D/I/X: diffusion limits, Brownian paths, martingales and stochastic integration. Do not suggest that a fair game guarantees a short play or that a large sample eliminates bias.

**Inspected source.** Grinstead–Snell, *Introduction to Probability*, CHANCE version, §§4.1, 10.2, 11.4, 12.2; contents and relevant random-walk text inspected. [Author-hosted text](https://math.dartmouth.edu/~prob/prob/prob.pdf). These locators are a source queue for the detailed family proof, not a claim that every exercise was checked.

## 62 — Statistics

**Distinguishing questions.** What can incomplete observations establish about an unknown population or mechanism, with what uncertainty and assumptions? This field needs its own designs; calculating dice probabilities is not statistical inference.

1. **Sampling distributions and estimator choice.** Repeated random samples produce different estimates. In independent sampling, an average can be unbiased while its uncertainty remains appreciable; a convenient or selectively observed sample need not be unbiased.
2. **Randomization tests.** Under a sharp no-treatment-effect null and the actual randomized assignment mechanism, enumerate treatment-label assignments and compare a prespecified statistic. The exact reference distribution comes from the design, not from “everything seems random.”
3. **Interval coverage.** A procedure's confidence level concerns its repeated-sampling coverage. Bootstrap samples draw with replacement from the empirical distribution; a bootstrap interval is not automatically exact, especially with tiny or unrepresentative samples.
4. **Association, confounding, prediction.** Compare a pooled relationship with the within-group relationships, or compare training fit with held-out prediction. More variables or a higher-degree curve can improve fit without improving prediction or supporting a causal conclusion.

**Entrance/gates.** O/C: secretly fill jars and let groups choose how to sample; record distributions of guesses. F: compare proportions and averages. A/P: define statistic, null, and assignment space; simulation can precede calculus. L/D: regression geometry and likelihood optimization. A low-threshold task must preserve an unknown target, observed evidence, and justified uncertainty. Avoid interpreting a p-value as the probability the null is true, or showing only a single attractive sample.

**Inspected sources.** Allen Downey, *Think Stats*, [ch. 8, Estimation](https://allendowney.github.io/ThinkStats/chap08.html), [ch. 9, Hypothesis Testing](https://allendowney.github.io/ThinkStats/chap09.html); OpenIntro, *Introduction to Modern Statistics*, [Foundations of inference, chapters 11–13](https://openintro-ims.netlify.app/foundations-of-inference.html). Exact finite designs are preferred for the first cards; population claims remain conditional on sampling.

## 65 — Numerical analysis

**Distinguishing questions.** When an exact formula is unavailable, how can an approximation be computed, certified, and kept stable? Distinguish sensitivity of the mathematical problem from error introduced by the algorithm.

1. **Bracketing versus tangent iteration.** Continuity and opposite endpoint signs guarantee a bisection root bracket; each step halves its width. Newton iteration additionally needs derivatives and suitable starting conditions for convergence. For f(x)=x³−2x+2, starting at zero produces 0→1→0 exactly.
2. **Conditioning versus residual.** A small equation residual need not mean a small solution error. In f(x)=εx−1 with ε positive and tiny, changing the right side slightly produces a large absolute change in x; scaling and relative error must be stated.
3. **Time stepping can invent instability.** Euler's update for y′=−ay, a>0, is y[n+1]=(1−ah)y[n]. Decay in magnitude requires 0<ah<2, although the continuous solution always decays. Halving steps is meaningful only alongside an error/stability question.

**Entrance/gates.** O/V: repeatedly trap a balance point between two marks; F/A: halving intervals and recurrence tables; D: tangents, Taylor error, ODE interpretation; L: ill-conditioned systems; X: functional error norms for PDE methods. A ruler gives measurement uncertainty, not an exact real oracle. An Euler table is an exact recurrence and an approximation to the ODE, with separate claims.

**Inspected sources.** Yano–Penn–Konidaris–Patera, *Math, Numerics, and Programming*, [Unit VI, §29.2, especially §29.2.5](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-spring-2013/60af88c658ba3e83cdf7c43289aeb5b4_MIT2_086S13_Unit6_Textbook.pdf); Driscoll–Braun, [*Fundamentals of Numerical Computation*](https://fncbook.com/), chapters 1, 6 and 11 located by contents. The three elementary claims above also admit direct algebraic checks.

## 68 — Computer science

**Distinguishing questions.** What can a finite rule system recognize or compute, and how do its time, memory, randomness, and interaction requirements grow?

1. **Finite memory and distinguishable histories.** A deterministic finite automaton recognizing strings whose number of red symbols is divisible by three needs three distinguishable remainder states. A diagram is an exact machine once alphabet, start state, transitions, and acceptance are specified.
2. **Recognition versus generation.** Balanced parentheses need unbounded counting depth in the unrestricted problem; a fixed maximum depth admits a finite-state machine. “Our sample machine works” does not settle all lengths.
3. **Checking versus finding.** A satisfying assignment to a finite Boolean formula can be checked efficiently. Encoding a family of puzzles as satisfiability is a reduction only after proving both directions and bounding encoding size; a difficult classroom puzzle does not establish NP-hardness.
4. **Diagonal limits.** The halting problem for arbitrary programs is undecidable. A finite collection of small programs can be exhaustively analyzed, so finite testing does not instantiate the unrestricted impossibility theorem.

**Entrance/gates.** O/C: walk through labeled machine states and invent accepted/rejected strings; A/P: reason over arbitrary lengths, construct a separating suffix; X: program encodings, self-reference and reductions. Sorting/search can be a second strand, but should not displace semantics, formal languages, verification, learning, or complexity from the frontier.

**Inspected source.** Michael Sipser, [MIT 18.404J lecture collection](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-videos/), lectures 1–5, 8–9, 14–16, and [lecture 1 slides](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf). Course structure inspected; full proofs beyond the small automata remain a family-stage obligation.

## 70 — Mechanics of particles and systems

**Distinguishing questions.** How do forces, constraints, symmetry and conserved quantities determine motion? A mechanism should include a time evolution, not just a static balance picture.

1. **Symmetry and conservation.** If a Lagrangian has no dependence on a coordinate, its conjugate momentum is conserved along Euler–Lagrange solutions. Energy conservation similarly requires time-translation symmetry with the appropriate hypotheses.
2. **Normal modes.** Linearization about a stable equilibrium reduces coupled small oscillations to an eigenvalue problem. Two identical masses coupled by springs have collective in-phase and out-of-phase motions.
3. **Stationary action.** For smooth fixed-endpoint variations, stationary action produces the Euler–Lagrange equations. The physical path need not globally minimize action; “nature always takes the shortest path” is false.

**Entrance/gates.** O/V: move a linkage, count independently adjustable joints, compare coupled pendulum motions; this is experimental modeling. F/A: ideal collision momentum and energy bookkeeping; L: modes; D/I: action and nonlinear motion. Conservation can be explored below calculus using exact collision rules, while proving the general symmetry theorem stops at calculus. Friction, external forces, and large amplitudes challenge the idealization productively.

**Inspected source.** David Tong, *Classical Dynamics*, [§§2.1, 2.3–2.6](https://davidtong.org/teaching/classical-dynamics/dynhtml/S2), particularly the stationary-versus-minimum warning, constrained coordinates, two-body reduction and small oscillations. Hamiltonian recurrence and chaos remain separate follow-up territory.

## 74 — Mechanics of deformable solids

**Distinguishing questions.** How does a body's shape change under loading, and when does it buckle, yield, or fracture? Constitutive assumptions are mathematical input, not incidental engineering detail.

1. **Series versus parallel elasticity.** Ideal Hookean springs in series add compliances; parallel springs add stiffnesses. Equal displacement and equal force are different constraints. This is an exact small network of constitutive laws.
2. **Stress, strain and anisotropy.** Force is not stress, and extension is not strain. Two geometrically similar specimens with different cross-sections need different loads for the same stress; direction-dependent material response is distinct from geometry-dependent stiffness.
3. **Buckling as loss of stability.** An ideal pinned slender Euler–Bernoulli column first buckles at P=π²EI/L² under its model assumptions. Different end conditions alter the answer; an imperfect strip can bend before the ideal threshold.

**Entrance/gates.** O/V: compare folded paper strips and elastic arrangements, choose a fair comparison; F: force per area and relative extension; A: spring equations; D/I/L: beam equations and eigenmodes. A spring network is a finite model, not proof of continuum elasticity. Do not claim that all rubber bands are Hookean, or that stiffness and strength are synonymous.

**Inspected source.** Allan Bower, *Applied Mechanics of Solids*, [§3.2, especially 3.2.1–3.2.3](https://solidmechanics.org/Text/Chapter3_2/Chapter3_2.php); [contents, chapters 5, 9, 10](https://solidmechanics.org/) locate energy, failure, rods and beams. Buckling formula is a candidate requiring its beam chapter checked before a full family is accepted.

## 76 — Fluid mechanics

**Distinguishing questions.** How can local conservation laws describe deforming continuous matter, and when can viscosity, compressibility, rotation or turbulence be neglected?

1. **Conservation along a stream tube.** In steady incompressible flow without leaks, volume flux is constant, so mean speed rises when cross-sectional area decreases. Unsteady storage invalidates that shortcut.
2. **Bernoulli's relation.** For steady inviscid flow with conservative body force, the energy expression is constant along a streamline; equality across different streamlines needs additional assumptions. Faster flow and lower pressure is not a universal law for every experiment.
3. **Low-Reynolds-number reversibility.** Negligible inertia gives linear Stokes equations. Reciprocal back-and-forth shape changes cannot propel the standard isolated swimmer under the scallop-theorem assumptions. Boundaries, non-Newtonian fluids or extra degrees of freedom change the setting.

**Entrance/gates.** O/V: move material strips to distinguish pathlines from a snapshot of arrows; F: flow-rate conservation; A/V: pressure-energy bookkeeping; D/I/X: vector calculus, PDEs, Reynolds number and viscous asymptotics. Beads on a graph can model a conservation network but omit deformation and shear. The swimmer is promising for a visual adolescent investigation, not yet a verified low-preparation child activity.

**Inspected source.** Tong, *Fluid Mechanics*, [chapter 1: inviscid flows](https://davidtong.org/pdfs/teaching/fluid-mechanics/fluids1.pdf), continuity and Euler/Bernoulli development; [course structure](https://davidtong.org/teaching/fluid-mechanics/) locates viscous flow and instabilities. The scallop anchor needs an additional primary source before promotion beyond candidate status.

## 78 — Optics, electromagnetic theory

**Distinguishing questions.** How do fields superpose and propagate, and how do geometry, material response and boundary conditions shape waves?

1. **Reflection and refraction.** Reflecting one endpoint converts a shortest broken path at a flat mirror into a straight-line problem. With different constant speeds in two media, minimizing travel time leads to Snell's law; minimum distance gives the wrong refracted path.
2. **Electrostatic boundary problems.** Potentials superpose in a linear fixed-medium model, but conductor boundaries constrain the solution. Discrete harmonic averaging has a maximum principle; its grid model must be distinguished from the continuum Laplace equation.
3. **Interference and polarization.** Coherent waves add amplitudes, not intensities. Two equal opposite-phase waves cancel in the ideal linear model. Projections through ideal polarizers depend on angle; adding a middle polarizer can transmit light through an otherwise crossed pair.

**Entrance/gates.** O/V: mirror paths and translucent wave strips; F/A: weighted travel times and signed amplitudes; trigonometry: refraction and polarization; D/I/X: Maxwell equations, boundary-value PDEs and diffraction integrals. String or water waves share superposition but are not electromagnetic fields. A laser drawing alone does not prove Fermat's principle.

**Inspected source.** Tong, [*Electromagnetism*, course chapters 1–3](https://www.davidtong.org/teaching/electromagnetism/), electrostatic potentials, wave propagation and polarization; [Electrodynamics chapter, §§4.3.2–4.3.3, PDF pp. 20–24](https://www.davidtong.org/pdfs/teaching/electromagnetism/electro3.pdf), polarization and reflection, inspected after the older PDF link failed. Refraction and the three-polarizer claim still need their exact source checked at family stage.

## 80 — Classical thermodynamics, heat transfer

**Distinguishing questions.** What transformations are possible under energy and entropy constraints, and how does heat move through space? Keep thermodynamic state functions separate from microscopic explanations in field 82.

1. **Path dependence versus state.** Internal energy is a state function, whereas heat and work depend on a process. On a pressure-volume cycle, signed enclosed area is work for the quasistatic idealization.
2. **Carnot bound.** A heat engine between reservoirs at absolute temperatures Th>Tc has efficiency at most 1−Tc/Th; reversible engines attain the ideal bound. Celsius ratios and hidden extra reservoirs invalidate the usual calculation.
3. **Diffusion and maximum principles.** Source-free heat diffusion smooths temperature differences under appropriate boundary conditions. An insulated body's total heat is conserved; fixed-temperature boundaries exchange heat, so the boundary specification matters.

**Entrance/gates.** O/F: exchange measured warm/cool water and compare equilibrium predictions under equal specific-heat assumptions; V/A: area and energy ledgers; D/I: diffusion equations and entropy integrals. Averaging counters is an exact discrete process, a shared mechanism with diffusion, and not a derivation of the heat equation. Stop before claiming entropy is simply “messiness.”

**Inspected source.** Tong, [*Statistical Physics*, ch. 4, Classical Thermodynamics](https://davidtong.org/teaching/statistical-physics/statmechhtml/S4), laws, heat engines and thermodynamic potentials. Heat-PDE family verification should additionally use the numerical-analysis/analysis dossier; it is not supplied by thermodynamics alone.

## 81 — Quantum theory

**Distinguishing questions.** What changes when states are amplitudes in a Hilbert space and observables are noncommuting operators? The probabilistic output does not make quantum mechanics ordinary hidden dice.

1. **Amplitude interference.** Adding state amplitudes and then squaring magnitudes differs from adding classical probabilities. Two real two-component vectors already provide a meaningful restricted calculation; complex relative phases extend it.
2. **Measurement order.** Projective measurements in different bases generally do not commute. Specify normalized state, projectors, outcome probabilities and state update; a decorative “quantum coin” omitting these is insufficient.
3. **Discrete spectra from boundaries.** A particle in an infinite one-dimensional well has standing-wave eigenstates with energies proportional to n². The boundary conditions, Hamiltonian and normalization are essential, not arbitrary numbering of allowed shapes.

**Entrance/gates.** V/F: projections and squared lengths for a real-amplitude special case; L/A: matrices, norms and probabilities; complex arithmetic: general finite states; D/I/X: Schrödinger equations and unbounded operators. A three-polarizer exploration is an analogue until the single-photon measurement model is specified. Finite-state quantum examples can stop below calculus while the well genuinely requires it.

**Inspected source.** Tong, [*Quantum Mechanics*, ch. 3 §§3.1–3.4](https://www.davidtong.org/teaching/quantum-mechanics/qmhtml/S3), and [chapter map including the one-dimensional well](https://davidtong.org/teaching/quantum-mechanics/). Entanglement, quantum computation and scattering remain distinct frontier mechanisms.

## 82 — Statistical mechanics, structure of matter

**Distinguishing questions.** How do microscopic states and interactions produce macroscopic behavior, including sharp phase changes and fluctuations?

1. **Multiplicity versus a macrostate.** Counting microstates with a fixed energy or particle total explains why some macrostates are more numerous. Equal likelihood of microstates is an assumption to inspect, not a consequence of counting.
2. **Competing energy and entropy.** A finite Ising model assigns spins and interaction energy; canonical weights are proportional to exp(−E/kT). Enumerating a four-site system exposes alignment versus multiplicity without claiming a true finite-temperature singular phase transition.
3. **Thermodynamic limits and correlations.** Large-system limits can be nonanalytic even when every finite partition function is smooth. Mean-field self-consistency and exact low-dimensional models answer different questions and need different qualifications.

**Entrance/gates.** O/C: list two-color spin arrangements, count agreeing neighbors, compare energy ties; F: weighted sampling; A: exponentials and partition functions; D/I/X: infinite-volume limits, criticality and correlation functions. Ordinary majority voting shares an interaction motif but is not the canonical Ising measure. A tiny model honestly covers a Hamiltonian and ensemble, not the general phase-transition theorem.

**Inspected sources.** Tong, [*Statistical Physics*, ch. 1, ensemble foundations](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html), and [chapter 5 outline](https://davidtong.org/teaching/statistical-physics/) for Ising, mean field and criticality. Small finite partition functions are ideal candidates for exact independent enumeration.

## 83 — Relativity and gravitational theory

**Distinguishing questions.** How do invariant spacetime intervals, causal structure and curvature govern observation and motion? Ordinary curved-surface geometry is useful preparation but does not itself represent Lorentzian spacetime.

1. **Light cones and invariant interval.** In 1+1 special relativity, c²Δt²−Δx² is invariant under Lorentz transformations. Events may be timelike, null or spacelike separated; arbitrary rotations of a Euclidean drawing do not preserve this interval.
2. **Proper time along paths.** Different timelike worldlines between fixed events can accumulate different proper times. Piecewise inertial paths offer a calculable twin-clock example with square roots and specified turnaround.
3. **Geodesics in curved spacetime.** A metric determines a connection and test-particle geodesics; the Einstein equations additionally determine the metric from matter. Solving motion in a supplied metric is not solving the gravitational field equations.

**Entrance/gates.** V/A: space-time coordinates, speeds and square roots; D/I: proper-time integration; L/X: tensors and differential geometry for GR. A light-clock diagram can give a faithful special-relativistic argument. A rubber-sheet model is motivation only and can misleadingly import an external downward force. It is acceptable for most of this field to stop at algebraic high-school or calculus access.

**Inspected source.** Tong, [*General Relativity*, ch. 1 §§1.1–1.3](https://davidtong.org/teaching/general-relativity/grhtml/S1), particularly equations (1.8), (1.28)–(1.35), parameter constraints and the Schwarzschild example.

## 85 — Astronomy and astrophysics

**Distinguishing questions.** How can motion and radiation constrain systems that cannot be directly manipulated, and how do gravitating systems form or remain stable?

1. **Orbit inversion.** In a two-body inverse-square model, period and orbital scale constrain mass; an observed projection does not reveal every orbital parameter. Conics are consequences of the force law, not merely shapes to draw.
2. **Virial balance.** For a suitable bounded, time-averaged gravitational system, 2⟨T⟩+⟨U⟩=0. This connects velocity dispersion and size to mass; it is not an instantaneous identity for every collapsing cloud.
3. **Jeans instability.** Linearized homogeneous self-gravitating gas balances pressure against gravity; wavelengths beyond its Jeans scale grow in the ideal model. The model's background assumptions and linearization must be explicit.

**Entrance/gates.** V/F: compare orbit traces and inverse-square scaling with geometric measurements; A: infer a parameter under an assumed model; D/I/L: orbit ODEs, virial derivation and perturbation eigenmodes. Accessible data puzzles should preserve uncertainty and model dependence. “Make constellations” has no substantive bridge to these mechanisms. Real astronomy may require a supplied data set and facilitator preparation beyond counters.

**Inspected source.** MIT, *8.902 Astrophysics II* (2023), [full lecture notes](https://ocw.mit.edu/courses/8-902-astrophysics-ii-fall-2023/mit8_902_f23_lec_full.pdf), PDF pp. 15–16, virial theorem assumptions; PDF pp. 45–46, Jeans scale and crossing/free-fall times. Orbit work also connects to Tong's mechanics, §2.5.4. Stellar structure and radiative transfer remain explicit gaps.

## 86 — Geophysics

**Distinguishing questions.** How do rotation, stratification, waves and limited observations constrain Earth's fluids and interior? Shared PDEs do not erase the field's distinctive balances and inverse problems.

1. **Rotating-frame balance.** In a rapidly rotating, slowly evolving large-scale flow, pressure-gradient and Coriolis terms can approximately balance, giving geostrophic flow along pressure contours. Water simply flowing downhill is a misleading default.
2. **Potential-vorticity conservation.** In an ideal inviscid shallow-water layer, (relative vorticity + Coriolis parameter)/depth is materially conserved. Changing depth or latitude links column stretching and rotation; forcing and friction break the conservation statement.
3. **Wave-speed inverse problems.** In a layered model with specified ray assumptions, different travel times can reveal interfaces or speeds, but nonuniqueness and incomplete observations remain. Finite ray sums are an honest algebraic special case of a larger inverse problem.
4. **Depth controls long-wave speed.** Small-amplitude, nonrotating shallow-water gravity waves have speed √(gH) under the long-wavelength approximation. This predicts changes in travel time without equating the wave's motion with the motion of an individual water parcel.

**Entrance/gates.** V/F: follow tracer paths or infer two unknown travel speeds from a few measured times; A/L: solve inverse systems and test whether data suffice; D/I/X: rotating shallow-water PDEs and continuous tomography. A turntable demonstration is an experiment, not a miniature ocean with matched dimensionless parameters. Seismology and geomagnetism require additional sources before claiming subfield coverage.

**Inspected source.** Geoffrey Vallis, [*Atmospheric and Oceanic Fluid Dynamics*, author-hosted excerpts](https://empslocal.ex.ac.uk/people/staff/gv219/aofd/aofd2_r2.pdf): contents locate §§3.4, 3.6.1 and 5.1 for geostrophy and potential vorticity; §7.1, equations (7.18)–(7.23), PDF pp. 75–76, inspected for the shallow-water limit and parcel motion. The [author's edition page](https://empslocal.ex.ac.uk/people/staff/gv219/aofd/) distinguishes sample from full book. This supports the fluid strand, not the proposed seismological extension.

## 90 — Operations research, mathematical programming

**Distinguishing questions.** How can competing feasible decisions be optimized, and how can one certify that no better decision exists? Include continuous convexity, uncertainty and scheduling, not only shortest paths.

1. **Convex local-to-global reasoning.** For a convex objective on a convex feasible set, every local minimum is global. Strict convexity ensures at most one minimizer, but neither existence nor feasibility follows automatically.
2. **Dual bounds as certificates.** A feasible primal maximization allocation and feasible dual resource prices give lower and upper bounds; equality certifies optimality. Strong duality needs its own hypotheses outside ordinary feasible finite linear programs.
3. **Dynamic programming.** A finite-horizon state captures everything needed for the remaining cost; solve backward by comparing immediate cost plus optimal future cost. A greedy next move can fail when it ignores later resource consequences.
4. **Integer constraints matter.** A fractional relaxation gives a bound but may not yield an implementable integer allocation. Rounding can violate resource constraints; integrality is a theorem in particular structures, not a general convenience.

**Entrance/gates.** O/C: build products from limited colored pieces, choose bundles, devise a price-based impossibility certificate; F/A: continuous allocations and inequalities; P: justify a bound for all choices; L/D: duality and convex optimization. A finite toy factory is exact integer optimization; its continuous relaxation is a second model.

**Inspected source.** Boyd–Vandenberghe, [*Convex Optimization*](https://www.seas.ucla.edu/~vandenbe/cvxbook/bv_cvxbook.pdf), chapters 2–5, especially local/global optimality and weak/strong duality. Dynamic programming and discrete optimization deserve separate source checks at family stage rather than being attributed to this convex text.

## 91 — Game theory, economics, social and behavioral sciences

**Distinguishing questions.** What changes when outcomes depend on other agents' choices, preferences and information? Optimization for one planner and equilibrium among several participants are different questions.

1. **Mixed strategies.** A finite two-player zero-sum game has a minimax value when randomized strategies are allowed. Matching pennies has no pure-strategy equilibrium; making the randomizer observable changes the game.
2. **Nash equilibrium versus social optimum.** A finite game has a mixed equilibrium, but equilibrium can be inefficient and need not be unique. In a small congestion game, compare unilateral incentives with total cost.
3. **Coalitions and allocation.** A transferable-utility coalition game specifies what each coalition can obtain. A core allocation must resist every coalition; the core can be empty. A proposed notion of fairness is an axiom choice, not a mathematical universal.

**Entrance/gates.** O/C: play a simultaneous-choice matrix game with cards; F: compare expected payoffs; A/P: solve indifference equations and test every profitable deviation; X: fixed-point existence arguments. Nim from prior weeks is a valid combinatorial-game branch but should not stand in for strategic or economic games. Children's observed play is not proof of equilibrium or of rational-behavior assumptions.

**Inspected sources.** Thomas Ferguson, [authored game-theory course and notes outline](https://www.math.ucla.edu/~tom/GameTheory.html), Part II §§1–4, Part III §§1–2, Part IV §§1–3. Old linked text paths fail, so this supplies scope evidence only. Giacomo Bonanno, [*Game Theory*](https://arxiv.org/pdf/1512.06808), §§1.6, 5.2–5.3, Theorems 5.1–5.2 and the mixed-strategy calculations on printed pp. 195–199, supplies inspected strategic-game exposition. Coalitional claims still require a detailed source or a self-contained finite proof.

## 92 — Biology and other natural sciences

**Distinguishing questions.** Which mathematical mechanisms explain growth, competition, transmission, heredity and reaction, and when do competing models make distinguishable predictions?

1. **Logistic growth versus exponential growth.** dN/dt=rN(1−N/K), r,K>0, has equilibria 0 and K with different stability. A chosen discrete update can overshoot or become negative; it is not automatically the same population model.
2. **Epidemic thresholds.** In a closed homogeneous-mixing SIR model, infections initially grow when βS(0)>γ under the convention S′=−βSI. Susceptible depletion can stop growth without every individual being infected.
3. **Genetic drift versus selection.** Randomly sampling the next finite generation can eliminate an allele even when its expected fraction is unchanged. Selection, mutation and population size are separate parameters, not explanations to interchange casually.
4. **Stoichiometry and reaction rates.** A reaction network has conserved linear combinations of species counts; mass-action rates then determine dynamics. Atom bookkeeping alone does not establish a reaction's speed or equilibrium.

**Entrance/gates.** O/C: draw next-generation colored counters or move counters between S/I/R compartments under fully specified rules; F: proportions and repeated sampling; A: recurrences and conservation; L/D: stability, kinetics and population equations. Token processes are exact stochastic/discrete models, not automatically numerical solutions of a deterministic ODE. Avoid implying that a model is a forecast without parameter estimation and empirical checks.

**Inspected source.** Jeffrey Chasnov, [*Mathematical Biology*](https://www.math.hkust.edu.hk/~machas/mathematical-biology.pdf), §§1.1–1.4, 4.1–4.5, 5.5, 6.1–6.2; preface and chapter structure inspected. Mathematical ecology, biochemical reaction systems and sequence alignment receive separate branches; Fibonacci alone would underrepresent this field severely.

## 93 — Systems theory; control

**Distinguishing questions.** What can a system's inputs change, what can its outputs reveal, and can feedback achieve a goal despite disturbance and imperfect knowledge?

1. **Feedback gain and stability.** In x[n+1]=ax[n]+u[n], choosing u[n]=−kx[n] produces multiplier a−k. Convergence to zero requires |a−k|<1. Stronger correction can create oscillation or divergence.
2. **Reachability.** For a finite-dimensional linear time-invariant system, the columns B, AB, …, A^(n−1)B determine its reachable directions. Missing directions cannot be repaired merely by trying more controls.
3. **Observability.** Distinct internal states can generate the same measured output sequence. A sensor that reads the sum of two identical independent modes may fail to reveal their difference; adding a second sensor can remove that ambiguity.

**Entrance/gates.** O/V: steer a paper position marker under a fixed update rule, choose corrections, compare delayed information; F/A: signed multipliers and recurrence behavior; L: rank, modes and observability; D/I: continuous feedback and optimal control. Finite reachability games are exact control systems only when dynamics, input restrictions and observations are specified. A feedback experiment by itself does not cover robust control or Kalman filtering.

**Inspected source.** Åström–Murray, *Feedback Systems*, [chapter 7, State Feedback, summary items 1–6](https://www.fbswiki.org/wiki/index.php/State_Feedback), and [chapter 8 scope](https://www.fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers). The scalar discrete example is directly proved by its geometric progression. Advanced rank and estimation claims remain explicit proof gates.

## 94 — Information and communication, circuits

**Distinguishing questions.** What resources are required to encode, convey, reconstruct or protect information through constrained or noisy channels?

1. **Variable-length coding.** Unequal message probabilities can make unequal codeword lengths efficient, but unique decoding matters. Prefix-free binary codewords form leaves of a binary tree; allowing a codeword to prefix another can introduce ambiguity.
2. **Error detection versus correction.** Minimum Hamming distance d detects every error pattern of fewer than d changed bits and corrects every pattern of at most floor((d−1)/2) errors by nearest codeword. The assumed error model is essential.
3. **Capacity versus finite performance.** Shannon's noisy-channel theorem concerns asymptotic reliable transmission below capacity under its channel assumptions; a particular short repetition code does not reach the theorem's guarantee.
4. **Circuit laws and transients.** Kirchhoff conservation plus component laws give a solvable linear resistive network; capacitors introduce state and RC transients. This deserves a separate circuit strand rather than being swallowed by communication games.

**Entrance/gates.** O/C: send counter patterns through a partner who flips a specified number; choose redundant encodings; F: weighted average length; A/L: linear codes or circuits; D/I: signal filtering and transients; X: asymptotic coding theorems. A secret cipher is not automatically error correction. Current Week 6 query-code work is prior-use adjacency, not a new family merely by renaming the story.

**Inspected source.** Claude Shannon, [*A Mathematical Theory of Communication*](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf), Parts I–II, source coding example on PDF p. 18 and noiseless/noisy coding statements. Hamming distance and circuits need their own detailed sources or self-contained proofs in later cards; Shannon's paper is not a universal citation for all field 94.

## 97 — Mathematics education: research-support disposition

**Distinguishing questions.** Which representations support learners' mathematical decisions? What changes between entering, exploring, explaining and proving? What evidence separates an attractive proposal from a successful teaching design?

1. **Representation and transfer.** Compare the same mathematical relation represented by objects, diagrams and symbols. Similar surface performance need not mean that a child recognizes the shared structure.
2. **Participation and proof.** Record independent examples, counterexamples and explanations, alongside hints and adult assistance. Solving quickly and understanding generally are separate observations.
3. **Design and assessment.** Revise a task in response to observed obstacles, preserving version and context. A repeated success with one group supports local feasibility; it does not justify universal grade labels or causal effects.

**Source distinction.** Rozhkovskaya's *Math Circles for Elementary School Students*, local EPUB `OEBPS/part0010.xhtml`, “Introduction: Berkeley 2009,” explicitly reports grades 1–3 groups following the same lesson plans and the aim of individual adult assistance; `part0027.xhtml`, “Introduction: Manhattan 2011,” reports locally adapted organization and community support. These are authored practice accounts, not controlled evidence that our proposed variants will work. Our suggestions about logging and comparison are inferences.

**Disposition.** This field supports design, review and pilot protocols; it does not need a student worksheet labeled “mathematics education.” Gates concern facilitator observation and educational research methods. Reading, working memory, motor access and mathematical prerequisites must be recorded separately. The [local source](../../../external-resources/msri-math-circle-books/Math%20Circles%20for%20Elementary%20School%20Students.epub) was actually inspected; avoid inventing child responses or classroom results.

## Protected frontier and handoff

The first design batch should contain genuinely different mechanisms: a random walk; a sampling or randomization inference; a numerical failure; an automaton; coupled motion; constitutive constraints; continuous flow; wave interference; thermodynamic process; finite quantum measurement; finite statistical ensemble; spacetime geometry; astronomical inference; rotating-fluid or inverse-data model; dual optimization certificate; strategic equilibrium; stochastic population model; feedback/observability; error-correcting communication. Several require adolescent algebra, calculus or linear algebra. That is successful coverage of prerequisites, not a failure to reach elementary school.

Important remaining territories include stochastic calculus and large deviations; causal identification and Bayesian decision theory; PDE numerical convergence; machine learning and formal verification; rigid-body chaos; nonlinear elasticity and fracture; turbulence and multiphase fluids; diffraction and inverse scattering; irreversible thermodynamics; quantum many-body theory; renormalization; Einstein field equations; stellar structure and radiative transfer; solid-Earth inversion; stochastic/integer optimization; mechanism design and social choice; evolution, reaction–diffusion and sequence comparison; robust/optimal control; cryptography, continuous signals and circuit synthesis. These are **uninvestigated descendants or source-located candidates**, not implicitly covered by the initial anchors.

All external URLs were checked in this research pass. A successful source lookup or contents read is distinguished above from inspection of the relevant exposition. Failed old links are recorded rather than substituted with uninspected mirrors. No sources were downloaded into this file's working area, no pilot evidence was generated, and no PDFs were created.
