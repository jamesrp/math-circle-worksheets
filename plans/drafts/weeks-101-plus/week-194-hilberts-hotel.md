# Week 194 (draft plan): The endless hotel and the strip nobody listed

**Strand:** logic (Codes and logic). **Deep-math field:** set theory, one-to-one matching, the diagonal argument. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Two collections have the same size when their members can be matched one to one with nobody left over. For endless collections this has surprising consequences, told as Hilbert's hotel (an infinite corridor of rooms 1, 2, 3, …, every room full). One more guest: everyone moves from room n to room n + 1, and room 1 is free. Endlessly many more guests: everyone moves from n to 2n, and all the odd rooms are free. So the counting numbers match the even numbers (n with 2n), and also all whole numbers, listed 0, 1, −1, 2, −2, …, and even all positive fractions, listed along the diagonals of a grid. A collection that can be put in one endless list is called countable. Cantor's diagonal theorem (G. Cantor, "Ueber eine elementare Frage der Mannigfaltigkeitslehre", 1890/91): the endless strips of two colours (red, blue, red, red, …) cannot all be put in one list. Given any list, build a new strip by looking down the diagonal: its first square is the opposite colour of the first strip's first square, its second is the opposite of the second strip's second square, and so on. The new strip differs from every listed strip somewhere, so it is missing from the list. Hence there are different sizes of infinity, and no infinite list holds every strip (proved). The same move proves that no list of k strips of length k contains them all (checked for k up to 4, where there are 2^k strips); for finite strips this is weak, since 2^k > k is obvious and all 8 three-square strips fit in a list of 8, but for endless strips the diagonal is the whole proof. The argument is constructive and local: it needs only one disagreement per row. Limits: the hotel stories assume rooms numbered by every counting number and moves done all at once; "same size" means a matching exists, not that a given matching works. Children can discover the room-moving tricks, that two endless rows can match even when one looks half as big, and the diagonal recipe that beats any list a partner writes.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Diagonaalargument en de Continuümhypothese](https://fa.ewi.tudelft.nl/~hart/onderwijs/HOVO/2024/20240424-diagonaal_en_CH.pdf) — K. P. Hart, TU Delft, lecture notes in Dutch, April 24, 2024 (read November 4, 2026). Cantor's 1890/91 paper "Ueber eine elementare Frage der Mannigfaltigkeitslehre" and its proof with sequences of two letters m and w, flipping the diagonal.
- [The Theory of Sets](https://mathcircle.berkeley.edu/sites/default/files/archivedocs/2013_2014/lecture/1314lecturespdf/BMC-Intermediate%20Nov.%2012th,%202013.pdf) — Alexander Givental, Berkeley Math Circle, Intermediate, November 12, 2013 (read November 4, 2026). Hilbert's hotel (1 + ∞ = ∞), matching sets to compare size, fractions against counting numbers, and the diagonal argument for the continuum, as a circle handout.
- [Hilbert's Hotel](https://nrich.maths.org/articles/hilberts-hotel) — Robert Crowston, NRICH, 2011, ages 14 to 18 (read November 4, 2026). One more guest by moving to the next room; infinitely many by moving to twice the room number.
- Prior use with children: [The Infinite Hotel](https://www.macmillan-academy.org.uk/scholar-lab/activities/infinite-hotel.html) — The Scholar Lab, Macmillan Academy, Key Stage 3 (read November 4, 2026): students write and justify room-moving methods for one more guest, infinitely many guests and infinitely many coaches, and are pointed to the diagonal argument. Givental's handout above is the other circle use. No K–5 use was found (searched "Hilbert hotel infinity lesson elementary students Cantor diagonal math circle").

## A kid-friendly way in

A corridor of numbered doors and a strip-making challenge. The corridor: a long paper strip of numbered "rooms" taped along a wall, running off the end with "and so on", and a cup of guest tokens; an adult tells the "every room is full" story and children act out the moves ("everyone, step to the next door") with tokens. The strips: square counters, red one side and blue the other, laid in rows of four on a 4-by-4 mat. One child lays a list of four rows; the partner must build a row that is not on the list, and then a method that always works. Prep: a numbered door strip, a 4-by-4 mat and 20 two-colour counters per pair (Week 6 or Week 18's counters); about 15 minutes. Launch (3 minutes): six children are guests on six chairs labelled 1 to 6 "and the rest of the endless hall"; a new guest arrives, and the room finds the "everyone moves up" trick.

## By band

- **K–1:** The diagonal game with three rows of three counters: the adult lays three rows; the child makes a row that is not there, by making its first square differ from row 1's first, its second from row 2's second, its third from row 3's third (colour stickers mark the diagonal). Matching game: pair cubes with cubes by laying them side by side. Almost no reading.
- **2–3:** Room puzzles: one more guest, two more, a bus of endlessly many (move to 2n). Is there "the same number" of even numbers and counting numbers? Then the four-row strip challenge: find a method that beats any list your partner makes, and test it on several lists.
- **4–5:** Explain why the diagonal row cannot be on the list, even an endless one. Contrast: whole numbers and fractions can be listed (find the listing); endless strips cannot. What would go wrong if someone claimed a complete list of strips? Why is the finite version weak (8 three-square strips do fit in a list of 8)?

## Checked facts

All in `check_logic_3.py`, function `check_week_194()`:
- n → n + 1 leaves room 1 empty and n → 2n gives distinct even rooms (checked to 1000).
- The zigzag 0, 1, −1, 2, −2, … lists each whole number from −50 to 50 once.
- For every list of k strips of length k (k = 1 to 4), the flipped diagonal differs from every row, at the diagonal place; 2^k > k.
- Three-square strips: 8 in all; a list of 3 misses at least 5; a list of 8 can hold every one.
- Listing fractions p/q along the grid's diagonals (p, q ≤ 6, lowest terms) gives each value once.
- Cited, not computed: Cantor's theorem for endless strips and its 1890/91 source (Hart; Givental).

## Nearest existing themes

This topic substantially overlaps two existing items. Atlas family AD-02 is the diagonal argument with four counters ("build a pattern that differs from every row, and find a method that beats any list a partner writes"), the same activity proposed here for 2–3; it has no K–1 entry and is in the path's left-out list. Week 82 (Endless class lines) already matches endless lines kid for kid, with the star in front absorbed (1 + ω = ω, the hotel's one more guest) and an endless row of pairs matched to one row (the move to 2n). The catalog's concept "diagonal-argument" has no week, only AD-02. The distinct angle proposed: a week that is the full-band home for AD-02, adding the K–1 three-by-three diagonal game and the contrast "these endless collections can be listed, these cannot", with the hotel only as a short bridge from Week 82 (or as a Week 82 return visit if Week 82 runs first). Draft Week 138 (busy beaver) notes that Turing's halting proof is a diagonal argument, a possible 4–5 link. Week 80 (Midnight laboratory) and draft Week 141 handle other endless processes. New against all of these: uncountability itself, with a K–1 entry.

## App connection

Codes and logic region, possible family "Not on the list": the app shows a list of colour strips (growing to endless with "and so on" fades), and the child builds a strip that is not on it; the app highlights the diagonal squares after a correct build. Puzzles: "Make a strip that is not on this list of 3"; "Your strip must differ from row 5 at square 5"; and a hotel level where the child drags all guests at once with a rule (next room, double the room) to free rooms. Week 82's line art could carry the hotel level.

## Open questions

- Is "endless" meaningful to K–1, or should the K–1 entry stay finite (the 3-by-3 diagonal game) with no infinity at all? The plan assumes the latter.
- AD-02's existing pages may already serve 2–3 and 4–5; decide whether to reuse them and write only a K–1 page and the facilitator overview.
- The weak finite version (all 8 strips fit in a list of 8) may confuse children who just "won" with the diagonal; the guide should say when the diagonal really matters.
- Schedule after Week 82 so that matching is familiar.
