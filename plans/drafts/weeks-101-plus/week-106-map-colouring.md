# Week 106 (draft plan): Colouring maps

**Strand:** networks (Maps and networks). **Deep-math field:** graph theory and topology (planar colouring, surfaces). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Colour the countries of a map so that two countries sharing a border (more than a single point) differ. Three results frame the week. First, a map made entirely of whole straight lines across the page, or of whole circles, needs only two colours: colour a country by whether it lies on the positive side of (or inside) an even or odd number of the lines or circles; crossing one border changes that count by exactly one, so neighbours differ (proved; children can see it). Second, every map in the plane can be coloured with four colours. This is the four colour theorem, proved by Appel and Haken in 1976 with substantial computer checking and re-proved, also with a computer, by Robertson, Sanders, Seymour and Thomas (1997); four can be needed, for instance by a country surrounded by a ring of an odd number of countries (a ring of 5 round a middle country needs 4, a ring of 4 needs only 3, and an odd ring alone needs 3). Five colours are much easier: a counting argument from Euler's formula shows that every map has a country with at most five neighbours, and a careful recolouring argument then finishes; this is a standard textbook proof, not reproduced here. Third, on other surfaces the answer changes: on a torus seven colours always suffice and seven can be needed (Heawood 1890 for the bound and a seven-country map in which every country touches every other; Ringel and Youngs 1968 completed the general surface formula). The seven-country torus map is checked here as the dual of the seven-vertex triangulation with triangles {i, i+1, i+3} and {i, i+2, i+3} mod 7, which has 7 corners, 21 edges and 14 faces (Euler characteristic 0). Children can discover two-colouring for line and circle maps and explain it, find maps needing three and four, fail to find one needing five, and on a torus board see seven mutual neighbours.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Four-Colour Theorem](https://thomas.math.gatech.edu/PAP/fc.pdf) — Neil Robertson, Daniel Sanders, Paul Seymour, Robin Thomas, preprint dated February 1994, revised January 1997 (journal not named on the copy read). Statement, and the history of Appel and Haken's 1976 computer proof and why it was not fully accepted (read November 3, 2026).
- [Colouring the Torus](https://parabola.unsw.edu.au/sites/default/files/2024-03/vol35_no2_1.pdf) — John Steele, Parabola 35(2), 1999. Euler characteristic of the torus, Heawood's 1890 bound of 7, his seven-colour map, Ringel and Youngs 1968 (read November 3, 2026).
- Prior use with children: [Map Coloring Teaching Guide](https://jrmf.org/wp-content/uploads/Map-Coloring-Teaching-Guide.pdf) — Julia Robinson Mathematics Festival. Pairs colour US regional and Iowa county maps with as few colours as possible; odd cycles and wheels as reasons for more colours (read November 3, 2026).
- Prior use with children: [Map Coloring: From Checker Boards to Möbius Strips](https://webspace.ship.edu/lebryant/mathcircle/pdf/map-coloring.pdf) — math circle handout on a Shippensburg University site (no author named). Maps of whole lines across the page and the proof that two colours suffice; a six-region Möbius strip map needing six colours (read November 3, 2026).

## A kid-friendly way in

Scribble maps. Each child draws three or four long straight lines right across a sheet with a ruler (or three overlapping circles traced round cups) and colours the countries. Then printed maps: a middle country with a ring of 4 and with a ring of 5 neighbours, a regional map, and a blank square "portal board" (Week 41) for the torus. Prep: print four maps, gather crayons in five colours, rulers and cups; about 15 minutes. Launch (2–3 minutes): draw two crossing lines on the board, colour the four countries with two colours together, add a third line and ask whether two colours still work.

## By band

- **K–1:** line and circle scribble maps with two crayons; then colour the ring maps with as few crayons as possible and compare (ring of 4: three crayons; ring of 5: four).
- **2–3:** explain why any line or circle map works with two colours (count the lines you are above or the circles you are inside); find the fewest colours for printed maps; challenge: draw a map that needs five colours (nobody can, and adults know it is a theorem).
- **4–5:** explain the parity rule in words; find why a middle country with an odd ring needs four; on the portal board, where leaving one edge brings you back on the opposite edge, find seven countries that all touch each other (or colour a prepared seven-country torus map) and see that six colours fail.

## Checked facts

Computed in `check_counting_networks.py`, `check_week_106()`:

- a four-line map has 11 countries (1 + 4 + 6) and the "number of lines above" parity colours every neighbouring pair differently (checked on a grid of sample points); three overlapping circles make 8 regions including the outside;
- colours needed: middle country with a ring of 3, 4, 5, 6 needs 4, 3, 4, 3; a ring of 5 alone needs 3;
- E ≤ 3V − 6 gives a country (vertex) with at most five neighbours;
- the 7-vertex torus triangulation: 14 triangles, 21 edges each in two triangles, Euler characteristic 0, each vertex link a 6-cycle; Heawood numbers 4 (sphere) and 7 (torus).

Cited, not computed: the four colour theorem, Heawood's and Ringel–Youngs's results, the five-colour proof.

## Nearest existing themes

Week 62 (conflict networks and scheduling) colours networks to schedule activities, including odd cycles needing three; this week colours maps (the dual view) and adds the plane's four-colour limit and the torus. Week 16 uses three colours in Sperner's lemma; Week 40 colours knot diagrams; Week 56 proves Euler's formula; Week 41 builds the torus portal board. The scouting draft untangling-networks uses the same Euler-formula counting and draws K7 on a torus, so the torus station overlaps it; if both run, this week should come second. The original grades 2–3 plan already listed map colouring. New here: parity two-colouring of line and circle maps, a famous computer-assisted theorem, and the jump from 4 to 7 on a different surface.

## App connection

Maps and networks: a "map painter" family where the child taps countries to colour them and the app flags clashing neighbours; puzzles ask for the fewest colours, "this map is coloured with five: recolour with four", "add one country so the map needs four", or a torus map that wraps at the edges and needs seven. Week 62's colouring family could share the clash checker.

## Open questions

- A clean seven-country map drawn on Week 41's square portal board still needs to be made and checked by hand.
- Whether K–1 children draw lines fully across the page (a half line breaks the two-colour rule); prepared line maps may be safer.
- Whether this should be a Week 62 return visit instead of a new theme.
