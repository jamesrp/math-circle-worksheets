# AD2 independent design and mathematics review

Status: **PASSED for worksheet production**, after author repairs and reviewer reread on 2026-09-25. This is a design/math release, not a PDF-layout review or classroom pilot.

Reviewer: `worksheets_geometry`, independently of author `expand_ad1`. Coverage: all eight families AD-09–AD-16, all 25 proposed student pages, all 49 student prompts, all eight guide extensions, the exact figures/data, source notes, gates, prior-use notes and author check program. I derived the instances and proof arguments independently before reading the full supplied keys, then compared each key. Reading the author's finite checker informed the audit but was not treated as independent proof.

The companion `review-ad2-checks.py` imports no author code and changes no author files. Its exact arithmetic and exhaustive finite inventories pass, with evidence in `review-ad2-checks-results.json`. General proofs below were checked as arguments; finite regressions are not substitutes for them.

## Findings and closure

1. **AD-16, prompt 4: unavailable formula at its first use.** The page asked what fails in the tangent-slope formula, but the expression was first supplied on the following page. The author now includes `s=(3x²+a)/(2y)` in the prompt. Reread: this makes the required object available without silently requiring implicit differentiation beyond the named formal-partials gate. Closed.
2. **Source metadata and prose boundaries.** Three occurrences of “so urce,” “multiple−16,” and several AD-16 comma/math boundaries impaired readability. The author repaired them. I reread the three source entries and the projective/equation keys; all requested instances are clean. Closed. PDF review should still inspect actual line breaks and mathematical glyphs.

No wrong answer, missing general proof, inappropriate replacement of the adult topic, or unresolved mathematical/design blocker remains.

## AD-09 — simultaneous schedules

Checked prompts 1–6 and the three-clock extension. The four/six reports have a common parity and repeat every 12. Direct enumeration gives `(3,5)` at 11, and the four legal one-step repairs of `(2,5)` first occur at 5, 11, 10 and 6. The eight/twelve compatibility class is agreement modulo 4, with `(5,9)` at 21 modulo 24 and `(2,9)` impossible. Counting candidate same-residue pairs and proving distinctness over the full period proves completeness without checking each pair separately.

For the theorem, put `m=dM`, `n=dN`, `b−a=dc`, and use `uM+vN=1`. Then `t=a+muc` has both prescribed residues; the difference of two answers is a multiple of `mn/d`. This includes a modulus of 1, negative intermediate answers, and the first nonnegative representative. The given ten/six example reduces to 7 modulo 30. The extension yields 47 modulo 60, with both necessity and sufficiency. My checker independently compares the compatibility criterion to every full-period inventory for 144 modulus pairs and 6,084 reports.

The proposed clock diagrams and blank candidate matrix suffice; the matrix's full domain does not announce the compatible subset. The learner chooses reports and repairs before the classification. The entry is accessible with remainders; Bézout is a visibly supplied advanced step. Modular orbits/common multiples are honestly cross-linked as prior experience, while consistency and repair are the new destination.

## AD-10 — triangular squares and descent

Checked prompts 1–6 and the total recurrence. The first larger match within 36 is triangle side 8/square side 6; adding one gives 45 versus 49. The substitutions give `x²−2y²=1`; conversely parity forces odd `x`, even `y`, and positivity excludes the zero solution. Both transformation matrices preserve the quadratic form and are inverses.

The crucial descent proof is complete: for `y>2`, `4y/3 < x < 3y/2`, so `(3x−4y,3y−2x)` has positive coordinates and smaller positive `y`. Parity excludes a terminal value 1; value 2 forces `(3,2)`. Reversing proves every positive solution occurs, and strict growth proves its order and uniqueness. The totals are `1,36,1225,41616,1413721,48024900`; the first above one million has labels 1681 and 1189, followed by 9800 and 6930. Direct square testing up to `y=20000` independently recovered these six pairs. The extension's conjugate-power formula gives `N_next=34N−N_previous+2`; it does not independently establish completeness.

Open ledgers must remain unsized to the iteration count. Counter rearrangement is an entry, not the promised new core; the actual satisfying stopping point retains algebra, inequalities and descent. This is a substantive recurrence revisit, openly acknowledged, and a good proof-focused older-learner candidate rather than an elementary session in disguise.

## AD-11 — two arithmetic systems on four symbols

Checked prompts 1–6 and Frobenius. Polynomial remainders give rule A's `t²=t`, `tu=0`, `u²=u`; only 1 is a unit. Rule B gives `t²=u`, `tu=1`, `u²=t`; all three nonzero elements are units. The inverse proves no collision for multiplication by `t`; the supplied quotient-ring fact, rather than a partial table, provides associativity. No relabeling can identify B with arithmetic modulo 4, because additive orders and nonzero zero divisors differ.

At distinct inputs `r,s`, the unique affine machine has `a=(h+k)/(r+s)`, `b=h+ar`, including equal output/constant cases. The displayed reports yield `a=u,b=1,f(u)=u` in B and no solution in A. The extension swaps `t,u` while preserving both operations. My bit-polynomial checker verifies all 192 distinct-input/report cases, both inverse classifications and all Frobenius operation pairs.

Separate blank product tables and a partner decoding game provide genuine choices. The four symbols are not displayed as residues modulo 4. Supplied ring structure is distinguished from what the learner proves. Bit addition and distribution are real prerequisites; general field classification is neither required nor claimed.

## AD-12 — classical construction obstruction

Checked prompts 1–6 and trisection. Pythagoras gives the legal square-root constructions; a cube of side `√3` has volume `3√3`. The two exact rational cubes bracket 3. A line/circle step leads to at most a quadratic extension: the key covers vertical lines, parallel lines, concentric circles, tangency, negative real discriminants and coincident objects, which do not create isolated new intersections.

`X³−3` has no rational root and is an irreducible cubic, so its root's degree 3 violates the supplied necessary condition. The same argument classifies positive integer volumes: exactly integer cubes work. Zero is separately degenerate. The text correctly refuses to reverse the power-of-two degree condition, and explicitly constructs `2^(1/4)` using two square-root steps. In the extension, `u=2cos20°` satisfies `u³−3u−1=0`; neither rational-root candidate works. Thus this one impossible trisection disproves a universal procedure without saying every individual trisection is impossible.

The unit construction space and the geometric-mean semicircle are sufficient diagram specifications; production must show the perpendicular and the two diameter segment labels. Algebraic degree and irreducibility are necessary for the actual obstruction and are explicitly gated. This is the most theorem-dependent family here; the degree theorem is honestly supplied, not inferred from several pictures. It is a satisfactory advanced investigation, not a claim that counter play proves constructibility.

## AD-13 — staircase quotients

Checked prompts 1–6 and all positive rectangle dimensions. The original survivors have column sizes 4,3,1. Each corner's own position witnesses nonredundancy. Of all eight allowed moves, the survivor counts are `9,infinite,10,9,9,9,infinite,9` in the listed right/up order. Only moving `(2,1)` right frees exactly two. The axis corners prove finiteness; removing their blocking role exposes an entire infinite row or column. Common killed positions are `(0,3),(1,2),(2,0)`.

The ideal consists precisely of sums of divisible monomials. Their span cannot contain a nonzero combination of surviving monomials, proving both spanning and independence. `(x+y)³` reduces to `3xy²+y³`; total degree is not the criterion. Multiplication by `y` sends the remaining basis vectors to distinct nonzero vectors, so there is no hidden cancellation; the joint annihilator is the span of `y³,xy²,x²`. The rectangular extension has dimension `rs` and one-dimensional joint kernel, including `r=1` or `s=1`. My checker examines all eight moves and 64 rectangles.

This is a particularly strong concrete-to-algebra arc: a learner's corner choices change a visible finite object and later support a basis proof. The infinite grid must have continuation arrows and sufficient room for changed corners; no finite paper edge may silently serve as a boundary. Polynomial quotient/basis terminology belongs to the marked advanced continuation, not the launch.

## AD-14 — dual numbers and derivatives

Checked prompts 1–6 and the second-order extension. Units are exactly `a+bε` with `a≠0`, inverse `a⁻¹−ba⁻²ε`; `ε·0=ε·ε` demonstrates cancellation failure. The selected program sends `3+bε` to `10+16bε`. The polynomials `z²` and `z²+(z−2)²` agree at `2+ε` but differ at 3, showing the lost information explicitly.

Expansion of powers keeps the zero-ε and one-ε terms, proving the derivative identity for every rational input and every polynomial. The constant term, `a=0`, and exponent 1 are handled without a negative-power artifact. Product and composition comparisons, with the supplied finite-root fact, justify polynomial identities. In order 3 the coefficient is `cf′(a)+b²f″(a)/2`; the cube example gives `8+12ε+42ε²`. An independent coefficient-array Horner evaluator verifies 189 second-order cases, including zero and rational inputs.

The paired coefficient ledger should leave actual intermediate computation space. Formal quotient arithmetic is retained; ε is never called a small real number. This is a strong advanced algebra/calculus bridge with learner-created counterexamples, not merely a derivative lookup exercise.

## AD-15 — rational ellipse parametrization

Checked prompts 1–6 and the gcd extension. Substitution factors by the known root, giving `((1−2t²)/(1+2t²),2t/(1+2t²))`. The denominator is positive, `x+1` never vanishes, and zero slope is ordinary. Slopes 1 and 2/3 give the keyed exact points; the supplied challenge decodes to 3/2. Conversely every rational point except `(-1,0)` has the unique rational slope `y/(x+1)`. The vertical tangent accounts for the omitted point.

Clearing denominators yields `(q²−2p²,2pq,q²+2p²)`. Completeness is stated as equality of coordinate ratios, not a false claim that every integer triple literally equals the raw formula. The cubic counterexample leaves `x²+1` after the known root and refutes only the proposed general guarantee. For coprime `p,q`, no odd prime divides all three entries; the gcd is 1 for odd `q` and 2 for even `q`. This includes `p=0`. My checker verifies 511 coprime positive-denominator slope cases and the inverse exactly.

Draw the ellipse with vertical semiaxis `1/√2`, equal axis units, and only its supplied basepoint. Learner secants remain unprinted initially. This is a good exact-algebra investigation with encoding, inverse proof and a genuine limit of the method. The reuse of rational slopes and deliberate contrast with AD-16's ground field are clearly identified.

## AD-16 — a finite elliptic-curve group

Checked prompts 1–7 and the subgroup extension. The three affine inventories have respectively 8,3,5 points. Enumerating homogeneous triples modulo scalar multiplication independently gives nine projective points for the original curve, exactly one with `Z=0`. Its discriminant is 4 modulo 5. The singular test gives vanishing partials and undefined `0/0` slope; the text carefully avoids claiming singular curves have no other useful structures.

For `P=(0,1)` the orbit is `O,(0,1),(4,2),(2,1),(3,4),(3,1),(2,4),(4,3),(0,4),O`. Associativity is openly supplied by the nonsingular group theorem; an orbit alone is not falsely presented as proving it. The clock labels solve the four equations with label sets `{5}`, empty, `{0,3,6}`, `{1,4,7}`. Orders and the three subgroup sets follow. My independently implemented field addition checks all 81 pairs against the clock, all 729 associativity triples, and all 512 subsets for subgroup closure.

The discrete grid must remain unconnected, and the orbit ledger must not have nine preset slots. The point at infinity appears only after its projective explanation. The new payoff is cyclic structure and equation solving, not merely counting modular points. This is the steepest prerequisite gate: projective triples, field inverses, partial derivatives and a supplied group theorem are substantive requirements and must remain visible. Four pages are justified; compressing the theorem and formulas onto an overfull page would damage this otherwise sound design.

## Primary-source check and production notes

On 2026-09-25 I reopened the named primary sources and checked the passages relevant to the supplied framework: [Conrad's CRT proof](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/crt.pdf), [Pell correspondence and multiplication](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn1.pdf), [finite-field quotient construction and warning](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf), [Judson's construction theorem and intersection analysis](https://judsonbooks.org/aata-files/aata-html/fields-section-constructions.html), [Milne's monomial basis and dual-number passages](https://www.jmilne.org/math/CourseNotes/AG.pdf), [Vakil's circle parametrization](https://math.stanford.edu/~vakil/216blog/FOAGjan2915public.pdf), and [Milne's elliptic-curve nonsingularity/group law](https://www.jmilne.org/math/Books/EC2.pdf). Their scope matches the adaptations. In particular, Judson's displayed positive-exponent wording must not exclude rational degree 1; the worksheet correctly uses a nonnegative exponent and treats the condition as necessary. Milne's nonvanishing criterion differs by an invertible factor from the worksheet discriminant, as the source note now explains.

Preparation is realistic: counters, clock drawings, blank grids and ordinary construction tools, with algebraic papers clearly distinguished from elementary entries. No specialized physical apparatus is essential. Timing remains unpiloted and advanced arcs may require multiple sessions. Strong first-pilot choices by concrete richness are AD-13 and AD-11; AD-12 and AD-16 require the most careful facilitator preparation. These are candid differences of classroom fit, not release blockers.

The author may now create AD2 PDFs under the editor's existing production authorization. Independent PDF review remains required: every student page full-size, every guide contact sheet, and dense math/diagrams full-size, with special attention to answer-count scaffolds, ellipse scale, the construction diagram and AD-16's lengthy supplied rules.
