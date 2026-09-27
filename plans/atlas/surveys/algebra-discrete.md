# Research survey: foundations, discrete mathematics, and algebra

**Stage:** breadth-first research dossier, 25 September 2026. **Assigned MSC2020 fields:** 00, 01, 03, 05, 06, 08, 11–20: sixteen top-level fields. This is a research map and a candidate inventory, not a set of reviewed activities, a complete subfield census, or classroom evidence. The original atlas draft is advisory. The questions below are original design proposals unless a source exercise is explicitly identified.

Read against `README.md`, `math_circle_atlas_plan.md`, and `plans/fall-weeks-02-10-mathematical-redesign.md`. Current Weeks 1–10 are planned material, not documented successful pilots. They already occupy a substantial part of the elementary discrete entrance; a new story around toggles, permutations, or Euler routes must not be counted as new mathematics.

## How to interpret the entrances

**E — exact:** the proposed finite or restricted problem is genuinely an instance of the stated structure. **R — representation:** the objects and actions faithfully realize that structure. **A — analogue:** a useful shared mechanism that does not establish the advanced result. **G — gated:** meaningful work remains at the stated prerequisite level. Every entrance still needs a separate design-and-review pass.

The capability gates are not grades. **Objects** means sorting, matching, spatial manipulation, and following a demonstrated rule; reading may be supplied orally. **Cases** adds systematic recording, comparison, and reasons covering every case. **Arithmetic** adds the operations explicitly named. **Symbols** adds equations, variables, and functions. **Linear** means vectors, matrices, and linear maps; **Structural** means sets of objects/maps, quotients, proof, and universal properties. These are independent capabilities, not a compulsory ladder.

## 00 — General mathematics: a cross-cutting facet

This category cannot be honestly “covered” by one puzzle. It includes exposition, philosophy, problem solving, and general mathematical work. Preserve it as a facet and use it to ask what kind of mathematical claim an investigation produces. The official MSC is a research-literature taxonomy, not a list of classroom subjects [S0].

Three productive questions run across the atlas:

1. **What would convince another person?** Offer a construction, an impossibility claim, and an optimality claim on the same small board. For example, a route demonstrates existence; a parity obstruction rules out a route; a route matching a lower bound proves optimality. Ask which claims a photograph certifies and which need a reason. **E:** this is actual mathematical justification, with an Objects entrance and a Cases explanation gate.
2. **What has been forgotten in a model?** Redraw a network while preserving endpoints of every edge. Does the route question change? Then merge two vertices and ask again. Children decide which changes preserve the problem, instead of merely being told that the picture is a graph. **E/R:** graph isomorphism and a counterexample to an invalid quotient. Week 10 is a direct prior instance; the new question would be model equivalence, not another route puzzle.
3. **Which conjecture deserves to survive?** Generate examples, seek a counterexample, repair the hypothesis, then distinguish the repaired statement from its converse. Euclid's finite-list prime argument is a useful adult calibration: “the constructed number is prime” is stronger than, and unnecessary for, the proof [S2]. A child who understands factors can find a counterexample to the stronger claim.

**Stop/trap:** these are proof-and-model facets, not substitutes for foundations, philosophy of mathematics, or mathematical education research. A checklist that says “uses reasoning” adds no substantive coverage. The next survey must separately investigate general mathematical modeling and philosophy; this dossier does not settle either.

## 01 — History and biography: questions with provenance

History concerns how mathematics actually developed, including notation, tools, institutions, and people. Do not use legendary anecdotes as evidence. Three source-grounded mathematical comparisons are available now:

1. **Why does repeated subtraction find a common measure?** Reconstruct Euclid VII.2 with two lengths made of unit blocks. Compare subtracting one copy at a time with removing several copies. **E:** the invariant common-divisor set and termination are visible; division notation is optional [S1].
2. **Does a finite list of primes exhaust the possibilities?** Reconstruct IX.20 and examine why the new number need not be prime. **E:** a new prime divisor, not necessarily a new prime equal to the constructed integer, defeats a proposed exhaustive list [S2]. The child gate is multiplication, divisibility, and the meaning of “any proposed list.”
3. **What did Euler remove from the bridge map?** Compare a geographic drawing, a sequence of region letters, and a modern graph. Which information survives? The Euler Archive identifies the original work E53 and distinguishes written and publication dates [S3]. **E:** the route problem; **A:** claiming the modern graph formalism exactly reproduces Euler's presentation without reading that presentation.

These should become comparative investigations, not mini-biographies preceding arithmetic. At a later gate, ask how a proof changes when zero is admitted as a number, or when algebraic notation replaces geometric magnitudes; those require further historical sources.

**Stop/trap:** three European-source anchors do not cover mathematical history. Egyptian, Babylonian, Chinese, Indian, Islamic, Indigenous, and modern global mathematical traditions remain an explicit research frontier, with authored historical scholarship needed. “Ancient people did our modern worksheet” is an anachronism. Existing Weeks 4/9 overlap Euclidean divisibility and Week 10 overlaps Euler; historical framing alone does not create new mechanism coverage.

## 03 — Mathematical logic and foundations

Distinguishing territory includes truth versus proof, expressibility, models, computation, set-theoretic size, and independence. A collection of truth puzzles alone misses most of it. Open Logic supplies inspected anchors for diagonalization, first-order compactness, and undecidability [S4].

1. **Can two different rule cards accept exactly the same objects?** On a finite inventory, compare “red and round” with the negation of “not red or not round”; then alter a quantifier. **E:** Boolean semantics and equivalence. Objects suffice for participation; Cases is needed to justify equivalence over all possible property combinations.
2. **Can you defeat every row in a proposed list?** Given an (n ×  n) binary array, construct a length-(n) row differing from row (i) at position (i). **E:** finite diagonal construction. The infinite binary-sequence argument needs a separately stated rule for every positive integer. It proves no enumeration of all infinite binary sequences exists; the finite activity alone does not prove uncountability.
3. **Can every finite set of demands be met, while the whole collection requires a new kind of model?** Explore demands “there are at least (n) objects,” then the infinite set of all such demands. **E:** concrete finite models; **G:** first-order compactness requires syntax, satisfaction, and quantifiers. Do not claim that every infinite puzzle inherits compactness under arbitrary rules.
4. **Can a machine reliably predict whether all other machines stop?** First trace tiny explicitly specified programs, distinguishing a terminating computation from an observed prefix. **E:** computations; **G:** the diagonal impossibility argument requires encodings and self-application. A looping toy machine is not a proof of undecidability.

**Frontier:** proof theory, constructive logic, forcing, large cardinals, descriptive set theory, and reverse mathematics remain unscreened internally. Week 5 supplies finite constraint satisfaction and Week 6 elimination of candidates; neither already covers model theory or incompleteness. Useful early designs are truth-table equivalence and diagonal adversarial construction; advanced claims must remain gated.

## 05 — Combinatorics

Counting, extremal structure, designs, graph theory, algebraic combinatorics, and random constructions have different mathematical questions. Four precise anchors from Stanley are available [S5]:

1. **How many walks of a fixed length reach a destination?** Children move counters on a small network and count by last step. The (i,j) entry of (A^k) counts length-(k) walks for the specified adjacency convention. **E:** recurrence on a finite graph; matrix multiplication can arrive after the combinatorial reasoning. Distinguish walks from simple paths.
2. **How many subsets can be chosen if none may contain another?** Begin with all subsets of four named objects. Children choose a large incomparable collection and challenge another group's certificate. **E:** antichains in a Boolean lattice. The general largest size is choose(n, floor(n/2)); full proof needs a chain or counting argument, not just inspection of the middle layer.
3. **How many ways can a network stay connected after deleting all unnecessary links?** Enumerate spanning trees of a square with one diagonal. **E:** tree enumeration. The Matrix-Tree Theorem connects the count to a Laplacian cofactor for a finite connected loopless graph; determinant evaluation is a later gate.
4. **Can every labeled tree be encoded by a short list and decoded uniquely?** Try leaf deletion on four labels before deriving Prüfer coding. **E:** bijection; for (n ≥ 2), the eventual count (n^{n-2}) is a theorem about labeled trees, not unlabeled shapes.

**Access:** Objects for constructing, Cases for exhaustive lists and bijections, arithmetic for counts, Linear for spectral extensions. **Stop/trap:** a huge brute-force list is not automatically an engaging investigation; proving completeness must remain possible at the chosen scale. Source-dependent graph conventions matter, particularly loops.

**Frontier:** extremal/Ramsey theory, probabilistic method, matroids, design existence, enumeration via generating functions, analytic combinatorics, and additive combinatorics need independent dossiers. Weeks 1/5/7/8/10 already cover tilings, Latin constraints, impartial games, and routes. Antichains and tree codes supply genuinely different questions.

## 06 — Order, lattices, ordered algebraic structures

The defining move is replacing a single line of “bigger/smaller” with partial comparison and asking about common bounds. Burris–Sankappanavar I §§1–5 distinguishes lattices, distributivity, complete lattices, and closure [S6].

1. **Can two collections be incomparable?** Order subsets by inclusion, or positive divisors of 12 by divisibility. Find a greatest common lower bound and least common upper bound. **E/R:** meet/join, respectively intersection/union or gcd/lcm. Objects can handle subset cards; divisibility requires multiplication or supplied division diagrams.
2. **Does distributing one operation across another always work?** Compare subset lattices with the five-element diamond (M_3). With distinct middle elements (a,b,c), test (a ∧ (b ∨  c)) against ((a ∧  b) ∨ (a ∧  c)). **E:** a small exact counterexample; a Hasse diagram is a new representation to teach, not a prerequisite to assume.
3. **What is forced by a chosen starting collection?** On a four-object system with explicit implications, repeatedly add forced objects. Compare all legal orders of applying rules. **E:** extensive, monotone, idempotent closure. Ask whether closing the union differs from merely uniting two closed sets; the closed sets form a lattice whose join may require closing again.
4. **How can two comparison systems translate optimally into one another?** “How many three-seat benches are needed?” and “How many children can these benches seat?” instantiate ceil(x/3) ≤ n if and only if x ≤ 3n, for nonnegative integer counts. **E:** a Galois connection of preorders, with rounding/division gate [S7, §1.4].

**Stop/trap:** not every poset is a lattice, not every lattice is distributive, and a closure procedure does not establish all of lattice theory. Ordered groups, vector lattices, and Boolean duality are an advanced frontier. Week 1's tiling-order ideas are related but do not license a blanket lattice label.

## 08 — General algebraic systems / universal algebra

This field studies operations and identities across many kinds of algebra, including when quotienting, combining, or freely generating structures preserves laws. Its interest is in the common structure, not merely using unusual arithmetic [S6, II §§1–11; III §§1–4].

1. **Can a binary-operation table obey some laws and violate others?** Provide three symbols and let children invent a complete table; challenge commutativity, associativity, or an identity with explicit witnesses. **E:** finite algebras. A small table can have a substantial question; asking children to verify all triples mechanically cannot be the whole activity.
2. **Which symbols may safely be treated as the same?** Start with addition modulo four. Merge 0 with 2 and 1 with 3; compare with merging only 0 with 1. **E:** the first partition is a congruence, the second fails well-definedness. Children must test whether choices of representative change an answer.
3. **Can two machines run side by side and retain the same laws?** Build pairs of states and apply each operation coordinatewise. **E:** direct product. The interesting question is what properties survive and whether every paired state can actually be reached from selected generators; do not assume all products are cyclic.
4. **What is the most general machine with two buttons and no extra rules?** Use words in two letters; concatenate, then optionally impose (aa=a), or (ab=ba), and investigate equivalent words. **E:** free monoids and presentations. **G:** Birkhoff's HSP theorem concerns equational classes of a fixed signature and closure under homomorphic images, subalgebras, and products; word play is not its proof.

**Stop/trap:** universal algebra and algebraic geometry use “variety” differently. A Latin square is a quasigroup table but need not be a group table. Week 5 is a candidate exact quasigroup connection, yet tower-clue uniqueness is a different question from identity preservation. Constraint-satisfaction polymorphisms and decidability remain research frontier.

## 11 — Number theory

Arithmetic patterns become serious mathematics through divisibility, local obstructions, global solutions, approximation, and arithmetic structure. Four different mechanisms should be kept apart:

1. **Can one hidden number meet two remainder reports?** Use two rotating rings of sizes 3 and 4, then 4 and 6. For coprime positive moduli (m,n), every residue pair has exactly one solution modulo (mn) [S8, Theorem 1.1]. **E:** Chinese remaindering. For the changed pair, children must discover incompatibility instead of being told the same theorem applies.
2. **Can a number be both triangular and square?** Build 1 and 36 with dots, then seek the next example. The transformation (m(m+1)/2=n^2 ⇔ (2m+1)^2-2(2n)^2=1) connects the question exactly to a restricted Pell equation [S9, §3]. **E:** the dot question; **G:** proving all solutions requires more than extending a numerical pattern. The recurrence from multiplying by (3+2√2) can be checked symbolically once quadratic expressions are available.
3. **Can a local test rule out a global integer solution?** Ask whether (x^2+y^2=3 (mod 4)) can occur: squares have residues 0 or 1, so it cannot. **E:** a modular obstruction. Then ask whether passing one test guarantees a solution; it does not. This is an original small instance, not a claim to have taught the arithmetic local-to-global principle.
4. **Can you always escape a finite proposed prime list?** Euclid's argument gives a complete elementary impossibility proof [S2]. Change “prime” to other multiplicatively defined lists only after checking which argument survives.

**Access:** remainders can be tracked by movement before division algorithms; Pell begins concretely but its classification stops at Symbols with an additional proof gate. **Frontier:** analytic prime distribution and (L)-functions, algebraic number fields, (p)-adic arithmetic, elliptic curves, transcendence, Diophantine approximation, and arithmetic dynamics remain substantive future branches. Weeks 4 and 9 cover gcd/orbits; they are not new coverage here.

## 12 — Field theory and polynomials

The central questions concern which equations become solvable after enlarging the number system, how roots can be permuted while preserving arithmetic, and what new operations permit. Three distinct bridge candidates:

1. **Can arithmetic with four symbols allow division by every nonzero symbol?** Construct 𝔽₂[t]/(t^2+t+1), representing (0,1,t,1+t) with two-bit cards. Compare with arithmetic modulo four. **E:** the former is a field; the latter has zero divisors. The irreducible-polynomial requirement matters [S10, Theorem 1.1 and warning]. Objects plus table-following permits exploration; polynomial reduction and proof are later gates.
2. **Which changes to roots preserve every arithmetic relation?** In ℚ(√2), test (a+b√2 ↦  a-b√2). Then compare two independent square roots. **E:** automorphisms of a specified extension, not arbitrary permutations of a printed list of roots. The Symbols gate includes fractions, distributivity, and the distinction between a number and its decimal approximation.
3. **Which lengths can ruler and compass actually create?** Construct square roots geometrically, then investigate why duplicating a cube requires a different algebraic degree. A constructible real number has degree a power of two over ℚ; this necessary condition rules out ∛2 [S11, §21.3]. **E:** exact construction questions; **G:** the obstruction proof needs field extensions. “I tried and failed” is not the proof.

**Stop/trap:** prime-power field size does not mean ℤ/p^nℤ is a field. General quintic insolvability is not “no quintic can be solved.” Full Galois correspondence, inseparability, valuation theory, difference and differential fields remain gated or unscreened. Week 4 cyclic motion is useful preparation but does not itself realize field arithmetic.

## 13 — Commutative algebra

The distinctive objects are rings, ideals, modules, localizations, and dimension: algebra that records the structure of solutions and the failure of familiar cancellation rules. Milne's chapters 1–2 provide the inspected ring/ideal and geometric anchors [S12].

1. **What remains after certain monomials are declared zero?** On the exponent grid (i,j) for (x^iy^j), mark all multiples of (x^2,xy,y^3). Ask which monomials survive and how multiplying by (x) or (y) moves or kills them. **E/R:** a monomial quotient with basis (1,x,y,y^2) over a field. Cases and grid movement suffice for discovering the four survivors; vector-space dimension is a later interpretation.
2. **Can a nonzero thing square to zero?** Compare (k[t]/(t^2)) with (k[t]/(t)). Track multiplication using (t^2=0) and notice that both equations have the same ordinary zero set, although the quotients differ. **E:** nilpotents and information lost by taking only points. This is a genuine small algebra, not a tiny nonzero real number.
3. **What changes when selected numbers become invertible?** Allow fractions whose denominators are powers of two. Can (1/3) be represented? Compare with allowing every odd denominator. **E:** localizations of ℤ. Rational arithmetic permits a complete small argument; prime ideals enter only later.
4. **Can infinitely many polynomial constraints be controlled by finitely many generators?** First study an upward-closed set of exponent-grid points and its minimal corners. **E:** a monomial-ideal special case. **G:** Hilbert's basis theorem concerns Noetherian coefficient rings and polynomial rings; finitely many drawn corners do not prove it generally.

**Stop/trap:** quotient by an ideal is not “ignore the inconvenient terms” without checking closure. Gröbner bases, depth, regularity, homological dimensions, and local algebra remain separate research work. Toggle spaces in Week 2 are vector spaces, not automatic commutative-algebra coverage. The monomial grid is a promising genuinely new lower entrance.

## 14 — Algebraic geometry

The territory links equations, geometric objects, maps, singularities, and arithmetic over different fields. Coordinate plotting alone is not enough. Four candidate questions retain distinct geometry:

1. **Can every rational point on a circle be found by shooting a rational-slope line from one known point?** Use the circle (x^2+y^2=1) and the point ((1,0)). Solve for the second intersection and account for the exceptional point. **E:** rational parametrization of a conic [S13, §6.5, printed pp. 191–193]. Enter with drawing; solving and proving completeness require fractions and quadratic equations.
2. **Where did the second intersection go?** Vary a line meeting a parabola: two real intersections can merge or leave the real plane. **E:** line–conic intersection. **G:** Bézout's theorem counts degree-product intersections in the projective plane over an algebraically closed field, with multiplicity and no shared component [S12, Theorem 6.37]. The child experiment should expose missing hypotheses, not claim “all curves always meet that many times.”
3. **Do two equations describe the same geometric object?** Compare (y=x^2), the parametrization ((t,t^2)), and (xy=0). Ask whether one parameter can recover every point and whether crossing lines behave like a smooth curve. **E:** specified maps and reducibility; **G:** tangent spaces/singularity schemes need polynomial and linear tools.
4. **What does a curve look like over a finite field?** Enumerate the solutions of (y^2=x^3-x) over 𝔽₅, then compare with a real plot. **E:** arithmetic points of the same polynomial relation over different fields. This is a point-counting investigation, not yet elliptic-curve group law or cryptography.

**Stop/trap:** a plotted curve is not a scheme, and a finite grid is not an approximation to all algebraic geometry. Schemes, sheaves, cohomology, moduli, birational geometry, and enumerative geometry remain protected advanced branches. Week 9 rational slopes are relevant preparation, not equivalent content.

## 15 — Linear and multilinear algebra / matrix theory

This field studies combination, dependence, transformation, and canonical structure. It has excellent low entrances, but the familiar toggle model samples only one coefficient field. Axler supplies the linear-map, spectral, and inner-product anchors [S14].

1. **Which sets of moves do the same job?** For a specified finite toggle board, find both reachable outputs and press patterns that do nothing. **E:** image/kernel over 𝔽₂, with rank–nullity explaining their sizes after a basis is established. Week 2 already owns this mechanism; a new board is only an instance unless the question changes substantially.
2. **Which features survive repeated averaging?** Apply ((x,y) ↦ ((3x+y)/4,(x+3y)/4)). The sum stays fixed while the difference halves. **E:** eigen-directions in a (2 × 2) map. Children can move two markers and compare midpoints; fractions support exact reasoning. This adds real-scalar dynamics missing from binary toggles.
3. **Can a transformation flatten a picture, reverse it, or preserve its area?** Compare two planar shears and a projection on a unit-grid parallelogram. **E:** determinant as signed area scaling. Counting squares is entry; signed coordinates and a general proof come later. Do not infer that area preservation implies distance preservation.
4. **Which approximate solution is best when exact measurements disagree?** Find the nearest point on a line to a marked point, then connect perpendicular error to least squares. **E:** orthogonal projection in a Euclidean inner-product space. Measurement is exploratory; proof requires exact geometry or dot products.

**Frontier:** multilinear maps, tensors, bilinear forms, canonical forms, matrix inequalities, and spectral algorithms need their own questions. Rank–nullity holds over any field with finite-dimensional domain, but Axler's inspected text restricts its standing scalars to ℝ or ℂ; the binary version needs its own algebraic proof. No calculus gate is inherent here.

## 16 — Associative rings and algebras

The distinctive change is that multiplication can encode composition and need not commute. Modules and representations turn algebra into actions on spaces; noncommutativity is not merely an amusing exception. Etingof et al. §§1.2–1.8 and chapters 2, 5 anchor this territory [S15].

1. **Does changing the order of two operations change the result?** Use matrices (A=[[1, 1], [0, 1]]), (B=[[1, 0], [1, 1]]), and a marked lattice point. **E:** matrix multiplication acting on vectors. Arrow movement allows entry before multiplying arrays; the investigator must specify right-to-left composition.
2. **Can two nonzero transformations compose to zero?** Project onto the horizontal axis and then project onto the vertical axis. **E:** zero divisors in an endomorphism ring. Contrast with invertible transformations and ask exactly what information disappeared. This is not evidence that real-number multiplication has zero divisors.
3. **Can a network of vector spaces be assembled from simpler pieces?** Begin with one linear arrow (V →  W). Classify small maps up to independent basis changes by rank, then add a second arrow. **E:** quiver representations. **G:** vector spaces and changes of basis are unavoidable for the mathematical question; dots and arrows without linear data are only a motivational picture.
4. **When does an action split into independent parts?** Compare the coordinate-axis decomposition of a diagonal operator with a (2 × 2) Jordan block. **E:** invariant subspaces and failure of complete reducibility. The general semisimplicity question is richer than finding an invariant subset of tokens.

**Stop/trap:** the set of all functions under composition is a monoid; it becomes an associative algebra only with suitable compatible addition and scalar multiplication. Weeks 3/4 already show noncommuting or cyclic actions but do not cover module decomposition. Division algebras, homological ring theory, noncommutative geometry, PI rings, and quantum groups remain distinct advanced frontier.

## 17 — Nonassociative rings and algebras

Lie, Jordan, and alternative algebras deserve separate treatment. “Order matters” means noncommutative; nonassociative means parentheses matter. Etingof's Lie-algebra definition and Baez's authored octonion survey anchor three different mechanisms [S15, §1.9; S16, §§2–3].

1. **Can the failure of two transformations to commute itself be measured algebraically?** For real square matrices set ([A,B]=AB-BA), and calculate a small commutator table. **E:** a Lie bracket; the Jacobi identity follows by expansion and associativity of the original product. **G:** matrix addition/multiplication and negatives. Physically reversing two finite rotations is motivation, not a direct realization of this infinitesimal bracket.
2. **What survives if matrix multiplication is symmetrized?** Define (A ∘  B=(AB+BA)/2) for real matrices; compare (A ∘ (B ∘  C)) and ((A ∘  B) ∘  C). **E:** a special Jordan algebra and a discoverable failure of associativity. Fractions and matrices are a genuine prerequisite, not something a colorful story removes.
3. **Can a seven-point diagram encode multiplication that fails associativity?** Use a fixed oriented Fano-plane multiplication convention for octonion units, including signs. Ask for a concrete pair of parenthesizations giving different answers. **E:** multiplication of specified units; reading a signed operation table is sufficient for a finite counterexample. **G:** the normed division algebra, exceptional structures, and their classification need substantial linear algebra.

**Stop/trap:** never claim any cyclic triangle drawing is “the octonions”; orientation, sign, unit, and anticommutation conventions are essential. A small counterexample establishes failure of associativity, not the division-algebra theorem. The finite table entrance may be mathematically exact yet pedagogically thin; it should compete honestly with the stronger matrix-commutator investigation. No current week substantially covers this field.

## 18 — Category theory and homological algebra

The subject concerns composition, maps between structures, universal constructions, and algebraic information extracted from sequences of maps. Fong–Spivak gives concrete categorical models [S7]; homological algebra must retain its extra linear structure rather than being absorbed into generic arrow drawing.

1. **Can two different routes through machines always give the same answer?** Supply finite sets, explicit functions, and a square of machines. Test commutativity for every input and repair one map. **E:** commuting diagrams in finite sets. Composition is associative, but equality of the two routes is additional data to investigate.
2. **How can two lists be paired using a shared label?** Build ({(a,b):f(a)=g(b)}) from two finite labeled collections. Ask why every other consistently paired collection has exactly one map to this collection preserving its two projections. **E:** pullback in sets [S7, §3.5.3]. Objects supplies the construction; the uniqueness property needs Structural reasoning.
3. **What is the best translation between “resources required” and “tasks possible”?** The benches/children adjunction in field 06 is an exact preorder example. The shared mechanism should be one family with two research links, not two counted activities.
4. **Which closed edge-patterns are boundaries of faces?** Work over 𝔽₂ with vertices, edges, and triangular faces. The boundary of a face-boundary is zero; a triangle loop is a cycle whether or not its face is filled, but it is a boundary only in the filled version. **E/R:** a small chain complex and its first homology. Source support for the general homological setting is the Stacks Project's complexes and cohomology section [S17]; the finite construction needs its own checked matrices.

**Stop/trap:** a loop in a picture need not represent a nonzero homology class. A commuting diagram is not automatically a universal one. Derived categories, higher categories, operads, toposes, and spectral sequences remain hard gates. Week 2's incidence map is an exact preparatory object; adding faces and quotienting cycles by boundaries creates the new mathematical question.

## 19 — Algebraic K-theory

K-theory builds invariants from algebraic or geometric objects and how they combine; stable equivalence and group completion are genuine initial mechanisms, but not the whole field. Weibel II §§1–2 was inspected directly [S18].

1. **Can we consistently subtract collections that only know how to combine?** Represent a formal difference by a pair (a,b); for ordinary nonnegative counts, identify (a,b) with (c,d) when (a+d=b+c). **E:** group completion of ℕ to ℤ. Counters and cancellation permit early entry. The interesting question is well-definedness of addition and equivalence, not routine negative-number arithmetic.
2. **What if cancellation fails?** Try the commutative monoid {0,e} with (e+e=e). In any group receiving a monoid homomorphism, the image of (e) must be zero. **E:** group completion can lose information. This counterexample guards against pretending the simple pair rule describes all monoids without adjustment; general equality allows adding a common extra element.
3. **Can two kinds of symmetry-orbit be counted independently?** For a two-element group, classify finite actions into fixed points and swapped pairs. Addition is disjoint union. **E:** the additive monoid underlying its Burnside ring, whose completion is ℤ^2; investigate products to see why total number of points alone forgets structure [S18, Example 1.5].
4. **Why is (K_0(k) ≅ ℤ) for a field?** Finite-dimensional vector spaces combine by direct sum and are classified by dimension. **G/E:** this is actual (K_0), once vector spaces/projective modules and the definition are available. The counter story in question 1 is its underlying completion mechanism, not a claim that all counter play teaches algebraic K-theory.

**Stop/trap:** higher (K)-groups, projective modules over general rings, vector bundles, localization theorems, and links to arithmetic require protected advanced work. This field should be marked “small exact construction found; major prerequisite gate remains,” not rejected wholesale or declared elementary.

## 20 — Group theory and generalizations

Symmetry, generation, actions, quotients, representations, and geometric group theory provide different questions. The following extend beyond merely identifying repeated cycles; Judson §§14.1 and 14.3 anchor action and orbit counting [S11].

1. **How many moves does it take to restore a labeled triangle?** Generate its six symmetries using a rotation and one reflection; compare words that act identically. **E/R:** (D_3), generators/relations, and a finite Cayley graph. Objects permits manipulation; Cases is needed to establish completeness and shortest words. Contrast the two orders of rotation and reflection.
2. **How many genuinely different necklaces are there?** For length-four binary necklaces, decide explicitly whether only rotations or also reflections identify arrangements. Count orbits directly, then by fixed configurations. **E:** finite group action; Burnside averages fixed-point counts. Dividing by the number of symmetries fails when stabilizers vary.
3. **What information can be forgotten while multiplication still makes sense?** Send a permutation to its parity, or a square symmetry to its action on the two diagonals. **E:** a homomorphism and its kernel. The question is which distinctions can be erased consistently, not merely grouping objects by resemblance.
4. **What changes when moves are not reversible?** Add a “send every token to one place” operation. **E:** transformation semigroups/monoids, which are included in this MSC field. Compare eventual cycles and transient behavior with the pure permutation case. This changes the mathematical question from Week 3, where every state lies on a cycle.

**Access:** the first two can begin with spatial operations and systematic cases; parity needs transpositions and a proof that the sign is well-defined. **Stop/trap:** symmetry group, configuration space, and set of legal moves are different objects. Representations require linear structure. Infinite groups, growth, word problems, group cohomology, profinite groups, and classification of finite simple groups remain separate frontier. Weeks 3/4 are direct overlap; the most promising new choices are stabilizers, quotient maps, and irreversible transformations.

## Priorities and non-duplication decisions

The next bridge-design batch should prioritize antichains; tree codes; closure systems; valid versus invalid quotienting; triangular-square numbers; four-symbol field arithmetic; monomial staircases; rational conics; averaging eigen-directions; and face boundaries. These offer different decisions and explanations from current Weeks 1–10.

A protected advanced batch should tackle polynomial/field obstructions, quiver decompositions, matrix commutators, and group completion with failure of cancellation. It is acceptable for those to stop at explicit algebra or linear-algebra gates. Historical comparison and proof/model questions should be tagged as cross-cutting lenses; they must not pad the family count.

No statement here justifies “all of algebra surveyed exhaustively.” Every listed top-level field has been substantively screened; its internal frontier remains large. Recommended ledger dispositions are **00/01: facet with substantive candidate questions**, **03/05/06/08/11–18/20: candidate mechanisms, review pending**, **19: exact preliminary mechanisms plus identified advanced gates**. None is “classroom validated.”

## Inspected source register

URLs below were opened through the web tool on 25 September 2026; specific theorem/section text was inspected where cited. These sources support mathematical anchors, not the proposed capability profiles. No downloaded source files or redistributed book text were created by this survey.

- **S0.** AMS/zbMATH, [MSC2020 database](https://mathscinet.ams.org/mathscinet/msc/msc2020.html) and [research-taxonomy help](https://mathscinet.ams.org/mathscinet/info/docs/search-extras/search-msc). Supports scope and taxonomy purpose; the coordinator owns the complete pinned import.
- **S1.** Euclid, *Elements*, David E. Joyce's edition, [VII.2](https://mathcs.clarku.edu/~djoyce/elements/bookVII/propVII2.html): common measure by repeated subtraction. Translation/commentary, not a claim to inspect an ancient manuscript.
- **S2.** Euclid/Joyce, [IX.20](https://mathcs.clarku.edu/~djoyce/elements/bookIX/propIX20.html): prime outside any assigned finite list; inspect the prime/composite split.
- **S3.** Euler Archive, [E53: Solutio problematis ad geometriam situs pertinentis](https://scholarlycommons.pacific.edu/euler-works/53/), archival metadata and content summary. Original-paper text was not inspected; any comparison of Euler's exact presentation remains an additional task.
- **S4.** Open Logic Project, [*Sets, Logic, Computation*](https://slc.openlogicproject.org/slc-screen.pdf), chapter 4 diagonalization (printed pp. 58–60), §12.9/Theorem 12.23 compactness, chapter 15 undecidability. Inspected corresponding PDF text; no source claim about young learners.
- **S5.** Richard P. Stanley, [*Topics in Algebraic Combinatorics*, 1 February 2013 author draft](https://math.mit.edu/~rstan/algcomb/algcomb.pdf): Theorem 1.1 walks, chapter 4 Sperner property, Theorem 9.8 Matrix-Tree, chapter 9 appendix on tree encodings. This PDF's printed pagination differs from its file page count and published editions.
- **S6.** Stanley Burris and H. P. Sankappanavar, [*A Course in Universal Algebra*, Millennium edition](https://math.hawaii.edu/~ralph/Classes/619/univ-algebra.pdf): I §§1–5; II §§5–11, especially Theorem 11.9 (Birkhoff); III §§1–4. The authors' [distribution page](https://www.math.uwaterloo.ca/~snburris/htdocs/ualg.html) describes editions and rights.
- **S7.** Brendan Fong and David I. Spivak, [*Seven Sketches in Compositionality*](https://ocw.mit.edu/courses/18-s097-applied-category-theory-january-iap-2019/a4175d61479a35340d6307ae5e48ef5a_18-s097iap19textbook.pdf), Definition 1.95 and Example 1.97 (Galois connections); §3.5.3, pullbacks of sets, especially colored-pair example; chapter 3 categories/functions. The benches interpretation is this survey's proposed finite-count specialization.
- **S8.** Keith Conrad, [*The Chinese Remainder Theorem*](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/crt.pdf), Theorem 1.1 and §2 proof.
- **S9.** Keith Conrad, [*Pell's Equation, I*](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn1.pdf), §3/Theorem 3.1 triangular-square numbers; §4 multiplication of quadratic units.
- **S10.** Keith Conrad, [*Finite Fields*](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf), Theorem 1.1, examples and warning on p. 1; executive summary. Four-element model here is a proposed specialization.
- **S11.** Thomas W. Judson, *Abstract Algebra: Theory and Applications*, [§21.3 Geometric Constructions](https://judsonbooks.org/aata-files/aata-html/fields-section-constructions.html), [§14.1 Groups Acting on Sets](https://judsonbooks.org/aata-files/aata-html/actions-section-groups-acting-on-sets.html), [§14.3 Burnside's Counting Theorem](https://judsonbooks.org/aata-files/aata-html/actions-section-burnsides-counting-theorem.html). Also inspected chapter-level contents for fields, finite fields, and lattices.
- **S12.** J. S. Milne, [*Algebraic Geometry*, version 6.10](https://www.jmilne.org/math/CourseNotes/AG.pdf), chapter 1 rings/ideals/localizations; chapter 2 Hilbert basis theorem and Theorem 2.16 Nullstellensatz; Theorem 6.37 Bézout. Assumptions about the field must be carried with theorem statements. The specific monomial quotient and finite-field enumeration are proposed examples, not attributed exercises.
- **S13.** Ravi Vakil, [*The Rising Sea*, January 29, 2015 draft](https://math.stanford.edu/~vakil/216blog/FOAGjan2915public.pdf), §6.5, printed pp. 191–193, rational parametrization of a circle. Inspected historical draft, explicitly not the current published edition.
- **S14.** Sheldon Axler, [*Linear Algebra Done Right*, fourth edition author PDF](https://linear.axler.net/LADR4e.pdf), §3A linear maps/composition, §3B/Theorem 3.21 rank–nullity, §6C/Definition 6.55 orthogonal projection, §7B/Theorems 7.29 and 7.31 spectral theorems. Source standing scalars are real/complex; do not cite it as if its text states the finite-field version.
- **S15.** Pavel Etingof et al., [*Introduction to Representation Theory*, January 10, 2011 notes](https://math.mit.edu/~etingof/replect.pdf), §§1.2–1.9 algebras/representations/quivers/Lie algebras, chapter 2 decompositions, chapter 5 quivers. Definition 1.39 and Example 1.40 explicitly inspect the Lie bracket and Jacobi identity. These notes use numbering different from the later book.
- **S16.** John C. Baez, [*The Octonions*, author PDF](https://math.ucr.edu/home/baez/octonions/octonions.pdf), §2.1 Fano-plane rules (printed pp. 6–8) and §3 Jordan product/discussion (printed pp. 19–20); also inspected the [associator discussion](https://math.ucr.edu/home/baez/octonions/node2.html). PDF text was inspected. A final signed-table activity must visually inspect the multiplication diagram before selecting an exact instance.
- **S17.** Stacks Project, [§12.13 “Complexes”](https://stacks.math.columbia.edu/tag/010V), definition of homology following Lemma 12.13.3 and the cochain counterpart; also inspected Lemma 12.13.12. This is not a source for a child activity; a future design must explicitly verify its finite boundary maps and quotient.
- **S18.** Charles Weibel, [*The K-book*, chapter II](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf), §1 group completion, Proposition 1.1, Example 1.5 Burnside ring; §2 definition and first computations of (K_0). [Author contents page](https://sites.math.rutgers.edu/~weibel/Kbook.html) distinguishes chapter-PDF pagination from the published volume.
