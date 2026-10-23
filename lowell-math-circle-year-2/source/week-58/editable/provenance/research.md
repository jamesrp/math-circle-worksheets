# Week 58 research: fair division with different preferences

Prepared 4 October 2026. New, unscheduled library theme; mathematical research and outline only. The proposed materials and classroom route are unpiloted. Paper-cutting, timing and adult-handling pretests have not been performed.

## Mathematical destination and assumptions

Each person evaluates every bundle using that person's own preferences. A complete allocation uses every item once and gives each item to one person. Values are nonnegative and additive: a bundle's value is the sum of its items' values. They can differ between people and include zero. No comparison between different people's numerical scores is needed. Equal counts, equal physical size and equal value are different claims.

For n people, **proportional** means each person receives at least 1/n of the total value that person assigns to everything. **Envy-free** means each person values their assigned bundle at least as highly as every other individual bundle. Ties pass. These definitions do not mean everyone obtains a favorite item, the sum of scores is largest, or people assign equal numbers to their own bundles. Negative values (chores), complementarity, changing tastes, and paying compensation fall outside this model.

The useful theorem is: under additive values and a complete allocation, envy-free implies proportional. For observer i, every other bundle is worth at most the observer's own bundle. Adding all n comparisons gives total value at most n times own value. With two people the converse holds: own value at least half the total implies it is at least the other bundle's value. With three people that converse fails. Leaving items unallocated can invalidate this argument, and cannot repair an all-items requirement by hiding an awkward object.

These definitions and relationships are supported by Procaccia, *Cake Cutting Algorithms*, §13.2, downloaded PDF pp. 1–3 (author-hosted chapter pagination). The arguments and examples below are independently worked for this project.

## Exact small examples checked independently

* Four distinct cards R1, R2, B1, B2: Ada values each R at 3 and each B at 1; Ben values each R at 1 and each B at 3. Each total is 8. Ada receiving both Bs and Ben both Rs gives equal counts but own values 2 versus the other's bundle valued 6, for both observers. Switching the two color bundles gives each own value 6 versus 2 and passes both comparisons. One R and one B each also passes, tied at 4. Of all 16 labeled complete allocations, exactly five are envy-free: the color split plus the four mixed splits. Reversed owners are not duplicates, because people have different tastes.
* Three indivisible equally valued cards, two people: any full allocation has counts 0/3 or 1/2, so the smaller bundle is envied. No full envy-free allocation exists. It also cannot give both people at least 1.5 items' value. Dividing one card into two equally valued halves permits 1.5/1.5, but changes the resource model. Random allocation, taking turns, discarding items, and “envy-free up to one good” are different guarantees and should not be called exact envy-free division.
* Three people and three complete panels X, Y, Z, allocated to A, B, C respectively: A's values are (4,8,0), B's (0,4,8), C's (8,0,4). Each total is 12 and own panel is worth 4, so the allocation is proportional. Every person prefers a different panel worth 8. The cyclic rows can be realized by three equal-length divisible panels with those constant value densities. The example refutes equivalence of the two fairness notions for three people; it does not claim three-person envy-free cake division is impossible.

`verify_math.py` exhausts these cases, then checks all 729 two-person value profiles on three goods with individual values 0,1,2 (5,832 allocations). Output is `math-checks.json`. This audit covers the research instances; the eventual worksheet's invented instances need a fresh audit.

## Cut and choose: what it guarantees and why

For two people and a divisible resource, the cutter makes two pieces of equal **own** value. The chooser takes a piece of maximum **own** value, with either piece allowed at a tie. The cutter receives the remainder. The cutter is indifferent; the chooser does not prefer the remainder. Thus both comparisons pass. Additivity gives proportionality as well. Existence of an exact equal-value cut requires divisible/nonatomic values (for an interval, a continuous cumulative value function suffices); it does not follow for whole candy cards.

Own equal value need not mean equal lengths. For two unit-length panels, cutter densities are 3 on the first and 1 on the second, chooser densities 1 then 3. Cutting at 2/3 of the first panel creates cutter values 2 and 2. The chooser sees 2/3 and 10/3 and takes the latter. A 300 mm paper model with a 150 mm red panel then a 150 mm blue panel has the analogous cutter's cut 100 mm from the left end. Each person's density means equal lengths within one color have equal value; the cut piece's value is proportional to its length within that color. It is not a rule that a tiny fragment retains a whole token's score.

This proof is independently expressed from the standard method in Procaccia §13.3.1, PDF p. 4. The model is ideal; a child's approximate physical cut establishes an approximation, not exact equality. If someone deliberately cuts unequal-value pieces, the cutter's guarantee may fail. Changing a preference card during allocation changes the problem.

For three people, “cut three equal pieces and let the others choose” does not guarantee envy-freeness: the second chooser may prefer the first chooser's piece. The proportional/envious cyclic panels give a manageable upper explanation branch. Procaccia §13.3.3, pp. 5–6, gives the genuine three-person Selfridge–Conway method with trimming and a separate allocation of trimmings. That full algorithm is source background, not a proposed first elementary route. No claim about the current research frontier is taken from this older chapter.

## Source and provenance decisions

Primary inspected mathematics: [Ariel D. Procaccia, Cake Cutting Algorithms](https://procaccia.info/wp-content/uploads/2020/03/cakechapter.pdf), §§13.2–13.3.3, PDF pp. 1–6; local reference `external-resources/new-themes-52-63/week58-59/procaccia-cakechapter.pdf`. Pages 3–6 were also rendered and inspected. This is a scholarly model and algorithm source, not evidence that the elementary adaptation has been tested.

The suggested Cecil Rousseau fair-division anchor was sought but no exact accessible original document was located. A failed guessed URL and search results are not citations. The inspected Procaccia chapter is the primary alternative. All intended student wording, diagrams, people, token values and recording layouts must be authored afresh. Reference PDFs stay in external-resources and do not enter a portable worksheet-source ZIP. Root `REPUBLISHING.md` was read; generated workflow prompts contain existing borrowed exemplars and are local workflow records, not distributable source material.

## Teaching evidence and inferred adaptation

* Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*, Preface printed vii–ix (PDF pp. 8–10): the authors describe student interaction, deep topics developed over time, independent problem solving, manipulatives, and clear, easy-to-understand statements. This is an actual account of their practice. Our inference is to keep one visible preference card and one recoverable allocation at a time, with the observer evaluating both bundles; adults may read, while children retain the division and choice decisions.
* Rozhkovskaya, *Math Circles for Elementary School Students*, Introduction “Berkeley 2009” (`OEBPS/part0010.xhtml`) records individual adult support. Lesson 1 “At the lesson” (`part0011.xhtml`) records that the crossing stage was harder and slower than planned. Lesson 6 “At the lesson,” sausage discussion (`part0016.xhtml`), records the need for more concrete examples before the one-extra-piece argument was convincing. Our inference is to give substantial physical division/choice time before the additive-value table or universal guarantee.
* First-year actual source: `lowell-math-circle-year-1/lowell-math-circle/Math Circle Fall 2025/Handouts 8.docx`, Problems 8.1 and 8.5, shares apples by counts/divisibility and counts distributions including zero. This is a mathematical precedent, not a classroom outcome report. Week 58 changes the meaning of fairness to differing subjective valuations. Current `worksheet-workflow/context.md` separately records organizer observations: pattern-block handling succeeded and paper-only lamp rules were difficult. Those observations support externalizing bundles/preferences; they do not establish this new route's success.

## Honest prerequisites and route

Main printed pages: **Grades 2–5**, with a readiness-dependent **Grades 3–5** explanation/three-person section if appropriate. One combined `draft/students.pdf`, then `final/students.pdf`, with the actual band on each page under `../STAGE-ROUTING.md`. No three separate grade packets are required.

Genuine younger oral entry: handle colored cards, divide all cards between two trays, and have the other child choose a tray first. The child chooses the division and explains or points to which bundle they prefer; an adult reads, records or mediates turns. This entry can suit some K–1 children without arithmetic, but it does not establish an equal-value guarantee for indivisible cards and warrants no manufactured K–1 worksheet. Show one non-task division → first choice → remaining bundle visual before this unfamiliar turn convention.

The main numerical route requires adding small scores and comparing a bundle with the alternative using **one unchanged person's card**. Dot groups can replace multiplication. Children must understand “whole item” versus “splittable strip” and keep the observer fixed during a comparison. The upper route requires comparing three bundles and understanding a universal claim/counterexample; thirds and formal symbols are adult shorthand, not entry prerequisites. Giftedness does not replace these gates. Older pairs may use their third child as an observer/referee, rotating; a referee is not another recipient in a two-person trial.

## Preparation, physical constraints and unperformed pretests

Use five pair kits across the fixed tables (two younger, two middle, one upper pair plus rotating referee). Each kit: 12 sturdy 25 mm cards, four of each of three colored/shaped types; two 150–180 mm trays; two large preference cards at least 100×150 mm with types and 0–3 dots or scores; ten 300×40 mm paper strips with two clearly marked 150 mm color regions; blank paper and pencil. Prepare one three-tray kit and three observer cards for the upper branch. Cards depict pretend goods; no food is necessary. Each instance's available cards and values must be specified by the writer, with unused cards removed. Four-card cases are mathematically sufficient; the supplied dozen is a material limit, not a prescribed task.

Only paper strips may be cut when divisibility is declared. For density strips, partial lengths carry proportionate value within each region. Adult-held scissors and a marked ruler are needed; print at 100%, verify the 100 mm scale before use, and join Letter sheets with a butt seam for a 300 mm strip rather than shrink it. Scoring aids must not obstruct moving cards. Do not make arithmetic transcription the activity. For an ideal theorem exact cuts are assumed; any trial with millimeter cutting error must be described as an experiment with that error.

Unperformed: print-scale and seam check; rehearsal of split/choose/reset with the non-mathematician adult; whether children retain the fixed-observer comparison; card/tray handling; scissors timing; 35–40 minute work route; classroom piloting. These remain guide preflight items, not completed validation.

## Novelty against inspected current packets

The linked `novelty.md` records actual pages across the relevant base and bonus variants. Returning children meet a new allocation object and fairness condition, rather than a new stable-matching profile or a renamed random-output exercise.
