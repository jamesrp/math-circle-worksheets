# AP3 independent design review

**Status: CLOSED — approved for PDF production.** Reviewer: expand_ga1, 2026-09-26. All eight assigned families, all 48 student prompts and all eight guide extensions were independently calculated or proved and compared with the complete keys. The original adult questions, figure specifications, prerequisite gates, preparation/timing, prior-use distinctions, source scope, author design note and full check program were read. No blocking mathematical or design repair is outstanding. This is design approval, not PDF approval or classroom validation.

The author program was read and run; all eight groups pass. Independent supplementary code and results are `review-ap3-checks.py` and `review-ap3-checks-results.json`. Its stored data hash identifies the reviewed version. The finite checks support the explicit general proofs below; they do not establish unbounded-time, arbitrary-parameter or all-real-input claims by sampling.

## AP-19 — inverse channel survey

Checked prompts 1–6 and the effective-depth extension. Writing u=H₁^(−1/2), v=H₂^(−1/2) gives u+v=5/6 with u,v strictly positive. The three first-depth choices produce second depths 9, 4 and 144/49. The equal-depth interpretation gives 144/25, and H₁ must exceed 36/25; equality would require an infinite second depth. Thus the claimed ambiguity is the complete open segment, not a few examples.

For a receiver at x, its row is (min(x,6),max(x−6,0)); against the total-time row its determinant has magnitude 6 min(x,12−x). Exactly the interior positions are independent. Solving gives u=S/x on the first half and v=(T−S)/(12−x) on the second. The printed positivity intervals follow by requiring both recovered coordinates to be positive, including agreement at x=6. The reports at 3, 6 and 9 recover (4,9).

Independently inverted all four timing endpoints in prompt 5; the printed reciprocal-square fractions and their ordering agree. Depths remain coupled by the total-time equation, so the warning against an independent rectangle is necessary and correct. Each slowness error has magnitude |e|/min(x,12−x); maximizing the denominator uniquely gives x=6. The key distinguishes the algebraic bound from truncation by physical positivity. The effective speed is the harmonic mean of the two speeds, and monotonicity of reciprocal squares puts effective depth between actual depths. It is not their arithmetic average. The unknown-g scaling is also correct.

The hidden, unscaled bed specification prevents a geometric answer leak; endpoints and the interface must be labeled, and receiver position must be selectable. The task supplies its wave law and additive travel-time model, so algebra and square roots are the actual gate. The payoff is an inverse problem with a chosen informative measurement and quantified conditioning, distinct from AP-27's dynamic sensor delay.

## AP-20 — resource prices and integer restrictions

Checked prompts 1–6 and every real-capacity regime. Direct enumeration agrees with the seven feasible whole plans for stock (5,4), uniquely optimized by (2,1) at 10. The suggested greedy claim fails at two B products, revenue 8. Solving the two recipe price equations gives (r,b)=(2/3,5/3). The exact slack identity is

`(2/3)(R−2x−y)+(5/3)(B−x−2y)=(2R+5B)/3−3x−4y`.

Positive prices and nonnegative resource slacks prove the bound for all real feasible quantities. Equality requires both resource constraints tight, and their nonsingular system proves uniqueness. At stock (4,4), fractional quantities 4/3 each attain 28/3; integer production can make at most two products, hence at most 8 points, attained by two B. This closes the gap left even after rounding the fractional bound down to 9. The extra red/blue cases yield 10/11. Whole-product gains are 2 points and 3 points; fractional gains are 2/3 point and 5/3 points. The different baselines account for this distinction. For blue stock 4, independently derive breakpoints R=2,8 and values 4R, (2R+20)/3, 12. Each printed plan and each of the three price certificates is feasible in its range, including shared endpoints. No strong-duality theorem is needed.

Counters and separate used/leftover records suffice. Fractional production is introduced explicitly before its proof; variable x,y separates quantities from the blue price b. The final choice of which counter to add is substantive. Recipe icons must display multiplicity without supplying the best bundle. Gates and timing are credible as unpiloted estimates.

## AP-22 — private randomizers and minimax

Checked prompts 1–6, including ε=0 and ε=1/3, and the positive-diagonal extension. The independent payoff polynomial is 1−p−q+3pq. A fixed p guarantees min(2p,1−p), uniquely maximized at p=1/3; a fixed q caps payoff at max(2q,1−q), uniquely minimized at q=1/3. Both values are 2/3. Weighted averages of pure responses provide the universal certificates. Indifference alone is not used as a proof.

Against q=3/4, pure U uniquely earns 3/2 but has worst-case payoff zero. The near-optimal inequalities yield precisely the printed intervals and fractions at ε=1/15. Revealing the actual row allows a zero-payoff response every round. A shared three-way ticket instead gives correlated diagonal outcomes and expectation 4/3 despite the same marginals. This correctly demonstrates why independence is a hypothesis. General A,B>0 yield probability B/(A+B) for each player and value AB/(A+B), with strict positivity giving uniqueness.

Private replaced slips, independent sampling and known recipes are explicit. The initial bag may use up to six slips; no three-slip optimum is supplied before discovery. Expected payoff is repeatedly distinguished from a sure per-round outcome. This retains the adult game-theoretic idea rather than using an unrelated perfect-information game.

## AP-24 — neutral copying and fixation

Checked prompts 1–6 and general N, including already absorbed states. The old generation is held fixed while every child is sampled, and fresh draws are required at later generations. This prevents an accidental Moran or sequential-replacement process. Chosen losing and mixed histories both have positive probability.

For N=2 the transition from the mixed state has probabilities (1/4,1/2,1/4). Therefore mixed survival is 2^(−k), the two absorbed probabilities are each (1−2^(−k))/2, and expectation stays one, including k=0. Survival has positive probability at every finite k but zero probability forever. The strict 1/100 threshold first occurs at k=7. Without replacement, both original parents are copied once and mixing persists; its unchanged expectation cannot distinguish these processes.

For N=3, independent binomial expansion gives rows (8,12,6,1)/27 and (1,6,12,8)/27. Both transient row sums are 2/3, so mixed survival is (2/3)^k even though the red count can change inside the mixed set. Conditional expectation preserves E[Xₖ]=1. Subtract the contribution of states 1 and 2, bounded by 2(2/3)^k, to obtain eventual red fixation probability 1/3. Increasing absorbed-red events justify passing to eventual fixation. No unequal-start symmetry argument appears.

For every finite N, the event that all children choose one specified parent has probability N^(−N), independently of the current color composition. Conditional bounds iterated over time give the geometric survival bound; independence of successive population states is unnecessary. The vanishing mixed contribution proves fixation probability i/N, including i=0,N. My separate first-step linear systems recover all 45 interior fixation probabilities for N=2 through 10 exactly.

Separate numbered parent/offspring mats and the explicit replacement rule suffice. The real gate includes conditional averages and geometric limits, not merely color play. This remains a finite stochastic-process investigation with a meaningful asymmetry continuation.

## AP-25 — conserved labels and reachability

Checked prompts 1–6 and the enabling-obstruction extension. The reaction vector (−1,−2,+1) preserves exactly weights satisfying w_C=w_A+2w_B. Thus every linear total is r(A+C)+s(B+2C), with arbitrary real r,s. Necessity follows from a legal one-step state; sufficiency works in both directions. Positive examples (1,1,3) and (2,1,4) have the printed initial totals 14 and 19.

With C=z, the initial invariants force (5−z,9−2z,z), 0≤z≤4 integer. All five listed states are connected by legal adjacent firings; no sixth state passes nonnegativity. Both invented exclusion targets pass exactly one test. In general, the interval 0≤z≤min(a+c,floor((b+2c)/2)) is complete, monotone routes are legal, and the shortest distance is |z−c|. My separate shortest-path search checks the minimum-length assertion across 450 source/target pairs.

For 2A↔2B, total plus parity yields precisely (5,0),(3,2),(1,4), all reached constructively. In A+B↔2B, zero B blocks both directions. For positive B the exact class is every positive B count through total a+b; backward moves cannot create B=0 because they require at least two B. This correctly distinguishes a necessary integer displacement from a legally enabled path.

Blank weight tags and open state records preserve invention; exactly five state boxes would disclose the classification and are explicitly prohibited. Counters suffice, and no kinetic law is misrepresented as proved by the game. The linear-algebra and integer-interval gates are stated honestly.

## AP-27 — observability and measurement delay

Checked prompts 1–6 and the signed general sensor extension. Equal rates make every later row proportional to the sum row: all splits of 8 yield 8·2^(−n). The zero nonnegative state is the correctly noted exceptional unique record. Either proposed extra sensor gives a nonsingular system; the weighted-sensor compatibility interval is also correct.

For rates 1/2,1/4, the readings recover a=b=4, y₂=5/4, whereas (6,2) predicts y₁=7/2. General inversion gives a=4y₁−y₀ and b=2y₀−4y₁; nonnegativity is equivalent to the printed wedge, including both boundaries and the origin. The recovered error is ±e/(r−s): the two stated rates give bounds 1/25 and 1, attained without violating positivity at (4,4).

For a delayed reading the denominator is dₖ=(3/4)^k−(1/2)^k. Its consecutive difference equals (1/4)(1/2)^k[2−(3/2)^k], positive only at k=1 and strictly negative at every k≥2. Therefore k=2 uniquely maximizes separation, giving d₂=5/16 and the sharp algebraic bound 4/125. This is a proof for every positive integer delay, not a finite table. The extension determinant αβ(s−r) is necessary and sufficient for all real initial states. In singular cases the full record has the same invisible direction; a small perturbation of an interior positive state shows nonnegativity does not restore global observability, while boundary exceptions can remain unique.

Hidden initial levels, known decay factors and the sum-only sensor must be unambiguous. The optimal delay must not be labeled in the launch. The reconstruction/conditioning distinction is substantive and different from AP-19's spatial receiver placement.

## AP-28 — one-bit correction and its limit

Checked prompts 1–6 and the two-check extension. Distance at least three is necessary by explicit common received words for distances zero, one or two, and sufficient by the triangle inequality for disagreement counts. The six distances of the supplied construction are 3,3,4,4,3,3. The received examples decode C, A, B with the printed positions/no-change decision.

Four length-four radius-one neighborhoods require 20 words in a 16-word space, impossible. Padding shorter words preserves distances, so this excludes every shorter length. The five-bit code covers 24 of 32 received words; 00110 has distances 2,3,3,2 and lies outside. Two flips sending A to 11000 misdecode as B. The even-parity three-bit construction detects any one-bit change; 001 is ambiguous among three originals, establishing the correction distinction.

The extension has eight kernel words. Its five single-bit signatures are 10,11,01,10,01, so every single flip is detected but repeated signatures prevent universal correction. The explicit distance-two pair and ambiguous received word are correct. The author accepted the optional completeness refinement and I reread its final text: for any error e, h(c+e)=h(e), so it detects precisely nonzero-syndrome patterns. There are 24 detected patterns and seven nonzero undetected patterns; the eighth kernel pattern is no error. This field and its added all-256-pair checks are closed.

The page-2 codebook is explicitly supplied only after construction attempts. Four launch strips are legitimate because the message count is a given; they do not disclose a solution count. Six pair-audit slots likewise reflect the supplied four messages. The proof concerns worst-case finite errors, not Shannon capacity.

## AP-30 — meter loading

Checked prompts 1–6, the ideal-wire boundary, and the general-resistance extension. No meter gives (6−X)/2=X and X=2. The loaded equation is (6−X)/2=X+X/R, giving X=6R/(3R+2), lower current X, meter current 6/(3R+2), and incoming current 6(R+1)/(3R+2). Every value for R=1,2,6 checks. Finite positive R always lowers the voltage and raises source current; the unloaded result is the R→∞ limit.

Relative error 2/(3R+2) gives the necessary and sufficient threshold R≥2(1−ε)/(3ε), with equality and the 66-ohm / 1.98-volt example correct. At R=2 the power sum 81/8+18/8+9/8 equals source power 108/8. For an ideal short, X=0, source and wire currents are 3 and lower current is zero; source and top-resistor power are 18, wire power zero. This is correctly handled without 0/0.

Two 2-ohm meters agree at 6/5 V. For m branches, X=6R/(3R+2m), giving the stated tolerance rule and 132-ohm threshold for two meters. The general circuit has V₀=Vb/(a+b), effective resistance ab/(a+b), and loading factor R/(R+ab/(a+b)). This directly proves the special equivalent-source description; it does not assert a general network theorem.

Junction dots, separate meter branches, reference current arrows and source/ground labels are necessary renderer requirements and are specified. No physical powered build is required. The task makes a chosen sensor part of the modeled system, with energy providing a separate audit.

## Sources, checks and release scope

I reopened the linked primary material: Vallis §7.1.3 / PDF pages 75–76 (the stated long-wave limit); Boyd–Vandenberghe §5.1.3 / PDF page 230 (feasible-point weak-duality inequality); Bonanno §§5.2–5.3 / PDF pages 197–205 (mixed distributions and the warning that support indifference alone is insufficient); Chasnov §5.5 / PDF page 84 (Wright–Fisher versus Moran) and §6.1 / PDF pages 91–92 (signed reaction changes); the official Feedback Systems chapter listing; the MIT state/output/noise notes; Shannon Part II §11 / PDF page 19; and Tong §4.1.3 / PDF pages 8–11 (Ohm behavior and dissipation). The author's inability to inspect the linked Feedback Systems chapter PDF is disclosed rather than hidden. The exact special models are proved here and do not depend on an inaccessible theorem.

The checks and proofs preserve the original adult questions. Prior-use links explain how repeated broad themes differ in their data, learner decisions and proof goals. Actual mathematical gates are visible, with manipulatives treated as entry points rather than replacements for the later reasoning. No answer-leaking layout is specified. Production must still verify every rendered prompt, table, branch, symbol and workspace under the PDF review contract.

Independent finite checks: 236 noninteger-position sensor inversions; 507 exact price-slack identities; 3,721 payoff/regret cases; 45 independently solved absorbing-chain probabilities; 450 shortest legal reaction routes; 100 delay-difference identities and 625 signed sensor determinants; all 256 kernel-codeword/error pairs and all 32 received words for the supplied code; 256 exact general-network power certificates. All pass. These investigations remain unpiloted; expected timing and learner engagement have not been observed.
