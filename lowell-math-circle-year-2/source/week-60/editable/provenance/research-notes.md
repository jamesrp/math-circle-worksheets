# Week 60 research: Take it or pass

Prepared October 4, 2026. Research and outline only; student problems are for the fresh writer. Proposed theme, unpiloted. The actual ticket-handling procedure has not been rehearsed.

## Mathematical overview and model limits

Fix a positive integer horizon n before the round. Every draw independently samples the same known finite score distribution. After observing a score, accept it and end, or pass it permanently. No recall, fees, score accumulation, or choice of the unseen offer is allowed. If the nth draw is reached, acceptance is mandatory, including a zero score. The objective is the expectation of the one accepted score, not its worst possible value, a guaranteed win, or the chance of selecting the largest value in the whole hidden sequence.

Let V_m denote the largest expected score before seeing any of m remaining offers. V_1 is their mean. For m > 1,

`V_m = E[max(X, V_{m-1})]`.

After the current offer x appears with m offers including this one left, accepting gives x; passing leaves optimal expected reward V_{m-1}. Therefore accept if x > V_{m-1}, pass if x < V_{m-1}, and either action is optimal at equality. At the final offer there is no continuation option. The induction compares all legal future policies, not just one more draw. A randomized decision cannot improve the maximum of the two available expectations.

Ferguson's general finite-horizon recursion is in Chapter 2, printed p. 2.1 / PDF p. 1. Section 2.4, printed pp. 2.7-2.8 / PDF pp. 7-8, distinguishes a known finite population without replacement from independent offers. The latter gives the recurrence used here. His section 2.1, printed p. 2.2 / PDF p. 2, defines the classical secretary problem: only relative ranks are observed and reward is one for selecting the overall best. Our score distribution is visible and numerical reward matters; the secretary cutoff near n/e is not a theorem for this activity. [Ferguson, *Optimal Stopping and Applications*, Chapter 2](https://www.math.ucla.edu/~tom/Stopping/sr2.pdf).

Replacement makes the past irrelevant to future scores. With a known deck drawn without replacement, the remaining inventory becomes part of the state; these constant continuation values would be wrong. With recall, accepting the best seen at the end changes the model. With fees, reinforcement, unknown horizon, or a different objective, solve a new model rather than carry over the thresholds.

Experiments can suggest a policy. A complete, properly weighted outcome collection evaluates it exactly. Backward induction or an exhaustive policy audit establishes optimality. Expected score is an average over the specified possibilities; it does not promise the average of a short observed batch.

## Checked small instance

Three equal physical tickets have scores 0, 4, 6. This instance was calculated here, not copied as a source exercise.

| Offers before first draw | Best mean | Optimal acceptance before the mandatory final draw |
|---|---:|---|
| 1 | 10/3 | Final offer must be accepted |
| 2 | 40/9 | Accept 4 or 6; pass 0 |
| 3 | 134/27 | First accept only 6; if continuing, use the two-offer policy |

For two offers, nine complete words produce accepted scores 0 once, 4 four times, and 6 four times: total 40. For three offers, 27 words produce accepted scores 0 twice, 4 eight times, and 6 seventeen times: total 134. Thus 4 changes from an acceptance with two offers left to a pass with three.

The tempting policy comparing every nonfinal score only with the next draw's mean accepts 4 too early at horizon three and averages 130/27. The improvement 4/27 is small but exact. Allowing recall would instead yield the expected maximum 142/27; this is a boundary check, not an available student move.

`check_examples.py` enumerates all 8 deterministic history policies at horizon two and all 4,096 at horizon three, including policies that react differently to different earlier observations. Its exact rational optimum matches the recursion. Multiple enumerated policies can agree on every reachable choice while differing after an earlier acceptance; that does not produce distinct behavior in actual play. Results are in `math-checks.json`.

Full length-n draw words are equally likely. Stopped records of different lengths generally are not. For instance a first-draw acceptance represents all possible unseen tails. Do not compare an unweighted list of shortened stopped records or retain one representative per different score. The first unfamiliar full-word-to-accepted-score record needs a small input/intermediate/output demonstration using a different practice distribution; the writer chooses its form. Optional hints and the backward calculation stay with adults.

## Readiness and suggested page-band menu

Recommend one combined `students.pdf`, with a substantial Grades 3-5 concrete entry and a Grades 3-5 exact comparison continuation, then a Grades 4-5/readiness-dependent explanation or design continuation if the writer finds a worthwhile task. This is a menu of entry levels, not a problem list or fixed page count. Avoid a decorative K-1 packet. The same investigation need not be duplicated at three levels.

- Reading: adult may read the short rules; children must retain accept/pass and the fixed deadline. A partner or referee should enforce the action.
- Arithmetic: compare 0, 4, 6; count two or three turns. Exact comparison can use pooled equal-case score totals and adult addition; fractions are not needed to compare policies on the same number of cases. Interpreting different-sized outcome collections needs equivalent averages or concrete equal-sized batches.
- Reasoning: distinguish one fortunate result from an exact policy average; keep a choice rule fixed while comparing possible offers; decide using current score and turns remaining. This is plausible for ready third graders with mathematical adult support, not a claim of classroom validation.
- Upper continuation: backward induction and the meaning of a continuation average; explaining why no history-dependent policy can do better. Fractions and notation are gates for a symbolic extension, not required for the physical core.

## Format, launch, pacing and preparation recommendations

Use the current fixed KK11 / 3333 / 445 context, checked against `worksheet-workflow/context.md`; the older roster in README is historical. Three adults remain anchored. This theme's core is for the two older tables. Choosing another already approved concrete activity for KK11 is a scheduling decision for the organizer; do not count that as new Week 60 coverage.

Allow a little ticket handling, then demonstrate one legal practice round with a different distribution: reveal the current offer, return the randomizing ticket and mix, pass once with a visible turn counter removed, and accept the current offer to end. A partner should visibly prevent reclaiming a pass. Demonstrate the mandatory last choice. Do not demonstrate the optimal 0/4/6 policy. An ideal known distribution is an assumption; indistinguishable slips and mixing are its proposed physical implementation.

A possible hour has five minutes of movement, about four minutes of shared action, 20-30 minutes of policy play and exact cases, a reset/role swap, and a readiness-dependent continuation or closing comparison. Timings are proposals. A rich exact comparison can take a second visit. Keep a single recoverable word and accepted score rather than concurrent statistics; share complete cases at a table.

The outline specifies three older-table kits and exact sizes. Reusable outcome cards should be supplied as author-created assets if the writer uses them; asking every child to transcribe 27 words is not the mathematics. Cutting supplied slips/records may take 10-15 minutes; hand-making complete sets takes longer. Both estimates and the procedure are untested. Before classroom use, rehearse return/mix, the display-copy distinction, irreversible passes, final mandatory choice, and role rotation with the actual bag and cards.

## Prior work and novelty boundary

Current `WEEKS-11-51.md` and `BONUS-AND-RETURN-VISITS.md` were inspected, together with the current Week 24 and Weeks 42-46 PDF models. The research cache preserves extracted current-page text; selected relevant rendered pages were also inspected.

| Prior theme and page evidence | Connection and difference |
|---|---|
| Week 24 Grades 4-5, PDF pp. 1-7; bonus pp. 1-4, especially bonus p. 4 | Known uniform card draws, complete counts and expected points already exist. The bonus optimizes concealed mixtures against opponents; Week 60 optimizes when to end a sequence. It is not a first introduction to expectation in this library. |
| Week 42 Grades 4-5, PDF pp. 1-4; bonus pp. 1-3 | Independent replacement and equal histories support fairness extraction. Week 60 retains that physical model but chooses acceptance times for score. |
| Week 43 Grades 4-5, PDF pp. 1-4; bonus pp. 1-3 | Equal-probability histories and resets already support shuffle uniformity. Week 60 is not another uniform-shuffle catalog. |
| Week 44 Grades 4-5, PDF pp. 1-4; bonus pp. 1-3 | Reinforcement changes future distributions. Week 60 explicitly does not reinforce; the unchanged distribution is essential to its threshold theorem. |
| Week 45 Grades 4-5, PDF pp. 1-4; bonus pp. 1-3 | Conditioning on hidden cards/reports is prior work. Here the score itself is revealed and independent future offers need no posterior update. |
| Week 46 Grades 4-5, PDF pp. 1-4; bonus p. 2 | Random instruction stories and finite coverage counts are prior work. Neither coverage waiting nor forgetting a start is the acceptance objective. |

No finite expected-score stopping activity was located in those current indexed themes. This is a scoped overlap check, not a claim that no similar mathematics appears anywhere in the atlas or a claim of newly invented mathematics. Returning children can reuse the exact-draw model while confronting a new decision theorem. Record actual prior use rather than infer mastery from file presence.

## Pedagogy evidence, observations and our inferences

The organizer's first-year collection was consulted by extracting the eleven Fall 2025 DOCX handouts and inspecting the pattern-block handout. *Pattern Block Exercises - Google Docs*, PDF p. 1, explicitly begins with five minutes of handling blocks and then pairs/trios. Handouts 3, Problem 3.1, revisits the prior take-away game's copying strategy. These establish precedents for material exploration and returning to a known action; they do not establish attendance or optimal-stopping experience. README reports the stronger first-year lesson: concreteness and learning by doing. The current context records the later successful tiling and unsuccessful paper-lamp sessions; the lamp rule was hard to retain. **Our inference:** make the deadline and irreversible choice visible and partner-enforced.

Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*, printed p. viii / PDF p. 9, explicitly seeks topics with deeper mathematical context; pp. ix-x / PDF pp. 10-11 describe independent attempts, available manipulatives, changing pace/depth and extra challenges. **Our adaptation:** retain optimality as the destination while allowing a physical first visit and later proof. The book does not prescribe this ticket activity or our staffing.

Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 7, “At the lesson,” item 1 (`OEBPS/part0017.xhtml`), reports game outcomes plausibly caused by missed legal moves; item 2 records strong engagement with open K'nex polygon construction. Lesson 8, “At the lesson,” item 2 (`part0018.xhtml`), reports copying/coloring delays and changed support. **Our adaptation:** check legal rounds before interpreting strategies, and provide movable outcome records. These are source-supported design choices, not a pilot of our activity.

## Provenance and next-stage routing

Downloaded Ferguson reference: `external-resources/new-themes-52-63/week60-61/ferguson-finite-horizon-sr2.pdf`; URL and checksum are in that folder's manifest. Established stopping theory is credited; the 0/4/6 finite-policy audit, wording, proposed materials and future worksheet figures are author-created. Do not copy source prose or figures. Read root `REPUBLISHING.md`: workflow style exemplars contain borrowed material. Generated prompts may remain in this run, but the future portable source ZIP must omit prompt blocks, third-party books, source screenshots and copied exemplars. Attribution is not republication clearance.

Outline: `outline.md`. Run: `tmp/worksheet-runs/week-60-new-v1/`. Follow root `STAGE-ROUTING.md`: one combined student packet and fresh writer, adversarial critic, independent mathematical review, and reviser; no generator changes. Recommend the math review because exact outcome weights and competing policy claims are central. A facilitator guide is a separate subsequent step, opening with the facts and limits above and keyed to the actual final student tasks. No student packet, guide or classroom result is claimed by this research stage.
