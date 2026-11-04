# Week 181 (draft plan): A new road makes traffic worse

**Strand:** games (Games and choices), touching networks (Maps and networks). **Deep-math field:** game theory on networks (selfish routing, equilibria, the price of anarchy). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Drivers each choose a route from start to finish, and a road's travel time can grow with the number of cars on it. Traffic settles where no driver can shorten their own trip by switching alone (an equilibrium). Dietrich Braess (1968, "Über ein Paradoxon aus der Verkehrsplanung") showed that adding a road can make every driver slower at equilibrium. In Braess's example as presented by Nagurney, six travellers on two routes take 83 each; a new link opens a third route that looks faster (70 at the old traffic), drivers move to it, and the new equilibrium has everyone at 92. A floor-map version with whole cars: two routes from S to E, each made of a crowded road (minutes = number of cars on it) and a long road (always 5 minutes); four cars split 2 and 2 and take 7 minutes each. A free shortcut joining the two crowded roads makes "crowded, shortcut, crowded" tempting, all four cars end up on it, and each takes 8 minutes; leaving it alone would cost 9. The best arrangement with the shortcut open is still 2 and 2 (28 car-minutes against 32). Whether the new road hurts depends on how many cars there are: it helps 1, 2 or 3 cars and hurts 4 to 7. Roughgarden and Tardos ("How bad is selfish routing?", later recognised with an IEEE Test of Time award) bounded the damage: for traffic that can be divided finely and travel times that grow linearly, the average time at equilibrium is at most 4/3 of the best possible average, in any network, and Pigou's two-road example (one road always 1 hour, one road taking x hours when a fraction x of traffic uses it) reaches 4/3 exactly; the continuous Braess network also has ratio 2 against 3/2. Proved: Braess's example, the 4/3 bound for divisible traffic with linear (affine) times, its tightness. Checked here: the floor-map equilibria for 1 to 8 cars, Braess's numbers 83 and 92 with whole travellers, and Pigou's 3/4. Limits: the 4/3 theorem is about finely divisible traffic; with a few whole cars equilibria can be several and the theorem does not apply as stated, so the floor-map ratios (8/7 for four cars) are computed directly, not taken from the theorem. Reports of real road closures that helped traffic are not part of this plan's checked mathematics.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Braess Paradox](https://supernet.isenberg.umass.edu/facts/braess.html). Ladimer S. Nagurney, Supernetworks Center, UMass Amherst. Braess (1968), *Unternehmensforschung* 12, 258–268, and the 2005 English translation in *Transportation Science*; the worked example with 6 travellers, link times 10f, f + 50, f + 50, 10f and the new link f + 10, giving 83 before and 92 after (read November 4, 2026).
- [Lecture 11: Selfish routing and the price of anarchy](https://www.timroughgarden.org/f13/l/l11.pdf). Tim Roughgarden, CS364A, Stanford, October 28, 2013. Braess's paradox with divisible traffic (3/2 before, 2 after), Pigou's example (1 against 3/4), and the 4/3 bound for affine cost functions (read November 4, 2026).
- [Tim Roughgarden and Éva Tardos: Test of Time Award](https://tc.computer.org/tcmf/?p=86). IEEE Computer Society Technical Committee on Mathematical Foundations of Computing. "How bad is selfish routing?" as a founding paper of algorithmic game theory; price of anarchy at most 4/3 for affine latencies, and tight (read November 4, 2026).
- Prior use with students: [Braess's Paradox teacher's guide](https://web.mit.edu/blossoms/sites/default/files/video/guide/Abuhlail-guide-English.pdf). Video lesson guide on the MIT BLOSSOMS site, for intermediate school students; the activities include distributing four cars over the routes before and after the new road, finding the equilibrium and the best total, and debating real cases (read November 4, 2026). No K–5 use was found (searched NRICH, JRMF and circle pages).

## A kid-friendly way in

The floor map. Masking tape on the floor makes a diamond: start S, towns A and B, finish E. Two roads are "crowded roads" (a sign shows a car; travel time = number of cars on it, counted with cubes stacked on the sign), and two are "long roads" (always 5 cubes). Each child drives a toy car and picks a route; times are added from the cubes on the signs. Then any one driver may switch if switching alone gives them a shorter trip; play stops when nobody wants to switch. Then an adult opens a free shortcut from A to B, and the room plays again. Prep: tape, two crowded-road signs and two long-road signs, a shortcut sign, toy cars, cubes, a trip card per child: about 20 minutes. Launch (2 to 3 minutes): four children drive while an adult stacks the cubes, showing how a crowded road's time grows with each car and how a trip time is added up; the room is asked to predict what the shortcut will do.

## By band

- **K–1:** four drivers on the floor map, cubes stacked by an adult; find the arrangement where nobody wants to switch (2 and 2, 7 minutes), then open the shortcut, watch everyone take it, and compare: 8 minutes. Spoken question: was the new road good for us?
- **2–3:** the question "Does a new road always help?" Play with 2, 3, 4 and 5 cars on a printed map with counters; record each settled arrangement and everyone's time before and after the shortcut. Discover that it helps 3 cars and hurts 4.
- **4–5:** explain why all four cars stay on the shortcut (leaving it costs 9) and why the 2 and 2 split is still best for the group (28 against 32 car-minutes). Then Braess's own numbers with 6 travellers (83 and 92), and Pigou's two roads: with half the traffic on each road the average is 3/4, but everyone chooses the crowded road and the average is 1. The guide can mention the 4/3 theorem as what mathematicians proved about how bad it can get.

## Checked facts

Computed in `check_games_3.py`, `check_week_181()`:

- floor map, 4 cars: before, the only settled split is 2 and 2 (7 minutes each); with the shortcut, the only settled arrangement is all 4 on it (8 each; a lone switcher to an old route would take 9); best total with the shortcut is 28 car-minutes, equilibrium 32, ratio 8/7;
- floor map, group totals before and after the shortcut for 1 to 8 cars: 6 → 2, 12 → 8, 20 → 18, 28 → 32, 38 → 42 to 50, 48 → 52 to 60, 60 → 62 to 70, 72 → 72 to 80 (several equilibria from 5 cars on);
- Braess's example with 6 whole travellers: before, only 3 and 3 at 83; after, only 2, 2, 2 at 92; the new path at the old traffic takes 70;
- Pigou: average 1 at equilibrium, 3/4 at best, ratio 4/3; continuous Braess 3/2 and 2.

Cited, not computed: the 4/3 theorem for all networks.

## Nearest existing themes

Atlas AP-23 (three travellers on two roads) already shows that a state where nobody wants to switch need not be cheapest for the group, and that is the core lesson of Pigou's example; Week 135 (trust game, draft) and Week 148 (two-thirds, draft) teach equilibria in other games. Week 13 (route packing) and Week 53 (cheapest networks) are network weeks without selfish drivers. New here: the paradox that adding capacity makes everyone worse off, a network map acted out with the children as drivers, and the dependence on the number of cars. Honest overlap: the Pigou part repeats AP-23's lesson; Braess's network and the count table are what justify a week.

## App connection

Games and choices, with a Maps and networks board. A "Rush hour" family: drag cars onto routes, road signs show times from current traffic, and a "settle" button lets unhappy cars switch one at a time. Example puzzles: "Find where the 4 cars settle"; "Add one road to this map that makes every driver slower"; "Close one road to make everyone faster". Fit B: needs an equilibrium finder (small enumeration) and a map editor.

## Open questions

- Floor space and flow: does acting out switching with 4 to 8 children stay orderly, or should most of the play move to table maps with counters after the launch?
- "Switch only if it helps you alone" must be enforced one driver at a time; the guide needs a turn rule.
- Several equilibria from 5 cars on may confuse 2–3; keep their exploration at 2 to 4 cars and give the larger counts to 4–5.
- The real-world examples (road closures that helped traffic) need a sourced reference before they appear in a guide.
