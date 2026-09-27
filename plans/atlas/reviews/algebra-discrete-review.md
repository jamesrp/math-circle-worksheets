# Independent review: algebra and discrete families AD-01–AD-24

Reviewer: applied/probability author, independently reviewing the other author's volume. Date: 2026-09-25. Scope: the 24 cards in `families/algebra-discrete.json`, using `review_protocol.md`. This is mathematical and editorial review, not classroom observation or validation by a human educator.

**Result:** no blocking mathematical errors found. All 24 core instances, supplied solutions and boundary examples were checked. Two substantive launch ambiguities and one material-card clarification were reported to the editor and repaired during review; their current text was reread and the issues are closed. Two optional maintenance changes were also applied and reread. No material finding remains open. No AD source JSON was edited by this reviewer.

## Method and evidence

The first pass read each card's materials, learner launch and example problem without its solution. I worked each instance independently, then read and compared all solutions, boundaries, gates, bridges, extensions and session plans. Exact computations were subsequently encoded in [ad-independent-checks.py](ad-independent-checks.py). Its successful output is saved as [ad-independent-checks-results.json](ad-independent-checks-results.json). The script contains no imports from the family file and does not copy its answers as an input oracle. Assertions compare independently constructed objects and arithmetic with the review's expected results.

The script covers all 24 IDs, but its depth deliberately differs by topic. It exhaustively checks finite domains where feasible: all B4 antichains; all length-two Prüfer messages; all partitions of four residues; all F4 triples for multiplicative associativity and distributivity; all finite curve pairs; all edge patterns and necklace words. It checks exact examples, not general field theory, rational parametrization, module classification or universal properties. Those arguments were checked separately below. A finite test does not certify a general theorem.

Novelty was compared with `connections.md`, `prior-use-map.md`, the repository README, and the current Weeks 2–10 mathematical redesign notes. This confirms changes in mathematical question relative to the recorded plans. It does not establish what a particular returning child actually encountered. The actual-use log remains authoritative. The lesson-format source notes were reviewed for the distinction between a proposed timetable and demonstrated classroom pacing.

## Findings and closure

### Substantive clarification AD-06 — closed

The original launch said “above/below” rather than “at or above/below,” leaving equality ambiguous, and asked about an unnamed three-tile shortcut. This could make the learner's actual operation differ from meet/join or leave the investigation unspecified.

Exact repair, now present: explicitly allow a tile to be at or above/below itself; define join and meet; ask learners to compare `a meet (b join c)` with `(a meet b) join (a meet c)`. I reread this field after the editor applied it. The two recipes now specify the distributivity question without supplying its answer.

### Substantive clarification AD-18 — closed

Two chosen unit-vector images do not determine an arbitrary machine. The original launch needed the linearity assumption already present in the anchor.

Exact repair, now present: “A linear machine sends the horizontal unit arrow to u and the vertical unit arrow to v. Its full rule is T(x,y)=x u+y v.” I reread the repaired field. The transformed parallelogram and determinant interpretation now follow from the learner rule itself.

### Material clarification AD-20 — closed

The anchor defined E,F,H but the original materials only named them. Copying their actual entries onto the material-card specification prevents a facilitator from having to reconstruct the mathematical setup from prose elsewhere.

Exact repair, now present: `E=[[0,1],[0,0]], F=[[0,0],[1,0]], H=[[1,0],[0,-1]]`. I reread the repaired materials. This was a practical self-containment issue, not a mathematical defect.

### Optional maintenance — closed or unnecessary

- **AD-05, closed:** the core graph has only one diagonal, so the boundary's reference to “the diagonal crossing” was premature. The editor applied: “If a second diagonal is added, its crossing is not a vertex unless declared; declaring a junction changes the graph and the count.” I reread that exact field after the change.
- **AD-23, closed:** the `www.math.rutgers.edu` source URL returned an internal error through this review's web tool. The author's [sites.math.rutgers.edu mirror](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf) was accessible and has the claimed calculation. The editor switched to it; I reread the updated source entry. A single retrieval failure does not prove the old URL is permanently broken.
- **AD-16, no repair required:** I directly checked `Δ=−16(4(−1)^3+27·0^2)=64≡4 mod5`, hence nonzero. The current anchor states the correct nonzero-discriminant claim without its numerical expansion. Adding the expansion later is optional facilitator detail, not an unresolved defect. The finite enumeration does not need the formula, and the existing gate separates it from the elliptic group law.

## ID-by-ID mathematics, bridge and access review

### AD-01 — passes

A blue round object alone makes “every red object is round” true and its converse false; adding a red round object also works. The empty world makes both universal statements true and cannot be the counterexample. All sixteen presence/absence worlds on the four predicate types were enumerated. The two-vertex self-arrow extension separates the two quantifier orders as claimed. Objects and predicates instantiate finite structures exactly. The adult must preserve the universal/existential distinction, but no reading or arithmetic is essential. This is countermodel construction, distinct from solving one consistent set of Latin-square clues.

### AD-02 — passes

The displayed diagonal is 0111 and its complement 1000 is absent. All 65,536 ordered four-row lists were checked. For every row i, the new word disagrees at coordinate i; the same pointwise argument proves the infinite-sequence continuation once indexing and quantification are available. Listing all sixteen finite words defeats an overbroad finite claim, so the boundary is sound. The finite game is a complete lower stopping point. It differs from Week 6's information-gathering question: the opponent supplies a list and the learner constructs an omitted object.

### AD-03 — passes

Six two-element subsets attain the maximum. The six supplied chains partition all sixteen subsets, so any legal antichain takes at most one member from each chain. Independent exhaustive search over all 65,536 subcollections confirms maximum six. For three objects, combining the singleton and pair layers is indeed illegal. The five-object extension gives the correct candidate size ten but still asks for its certificate. The concrete containment relation supports serious optimality reasoning without needing the general Sperner theorem; broad theorem coverage is not implied by the small result.

### AD-04 — passes

Code (2,4) reconstructs edges 12,24,34. Independent decoding and encoding were inverse on all sixteen codes, and their image was exactly the sixteen connected three-edge subgraphs of K4. The label hypothesis is essential: there are only two unlabeled four-vertex tree shapes. General invertibility follows by repeatedly identifying the smallest remaining label absent from the remaining code; degree equals one plus remaining occurrences. Pruning and reconstruction are real learner decisions. The graph materials recur from Week 10, but communication by bijection is a different question from route inspection.

### AD-05 — passes; boundary wording repair closed

There are ten three-edge choices and exactly eight are connected trees; the two failures are the two triangles plus an isolated vertex. The stated cofactor has determinant eight. The graph is finite, connected and loopless, matching the sampled Matrix-Tree theorem. Its disconnected boundary is correct. The added second diagonal produces K4 only under the stated no-junction convention. The weighted continuation explicitly requires another checked theorem before use. Enumeration is a complete concrete task; determinants and Cauchy–Binet remain an honest higher gate. AD-04/GA-25 overlaps are intentional and require preserving the changed question.

### AD-06 — passes after substantive repair

All 25 ordered pairs in M3 have a unique meet and join. For distinct middle elements a,b,c, `a meet (b join c)=a` while `(a meet b) join (a meet c)=0`. The boundary correctly distinguishes any common upper bound from a least common upper bound. The subset deck supplies a comparison structure; the M3 tiles instantiate the actual nondistributive lattice. The repaired explicit two-recipe launch now makes this investigation usable. Divisor and vector-subspace extensions are valid, with linear algebra retained for the latter.

### AD-07 — passes

The closures of {a}, {c}, {a,c} are {a,b}, {c}, {a,b,c,d}. The seven closed sets are ∅, {b}, {c}, {a,b}, {c,d}, {b,c,d}, {a,b,c,d}. Enumeration confirms all intersections are closed and all six repeated rule-sweep orders agree on all sixteen starts. The general order-independence argument is stronger: each addition lies in every closed superset of the start; terminality therefore produces its unique least closed superset. The deletion boundary breaks that reasoning. Token addition is an exact closure mechanism, rather than a claim to have taught all of universal algebra.

### AD-08 — passes

Among all fifteen partitions of Z/4Z, exactly equality, parity, and the one-bag partition respect addition. The {0,1}/{2}/{3} proposal fails because representatives 0 and 1 of the same first bag can produce 0 or 2 when added to themselves. Translation propagates identified pairs and proves the classification without relying on enumeration. The extra unary operation breaks parity as stated. The trivial quotient is legal but forgetful, an effective boundary. Learners choose identifications and test representative independence; that is new relative to following a modular orbit.

### AD-09 — passes

The time is 5 in 0,…,11; no residue pair for moduli three and four is impossible. For moduli four and six, exactly twelve of twenty-four pairs occur, precisely those of equal parity; the displayed 1/2 pair is impossible. Uniqueness is modulo twelve and not as an unrestricted integer. A twelve-slot search genuinely instantiates simultaneous congruences. General Chinese-remainder arguments appropriately require coprimality and modular inverses/Bezout. The launch permits a failed attempt to invent inconsistent reports, followed by explanation, rather than assuming such a pair exists.

### AD-10 — passes

Eight triangular rows and a 6×6 square both use 36 counters. With x=2m+1 and y=2n, the equation becomes x²−2y²=1. The recurrence maps (17,12) to (99,70), hence (m,n)=(49,35) and 1225 counters. Algebraically `(3x+4y)^2−2(2x+3y)^2=x²−2y²`; positivity gives strict growth. Seven recurrence outputs were checked exactly. This proves infinitely many generated examples, not that no other positive solutions exist or that each is the next smallest. The card explicitly reserves completeness for descent. Figurate-number prior use remains an instance-level uncertainty.

### AD-11 — passes

In F2[t]/(t²+t+1), writing u=1+t gives t²=u, tu=1, u²=t. The nonzero inverses are 1↔1 and t↔u. The degree-two modulus has no root in F2 and is irreducible. All triples were checked for multiplication associativity and distributivity; addition is coefficientwise binary addition. The reducible t² boundary gives a nonzero nilpotent and no field. The Frobenius extension fixes 0,1 and exchanges t,u. The counters encode actual quotient arithmetic, while the proof gate correctly requires either quotient reasoning or all finite axioms, not just an inverse table.

### AD-12 — passes

The unit-square diagonal constructs √2. A doubled cube requires ∛2, whose polynomial x³−2 has no rational root and, being cubic, is irreducible. Its degree three cannot divide the power-of-two degree of a quadratic tower. The source's positive-exponent typo is correctly avoided by the card's inclusion of degree one. The necessary-versus-sufficient warning is correct. This is a genuinely advanced impossibility proof with field theory as a hard prerequisite; a close physical drawing does not constitute the result. The facilitator should use the stated concrete stopping point when the tower-law gate is unmet.

### AD-13 — passes

Only (0,0),(1,0),(0,1),(0,2) survive. No larger grid adds a survivor: surviving coordinates satisfy i≤1, j≤2, and cannot have both i,j positive. In k[x,y]/(x²,xy,y³), the four corresponding monomials span and are independent because every monomial in the ideal is divisible by a generator; no combination of the survivors lies in that monomial ideal. Removing xy gives six survivors. The x−y boundary is an important faithful-bridge guard: equality of classes is not deletion of both. Grid play is complete before the polynomial/vector-space proof gate.

### AD-14 — passes

The inverse of 2+3ε is 1/2−3ε/4. In general `(a+bε)(c+dε)=ac+(ad+bc)ε`; this has inverse iff a≠0, while ε is nonzero but squares to zero. The quotient normal form establishes that ε has not silently become zero. Evaluation at ε=0 preserves arithmetic but is noninjective. The polynomial derivative identity is exact under the formal rule, not a claim about a tiny real number. Coefficient choice offers exploration, and the card distinguishes this invertibility/nilpotence problem from AD-13's normal-form counting.

### AD-15 — passes

Substitution into y=t(x+1) gives the second point `((1−t²)/(1+t²),2t/(1+t²))`; t=1/2 gives (3/5,4/5). Conversely, every rational circle point except (−1,0) has rational slope y/(x+1) and is recovered. The base point requires the vertical tangent, which has no finite slope. Rational samples were checked exactly; the preceding algebra, not the samples, proves completeness. Pythagorean triples follow, but primitivity needs extra conditions, explicitly reserved by the card. This is an honest algebra stop below broader algebraic-geometry claims.

### AD-16 — passes

The seven affine F5 points are (0,0),(1,0),(2,1),(2,4),(3,2),(3,3),(4,0). Projectivizing yields Y²Z=X³−XZ²; at Z=0, X=0 and all nonzero Y give one projective point. The total is eight. Independent enumeration over F7 also gives seven affine points. The nonzero discriminant certificates are 4 mod5 and 1 mod7. Modular four arithmetic fails the field hypothesis. The actual learner task is finite solution-set enumeration; projective coordinates, nonsingularity and group-law associativity remain higher gates, so the accessible entry does not falsely stand for the entire elliptic theory.

### AD-17 — passes

For inputs 0,8, the invariant sum is eight and signed gap halves each synchronous round; after three rounds the markers are 3.5,4.5. Induction gives `(4−4/2^n,4+4/2^n)`. With step fraction a the signed gap factor is 1−2a, so unequal inputs converge exactly for 0<a<1. At a=1 they swap forever. Simultaneous use of old positions is clearly stated and essential. Choice of starts and step size provides a meaningful investigation. Connections to GA contraction/AP feedback are recorded as related but different questions, not wholly new objects.

### AD-18 — passes after substantive repair

The shear has determinant one, swap determinant minus one, and projection determinant zero. The vertical shear image has length √2, showing area preservation does not mean rigidity. Composing the displayed two shears in the stated order gives [[1,1],[1,2]], determinant one. The repaired linear rule supports both the parallelogram and invertibility discussion. Ordinary unsigned area is |det|; orientation carries the sign. Cutting is optional, reducing a practical access demand. Derivation and composition laws retain algebra/linear-algebra gates.

### AD-19 — passes

The kernel is spanned by (1,−1,1); together with (1,0,0),(0,0,1) this is a basis of Q³, and their images give the two standard target directions and zero. The transformed matrix is [[1,0,0],[0,1,0]]. The block inventory is two transmitted, one killed, no unreachable. The extension map has rank one and inventories 1/2/1 in that order. Source comparison confirms independent domain/target bases. The I versus 2I boundary correctly prevents confusing this equivalence with similarity. Keeping vector spaces as an entry gate is essential: mere routing tokens would lose the mechanism.

### AD-20 — passes; materials clarification closed

Direct multiplication gives [E,F]=H, [H,E]=2E, [H,F]=−2F. Thus `[[H,E],F]=2H` but `[H,[E,F]]=0`. The cyclic Jacobi terms for E,F,H are 0,−2H,2H. General expansion cancels twelve signed associative triple products; finite basis testing is a check, not its proof. A matrix commuting with the identity supports the boundary. The trace-zero span and [D,Mx]=I continuations are mathematically sound with their stated gates. The supplied E,F,H values now appear in materials. Partner calculations and table choices preserve investigation despite its unavoidable symbolic prerequisite.

### AD-21 — passes

The compatible catalog is (Ada,r),(Bo,r),(Cy,s),(Cy,t). Green has no pair; repeated red/blue identities cannot be merged. For any compatible assignment from any set X, h(x)=(u(x),v(x)) exists in the catalog and is forced by its two projections. This proves both existence and uniqueness, not merely a matching count. The number-of-pairs extension is the sum of products of color-fiber sizes. A one-color target gives the Cartesian product. Concrete pairing is a satisfying lower task; the all-X universal statement is deliberately an abstraction gate. Its categorical content depends on retaining that second question.

### AD-22 — passes

Among all 32 edge patterns, the four cycles are 0,T1,T2,T1+T2. The face-ABC boundary subspace is {0,T1}, giving exactly two classes. No faces gives four classes; both faces gives one zero class. Every face boundary has even vertex incidence, so a legal move preserves cycles. The outer square survives with only ABC filled and dies with both faces. Coefficients and legal faces are explicit, preventing the common false identification of visible regions with available 2-cells. The exact graph overlaps AD-05/GA-25, but quotienting by face boundaries changes the question substantively.

### AD-23 — passes

The difference (2,1)−(1,2)=(1,−1) is not an actual finite module's dimension pair. The two central idempotents split each module into two rational vector spaces; R-linear isomorphism preserves both parts. All finite pairs are sums of the projective summands e1R,e2R, yielding the monoid N². Its group completion is Z² by coordinate differences. Free modules have pairs (n,n), while (1,0) is projective nonfree. Equal total dimensions do not imply R-isomorphism. This is an honest advanced card: counters alone are expressly called preparatory, not a full K-theory lesson. The source's product computation agrees.

### AD-24 — passes

The six listed binary rotation orbits have sizes 1,1,4,4,2,4. Fixed counts 16,2,4,2 average to six. Each orbit contributes |G| to the count of fixed pairs by orbit–stabilizer, which establishes the averaging principle rather than merely matching two counts. Allowing reflection happens to leave this particular binary count unchanged. For three colors on three beads the rotation/dihedral counts are eleven/ten, independently enumerated. The precise equivalence rule excludes turning over and exchanging colors; this avoids an ill-posed symmetry puzzle. Stabilizer-sensitive counting is new relative to Week 3 return-time questions.

## External sources independently sampled

These are review checks in addition to the author's source pass. They do not imply all citations in all 24 cards were independently reopened.

| Cards | Actually inspected source and locator | What was checked |
| --- | --- | --- |
| AD-03, AD-05 | [Stanley, Topics in Algebraic Combinatorics](https://math.mit.edu/~rstan/algcomb/algcomb.pdf), Cor. 4.8; Thm. 9.8, PDF pages 42 and 142–143 | Boolean-lattice Sperner claim; connected finite loopless graph and Laplacian cofactor hypotheses. The Prüfer appendix was located, but its general proof was not separately source-audited in this review; the finite bijection and deletion argument were checked directly. |
| AD-12 | [Judson, §21.3](https://judsonbooks.org/aata-files/aata-html/fields-section-constructions.html), Lemma 21.3.6, Thm. 21.3.7 and cube-doubling paragraph | Quadratic extensions and degree obstruction; noticed the printed k>0 convention omits degree one. The card handles that correctly. Other typographical problems on that webpage do not replace the direct tower argument. |
| AD-19, AD-20 | [Etingof et al., representation-theory notes](https://math.mit.edu/~etingof/replect.pdf), Ex. 5.8, PDF page 81; Def. 1.39, Ex. 1.40/1.46, PDF pages 15–16 | Complements to kernel/image give the three one-arrow indecomposables; Lie/Jacobi definition and sl2 relations have the card's conventions. |
| AD-21 | [Fong–Spivak, Seven Sketches](https://ocw.mit.edu/courses/18-s097-applied-category-theory-january-iap-2019/a4175d61479a35340d6307ae5e48ef5a_18-s097iap19textbook.pdf), §3.5.3, PDF page 125 | Colored compatible-pair pullback construction. The arbitrary-X existence/uniqueness argument was also proved directly. |
| AD-22 | [Stacks, §12.13](https://stacks.math.columbia.edu/tag/010V), chain-complex definition and formula following Lemma 12.13.3 | Correct chain convention H_i=ker(d_i)/im(d_(i+1)), distinct from the later cochain convention. The small complex was built directly. |
| AD-23 | [Weibel, K-book chapter II](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf), §1; §2 and paragraph preceding Ex. 2.1.4, PDF page 6 | Projective-class monoid, group completion, and product-ring computation. The Q×Q decomposition was checked directly, without needing the general semisimple-ring theorem. |

## Limits and disposition

The volume is suitable to proceed to plan-PDF production; no material finding from this review remains open. This judgment means the mathematical instances and claims survived the checks described here; it does not mean the cards are classroom-tested or that every proposed advanced continuation has been developed.

The full general proofs behind infinite Pell classification, weighted Matrix-Tree, arbitrary Gröbner normal forms, elliptic group-law associativity, general quiver classification, topological invariance and higher K-theory remain outside this review. The cards largely say so explicitly. No new source claim is made for these continuations. Source links not in the sample table were not rechecked independently during this review.

Minute-by-minute timings and small preparation estimates remain proposals. Advanced cards AD-12, AD-19, AD-20 and especially AD-23 assume substantial mathematical readiness; they should not be scheduled for learners lacking those gates merely because some props are concrete. The lower stops elsewhere remain meaningful investigations in their own right. Future actual use must record exact instances, rule misunderstandings, time spent and learner explanations before assigning classroom-validation status.
