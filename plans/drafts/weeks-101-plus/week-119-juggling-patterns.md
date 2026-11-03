# Week 119 (draft plan): Juggling patterns

**Strand:** symmetry and counting (Patterns and symmetry). **Deep-math field:** combinatorics (permutations, counting), the mathematics of juggling. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Siteswap notation describes a juggling pattern by the heights of its throws: on every beat at most one ball is thrown, and a throw of height t lands t beats later (0 means an empty beat). A repeating sequence t_0, t_1, …, t_(n−1) can be juggled, with no two balls landing on the same beat, exactly when the numbers i + t_i, taken mod n, are all different, that is, when "beat plus throw" is a permutation of the n beats. The average theorem: a jugglable pattern uses exactly (t_0 + … + t_(n−1))/n balls, so the average is always a whole number; 441 and 531 are three-ball patterns, 432 and 321 crash. Counting (Buhler, Eisenbud, Graham and Wright, "Juggling drops and descents", 1994): there are exactly b^n jugglable sequences of period n with fewer than b balls, so exactly (b + 1)^n − b^n with exactly b balls, counting rotations such as 15 and 51 as different. For period 2 and three balls that is 4² − 3² = 7: 06, 15, 24, 33, 42, 51, 60. The site swap itself is a reasoning move children can use: exchanging where two throws land, t_i and t_j become t_j + (j − i) and t_i − (j − i), turns one valid pattern into another (33 becomes 42). Proved: the permutation test, the average theorem, the count. Checked here: the test and the average theorem on every sequence of period up to 4 with throws up to 7, and the count for period up to 4 and up to 3 balls. Not covered: counting patterns up to rotation, and real-hand constraints (two hands, catching), which this week ignores. Children can find the crash rule, discover that the ball count is the average, and list all patterns of a small period.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Enumerating (multiplex) juggling sequences](https://arxiv.org/pdf/0801.2597). Steve Butler and Ron Graham, arXiv 0801.2597. States the test (all i + t_i mod n distinct), the average theorem, and that period-n sequences with fewer than b balls number b^n, citing Buhler, Eisenbud, Graham and Wright, *American Mathematical Monthly*, 1994 (read November 3, 2026).
- [Juggling Drops and Descents: Juggling](https://www.cecm.sfu.ca/organics/papers/buhler/paper/html/node2.html). Web version hosted by the Centre for Experimental and Constructive Mathematics, SFU; its index page credits Joe Buhler and Ron Graham and the *American Mathematical Monthly* 101 (1994). Juggling patterns as permutations of the beats and the average theorem (Theorem 1) (read November 3, 2026).
- Prior use with children: [Mathematics of Juggling](https://circles.math.ucla.edu/circles/lib/data/Handout-4433-4262.pdf). Glenn Sun after Allen Knutson, UCLA Math Circle, Advanced 1, October 9, 2022. Ladder diagrams, testing 51, 441, 324, 345, proving the average theorem, state diagrams (read November 3, 2026).

## A kid-friendly way in

Rainbow strips. A long paper strip marked with beats 0 to 19, and "rainbow sticks": card arcs of lengths 1 to 7 beats, colour-coded by length. A pattern card such as 4 4 1 repeats under the strip; from every beat a child lays the rainbow of that length. The rule is one sentence: no two rainbows may land on the same beat. To count balls, lay a pencil across the strip between two beats far from the start and count the rainbows it crosses. Optional movement: three children pass beanbags to a steady clap for the pattern 3, so the class sees a throw land three beats later. Prep: print strips, cut rainbow sticks from card, about 25 minutes. Launch (2 to 3 minutes): on the board, lay 3-rainbows from every beat (no crashes, three cross any gap), then try 4 3 2 and watch two rainbows land together.

## By band

- **K–1:** copy a repeating pattern of rainbow colours onto the strip; spot crashes; count the rainbows crossing the pencil. Patterns use only 1 to 5 and the card shows colours as well as numbers.
- **2–3:** which three-number patterns work? Test 441, 531, 423, 432, 345, then invent new ones; record each pattern's ball count and look for a rule (the average). Find every two-number pattern that uses three balls (there are 7).
- **4–5:** the landing clock: write beat + throw for each beat of the pattern, divide by the period and look at the remainders; why do different remainders mean no crash? Why is the ball count the average (each ball is one rainbow over the gap; follow the rainbows for one full period)? Then the table of period-2 counts by number of balls (1, 3, 5, 7 for 0, 1, 2, 3 balls) and a guess at the formula; the site swap move as a way to make new patterns.

## Checked facts

Computed in `check_symmetry_games.py`, `check_week_119()`:

- 3, 441, 531, 51, 423, 55500, 42, 60, 633 pass the test and their ball counts (found by simulating and counting arcs across a gap) equal their averages; 432, 321, 54 and 6431 fail;
- every jugglable sequence of period 1 to 4 with throws 0 to 7 has a whole-number average equal to its ball count;
- for period n = 1 to 4 and b = 0 to 3, the number of sequences with exactly b balls is (b + 1)^n − b^n;
- the seven period-2 three-ball sequences are 06, 15, 24, 33, 42, 51, 60.

Cited, not computed: the general count b^n (Butler and Graham, citing Buhler, Eisenbud, Graham and Wright).

## Nearest existing themes

No catalog week or atlas family mentions juggling. The landing clock is Week 4's hopping on a circle (i + t mod n) and the test asks for a permutation, as in Week 3 (Shuffle machines); the average theorem is a double count (each arc counted once for every gap it spans), the kind of move Week 10 (Bridges) makes when it counts bridge ends. Week 33 (necklaces) counts strings up to rotation, which is the open-ended follow-up here (counting patterns up to rotation). New: a time-line representation (arcs over beats), a permutation test that children discover from crashes, and an exact enumeration formula they can guess from a table.

## App connection

Patterns and symmetry. A "Juggling ladder" family: the child taps throw heights onto a beat line and the app animates balls along arcs, flashing any crash. Example puzzles: "Make a three-ball pattern of length 3 with no throw higher than 5" (several answers, checked by the test); "Change one number so this pattern stops crashing"; "Find all seven two-throw patterns with three balls". Fit B: a new mechanic with simple validators.

## Open questions

- Do rainbow sticks of exact beat lengths stay put on a strip, or should children draw arcs with a template instead? Rehearse with a 20-beat strip.
- The start of a strip has fewer arcs overhead; the facilitator guide must say to count balls far from the start.
- Whether the beanbag clap demonstration helps or distracts; it is optional and not needed for the mathematics.
