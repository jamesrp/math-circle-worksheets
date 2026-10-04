# Making threes facilitator guide

## Mathematical overview

**Object.** Use exactly the nine combinations of three shapes (circle, triangle, square) and three fills (open, striped, solid), one tile of each combination. An allowed three has three different tiles; each attribute is independently all the same or all different. Storage positions are irrelevant. A bent-looking arrangement can be allowed and a straight row of physical tiles can fail.

**Unique completion and incidence.** Any pair of distinct tiles has exactly one completing tile: for each attribute keep the shared value, or use the missing value when the two values differ. Encoding the attributes as 0, 1, 2 gives the affine plane F₃², with completion z = -x - y coordinatewise modulo 3. It has 12 allowed threes, four through each tile. Distinct threes meet in 0 or 1 tile. There are exactly four ways to partition the nine tiles into three allowed threes, ignoring the order of the groups.

**Maximum without a three.** The largest line-free collection has 4 tiles. A two-by-two attribute rectangle is a witness. Five line-free tiles would have ten pairs, all completed among the four unchosen tiles. Each unchosen tile can complete at most two disjoint pairs, giving capacity at most eight. This contradiction establishes the upper bound.

**No early stopping.** Every legal three-tile collection has exactly three possible fourth tiles. Legal collection sizes 0, 1, 2, 3, 4 have respectively 9, 8, 6, 3, 0 legal extensions. Therefore legal adding from empty always lasts exactly four moves. In the two-player normal-play game, the second player wins regardless of choices, provided both obey the rule. It is a discovery about forced length, not a strategy-rich game.

**Limits.** These exact counts use two attributes with three values each and no duplicate tiles. Ordinary tic-tac-toe has only eight geometric lines and is a different object. One-attribute warmups and larger SET decks do not inherit this nine-tile maximum or game result.

## Readiness and intended discoveries

**K-1 before-use gate, not yet performed:** a child must reliably apply both attribute tests independently, including a near miss with exactly two equal fills. If this is not secure, use a one-attribute preparation or defer this packet. Do not claim that the preparation realizes the nine-point geometry.

K-1 can discover completion and grouping concretely. Grades 2-3 can search for large legal collections and notice the fixed game length. Grades 4-5 can prove uniqueness, incidence counts, the maximum, and absence of early stopping. Finding examples, proposing a general rule and justifying the rule are different outcomes.

**Status.** Final v2 has 4 / 5 / 5 problems. Finite mathematics is checked. Child readiness, material handling and the proposed hour remain untested.

---page---

# Preparation and session plan

## Materials and before use checks

For ten children, prepare one set of nine large tiles per child, with circle, triangle and square each in open, striped and solid fill. Tile squares about 45 mm across and clearly different fills work well. No commercial card artwork or color-only distinctions are needed. Keep five pair sets together initially; individual sets are useful for preserving a found collection. Per table supply three blank mats, selection counters, a tray for unused tiles, and spare paper. The final student grid is a parking/recording aid, not a rule about straightness.

For an optional upper proof, add ten small pair markers and four dishes. Adults can write the two tile names on each pair marker. Use a large demonstration tile set. **Estimated first preparation:** 20-35 minutes to print or draw, cut and sort reusable sets; allow another 5 minutes to rehearse the rule. Check that every set has exactly one of each combination and no indistinguishable stripe/solid printing.

**Two-attribute readiness check:** show the printed allowed triple (open circle, solid triangle, striped square) and the near miss (open circle, open triangle, solid square). Ask the child to judge shapes first and fills second, then move the pieces into a bent arrangement and ask again. Offer two new pairs and a fresh near miss without telling the answers. Proceed with the nine-tile tasks only if the child can explain or point out both attribute conditions. This is a practical proposed check, not a validated developmental test or a completed classroom observation.

If the gate fails, sort or complete triples using only three shapes while holding fill fixed. Keep it playful and brief. That activity is preparation only; omit the cap and game claims. The youngest adult should not have to run a second proof lesson while simultaneously repairing the rule.

## Common launch and flexible hour

**0-8 minutes:** let children handle the tiles, then use the printed valid completion and near miss. Show the two attributes separately. Rearrange the valid triple so it is visibly not a straight line. Ask whether the rule changed. Do not announce the largest legal collection.

**8-23 minutes:** solve the four printed pairs and trade invented pairs. Move to partitions or no-three building when completion is reliable. Adult reading and recording are enough; modular arithmetic is not a prerequisite.

**23-27 minutes:** movement break. Three children can hold shape/fill cards in changing positions while the group checks the attributes.

**27-45 minutes:** investigate large line-free collections. Older groups may play the adding game several times and predict whether a different move can change its length. Recheck any claimed five-tile success for an overlooked allowed three.

**45-57 minutes:** choose one explanation: unique completion, all triples through one tile, the maximum, or forced game length. The ten-pair proof is optional adult scaffolding after exploration, not a prescribed student procedure.

**57-60 minutes:** save a construction and one unresolved question. A child who thoroughly understands completion need not finish the optimization. Grade labels are approximate; route by rule fluency and interest.

---page---

# Keys for K-1 and Grades 2-3

## The four printed pairs

Read in page order: top left, top right, bottom left, bottom right.

**Top left:** open circle + striped circle → solid circle. **Top right:** open circle + open triangle → open square. **Bottom left:** striped circle + solid triangle → open square. **Bottom right:** striped triangle + open square → solid circle.

For new pairs, apply the rule to each attribute. Since the inputs differ in at least one attribute, the third tile is distinct from both.

## K-1

**Problem 1:** the four completions above. Other paired choices have one answer each. A child may demonstrate the answer without writing names.

**Problem 2:** four partitions exist in total; page 4 lists all. Easy entry examples are the three same-shape groups or the three same-fill groups. The problem asks for different ways, not necessarily a completeness proof at this band.

**Problem 3:** 4 tiles is the maximum. One answer is open circle, striped circle, open triangle and striped triangle. Every triple from this set has exactly two of some shape or fill, so it fails one condition. “We could not add another” verifies maximality of a particular attempt only; page 5 explains why no five-tile answer can exist.

**Problem 4:** four triples through any chosen tile. For an open circle, the other pairs are: striped circle + solid circle; open triangle + open square; striped triangle + solid square; solid triangle + striped square. The eight other tiles are paired off once each. The chosen tile's physical position in the middle of the table has no mathematical effect.

## Grades 2-3

**Problem 1:** the four completions above; no pair of distinct tiles has two answers. Common attributes force the same value, and differing attributes force their third value.

**Problem 2:** exactly four unordered splits, listed on page 4. Reordering the same three groups is not a new split.

**Problem 3:** maximum 4, with the same two-by-two witness. Once four legal tiles have been found, replacing one with another and then adding a fifth cannot work, because no legal five-tile collection exists anywhere. If a child has fewer than four, adding is possible without replacing anything.

**Problem 4:** four triples through a chosen tile. Each uses two of the other eight tiles, and unique completion pairs those eight without overlap or omission.

**Problem 5:** all legal games last exactly four moves. The second player makes move 4; the first player then has no legal move and loses. Choices change the final collection, not the duration or winner. If a game ends after three moves, inspect the three legal fourth choices. If it lasts five, find the forbidden triple. This answer concerns legal play, not a player voluntarily passing.

---page---

# Key for Grades 4-5

## Problems 1 through 3

**Problem 1:** the printed completions are solid circle, open square, open square and solid circle. Attribute-by-attribute forcing proves uniqueness for every distinct pair. All nine combinations are present, so the forced combination always exists as a tile.

**Problem 2:** maximum 4. The open/striped circles and open/striped triangles give a witness. The ten-pair argument on page 5 rules out five, hence every larger size too. Children can first verify the witness by choosing each of its four triples and locating a failing attribute.

**Problem 3:** two different allowed threes share 0 or 1 tile. If they shared two, those two would have two completions, contradicting Problem 1. Disjoint examples are the three circles versus the three triangles; intersecting examples are all circles versus all open tiles. Exactly four threes pass through any chosen tile. Pair the other eight by unique completion; each pair appears in one such three, giving 8/2 = 4.

## Problem 4 and the complete partition key

Use C, T, S for circle, triangle, square and O, H, F for open, striped, solid. Here H means hatch/striped; these codes are adult shorthand, not a new student representation to impose. For example CH is the striped circle.

**Split 1, shapes:** {CO, CH, CF}; {TO, TH, TF}; {SO, SH, SF}.

**Split 2, fills:** {CO, TO, SO}; {CH, TH, SH}; {CF, TF, SF}.

**Split 3:** {CO, TH, SF}; {CH, TF, SO}; {CF, TO, SH}.

**Split 4:** {CO, TF, SH}; {CH, TO, SF}; {CF, TH, SO}.

These are also the complete list of 12 allowed threes, arranged into four parallel classes. For a direct count: there are three all-same-shape triples, three all-same-fill triples, and six triples using each shape and each fill once (one for each assignment of three fills to three shapes). Their total is 12. The two attributes cannot both be all same when the three tiles must be different.

**Why the partition list is complete:** any two disjoint affine lines have the same direction. With coordinates modulo 3, the four directions are horizontal, vertical, slope 1 and slope -1; lines with different directions intersect. Once one triple in a partition is chosen, its two parallel mates are forced to cover the remaining six points. Thus only the four listed splits are possible. A fully concrete alternative is to check the list of 12 triples: each triple is disjoint from precisely its two companions in its displayed split.

## Problem 5

Every legal adding sequence stops at four tiles, never sooner. With three legal tiles, completing each of its three pairs gives three distinct forbidden unused tiles. Of the six unused tiles, exactly the other three remain legal. Smaller legal collections also extend; a legal four cannot extend by the maximum theorem. Optional hint: “With three tiles chosen, which unused tiles are ruled out by a pair?” This question belongs with the adult, not as a mandatory procedure before the child explores.

---page---

# Proofs and source notes

## The maximum proof with physical pairs

Assume five chosen tiles contain no allowed three. Their ten unordered pairs each have a unique completion, and none of those completing tiles can be chosen. Put each pair marker into the dish of its completing unchosen tile. There are four dishes.

Two different pairs in the same dish cannot share a chosen tile. If {a,b} and {a,c} were completed by x, then a and x would have both b and c as their unique completion. Thus pairs in each dish are disjoint. Among five chosen tiles, there can be at most two disjoint pairs. Four dishes hold at most eight pair markers, yet there are ten. Contradiction. Four tiles work, so the maximum is exactly four. This is an elementary incidence/counting proof, not an assertion from unsuccessful searching.

## Why a legal triple never gets stuck

Let a, b and c be the three chosen tiles, with no allowed three. Complete pairs ab, ac and bc. Their completions lie outside the chosen set. No two completions can coincide, because the pairs share a tile and uniqueness would then force the other two chosen tiles equal. These are exactly the forbidden fourth tiles: any new forbidden triple must use the new tile and two existing tiles. There are six unused tiles and only three forbidden ones, leaving exactly three legal choices.

For size two, one of seven unused tiles is forbidden, leaving six; sizes zero and one allow nine and eight. A legal four has no extension because five is impossible. This proves the extension counts 9, 8, 6, 3, 0 and the fixed four-move game. It does not depend on the visible storage grid.

## Verification and limits

A fresh finite check builds triples directly from the two attribute tests, verifies all 36 pair completions, all 12 triples, their intersections, all four partitions and every subset through size five. Counts of legal subsets of sizes 0 through 5 are 1, 9, 36, 72, 54 and 0. Every legal triple has three extensions; every maximal legal collection has size four. These are mathematical checks only. The K-1 readiness trial remains unperformed.

## Sources

Julia Carney, **SET and Finite Affine Geometry**, University of Chicago REU (2021), sections 1-3 for the attribute rule, finite affine incidence and the SET connection; section 5, pp. 15-16, for cap context and the two-dimensional four-point maximum. [Author-hosted paper](https://www.math.uchicago.edu/~may/REU2021/REUPapers/Carney.pdf). This guide supplies its own complete nine-tile maximum and no-early-stopping proofs.

Tanya Khovanova, **SET Tic-Tac-Toe** (June 2020). [Original game investigation](https://blog.tanyakhovanova.com/2020/06/set-tic-tac-toe/). This is a related game precedent, not a claim that the final shared-collection avoidance game has the same rules or strategic behavior.

Givental, Nemirovskaya and Zakharevich, **Math Circle by the Bay** (AMS/MSRI, 2018), Preface pp. viii-ix: deep multi-level themes, manipulatives and discussion of explanations. The preparation, pacing and readiness check here are local untested proposals.
