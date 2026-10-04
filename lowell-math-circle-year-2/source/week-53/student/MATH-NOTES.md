# Mathematical check notes

These notes record the mathematical destination and finite verification. They contain no pacing, hints or facilitator script. The finite checks are reproducible with `verify_math.py`; testing printed examples is not proof of an arbitrary-map claim.

Assumptions throughout the optimization questions: a finite connected undirected available graph, whole links and fixed vertices, positive purchase prices, one payment per purchased link. No unprinted links, partial purchases or new junctions. Zero or negative prices require additional qualifications: a cheapest connected purchase may then include a zero-cost or profitable loop. The printed tasks do not use those prices.

| Problem | Checked result or witness |
|---|---|
| 1 | Left minimum 3, unique AB/BC. Right minimum 3, two optima AB/BC and AB/AC. |
| 2 | Minimum 4; CD plus any two of AB, BC, AC: three optima. |
| 3 | Minimum 7, unique AB/BC/CD. AB/BC/AC cost 6 but leave D isolated. |
| 4 | Minimum 6; CD and DE plus any two of AB, BC, AC: three optima. |
| 5 | Left cost 10. Improving single swaps: return AD/buy CD →9; return AC/buy BC →7; return AC/buy CD →8. Right cost 6 has no improving single swap. |
| 6 | Minimum 8, unique AB/BC/CD/DE/EF. These five links are mandatory; AC, DF, BD and CE are in no optimum. |
| 7 | In edge order AB,BC,AC,AD,BD,CD: prices 1,1,3,2,3,4 give unique cost-4 optimum AB/BC/AD. Prices 1,2,2,1,4,4 give two cost-4 optima AB/AD/BC and AB/AD/AC. Both use repeated prices in {1,2,3,4}. All 4,096 assignments have been independently checked: 1,956 give a unique optimum and 2,140 give multiple optima. |
| 8 | Top cost 8 is optimum. Bottom cost 14 is not. Exactly four improving swaps: AC→BC gives 13, AC→CD gives 13, BD→CD gives 11, DF→EF gives 12. General conclusions: positive-cost loops are never cheapest; a connected loop-free purchase without an improving single swap is cheapest. |
| 9 | Printed optimum AB/BC/CD costs 6. Distinct prices guarantee uniqueness on any connected available graph, rather than merely on the printed map. |

In Problem 6 the mandatory links have actual unique-cheapest cut evidence: cuts {A}, {A,B}, {A,B,C}, {E}, {F} certify AB, BC, CD, DE, EF respectively. Strictly heaviest edges of actual cycles certify the excluded links: ABC excludes AC=3; DEF excludes DF=4; BCD excludes BD=5; CDE excludes CE=6. Repeated prices occur on this map without producing several optima. CD=2 is forced by its price; it is not a graph bridge. BD and CE bypass C and D respectively, so deleting any single available link leaves this graph connected. The cuts/cycles are evidence available to a later guide, not printed methods for the child.

## General argument audit

A bought loop gives an alternative connection between the endpoints of each of its links. Removing one link leaves all places connected and refunds a positive price, so a cheapest connected purchase has no loop. This conclusion uses positivity. Such a connected acyclic purchase is a spanning tree; its n−1 link count is a consequence, not the target or a sufficient connection/optimality test.

A one-link swap starts from one unchanged purchase, buys one unused available link and returns one bought link; its resulting purchase must connect every place. “Cheaper” means a strictly lower total price.

For a tree T, adding an unused edge f creates one loop. An improving single swap exists exactly when f is cheaper than some edge on T's path between its endpoints. Thus “no improving swap” means every unused edge's price is at least the maximum price on its T-path. To prove sufficiency, delete any edge e of T. For the resulting two sides, every other available crossing edge f costs at least e, because e belongs to f's T-path. Given any competing tree missing e, add e and remove an edge f crossing those sides from the new loop. The removed edge is outside T; this changes the competing tree toward T without increasing cost. Repeat to transform any competing tree into T. Any connected competing purchase can first have loops removed. The loop-free condition is essential: buying all three price-1 links of a triangle has no unused link and hence no one-for-one improving swap, but costs 3 while a tree costs 2. This proves the arbitrary-map answer in Problem 8, rather than inferring it from the two test cases.

For distinct prices, suppose optimum trees T1 and T2 differ. Let e be the cheapest edge in their symmetric difference, with e in T1. Add e to T2. Its loop contains an edge f in T2 but outside T1, since otherwise T1 would already have a loop. Distinct prices give price(e)<price(f), so replacing f makes T2 cheaper, a contradiction. Ties destroy this strict comparison and may allow several optima, but do not require them, as Problems 1, 6 and 7 show.

The general facts are established minimum-spanning-tree mathematics; no claim of novel mathematics is made. See exact mathematical and teaching source references in `PROVENANCE.md`.

## Independent review evidence

Fresh adversarial and mathematics reviewers inspected all nine draft pages. The math reviewer independently transcribed all fixed graphs and reconstructed every one of the 27 actual-PDF graph instances; it did not import writer data or checkers. Its full inverse multiplicity distribution was 1:1956, 2:936, 3:768, 4:144, 5:96, 6:96, 8:72, 9:24, 16:4. All 152 spanning trees across the ten fixed weighted graph types obeyed the path certificate and local/global criterion. These finite checks support the printed examples; the arguments above establish the arbitrary-map facts. The revision repeats actual-final-PDF checks and independently reruns the reviewer's audit. These notes are mathematical verification, not a facilitator guide or physical/classroom validation.
