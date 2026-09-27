# Independent AD-01–08 design review

Reviewer: GA1 author. September 25, 2026. **All eight families, all 50 student prompts and all eight guide-only extensions were read and independently solved.** I also read the design note, exact mathematical checker, diagram data, gates, prior-use notes and source-evidence descriptions. Author files were read-only. A re-run of the checker passed with its result-file write captured in memory, so no author-owned file was changed.

The designs have substantial mathematical destinations and preserve their genuine prerequisite gates. Four small but important rule/proof-scope repairs were sent to the author. All four were repaired and independently reread; design review is now closed with no outstanding findings. No renderer or PDF was reviewed.

## Findings and closure

1. **AD-03, page 1 intro:** explicitly state the legal-collection rule: no two distinct selected cards may contain one another. The title strongly suggests it, but the body defines “inside” and then asks for a “legal collection” without making that rule explicit.
2. **AD-05, page 1 intro:** explicitly define minimal connected: every vertex is connected, and removing any kept edge disconnects the graph. This distinguishes inclusion-minimality from physical shortest roads or merely finding a small network.
3. **AD-05, page 4 supplied theorem:** say “finite connected simple graph.” The given off-diagonal −1 formula is for simple graphs; excluding loops alone does not exclude parallel edges. All actual instances are simple, so no calculations change.
4. **AD-04, prompt 3 solution:** explicitly establish the degree/occurrence invariant in the **decoded tree**, not only in an already encoded tree. A vertex receives one incident edge at its own removal (or the final pair) and one for every appearance in the message before removal; thus its degree equals occurrences plus one, also for every suffix. This makes `encode(decode(word))=word` explicit as well as `decode(encode(tree))=tree`, completing the counting bijection without an implicit step.

## AD-01: every/some counterworlds

Checked prompts 1–6 and the arrow extension. Independently, the required red witness must be RC and a counterexample to circle→red must be BC, requiring two different cards. Only RS breaks red→circle. With the square-existence promise, RS is unavailable and BS is required, forcing claims A and D. Claim B needs BC plus a square, so its least counterworld has two cards; C fails in the one-card BS world.

For either BS alone or the empty tray, the universal has no counterexample but the existential has no witness. RS+RC makes “not every red is a circle” true and “every red is a square” false. BS alone reverses their truth values. The one-person arrow world needs a self-arrow and therefore fails the no-universal-recipient condition; two self-arrows give the minimum two-person witness.

The four-type mat is sufficient; monochrome R/B labels must accompany colors. The empty-domain convention is honestly marked as a game rule, while BS already demonstrates the important empty-class distinction in a nonempty domain. No cardinal arithmetic or first-order theorem is substituted for actual witness reasoning. The year-1 truth/Week 5 overlap is acknowledged.

## AD-02: escaping a pattern list

Checked prompts 1–6 and the three-symbol extension. The supplied diagonal is `0111`, whose complement is `1000`. Direct witnesses against the rows can be positions 1, 1, 3 and 2. Any row-position bijection creates one protected mismatch per row; repeated rows or changed off-diagonal entries cannot remove those assigned witnesses. Four distinct supplied rows leave twelve of sixteen words; five rows leave at least eleven; the four possible prefixes times four suffixes supply all sixteen.

For an infinite list, defining `b_i=1−s_i(i)` gives a definite mismatch at every proposed row i, including 137. Prepending b merely changes the input list; diagonalizing again gives a new missing sequence, which differs from b at position 1. The argument does not promise one fixed sequence missing from every list. For three symbols, cyclically changing the assigned symbol always differs, so the same mechanism works.

The matrix data are complete and the method card is intentionally later. The infinite page keeps its actual arbitrary-index gate and explicitly revisits GA-29's diagonal mechanism. Four finite rows are not presented as a proof of the infinite assertion. No repairs needed.

## AD-03: maximum nonnested collections

Checked prompts 1–6 and the five-symbol extension. The six two-symbol sets form an antichain. I independently audited every item of the six-chain certificate:

`∅–A–AB–ABC–ABCD`; `B–BC–BCD`; `C–AC–ACD`; `D–AD–ABD`; `BD`; `CD`.

Each consecutive containment is strict, all sixteen cards appear exactly once, and at most one card can come from each chain. Thus the upper bound six matches the construction. Empty or full cards permit no other selected card.

With A required, all containing-A cards and the empty card are barred, leaving the seven nonempty subsets of BCD. The chains `B–BC–BCD`, `C–CD`, `D–BD` bound additional choices by three, and `{A,BC,BD,CD}` attains four. Complementation turns a prescribed triple into a prescribed singleton and reverses containment. Any mixed-size antichain other than the trivial empty/full cases includes a singleton or triple (only sizes 1,2,3 remain), hence has at most four. This validates the stronger facilitator statement.

For five symbols, a k-set occurs as an initial segment in `k!(5−k)!` of the 120 permutations. Each permutation chain contains at most one antichain member, so `sum 1/binomial(5,k)≤1`; denominators are at most ten, proving size≤10. All pairs attain ten. This is a complete argument, not extrapolation from four symbols.

The whole deck and six blank chain strips are sufficient. Delay the strips/hints until after searching if their count would prematurely disclose the bound. The explicit legal-rule repair above is needed; all mathematical values are correct.

## AD-04: tree communication and inverse codes

Checked prompts 1–6 and the convention extension. Independent encodings: X deletes 2 then 1 and sends `(1,3)`; Y deletes 1 then 3 and sends `(3,2)`. Decoding `(3,1)` chooses missing leaves 2 then 3, producing edges `23,13,14`. With five labels, `(4,4,2)` removes 1,3,4 and gives `14,34,24,25`, with degrees `1,2,1,3,1` and leaves 1,3,5. The distinct-entry message `(1,2,3)` gives path `4–1–2–3–5`, hence exactly two leaves.

A suffix on m survivors has m−2 entries, so at least two labels are absent and the smallest is well-defined. A label removed as absent cannot appear in a later suffix. Thus the chosen neighbor survives, and backward attachment proves the decoder returns a tree. In that tree each message occurrence adds one incident edge, while every vertex has one final edge at removal or at the final pair. This proves the required degree invariant at every stage, and hence both inverse identities. There are therefore `n^(n−2)` labeled trees for n≥2; n=2 has the empty code and one edge. For four vertices, the four repeated messages give stars and the other twelve give paths.

Largest-leaf encoding of X deletes 4 then 3, giving `(3,1)`; smallest-leaf decoding gives a different tree as claimed. Labels rather than drawings are counted. The optional general argument honestly needs induction. The figures specify all required edges and labels. Add the decoded-tree invariant explicitly as requested above; no finite-answer repairs are needed.

## AD-05: road closure and determinants

Checked prompts 1–8 and the Matrix-Tree extension. Independently, a minimal connecting graph has three edges. With no diagonal AC, omit any one perimeter edge: four cases. With AC, choose one edge incident to B from AB/BC and one incident to D from CD/DA: four more. Closing AC leaves four; closing AB leaves the perimeter path BC–CD–DA plus the two AC trees obtained by pairing BC with CD or DA: three. Symmetries preserving AC act transitively on perimeter roads, so every perimeter closure leaves three.

With both diagonals available, no-diagonal, one-diagonal and both-diagonal classes have sizes 4,8,4. In K4 all six edges are equivalent; the 16 trees have 48 total edge occurrences, giving eight containing each edge and eight surviving its removal. Equivalently any edge deletion recovers the original five-road graph up to relabeling.

I reconstructed the Laplacian with diagonal `3,2,3,2` and −1 at exactly the five adjacencies. Deleting D gives determinant `15−4−3=8`; deleting A gives `2(6−1)−2=8`. Every row of the full matrix sums to zero, so its determinant is zero. In the supplied proof sketch, Cauchy–Binet sums squared incidence minors; a cycle gives dependence and a spanning tree gives determinant ±1 by leaf expansion. Acyclic n−1-edge graphs on n vertices are connected, so those exhaust nonzero cases. The sketch is valid with its stated Cauchy–Binet gate.

The road diagram and distinct crossing convention are exact. The practical payoff goes beyond accepted GA-25's tree/exchange work: which road closure preserves the most options? Add the explicit minimality rule and simple-graph theorem scope. The advanced determinant page is properly separated from the finite counting core.

## AD-06: distributivity versus missing operations

Checked prompts 1–6 and the vector-space extension. For X=AB,Y=AC,Z=BC, both recipes yield AB. Membership of a symbol is the Boolean equivalence `x and (y or z) = (x and y) or (x and z)`, proving the identity for all sets.

In the five-tile diamond, comparable pairs use the smaller/larger input as meet/join; distinct middle tiles have meet 0 and join 1. These cases exhaust all pairs. Taking X=a,Y=b,Z=c gives left result a and right result 0, so all operations exist although distributivity fails. The same holds for each of the six permutations of distinct middle tiles.

In the six-tile order, common upper bounds of p,q are r,s,1, with neither r nor s least; dually the lower bounds of r,s are 0,p,q with no greatest. After adding r<s, the only incomparable pair is p,q, with meet 0 and join r. All other pairs are comparable, so the diagram is a lattice. The reverse repair is symmetric.

For the subspace continuation, two distinct lines in a two-dimensional vector space intersect only at zero and span the plane; any three distinct lines plus 0 and the plane form the required five-element sublattice. “Join is span/sum, not set union” is an essential and correctly stated distinction.

The cover data are sufficient. The renderer must ensure apparent line crossings do not create nodes or comparisons and clarify that relative page height alone is not an order relation. Gates are honest: arithmetic is unnecessary, but least/greatest-bound reasoning is substantive. No design repairs needed.

## AD-07: positive-rule closure

Checked prompts 1–6 and the closure-axiom extension. From `{a,d}`, the legal first additions b or c both lead to all four. Every full generator must contain a, which no rule creates. A alone only gives ab, so the two minimum generators are ac and ad. The seven closed sets are `∅, b, c, cd, ab, bcd, abcd`; this follows by the direct restrictions a⇒b, d⇒c and bc⇒d.

The closed sets ab and c have union abc, which forces d. Any rule whose prerequisites occur in an intersection has them in both sets, so its output is in both; intersections stay closed. A completed run terminates after at most four minus starting-size additions and is contained in every closed superset of the start by induction. Comparing two terminal sets gives mutual containment. This is the least-closed-superset proof of order independence, and immediately yields extensiveness, monotonicity and idempotence.

Replacement a→b versus a→c has distinct terminal outcomes because the premise disappears. It violates the persistence assumption even though both branches terminate. All rules are visible, no memory game is smuggled in, and the subset cards suffice. The new union-trigger payoff and general proof are substantial. No repairs needed.

## AD-08: representative-independent operations

Checked prompts 1–6 and the modulo-six extension. The supplied partition `01|23` fails because 0+0 and 1+1 have the same input bags but different output bags. `02|13` gives the usual parity table and succeeds for all sixteen representative pairs. In `02|1|3`, adding 1 to 0~2 forces 1~3, so one merge is necessary and sufficient. In `01|2|3`, translating 0~1 repeatedly forces all four equivalent, requiring two pairwise bag merges.

Any nontrivial identified pair in a four-ring is adjacent or opposite. Adjacent forces the indiscrete partition; opposite forces parity, and any additional identification forces the indiscrete partition. Together with singletons these are exactly the three valid partitions. The unary map with outputs `0,0,1,1` destroys parity via equivalent inputs 0 and 2 whose outputs fall into different parity bags; singleton and one-bag partitions remain valid.

For modulo six, the 0-class is a subgroup because translation respects equivalence; each class is its coset. The possible subgroups are `{0}`, `{0,3}`, `{0,2,4}` and all residues: an element 1 or 5 generates everything, 2 or 4 generates the even class, and adding 3 to that yields everything. Hence the four partitions stated in the key are exhaustive. The proof needs the explicitly stated coset gate, which is retained.

All ring/table/machine data are adequate. Independent choice of the two representatives, including equal inputs, is explicit. Parity is not pre-announced on the first page, and the final extra-operation task demonstrates why quotient validity depends on the operations. No repairs needed.

## Evidence boundaries

The author checker passed, including its complete finite enumerations. My conclusions above are based on independent derivations rather than merely that re-run. Source-evidence descriptions match the used mathematics: Open Logic for semantics/diagonalization, Stanley for antichains/trees/Matrix-Tree, and Burris–Sankappanavar for lattice/closure/congruence definitions. I reviewed those source records and application scope, not a second full pass through every cited book. General proof claims were checked as written arguments.

No PDF usability claim is made. During production, especially inspect the usable deck/cards, two-dimensional order diagrams, original-versus-added diagonal crossing, dynamic leaf ledger, staged answer disclosure and actual work area.

## Closure record

The author applied all four repairs on September 25. I reread the exact changed text: AD-03 now gives the no-two-nested-selected-cards rule and permits partial overlap; AD-05 defines minimality by deletion and limits the supplied theorem to simple graphs; AD-04 explicitly proves the residual decoded-tree degree formula and both inverse identities. All four findings are closed. **AD1 design is approved for production**, subject to the separate required PDF review.
