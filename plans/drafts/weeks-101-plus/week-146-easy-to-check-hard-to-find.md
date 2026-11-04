# Week 146 (draft plan): Easy to check, hard to find

**Strand:** logic (Codes and logic). **Deep-math field:** computational complexity, certificates. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Some puzzles have answers that are quick to check but seem to need a long search to find. The partition problem is the cleanest: given some whole-number weights, can they be split into two groups with equal totals? A proposed split is checked with two sums. Finding one may mean trying many of the 2^(n−1) ways to share n weights between two unnamed pans (512 for 10 weights, 524,288 for 20, about 5.5 × 10^11 for 40). The class NP consists of yes-or-no questions whose "yes" answers have short certificates that can be checked quickly (Cook's Clay description: a certificate y for an instance x, checked by a fast relation); P consists of questions that can be answered quickly outright. Whether P = NP is open, and it is one of the seven Clay Millennium Prize problems (2000). Cook (1971) and, independently, Levin defined NP-completeness, Karp (1972) gave the definition its standard form, and many natural problems are NP-complete: a fast method for any one of them would give fast methods for all of NP. Number partitioning, three-colouring a map, and placing the fewest "ice-cream vans" so every street corner is next to one (a dominating set) are all NP-complete. Three honest limits. First, NP-completeness is about the worst case as the numbers grow; with small whole numbers, partitioning is easy by keeping a running list of reachable totals (for the 7-stick bag below the list never holds more than 49 totals, 0 to 48), so kid-sized puzzles are hard to search by hand but not hard for computers. Hayes and Mertens describe how difficulty depends on the ratio of digits to weights, with a sharp easy-hard transition. Second, "no" answers are different: sometimes there is a short reason (an odd total; all weights even but half the total odd; one weight bigger than half), but for the bag 1, 3, 4, 7, 8, 11 (total 34) no equal split exists and none of those reasons applies; whether every "no" has a short certificate is another open question. Third, simple rules fail: "put the next biggest weight on the lighter pan" splits 3, 3, 2, 2, 2 into 7 and 5, though 3 + 3 = 2 + 2 + 2. Children can discover the asymmetry between checking and finding, that a puzzle maker can guarantee a solution by building it first (split a tower, then mix the pieces), and that a "no" sometimes has a neat reason and sometimes does not.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The P versus NP Problem](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf) — Stephen Cook, official problem description for the Clay Mathematics Institute (read November 4, 2026). Definitions of P and NP through a checking relation and certificates; Cook (1971), Karp (1972) and Levin on NP-completeness; subset sum and three-colouring as examples.
- [The Easiest Hard Problem](https://www.americanscientist.org/node/1946) — Brian Hayes, American Scientist 90(2), March–April 2002 (read November 4, 2026). Number partitioning is NP-complete; picking playground teams is the greedy heuristic; greedy and Karmarkar–Karp differencing can miss a perfect split; difficulty depends on bits per number over count.
- [The Easiest Hard Problem: Number Partitioning](https://arxiv.org/abs/cond-mat/0310317) — Stephan Mertens, arXiv, 2003 (read November 4, 2026). Abstract: NP-hardness, the random easy-hard phase transition and what it means for algorithms.
- [Clay Mathematics Institute $1,000,000 Prize problems](https://cs.nyu.edu/pipermail/fom/2000-May/004001.html) — Joe Shipman, FOM mailing list, May 30, 2000 (read November 4, 2026). The announcement of the seven Millennium Prize Problems, P versus NP listed first, $1,000,000 each.
- Prior use with children: [Dominating Sets](https://classic.csunplugged.org/activities/dominating-sets/) — CS Unplugged (read November 4, 2026), with its [teachers' supplement](https://classic.csunplugged.org/documents/activities/dominating-sets/unpluggedTeachersSupplement2012-draft-v1-dominatingSets.pdf) (read November 4, 2026): ages 7 and up place ice-cream vans on a Tourist Town map; six is the fewest; checking a placement is easy, finding the fewest is hard, and the problem is NP-complete.

## A kid-friendly way in

Cube sticks on a two-row mat (the Week 30 kit): a "bag" is a set of linking-cube sticks of given lengths, and the job is to lay them end to end in two rows of equal length. A checker slides the two rows side by side and sees at once whether they match. Puzzle makers build a solvable bag by snapping one long tower, breaking it into two equal halves, and breaking each half into sticks before mixing them. Prep: snap stick sets for three bags per pair (for example 1 to 6 for K–1, the 7-stick bag 2, 3, 5, 7, 8, 10, 13, and the "no" bag 1, 3, 4, 7, 8, 11), plus number cards for the same bags; about 25 minutes. Launch (2 minutes): one child splits a bag of 5 sticks into two rows behind a folder; the folder lifts and the room checks in two seconds. Then a table gets the same bag unsplit and a timer.

## By band

- **K–1:** Split small bags (lengths 1 to 6) into two equal rows; check a friend's rows by lining them up. Be a puzzle maker: break a tower in half, break the halves into sticks, mix, and hand the bag over. No reading.
- **2–3:** The 7-stick bag has exactly one split; time finding it against checking it. Try the "biggest stick to the shorter row" rule and find a bag where it fails. Then a bag with no split: can you convince someone it has none without trying everything?
- **4–5:** Count the ways to share n sticks (each stick has two places; doubling), and estimate how long 20 or 40 sticks would take by hand. Collect quick reasons for "no" (odd total, a stick longer than half, all even with an odd half) and find a "no" bag none of them explains. Compare with checking a 3-colouring of a printed map. The P versus NP story as an open problem with a prize.

## Checked facts

All in `check_logic_games_2.py`, function `check_week_146()`:
- 3, 3, 2, 2, 2 splits only as 3 + 3 = 2 + 2 + 2; greedy leaves a gap of 2.
- Bag 2, 3, 5, 7, 8, 10, 13 (total 48): exactly one split, 2 + 5 + 7 + 10 = 3 + 8 + 13 = 24; greedy gives rows 25 and 23.
- 7 sticks: 2^7 = 128 placements, 64 splits if rows are not told apart; 10 sticks 512 splits, 20 sticks 524,288, 40 about 5.5 × 10^11.
- Bag 1, 3, 4, 7, 8, 11 (total 34): no split, though the total is even and no stick exceeds 17. Bags 2, 2, 2, 8 and 1, 1, 1, 7 have no split for the quick reasons above.
- The running list of reachable totals for the 7-stick bag never exceeds 49 entries.
- The Petersen graph: 15 edges to check; 3^10 = 59,049 colourings to search, 120 of them proper.
- Cited, not computed: P versus NP open, NP-completeness of partition, colouring and dominating set (Cook, Hayes, CS Unplugged).

## Nearest existing themes

Week 62 (Conflict networks) asks for a schedule and a reason fewer slots fail: certificates on both sides for small cases. Draft 140 (Proving without telling) proves a 3-colouring exists without revealing it, which is the NP certificate kept secret; this plan is the step before it. Week 30 shares the stick mat but asks which targets one kit balances, not whether a bag splits. Week 54 (Partitions) uses "partition" in the different sense of writing n as a sum. Draft 128 (Splitting necklaces) shares fairly with few cuts. New: the asymmetry between checking and finding, certificates for yes and for no, and an open problem stated honestly.

## App connection

Codes and logic region (or Numbers), possible family "Two-row split": sticks drop into two rows and the rows light green when equal; a "maker" mode builds a bag by cutting a tower so the child sees why maker bags always work. Puzzles: "Split 2, 3, 5, 7, 8, 10, 13"; "This bag has no split: pick the reason, or say none of these"; "Beat the greedy robot: give it a bag it fails on". Could share sticks with Weight kits (Week 30).

## Open questions

- The honest caveat that small bags are easy for computers: does it undercut the message for children, or is it a good 4–5 discussion?
- Is the 7-stick bag the right difficulty for 2–3 (hard but not hopeless)? Pilot the timing.
- Whether a "no" bag frustrates more than it teaches; it may need an adult-led ending.
- Overlap with draft 140: if both are built, run this one first.
