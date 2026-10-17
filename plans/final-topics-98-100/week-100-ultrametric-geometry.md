# Week 100 Distance in nested worlds

Planning proposal, October 17, 2026. Children build and reconstruct a geometry in which closeness comes from nested groups rather than ruler length or road length. This supplies an accessible entrance to ultrametric spaces, hierarchical clustering and, as a later connection, 2-adic distance.

## Mathematical destination before solutions

Take a finite collection of distinct object cards. Put them in a hierarchy of groups: any two groups are disjoint or one contains the other, there is an outer group containing every card, and every card has its own singleton group. Give nonsingleton groups positive height labels that strictly increase on going outward. The distance between two different cards is the label of the smallest group containing both; a card has distance zero from itself. The proposed kits use labels 2,4,8; those are distances, not counts of cards or physical ring diameters. A group may have three children rather than two.

**This distance obeys the strong triangle inequality:** d(A,C)≤max(d(A,B),d(B,C)). The smallest groups containing AB and BC both contain B, so one contains the other. The larger contains A and C. In any triple, therefore, the largest distance occurs at least twice. Distances 2,4,4 work; 2,2,4 do not. Equilateral triples are allowed when a group has three children; a binary-only example must not become a false universal claim.

**Balls are nested or disjoint, and every member is a center.** Define the radius-r ball about A to be all cards at distance at most r from A, including A. If B is in that ball, the strong inequality makes the radius-r ball about B identical. If balls of radii r≤s share a member, the smaller lies in the larger. In the kit these balls are visible groups, including singletons; the same argument works for arbitrary ultrametrics. “Center” means specifying the distance test, not the geometric middle of a drawn oval.

**Distance data reconstruct the grouping at every threshold.** “Distance at most r” is an equivalence relation: transitivity follows from the strong inequality. Increasing r merges its classes. Thus valid complete distance data recover the nested groups and their merger heights. Drawing left/right order or rotating rings does not change the geometry. Arbitrary distance tables need not satisfy this rule; an inconsistent triple is a checkable obstruction.

**A genuine number-theoretic continuation.** For distinct integers a,b, write a−b = 2^v times an odd integer. The 2-adic distance is 2^(−v), with d(a,a)=0. On cards 0,…,7 use scaled distances 8·2^(−v): different parity gives 8, difference divisible by 2 but not 4 gives 4, and difference 4 gives 2. Congruence groups modulo 2,4,8 make the nesting tangible. If 2^k divides both a−b and b−c, it divides a−c, giving the strong inequality. This is a finite subset of the integer 2-adic metric, not the construction of the completed number field. No infinite digit strings or exponent arithmetic are needed for entry.

Recommended grades 3–5: comparing labels, retaining an unfamiliar distance definition, and using three pairwise relations. A ready second grader may use the object-and-ring route with oral instructions. Number cards need parity and grouping by remainders; adults can supply pregrouped cards. No K–1 packet is proposed. Experiments suggest the triangle and ball rules; nested containment explains why they always hold.

## Materials and complete opening

Per pair: six object cards A–F, washable marker, movable paper frames or cord loops, labels 2,4,8, and three distance cards for a triple. Use letters plus distinct pictures/shapes if reading requires support. Draw one outer frame on a landscape sheet and movable interior frames; allow roughly 250 by 180 mm for a six-card hierarchy. Use at least 25 mm cards and keep group labels beside their frame. Do not use physically nested opaque cups, which hide memberships. The upper trio rotates builder, clue reader and checker. Three older-table kits plus a demonstration board should take about 20 minutes to prepare by hand, subject to rehearsal.

Let children try grouping the cards. Then demonstrate on unrelated cards X,Y,Z:

```text
Input: outer group 6 [ inner group 3 [ X Y ]   Z ]
Middle: point to X and Z; group 3 contains only X, group 6 contains both.
Output: distance X–Z = 6. Sliding X across the page within its group changes nothing.
```

Separately read X–Y=3, to show that the smallest common group matters. Show one complete ball query before P2: choose X and radius 3; Y passes the test, Z fails, and X is included because its self-distance is zero; output `{X,Y}`. This example establishes the unusual convention without giving the later target grouping or triangle obstruction.

Shared rules: groups must be nested or separate; outward labels increase; distance is the smallest common group's label; self-distance is zero. Allow groups with more than two subgroups. “Within r” always means at most r.

## Five substantial investigations

1. **Build a grouped world containing three cards with pair distances 2,4,4. Can you build one with 2,2,4? What about 4,4,4?** Supply movable cards and three pair-label strips. For 2,4,4, put A,B together at 2 inside a group with C at 4. For 2,2,4, two radius-2 relations force all three into one radius-2 class, contradicting distance 4. For 4,4,4, put three separate cards directly inside one group labeled 4. Children can then invent a triple for a partner to build or reject. Keep the search open; don't announce “all triangles are isosceles” beforehand.
2. **Find all cards within distance 4 of A in your world. Which other cards can replace A and give exactly the same collection? Can two balls share a card without one containing the other?** Begin with the successful hierarchy from P1, then provide the five-card world below and frames for radius 2,4,8. A ball is a collection of cards selected by the stated distance test, not an arbitrary oval. Children should physically place the returned collections before discussing the claim. A partner may choose centers and radii; no full 25-entry distance table is needed.
3. **Rebuild this hidden five-card world from its distance clues. Could a different drawing give the same distances?** Supply ten movable pair cards: AB=2; AC=BC=4; DE=2; and AD=AE=BD=BE=CD=CE=8. The groups are AB at 2, ABC at 4, DE at 2, and ABCDE at 8. The hierarchy is determined at these levels, while positions and left/right order are not. Children can organize the cards as they choose. An adult can initially offer the three AB/AC/BC cards, adding the others only after the first grouping is understood; that is optional pacing, not a forced student recipe.
4. **One distance clue in a copy of that world has changed: AC now says 2, while all nine other clues remain unchanged. Can the whole collection still be built? Repair it by changing one clue.** The triangle ABC now has 2,2,4, so it fails. Changing AC back to 4 works; changing BC to 2 also works, making ABC a three-child group at 2. Changing AB to 4 works too: AC form the close pair and B joins at 4. All three repairs preserve every other clue; therefore the data alone do not identify which measurement was wrong. Restrict repaired distances to 2,4,8. Other one-clue repairs cannot remove the inconsistent ABC triple. This is an inverse-geometry problem, not an arbitrary logic puzzle.
5. **Build a number world with cards 0–7. Two different cards are distance 8 if one is odd and one even, distance 4 if they have the same parity but different remainders on division by 4, and distance 2 if their difference is 4. Which cards are closest to 0? Find a pair far apart on the number line but close here.** Start by physically grouping even/odd cards, then the same-remainder pairs; use counters in groups of four if needed. Provide a separate worked conversion first: for cards 1 and 5, both are odd and leave remainder 1 on division by 4, so their group has label 2 and their distance is 2. The grouping is not a demand to recompute every pair's distance. The balls around 0 at radii 2,4,8 are `{0,4}`, `{0,2,4,6}`, and all eight cards. Cards 0 and 4 are closer than 0 and 1. This is an optional later visit; the object geometry is complete without it.

## Checked small example and explanation

The five-card hierarchy in P3 has distance matrix:

| | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 2 | 4 | 8 | 8 |
| B | 2 | 0 | 4 | 8 | 8 |
| C | 4 | 4 | 0 | 8 | 8 |
| D | 8 | 8 | 8 | 0 | 2 |
| E | 8 | 8 | 8 | 2 | 0 |

Radius-4 balls about A, B and C all equal ABC. A radius-2 ball about C is the singleton C, since no other card is within 2. Thus the supplied radius need not appear as a group's label for that center. The three-card check covers all choices and the nested-group proof explains the general case. The eight-number model has 15 distinct balls: eight singletons, four pairs, two parity classes and the whole set. The code checks all 512 ordered triples and every pair of these balls. It also checks all three repairs in P4.

## Plausible sequence and limits

Movement, material play and the brief convention launch take about 10 minutes. Spend 15–20 minutes building and rejecting triples, then 15–20 minutes on balls or hidden-world reconstruction. Save repair and number geometry for a return visit. An adult may read clues and record the children's grouping. If the adult must continually decide which common group determines a distance, postpone inverse reconstruction and stay with visible group comparisons. No assumption of advanced reading or formal proof follows from mathematical giftedness.

Oleksiy Dovgoshey, [*Finite Ultrametric Balls*](https://arxiv.org/html/1810.03128v2), §1, Proposition 1.2 and Proposition 1.5, gives the center and nesting facts. Theorem 3.15 characterizes which finite set-families can be all ultrametric balls: they contain the whole set and singletons, and intersecting members are nested. The activity is an elementary finite specialization; its chosen cards, examples and investigations are original planning choices. The 2-adic divisibility argument above is supplied directly; it does not rely on the research paper to develop p-adic arithmetic.

Weeks 67 and 69 use shortest-road distance and tree geodesics; their tree triangles form tripods, but arbitrary tree vertices do **not** obey the ultrametric inequality. Three consecutive road vertices have distances 1,1,2. Here only object leaves are points and distance is a merger height, not a count of roads. Week 68 studies how deletion separates infinite ends; no end classification is repeated. Week 77 tracks loops under filling, not clusters or ultrametric balls. Week 96 uses prime-factor sub-bags, and Week 97 uses collisions of squaring modulo a modulus; P5 uses agreement modulo successively higher powers to define distance. Reserved Week 91 has a binary routing tree and deterministic balance, neither of which is this metric. The object route deliberately allows nonbinary branching to make that distinction visible.
