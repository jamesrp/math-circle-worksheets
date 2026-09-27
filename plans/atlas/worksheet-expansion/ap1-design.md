# AP1: eight investigation designs

Assigned families: AP-02, AP-03, AP-04, AP-05, AP-06, AP-08, AP-09, AP-10. No original atlas or random-ten files changed. Each has three staged student pages, complete per-prompt solutions, delayed hints, explicit gates, exact figure data and guide-only extensions. Independent design review is closed and the custom renderer now produces a reviewed development preview. See `ap1-maker-qa.md` for actual page counts and inspection scope.

The current Week 1 and random-ten benchmark was reread, together with the lesson-format source notes. Learning through choosing, testing and explaining drives the designs; source teaching advice is not classroom-pilot evidence. `ap1-data.json` is the full design/key. `ap1-checks.py` and its result file record exact finite verification; general arguments remain in the per-task solutions.

## AP-02 — The same clue, a different experiment

First-pilot candidate for a group comfortable with fractions. The protocol distinction creates the surprise; avoid turning the repeated-draw page into long simulation or presenting posterior fractions before learners filter the cards.

**Core gate:** Counting equally likely labeled outcomes and fractions; distinguish a random selection from a deliberate report. No algebra is needed for the complete finite certificate.

**Extension gate:** Multiply simple fractions or count a two-draw grid; prior odds and likelihood ratios are an optional algebraic continuation.

**Investigation arc:** Which messenger should change your mind? → Ask the same bag twice → Can you cancel a clue?.

**Payoff:** Two correct but different answers to the red clue, proved from the mechanism; then a complete two-draw evidence comparison.

**Connection:** Finite conditional probability and likelihood ratios. The outcome cards are the actual sample space; no continuous prior or real-world bag-selection model is silently assumed.

**Prior use:** Year-1 probability is related, and AP-01 in the trial uses fair paths. This new question concerns selection of evidence, not endpoint probabilities. Original atlas bag counts remain but the two-messenger and two-draw comparison are developed here.

**Source decisions:**

- [Grinstead and Snell, Introduction to Probability](https://math.dartmouth.edu/~prob/prob/prob.pdf), §4.1 Discrete Conditional Probability, especially Bayes formula, printed pp.133–146. The textbook supplies the conditioning framework. Messenger protocols, two-draw grids and fixed-size extremal design are independently derived finite instances. Reopened the author-hosted PDF, checked §4.1 and Bayes discussion; all outcome counts independently enumerated in ap1-checks.py.

**Checked tasks:** 1, 2, 3, 4, 5, 6.

## AP-03 — How surprising are these labels?

Promising with explicit statistical reasoning gates. A complement-pair representation avoids twenty rows of repetitive arithmetic. “Unusual under this no-effect model” is the payoff, never “probability training is useless.”

**Core gate:** Choose subsets systematically, add six small scores and compare sums; fractions such as 1/20. The real reasoning gate is fixing the null assumption and actual assignment rule.

**Extension gate:** Understand the difference between a prespecified one-sided rule and a rule selected after seeing the result; paired randomization uses three independent fair coins.

**Investigation arc:** Assign the clips before explaining the result → Choose the alarm rule before looking → A new assignment rule changes the answer.

**Payoff:** A complete 20-assignment reference set and a prespecified tail count, followed by an explanation of why a different assignment design gives a different answer.

**Connection:** Exact randomization inference under the sharp null: each participant would have the same score with or without training. Scores are fixed only for that hypothetical calculation; treatment labels follow the actual random assignment.

**Prior use:** No matching inference worksheet in Weeks 1–10 or random-ten. AP-02 also conditions on a mechanism, but this asks whether randomized labels alone can explain a prespecified extremeness statistic.

**Source decisions:**

- [Allen Downey, Think Stats, third edition](https://allendowney.github.io/ThinkStats/chap09.html), Think Stats 3, §9.2 simulation/permutation mechanics and chapter 9 discussion of test statistics and null models. The text supplies general test/permutation terminology; the sharp-null randomized-experiment argument and paired-design comparison are derived here, not attributed to observational exchangeability examples. Reopened chapter 9, inspected the statistic/null/permutation discussion. Independently enumerated every 20 and 8 assignment and both tails.

**Checked tasks:** 1, 2, 3, 4, 5, 6, 7.

## AP-04 — A very precise wrong answer

First-pilot candidate when averages are familiar. The two indistinguishable hidden worlds produce a genuine impossibility argument rather than merely saying “bias is bad.” Avoid repeated draws after the mechanism is already clear.

**Core gate:** Means of small numbers, counting equally likely draws, and distinguishing the whole target population from the draw bag. The non-identifiability explanation needs systematic reasoning.

**Extension gate:** Weighted averages with known group sizes; no calculus or asymptotic theorem needed.

**Investigation arc:** Could two different worlds look identical? → A noisy rule with the right center → Design a better two-card survey.

**Payoff:** Two different hidden populations yield exactly the same allowed observations, proving that more restricted data cannot determine the full mean; an improved sampling design is justified.

**Connection:** Sampling frames, non-identifiability, unbiasedness, and stratified estimation. Equal probability within a restricted frame is not equal coverage of the target population.

**Prior use:** Related to AP-02 because mechanisms matter, but distinct target: estimating a finite-population mean from a sampling frame. No corresponding trial worksheet or Week 1–10 instance.

**Source decisions:**

- [Allen Downey, Think Stats](https://allendowney.github.io/ThinkStats/chap08.html), Chapter 8, §8.1 Estimation of means; discussion of biased and unbiased estimators. Uses the distinction between an estimator and its sampling distribution. The two-world impossibility construction and unequal-block repair are independently derived, not copied from the source examples. Reopened estimation chapter, inspected finite-sampling and bias discussions; all 64 two-draw outcomes and block-weight calculations checked exactly.

**Checked tasks:** 1, 2, 3, 4, 5, 6.

## AP-05 — Build a promise an interval can keep

Promising with a genuine statistics gate. The width optimization and intentionally unhelpful 50%procedure make coverage tangible. The coin-rule page is optional; explain its purpose before invoking general confidence-interval terminology.

**Core gate:** Signed integer addition and subtraction, closed intervals, fifths and systematic cases. Keep one unknown target fixed while the instrument error varies.

**Extension gate:** Compare a procedure’s repeated coverage with what is known from a realized report; optional randomized interval procedures use a separate independent coin.

**Investigation arc:** What does the strip catch? → The shortest four-out-of-five promise → An honest percentage can hide a bad rule.

**Payoff:** A shortest 80%translation interval with a lower-bound proof, and an explanation that coverage describes the random procedure rather than a posterior distribution on the secret.

**Connection:** Exact finite confidence coverage Pθ{θ∈I(X)}. The instrument model is X=θ+E with fixed unknown integer θ and a fresh uniform five-card error. No prior onθ is assumed.

**Prior use:** No matching trial activity; AP-02 has probabilities for a randomly selected bag, whereas this holds an unknown target fixed. Keeping those different probability models explicit is part of the investigation.

**Source decisions:**

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm), NIST/SEMATECH §1.3.5.2, introductory interpretation paragraphs before the t-interval formula. Uses only the repeated-sampling meaning of coverage. The five-error model, shortest-offset proof and independent-coin counterexample are separately constructed; no t-distribution calculation is borrowed. Directly reread the interpretation distinguishing procedure coverage from the probability assigned to a realized interval. Enumerated offsets/errors and randomized branches exactly.

**Checked tasks:** 1, 2, 3, 4, 5, 6, 7.

## AP-06 — When the tangent robot comes back

Advanced first-pilot candidate for learners taking calculus. The safeguard gives more than a familiar failure example. Do not relabel tangent motion as a lower-prerequisite guessing game.

**Core gate:** CALCULUS: derivative as tangent slope, evaluating cubics, rational arithmetic and a tangent-line zero. The loop is a Newton-method investigation only with this gate retained.

**Extension gate:** Continuity/Intermediate Value Theorem and algebraic interval-width bounds for a safeguarded method; a supplied geometric-decay fact is enough for finite error certification.

**Investigation arc:** Follow a tangent, not the curve → A failed run is not a failed equation → Give the tangent robot a guardrail.

**Payoff:** An exact non-root 2 cycle despite available roots, plus a modified method whose sign bracket shrinks by a proved factor.

**Connection:** Newton iteration as numerical dynamics; a sign-bracket invariant plus a contraction bound gives a global certificate in this specific interval. The new cubic differs from the atlas’s shared AP-06/GA-28 counterexample.

**Prior use:** AP-06 and GA-28 in the original atlas share x³−2x+2. This investigation deliberately changes the example to x³−5x and develops a bracket-preserving safeguard. Delivered AP-07 studies explicit-Euler stability, accuracy and an optimization certificate: both diagnose numerical procedures, but the failure mechanism and certificate differ here.

**Source decisions:**

- [Yano, Penn, Konidaris and Patera, Math, Numerics, and Programming](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-spring-2013/60af88c658ba3e83cdf7c43289aeb5b4_MIT2_086S13_Unit6_Textbook.pdf), Yano et al., Unit VI, §29.2.1 tangent construction; §29.2.3 failure checks and bisection discussion, PDF pp.5–8. Retains the Newton derivation but changes the cubic to avoid merely repeating GA-28. The middle-half safeguard and its 3/4 width bound are independently designed/proved. Reopened the MIT primary textbook PDF and inspected the formula, derivative-zero issue and bracketing discussion. Exact rational iterates and safeguard decisions independently checked.

**Checked tasks:** 1, 2, 3, 4, 5, 6.

## AP-08 — How many rooms must a machine remember?

First-pilot candidate with low arithmetic requirements and substantial proof. Learners get construction and adversarial testing before state-distinguishability is introduced. Do not confuse passing several short tests with a universal proof.

**Core gate:** Follow directed arrows labeled R/B, count red cards in triples, and reason that the current room is the machine’s only memory. Lower bounds require comparing histories followed by the same suffix.

**Extension gate:** Two simultaneous remainder conditions and a six-state construction; a pairwise distinguishability argument proves minimality.

**Investigation arc:** Build it. Try to break it. → Build a certificate about memory → Remember two things at once.

**Payoff:** A working three-room machine and a proof that every two-room machine fails for some finite string; optional six-room extension has its own lower bound.

**Connection:** Deterministic finite automata and the concrete distinguishable-prefix principle underlying Myhill–Nerode minimality. The finite lower bound is proved directly without invoking the full theorem.

**Prior use:** Delivered AP-26 studies state memory and recurrence; Weeks 1–10 also use state diagrams. This investigation adds a new payoff: distinguishing common future strings gives a lower-bound certificate for every smaller deterministic machine, alongside explicit correct constructions.

**Source decisions:**

- [Michael Sipser, MIT Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf), Sipser MIT18.404J Lecture 1, PDF pp.6–9, finite automata definition, computation and even-count language example. Uses the formal room/transition/acceptance model. The three- and six-state constructions, short-test counterexample and lower-bound certificates are independently proved. Reopened the MIT lecture PDF and inspected state/alphabet/transition/start/accept definitions and computation. Enumerated all 64 fixed-start two-state machines plus all short strings and all 15 six-state history pairs.

**Checked tasks:** 1, 2, 3, 4, 5, 6.

## AP-09 — Two motions hiding in one machine

Promising with algebra; specialist continuation with calculus. The classification and sum/difference coordinates give a strong mathematical payoff. Keep temporal frequencies and recurrence claims behind the calculus gate.

**Core gate:** ALGEBRA: signed displacement coordinates, linear force formulas, proportional pairs and factorization. The complete static force-pattern classification is a real stop; paper movement alone is not the whole result.

**Extension gate:** CALCULUS: differentiate cosine twice and verify a two-component ODE. Exact nonrepetition additionally uses the irrationality of √3 and cosine’s period.

**Investigation arc:** Which shapes pull straight back? → A different pair of coordinates → Can periodic pieces fail to repeat together?.

**Payoff:** Classify the two force patterns and uniquely decompose any initial displacement. With calculus, verify the motion and explain why two periodic modes can combine into a motion with no exact common repeat.

**Connection:** Normal modes diagonalize a coupled linear system. With unit masses and three unit Hookean springs, x″=−Kx for K=[[2,−1],[−1,2]]. Algebra finds eigendirections; differentiation verifies their oscillations.

**Prior use:** AP-10 also uses spring laws, but studies static effective stiffness. Trial AP-07 studies a numerical recurrence, not exact coupled motion. No earlier coupled-mode sheet is documented.

**Source decisions:**

- [David Tong, Classical Dynamics](https://davidtong.org/teaching/classical-dynamics/dynhtml/S2), Tong, Classical Dynamics §2.6 Small Oscillations and Stability; neighboring examples of normal-mode diagonalization. Uses the general normal-mode framework. The two-unit-mass worksheet, full shape classification, nonrepeat proof and retuned middle spring are independently derived for the stated matrix. Reopened Tong’s author-hosted section, inspected the small-oscillation/eigenmode setup. Matrix identities and decompositions checked exactly; time formulas checked analytically in the key, not inferred from numerical plots.

**Checked tasks:** 1, 2, 3, 4, 5, 6, 7.

## AP-10 — Add a spring: softer or stiffer?

First-pilot candidate for an algebra-ready group. The complete four-response classification and series/parallel duality make this more than substituting into two formulas. Younger exploration of hardware alone is not advertised as the full mathematical result.

**Core gate:** Fractions and algebra with F=kx; distinguish shared force from shared extension. Proving completeness for three springs requires structural cases, not calculus.

**Extension gate:** Series-parallel recursive constructions and reciprocal duality. Continuum elasticity, material failure and non-series-parallel networks remain outside this core.

**Investigation arc:** What is shared? → How many three-spring responses exist? → Turn a design into its reciprocal.

**Payoff:** Explain the series/parallel reversal from compatibility and force balance; classify all three-unit-spring responses and certify an impossible target, then construct it with four.

**Connection:** Finite ideal elastic networks: constitutive equations plus connection constraints determine effective stiffness. Series-parallel composition has an exact reciprocal symmetry for unit springs.

**Prior use:** AP-09 shares the linear spring model but studies coupled motion. Electrical resistor networks have related algebra; cross-link the representation instead of counting a relabeled network as unrelated content.

**Source decisions:**

- [Allan Bower, Applied Mechanics of Solids](https://solidmechanics.org/Text/Chapter3_2/Chapter3_2.php), Bower, Applied Mechanics of Solids §3.2, linear elastic constitutive assumptions; finite spring laws derived in the worksheet. Uses linear-elastic model discipline. Series/parallel compatibility, all three-spring responses and reciprocal duality are derived directly, not claimed as a theorem printed in this continuum section. Reopened the author-hosted linear-elastic section. Independently solved force/extension equations and exhaustively generated all recursive 3/4 spring stiffness values with exact fractions.

**Checked tasks:** 1, 2, 3, 4, 5, 6.

## Production handoff

`lowell-math-circle-year-2/source/atlas-remaining/ap1.py` supplies the custom student renderer and worked outcome, machine and spring figures. Current preview is `tmp/pdfs/atlas-remaining/ap1-reviewed-preview/`: 25 student PDF pages including contents and 39 guide pages. The maker inspected every student page at full size and every guide page on contact sheets, with dense mathematics and all worked figures at full size. Independent PDF review remains the next gate.
