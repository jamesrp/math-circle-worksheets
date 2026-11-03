# Week 128 (draft plan): Splitting necklaces

**Strand:** shape (topology) with fair division (app region "Shapes and spaces"; a "Games and choices" variant is possible). **Deep-math field:** combinatorial topology, Borsuk–Ulam, fair division. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

An open necklace (a string of beads, ends not joined) has k colours, each appearing an even number of times. Two thieves want to cut it into pieces and share the pieces so that each gets exactly half of every colour. Theorem (Goldberg and West 1985 for two thieves; Alon and West 1986 with a Borsuk–Ulam proof): at most k cuts always suffice. The bound is sharp: if each colour sits in one contiguous block, every block must be cut, so k cuts are needed. Alon (1987, "Splitting necklaces") proved the version for q thieves: (q − 1)k cuts suffice. The proofs are topological and non-constructive; they guarantee a split without saying where it is. For two colours there is an elementary argument children can follow: slide a window covering exactly half the beads from the left end to the right end. At the start the window holds some number r of red; at the end it holds the rest, R − r, where R is the total. Each one-bead slide changes the red count by at most one, so somewhere the window holds exactly R/2 red, and then it automatically holds half the blue too, because its size is half the necklace. Two cuts at the window's ends finish the job. This is the discrete intermediate value theorem, the same "no jump" move as Borsuk–Ulam in one dimension. Its sister result, the ham sandwich theorem (Steinhaus's problem of 1938, proved by Banach with Borsuk–Ulam; Stone and Tukey 1942 in all dimensions), says one straight cut can halve two regions in the plane at once. What children can discover: one cut is sometimes enough, two always seem to be, some necklaces force two, and with three colours three cuts seem always to work.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Borsuk-Ulam theorem and bisection of necklaces](https://www.ams.org/proc/1986-098-04/S0002-9939-1986-0861764-9/) — Noga Alon and Douglas B. West, Proceedings of the AMS 98 (1986), 623–628. Every necklace with k colours has a bisection with at most k cuts; cites Goldberg and West, "Bisection of circle colorings" (1985) (read November 3, 2026).
- [The Borsuk-Ulam Theorem and bisection of necklaces (author PDF)](https://web.math.princeton.edu/~nalon/PDFS/Publications/The%20Borsuk-Ulam%20Theorem%20and%20bisection%20of%20necklaces.pdf) — same paper. Contiguous colour blocks force k cuts; Goldberg–West proof by induction on a continuous version; Hobby–Rice theorem; note added in proof that Alon proved the q-thief conjecture (read November 3, 2026).
- [The humble ham sandwich inspired a math theorem for sharing food fairly](https://www.scientificamerican.com/article/the-humble-ham-sandwich-inspired-a-math-theorem-for-sharing-food-fairly/) — Scientific American (translated from Spektrum der Wissenschaft). Steinhaus 1938, Banach's Borsuk–Ulam proof, Stone and Tukey 1942, the two-dimensional case, existence without a method (read November 3, 2026).
- [Necklace Splitting (a lesson for jewel thieves) - Numberphile](https://rosetta.to/u/numberphile/necklace-splitting-a-lesson-for-jewel-thieves-numberphile) — archive page with transcript of the Numberphile video (June 2019). Two thieves need at most two cuts for two types; (k − 1)·t cuts for k thieves and t types; non-constructive proof (read November 3, 2026).
- Prior use with children: none found. Searched "necklace splitting problem two thieves math circle handout beads" and "necklace thieves math circle worksheet"; results were research papers, an REU paper and the Numberphile video.

## A kid-friendly way in

Materials: pony beads in three colours and pipe cleaners or string, or simply printed bead strips cut from card with scissors. Each table gets prepared strings such as RRRRBBBB, RBRBRBRB, RRBBBBRR, and three-colour strings like RRBBGG, RGBBGR and RRGBBGRR (every colour an even count). Two paper cups labelled with the two "thieves". Prep: about 20 minutes to thread or print 12 strings. Launch (2 minutes): hold up a string with 4 red and 4 blue, make one cut in the middle, and check fairly with the cups; then show RRRRBBBB, where one cut fails, and ask how few cuts can always work.

Suggested hour: 0–5 launch; 5–25 two-colour strings with cups; 25–45 stump-a-partner and three-colour strings; 45–55 half-window demonstration on one long string; 55–60 share the hardest necklace anyone built.

## By band

- **K–1:** Two colours, short strings (2 red and 2 blue). Children make cuts with scissors on paper strips and share pieces into two cups until both cups match. Count cuts with tally marks.
- **2–3:** Two colours, 8 beads: sort strings into "one cut is enough" and "needs two". Can anyone find a string that needs three? Make your own string to stump a partner.
- **4–5:** Three colours: find splits with three cuts, find a string that needs all three, and explain the sliding-window argument for two colours with a paper window that covers half the beads.

## Checked facts

- `check_week_128()`: there are 70 strings with 4 red and 4 blue; every one can be split fairly with at most 2 cuts, RRRRBBBB needs 2 and RBRBRBRB needs 1. Exactly 36 of the 70 need only one cut (the first four beads must hold two red: 6 × 6 = 36).
- `check_week_128()`: the half-window argument checked exhaustively for two colours with counts (2,2), (4,2), (4,4), (6,4), (2,6): some window of exactly half the beads holds exactly half the red.
- `check_week_128()`: with three colours (2,2,2) (90 strings) and (4,2,2), every string splits with at most 3 cuts even when the pieces are handed out alternately, and some strings (for example RRBBGG) need all 3.
- The general k-cut theorem, the q-thief theorem and the ham sandwich theorem are cited, not computed.

## Nearest existing themes

Week 58 (Fair division) uses additive values and cut-and-choose; atlas GA-02 is the one-dimensional Borsuk–Ulam move (a matching opposite pair on a loop); Week 16 (Sperner) is the discrete cousin; GA-22 splits coloured pegs with stretched bands. Week 33's "necklaces" are rings counted up to rotation, a different topic despite the name. New here: a discrete fair-division problem where the guarantee comes from a no-jump argument and where the number of cuts is the quantity to minimise.

## App connection

"Shapes and spaces" or "Games and choices". A bead string on screen; the child taps gaps to cut and drags pieces into two bags; the bags show colour counts. Puzzles: "split this necklace with at most two cuts", "find the necklace in this set that needs three cuts", and a two-player mode where one player builds a string and the other must split it within k cuts. Could share a family with any existing "drag to two bins" mechanic.

## Open questions

- Do K–1 children handle "half of each colour" as a goal, or should their version be equal counts of one colour only?
- Is the half-window argument reachable for 4–5 with a physical window, or only as a facilitator demonstration?
- For three colours, is exhaustive search too long at the table? Possibly provide a curated set of six strings.
- Decide whether to include a circular necklace variant (joined ends), which changes the cut counting.
