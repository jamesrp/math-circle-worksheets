# Week 188 (draft plan): A few shortcuts make a small world

**Strand:** networks (Maps and networks), with chance. **Deep-math field:** graph distance, random graphs (small-world networks). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Distance in a network is the fewest links on a route between two people; the diameter is the largest distance. In a ring of n people who know only their two neighbours, the diameter is n/2 and the average distance grows in proportion to n (n²/(4(n − 1)) for even n: about 4.27 for 16 people and 6.26 for 24). Watts and Strogatz (Nature, 1998) showed in simulations that rewiring only a few links of such a ring at random makes typical distances short while each person's neighbourhood stays tightly knit: "small-world" networks. A theorem makes this precise for one model: adding a random matching (everyone gets one random extra friend) to a ring of n people gives, with probability tending to 1, diameter about log₂ n (Bollobás and Chung, 1988, with a lower bound of log₂ n minus a small constant and an upper bound of log₂ n + log₂ log n + 10). So a ring of a million people with one random extra friend each would have diameter near 20 rather than 500,000. The social story is Milgram's 1967 letter-passing experiment (written up by Travers and Milgram, 1969): 217 of 296 starters sent a folder on, 64 folders (29 per cent of those sent) reached the Boston target, and completed chains had a mean of 5.2 intermediaries, the source of "six degrees of separation"; the low completion rate means it is evidence, not proof, about real friendships. Two features children can find: one shortcut can leave the farthest pair exactly as far as before (in a ring of 16 with a shortcut straight across, the two people midway between its ends, on opposite sides, are still 8 apart) while the average drops a lot (from 4.27 to 3.51), and a second shortcut cuts the diameter to 5 (average 2.93). Checked here: the ring formulas, those examples, and seeded random trials (ring of 16: averages about 3.4, 2.9 and 2.4 with 2, 4 and 8 random shortcuts). Proved: the ring formulas and Bollobás–Chung. Observed in simulation and data: the Watts–Strogatz and Milgram findings.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Collective dynamics of 'small-world' networks](https://ideas.repec.org/a/nat/nature/v393y1998i6684d10.1038_30918.html) — Duncan J. Watts and Steven H. Strogatz, *Nature* 393 (1998) 440–442 (RePEc abstract page). Rewiring a regular ring gives networks that are highly clustered with short path lengths; examples include the *C. elegans* nervous system, the western US power grid and film actors (read November 4, 2026).
- [An Experimental Study of the Small World Problem](https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f24/wrap/readings/Travers+Milgram-Sociometry-1969-2786545.pdf) — Jeffrey Travers and Stanley Milgram, *Sociometry* 32(4), 1969, 425–443. 296 starters, of whom 217 sent the folder on; 64 completed chains (29 per cent); mean 5.2 intermediaries; procedure first tested by Milgram (1967), *Psychology Today* (read November 4, 2026).
- [The Diameter of a Cycle Plus a Random Matching](https://www.math.lmu.de/~kpanagio/ModelsLitSS12/WattsStrogatzDiameter.pdf) — B. Bollobás and F. R. K. Chung, *SIAM Journal on Discrete Mathematics* 1(3), 1988. Diameter about log₂ n with high probability, with explicit bounds (read November 4, 2026).
- [Six degrees of separation](https://plus.maths.org/content/six-degrees-separation) — Marianne Freiberger and Rachel Thomas, Plus magazine, December 6, 2024. Plain-language account of Milgram's letters and of Watts and Strogatz's ring with a few random shortcuts (read November 4, 2026).
- Prior use with children: none found for K–5 (searched NRICH, JRMF and circle pages for six degrees, small world and shortcuts). The nearest classroom use is university level: James Sethna's exercise [Six degrees of separation](https://sethna.lassp.cornell.edu/StatMech/ComputerExercises/SmallWorld/SixDegreesOfSeparation.pdf) (*Statistical Mechanics*, Oxford 2006, Exercise 1.7), a programming task on a ring with p·L·Z/2 random shortcuts (read November 4, 2026).

## A kid-friendly way in

A message ring. Children stand in a circle holding a long yarn loop; a message (a bean bag) may move only along yarn. Pick a sender and a receiver by drawing name cards, pass the bag one step at a time, and count the passes on a tally board. Then add shortcuts: two children chosen by drawing cards hold the ends of a long piece of yarn across the circle. Pass again; record the fewest passes. Prep: a ball of yarn, 4 to 8 long shortcut pieces, name or number cards, a distance-chart sheet for older children; about 15 minutes. Launch (2–3 minutes): eight volunteers in a ring; pass from one to the person opposite (4 passes), add one yarn shortcut, and pass again (1 pass).

## By band

- **K–1:** count passes around the ring between two drawn names, before and after one or two shortcuts; who is now closest to me, and who is farthest?
- **2–3:** for a printed ring of 16 dots, find the farthest pair and the average distance from one person; add one shortcut straight across and find that the farthest pair has not moved closer; add a second and look again. Where should 2 shortcuts go to make the farthest distance as small as possible?
- **4–5:** compare planned shortcuts with random ones (drawn names): pool class results for 2, 4 and 8 random shortcuts; explain the ring's n/2 diameter; hear the Milgram letters and Bollobás–Chung's log₂ n, and guess the distance in a ring of 1000 with one random extra friend each.

## Checked facts

Computed in `check_networks_3.py`, `check_week_188()`:

- ring of 16: diameter 8, average distance 64/15 (about 4.27); ring of 24: diameter 12, average 144/23 (about 6.26); even rings average n²/(4(n − 1)) for n up to 40, and 48 checked;
- ring of 16 plus shortcut 0–8: diameter still 8, average 421/120 (about 3.51); plus 4–12 as well: diameter 5, average 44/15 (about 2.93);
- 24 people each knowing two neighbours on each side: diameter 6, average 78/23 (about 3.39);
- seeded random shortcuts, 400 trials each: ring of 16 averages about 3.36, 2.89, 2.43 with 2, 4, 8 shortcuts; ring of 24 about 4.03 and 3.29 with 4 and 8.

Cited, not computed: Bollobás–Chung, Watts–Strogatz and the Milgram figures.

## Nearest existing themes

Week 67 (Meeting on shortest roads), Week 69 (Thin and fat road triangles) and Weeks 66 and 74 measure graph distance in structured networks; Week 68 (How many ways out) studies infinite graphs. Draft 152 (Who is most important?) walks randomly on a network, and draft 182 (gossip) spreads information by calls. New here: random shortcuts as the change that collapses distance, the diameter-versus-average contrast, and a theorem (log₂ n) about random graphs.

## App connection

Maps and networks: a "shortcut" family. A ring of dots; the child places a fixed number of shortcut links and the app shows the farthest pair and the average distance live, with stars for meeting targets (16 dots, 2 shortcuts, farthest distance 5 or less). A "random" button adds shortcuts by chance so children can compare their planned shortcuts with luck.

## Open questions

- Circle size: 16 children may not all be present; the facilitator guide needs ring results for the actual group size, and a dot-ring sheet as backup.
- Whether passing the bag stays the fewest-pass route when children choose directions; a "guess the fewest passes first" rule may help.
- Whether the Milgram story belongs on student pages at all (it is about adults and letters) or only in the adult guide.
