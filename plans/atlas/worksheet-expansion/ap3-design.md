# AP3: eight complete investigations, design handoff

Author: `worksheets_geometry` (AP owner). Date: 2026-09-26. Exactly AP-19, AP-20, AP-22, AP-24, AP-25, AP-27, AP-28 and AP-30. The current data has 24 staged student pages, 48 fully keyed student prompts and eight fully keyed guide extensions. No renderer or PDF has been created for this batch. Original cards and previously approved batches are unchanged.

`ap3-checks.py` and `ap3-checks-results.json` provide exact finite audits. These support, rather than replace, the general proofs in the solutions. Each family includes a prerequisite line for the contents, full reading/arithmetic/reasoning gates, realistic preparation, timing, launch, staged hints, source evidence, prior-use cross-links and exact drawing data. Student pages should be handed out sequentially. Page count can increase if diagrams and proof regions need more room during production; do not compress type to preserve 24.

## Design decisions

| Family | Learner choices and route | Real destination / prerequisite | Assessment |
|---|---|---|---|
| AP-19 | Choose one depth; construct a competing channel; place an interior receiver; compare placements with bounded timing error | All positive ambiguity pairs, complete reconstruction conditions, and a uniquely optimal receiver position under a stated noise model. Square roots, linear equations and intervals. | Promising for algebra-ready learners; actual wave law remains supplied. |
| AP-20 | Build a production plan; invent resource prices; choose an extra resource | Matching construction/price certificate, equality conditions, then an integer/fractional gap and marginal-gain distinction. Fractions and inequalities. | Strong first-pilot candidate with manipulatives and a short universal proof. |
| AP-22 | Build unequal private bags; challenge them; choose a tolerance | Matching minimax bounds, unique optimal mixtures, complete near-optimal ranges, and a changed-information counterexample. Independent probabilities and expectation. | Promising; observed scores are explicitly not proof of an expected guarantee. |
| AP-24 | Invent contrasting legal histories; choose a small-survival threshold; change population size | Exact transition laws, finite-time distribution, almost-sure absorption and asymmetric fixation probability without optional stopping. Probability, conditional averages, geometric tails. | Concrete entry; limiting argument is a genuine additional gate. |
| AP-25 | Make legal trades; invent conserved labels; choose reachable and impossible targets | All linear invariants, a complete reachable interval with shortest-path proof, and a parity obstruction in a changed network. Counter arithmetic through algebra. | Strong first-pilot candidate; broader-network limitations are demonstrated, not merely warned about. |
| AP-27 | Choose indistinguishable splits and a new sensor; choose rates and observation delay | Permanent ambiguity versus exact recovery, nonnegative data cone, sharp noise amplification and a proven optimal discrete delay. Linear equations and powers. | Promising with algebra; uniqueness and robustness remain separate. |
| AP-28 | Invent four strips; choose damaging bits; organize all received words | An attained optimal five-bit code, universal four-bit obstruction, and detection/correction separation. Counts, binary words, powers through 32. | Strong first-pilot candidate. The supplied codebook is a staged comparison, not a launch answer. |
| AP-30 | Choose meter resistance; select a tolerance; add another meter | Correct loaded circuit, sharp tolerance threshold, power audit and a multiple-meter agreement counterexample. One linear equation, fractions and inequalities. | Promising with algebra; paper model only, with component laws supplied. |

## What changed from the original cards

- **AP-19:** The original depth-recovery example becomes an inverse-survey design. Every interior receiver position is classified, positivity restrictions are derived, and equal timing error gives amplification ε/min(x,12−x), uniquely minimized at the interface. Both depths stay hidden in the diagram: no bed shape may imply an answer. The equal-depth interpretation is moved to an extension about effective depth.
- **AP-20:** The original plan/certificate is retained as a tractable launch but gains a proof of uniqueness, an independent integer upper bound, and a decision between adding red or blue stock. The optional full real-capacity formula has three regimes, each with a feasible plan and price certificate. Recipe quantities use x,y; prices use r,b to avoid confusing blue price with product B.
- **AP-22:** The supplied 2×2 game becomes a learner-built bag investigation. Both players' certificates are required. A best response against q=3/4 separates exploitation from a worst-case guarantee. Exact ε-ranges and shared-ticket/revealed-action changes show why hidden independence is a mathematical hypothesis.
- **AP-24:** The original two-parent chain is followed by a three-parent population starting asymmetrically. A finite-time expectation bound proves all-red fixation probability 1/3 without an invalid symmetry argument. The general-N extension uses a uniform one-generation absorption event and a vanishing mixed-state contribution, avoiding unintroduced stopping theorems.
- **AP-25:** Initial inventory (4,7,1) permits both forward and backward exploration and a five-state chain. Learners invent their own positive labels before the full real left-nullspace classification. The core proves that every invariant-compatible nonnegative integer state is actually reached. The changed 2A↔2B reaction shows a parity obstruction; the guide's A+B↔2B network adds an enabling obstruction even when integer displacement is possible.
- **AP-27:** The original equal/unequal rate contrast is extended to complete nonnegative compatibility conditions and a sensor choice. Error propagation is exact. A separate known-rate pair 3/4 and 1/2 has an optimal observation delay of two steps, proved against all positive integer delays by the sign of consecutive differences. Waiting is therefore a design decision, not always a benefit.
- **AP-28:** Learners first construct and attack their own code. The known five-bit code appears only on page 2 as a clearly supplied construction to audit. The later page counts covered received words, exhibits a violated promise that triggers an alarm, and a two-flip violation that silently misdecodes. Three-bit detection and repeated parity-check signatures prevent conflating more checks with correction.
- **AP-30:** Learners choose a finite-resistance meter and derive a sharp resistance threshold for any relative loading tolerance. Power provides an independent audit. Two agreeing meters produce a more disturbed voltage, and m meters yield a general threshold. Zero resistance is treated as a short separately, never by 0/0.

## Source scope and scientific assumptions

The original atlas is a pointer, not an authority. Primary/reference content was reopened on 2026-09-26.

- Vallis explicitly gives √(gH) in the long-wave/shallow-water limit. The worksheet supplies a two-region travel-time approximation and excludes interface reflection/current/rotation effects. It does not infer real bathymetry from a toy channel.
- Boyd–Vandenberghe supplies the feasible-point inequality behind weak duality. The resource-price bound is proved directly; no strong-duality theorem is assumed.
- Bonanno supplies mixed-strategy and support-indifference context. Indifference only finds candidates; the worksheet proves both global bounds separately.
- Chasnov's genetic-drift section describes Wright–Fisher and then switches to Moran. AP-24 explicitly uses the former sampling definition and derives its own finite-generation results. No Moran/diffusion result is transferred to the wrong process. The separate reaction section provides signed stoichiometric context, not the worksheet's reaction coefficients or reachability theorem.
- The official Åström–Murray page identifies observability and state estimation, but the linked chapter PDF failed to fetch. This limitation is recorded in the data rather than claiming it was read. The primary MIT 6.3100 state/output and noise material was inspected as additional context. Every special-case reconstruction and delay statement is proved in the key, so no blocked source is an unproved premise.
- Shannon's noisy-channel setup is contextual. The one-bit adversarial code and its finite optimal-length proof are self-contained; they are not an assertion of asymptotic channel capacity.
- Tong supplies Ohm behavior as an extra physical assumption and I²R dissipation. AP-30's network topology and conservation equations are explicit, with all source/component values ideal and exact.

All exact source locators, URLs, adaptations and inspection limits are in `ap3-data.json`. Scientific rules are visible supplied assumptions on student pages, not claims proved by counter games.

## Verification and production instructions

The checker passes all eight families. It enumerates 539 two-region survey inversions; integer resource plans and 25 independent LP vertex problems; rational mixed-strategy/tolerance cases; all ordered parent choices for N=2 through 6; 343 reaction-state BFS inventories and 49 catalyst inventories; 972 observed-state inversions; all 1,820 four-word length-four codebooks; every length-five received word; and exact meter current/power identities over rational networks. Inspect the results JSON for exact counts and values.

The proofs additionally cover continuous choices, strict positivity, zero states, equality cases, all integer times, arbitrary inventories, indefinite future absorption and all allowed adversarial errors. The finite checker is not evidence for a theorem beyond those proofs.

For production, prioritize usable custom objects: a hidden-depth channel with chosen receiver; physical recipe cards; unfilled bag layouts; separate old/new generation mats; invented reaction-label tags; hidden tank boxes with a fixed sensor; large bit strips; and an unambiguous loaded circuit with junction dots and separate meter branches. Use neutral scaffolds before discovery. In particular:

- Do not preprint the optimal receiver position, best bag proportions, reaction-state chain length, codebook on page 1, optimal observation delay, or loaded voltages.
- Four message strips are legitimate because four messages are a stated requirement; a fixed number of answer boxes for undiscovered states would not be.
- The all-positive depth intervals in AP-19 are coupled by the exact total time; a filled rectangle would falsely imply independent depth choices.
- Keep AP-24's old parent generation fixed while making every offspring; sequentially replacing parents would change the model.
- Keep formula/label spacing clear, including slowness versus depth and relative error versus volts. Provide the full equation where it is first used.

All investigations remain unpiloted. Source inspection, exact mathematics and render review do not establish actual classroom timing or engagement.
