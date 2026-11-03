# Week 112 (draft plan): Spreading claps around a circle

**Strand:** number (Numbers). **Deep-math field:** number theory, discrete geometry, combinatorics on words. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Place k claps on a circle of n equally spaced beats "as evenly as possible". Godfried Toussaint (Bridges, 2005) observed that Bjorklund's algorithm, written for timing pulses in a neutron accelerator, has the structure of Euclid's gcd algorithm and produces rhythms E(k, n) found in music worldwide: E(3, 8) = x..x..x. is the Cuban tresillo, E(5, 8) = x.xx.xx. the cinquillo. Demaine, Gomez-Martin, Meijer, Rappaport, Taslakian, Toussaint, Winograd and Wood (Computational Geometry, 2009) proved that several definitions agree up to rotation: maximising the sum of all pairwise chord lengths between claps, Bjorklund's construction, and a spacing condition; and that up to rotation the answer is unique. A simple formula gives a representative: clap at beats ⌊i·n/k⌋ for i = 0, …, k − 1. Three facts children can check with their bodies: next-clap gaps take only the two values ⌊n/k⌋ and ⌈n/k⌉; swapping claps and rests turns E(k, n) into E(n − k, n) (the tresillo's rests, rotated, are the cinquillo); and if d = gcd(k, n) > 1 the rhythm is d copies of E(k/d, n/d), so 4 claps in 12 is x.. repeated four times. A caution worth discovering: gaps alone do not settle it, because x.xxx. and xx.xx. both use gaps 1 and 2, yet only the second is evenly spread; the full condition also asks each clap's second-next, third-next, … clap to sit at the evened-out distance. These facts are proved in the cited paper and confirmed here by exhaustive check for n ≤ 12. Nothing here is open; the musicological claim that such rhythms are common is an observation, not a theorem.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Euclidean Algorithm Generates Traditional Musical Rhythms](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf) — Godfried Toussaint, McGill University (Bridges conference paper; the PDF does not print the year). Bjorklund and Euclid, E(3,8) tresillo, E(5,8) cinquillo, E(2,5), E(3,4), E(5,12), and rhythms as necklaces under rotation (read November 3, 2026).
- [The distance geometry of music](https://users.monash.edu/~davidwo/papers/Demaine-etal-Rhythm-CGTA.pdf) — Demaine et al., Computational Geometry: Theory and Applications 42 (2009). Theorem 4.1 (equivalent definitions, unique up to rotation) and Theorem 4.5 (uniqueness proof split by gcd) (read November 3, 2026).
- Prior use with children: none found for Euclidean rhythms as such. Searched "Euclidean rhythms classroom activity children drumming circle math". Closest: [Phil Tulga, Musical Math](https://www.philtulga.com/MusicalMath.html), school assemblies and workshops where students clap world drum rhythms and read patterns with Unifix cubes (read November 3, 2026). A book chapter, [Muthsics for clueless: An experiment with euclidean rhythms](https://observatorio-investigacion.unavarra.es/documentos/6173e7441c8ff27873b93f12) (Wilhelmi and Montiel, 2018), describes an experiment whose audience the page does not state (read November 3, 2026).

## A kid-friendly way in

A ring of 8 paper plates (later 12) on the floor, numbered around. Children stand at plates; a leader walks or taps around the ring at a steady pulse, and a child on a "clap plate" claps when the pulse arrives. The task: put 3 cups on 8 plates so the claps sound as evenly spread as possible, then play it. Drumming on upturned cups at tables (cup-on plate means hit, empty means rest) works as a seated version. Recording is a strip of 8 squares with x for a clap and a dot for a rest. Prep: 12 paper plates, a dozen cups, printed strips; under 15 minutes. Launch (2–3 minutes): everyone claps a steady 8 with the leader, then the leader places 2 cups opposite each other and the group plays it; ask tables to do the same with 3 cups.

## By band

- **K–1:** play 2, 3 and 4 claps on 8 plates and on 12; hear which feel even; copy a tapped rhythm onto cups.
- **2–3:** 3 claps on 8: how many really different rhythms are there if turning the ring does not count? (7; 5 if flipping it over also does not count.) Which one is most even? Then 5 claps on 8 and the surprise that its rests are the 3-clap rhythm.
- **4–5:** find the most even k on n for several pairs; compare the gap lists; explain why 4 on 12 repeats and 5 on 12 does not; test whether "only two gap sizes" is enough (x.xxx. versus xx.xx.).

## Checked facts

Computed in `check_number.py`, `check_week_112()`:

- the floor formula gives rotations of x..x..x. (E(3,8)), x.xx.xx. (E(5,8)), x.x.. (E(2,5)), x.xx (E(3,4)), x..x.x..x.x. (E(5,12)); E(4,12) = x..x..x..x..;
- for every n ≤ 12 and k ≤ n: the patterns meeting the full spacing condition are exactly the rotations of E(k, n); for k ≥ 2 the patterns of greatest chord-length sum are exactly the same set; swapping claps and rests gives E(n − k, n); a common factor d repeats E(k/d, n/d) d times;
- gaps alone are not enough: x.xxx. has gaps 2, 1, 1, 2 but fails the spacing condition, while xx.xx. passes;
- 3 claps on 8 beats: 56 patterns, 7 up to rotation, 5 up to rotation and flipping; E(5,12) gaps are 2, 2, 2, 3, 3; E(7,12) gaps are 1, 1, 2, 2, 2, 2, 2.

## Nearest existing themes

Week 4 (stars and wheels) hops a fixed step around n dots and meets gcd(n, k); Week 33 (prime-length necklaces) counts rings up to rotation. This week uses the same circle and the same "up to rotation" idea but asks a different question: the most even placement of k marks, its uniqueness, and its link to Euclid's algorithm. Week 32 (squares inside rectangles) is the geometric face of the same Euclidean algorithm, and Week 91 (rotor-router machines) has alternating switches that split visits as evenly as possible, which is a close cousin worth pointing out in the guide. New here: rhythm and sound as the representation, maximal evenness as an optimisation with a unique answer, and complements.

## App connection

Numbers region, or Patterns and symmetry if the app treats rings there: a "rhythm ring" family where the child toggles beats on a circle, hears the loop, and must hit a target (k claps, most even, or "match this rhythm up to rotation"). Example puzzles: "place 5 claps on 12 so no two gaps differ by more than 1, and every pair is as far apart as possible"; "find the rhythm whose rests sound like the tresillo".

## Open questions

- Whether children's sense of "even" from listening matches the mathematical one; a home pilot with real cups would show it. Untested.
- Noise and space: a ring of plates needs floor room; the seated cup version may be the realistic default.
- The Toussaint paper is dated 2005 here, but the PDF read does not print its year (it cites Bridges papers up to 2004); confirm from the Bridges archive before a guide.
