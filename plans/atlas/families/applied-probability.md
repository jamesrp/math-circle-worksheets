# Applied Probability - investigation families

Facilitator planning cards. These are proposed investigations, not classroom-piloted student packets. The JSON alongside this file is the editable source; this Markdown is generated.

<a id="ap-01"></a>
## AP-01 - Which shore will the wandering token reach?

Primary field: 60. Related: 65. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a random path have an exactly predictable endpoint probability, and why is that probability harmonic?

**Anchor.** An independent fair nearest-neighbor random walk on 0,1,...,N, stopped at 0 or N, hits N with probability i/N from i. The first-step equations and boundary values determine the finite answer.

**Bridge (exact-special-case).** A token position is precisely the state of the stopped Markov chain. Independent fair coin flips implement its transition rule. Limits: Short experimental frequencies are estimates. This is not Brownian motion or a proof of a diffusion limit.

**Prerequisite gates.**

- **Entry:** O/C: move one place following a coin result and recognize endpoints.
- **Explore:** C/F: tally outcomes from repeated starts; compare fractions.
- **Explain:** F/A: an interior winning chance is the average of its two neighbors.
- **Prove:** A/P: solve the finite averaging equations, and justify eventual absorption.
- **Reading:** None with oral rules; a recorder may label the table.
- **Arithmetic:** Small counts; quarters and halves for the worked example.
- **Reasoning:** Separate individual paths from repeated experiments; hold the starting location fixed.
- **Hard Stop:** Martingale stopping theorems and Brownian limits require new probability prerequisites.

**Materials and preparation (5 minutes).** Draw five numbered spaces, provide a token and coin, and prepare a start/end tally sheet. A partner can flip while another directs moves.

**Launch.** Put the token on 1 of the track 0–1–2–3–4. Heads moves right one space, tails left one. Stop when it reaches 0 or 4. Which starting places make reaching 4 easier? Choose a start and investigate.

**Learner choices.** Choose starts, organize trials, decide whether to compare counts or proportions, and propose a track change to test.

**Hour menu.** 0–10 explore coin paths freely; 10–15 agree on independent tosses and stopping; 15–35 collect starts and endpoint records; 35–40 walk a human-size track; 40–55 build a probability-height drawing or longer track; 55–60 share a conjecture and its evidence.

**Explore.**

- Could starting one place farther right make the winning chance smaller?
- What must the chance at 2 have to do with the chances at 1 and 3?

**Hint ladder.**

1. Give endpoints height 0 and height 1; leave interior heights blank.
2. Make every interior height the average of its neighbors. Equal spacing works.

**Checked instance.** Find the exact probability of reaching 4 before 0 when starting at 1.

**Reasoning.** Write p0=0,p4=1 and 2pi=p(i−1)+p(i+1). Consecutive differences are equal, so p1=1/4,p2=1/2,p3=3/4. Absorption occurs almost surely: from any interior state, four consecutive heads suffice; each independent block has probability 1/16, so survival through k blocks is at most (15/16)^k. This justifies the endpoint interpretation.

**Boundary.** A coin with heads probability 3/4 breaks equal averaging. Starting at 1 on 0–1–2 then wins with probability 3/4, not 1/2.

**Extensions.**

- Use track 0–6 and explain why doubling a start from 1 to 2 doubles its endpoint probability.
- With algebra, solve the biased recurrence; with advanced probability, compare discrete harmonic functions and diffusion.

**Satisfying stop.** A complete five-position chance map, supported by a finite averaging argument.

**Prior use.** Week 1 extensions include random walks on tiling graphs; this uses absorbing boundaries and harmonic probabilities. Actual use of this new instance is unknown.

**Sources.**

- [Grinstead and Snell, Introduction to Probability](https://math.dartmouth.edu/~prob/prob/prob.pdf), Chapters 4 and 12.2. Inspection: relevant exposition inspected; finite instance independently derived below.

<a id="ap-02"></a>
## AP-02 - The clue that changes the bag

Primary field: 60. Related: 62. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does evidence update probabilities, and why must its selection mechanism be specified?

**Anchor.** Conditional probability on a finite equally likely sample space is the fraction of surviving outcomes. Posterior odds depend on prior selection and evidence likelihood, not only on the visible counter.

**Bridge (exact-special-case).** Bag choices and individually labeled counter draws constitute an explicit finite experiment. Filtering cards implements conditioning exactly. Limits: A posterior describes this specified model; it does not establish that a physical bag was chosen uniformly.

**Prerequisite gates.**

- **Entry:** O/C: match a card to a bag and remove outcomes inconsistent with a clue.
- **Explore:** C/F: compare surviving case counts and fractions.
- **Explain:** P: explain why retained cases have equal probability.
- **Prove:** F/A: derive Bayes probabilities with unequal bag-selection weights.
- **Reading:** Labels can be colors or pictures; rules can be spoken.
- **Arithmetic:** Counting six outcomes; halves, thirds and sixths.
- **Reasoning:** Keep the process producing the clue separate from the clue itself.
- **Hard Stop:** Continuous Bayesian inference needs densities and integration; a finite case is already complete mathematics.

**Materials and preparation (10 minutes).** Two opaque cups A and B, each with three labeled counters. A contains RRBlue; B contains RBlueBlue. Provide six outcome cards A1,A2,A3,B1,B2,B3.

**Launch.** Bag A contains two red counters and one blue; bag B contains one red and two blue. Choose A or B by a fair coin, then draw one counter uniformly without looking. You see red. Which bag is now more likely? Arrange all possible bag-and-counter outcomes before making your claim.

**Learner choices.** Choose a representation of outcomes, design a different pair of bags, and compare information from red, blue, or a different reporting rule.

**Hour menu.** 0–10 inspect and label counters; 10–15 rehearse the two random choices; 15–35 build and filter outcome cards; 35–40 swap investigator and dealer roles; 40–55 change the clue-producing rule or bag-selection coin; 55–60 describe what information matters.

**Explore.**

- Why are the bags equally likely before drawing but not after seeing red?
- Would hearing “this bag contains red” give the same information as seeing a randomly drawn red?

**Hint ladder.**

1. List bag identity and counter identity together, not just the two possible colors.
2. Cover every blue-draw card and compare the bag labels still visible.

**Checked instance.** With a fair bag choice and uniform draw, compute P(A given red). Then compare an announcer who merely reports whether the chosen bag contains any red.

**Reasoning.** There are six equally likely outcomes. Three are red: two from A and one from B. Therefore the posterior chance of A is 2/3. Both bags contain red, so the announcer always gives the second report; that report leaves the chance at 1/2. The identical word red does not make the experiments equivalent.

**Boundary.** If A is selected with probability 1/3 and B with probability 2/3, red has contributions 2/9 from each bag; the posterior chance of A is then 1/2.

**Extensions.**

- Choose integer bag contents making a red observation leave the prior odds unchanged; equal red fractions do so.
- Use a tree with unequal prior weights and derive posterior odds = prior odds × likelihood ratio.

**Satisfying stop.** Two different clue mechanisms produce different correct answers, explained with surviving cards.

**Prior use.** The year-1 collection contains probability activities. This exact evidence-selection investigation is new; do not count a changed color story as a new mechanism.

**Sources.**

- [Grinstead and Snell, Introduction to Probability](https://math.dartmouth.edu/~prob/prob/prob.pdf), Chapters 4 and 12.2. Inspection: relevant exposition inspected; finite instance independently derived below.

<a id="ap-03"></a>
## AP-03 - Could the treatment labels have landed this way?

Primary field: 62. Related: 05, 60. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can randomized assignment support an exact inference without assuming a normal population?

**Anchor.** Under the sharp null that treatment changes no participant’s outcome, outcomes remain fixed while treatment labels follow the actual assignment mechanism. A prespecified tail of the randomization distribution gives an exact finite test.

**Bridge (exact-special-case).** Assigning two treatment labels uniformly among four fixed outcome cards reproduces a complete randomized experiment under its sharp null. Limits: These invented scores are a mathematical example, not evidence about a real treatment. A test does not compute the probability that the null is true.

**Prerequisite gates.**

- **Entry:** O/C: assign two labels and compare two groups.
- **Explore:** F: compute two-number means and enumerate six assignments.
- **Explain:** P: justify equal assignment probabilities under the stated design.
- **Prove:** F/P: relate tail counts to a prespecified statistic and null model.
- **Reading:** Short labels; a partner can read the experimental story.
- **Arithmetic:** Small sums divided by two; sixths.
- **Reasoning:** Distinguish observed outcomes, hypothetical assignments, and the null assumption.
- **Hard Stop:** Observational causal inference requires additional assumptions; random shuffling does not manufacture randomized assignment.

**Materials and preparation (8 minutes).** Four outcome cards numbered 0,1,3,4, two treatment clips, and a six-row record sheet. Use a fictional paper-airplane training example, not health claims.

**Launch.** Four people received scores 0,1,3,4. Before the activity, exactly two were chosen uniformly for training. The trained pair scored 3 and 4. If training changed nobody’s score, how often could random labels make the trained average at least this much higher?

**Learner choices.** Choose a systematic listing method, predict which assignments are most extreme, and decide before counting whether to test improvement only or any difference.

**Hour menu.** 0–10 freely group the cards; 10–15 distinguish the six equally likely assignments; 15–35 calculate the difference for every assignment; 35–40 physically switch two group signs; 40–55 compare one-sided and two-sided questions; 55–60 state a conclusion with its exact assumption.

**Explore.**

- Why do we move labels while leaving scores fixed?
- Does a difference that occurs once in six assignments prove that training works?

**Hint ladder.**

1. Choose the two trained scores; the other pair is forced.
2. Subtract untrained mean from trained mean and order the six results.

**Checked instance.** Find the one-sided and two-sided exact tail proportions for observed trained scores {3,4}.

**Reasoning.** Trained pairs {0,1},{0,3},{0,4},{1,3},{1,4},{3,4} give mean differences −3,−1,0,0,1,3. Only one of six is at least 3, giving 1/6. Two have absolute difference at least 3, giving 2/6. Neither is small at a conventional 0.05 threshold. The tail direction must not be chosen after noticing which result looks better.

**Boundary.** If training was offered to the strongest participants rather than assigned uniformly, these six assignments are not the actual randomization distribution; this calculation cannot establish a treatment effect.

**Extensions.**

- Use six outcome cards with three treatment labels; enumerate the 20 assignments and study attainable tail proportions.
- Compare random sampling, which supports population generalization, with random assignment, which supports the treatment comparison; one does not automatically supply the other.

**Satisfying stop.** A complete exact reference distribution with a carefully qualified conclusion.

**Prior use.** No matching inference design is documented in Weeks 1–10. This is not another dice-fairness lesson.

**Sources.**

- [Allen Downey, Think Stats, third edition](https://allendowney.github.io/ThinkStats/chap09.html), Section 9.2 supports permutation-test mechanics; the randomized-assignment/sharp-null version here is independently proved. Inspection: relevant exposition inspected; finite instance independently derived below.

<a id="ap-04"></a>
## AP-04 - A sampling rule that always misses

Primary field: 62. Related: 60. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why does collecting more observations fail to remove selection bias, and how does sampling design differ from sampling variability?

**Anchor.** For uniform sampling of a finite population, the sample mean is unbiased. Sampling through a systematically selected subset can have persistent bias; increasing repetitions estimates that subset more precisely.

**Bridge (exact-special-case).** A concealed finite population and explicitly defined sampling mechanisms provide a genuine unknown-parameter inference problem. Limits: The small population makes all calculations available; it does not certify any particular real survey.

**Prerequisite gates.**

- **Entry:** O/C: select labeled cards and record a number.
- **Explore:** F: calculate averages and compare the spread of repeated samples.
- **Explain:** P: pair each equally likely sample with its contribution to the average.
- **Prove:** F/A: use linearity of expectation for uniform draws.
- **Reading:** Number cards plus two short selection rules; oral participation works.
- **Arithmetic:** Means of two or four small integers; fractions.
- **Reasoning:** Separate randomness of selection from representativeness of its sampling frame.
- **Hard Stop:** Correcting unknown real-world nonresponse needs extra information; no universal arithmetic adjustment is promised.

**Materials and preparation (10 minutes).** Population cards with values 1,1,1,1,5,5,5,5, kept in two labeled sections. Prepare a full-population draw bag and a bag restricted to the four 1-cards; keep identities visible to the facilitator.

**Launch.** Estimate the average value of all eight hidden cards. Team A draws two identifiers uniformly from all eight; team B draws from the first four only. Replace each card after recording it, including between the two draws in a sample. Repeat your samples. Which extra information would make a guess trustworthy?

**Learner choices.** Choose a sampling rule, decide how many repetitions to collect, and propose an audit that might reveal a missing part of the population.

**Hour menu.** 0–10 explore guessing from covered cards; 10–15 define the target average and two selection rules; 15–35 collect independent samples with replacement; 35–40 exchange sampler and recorder roles; 40–55 reveal the population and explain contrasting records; 55–60 propose a better survey design.

**Explore.**

- Can one group be extremely consistent and still wrong?
- What is the difference between drawing randomly from a bag and including every population member in that bag?

**Hint ladder.**

1. Write the target population above the record, separately from the draw bag.
2. After revealing all eight cards, compare the mean in each sampling frame.

**Checked instance.** For two independent uniform draws with replacement from all eight cards, find the distribution of the sample mean. Compare draws restricted to the four 1-cards.

**Reasoning.** Each full-population draw is 1 or 5 with probability 1/2. The two-draw mean is 1,3,5 with probabilities 1/4,1/2,1/4, so its expected value is 3, the population mean. The restricted rule always gives mean 1, even after arbitrarily many draws; its bias is −2. Sampling more from that same frame does not repair the omission.

**Boundary.** A single full-population sample can still give 1. Unbiasedness is a repeated-sampling property, not a promise that every individual estimate is right.

**Extensions.**

- Compare samples of one, two and four cards: uncertainty shrinks while the uniform target stays 3.
- Let sampling probabilities depend on card value and investigate how known inverse-probability weights can correct a specified design; unknown selection remains a genuine obstacle.

**Satisfying stop.** Explain how a noisy estimate can be appropriately centered while a perfectly consistent estimate can be biased.

**Prior use.** No corresponding sampling-frame task is documented in the existing packets. Retain the selected population and sampling rule in future use logs.

**Sources.**

- [Allen Downey, Think Stats](https://allendowney.github.io/ThinkStats/chap08.html), Chapter 8: estimation, bias and sampling distributions. Inspection: relevant exposition inspected; finite instance independently derived below.

<a id="ap-05"></a>
## AP-05 - An interval-making machine

Primary field: 62. Related: 60. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** What does a confidence procedure guarantee over repeated samples, and what does it leave unknown after one sample?

**Anchor.** Coverage is Pθ(θ lies in I(X)) for a sampling procedure I. It is a property indexed by the unknown parameter; it need not equal a posterior probability after observing a particular interval.

**Bridge (exact-special-case).** A finite shift experiment gives exactly calculable interval coverage without asymptotic approximation. Limits: This deliberately simple instrument model is not the binomial proportion problem or a general method for constructing confidence intervals.

**Prerequisite gates.**

- **Entry:** O/C: move an interval marker to include three neighboring integer points.
- **Explore:** F/A: interpret unknown integer θ plus a random measurement error.
- **Explain:** P: list all five equiprobable errors and decide which intervals cover θ.
- **Prove:** A/P: show the covering errors are the same for every integer θ.
- **Reading:** Short instrument rules and interval endpoints; oral diagram explanation is possible.
- **Arithmetic:** Add/subtract integers up to two; fifths.
- **Reasoning:** Reason about a fixed unknown target and a random interval, not a moving target.
- **Hard Stop:** A probability distribution for θ after data requires an additional prior model; do not supply one silently.

**Materials and preparation (10 minutes).** Integer number line, an opaque envelope containing a secret integer θ, five equally likely error cards −2,−1,0,1,2, and transparent three-point interval strips.

**Launch.** Our instrument reports X=θ+E, where θ is a fixed hidden integer and E is a fresh uniform draw from −2,−1,0,1,2. After each reading X, report [X−1,X+1]. Without knowing θ, can you predict how often this interval-making rule will cover it?

**Learner choices.** Choose an interval width, compare coverage against precision, and design a rule whose advertised coverage can be checked.

**Hour menu.** 0–10 explore intervals on a number line; 10–15 establish the hidden target and error mechanism; 15–35 draw readings and place strips; 35–40 reveal θ and step to the five error positions; 40–55 prove coverage for any integer target or change width; 55–60 explain the guarantee in words.

**Explore.**

- Which errors make the interval miss, and why?
- If the observed interval is [6,8], what extra assumption would be needed to assign probabilities to possible hidden targets?

**Hint ladder.**

1. Pretend θ is 0 temporarily; list all five readings.
2. Translate the whole picture. Does the list of successful error cards change?

**Checked instance.** Compute coverage of [X−1,X+1] and [X−2,X+2]. Is the first an exact 60% procedure for every integer θ?

**Reasoning.** The first covers θ exactly when −1≤E≤1, which occurs for three of the five cards, so coverage is 3/5 for every θ. The wider interval covers for all five errors and has 100% coverage under this bounded-error model. These probabilities describe repetitions of the random instrument with θ fixed.

**Boundary.** If the error distribution puts probability 1/2 on each of −2 and 2, the narrow procedure has zero coverage. Its claim depends on the stated error mechanism, even though its printed endpoints look unchanged.

**Extensions.**

- Asymmetric intervals can have the same coverage: [X−2,X] covers errors 0,1,2. Compare their practical consequences.
- Investigate confidence procedures for an unknown coin probability later; finite sample spaces permit exact checks but the coverage calculation is no longer a translation argument.

**Satisfying stop.** A proved 60% interval procedure and an explanation of what its percentage measures.

**Prior use.** No confidence-coverage task is documented in the current collection. Do not label this a bootstrap activity; it uses a known error model.

**Sources.**

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm), Section 1.3.5.2, introductory interpretation of confidence intervals as repeated-sampling procedures; the five-error model here is independently derived, not the handbook’s t-interval example. Inspection: introductory interpretation directly inspected; all five errors independently enumerated.

<a id="ap-06"></a>
## AP-06 - A root finder caught in a two-step loop

Primary field: 65. Related: 26, 37. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why can a locally excellent numerical method fail completely from an unfortunate starting point?

**Anchor.** Newton iteration xnext=x−f(x)/f′(x) replaces a smooth equation by its tangent equation. Local convergence near a simple root does not imply convergence from every start.

**Bridge (exact-special-case).** The plotted tangent steps and rational calculations are the actual Newton algorithm on a specified cubic. Limits: A plotted curve gives visual guidance; the exact loop is established algebraically. This is not a general convergence theorem.

**Prerequisite gates.**

- **Entry:** V/A/D: coordinates, evaluating a cubic and the meaning of derivative as tangent slope.
- **Explore:** A/F: calculate successive rational iterates or direct a calculator.
- **Explain:** P: verify a repeating state and show why deterministic iteration then repeats forever.
- **Prove:** D/X: a general convergence theorem needs quantitative derivative control near a simple root.
- **Reading:** Symbolic formula and a short algorithm; shared recorder permitted.
- **Arithmetic:** Signed integers and fractions; cubic substitution.
- **Reasoning:** Distinguish the equation’s root from an algorithm’s current guess.
- **Hard Stop:** Do not remove tangency and call a number guessing game Newton’s method; calculus is a legitimate entry gate here.

**Materials and preparation (12 minutes).** Graph paper with f(x)=x^3−2x+2 drawn from −2 to 2, ruler, and calculator. Prepare a table with x, f(x), f′(x), next x.

**Launch.** The robot finds a root by following the tangent line down to the x-axis, then repeating from there. Use f(x)=x^3−2x+2 and f′(x)=3x^2−2. Start at 0. Can you predict the robot’s thousandth guess without doing a thousand calculations?

**Learner choices.** Choose starting points, compare exact and decimal records, and invent a warning rule that detects repeated states.

**Hour menu.** 0–10 explore the curve and tangent drawings; 10–15 calculate one complete Newton step together; 15–35 investigate starts 0,1 and −2; 35–40 exchange graph and calculation roles; 40–55 contrast looping with a sign-changing bracket; 55–60 state what failed and what remains true.

**Explore.**

- Does a loop mean that the original equation has no root?
- What information does a bracket supply that a single tangent guess lacks?

**Hint ladder.**

1. At 0, calculate the numerator and denominator separately.
2. Once both 0→1 and 1→0 are exact, every later iterate is determined.

**Checked instance.** Verify the loop from 0 and show that the cubic nevertheless has a real root.

**Reasoning.** f(0)=2 and f′(0)=−2, so Newton gives 1. At 1, f(1)=1 and f′(1)=1, so it gives 0. Thus even-numbered iterates are 0 and odd-numbered iterates 1. Meanwhile f(−2)=−2 and f(−1)=3; continuity guarantees a root between −2 and −1. The equation is solvable while this algorithmic run fails.

**Boundary.** At x=√(2/3), the derivative is zero, so this formula is undefined. A stopping rule based only on a small step is also not a universal accuracy certificate.

**Extensions.**

- Bisect [−2,−1] to retain a guaranteed root bracket; after n halvings its width is 2^(−n).
- Explore Newton basins for other polynomials as a numerical-dynamics continuation; state precision and maximum iterations rather than treating a picture as proof.

**Satisfying stop.** A fully proved infinite loop and a guaranteed root bracket coexist.

**Prior use.** The advisory atlas already uses this Newton counterexample. Record this as its developed facilitation card, not a newly discovered example.

**Sources.**

- [Yano, Penn, Konidaris and Patera, Math, Numerics, and Programming](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-spring-2013/60af88c658ba3e83cdf7c43289aeb5b4_MIT2_086S13_Unit6_Textbook.pdf), Section 29.2: Newton iteration and pathologies. Inspection: relevant exposition inspected; displayed instance independently derived.

<a id="ap-07"></a>
## AP-07 - A cooling model that heats itself up

Primary field: 65. Related: 34, 80. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can discretizing a stable differential equation produce oscillation or explosive growth?

**Anchor.** Forward Euler applied to y′=−ay with a>0 gives y[n+1]=(1−ah)y[n]. The numerical magnitude decays exactly when |1−ah|<1, whereas the continuous solution y(0)exp(−at) always decays.

**Bridge (exact-special-case).** The finite recurrence is precisely an Euler discretization of the specified scalar ODE. Comparing its multiplier with the continuous solution preserves a numerical-stability question. Limits: No claim that every recurrence is an ODE or that stability alone guarantees small discretization error.

**Prerequisite gates.**

- **Entry:** F/A: signed multiplication and repeated updates.
- **Explore:** V: plot a table at equally spaced times; compare signs and magnitudes.
- **Explain:** A/P: classify powers of a constant multiplier.
- **Prove:** D: relate the update to the differential equation; A suffices for recurrence stability.
- **Reading:** A short recurrence; a partner can maintain the table.
- **Arithmetic:** Halves, signed integers and powers.
- **Reasoning:** Track three distinct objects: physical temperature difference, continuous model, and numerical approximation.
- **Hard Stop:** General ODE error bounds need calculus and regularity hypotheses. The recurrence analysis is a satisfying independent stop.

**Materials and preparation (5 minutes).** Graph paper and two-color counters representing positive and negative differences from room temperature; calculator optional. No actual hot water is necessary.

**Launch.** A model says the difference from room temperature falls at a rate equal to itself. Our computer approximates one step by “new difference = old difference − h times old difference.” Start at 8. Choose h from 1/2,1,3/2,2,3. Which choices look like cooling, and which invent strange behavior?

**Learner choices.** Choose step sizes, decide what counts as a sensible approximation, and separate monotone decay from merely shrinking magnitude.

**Hour menu.** 0–10 explore update cards; 10–15 identify the signed difference variable; 15–35 generate and plot sequences; 35–40 use body positions above/below a floor line for signs; 40–55 classify every positive h or compare equal elapsed time; 55–60 present a numerical failure.

**Explore.**

- Why does a negative value mean below room temperature rather than negative absolute temperature?
- Can a shrinking sequence still be a poor picture of monotone cooling?

**Hint ladder.**

1. Rewrite the update as multiplication by 1−h.
2. Classify whether the multiplier is between 0 and 1, between −1 and 0, exactly −1, or below −1.

**Checked instance.** Compare h=1/2, h=3/2 and h=3 from y0=8.

**Reasoning.** The multipliers are 1/2,−1/2,−2. Sequences begin 8,4,2,1; 8,−4,2,−1; and 8,−16,32,−64. The first decays monotonically, the second decays while alternating, the third grows in magnitude. For a=1, stability is 0<h<2. Only the first qualitatively matches positive monotone continuous decay.

**Boundary.** At h=2, values alternate 8,−8 forever: bounded does not mean converging to equilibrium. At h=1, Euler reaches zero immediately, although the continuous solution remains positive at every finite time.

**Extensions.**

- For a=2, derive 0<h<1 rather than copying the previous threshold.
- Compare equal elapsed times with h=1/2 and h=1/4; discuss convergence separately from stability.

**Satisfying stop.** A complete classification of one update rule and an explanation of why smaller steps can matter.

**Prior use.** No numerical time-stepping investigation is documented in the existing worksheets. This extends continuous mathematics beyond the existing bisection prototype.

**Sources.**

- [Driscoll and Braun, Fundamentals of Numerical Computation](https://fncbook.com/), Chapter 6 initial-value problems and chapter 11 diffusion located; scalar stability proof supplied here. Inspection: chapter scope inspected; scalar Euler stability proof supplied independently on this card.

<a id="ap-08"></a>
## AP-08 - How much memory does the red-symbol machine need?

Primary field: 68. Related: 03, 20. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can one prove that a finite-state machine needs at least a given number of states?

**Anchor.** For strings over {R,B}, the language with a multiple of three R symbols has a three-state deterministic automaton. Prefixes with different R-count remainders are distinguishable by a common suffix, proving a three-state lower bound.

**Bridge (exact-special-case).** Floor circles are machine states, arrows are transitions, and ending at a marked circle is acceptance. Limits: This finite-memory language is not an example of undecidability or proof of a complexity-class separation.

**Prerequisite gates.**

- **Entry:** O/C: follow one arrow per symbol and remember only the current circle.
- **Explore:** M: count red symbols modulo three, or group counters in triples.
- **Explain:** P: compare histories through the future strings that distinguish them.
- **Prove:** P: contradiction using two histories assigned the same state.
- **Reading:** Two symbol labels and arrow directions; spoken symbol streams work.
- **Arithmetic:** Counts and remainders modulo three; no large computation.
- **Reasoning:** The machine cannot secretly remember earlier symbols outside its state.
- **Hard Stop:** Pumping lemmas and arbitrary language proofs need quantified string reasoning; no need to introduce them before the concrete lower bound.

**Materials and preparation (8 minutes).** Three floor circles or paper cards, R and B arrow cards, and a star marking the accepting state. Provide short example strings and blank cards for learner tests.

**Launch.** Build a machine that reads R and B cards one at a time and says yes exactly when the number of R cards is a multiple of three, including zero. It may remember only which circle its token occupies. Can two circles do the job, or are three necessary?

**Learner choices.** Choose state labels, design transitions, invent tests that break a proposed machine, and decide how to convince another group that two states cannot suffice.

**Hour menu.** 0–10 play human machines on short strings; 10–15 enforce the memory rule; 15–35 build and attack two- and three-state designs; 35–40 walk the machine with spoken symbols; 40–55 develop a distinguishing-history proof; 55–60 demonstrate an accepting and rejecting example.

**Explore.**

- What should a B do to the state?
- If two different histories leave the same state, what happens when the same future cards follow both?

**Hint ladder.**

1. Name states by red counts 0,1,2 after discarding complete triples.
2. Compare the three histories empty, R and RR. Can each pair be separated by an appropriate suffix?

**Checked instance.** Construct a correct three-state machine and rule out every deterministic two-state machine.

**Reasoning.** States q0,q1,q2 record remainder 0,1,2. R advances cyclically; B stays put; q0 starts and accepts. Among empty,R,RR, a two-state machine puts some pair in the same state. Empty versus R are distinguished by empty suffix; empty versus RR likewise. R versus RR are distinguished by suffix R: RR rejects but RRR accepts. Identical states must react identically to identical suffixes, contradiction.

**Boundary.** If the task only allows input strings of length at most one, two states suffice. The lower bound depends on allowing every finite length.

**Extensions.**

- Replace three by m and prove m states are necessary using remainder histories and suitable suffixes.
- Add a second condition, such as even B count, and investigate product states; prove necessity rather than assuming every product is minimal.

**Satisfying stop.** A working machine plus a convincing reason that fewer states cannot solve the unrestricted task.

**Prior use.** Weeks 3–4 use cyclic permutations and modular orbits. The new question concerns memory sufficiency and lower bounds, not another cycle table.

**Sources.**

- [Michael Sipser, MIT Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf), Lecture 1: deterministic finite automata and acceptance. Inspection: relevant exposition inspected; displayed instance independently derived.

<a id="ap-09"></a>
## AP-09 - Find the two dances hidden in coupled springs

Primary field: 70. Related: 15, 34. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why do coupled linear systems have collective modes, and how do these modes simplify motion?

**Anchor.** Two unit masses joined to each other and fixed walls by three unit Hookean springs obey x″=−Kx with K=[[2,−1],[−1,2]]. Eigenvectors (1,1) and (1,−1) have eigenvalues 1 and 3, hence angular frequencies 1 and √3.

**Bridge (exact-special-case).** Two displacement coordinates and their restoring-force arrows realize the specified linear mechanical system exactly on paper. Limits: Real springs and swinging demonstrations approximate the model; friction, unequal components and large deformations alter it.

**Prerequisite gates.**

- **Entry:** F/V: signed displacements from two equilibrium marks and force arrows.
- **Explore:** A: evaluate the two force formulas at chosen positions.
- **Explain:** L: recognize proportional vectors and decompose a displacement into two modes.
- **Prove:** D: differentiate cosine solutions twice and substitute into the ODE.
- **Reading:** Two coordinate formulas; a diagram supports paired explanation.
- **Arithmetic:** Signed sums, halves, and an optional square root.
- **Reasoning:** Two masses move simultaneously; equal displacement differs from equal force.
- **Hard Stop:** The claim about temporal frequency needs the ODE and calculus. Before that, force-pattern eigenvectors are the honest mathematical result.

**Materials and preparation (10 minutes).** Two movable paper mass markers on parallel number lines, three drawn springs, and arrows. A physical spring setup is optional and takes extra preparation; the paper core is sufficient.

**Launch.** Call the displacements from rest x1 and x2. The model gives forces F1=−2x1+x2 and F2=x1−2x2. Find starting displacement pairs for which the force pattern is a negative multiple of the starting pattern. Can you find two essentially different coordinated motions?

**Learner choices.** Choose displacement pairs, scale a successful pair, compare equal and opposite movements, and decide how an arbitrary position might be assembled from special patterns.

**Hour menu.** 0–10 explore displacement markers and spring extension signs; 10–15 establish the force formulas; 15–35 test patterns and make a force table; 35–40 move in matched and opposite pairs; 40–55 decompose (2,0) or verify cosine motions; 55–60 share a mode and its scope.

**Explore.**

- Why does moving both masses equally leave the middle spring unchanged?
- Which pattern receives the stronger restoring force for the same displacement magnitude?

**Hint ladder.**

1. Try (1,1) and (1,−1).
2. Add those two position patterns coordinate by coordinate.

**Checked instance.** Find modes and express displacement (2,0) as their combination, with both initial velocities zero.

**Reasoning.** K(1,1)=(1,1) and K(1,−1)=3(1,−1). Also (2,0)=(1,1)+(1,−1). Therefore x(t)=cos(t)(1,1)+cos(√3 t)(1,−1). Differentiating twice gives the prescribed restoring equation, and x(0)=(2,0), x′(0)=0. Learners without calculus can stop at the exact force and decomposition statements.

**Boundary.** For an initial pattern (1,0), the force (−2,1) is not proportional to that pattern; the second mass cannot remain still under this model.

**Extensions.**

- Change the middle stiffness to k>0; equal motion keeps eigenvalue 1, while opposite motion has eigenvalue 1+2k.
- Generalize to longer chains and vibration spectra after matrix and eigenvalue prerequisites.

**Satisfying stop.** Two collective patterns and an exact decomposition of a non-collective starting shape.

**Prior use.** No coupled-oscillation task is documented. This adds mechanics and linear algebra rather than relabeling a static balance puzzle.

**Sources.**

- [David Tong, Classical Dynamics](https://davidtong.org/teaching/classical-dynamics/dynhtml/S2), Section 2.6: small oscillations and stability. Inspection: relevant exposition inspected; displayed instance independently derived.

<a id="ap-10"></a>
## AP-10 - Which spring arrangement stretches farther?

Primary field: 74. Related: 15, 90. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How do local constitutive laws and connection constraints combine into an effective material response?

**Anchor.** An ideal Hookean spring satisfies F=kx. Springs in parallel share extension and add forces; springs in series share force and add extensions. Thus kparallel=k1+k2 and 1/kseries=1/k1+1/k2.

**Bridge (exact-special-case).** The spring diagrams are finite elastic systems with specified force and displacement compatibility, not arbitrary weighted graphs. Limits: The Hookean relation is an idealization. A rubber band’s response must be measured rather than assumed linear.

**Prerequisite gates.**

- **Entry:** O/V: distinguish end-to-end and side-by-side arrangements on a diagram.
- **Explore:** F/A: use F=kx and add force or extension according to the connection.
- **Explain:** P: identify the shared quantity before calculating.
- **Prove:** A: eliminate internal forces or displacements from the two spring equations.
- **Reading:** Labels k,F,x; a facilitator can narrate loading directions.
- **Arithmetic:** Fractions and reciprocals; small multiplication.
- **Reasoning:** Avoid confusing stiffness with force, or total extension with each spring’s extension.
- **Hard Stop:** Continuum elasticity requires strain, stress and calculus; these finite networks do not establish material failure or buckling laws.

**Materials and preparation (10 minutes).** Reusable paper spring symbols, load arrows, and ruler scales. Optional identical safe elastic elements and small masses can test approximate behavior, with forces kept modest.

**Launch.** You have two ideal springs. Spring A needs 2 force units per extension unit, and B needs 6. Predict how far a load of 6 stretches them when connected end-to-end, then when connected side-by-side between rigid bars. Defend which quantity is equal in each arrangement.

**Learner choices.** Choose how to draw the connections, select a test load, design a target stiffness, and decide whether a physical observation fits the ideal model.

**Hour menu.** 0–10 explore connection diagrams or elastic pieces; 10–15 introduce each spring’s law; 15–35 solve and compare arrangements; 35–40 trace force paths with partners; 40–55 build three-spring variants or examine measured deviations; 55–60 present a prediction with its assumptions.

**Explore.**

- Can adding a spring make the arrangement softer?
- Why is the load split in parallel but not in series?

**Hint ladder.**

1. Draw each spring as a separate object and label its two endpoint forces.
2. For series, add extensions. For parallel, add forces at the common moving bar.

**Checked instance.** For kA=2,kB=6 and load F=6, calculate total extension in both arrangements.

**Reasoning.** In series, each carries force 6, giving extensions 3 and 1, total 4. Effective stiffness is 6/4=3/2. In parallel, both extend x; total force is 2x+6x=8x, so x=3/4 and stiffness is 8. The stiffer branch carries force 6×3/4=9/2, while the other carries 3/2. Both totals check.

**Boundary.** Equal-force reasoning is wrong for parallel unequal springs: it would predict incompatible extensions 3/2 and 1/2 if each carried force 3. A rigid common bar requires equal extension.

**Extensions.**

- Use two identical springs of stiffness k to get k/2 in series and 2k in parallel, explaining the factor without fractions first.
- Build series-parallel networks for a chosen target stiffness; non-series-parallel networks lead to linear systems and energy minimization.

**Satisfying stop.** A surprising, quantitatively checked reversal: adding a spring can make a device softer or stiffer.

**Prior use.** No prior elastic-network task is documented; mathematical similarity to resistor networks will be cross-linked rather than counted as unrelated content.

**Sources.**

- [Allan Bower, Applied Mechanics of Solids](https://solidmechanics.org/Text/Chapter3_2/Chapter3_2.php), Section 3.2: linear elastic behavior; spring-network equations derived explicitly here. Inspection: relevant exposition inspected; displayed instance independently derived.

<a id="ap-11"></a>
## AP-11 - The narrow channel and the impossible flow map

Primary field: 76. Related: 35, 65. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How does local conservation constrain a continuous flow, and how can a proposed flow field be rejected before solving its dynamics?

**Anchor.** For steady incompressible flow through a stream tube with impermeable walls, volume flux Q=integral(u·n dA) is constant between cross-sections. If speed is uniform across a section, Q=Av; otherwise v denotes the section’s mean normal speed.

**Bridge (exact-special-case).** Area-and-mean-speed sections describe an ideal continuous incompressible stream tube. Conservation relates their fluxes directly. Limits: Counters can represent fixed volume parcels but do not prove continuum dynamics. No pressure claim is inferred from continuity alone.

**Prerequisite gates.**

- **Entry:** O/C/V: compare cross-section sizes and count volume packets per time interval.
- **Explore:** F: multiply area by speed and divide a fixed flux by area.
- **Explain:** P: use a control-volume storage ledger to reject unequal in/out flow.
- **Prove:** D/I: integrate the continuity equation or use the divergence theorem.
- **Reading:** A few area and speed labels; arrows and oral rules suffice.
- **Arithmetic:** Multiplication and division of small positive values; units.
- **Reasoning:** Distinguish speed, volume rate, and water already stored between sections.
- **Hard Stop:** Pressure differences require momentum/energy laws and assumptions; turbulence and viscosity cannot be deduced from this ledger.

**Materials and preparation (7 minutes).** Draw a wide-to-narrow tube with two cross-sections; use equal volume blocks and a one-second time card. Optional water transfer uses measuring cups, not a pressure demonstration.

**Launch.** A tube carries incompressible water steadily with no leaks. At its wide section the area is 6 square units and average forward speed is 2 units per second. At the narrow section the area is 3. What average speed is possible? Invent a flow map that looks plausible but cannot stay steady.

**Learner choices.** Choose areas, propose speeds, decide where extra water would accumulate in a bad map, and add a branch or storage reservoir deliberately.

**Hour menu.** 0–10 move equal-volume blocks between regions; 10–15 specify steady, incompressible and no-leak rules; 15–35 design and audit section labels; 35–40 act as equal-volume parcels crossing gates; 40–55 add branches or a changing reservoir; 55–60 explain one impossible flow map.

**Explore.**

- Why does a narrower channel require faster average flow under these assumptions?
- What would unequal inflow and outflow tell you if the region could store water?

**Hint ladder.**

1. Ask how much volume crosses each section in one second.
2. Inventory the water between the sections before and after that second.

**Checked instance.** Find narrow-section speed, then audit a proposed exit speed 3.

**Reasoning.** The incoming flux is 6×2=12 volume units per second. Conservation requires 3v=12, giving v=4. If the proposed speed were 3, outgoing flux would be 9 and the intervening region would gain 3 volume units per second. That contradicts steady flow in a rigid full tube with no leaks and incompressible material.

**Boundary.** For a reservoir whose level rises, unequal inflow and outflow is allowed: storage changes. For compressible gas, conserve mass flux ρAv rather than volume flux Av.

**Extensions.**

- Split flux 12 between two branches with areas 2 and 1; explore the infinitely many nonnegative flow allocations before additional physics chooses one.
- With calculus, derive the integral continuity law; with mechanics, add a justified Bernoulli relation and compare its stronger assumptions.

**Satisfying stop.** Reject an impossible continuous flow map using a clear volume-accounting argument.

**Prior use.** Week 10 route networks concern traversal; this question concerns conservation of flowing material and cannot be counted as another route puzzle.

**Sources.**

- [David Tong, Fluid Mechanics](https://davidtong.org/pdfs/teaching/fluid-mechanics/fluids1.pdf), Continuity equation and narrowing-pipe Bernoulli example, PDF pp. 23–24. Inspection: relevant exposition inspected; exact model calculation supplied here.

<a id="ap-12"></a>
## AP-12 - Where should the fastest path cross the shoreline?

Primary field: 78. Related: 49, 26. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why does a ray bend at a boundary between media, and how does minimizing travel time differ from minimizing distance?

**Anchor.** In two homogeneous isotropic media with positive constant speeds, a path made of straight segments meeting a flat interface has travel time T(x). Minimizing T yields the Snell relation sin(θ1)/v1=sin(θ2)/v2, with angles measured from the normal.

**Bridge (exact-special-case).** The adjustable crossing point parameterizes actual geometric-optics travel paths in the two-speed idealization. Limits: This variational calculation assumes the ray model; it does not derive Maxwell’s equations or wave diffraction.

**Prerequisite gates.**

- **Entry:** V/A: coordinates, Pythagoras and distance divided by speed.
- **Explore:** F: compute and compare square-root travel times or measure scaled segments.
- **Explain:** D: differentiate the time function and identify its zero derivative.
- **Prove:** D/P: positive second derivative proves the stationary point is the unique global minimizer.
- **Reading:** A diagram with speed labels and the time formula.
- **Arithmetic:** Square roots and fractions; exact 3–4–5 triangles make the worked optimum accessible.
- **Reasoning:** Distance and time are competing quantities; angles must be measured from a stated reference.
- **Hard Stop:** Without calculus, comparison gives evidence and an exact candidate, not a proof over all continuous crossing points.

**Materials and preparation (10 minutes).** Coordinate paper, ruler, two colored half-planes separated by y=0, and a sliding crossing marker. A calculator is optional for exploratory comparisons.

**Launch.** Travel from A=(0,4) to B=(7,−3), crossing the shoreline y=0 once. Above it speed is 3; below it speed is 4. Each segment is straight. Choose the crossing point (x,0) to minimize total time. Must the fastest route be the shortest route?

**Learner choices.** Choose trial crossing points, organize numerical or geometric comparisons, and decide what extra reasoning certifies the best continuous choice.

**Hour menu.** 0–10 explore paths and speed labels; 10–15 define total time; 15–35 compare candidate crossings; 35–40 trace two routes with different walking tempos; 40–55 differentiate or verify the proposed optimum; 55–60 contrast an experimental minimum with a proof.

**Explore.**

- Which side should gain distance when its speed is greater?
- Does a zero derivative alone prove the crossing is globally best?

**Hint ladder.**

1. Write T(x)=√(x²+16)/3+√((7−x)²+9)/4.
2. At x=3 both segment lengths are 5, making the derivative simple.

**Checked instance.** Prove x=3 uniquely minimizes travel time over all real crossing positions.

**Reasoning.** T′(x)=x/(3√(x²+16))−(7−x)/(4√((7−x)²+9)). At x=3, both terms equal 1/5. Also T″(x)=16/[3(x²+16)^(3/2)]+9/[4((7−x)²+9)^(3/2)] is positive everywhere. Thus T is strictly convex and x=3 is its unique global minimizer, with time 5/3+5/4=35/12. The direct straight route crosses at x=4, so shortest and fastest differ.

**Boundary.** If both speeds are equal, minimizing time is minimizing distance and the straight path is optimal. Changing the interface shape changes the parameterization.

**Extensions.**

- Vary the lower speed and predict the optimal crossing direction before calculating.
- Derive Snell’s relation by identifying each derivative ratio as a sine; total internal reflection is a separate wave-boundary question, not established here.

**Satisfying stop.** A concrete optimum whose geometry, time and proof all agree.

**Prior use.** Week 9 billiards uses reflections and unfolding. Refraction with unequal speeds adds a genuinely different continuous optimization mechanism.

**Sources.**

- [David Tong, Electromagnetism](https://www.davidtong.org/pdfs/teaching/electromagnetism/electro3.pdf), Wave and boundary framework inspected; Fermat optimization for this geometry proved self-contained below. Inspection: relevant exposition inspected; exact model calculation supplied here.

<a id="ap-13"></a>
## AP-13 - Add a wave and make the signal smaller

Primary field: 78. Related: 42. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why do coherent signals combine at the amplitude level, and how can adding a signal reduce local intensity?

**Anchor.** For same-frequency coherent scalar waves at a fixed location, amplitudes add linearly. If E(t)=A sin(t)+B sin(t+φ), the normalized time-averaged intensity 2⟨E²⟩ is A²+B²+2AB cosφ.

**Bridge (exact-special-case).** Signed waveform strips and their pointwise sums are exact scalar coherent-wave calculations. Limits: The scalar model fixes location, frequency and polarization. It does not describe every source, global energy flow, or incoherent light.

**Prerequisite gates.**

- **Entry:** V/F: compare heights above and below an axis and add signed heights.
- **Explore:** A: scale a sine-shaped template and shift it by half a period.
- **Explain:** P: show pointwise reinforcement or cancellation.
- **Prove:** Trigonometry and I: derive the time-average formula for an arbitrary phase.
- **Reading:** Wave labels can be pictures; full formula is an optional symbolic extension.
- **Arithmetic:** Signed sums and squares; fractions for averages.
- **Reasoning:** Do not add intensities before adding coherent amplitudes; distinguish a single location from the whole field.
- **Hard Stop:** Without phase and coherence assumptions, the interference formula is not justified. General electromagnetic energy conservation needs more physics.

**Materials and preparation (15 minutes).** Transparent sine-wave strips with amplitude 2 and amplitude 1, a shared horizontal time axis, and blank sum graphs. Preprint half-period alignment marks.

**Launch.** At one sensor, wave A has height 2 sin(t). You may add wave B with height sin(t) or −sin(t). Add their heights at each time before comparing the resulting signal. Can adding a wave make the sensor’s average squared reading smaller?

**Learner choices.** Choose relative phase, decide which sample times expose cancellation, and invent amplitude pairs that silence the sensor entirely.

**Hour menu.** 0–10 overlay and slide wave strips; 10–15 define pointwise addition; 15–35 draw sums and compare squared amplitudes; 35–40 partners move in phase and opposite phase; 40–55 explore unequal amplitudes or intermediate phase; 55–60 explain why the word add can mislead.

**Explore.**

- Why is the sum of two nonzero waves sometimes zero at every time?
- What assumption would fail if the second wave’s phase drifted unpredictably?

**Hint ladder.**

1. Start with the same phase and then turn one strip upside down.
2. For C sin(t), mean square is C²/2 over a full period; use 2 times that average as normalized intensity.

**Checked instance.** Compare normalized intensity before adding B, with B in phase, and with B opposite in phase.

**Reasoning.** Wave A alone has amplitude 2 and normalized intensity 4. In phase, E=3 sin(t), giving 9. Opposite in phase, E=sin(t), giving 1. Adding the same amplitude-1 wave therefore either increases or decreases the sensor’s intensity. With A=B=1 and opposite phase, the local field vanishes. These follow pointwise before any averaging.

**Boundary.** Independent drifting phases can average the cross term to zero, giving intensity A²+B² instead. Local cancellation does not mean energy vanished everywhere; source work and the spatial field require a larger model.

**Extensions.**

- Use a quarter-period shift and prove the normalized intensity is A²+B² for that coherent special phase.
- Generalize to rotating phasor vectors and Fourier superposition; unequal frequencies require a specified averaging interval.

**Satisfying stop.** A surprising reduction verified by both a waveform drawing and an exact calculation.

**Prior use.** No wave-superposition task is documented. Pattern repetition alone would not count as an equivalent investigation.

**Sources.**

- [David Tong, Electromagnetism](https://www.davidtong.org/pdfs/teaching/electromagnetism/electro3.pdf), Section 4.3: plane waves, polarization and superposition, PDF pp. 20–22. Inspection: relevant exposition inspected; exact model calculation supplied here.

<a id="ap-14"></a>
## AP-14 - Can the heat-engine sales pitch be true?

Primary field: 80. Related: 49. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How do conservation and entropy constrain possible transformations more strongly than either condition alone?

**Anchor.** For a cyclic engine exchanging heat Qh with a hot reservoir Th and rejecting Qc to a cold reservoir Tc, W=Qh−Qc. The reservoir entropy change is Qc/Tc−Qh/Th≥0; hence W≤Qh(1−Tc/Th), with equality for a reversible ideal engine.

**Bridge (exact-special-case).** Heat and work ledgers with two fixed absolute-temperature reservoirs are the exact algebraic constraints of an ideal thermodynamic cycle. Limits: Passing these necessary tests is not a construction of a real engine. The model omits finite-rate losses and engineering details.

**Prerequisite gates.**

- **Entry:** C/F: account for incoming heat, outgoing heat and work.
- **Explore:** F/A: divide heat quantities by absolute temperature.
- **Explain:** P: show why an energy-balanced proposal can still violate the entropy condition.
- **Prove:** A: rearrange the two constraints; deriving the second law itself is a separate physical foundation.
- **Reading:** Short proposal cards and a three-column ledger.
- **Arithmetic:** Small subtraction and simple fractions; ratios use kelvin.
- **Reasoning:** Distinguish a whole cycle from an intermediate state and internal changes from reservoir changes.
- **Hard Stop:** Entropy cannot be replaced with an undefined messiness metaphor. Advanced cycle analysis requires thermodynamic state variables and calculus.

**Materials and preparation (8 minutes).** Two reservoir cards labeled 600 K and 300 K, twelve heat tokens, work tokens and proposal sheets. This is a paper model; no hot materials or actual engine are needed.

**Launch.** Every engine must return to its starting internal state. It takes 12 heat units from a 600 K reservoir, sends Qc heat units to a 300 K reservoir, and outputs W work units. Design the biggest work claim that passes both W+Qc=12 and Qc/300−12/600≥0.

**Learner choices.** Choose heat/work splits, test a rival sales pitch, and compare changing the hot temperature with changing the cold temperature.

**Hour menu.** 0–10 explore token energy ledgers; 10–15 add the entropy constraint and absolute temperatures; 15–35 design, test and sort proposals; 35–40 physically transfer tokens between labeled stations; 40–55 change reservoir temperatures or cascade engines; 55–60 state the strongest valid bound.

**Explore.**

- Why is energy conservation insufficient to rule out converting all incoming heat to work?
- What happens to the maximum work when the two reservoir temperatures approach each other?

**Hint ladder.**

1. First eliminate one variable using energy balance.
2. The entropy inequality gives a minimum rejected heat, which gives a maximum work.

**Checked instance.** Evaluate proposals (W,Qc)=(8,4),(6,6),(4,8).

**Reasoning.** All conserve energy. Entropy changes are 4/300−12/600=−1/150, 0, and 1/150. Thus the first violates the second-law condition, the second reaches the reversible bound, and the third passes with positive entropy production. The maximum permitted work is 6. Passing the two tests is necessary within this model, not a guarantee that a proposed machine exists.

**Boundary.** Using the corresponding Celsius temperatures in the efficiency ratio would be invalid: ratios require absolute temperature. A third reservoir, net internal-state change or external work input also changes the ledger.

**Extensions.**

- With Th=600 K and Tc=400 K, the same heat budget permits at most 4 work units.
- Cascade reversible engines through an intermediate temperature and show the combined reversible efficiency still equals 1−Tc/Th.

**Satisfying stop.** Reject a tempting perpetual-motion-style proposal with an exact second constraint.

**Prior use.** No thermodynamic-cycle investigation is documented. This deliberately remains an algebraic thermodynamics entry rather than a generic sharing game.

**Sources.**

- [David Tong, Statistical Physics](https://davidtong.org/teaching/statistical-physics/statmechhtml/S4), Chapter 4: heat engines, entropy and Carnot efficiency. Inspection: relevant exposition inspected; exact model calculation supplied here.

<a id="ap-15"></a>
## AP-15 - Does the order of two quantum questions matter?

Primary field: 81. Related: 15, 60. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can two projective measurements fail to commute, even when each has only two possible answers?

**Anchor.** In a real two-component restriction of a two-dimensional quantum model, a normalized state ψ measured in an orthonormal basis yields outcome vector b with probability |b·ψ|² and updates to b. Measurement order can change the recorded joint outcomes. General complex states require the complex inner product.

**Bridge (exact-special-case).** Real normalized two-component states and projectors form a genuine restricted quantum model; the activity uses its exact probability/update rules. Limits: Ordinary arrows are representations of amplitudes, not hidden particle directions. General states have complex amplitudes, and this card does not establish an interpretation of measurement.

**Prerequisite gates.**

- **Entry:** V/F/L: vectors (1,0),(0,1) and diagonal unit vectors, dot products, squaring and probability trees.
- **Explore:** L: distinguish basis coordinates from a physical state and apply the stated update.
- **Explain:** P: sum probabilities over intermediate outcomes.
- **Prove:** L: compute noncommuting projectors and their sequential measurement probabilities.
- **Reading:** Symbolic rules; a facilitator may read the rule aloud and demonstrate one transition before learners construct the sequence trees.
- **Arithmetic:** Halves, quarters and 1/√2; calculator unnecessary with supplied dot products.
- **Reasoning:** Separate unknown outcome from state update; discard unobserved intermediate labels only after summing their branches.
- **Hard Stop:** Do not remove the Born rule or projection update and still call the resulting coin game quantum measurement.

**Materials and preparation (12 minutes).** Four state-arrow cards e0=(1,0), e1=(0,1), +=(1,1)/√2, −=(1,−1)/√2; branch-tree sheets and counters. Supply a dot-product table if needed.

**Launch.** Start in state e0. A Z question measures in {e0,e1}; an X question measures in {+,−}. Use squared dot products for probabilities and replace the state by the outcome card. Compare X then Z with Z then X. Record the Z answer wherever it occurs in each order. How often is that answer e1?

**Learner choices.** Choose measurement sequences, organize intermediate branches, and search for a sequence that changes a formerly certain answer.

**Hour menu.** 0–10 explore unit-vector projections; 10–15 establish probabilities and update separately; 15–35 build exact sequence trees; 35–40 exchange state keeper and probability recorder; 40–55 compare X–Z and Z–X or repeated measurements; 55–60 explain the order effect with a tree.

**Explore.**

- Why does asking Z twice immediately give the same second answer?
- Why can an unreported X result still change the later Z statistics?

**Hint ladder.**

1. For e0 measured in X, both squared dot products equal 1/2.
2. From either diagonal state, a Z measurement gives e0 and e1 with equal probability.

**Checked instance.** Compare the recorded Z outcome in X→Z and Z→X; also check Z alone and Z→Z.

**Reasoning.** In X→Z, X gives + or − with probability 1/2 each. Each branch then yields Z=e1 with probability 1/2, totaling 1/4+1/4=1/2. In Z→X, the first Z returns e0 with certainty, so its recorded e1 probability is zero. Z alone and Z→Z also never yield e1. The claim concerns recorded outcome statistics: the final unconditional mixed state is the same for these particular two mutually unbiased dephasing orders, so no difference between those final mixed states is asserted.

**Boundary.** If the two measurements use the same basis, repeated measurement does not create the order effect. Ignoring the state update incorrectly predicts the original statistics throughout.

**Extensions.**

- Using matrices P0=[[1,0],[0,0]] and P+=[[1,1],[1,1]]/2, verify P0P+ differs from P+P0.
- Allow a continuously rotated real basis and derive sin²θ/cos²θ probabilities; complex phases and entanglement are separate later branches.

**Satisfying stop.** An exact probability-tree comparison showing why a prior measurement changes a later question.

**Prior use.** No finite quantum-measurement family is documented. Classical polarizer experiments may motivate it but are not substitutes for these stated quantum rules.

**Sources.**

- [David Tong, Quantum Mechanics](https://www.davidtong.org/teaching/quantum-mechanics/qmhtml/S3), Sections 3.1–3.4: states, measurement, operators and commutation. Inspection: relevant exposition inspected; exact model calculation supplied here.

<a id="ap-16"></a>
## AP-16 - Count the tiny magnet before running it

Primary field: 82. Related: 05, 60. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can energetic preference compete with the number of available microscopic arrangements?

**Anchor.** A four-spin open Ising chain has spins ±1 and three adjacent interactions. Assign each configuration weight 2^a, where a is its number of agreeing adjacent pairs. This is a canonical Ising distribution at a specified positive inverse-temperature coupling, up to a common factor.

**Bridge (exact-special-case).** Four two-sided counters are literal spin configurations; adjacent-pair weights define a genuine finite statistical-mechanics ensemble. Limits: Sixteen states cannot exhibit a true thermodynamic-limit phase-transition singularity. The weights are a stipulated model, not measured magnetic behavior.

**Prerequisite gates.**

- **Entry:** O/C: flip four counters and count agreeing neighbors.
- **Explore:** M: organize configurations and attach powers of two as weights.
- **Explain:** F/P: distinguish counts from weighted probabilities.
- **Prove:** P: encode a configuration by its first spin and three agree/disagree choices.
- **Reading:** Color symbols and a short weight rule; oral explanation works.
- **Arithmetic:** Counts to 16, weights to 8, totals to 54; probability fractions optional.
- **Reasoning:** Configurations with equal energy share weights, but groups contain unequal numbers of configurations.
- **Hard Stop:** Infinite-volume phase transitions and criticality require limits and additional analysis; no claim that this toy has a critical temperature.

**Materials and preparation (8 minutes).** Four reversible red/blue counters per group, a strip showing exactly three neighbor links, and a table for agreement count 0,1,2,3. Do not wrap the chain into a ring.

**Launch.** Make every red/blue arrangement of four counters in a row. Count its agreeing neighboring pairs. Its raffle weight is 2 raised to that count: 1,2,4 or 8. Which total weight belongs to perfectly aligned arrangements, and which belongs to the more numerous partly aligned arrangements?

**Learner choices.** Choose an enumeration method, predict the largest weight class, and compare uniform sampling with the interaction-weighted model.

**Hour menu.** 0–10 play with spin patterns; 10–15 establish open ends and the weight rule; 15–35 catalog all sixteen configurations; 35–40 act as four neighbors agreeing or disagreeing; 40–55 calculate class probabilities or change the weight factor; 55–60 explain energy-versus-multiplicity competition.

**Explore.**

- Can a group of individually less-favored arrangements outweigh the two best-favored arrangements?
- Why does changing the first spin not change the agreement pattern?

**Hint ladder.**

1. Choose the first color, then choose agree or disagree independently at each of the three links.
2. For a fixed agreement count a, there are 2 times “three choose a” configurations.

**Checked instance.** Find class multiplicities, total weight and probability of complete alignment.

**Reasoning.** For a=0,1,2,3 the multiplicities are 2,6,6,2. Their total weights are 2,12,24,16, summing to 54. Complete alignment therefore has probability 16/54=8/27. The a=2 class has greater total weight, 24/54, despite each member having weight 4 rather than 8. Under uniform sampling alignment has probability 2/16=1/8.

**Boundary.** Closing the row into a ring adds an interaction. The three independent edge-choice count no longer applies; a ring must have an even number of disagreements.

**Extensions.**

- Replace factor 2 by b>0 and derive total weight 2(1+b)^3; alignment probability becomes b^3/(1+b)^3.
- Compare longer open chains with rings, then distinguish finite partition functions from infinite-system phase transitions.

**Satisfying stop.** A complete sixteen-state ensemble whose most numerous and most favored classes differ.

**Prior use.** No statistical-ensemble activity is documented. Coin colors alone are not a new family; the interaction weights and multiplicity question define this one.

**Sources.**

- [David Tong, Statistical Physics](https://davidtong.org/teaching/statistical-physics/), Chapters 1 and 5: canonical ensembles and Ising models; four-spin enumeration supplied here. Inspection: canonical-ensemble exposition and Ising chapter scope inspected; finite chain independently enumerated.

<a id="ap-17"></a>
## AP-17 - Two clocks, one reunion, different elapsed times

Primary field: 83. Related: 53, 26. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why is elapsed proper time path dependent in spacetime, even between the same departure and reunion events?

**Anchor.** In flat 1+1 spacetime with c=1, an inertial timelike segment has proper duration √(Δt²−Δx²). Proper durations add along a piecewise inertial path. This Lorentzian rule differs from Euclidean path length.

**Bridge (exact-special-case).** Coordinate events and piecewise inertial worldlines are exact special-relativistic objects under the stated metric. Limits: The diagram is not a physical scale model; an instantaneous turnaround is an idealization. The activity does not solve Einstein’s gravitational field equations.

**Prerequisite gates.**

- **Entry:** V/A: plot time and position, interpret speed and use the given interval rule.
- **Explore:** F: calculate squares and square roots using 3–4–5 triangles.
- **Explain:** P: distinguish coordinate duration from each clock’s proper duration.
- **Prove:** A/P: compare piecewise constant-speed routes; D/I for arbitrary smooth paths.
- **Reading:** Symbolic interval rule and axis labels.
- **Arithmetic:** Squares of 3,4,5 and addition; units chosen so c=1.
- **Reasoning:** The vertical axis is time, not a second space direction. A geometrically longer drawing need not mean more clock time.
- **Hard Stop:** General curved spacetime requires a metric and differential geometry; rubber sheets are not a substitute.

**Materials and preparation (8 minutes).** Graph paper with vertical t-axis and horizontal x-axis, rulers, colored worldline segments, and two clock counters.

**Launch.** Both clocks leave event (t,x)=(0,0) and reunite at (10,0). Clock A stays at x=0. Clock B travels to (5,3), then returns to (10,0). For each straight segment add √(Δt²−Δx²) to that clock. Which clock records more time, and can a different legal turn point change the gap?

**Learner choices.** Choose turn positions with speed below 1, compare symmetric routes, and decide which features of the drawing affect each clock.

**Hour menu.** 0–10 explore legal and too-fast segments; 10–15 introduce the interval rule; 15–35 compute several reunion paths; 35–40 move markers along equal coordinate-time slices; 40–55 prove the symmetric comparison or vary reunion duration; 55–60 explain the result without Euclidean-length language.

**Explore.**

- Why must |Δx| be smaller than Δt for a massive clock segment?
- What changes if B turns around at x=0 instead?

**Hint ladder.**

1. Compute each leg separately; both B legs have Δt=5 and |Δx|=3.
2. Compare √(25−d²) with 5 for a symmetric excursion to distance d.

**Checked instance.** Calculate both proper times and prove every symmetric nonzero excursion with |d|<5 gives B less than 10.

**Reasoning.** A records √(100)=10. Each B leg records √(25−9)=4, for total 8. For a general symmetric excursion to d, total is 2√(25−d²), which is less than 10 whenever 0<|d|<5. Equality occurs at d=0. No numerical approximation is required for the worked route.

**Boundary.** At |d|=5 the legs are lightlike and proper duration is zero; that is not a possible worldline for the massive clock assumed here. At |d|>5 the square root is not real because the proposed segment is spacelike.

**Extensions.**

- Fix the excursion distance and change turnaround coordinate time; investigate why constant-speed segments maximize each leg’s proper time under its endpoints.
- With calculus, evaluate proper-time integrals on smooth subluminal curves and examine how an actual turnaround approximates the ideal diagram.

**Satisfying stop.** An exact 10-versus-8 comparison and a clear statement of the model’s causal constraint.

**Prior use.** No spacetime activity is documented. Ordinary shortest-path investigations do not cover the Lorentzian sign change or proper time.

**Sources.**

- [David Tong, General Relativity](https://davidtong.org/teaching/general-relativity/grhtml/S1), Section 1.2.1, particle in Minkowski spacetime; proper time equation (1.16). Inspection: author-hosted proper-time exposition inspected; finite piecewise inertial calculation independently checked.

<a id="ap-18"></a>
## AP-18 - Weigh an unseen center from its orbiters

Primary field: 85. Related: 70, 62. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can observable orbital motion reveal an unobserved mass, and how can inconsistent estimates expose a failed model?

**Anchor.** For a negligible-mass test particle in a circular Newtonian orbit around a dominant point mass, v²/r=GM/r², hence M=v²r/G. The inference relies on circularity, the true three-dimensional speed and radius, and the assumed force law.

**Bridge (exact-special-case).** Radius/speed data cards are exact observations of a specified circular-orbit model; learners perform a genuine inverse parameter inference. Limits: The supplied observations are invented and exact. Real astronomy requires projection, uncertainty and distributed-mass modeling.

**Prerequisite gates.**

- **Entry:** V/F/A: radius, speed, square and the supplied circular-balance formula.
- **Explore:** A: infer one common mass from several orbiters and test consistency.
- **Explain:** P: show a model predicts a specific speed-radius relation.
- **Prove:** D/V: derive centripetal acceleration and the Newtonian circular formula.
- **Reading:** A small data table and clearly labeled assumptions.
- **Arithmetic:** Small squares, products and square roots.
- **Reasoning:** Distinguish fitting a parameter under a model from proving the model is true.
- **Hard Stop:** Noncircular orbits, projected velocities and extended mass distributions require new equations; do not silently apply the point-mass formula.

**Materials and preparation (8 minutes).** Orbit-circle drawings at radii 1,4,9, colored orbit markers, and cards giving speeds 6,3,2 in units with G=1. Provide an alternative deliberately inconsistent data card.

**Launch.** An unseen object is orbited by three tiny test particles. Assume their orbits are circular, all motion is visible in the page, gravity is inverse-square, and the central object dominates. With G=1, infer its mass from radius/speed pairs (1,6),(4,3),(9,2). Then decide whether the new card (4,4) fits the same story.

**Learner choices.** Choose which observation to use first, predict an unmeasured speed, and propose reasons why inconsistent data might arise rather than forcing agreement.

**Hour menu.** 0–10 inspect orbit diagrams and what a measurement means; 10–15 state the force-balance model; 15–35 infer masses and predict missing data; 35–40 trace fast inner and slow outer orbits; 40–55 audit inconsistent or projected data; 55–60 distinguish conditional inference from discovery of a law.

**Explore.**

- Why does a slower outer particle not necessarily imply a smaller central mass?
- What information would you seek before blaming an inconsistent observation on arithmetic?

**Hint ladder.**

1. Compute v²r for each observation.
2. For a fixed inferred mass, solve v=√(M/r) to make a prediction.

**Checked instance.** Find the common central mass and test the extra data card.

**Reasoning.** The first three estimates are 6²×1=36,3²×4=36,2²×9=36. The new card gives 4²×4=64 and is incompatible with the same exact point-mass circular model. The predicted speed at r=16 is √(36/16)=3/2. The inconsistency identifies a failed joint set of assumptions or data, not which component failed.

**Boundary.** A measured projected speed can underestimate true speed. At a turning point of an eccentric orbit, v²r need not equal GM, despite the same inverse-square force.

**Extensions.**

- Use small intervals for observed radii and speeds to obtain a mass interval and test overlap between orbiters.
- Investigate flat galaxy rotation curves: under spherical symmetry, enclosed mass scales as v²r/G, but this is a changed distributed-mass model, not the original point mass.

**Satisfying stop.** An unseen parameter inferred three ways and an inconsistency recognized honestly.

**Prior use.** No astronomical inverse problem is documented. A drawing of ellipses alone would not preserve this inference mechanism.

**Sources.**

- [MIT, Astrophysics II lecture notes](https://ocw.mit.edu/courses/8-902-astrophysics-ii-fall-2023/mit8_902_f23_lec_full.pdf), PDF pp. 15–16: dynamical mass inference and virial assumptions; circular special case derived from force balance here. Inspection: virial and dynamical-inference exposition inspected; circular-orbit formula independently derived from stated force balance.

<a id="ap-19"></a>
## AP-19 - Can travel times reveal the water depth?

Primary field: 86. Related: 35, 65. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can wave travel times infer hidden geometry, and which assumptions make that inverse problem identifiable?

**Anchor.** Small-amplitude long gravity waves in nonrotating shallow water of constant depth H have speed c=√(gH). For one-dimensional travel through specified constant-depth segments, total ray travel time is the sum of segment length divided by local speed.

**Bridge (exact-special-case).** Travel-time equations are an exact inverse problem inside the stated piecewise homogeneous long-wave approximation. Limits: Interface reflections, rapidly varying-depth corrections, rotation and finite-amplitude effects are omitted. A real tsunami is not established by this two-segment calculation.

**Prerequisite gates.**

- **Entry:** V/F/A: distance, speed, time and square roots.
- **Explore:** A: infer one unknown depth from a measured total time.
- **Explain:** P: distinguish one unknown from two and show nonuniqueness by two witnesses.
- **Prove:** D: derive wave speed from the linear shallow-water equations; A suffices for the finite inverse calculation.
- **Reading:** A labeled cross-section and three numerical data cards.
- **Arithmetic:** Small divisions, squares and fractions.
- **Reasoning:** Wave propagation is not the same as the journey of a particular water parcel; keep model and observation separate.
- **Hard Stop:** Continuous bathymetric inversion and real seismic/tidal data require more wave physics and uncertainty modeling.

**Materials and preparation (7 minutes).** A two-segment channel sketch, two movable depth labels, travel-time strips and a calculator optional. Use units with g=1 explicitly; no real water is needed.

**Launch.** A long, small wave crosses two 6-unit segments. In this ideal model its speed in depth H is √H. The first segment has depth 4. The total travel time is 5. Infer the second depth. Then hide both depths: does the same total time still determine them?

**Learner choices.** Choose candidate depths, decide which extra measurement would resolve ambiguity, and compare forward prediction with inverse reconstruction.

**Hour menu.** 0–10 explore speed-versus-depth cards; 10–15 state long-wave and piecewise-depth assumptions; 15–35 infer and check the hidden depth; 35–40 move wave markers using travel-time strips; 40–55 construct two indistinguishable depth pairs; 55–60 explain what the data determine.

**Explore.**

- Why can deeper water produce faster wave travel in this model?
- How would measuring the arrival time at the interface change the inverse problem?

**Hint ladder.**

1. The known first segment takes 6/√4 time units.
2. Subtract that time before solving for the remaining speed; square only after finding speed.

**Checked instance.** Recover the second depth, then exhibit nonuniqueness when both depths are unknown.

**Reasoning.** The first time is 3, leaving 2 for the second segment. Thus its speed is 6/2=3 and its depth is 9. If both depths are unknown, (H1,H2)=(4,9) and (9,4) both give total time 5. A genuinely different pair is (144/25,144/25): each speed is 12/5 and each time 5/2, again total 5.

**Boundary.** A total time of 3 or less is impossible with first depth 4 and a finite positive second depth: the first segment alone takes 3 and the second adds a positive time.

**Extensions.**

- Measure one intermediate arrival time and show how both depths become individually recoverable.
- From ηt+H ux=0 and ut+gηx=0 derive ηtt=gHηxx, then verify traveling waves f(x−ct) with c²=gH.

**Satisfying stop.** A hidden depth found and a clear counterexample to overinterpreting one measurement.

**Prior use.** No geophysical inverse-data family is documented. Ordinary path-length problems omit the depth-dependent wave model and identifiability issue.

**Sources.**

- [Geoffrey Vallis, Atmospheric and Oceanic Fluid Dynamics](https://empslocal.ex.ac.uk/people/staff/gv219/aofd/aofd2_r2.pdf), Section 7.1, equations (7.18)–(7.23), PDF pp. 75–76: shallow-water limit and parcel motion. Inspection: relevant exposition or named scope inspected; finite calculation self-contained below.

<a id="ap-20"></a>
## AP-20 - A price certificate for the best factory plan

Primary field: 90. Related: 15, 05. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can a proposed optimum be certified without examining every feasible allocation?

**Anchor.** A nonnegative resource-price vector whose priced ingredients cover every product’s sale value gives an upper bound on the revenue of every feasible production plan. Equality between such a bound and a feasible plan proves optimality by weak duality.

**Bridge (exact-special-case).** Products, resource inequalities and price certificates constitute a genuine finite linear/integer optimization problem and its dual bound. Limits: One integral optimum does not imply all linear programs have integral optima; general duality requires separate hypotheses.

**Prerequisite gates.**

- **Entry:** O/C: make two kinds of bundles from limited colored counters.
- **Explore:** C: enumerate integer plans and total revenue.
- **Explain:** F/P: assign fractional resource prices and show a universal bound.
- **Prove:** A: multiply resource inequalities by nonnegative prices and add them.
- **Reading:** Two recipe cards and values; oral description and physical bundles work.
- **Arithmetic:** Small counts initially; thirds for the sharp certificate.
- **Reasoning:** Distinguish finding a good plan from ruling out every better plan.
- **Hard Stop:** General linear-programming duality, existence and algorithms require algebraic/convex prerequisites; this finite certificate is complete without them.

**Materials and preparation (8 minutes).** Five red counters, four blue counters, product recipe cards A=(2 red,1 blue), B=(1 red,2 blue), and revenue labels 3 and 4. Include blank resource-price tags.

**Launch.** Make products without reusing ingredients. A sells for 3 and uses two red plus one blue; B sells for 4 and uses one red plus two blue. You have five red and four blue. Find the most revenue, then price the raw ingredients so your total ingredient budget proves nobody can earn more.

**Learner choices.** Choose product mixes, organize feasible cases, propose resource prices, and improve a loose upper bound until it matches a plan.

**Hour menu.** 0–10 build and undo bundles; 10–15 establish resource and sale rules; 15–35 search for good production plans; 35–40 exchange builder and auditor roles; 40–55 invent a price certificate with fractions or a scaled integer version; 55–60 present plan and matching bound.

**Explore.**

- Why does giving every raw ingredient price 1 fail to cover product B’s sale price?
- What makes a resource-price argument apply even to plans we never listed?

**Hint ladder.**

1. Find prices r,b with 2r+b at least 3 and r+2b at least 4.
2. Try making both equalities hold; alternatively multiply all money values by 3.

**Checked instance.** Prove the maximum revenue is 10 for five red and four blue counters.

**Reasoning.** Two A and one B use five red and four blue and earn 10. Prices r=2/3,b=5/3 make A’s ingredients worth 3 and B’s worth 4. All available ingredients are worth 5(2/3)+4(5/3)=10. Since no product sells above its ingredient value, every feasible plan earns at most 10. Equality proves optimality, even if fractional production were allowed.

**Boundary.** With four red and four blue, fractional A=B=4/3 earns 28/3, whereas the best integer plan is two B, earning 8. A fractional bound need not be attained by whole products.

**Extensions.**

- Scale all prices by three so the certificate uses integers 2 and 5 against product values 9 and 12.
- Change resource supplies and identify when the same price certificate remains sharp; this introduces sensitivity and complementary slackness.

**Satisfying stop.** A best plan accompanied by a short universal certificate, not only a search record.

**Prior use.** Existing tiling packets use upper bounds for packing. This connects the bounding habit to resource prices and linear optimization with a distinct feasible set.

**Sources.**

- [Stephen Boyd and Lieven Vandenberghe, Convex Optimization](https://www.seas.ucla.edu/~vandenbe/cvxbook/bv_cvxbook.pdf), Chapter 5: weak duality; finite resource certificate verified algebraically here. Inspection: relevant exposition or named scope inspected; finite calculation self-contained below.

<a id="ap-21"></a>
## AP-21 - Spend the battery now, or save it?

Primary field: 90. Related: 68, 93. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why can looking backward through a state space beat choosing the best immediate reward?

**Anchor.** For a finite deterministic horizon with state (day, remaining energy), the optimal value obeys Bellman’s recurrence: compare the reward plus optimal value of the resulting state for every legal action. The state must retain all information relevant to future feasibility and reward.

**Bridge (exact-special-case).** A two-unit battery, dated offers and accept/skip actions form an exact finite-horizon resource-allocation problem. Limits: Future offers are known here. Unknown or random future offers require an explicit information model and possibly different policies.

**Prerequisite gates.**

- **Entry:** O/C: spend energy tokens once, collect score counters and follow three dates.
- **Explore:** C: list legal plans and compare their scores.
- **Explain:** P: justify why optimal remaining decisions depend only on day and energy.
- **Prove:** P: backward induction over the number of remaining days.
- **Reading:** Three short offer cards; pictures can replace text.
- **Arithmetic:** Small whole-number subtraction and addition.
- **Reasoning:** An immediate attractive action may remove a more valuable future choice; the record must keep remaining energy.
- **Hard Stop:** Continuous optimal control and stochastic decision theory are continuations, not claims proved by the three-day table.

**Materials and preparation (8 minutes).** Two energy tokens, three ordered offer cards: day 1 costs 2 and pays 5; day 2 costs 1 and pays 4; day 3 costs 1 and pays 4. Prepare a 3×3 day/energy grid.

**Launch.** Start with two energy tokens and no recharge. On each day you may accept that day’s offer once if you can pay its energy cost, or skip it. Tomorrow’s offers are already visible. Find the best plan, then make a table that gives the best decision from every day and remaining-energy state.

**Learner choices.** Choose a plan, create a counterexample to a greedy rule, and decide how to organize reusable information rather than rechecking every complete story.

**Hour menu.** 0–10 act out possible spending plans; 10–15 agree on one-time offers and no recharge; 15–35 enumerate or build a decision tree; 35–40 swap planner and battery-keeper roles; 40–55 compress the tree into a backward table; 55–60 explain why a tempting first choice fails.

**Explore.**

- Why can the highest-value single offer be part of a worse overall plan?
- Which details of the earlier days matter after the remaining energy is known?

**Hint ladder.**

1. Begin on the last day, when there is no later consequence.
2. At each state compare skip with take plus the best value already recorded for the next day.

**Checked instance.** Find the optimal score and the backward values for energy 0,1,2.

**Reasoning.** On day 3, values are 0,4,4. Before day 2, values are 0,4,8: with two tokens take both remaining offers. Before day 1, values are 0,4,8; with two tokens, taking day 1 gives 5 while skipping gives 8. Thus skip day 1 and take days 2 and 3. Enumerating feasible subsets gives {},{1},{2},{3},{2,3}, with scores 0,5,4,4,8, confirming the table.

**Boundary.** If energy recharges by one unit overnight, the state transitions change and taking day 1 can become optimal. The old table must not be reused unchanged.

**Extensions.**

- Add a fourth dated offer and update the same state table.
- Introduce a random future offer with a stated distribution and compare a precommitted plan with a policy reacting to the observed offer.

**Satisfying stop.** A greedy counterexample and a complete optimal-decision table.

**Prior use.** Subtraction games use backward winning-state analysis. Here the payoff is accumulated reward under resource constraints, with optimization rather than alternating adversarial turns.

**Sources.**

- [Jeffrey Chasnov, Mathematical Biology](https://www.math.hkust.edu.hk/~machas/mathematical-biology.pdf), Chapter 7.3: dynamic programming located; this finite resource recurrence is self-contained. Inspection: dynamic-programming chapter located in authored contents; this finite decision recurrence has a complete independent proof.

<a id="ap-22"></a>
## AP-22 - How should you hide an unequal choice?

Primary field: 91. Related: 60, 90. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can randomization protect a player against an opponent who knows the strategy but not its realized action?

**Anchor.** A two-player zero-sum matrix game allows each player to choose a distribution independently and privately. For payoff matrix [[2,0],[0,1]], maximizing the guaranteed expected row payoff gives a mixed minimax equilibrium with value 2/3.

**Bridge (exact-special-case).** Simultaneous hidden action cards and score transfers realize the specified strategic-form game exactly. Limits: Observed short-run winnings need not equal expectation. Real people need not play equilibrium, and visible random draws change the information structure.

**Prerequisite gates.**

- **Entry:** O/C: choose cards secretly and score the four outcomes.
- **Explore:** F: compare long-run averages and design a three-card randomizer.
- **Explain:** A: calculate payoff against each opposing pure choice.
- **Prove:** F/P: show one strategy guarantees a lower bound and the other caps every strategy at the same value.
- **Reading:** A two-by-two score table; colors can replace U,D,L,R.
- **Arithmetic:** Thirds and multiplication by two; no money or betting required.
- **Reasoning:** Keep the chosen distribution public but the realized action private; players have opposite objectives.
- **Hard Stop:** General finite-game equilibrium existence uses more machinery; the exact two-by-two certificate suffices here.

**Materials and preparation (10 minutes).** Row cards U,D and column cards L,R, score counters, and two three-card draw packs. Row payoff is 2 for U/L, 1 for D/R, and 0 otherwise; column minimizes that score.

**Launch.** Choose your action simultaneously and reveal together. The row player wants a high score; the column player wants a low score. Everyone knows the payoff table. Can the row player guarantee a positive average even against an opponent who knows the row player’s randomization rule?

**Learner choices.** Choose mixtures, test predictable play, build a private randomizer, and seek a strategy whose guarantee does not depend on the opponent’s choice.

**Hour menu.** 0–10 play several rounds; 10–15 clarify simultaneous secrecy and opposite goals; 15–35 compare pure play and mixtures; 35–40 exchange roles; 40–55 derive matching lower and upper bounds; 55–60 explain why the mixture is unequal.

**Explore.**

- Why is choosing U and D equally often not necessarily best?
- What could the opponent do if it saw your realized action before choosing?

**Hint ladder.**

1. If U is chosen with probability p, payoffs against L and R are 2p and 1−p.
2. Make those two threats equal, then find a column mixture giving the same payoff to U and D.

**Checked instance.** Find both optimal mixtures and certify the game value.

**Reasoning.** Set 2p=1−p, giving p=1/3 and guarantee 2/3. If column chooses L with q=1/3, pure U earns 2q=2/3 and pure D earns 1−q=2/3. Therefore every row mixture earns exactly 2/3 against that column strategy, proving no larger guarantee is possible. The two matching bounds certify the equilibrium.

**Boundary.** If column sees the row action first, it chooses R after U and L after D, forcing payoff zero. The guarantee depends on simultaneous hidden realization.

**Extensions.**

- Change the diagonal rewards to positive a,b and derive row U probability b/(a+b) and value ab/(a+b).
- Contrast expected guarantee with every-round guarantee: the latter remains zero in this game.

**Satisfying stop.** Two three-card randomizers with a complete minimax certificate.

**Prior use.** Weeks 7–8 cover perfect-information combinatorial games. Simultaneous mixed strategies are a different branch and use a different notion of solution.

**Sources.**

- [Giacomo Bonanno, Game Theory](https://arxiv.org/pdf/1512.06808), Sections 5.2–5.3: mixed strategies, indifference and best replies. Inspection: mixed-strategy exposition inspected; this matrix solved independently.

<a id="ap-23"></a>
## AP-23 - A stable traffic pattern that costs more

Primary field: 91. Related: 90. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why can individually stable choices fail to minimize total cost?

**Anchor.** A pure Nash equilibrium has no strictly profitable unilateral deviation. In a finite congestion game, a player’s route cost depends on how many use it; equilibrium and social optimum are distinct conditions.

**Bridge (exact-special-case).** Three route-choice counters are literal players in an explicitly specified congestion game. Limits: This is a mathematical cost model, not a prediction of actual children’s traffic choices or a recommendation for a real transport policy.

**Prerequisite gates.**

- **Entry:** O/C: place one token per player on a route and count users.
- **Explore:** C: compute each player’s cost and total cost.
- **Explain:** P: test every kind of unilateral switch, including the cost change caused by joining.
- **Prove:** P: enumerate the four possible route occupancies.
- **Reading:** Two route cost labels; oral rules sufficient.
- **Arithmetic:** Counts to three and totals to nine.
- **Reasoning:** A switch changes the destination route’s crowding. Equal cost is not a strictly profitable deviation.
- **Hard Stop:** General equilibrium existence and price-of-anarchy bounds require additional game-theoretic definitions and proofs.

**Materials and preparation (5 minutes).** Three distinct player counters, route A labeled “cost equals number using A,” and route B labeled “cost always 2.” Provide a table for A-occupancies 0,1,2,3.

**Launch.** Three travelers choose A or B. Everyone on A pays the number of travelers on A; everyone on B pays 2. A configuration is stable if no single traveler can switch and strictly lower their own cost. Find every stable occupancy and compare total costs.

**Learner choices.** Choose configurations, act as a player searching for improvement, propose coordinated changes, and distinguish fairness from total efficiency.

**Hour menu.** 0–10 explore costs by moving counters; 10–15 define unilateral and strictly lower; 15–35 classify the four occupancies; 35–40 become three travelers and rehearse switches; 40–55 compare stable states with a planner’s optimum; 55–60 explain one surprising stable pattern.

**Explore.**

- Why can a B traveler not simply use the cost A had before they joined it?
- Can a stable pattern still have a cheaper alternative arrangement?

**Hint ladder.**

1. Record each current cost and then recompute the destination cost after one token moves.
2. Compare total costs separately from individual improvement tests.

**Checked instance.** Find Nash occupancies and the social optimum.

**Reasoning.** Let n be the number on A. Total costs for n=0,1,2,3 are 6,5,6,9. At n=0 a traveler improves from 2 to 1 by joining A. At n=3 a traveler improves from 3 to 2 by switching to B. At n=1, a B traveler joining A would pay 2, unchanged, and the A traveler would worsen from 1 to 2: stable. At n=2, an A traveler moving to B stays at 2, while the B traveler joining A would pay 3: also stable. The social optimum is n=1 with total 5; n=2 is a costlier equilibrium.

**Boundary.** If ties also trigger moves, stability is a different notion. Two A travelers may be indifferent to a move even though that move improves total cost.

**Extensions.**

- Change B’s constant cost to 3/2 and recompute equilibria and total optimum with fractions.
- Explore a small toll or coordination rule, stating whose objective it serves; no policy is universally best without an objective.

**Satisfying stop.** A complete table separating stable behavior from globally efficient behavior.

**Prior use.** No congestion-game task is documented. The existing route packets ask how to traverse edges, not how route users create strategic costs.

**Sources.**

- [Giacomo Bonanno, Game Theory](https://arxiv.org/pdf/1512.06808), Section 1.6: Nash equilibrium; finite congestion instance checked directly. Inspection: named source scope inspected; displayed finite result proved directly here.

<a id="ap-24"></a>
## AP-24 - A neutral population can lose a color

Primary field: 92. Related: 60. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why can random inheritance drive fixation even when the expected allele fraction remains unchanged?

**Anchor.** A neutral finite Wright–Fisher generation of size N samples N offspring independently with replacement from the current generation’s allele frequencies. Conditional expected next frequency equals current frequency, while absorbing all-one-color states remain possible.

**Bridge (exact-special-case).** Parent-color draws with replacement implement a genuine finite neutral allele-frequency model. Limits: This is a highly simplified haploid population with fixed size, no mutation and no selection. It is not a model of individual human traits.

**Prerequisite gates.**

- **Entry:** O/C: draw, replace, and record a parent color for each offspring.
- **Explore:** F: compare probabilities for two independent draws and repeat generations.
- **Explain:** P: distinguish an unchanged expectation from an unchanged realized population.
- **Prove:** F/A: derive transition probabilities and eventual absorption for the two-individual case.
- **Reading:** Color-only generation rows; spoken rules suffice.
- **Arithmetic:** Halves and quarters; optional powers for survival probability.
- **Reasoning:** The new generation replaces the old only after both offspring have been drawn; no within-generation updating.
- **Hard Stop:** Selection, diploidy, mutation and real demographic inference require changed models and biological assumptions.

**Materials and preparation (5 minutes).** Two parent counters, one red and one blue, an opaque draw cup, and a row of generation boxes. Use colored pencils to record offspring while replacing every parent draw.

**Launch.** Make a new generation of exactly two counters. For each offspring, draw a parent color uniformly from the current two, record that color, and replace the parent before drawing again. After both offspring are recorded, they become the new parents. Can a neutral rule eventually erase a color?

**Learner choices.** Choose how to record generations, compare several independent populations, and design a changed rule that would prevent or reverse loss.

**Hour menu.** 0–10 practice drawing with replacement; 10–15 establish simultaneous generation replacement; 15–35 run independent lineages; 35–40 exchange sampler and recorder roles; 40–55 enumerate one-generation outcomes and explain absorption; 55–60 compare expected counts with observed endpoints.

**Explore.**

- Why can both colors be equally successful in expectation while one disappears in a run?
- Once a color is gone, can this particular model recover it?

**Hint ladder.**

1. From one red and one blue, list RR,RB,BR,BB as distinct ordered offspring outcomes.
2. Only the two mixed outcomes keep both colors alive for another generation.

**Checked instance.** Starting from one red and one blue, find one-step probabilities and eventual fixation probabilities.

**Reasoning.** RR,RB,BR,BB each have probability 1/4. Red counts 2,1,0 therefore have probabilities 1/4,1/2,1/4 and expected count 1. The mixed state survives k generations with probability (1/2)^k, tending to zero. Symmetry gives eventual all-red and all-blue probabilities 1/2 each. Once all red or all blue, every parent draw has that color, so these states are absorbing.

**Boundary.** Drawing without replacement would preserve one red and one blue forever for N=2. That small rule change removes the drift in this example.

**Extensions.**

- Increase population size and compare time to loss; derive the binomial one-step distribution with fraction p.
- Add a specified small mutation chance after each draw and observe that formerly absorbing states no longer remain absorbing.

**Satisfying stop.** An exact explanation of random loss under a neutral rule.

**Prior use.** Year-1 probability examples do not document this generational sampling process. Record population size and rule version to distinguish future variants.

**Sources.**

- [Jeffrey Chasnov, Mathematical Biology](https://www.math.hkust.edu.hk/~machas/mathematical-biology.pdf), Section 5.5: random genetic drift; N=2 transition calculation provided below. Inspection: named source scope inspected; displayed finite result proved directly here.

<a id="ap-25"></a>
## AP-25 - What can never change in the reaction box?

Primary field: 92. Related: 15, 80. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How do stoichiometric constraints produce conserved quantities independently of reaction rates?

**Anchor.** For reaction A+2B ↔ C, a forward firing changes counts by (−1,−2,+1) and a backward firing reverses it. Linear quantities w·n are conserved exactly when w is orthogonal to that change vector; rates determine timing but not these conservation laws.

**Bridge (exact-special-case).** Colored molecule counters and legal reaction firings are the exact discrete stoichiometric state system for the stated reversible reaction. Limits: Tokens are hypothetical species; legal reachability does not determine real reaction speed, energy, equilibrium or chemical feasibility.

**Prerequisite gates.**

- **Entry:** O/C: exchange one A and two B for one C, or reverse it.
- **Explore:** C: record reachable count triples without creating negative counts.
- **Explain:** M/P: discover weighted totals unchanged by each exchange.
- **Prove:** A/L: solve w·(−1,−2,1)=0 and use invariance under sequences of moves.
- **Reading:** Three symbols or colors with a pictorial recipe; oral rules work.
- **Arithmetic:** Counts and doubling; optional linear equations.
- **Reasoning:** The total number of tokens is not conserved; different quantities may be conserved simultaneously.
- **Hard Stop:** Mass-action differential equations add rates and continuous concentration assumptions; do not infer them from token reachability alone.

**Materials and preparation (7 minutes).** A counters, B counters and distinct C counters, a forward/backward recipe mat, and count-triple records. Begin with 3 A and 4 B and no C.

**Launch.** A legal forward reaction trades exactly one A and two B for one C. A reverse reaction trades one C for one A and two B. Start with (A,B,C)=(3,4,0). Find every reachable collection. What totals stay fixed even though the number of counters changes?

**Learner choices.** Choose reaction sequences, invent a conserved counting method, propose impossible target states, and decide whether a certificate rules them out.

**Hour menu.** 0–10 practice both reactions freely; 10–15 establish nonnegative whole counts; 15–35 map reachable states and test targets; 35–40 partners act as molecule trades; 40–55 derive weighted invariants or add a second reaction; 55–60 explain an impossibility.

**Explore.**

- Why does simply counting all tokens fail as an invariant?
- Are invariant equations alone always enough to prove reachability in an arbitrary reaction network?

**Hint ladder.**

1. Imagine each C as a sealed packet containing the A and B used to make it.
2. Count A+C and B+2C separately.

**Checked instance.** List every reachable state and decide whether (0,0,3) can be reached.

**Reasoning.** A+C=3 and B+2C=4 stay fixed. Writing C=c gives A=3−c and B=4−2c. Nonnegative integer counts force c=0,1,2, yielding (3,4,0),(2,2,1),(1,0,2). Each is reached by zero, one or two forward reactions. Target (0,0,3) violates B+2C=4 since its value is 6, so it is impossible. Total molecule count falls by two per forward firing, demonstrating why the unweighted total fails.

**Boundary.** For a larger network, nonnegative invariant-compatible counts need not be reachable; modular obstructions or missing reactants needed to enable a move may prevent reachability. Here sufficiency was proved by an explicit sequence.

**Extensions.**

- Add A↔B and determine which conserved totals survive both reaction vectors.
- Assign positive forward and backward rates and compare dynamical equilibrium with stoichiometric reachability; conservation alone cannot locate the equilibrium.

**Satisfying stop.** A complete reaction-state list and two visible conservation laws.

**Prior use.** Weeks 2 and 4 use invariants for toggles and remainders. This is a distinct chemical-stoichiometry instance with changing molecule count and several simultaneous conservation laws.

**Sources.**

- [Jeffrey Chasnov, Mathematical Biology](https://www.math.hkust.edu.hk/~machas/mathematical-biology.pdf), Section 6.1: law of mass action; conservation proof is explicit for this network. Inspection: named source scope inspected; displayed finite result proved directly here.

<a id="ap-26"></a>
## AP-26 - The controller is correcting yesterday’s error

Primary field: 93. Related: 37. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** Why can delayed feedback destabilize a correction rule that works perfectly with current information?

**Anchor.** The discrete plant is x[n+1]=x[n]+u[n]. Current feedback u[n]=−x[n] sets the next state to zero. One-step delayed feedback u[n]=−x[n−1] instead creates a second-order recurrence whose behavior depends on the stored previous state.

**Bridge (exact-special-case).** Position, correction input and a one-step-old sensor report are exactly the state, control and observation of a discrete feedback system. Limits: This is not Euler’s approximation to a cooling ODE. Its clocked update and communication delay are the model itself.

**Prerequisite gates.**

- **Entry:** F/C: signed positions and one-step memory represented by two cards.
- **Explore:** F: apply full or half correction and plot a sequence.
- **Explain:** P: identify a repeating pair of states, not merely a repeated single reading.
- **Prove:** A: manipulate the two-step recurrence to prove periodicity or decay.
- **Reading:** Current, previous and correction labels; spoken role instructions support participation.
- **Arithmetic:** Signed addition, halves and quarters.
- **Reasoning:** Separate the current position from the sensor’s delayed report; update both cards in the correct order.
- **Hard Stop:** General delay-system stability and frequency-domain design require further control theory; the exact recurrence suffices.

**Materials and preparation (7 minutes).** A signed number line, two state cards labeled previous/current, correction arrows, and a two-person controller/plant station. Start both state cards at 1.

**Launch.** The plant adds your correction to its current position once each tick. Your sensor reports the previous tick’s position. Begin with previous=current=1. First always negate the reported number. Does the position settle at zero? Then try correcting only half the reported error.

**Learner choices.** Choose full or half correction, test a different initial state pair, and decide what information is necessary to predict the future.

**Hour menu.** 0–10 move positions with chosen corrections; 10–15 establish the delayed-report order; 15–35 compare full and half feedback; 35–40 exchange controller and plant roles; 40–55 prove the repeating pair or four-step shrink rule; 55–60 explain why strong correction need not be better.

**Explore.**

- Why is seeing a zero position once not enough to show the system has settled?
- What changes when the controller sees the current state instead?

**Hint ladder.**

1. Keep a two-column record of (previous,current).
2. A deterministic repeated pair makes every future pair repeat; for half correction, compare entries four steps apart.

**Checked instance.** Analyze full and half delayed correction from x[−1]=x[0]=1.

**Reasoning.** Full correction gives x[1..6]=0,−1,−1,0,1,1, returning the pair to (1,1): a six-step cycle. Current full correction would instead reach zero in one tick and stay there. Half delayed correction gives 1,1/2,0,−1/4,−1/4,−1/8,0,1/16,... from x[0]. Algebra from x[n+1]=x[n]−x[n−1]/2 yields x[n+4]=−x[n]/4, so every four-step subsequence decays to zero.

**Boundary.** A single repeated position does not prove a cycle: its preceding state might differ. The complete state is the ordered previous/current pair.

**Extensions.**

- Test other gains k in x[n+1]=x[n]−k x[n−1] and study characteristic roots with algebra.
- Add bounded disturbances and compare perfect nominal convergence with robustness; a new disturbance rule must be specified.

**Satisfying stop.** A proved delay-induced cycle and a weaker correction that converges.

**Prior use.** AP-07 also studies recurrence stability, but there the update approximates an ODE. Here delayed information changes the exact closed-loop state dimension; record the shared proof mechanism.

**Sources.**

- [Åström and Murray, Feedback Systems](https://www.fbswiki.org/wiki/index.php/State_Feedback), Chapter 7: state feedback; delay example is a self-contained discrete system. Inspection: relevant source framework inspected; finite example explicitly proved below.

<a id="ap-27"></a>
## AP-27 - Can one sensor see two hidden tanks?

Primary field: 93. Related: 15, 62. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** When do output observations determine a system’s hidden initial state, and when can infinitely many observations remain insufficient?

**Anchor.** For x[n+1]=Ax[n] and y[n]=Cx[n], two states are observationally indistinguishable if C A^n times their difference vanishes for every observed n. Distinct decay rates can make two total-output readings identify two initial components.

**Bridge (exact-special-case).** Hidden component amounts, linear updates and a sum-only sensor are a literal finite-dimensional linear observation system. Limits: Exact noiseless identification does not imply stable inference from noisy measurements. Physical tank drainage need not follow these fractional updates.

**Prerequisite gates.**

- **Entry:** O/C/F: hide two amounts and read only their total.
- **Explore:** F: halve or quarter the amounts each step.
- **Explain:** P: produce two distinct states with the same entire reading history.
- **Prove:** A/L: solve two linear equations or find an unobservable difference vector.
- **Reading:** Two update arrows and sensor labels; diagram-first explanation possible.
- **Arithmetic:** Halves and quarters, signed linear combinations.
- **Reasoning:** The visible total is not the full state; avoid assuming an unknown split is equal.
- **Hard Stop:** Kalman filtering requires a noise model and probabilistic estimation; it is not established by this exact reconstruction.

**Materials and preparation (8 minutes).** Two covered amount cards representing tanks, one total-readout card, and an update table. Use counters for integer starting values and fraction strips after decay.

**Launch.** A sensor reports only the sum of two hidden amounts. First both amounts halve each tick. Can any number of total readings reveal the original split? Now let the first halve and the second quarter each tick. Readings are 8 initially and 3 one tick later. Find the original amounts.

**Learner choices.** Choose indistinguishable hidden states, decide what extra sensor or changed dynamics would help, and test the reconstruction with a partner’s secret split.

**Hour menu.** 0–10 hide and guess two-counter splits; 10–15 fix the sensor and update rules; 15–35 compare histories under identical decay; 35–40 exchange hidden-state and observer roles; 40–55 reconstruct under distinct decay or inspect near-equal rates; 55–60 state an observability conclusion.

**Explore.**

- Why does collecting the same kind of information many times sometimes add nothing?
- How can changing the dynamics make one sensor sufficient?

**Hint ladder.**

1. For identical decay, express every future total as the original total times a power of 1/2.
2. For different decay, write a+b=8 and a/2+b/4=3.

**Checked instance.** Give indistinguishable states in the first model and solve the second model’s two readings.

**Reasoning.** Under identical halving, states (2,6) and (4,4) both produce totals 8,4,2,1,..., so no number of those readings distinguishes them. Under rates 1/2 and 1/4, equations a+b=8 and 2a+b=12 give a=b=4. In general a=4y1−y0 and b=2y0−4y1. Substitution recovers both measured totals.

**Boundary.** If the second decay factor is changed back to 1/2, the two equations become dependent. If rates are merely very close, exact uniqueness can coexist with high sensitivity to measurement error.

**Extensions.**

- Add a sensor reading the difference; one simultaneous sum and difference then identifies both components without waiting.
- Build the two-row observability matrix and investigate its rank and conditioning as the decay rates approach equality.

**Satisfying stop.** A proof of permanent ambiguity and a contrasting exact reconstruction.

**Prior use.** Week 6 asks optimal queries about codes. Here the measurements arise from evolving hidden state and fixed sensor design; this is a substantive systems-theory connection.

**Sources.**

- [Åström and Murray, Feedback Systems](https://www.fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers), Chapter 8: observability and state estimation; two-state examples derived below. Inspection: observability chapter scope inspected; both finite linear systems solved and checked directly.

<a id="ap-28"></a>
## AP-28 - Four messages that survive one damaged bit

Primary field: 94. Related: 05, 68. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How much redundancy is required to correct an adversarial error, and how can geometry in a discrete space certify a limit?

**Anchor.** Binary words of minimum Hamming distance at least three have disjoint radius-one Hamming balls and uniquely correct any one-bit error by nearest-codeword decoding. Four messages require at least five bits for that guarantee.

**Bridge (exact-special-case).** Bit strips, adversarial single flips and nearest-codeword decoding are exact finite error-correcting communication. Limits: This finite worst-case guarantee is distinct from Shannon’s asymptotic probabilistic channel theorem and from secret encryption.

**Prerequisite gates.**

- **Entry:** O/C: copy black/white patterns and flip at most one tile.
- **Explore:** C/P: count disagreements and compare candidate codewords.
- **Explain:** P: show a received word cannot be within one flip of two codewords distance three apart.
- **Prove:** M/P: count disjoint radius-one balls to rule out four-bit codes.
- **Reading:** Color patterns only; rule can be spoken.
- **Arithmetic:** Counts to five and powers of two up to 32.
- **Reasoning:** The error position is unknown; the guarantee must cover every single flip, not just errors tried experimentally.
- **Hard Stop:** Asymptotic capacity, optimal code families and decoding complexity are later questions; the finite code is complete.

**Materials and preparation (10 minutes).** Five-position black/white strips, four message symbols and codewords 00000,11100,10011,01111. Give an independent partner the role of flipping zero or one bit.

**Launch.** Send one of four messages using a five-bit strip. Your partner may secretly flip at most one bit. Design a decoding rule that always recovers the original. Then investigate whether four bits could ever give the same guarantee, even with a different code.

**Learner choices.** Choose a message, choose a damaging position as adversary, organize all received patterns, and seek either a shorter construction or an impossibility proof.

**Hour menu.** 0–10 practice damage and recovery; 10–15 state the at-most-one-flip rule; 15–35 test and audit the four codewords; 35–40 exchange sender/noise/decoder roles; 40–55 count neighborhoods to attack four-bit coding; 55–60 show a recovery and its universal justification.

**Explore.**

- Why must two message patterns differ in at least three places?
- How many distinct received patterns can one four-bit message produce with at most one flip?

**Hint ladder.**

1. If a received word is one flip from both originals, the originals are at most two flips apart.
2. A four-bit message has one unchanged pattern and four one-flip patterns; those five-pattern sets must be disjoint.

**Checked instance.** Decode received word 10111 and prove four-bit coding is impossible for four messages.

**Reasoning.** 10111 differs from 10011 only at the third bit, so it decodes to that codeword. The six pairwise distances of the supplied code are 3,3,4,4,3,3, hence the guarantee holds. For four-bit words, each radius-one ball contains 5 patterns. Four messages would require 20 distinct received patterns, but only 2^4=16 exist. Any shorter code could be padded with fixed zeros to length four without decreasing pairwise distance, so ruling out length four rules out every shorter length. Therefore four bits cannot suffice; the displayed five-bit code attains the minimum.

**Boundary.** Two flipped bits can mislead nearest decoding. From 00000, flipping the first two gives 11000, which lies one bit from 11100.

**Extensions.**

- Separate detection from correction: distance two detects any single flip but need not identify the original.
- Compare a threefold repetition code with the five-bit construction, then explore Hamming codes after linear algebra over two-element arithmetic.

**Satisfying stop.** A working optimal-length code with both a correction proof and a lower bound.

**Prior use.** Week 6 uses optimal code queries. This adds channel damage, Hamming distance and sphere-packing rather than duplicating the existing guessing questions.

**Sources.**

- [Claude Shannon, A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf), Part II: noisy communication framework; finite distance and sphere-packing proofs given here. Inspection: relevant source framework inspected; finite example explicitly proved below.

<a id="ap-29"></a>
## AP-29 - Give the common message a shorter name

Primary field: 94. Related: 05, 60. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How can unequal frequencies be converted into shorter unambiguous communication?

**Anchor.** A binary prefix code represents messages by leaves of a binary tree, preventing a codeword from prefixing another. For positive message weights, an optimal tree has no unary internal node, and shorter leaves should receive larger weights by an exchange argument.

**Bridge (exact-special-case).** Messages, binary strings and weighted bit totals are exact finite lossless source coding. Limits: The known message frequencies and prefix condition are part of the model. This does not prove general entropy bounds or all properties of non-prefix uniquely decodable codes.

**Prerequisite gates.**

- **Entry:** O/C: follow left/right branches and associate leaves with pictures.
- **Explore:** M: count total bits for a specified collection of messages.
- **Explain:** P: explain immediate greedy decoding in a prefix tree and why a prefix violation can make greedy stopping fail. A non-prefix code may still be uniquely decodable by another method.
- **Prove:** P: classify full binary trees with four leaves and use a label-swap argument.
- **Reading:** Four picture symbols and binary digits; a spoken “left/right” alternative works.
- **Arithmetic:** Weighted counts up to 16; division by eight optional.
- **Reasoning:** A codeword ends at a leaf. Preserve boundaries without secretly inserting separators for free.
- **Hard Stop:** Entropy bounds require logarithms and probability; optimality among unrestricted uniquely decodable codes needs an additional theorem.

**Materials and preparation (8 minutes).** Eight message tokens: four A, two B, one C, one D; binary-tree mats and movable leaf labels. Provide code strips but no free spaces or punctuation between words.

**Launch.** Our eight messages contain A four times, B twice, and C and D once each. Give each symbol a binary codeword so a receiver can decode a concatenation without separators. Restrict to prefix codes. Can you use fewer than the 16 bits required by two bits per symbol?

**Learner choices.** Choose tree shape and label placement, invent difficult concatenations, and compare total length with worst-case length.

**Hour menu.** 0–10 send and decode short strings; 10–15 establish no-free-separator and prefix rules; 15–35 construct trees and count bits; 35–40 partners walk left/right paths; 40–55 prove the best four-leaf tree choice; 55–60 show a savings calculation and decoding demonstration.

**Explore.**

- Why should the most frequent symbol get a shallow leaf?
- Could the shortest average code make one rare message longer than before?

**Hint ladder.**

1. Try A=0, then put all remaining words beneath the 1 branch.
2. An optimal positive-weight tree needs no node with only one child; remove such a step to shorten its descendants.

**Checked instance.** Optimize weighted total prefix-code length for weights 4,2,1,1.

**Reasoning.** Code A=0,B=10,C=110,D=111 has total 4×1+2×2+1×3+1×3=14 bits, average 7/4. An optimal four-leaf binary tree can be taken full. Its root splits leaf counts either 2+2, giving lengths 2,2,2,2 and total 16, or 1+3, giving 1,2,3,3. Swapping a larger weight into a shorter depth never increases cost, so the displayed assignment minimizes the second shape at 14. These exhaust full four-leaf shapes up to symmetry.

**Boundary.** Codes A=0 and B=01 are not prefix-free; without the rest of a specified code and a unique-decoding proof, greedily stopping at 0 can misread B.

**Extensions.**

- Change the frequencies to all equal; the balanced two-bit code now has total 8 and beats lengths 1,2,3,3 totaling 9.
- Use the two-smallest-weight merge idea to develop Huffman coding, proving why sibling placement permits recursive optimization.

**Satisfying stop.** An unambiguous code that saves two bits, with a finite optimality proof.

**Prior use.** Week 6 query trees share a branching representation. Here path length is weighted communication cost, and unknown separators create the central decoding constraint.

**Sources.**

- [Claude Shannon, A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf), Part I, PDF p. 18: code 0,10,110,111 and weighted average length. Inspection: relevant source framework inspected; finite example explicitly proved below.

<a id="ap-30"></a>
## AP-30 - The sensor changes the circuit it measures

Primary field: 94. Related: 15, 78. Status: reviewed plan v1; exact instance checked; not classroom-piloted.

**Adult question.** How do component laws and conservation determine a circuit, and why can attaching a measurement device alter the measured voltage?

**Anchor.** In an ideal DC resistor network, each edge current is voltage drop divided by resistance and currents balance at every internal node. A finite-resistance meter connected across a component becomes an extra parallel branch, changing the network solution.

**Bridge (exact-special-case).** Node voltages, Ohmic edge laws and current conservation form a literal ideal resistive circuit model; the meter is modeled as a specified resistor. Limits: Real meters, sources and components have tolerances and additional effects. Paper calculations avoid claiming that all physical devices obey these ideal values.

**Prerequisite gates.**

- **Entry:** V/F/A: interpret two labeled nodes and voltage differences along resistors.
- **Explore:** A: solve one linear node equation.
- **Explain:** P: distinguish a current split from equal currents and check the new measurement branch.
- **Prove:** A/L: derive node potentials from Kirchhoff equations and verify energy balance.
- **Reading:** Circuit sketch and Ohm’s law; partner calculation allowed.
- **Arithmetic:** Fractions and small linear equations; optional squares for power.
- **Reasoning:** A measuring device is part of the modeled system unless its loading is idealized away.
- **Hard Stop:** Capacitors, inductors and signal-frequency behavior add state and dynamics; they are not covered by a steady DC calculation.

**Materials and preparation (8 minutes).** Paper circuit with ideal 6 V source, a 2 Ω resistor from 6 V to node X, and a 1 Ω resistor from X to 0 V. Supply an optional meter branch of 2 Ω from X to 0 V.

**Launch.** First find node X’s voltage with no meter branch. Then attach a meter modeled as a 2 Ω resistor between X and 0 V and recalculate. Can the act of measuring lower the voltage being measured? Use current conservation rather than treating the original voltage as fixed.

**Learner choices.** Choose which node equation to write, test different meter resistances, and decide how a meter could disturb the circuit less.

**Hour menu.** 0–10 explore circuit connections and voltage differences; 10–15 introduce current=drop/resistance; 15–35 solve before and after attaching the meter; 35–40 trace and split current counters at the node; 40–55 vary meter resistance or check energy; 55–60 explain loading in a complete sentence.

**Explore.**

- Why is the incoming current no longer equal to the current through the original bottom resistor alone?
- What should happen as the meter’s resistance becomes extremely large?

**Hint ladder.**

1. Without the meter, equate (6−X)/2 to X/1.
2. With the meter, add X/2 to the outgoing side of that equation.

**Checked instance.** Compute X and all currents before and after adding the 2 Ω meter.

**Reasoning.** Without the meter, (6−X)/2=X gives X=2 V and current 2 A through both original resistors. With the meter, (6−X)/2=X+X/2 gives X=3/2 V. Incoming current is 9/4 A; outgoing currents are 3/2 A through 1 Ω and 3/4 A through the meter, totaling 9/4 A. The displayed voltage falls by 1/2 V while the source supplies more current.

**Boundary.** An ideal infinite-resistance voltmeter draws zero current and does not change this circuit. A zero-resistance branch would short X to 0 V and requires separate handling rather than division by zero.

**Extensions.**

- For meter resistance R>0, solve X=6R/(3R+2) and show it approaches 2 V as R grows.
- Verify source power equals the sum of resistor dissipation before and after loading; later add capacitance to study measurement transients.

**Satisfying stop.** A quantitatively checked case in which measurement changes the object measured.

**Prior use.** AP-10 spring networks share linear constitutive and compatibility reasoning. Keep that cross-link explicit; the new circuit question is sensor loading, not a renamed spring-combination exercise.

**Sources.**

- [David Tong, Electromagnetism](https://davidtong.org/pdfs/teaching/electromagnetism/electro3.pdf), Section 4.1.3, equation (4.4), printed pp. 74-77 / PDF pp. 8-11: Ohm’s law and Joule heating; the finite Kirchhoff equations are explicit below. Inspection: relevant source framework inspected; finite example explicitly proved below.

