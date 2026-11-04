# Week 161 (draft plan): Flexagons

**Strand:** symmetry (Patterns and symmetry). **Deep-math field:** combinatorics of folding, state graphs, Möbius bands. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A hexaflexagon is a strip of equilateral triangles folded flat into a hexagon of six "pats"; pinching three corners together and opening the centre (the pinch flex) turns it inside out and shows a face that was hidden. The trihexaflexagon (Arthur Stone, Princeton, 1939) folds from a strip of 10 triangles, one a glue tab, and shows three faces; the hexahexaflexagon folds from 19 and shows six. The counts are bookkeeping children can check: a face is six triangle sides, so three faces need 18 sides on 9 triangles and six faces need 36 sides on 18. The structure is a state graph. A state is the pair of faces showing (top and bottom), and a flex moves to a neighbouring state. Tuckerman's picture of this graph is a tree of triangles whose corners are the faces and whose edges are the states, a flex moving round one triangle. For the trihexaflexagon it is a single triangle: three states, each face in two of them. For the hexahexaflexagon a model consistent with the published facts is a central triangle (faces 1, 2, 3) with one triangle on each side bringing in faces 4, 5 and 6: it has 9 states, faces 1, 2, 3 lie in three triangles each and faces 4, 5, 6 in one, matching Gardner's report that the first three appear three times as often, and the Tuckerman traverse (keep flexing at one corner until it will not open, then move one corner) cycles through all six faces in 12 flexes. Anderson, McLean, Pajoohesh and Smith (2010) proved that with pinch flexes an order-3n hexaflexagon (9n triangles, 3n colour faces) is a Möbius band with 6n − 3 "mathematical faces" (states), 3 for the trihexa and 9 for the hexahexa, and counted faces under McLean's V-flex too: 3420 for the hexahexaflexagon. Tukey and Feynman worked out a full theory in 1940 that was never published. Proved: the 6n − 3 count and the V-flex counts (in the papers cited). Checked here: the triangle bookkeeping and the 9-state model's counts. Children can discover the hidden faces, draw the face map, and notice that some faces are hard to reach.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Flexagons](https://www.scientificamerican.com/article/flexagons/) — Scientific American 195(6), December 1956 (the page names Bunji Tagawa as illustrator; its editor's note says the article inspired the Mathematical Games column). Stone's 1939 discovery; the 10- and 19-triangle strips; the flexagon committee (Stone, Tuckerman, Feynman, Tukey); the Tuckerman traverse cycling all six faces in 12 flexes; faces 1, 2, 3 three times as frequent as 4, 5, 6 (read November 4, 2026).
- [The combinatorics of all regular flexagons](https://scholars.georgiasouthern.edu/en/publications/the-combinatorics-of-all-regular-flexagons-5/) — Thomas Anderson, T. Bruce McLean, Homeira Pajoohesh and Chasen Smith, European Journal of Combinatorics 31 (2010), 72–80. Order-3n flexagons from 9n triangles; Möbius band with 6n − 3 faces under pinch flexes; 3420 faces for order 6 with the V-flex (read November 4, 2026).
- [The V-Flex, Triangle Orientation and Catalan Numbers in Hexaflexagons](https://digitalcommons.georgiasouthern.edu/math-sci-facpubs/62) — Ionut Iacob, T. Bruce McLean and Hua Wang, College Mathematics Journal 43 (2012), 6–10. Hexahexaflexagon: 9 faces by pinch flex, 3420 with the V-flex (read November 4, 2026).
- Prior use with children: [Hexaflexagons activity leader guide](https://jrmf.org/wp-content/uploads/Hexaflexagons-Festival-Guide.pdf) — hosted on jrmf.org (the PDF does not name the organisation). Make a hexahexaflexagon; find every face; how many flexes from one face to all others; draw how the faces connect; younger children need help cutting and folding (read November 4, 2026). Also [Flexagons](https://mathcircle.berkeley.edu/sites/default/files/handouts/2023/230428_flexagons_handout%20%281%29_0.pdf) — Chris Overton, Berkeley Math Circle Intermediate 2, April 2023: why six faces, which face can follow which, Tuckerman's and others' graphs, and for which n an n-face hexaflexagon exists (read November 4, 2026).

## A kid-friendly way in

Fold a trihexaflexagon from a printed strip of 10 triangles (crease lines and numbers printed, glue tab shaded), with one adult per table helping the final fold and tape. Children colour or sticker each face as they find it (three colours on a trihexa), then draw a "face map": a dot for each colour and an arrow for each flex. Pre-folded spares let anyone who struggles with folding start flexing at once. Prep: print trihexa strips on card (two per child) and hexahexa strips for grades 4–5, fold six spares, scissors, glue sticks or tape, stickers in six colours; about 25 minutes including folding spares. Launch (2–3 minutes): hold up a pre-folded trihexaflexagon showing yellow, ask what is on the back, then pinch and open it to show a third colour; show the pinch slowly twice so everyone sees where the fingers go.

## By band

- **K–1:** flex a pre-folded trihexaflexagon (or one folded with an adult), put a sticker of a new colour on each new face, and find out how many colours it has; is any face hiding?
- **2–3:** fold a trihexaflexagon, colour each face, and draw the face map; then a hexahexaflexagon from a pre-folded spiral (an adult does the rolling step): find all six faces and record which faces were easy and which were rare.
- **4–5:** fold the hexahexaflexagon, run the Tuckerman traverse and count flexes until the start returns; draw the triangle map with faces at corners and states as edges; explain from it why faces 4, 5, 6 are rare and why 6 faces need 18 triangles. Notice that a face's picture comes back rotated or scrambled (the triangle orientation question).

## Checked facts

Computed in `check_number_symmetry_2.py`, `check_week_161()`:

- 3 faces × 6 triangles = 18 = 9 triangles × 2 sides (10 with the tab); 6 × 6 = 36 = 18 × 2 (19 with the tab);
- 6n − 3 gives 3 and 9 states for n = 1 and 2;
- the four-triangle model of the hexahexaflexagon has 9 edges (states); faces 1, 2, 3 lie in three triangles and 4, 5, 6 in one; no state shows two of faces 4, 5, 6 together; the one-triangle trihexa model has 3 states, each face in two.

The 12-flex traverse, the 3420 V-flex count and the Möbius-band statement are cited, not computed. The four-triangle model is my reconstruction from those facts and must be checked on a real flexagon.

## Nearest existing themes

The Hex scouting draft cites Gardner's Hexaflexagons book only for the game of Hex; no week or atlas family builds a flexagon. Week 3 (shuffle machines) and Week 103 draft (tower maps) also draw state maps and loops, which is the shared reasoning move; here the states are physical and partly hidden. Week 124 draft (fold and cut) is the other folding week, about creases rather than state. New: a Möbius band children make and use, and a face graph read off a toy.

## App connection

Patterns and symmetry region, a "flexagon" family: an animated hexagon with a pinch button at each corner; the child flexes and the board records the face map; puzzles: "reach the purple face in the fewest flexes", "which face can never be on top while orange is on the bottom?", "draw the map before you flex, then check". Art: a flex animation brief for Dot/Codex.

## Open questions

- Folding the hexahexaflexagon is a known stumbling point (the JRMF guide warns younger children need help); rehearse the strip and timing before choosing it for grades 2–3.
- Confirm the four-triangle face map and the 12-flex traverse on a physical hexahexaflexagon, and decide whether the guide should present the model as a discovery or a checked result.
- Whether the Scientific American 1956 article is Gardner's own text: the page read does not name an author.
