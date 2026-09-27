# Independent review: applied mathematics and probability

Reviewed 25 September 2026 by the geometry/analysis agent, independently of the AP author. Scope: all 30 cards in families/applied-probability.json, including every exact instance, solution, boundary, gate, bridge, and proposed extension. Each instance was worked from the rules before its supplied solution was displayed. A second pass read the solutions and all remaining fields. This is mathematical/editorial agent review, not classroom observation or human educator approval.

## Decision and finding closure

**All 30 core instances pass under their stated models. No blocking mathematical finding remains.** Two substantive clarifications and one source repair were requested and the saved replacements reread:

- **AP-29, explain gate — CLOSED.** “Why prefixes cause ambiguity” risked implying that every non-prefix code is not uniquely decodable. The saved gate now distinguishes immediate greedy decoding from general unique decodability, and says a prefix violation can make greedy stopping fail. Its boundary and hard stop were already appropriately scoped.
- **AP-05, source alignment — CLOSED.** The original Think Stats §8.6 favors a different confidence-interval interpretation. The editor replaced it with [NIST/SEMATECH §1.3.5.2](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm), whose introductory paragraphs directly support procedure coverage. The saved locator explicitly says the five-error construction is independently derived and is not the handbook’s t-interval example. I inspected the NIST interpretation and reread the saved source object.
- **AP-17, source retrieval — CLOSED.** The old Cambridge URL failed direct retrieval. The saved reference now uses [Tong’s current author-hosted page](https://davidtong.org/teaching/general-relativity/grhtml/S1), §1.2.1 and proper-time equation (1.16). That page retrieved successfully; I reread the replacement.

No AP source card was silently edited by this reviewer. The coordinator applied the repairs.

Optional improvements, which do not block plan PDF production:

1. AP-15’s reading gate suggests reading the worked tree aloud before independent exploration. Demonstrate one projection and the update rule, leaving sequence trees for learners. Suggested wording: “Symbolic rules; a facilitator may read the rule aloud and demonstrate one transition before learners construct the sequence trees.”
2. AP-28’s minimum-length proof can add: “Any shorter code could be padded with fixed zeros to length four without decreasing pairwise distance, so ruling out length four rules out every shorter length.”
3. AP-25’s boundary could replace “modular or kinetic obstructions” with “modular obstructions or missing reactants needed to enable a move,” keeping reachability separate from rate-dependent timing.
4. AP-30’s source locator can be sharpened to Tong, Electromagnetism, §4.1.3, equation (4.4), printed pp.74–77 / PDF pp.8–11, for Ohm’s law and Joule heating. The [no-www PDF](https://davidtong.org/pdfs/teaching/electromagnetism/electro3.pdf) retrieved successfully.
5. AP-03 can specify that Think Stats §9.2 supports permutation-test mechanics; the card independently proves its randomized-assignment/sharp-null version.
6. AP-06 and GA-28 deliberately share the Newton cubic. GA-28 now records this reuse. Schedule them as comparison/extension, not independent novelty credit.

## Independent exact checks

The standard-library script applied-probability-checks.py passed all **18 checks**. It enumerates the specified finite domains: randomized assignments, labeled sampling pairs, two-state automata, spin configurations, integer factory plans, offer subsets, congestion occupancies, offspring outcomes, reaction states, received bit strings, and prefix trees. Exact fraction/matrix arithmetic also checks quantum branches, feedback identities, observation inversion, and circuit conservation.

The script states its domains. Sampling several targets does not replace the translation proof for coverage; checking observation formulas on a finite grid does not replace their algebraic inversion. General claims below were assessed from arguments.

Run from the repository root:

    python3 plans/atlas/reviews/applied-probability-checks.py

## Card-by-card assessment

### AP-01 — Which shore will the wandering token reach?

**Pass.** The interior equations give probabilities 1/4,1/2,3/4. Four consecutive heads have probability 1/16 and force absorption from every interior state, making survival through k blocks at most (15/16)^k. The biased three-position boundary gives 3/4 directly. A token and independent coin are exactly the finite chain; experiment and probability proof remain distinct. Oral movement is a meaningful entry, while the complete chance map needs fractions/algebra. Absorbing probabilities add substance beyond an ordinary graph walk.

### AP-02 — The clue that changes the bag

**Pass.** Six equal-probability bag/counter outcomes leave three red cases, two from A, giving 2/3. The “contains red” report is certain in both bags and leaves 1/2. Changing the prior A-probability to 1/3 gives red contributions 2/9 from each bag and posterior 1/2. The evidence-producing procedure is fully specified. Labeled cards give a complete finite conditioning proof before formulas, and changed bags/reporting rules offer meaningful learner decisions.

### AP-03 — Could the treatment labels have landed this way?

**Pass; optional source precision above.** Enumerating six assignments gives differences −3,−1,0,0,1,3, with upper tail 1/6 and absolute-value tail 1/3. The sharp null fixes all outcomes while the actual randomization moves labels, which validates the finite test. Observational assignment cannot substitute for that design. The card avoids treating the tail probability as the probability that the null is true. Clipping and grouping cards provide real entry actions, and the boundary exposes an essential causal assumption.

### AP-04 — A sampling rule that always misses

**Pass.** The population is specified in materials as four ones and four fives. All 64 ordered labeled draws give sample means 1,3,5 with probabilities 1/4,1/2,1/4 and expectation three. Restriction to the ones gives bias −2 regardless of repeated sampling. Replacement is explicit. The boundary correctly separates unbiasedness from accuracy of one estimate. Learners choose sampling designs before revealing the population, preserving the inference question. Think Stats §§8.4–8.7 supports the sampling-distribution and selection-bias framework.

### AP-05 — An interval-making machine

**Pass after source repair.** Coverage means |E|≤1, hence 3/5 for every integer θ because translation changes no covering error. Width two covers all five errors. Mass only at ±2 makes narrow coverage zero. The asymmetric extension [X−2,X] covers exactly errors 0,1,2. Fixed parameter, random interval, and posterior inference are carefully separated. Interval strips instantiate the exact finite procedure; symbol-reading requirements are stated. The repaired NIST citation supports the interpretation and clearly does not supply the constructed instrument model.

### AP-06 — A root finder caught in a two-step loop

**Pass; deliberate overlap.** Newton maps zero to one and one to zero, proving the endless two-cycle. The cubic’s signs at −2 and −1 certify a real root independently. At √(2/3), the derivative vanishes and the iteration formula is undefined. The activity retains tangency and its calculus prerequisite instead of relabeling a guessing game. Learners vary starts and warning rules. The same cubic in GA-28 is explicitly reused for a bracket-method comparison; count the exact instance once.

### AP-07 — A cooling model that heats itself up

**Pass.** Multipliers 1/2,−1/2,−2 give the displayed sequences. The general condition is |1−ah|<1. At h=2 the sequence is bounded but does not decay; h=1 reaches numerical zero despite positive continuous exponential values. Negative values are temperature differences, not negative absolute temperatures. The recurrence is a valid independent entry, with the ODE link separately calculus-gated. Step-size decisions and comparison of stability with accuracy provide substantive investigation. The source’s scope-only status is honestly retained.

### AP-08 — How much memory does the red-symbol machine need?

**Pass.** Remainder states give the three-state construction. Empty, R, and RR are pairwise distinguishable by suffixes of length zero or one, proving the lower bound. Independent enumeration of all 64 complete two-state binary DFAs finds none correct even through length three, supplementing the unrestricted proof. Two states suffice for strings of length at most one, as the boundary says. Floor circles faithfully enforce the memory restriction. The lower-bound question is new relative to merely making modular cycles.

### AP-09 — Find the two dances hidden in coupled springs

**Pass.** K has eigenpairs ((1,1),1) and ((1,−1),3), and their sum is (2,0). The stated cosine motion satisfies both the ODE and zero initial velocity. Middle stiffness k changes the opposite-mode eigenvalue to 1+2k and preserves the equal-mode eigenvalue one. The paper force model is exact while physical springs are approximate. Learners may stop at proportional force patterns without claiming temporal frequencies. Tong §2.6 was inspected and supports the normal-mode framework.

### AP-10 — Which spring arrangement stretches farther?

**Pass.** Series extension is 6/2+6/6=4, with stiffness 3/2. Parallel extension is 6/8=3/4; branch forces 3/2 and 9/2 sum to six. Equal parallel forces would give incompatible extensions, so the boundary is correct. Rigid-bar compatibility and ideal Hookean behavior are explicit. Learners choose arrangements and target stiffness; algebra arises from the physical compatibility rule. The resistor-network connection is acknowledged, while AP-30’s sensor-loading question is a substantive variation.

### AP-11 — The narrow channel and the impossible flow map

**Pass.** Flux is twelve, so area three requires mean normal speed four. Proposed speed three creates a storage discrepancy of three volume units per second. A rigid full steady incompressible tube cannot sustain it; a rising reservoir can. Compressible flow correctly changes the conserved quantity to mass flux. The anchor specifies cross-sectional mean normal speed, avoiding an unstated uniform-flow assumption. Counters explain a conservation ledger without pretending to derive continuum mechanics. Branch allocation remains underdetermined until additional physics is supplied.

### AP-12 — Where should the fastest path cross the shoreline?

**Pass.** Differentiating the specified travel-time function gives zero at x=3 and strictly positive second derivative everywhere. The unique global minimum is 35/12. The direct shortest route crosses at x=4. At the optimum, sine/speed ratios are (3/5)/3=(4/5)/4=1/5, consistent with angles from the normal. Measurement supplies evidence; calculus supplies the universal optimum proof. Learners choose crossing positions and test the competing distance/time objectives. The source supports wave context while the Fermat calculation is independently complete.

### AP-13 — Add a wave and make the signal smaller

**Pass.** Amplitudes two, three, and one give normalized intensities four, nine, and one. Averaging sine products yields the arbitrary-phase cross term. Quarter-period coherent phase gives zero cross term; drifting phase can do so for a different reason. Local cancellation is not asserted to destroy global energy. Signed strips preserve actual pointwise superposition, and integration is an honest advanced gate. Tong §§4.3.1–4.3.2 and 4.4 were inspected for wave superposition and averaged quadratic energy.

### AP-14 — Can the heat-engine sales pitch be true?

**Pass.** Entropy totals are −1/150,0,+1/150. All proposals balance energy, but only the latter two satisfy the entropy inequality. Maximum permitted work is six; raising the cold temperature to 400 K reduces it to four. Cascaded reversible heat factors cancel the intermediate temperature. Cycle, reservoir, and absolute-temperature assumptions are explicit. Passing constraints is correctly distinguished from building an engine. The supplied physical inequality leaves learners a real optimization task. Tong §§4.3.2–4.3.3 supports the bound.

### AP-15 — Does the order of two quantum questions matter?

**Pass; optional scaffolding improvement above.** Exact projectors give recorded P(Z=e1)=1/2 for X→Z and zero for Z→X. Repeated Z remains certain. Both final unconditional density matrices are I/2 for these two particular mixed-order experiments, as the card carefully notes. Born probabilities and state updates are valid in the real two-dimensional restriction; ordinary arrows are not asserted to be hidden physical directions. Tong §3.3, equations (3.71)–(3.72), was inspected. The linear-algebra gate is justified; an elementary coin substitute would lose the mechanism.

### AP-16 — Count the tiny magnet before running it

**Pass.** Enumeration gives multiplicities 2,6,6,2; weighted totals 2,12,24,16; total 54; alignment probability 8/27. The first-spin/edge-choice encoding proves Z=2(1+b)^3. Closing a ring imposes even disagreement parity. The chosen factor two is a real Ising weight with βJ=(log 2)/2 up to a common factor. No finite-system phase-transition singularity is claimed. Counting remains accessible while the comparison of multiplicity with per-state favorability carries substantive statistical mechanics.

### AP-17 — Two clocks, one reunion, different elapsed times

**Pass after source repair.** Proper durations are ten and two times four. A nonzero symmetric excursion with |d|<5 has 2√(25−d²)<10. The lightlike boundary is excluded for the massive clock. The Lorentzian metric and instantaneous-turn idealization are explicit, and Euclidean drawing length is not substituted for elapsed proper time. Algebra supports the exact comparison without pretending to derive relativity. The repaired author-hosted Tong page supports the proper-time framework, and the saved reference was reread.

### AP-18 — Weigh an unseen center from its orbiters

**Pass.** The three original products v²r equal 36; the extra card gives 64. Predicted speed at radius sixteen is 3/2. Circularity, negligible test mass, point-mass dominance, inverse-square gravity, and true radius/speed are stated. The eccentric-orbit boundary correctly rejects using circular balance outside its assumptions. The spherical distributed-mass extension explicitly changes the model. The task preserves conditional parameter inference: inconsistency identifies failure of the joint model/data, not which assumption failed or whether real data validate the force law.

### AP-19 — Can travel times reveal the water depth?

**Pass.** First-segment time is three, leaving two; second speed is three and depth nine. Swapped depths and the equal pair (144/25,144/25) both retain total time five. Total time cannot be three or less with the first depth fixed and finite positive second depth. Eliminating velocity from the linear constant-depth system gives ηtt=gHηxx. Wave propagation is distinguished from parcel motion. Vallis §7.1.3, immediately after equation (7.19), supports the nondispersive long-wave speed; interface complications remain outside the stated approximation.

### AP-20 — A price certificate for the best factory plan

**Pass.** Plan (A,B)=(2,1) earns ten. Prices (2/3,5/3) value each product’s ingredients at its sale value and the supply at ten, proving optimality even with fractional production. Integer enumeration agrees. Supplies (4,4) give fractional optimum 28/3 and integer optimum eight, a genuine integrality gap. Nonnegative prices are essential and present. Counter bundling faithfully represents feasibility; the matching price certificate adds a universal upper bound beyond a good-looking construction.

### AP-21 — Spend the battery now, or save it?

**Pass.** Backward value rows are (0,4,4), (0,4,8), (0,4,8). Feasible subset scores are 0,5,4,4,8, so the final two offers are optimal. With one unit recharged overnight, taking all three becomes feasible and earns thirteen, validating the boundary warning. Day and remaining energy are sufficient state under known offers and no recharge. Learners decide plans and organize reused information. The source is honestly marked as chapter scope; the finite backward-induction proof is independently complete.

### AP-22 — How should you hide an unequal choice?

**Pass.** Row probability p(U)=1/3 equalizes threats at 2/3. Column probability q(L)=1/3 caps each pure-row payoff at 2/3, hence all mixtures by linearity. Seeing the realized row action permits payoff zero, as the boundary says. The randomization rule may be public while its realized action is private. The extension distinguishes expectation from every-round guarantees. Thirds suffice for the exact minimax certificate. Simultaneous hidden choices create a genuinely different question from prior perfect-information games.

### AP-23 — A stable traffic pattern that costs more

**Pass.** Occupancies n=0,1,2,3 have totals 6,5,6,9. Exactly n=1 and n=2 admit no strictly profitable unilateral switch. Joining a route changes its congestion, and ties do not count as improvements. The social optimum is n=1. With B-cost 3/2, n=1 is the sole equilibrium and remains optimal. Player counters faithfully instantiate the finite congestion game. Learners can choose configurations and test both unilateral switches and coordinated improvements rather than merely compute totals.

### AP-24 — A neutral population can lose a color

**Pass.** Four ordered offspring outcomes give red-count probabilities 1/4,1/2,1/4 and expectation one. Mixed-state survival through k generations is 2^−k, proving almost-sure absorption; symmetry gives fixation probability 1/2 per color. Without replacement, both colors persist in this N=2 example. Simultaneous generation replacement, fixed haploid population, no selection, and no mutation are explicit. The concrete sampling process is exactly the stated finite Wright–Fisher model, without a claim about individual human traits.

### AP-25 — What can never change in the reaction box?

**Pass; optional boundary wording above.** A+C=3 and B+2C=4 force the three listed nonnegative integer candidates, all realized by zero, one, or two forward firings. Target (0,0,3) violates the second invariant. Complete reachability enumeration agrees. Adding A↔B leaves linear conservation weights satisfying wA=wB and wC=3wA, giving A+B+3C. The paper exchanges form an exact stoichiometric state graph. Rates, equilibrium, and chemical feasibility are explicitly not inferred from reachability.

### AP-26 — The controller is correcting yesterday’s error

**Pass.** Full delayed correction produces the six-cycle 0,−1,−1,0,1,1 after the initial pair; its state matrix has sixth power I. Half feedback has fourth power −I/4, proving x[n+4]=−x[n]/4 for every initial pair and hence decay of all residue-class subsequences. The worked fractions agree. A repeated scalar position is correctly distinguished from a repeated complete state. Delay belongs to the exact model, unlike AP-07’s numerical approximation; the shared recurrence reasoning is openly cross-linked.

### AP-27 — Can one sensor see two hidden tanks?

**Pass.** Equal halving maps every split with total eight to totals 8,4,2,1,…, so (2,6) and (4,4) remain indistinguishable. Distinct rates give a+b=8 and 2a+b=12, hence a=b=4. General inversion a=4y1−y0, b=2y0−4y1 checks algebraically. Equal rates destroy rank; near equality causes sensitivity despite uniqueness. Hidden cards, update laws, and the sum sensor faithfully realize observability. Physical drainage and noisy statistical filtering are not falsely claimed.

### AP-28 — Four messages that survive one damaged bit

**Pass; optional shorter-length clause above.** Six pairwise distances are 3,3,4,4,3,3. All 32 received words lie within one flip of at most one listed codeword. Word 10111 decodes to 10011. Four radius-one balls of length four require twenty distinct words but only sixteen exist. The two-flip boundary from 00000 to 11000 genuinely leads toward 11100. Bit strips exactly preserve the finite adversarial problem; Shannon capacity and encryption are explicitly different. The construction plus impossibility proof provides a strong accessible stop.

### AP-29 — Give the common message a shorter name

**Pass after gate repair.** The code has total fourteen bits. Removing unary nodes is justified by positive weights. Full four-leaf trees have only depth multisets (2,2,2,2) or (1,2,3,3); exchanging labels puts larger weights no deeper than smaller ones, giving minima sixteen and fourteen. Independent enumeration of all five ordered full shapes and assignments agrees. Equal weights prefer the balanced tree, eight versus nine. Shannon’s PDF p.18 contains the same code and average 7/4. The saved gate now correctly separates prefix decoding from general unique decodability.

### AP-30 — The sensor changes the circuit it measures

**Pass; optional source locator above.** Without loading, X=2 and current two. With the meter, X=3/2, source current 9/4, bottom current 3/2, meter current 3/4. Source power 27/2 equals resistor powers 81/8+9/4+9/8. For R>0, X=6R/(3R+2) satisfies the node equation and tends to two. The zero-resistance limit is handled without dividing by zero. This is an exact finite resistor model; choosing meter resistance preserves a real loading investigation rather than repeating AP-10’s network-combination arithmetic.

## Source-check limits

Directly inspected in this independent review: Downey chapters 8–9; NIST confidence-interval interpretation; Tong classical dynamics §2.6, thermodynamics §§4.3.2–4.3.3, quantum §3.3, general relativity §1.2 through its current URL, and electromagnetism §§4.1.3,4.3,4.4; Vallis §7.1.3; Shannon’s displayed four-symbol code. Crucial source claims were sampled rather than every cited book being reread. Author-disclosed scope-only citations remain scope-only; every displayed finite instance was independently worked.

No classroom suitability, empirical physical-model validity, or exhaustive AP research-literature audit is claimed. Keep the source/bridge qualifications visible in rendered plans.

## Optional-refinement closure

After the main review, the coordinator adopted the five source/access/proof refinements. I reread the saved AP JSON and verified:

- **AP-03 — CLOSED:** its locator now attributes permutation-test mechanics to Think Stats §9.2 and identifies the sharp-null randomized-design proof as independent.
- **AP-15 — CLOSED:** the reading gate now scaffolds one transition and leaves sequence-tree construction to learners.
- **AP-25 — CLOSED:** its boundary now names modular obstructions or missing enabling reactants, keeping legal reachability distinct from reaction timing.
- **AP-28 — CLOSED:** its proof now pads any shorter code with fixed zeros, explicitly extending the length-four impossibility to every shorter length.
- **AP-30 — CLOSED:** its source now uses the working no-www URL and the inspected §4.1.3/equation (4.4) locator with printed and PDF page ranges.

The AP-06/GA-28 overlap was already recorded. No requested AP plan repair remains open. PDF production may proceed; layout and preservation of this latest text still require separate review.
