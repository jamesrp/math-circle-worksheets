# Independent design review: AP1

Reviewer: AD1 author. September 25, 2026. **Design review passed after five repair categories were closed.** This review covers AP-02, AP-03, AP-04, AP-05, AP-06, AP-08, AP-09 and AP-10: all **51 student prompts and eight guide extensions**, all page intros, figures, prerequisite gates, sources, prior-use notes, and the author’s exact check program. No PDFs are covered by this design review.

I first extracted the student prompts, model assumptions and figure data without the answer keys, solved the exact instances and general arguments, then compared with the keys. My independent [check program](review-ap1-checks.py) and [results](review-ap1-checks-results.json) corroborate the numerical instances and add checks of the tied-score extension, varied-block extension, fixed-size bag optimum, actual suffix-word certificates and spring change of basis. I also ran a temporary copy of the author’s checker outside the author-owned files; it passed. The proof reviews below are not replaced by either computation.

## Findings and repair closure

1. **AP-04, prompt 4 solution — statistical terminology.** “Consistency does not imply accuracy” risked contradicting the technical meaning of a consistent estimator. The owner replaced it with “repeatedly giving the same answer does not make it accurate.” Reread and closed.
2. **AP-06, page 3 rules — unequal subintervals.** “Retain the half-bracket” was inaccurate for an accepted Newton point that is not the midpoint. It now says to retain the subinterval whose endpoints have opposite signs. Reread and closed.
3. **AP-06, prompt 4 solution — index convention.** The expression `x_next=x_previous_previous` was ambiguous about which iterate was “previous.” It now specifies x_(n+1)=x_(n−1), distinct consecutive iterates and a nonroot current iterate. Reread and closed.
4. **AP-09, guide extension — attainable ratio.** For positive middle stiffness, the opposite/equal frequency ratio is strictly greater than one. “Any positive rational ratio” is now “any rational frequency ratio greater than 1.” Reread and closed.
5. **Across data — joined math/prose.** The first version contained strings such as “integerθstays,” “a100%rule,” “17a50%plausible” and “per formance.” The owner applied a prose-spacing cleanup. I reread all named examples and the repaired task keys; they are corrected. Final rendering must still check ordinary mathematical spacing and wrapping visually.

No numerical error or invalid main theorem remains in the reviewed data. The author preserves the calculus gate rather than substituting an unrelated lower-level activity.

## AP-02: all prompts 1–6 and the odds extension

Independent calculation: one draw gives likelihoods 2/3 versus 1/3. With equal prior odds, red gives A probability 2/3; the deliberate-red messenger has likelihood one from both bags and leaves 1/2. With replacement from one selected bag, the RR likelihoods are 4/9 and 1/9, giving 4/5. RB likelihoods are both 2/9; differing-color likelihoods both 4/9; at-least-red likelihoods 8/9 and 5/9, giving 8/13. The A,B,B ticket prior balances red masses (1/3)(2/3)=(2/3)(1/3), giving posterior 1/2.

For equal chosen bag size n and positive red counts a,b, posterior A is a/(a+b); this is maximized by a=n,b=1. Hence n/(n+1) is sharp for that fixed size. There is no overall finite optimum if bag size is unrestricted, which the key explicitly states. Equal positive red fractions are necessary and sufficient for an unchanged fair prior. For k reds the likelihood ratio is 2^k, proving the extension formula p2^k/(p2^k+1−p) for 0<p<1.

The exact labeled-counter deck and two 3×3 grids suffice; replacement, same-bag repetition and distinct B tickets are all explicit. The meaningful destination is dependence on evidence selection, not merely counting red objects. Fractions and finite sample-space reasoning are correctly labeled. The fixed-size extremal prompt must retain “state the bag size” and its no-global-optimum guide answer.

## AP-03: all prompts 1–7 and the tied-score extension

The score sum is 18. Trained sum S gives mean difference (2S−18)/3, so S=15 yields difference 4. A-containing triples are in bijection with choices of two of the other five people; pairing each with its complement gives 10 disjoint pairs and all 20 assignments. Their sums are recorded independently in the checker. Only DEF has sum 15 and only ABC has sum 3. Thus UP is 1/20 and a prespecified absolute-tail rule is 2/20. The directional rule chosen after observing which group wins selects either of those extremes, so its actual false-alarm chance is 1/10. An exact nonempty tail cannot be below one elementary outcome's probability 1/20.

The paired design has increments 6,4,2 over base sum 3, yielding sums 3,5,7,9,9,11,13,15, each assignment equally likely. Its upper tail is 1/8. In the tied extension, the top sum 5 requires both labeled score-2 people and either labeled score-1 person, so two of twenty assignments tie at the maximum: 1/10.

The design correctly fixes scores only under the sharp no-effect assumption and uses the actual assignment law. It does not invert a p-value into a probability of the null or generalize to a pilot population without a model. Complementary boxes and the three-coin tree provide sufficient exact scaffolds while avoiding precomputed tail counts. The arithmetic is modest but the null/randomization reasoning is a genuine gate. No accidental Week 1–10 or accepted-ten repeat was found.

## AP-04: all prompts 1–6 and the varied-block extension

The two example worlds have total means 3 and 5 but the identical observation law concentrated on 1, because the inaccessible identifiers are the only changed entries. Any number of those restricted readings therefore fails to distinguish them. A single hidden audit distinguishes the specified homogeneous example worlds but does not determine arbitrary hidden contents; the key preserves this scope.

For full two-draw sampling, value pairs (1,1),(1,5),(5,1),(5,5) have equal probabilities. Means 1,3,5 have probabilities 1/4,1/2,1/4 and expectation 3. The restricted distribution is a point mass at 1 and has bias −2. Equal homogeneous blocks force the block estimate 3. With block sizes 2 and 6, the target is 4 and weights 1/4,3/4 repair the ordinary mean 3. Generally expectation of the block-size-weighted sample is the finite-population mean; homogeneity is what makes these particular estimates exact.

The extension's four equally likely value combinations give means 2,3,3,4, expectation 3. The varied blocks remove certainty without introducing bias. The closed terminology repair prevents the wrong use of “consistency.” Blank hidden worlds on page 1 preserve the learner's choice; W/Z must remain delayed until after that task. The graphical probability scaffolds have the necessary x values and axis purpose.

## AP-05: all prompts 1–7 and changed-error extension

For offsets [a,b], capture is equivalent to −b≤E≤−a, independent of the fixed target. Original offsets [−1,1] capture errors −1,0,1, hence 3/5. Covering four of five integer errors needs width at least three. The only minimum-width error blocks are [−2,1] and [−1,2], giving reflected offset rules [−1,2] and [−2,1]. The fixed-integer-offset class and inclusive endpoints are explicit, so the optimization claim is not overgeneralized to arbitrary random sets. Width four with offsets [−2,2] covers every bounded error.

The independent-coin rule covers on all five heads cases and none of five tails cases. Its coverage is exactly 1/2 for each fixed target, even though the disclosed tails result is knowingly incompatible with the error bound. At X=7 the compatible integer targets are 5 through 9, excluding 17. This is an honest example separating procedure coverage from posterior belief. Comparison with the width-three rule properly permits different practical criteria instead of asserting an unstated universal optimum. Changing the error law to support only ±2 gives zero coverage for the original narrow interval.

The number lines and error/coin grid are sufficient. Signed arithmetic, fixed-target reasoning and independent randomization are explicit gates. The optional randomized-procedure page is not marketed as an elementary slogan about confidence intervals.

## AP-06: all prompts 1–6 and generalized guard extension

Independent derivation gives N(x)=2x³/(3x²−5). Starts 0,1,−1 yield respectively the fixed root and the exact ±1 cycle. From 2, the next two values are 16/7 and 8192/3661; oddness gives the negative-start values. The roots are 0,±√5; undefined tangent steps occur at ±√(5/3), where the function is nonzero. The parity argument proves the two requested distant iterates exactly. A repeated nonroot warning detects failure but does not itself choose a convergent next step.

For the guarded run: first proposal −1 is rejected from central interval [3/2,5/2], giving midpoint 2 and bracket [2,3]. Proposal 16/7 is inside [9/4,11/4], and f(16/7)=176/343>0, giving [2,16/7]. Continuity and opposite endpoint signs preserve a root. Any point in the central half leaves either possible retained subinterval with width at most 3/4 of the previous width. Therefore width≤2(3/4)^n; exact rational inequalities show 18 does not meet this worst-case 0.01 bound and 19 does. The actual method may finish sooner. The δ guard gives factor 1−δ for 0<δ≤1/2; δ=1/2 is midpoint-only.

The tangent plot is illustrative; exact formulas decide the cycle and acceptance. Calculus is retained as a core gate, with continuity explicitly used in the safeguard. The new cubic and bracket certificate distinguish this from original GA-28 and the accepted AP-07 Euler investigation. Repairs close the only rule/index ambiguities.

## AP-08: all prompts 1–6 and general-m extension

A machine accepting precisely zero-red strings passes every test through length two but first fails at RRR. The supplied two-room graph has exactly that behavior. Residue rooms 0,1,2 with R cycling and B looping are correct by induction on the input length. Empty,R,RR are pairwise distinguishable: empty suffix separates the first history from either other history; suffix R distinguishes R from RR. Two rooms cannot hold three pairwise distinguishable histories, because the same suffix from one room has one determined result.

For the simultaneous target, room pairs (red mod 3, blue mod 2) give six states. The four test answers are YES,NO,YES,YES; RBRBRBB contains three R and four B. For any distinct pair of the six listed histories, appending enough R and B to cancel the first history's remainders accepts the first and leaves a nonzero remainder in the other. The independent checker supplies all fifteen concrete suffix certificates. The identical argument gives m rooms necessary and sufficient for m≥1; m=1 is correctly handled by one accepting room.

The state-only-memory convention, deterministic outgoing arrows and acceptance criterion are explicit. The intentionally bad machine appears only after learner-design space, and correct three/six-state edges are withheld. This is a strong low-arithmetic proof investigation. It revisits state diagrams used elsewhere but introduces a different lower-bound mechanism.

## AP-09: all prompts 1–7 and stiffness extension

For x=(u,v), determinant of the displacement/force pair is u(u−2v)−v(−2u+v)=u²−v². Thus the only nonzero proportional directions have u=v or u=−v; direct substitution gives factors −1 and −3. Decomposition coefficients are (u+v)/2 and (u−v)/2, proving existence and uniqueness. Adding/subtracting force equations gives F1+F2=−S and F1−F2=−3D. The independent matrix change-of-basis calculation returns diagonal stiffness diag(1,3).

The proposed motion 2 cos(t)(1,1)+cos(√3 t)(1,−1) differentiates twice to the stated force and has all four initial conditions. Uniqueness of the linear ODE may be supplied, as identified by the key. Returning to positions (3,1) forces cos T=cos(√3T)=1. For positive T this would make √3 a ratio of positive integers, impossible. The claim is exact, and it does not deny arbitrarily close approximate recurrence. Changing middle stiffness to k retains equal factor 1 and gives opposite factor 1+2k; ratio two requires k=3/2. More generally integer ratio m≥2 requires k=(m²−1)/2. The repaired rational-ratio continuation respects k>0 and hence ratio>1.

The physical assumptions and common positive displacement direction are explicit. Separate rest marks avoid equating position with displacement. The algebra-only stop is substantial classification and decoupling, not falsely advertised oscillation physics. Time, recurrence and differentiation remain behind the calculus gate. No prefilled eigendirection boxes should be introduced in production.

## AP-10: all prompts 1–6 and arbitrary-stiffness dual extension

Under force six, series springs of stiffness 2 and 6 share force and extend 3 and 1, total four. Parallel springs share extension 3/4 and carry forces 3/2 and 9/2. Giving each force three would require incompatible extensions 3/2 and 1/2. Guided common bars and static massless connectors make these constraints explicit; merely drawing two springs beside one another would not suffice.

A three-leaf recursively series-parallel network has a final join S/P and a two-leaf child S/P. These four structural cases give stiffnesses 1/3,2/3,3/2,3 and force-six extensions 18,9,4,2. No stiffness one appears, proving the target impossible in the stated network class. Mirroring and associativity do not create new responses. The unit-leaf dual has reciprocal stiffness by induction using the two rational combination identities. Swapping each node in the tree exchanges series/parallel and also reciprocates unit-force extension.

Four leaves admit both S(P(1,1),P(1,1)) and P(S(1,1),S(1,1)), each stiffness one. This changes the resource count and does not contradict the three-leaf impossibility. Arbitrary positive leaf stiffnesses require reciprocating the leaves as well as swapping joins; the base case otherwise fails. The independent checker generates construction trees without early response deduplication and obtains the same three-leaf response set.

The exact abstract syntax and bar constraints are sufficient for the custom renderer. Algebra/fractions remain visible prerequisites. This has a complete classification and reciprocal proof, rather than a spring demonstration standing in for the mathematics.

## Source evidence and production gate

I independently opened every cited source URL. I checked the Open-access probability chapter contents/Bayes locator, Think Stats chapters 8 and 9 and the actual §9.2 permutation mechanism, NIST's confidence interpretation, the MIT Newton material and automaton formal-definition/computation slides, Tong §2.6, and Bower's linear-elastic section. The data correctly distinguish these framework sources from independently derived finite examples. In particular, Bower's continuum section is not claimed to contain the finite series-parallel duality theorem.

The mathematical/design gate is closed. Production still requires all student pages at full size and all guide pages on contact sheets plus dense-page checks. Key visual risks are accidental RR-grid answer filling, prematurely showing hidden W/Z cards, misdrawn tangent steps, DFA arrow/acceptance ambiguity, and spring bar constraints. This review makes no classroom-pilot claim and no PDF quality claim.
