# Week 195 (draft plan): Ordering stones with a balance

**Strand:** logic (Codes and logic). **Deep-math field:** comparison sorting, decision trees, information lower bounds. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Some stones look alike but weigh differently; a pan balance compares two at a time and says which is heavier. How many weighings are needed, in the worst case, to put n stones in order? Each weighing has two answers, so a method with k weighings is a decision tree with at most 2^k leaves, and each leaf can name only one of the n! possible orders. So at least ⌈log2(n!)⌉ weighings are needed (proved): 3 for three stones, 5 for four, 7 for five (since 2^6 = 64 < 120 = 5!), 10 for six. The bound counts outcomes but says nothing about how to reach it, and ordinary methods miss it: binary insertion and merge sort each need 8 weighings for five stones in the worst case. Merge insertion (Ford and Johnson, 1959) pairs the stones, sorts the winners, and inserts the losers in a clever order so that each insertion uses a balance's full power; it sorts five stones in 7 weighings and meets the counting bound for every n up to 11. At 12 stones the bound says 29, but 30 is the true minimum (exhaustive computer search, recorded in OEIS A036604), so the counting bound is not always exact. The exact minimum is known only for small n (OEIS lists n up to 22); Ford–Johnson was the best known method for 20 years and, by Peczarski's 2007 result, is still unbeaten below 47 stones; exact values for larger n are open. An exhaustive adversary search here confirms 3, 5 and 7 weighings for 3, 4 and 5 stones. Unlike a sorting network (Week 23), a weighing plan may choose its next comparison after seeing the last answer; this adaptivity is what lets five stones be ordered in 7. Children can discover that 3 stones sometimes need 3 weighings and sometimes only 2, the counting bound from a tree of outcomes, and, at 4–5, the seven-weighing plan for five stones.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [How to sort?](https://math.mit.edu/~shor/18.310/sorting.pdf) — Peter Shor, MIT 18.310 lecture notes, Fall 2011 (read November 4, 2026). The pigeonhole proof that k ≥ log2(n!), the table entry "≥ 7" for n = 5, and the exercise to sort five in 7 comparisons.
- [Optimal Sorting](https://opendsa-server.cs.vt.edu/OpenDSA/Books/CS4104/html/SortingOptimal.html) — OpenDSA, Virginia Tech CS4104 (read November 4, 2026). The ⌈log n!⌉ bound, the seven-comparison sort of five elements, merge insertion as the Ford and Johnson sort, matching the bound up to 11, and 30 against 29 at 12.
- [A036604: minimal number of comparisons needed to sort n elements](https://oeis.org/A036604) — OEIS (read November 4, 2026). The values 0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 30, … for n up to 22, with the Ford–Johnson count (A001768) as an upper bound and ⌈log2 n!⌉ (A003070) as a lower bound.
- [Merge-insertion sort](https://en.wikipedia.org/wiki/Merge-insertion_sort) — Wikipedia, secondary pointer (read November 4, 2026). Ford and Johnson 1959; best known for 20 years until Manacher (1979); Peczarski, "The Ford-Johnson algorithm still unbeaten for less than 47 elements" (2007).
- Prior use with children: [Sorting Algorithms](https://classic.csunplugged.org/activities/sorting-algorithms/) — CS Unplugged (read November 4, 2026): "students compare different algorithms to sort weights in order", linked to ACM K–12 Level I (grades 3–5). The page does not state the comparison bounds. No circle handout on the five-in-seven problem was found (searched "merge insertion" puzzle and "sorting 5 elements 7 comparisons").

## A kid-friendly way in

Identical containers (film canisters or plastic eggs) holding 1 to 5 metal washers, padded with cotton wool so they cannot be told apart by sound, and a bucket balance. Each weighing is recorded on a strip as a small picture (which two, which way it tipped). Children order 3, then 4, then 5 containers, counting weighings with cubes, and the table keeps a record board of "fewest weighings that always works". Prep: two sets of five loaded and numbered containers per table (washer counts marked inside the lid), a balance per table, recording strips; about 25 minutes, mostly checking that the balance tips clearly for one washer. Launch (3 minutes): with three containers in front of the room, weigh A against B, then the heavier against C; sometimes the order is settled after two weighings, sometimes a third is needed, and the room predicts which.

## By band

- **K–1:** Find the heaviest of 3, then of 5, with a knockout (4 weighings for 5). Then put 3 containers in order. Count weighings with cubes; notice that sometimes 2 are enough and sometimes 3 are needed. No reading.
- **2–3:** Order 4 containers. What is the fewest weighings that always works? Tables race on the record board; 5 is the record, and children draw their method as a tree of pictures with two branches at each weighing. How many different orders can 4 containers be in (24), and how many endings can a 4-weighing tree have (16)?
- **4–5:** Five containers: ordinary methods take 8; can 7 always work? Count first (7 weighings give 128 endings, enough for 120 orders; 6 give 64, not enough). Then discover the Ford–Johnson trick with hints from the guide: weigh two pairs, compare the two heavier ones, insert the fifth into the chain of three, then the last into the right place.

## Checked facts

All in `check_logic_3.py`, function `check_week_195()`:
- ⌈log2 n!⌉ for n = 1 to 12: 0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 29; the Ford–Johnson count: 0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 30; equal up to 11.
- Exhaustive adversary search: 1, 3, 5 and 7 weighings for 2, 3, 4 and 5 stones.
- 2^6 = 64 < 120 ≤ 128 = 2^7; 2^4 = 16 < 24 ≤ 32.
- Binary insertion and merge sort both need 8 weighings for 5 stones in the worst case.
- Three stones by "A against B, then the heavier against C": two weighings suffice in 2 of the 6 orders (1/3 of the time), when C is the heaviest.
- The heaviest of 5 by knockout: 4 weighings.
- Cited, not computed: the true minimum 30 for 12 (OEIS A036604; OpenDSA); Peczarski's result (Wikipedia).

## Nearest existing themes

Week 23 (Sorting machines) is closest: comparator networks, and the same count 2^k against n! (it shows 3 bars for three lanes and 5 for four). What is new here is adaptivity: a weighing plan is a decision tree whose next question depends on the last answer, so five stones need only 7 weighings, and Ford–Johnson's insertion order is a genuinely new idea. Draft Week 145 (The fake coin and the balance) uses the same balance but with three outcomes and a search for one odd coin; here the balance never balances and the goal is a full ordering. Week 6 (Code breaking) proves the 2^k bound for yes-or-no answers. The topic-scouting README set aside "Champion and runner-up" (largest and second largest of n) as a Week 23 return visit; the K–1 knockout here touches it, and the two could share a session. The pancake-flips and train-yard-sorting scouting drafts sort with other moves. The overlap with Week 23's counting bound is real, so the guide should present the bound as a return and spend the time on adaptive trees and the 5-in-7 plan.

## App connection

Codes and logic region, near Week 23's "Sorting machines" family: a row of identical stones and a balance; the child drags two stones onto the pans and sees which is heavier; the app plays an adversary that answers so as to keep as many orders alive as possible, and a counter shows how many orders remain. Puzzles: "Order 4 stones in 5 weighings against the tricky balance"; "Order 5 in 7"; "Find the heaviest of 8 in 7 weighings". The adversary turns the lower bound into play, as in draft Week 145's balance family.

## Open questions

- Material fit: does a classroom bucket balance tip reliably for one washer, and do the containers stay indistinguishable? Rehearse with the actual kit; draft Week 145 has the same question.
- Can 2–3 children draw their method as a branching tree, or should an adult scribe it?
- The 5-in-7 plan is intricate; decide how much the guide gives as hints and whether it suits a pilot table or only an extension.
- Whether this should be a Week 23 return visit rather than a week, given the shared counting bound.
