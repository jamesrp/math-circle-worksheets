# Week 199 (draft plan): Steering a card with perfect shuffles

**Strand:** symmetry and number (Patterns and symmetry). **Deep-math field:** group theory and number theory (permutation groups, multiplicative order, binary). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A perfect (faro) shuffle cuts a deck of 2n cards exactly in half and interleaves the halves one card at a time. In the out-shuffle the top card stays on top; in the in-shuffle the top card goes second. Number the places 0 to 2n − 1 from the top. The out-shuffle sends place i to 2i (mod 2n − 1, with the bottom card fixed), so it restores the deck after the multiplicative order of 2 modulo 2n − 1: 8 shuffles for 52 cards (2⁸ = 256 = 5 × 51 + 1), 21 for 50 and 52 for 54. The in-shuffle sends i to 2i + 1 (mod 2n + 1), so its order is the order of 2 modulo 2n + 1: 52 for 52 cards, and 26 in-shuffles turn the deck upside down. Diaconis, Graham and Kantor (Advances in Applied Mathematics, 1983) proved these and two deeper facts. First, Elmsley's rule (Alex Elmsley, 1957): to send the top card to place k, write k in binary and, reading left to right, do an in-shuffle for each 1 and an out-shuffle for each 0, because an out-shuffle doubles a top-half card's place and an in-shuffle doubles it and adds one. Second, they found the whole group the two shuffles generate. Both shuffles keep mirror partners together (the cards in places i and 2n − 1 − i end in mirror places), so at most n!·2ⁿ orders can ever be reached. For 52 cards that bound is met (the group is the full mirror-respecting group, of order 26!·2²⁶); for decks of 2^k cards the two shuffles reach only k·2^k orders (8 cards: 24 of 40320); and two decks are exceptional: 12 cards, where the group involves PGL(2, 5), the same small exceptional group that draft 117's turning squares produce, and 24 cards, where it involves the Mathieu group M₁₂. Proved: everything stated (DGK). Checked here: the orders, Elmsley's rule for every place in 8-, 16- and 52-card decks, the mirror rule, and the number of reachable orders for every even deck from 2 to 16 cards (2, 8, 24, 24, 1920, 7680, 322560, 64). Children can discover that two shuffles steer a card anywhere, that the steering words are binary numerals, and that mirror-coloured pairs stay mirror pairs.

**Overlap, stated plainly.** Week 3 (Shuffle machines) already has grades 4–5 find out-shuffle return times for 4 to 12 cards and for the full deck (8), and its guide names the in-shuffle, Elmsley's trick and DGK as "where it goes next". A week that only repeats return times would duplicate Week 3. The distinct angle proposed here is two shuffles used together: steering (Elmsley), the mirror invariant, and how few orders the pair can reach.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Mathematics of Perfect Shuffles](https://www.enseignement.polytechnique.fr/informatique/INF411/TD/TD1/Diaconis_Graham_Kantor_Perfect-Shuffles.pdf). Persi Diaconis, R. L. Graham and William M. Kantor, Advances in Applied Mathematics 4, 1983, 175–196. Orders of the out- and in-shuffles, Elmsley's binary lemma, the group generated for every deck size, the 2^k, 12 and 24 exceptions, 26 in-shuffles reverse 52 cards (read November 4, 2026).
- [How to cheat at cards](https://chalkdustmagazine.com/features/how-to-cheat-at-cards/). Kevin Houston, Chalkdust Issue 11, April 17, 2020. In and out shuffles, the binary rule (13 = 1101: in, in, out, in), orders 8, 21 and 52 for 52, 50 and 54 cards (read November 4, 2026).
- Prior use with children: [Brent Morris: Magician and Computer Scientist](https://www.cs4fn.org/mathemagic/brentmorris.php). cs4fn (a computer-science magazine for school students, with teacher resources). Perfect in- and out-shuffles and the binary rule (6 = 110: in, in, out) (read November 4, 2026). The library's own Week 3 uses out-shuffles with grades 4–5; no K–3 source was found (searched NRICH and circle pages for perfect shuffles).

## A kid-friendly way in

Eight picture cards on a mat with eight numbered spots, and two arrow mats like Week 3's machines: an "out" mat and an "in" mat that show where each spot's card goes. Older children also do real faro shuffles by dealing the halves into two rows and zipping them. Colour the cards in mirror pairs (spots 1 and 8 red, 2 and 7 blue, and so on). Prep: print two arrow mats and one spot mat per pair and colour eight cards, about 20 minutes. Launch (2 to 3 minutes): the facilitator runs one out-shuffle and one in-shuffle on a big mat, children call where the star card went, and the goal is posed: send the star card to a chosen spot.

## By band

- **K–1:** run the out mat until the cards are home (3 turns), then the in mat (6 turns). Then the steering game: an adult names a spot; children choose in or out each turn to get the star card there. Notice that the colours always stay a mirror. Counting to 8; no reading.
- **2–3:** find the shortest in/out word that sends the top card to each of the 8 places (0 to 7 counted from the top, or 1 to 8 with the adult converting), and record the words in a table. What do the words for 1, 2, 4 have in common? Can a word ever be shorter? Then 16 cards on the mat: predict a word before trying it.
- **4–5:** why the rule works: an out-shuffle doubles a top-half card's place, an in-shuffle doubles and adds one, so the word is the binary numeral of the place. Then the reachability question: with 4 cards, which of the 24 orders can in and out shuffles reach? (8; the mirror rule explains why no more.) Extension: how many shuffles of each kind restore 52 cards, using "double and take away 51" (Week 3's result, now explained for both shuffles).

## Checked facts

Computed in `check_symmetry_number_3.py`, `check_week_199()`:

- out-shuffle orders: 2, 4, 3, 6, 10 for 4 to 12 cards; 21, 8 and 52 for 50, 52 and 54 cards, each equal to the order of 2 mod (cards − 1); in-shuffle orders equal the order of 2 mod (cards + 1) for every even deck up to 58; 52 for 52 cards; 26 in-shuffles reverse 52 cards;
- Elmsley's rule moves the top card to every place in decks of 8, 16 and 52; 6 = 110 and 13 = 1101;
- mirror partners stay mirror partners under both shuffles for every even deck up to 28;
- reachable orders with both shuffles: 2, 8, 24, 24, 1920, 7680, 322560 and 64 for 2 to 16 cards; 8 cards reach 24 of 40320; 12 cards reach 2⁶ × 120.

Cited, not computed: the 52-card group of order 26!·2²⁶ and the 24-card Mathieu case (DGK).

## Nearest existing themes

Week 3 (Shuffle machines) is the closest and covers the out-shuffle return times, including 52 cards; see the overlap note above. Week 43 (Shuffling picture cards) asks whether a random shuffle is fair. Draft 118 (card magic) uses Gilbreath's principle, which is about a single random riffle, and the five-card trick; it never uses perfect shuffles. Draft 157 (remainders that repeat) studies the multiplicative order of 10 modulo a prime through decimals; the out-shuffle order is the same idea with 2, so draft 157 would supply the number theory and this week the card machine. Draft 117 (commutators) meets the same exceptional group PGL(2, 5). New here: steering with two moves, binary as the steering code, the mirror invariant, and reachability counts. If Week 3's return visits grow, this could be a Week 3 encore instead of a week.

## App connection

Patterns and symmetry, in the Cup swaps region beside Week 3's machines. A "Faro steering" family: two buttons, in and out; puzzles: "Send the cat to place 5 in three shuffles"; "Bring 8 cards home using only in-shuffles: how many?"; "Can you reach this order?" with a checkable "no" from the mirror colours. The existing shuffle-machine family could carry it with a second machine.

## Open questions

- Is Week 3's material close enough that a reviewer would rather fold this into a Week 3 return visit?
- Counting places from 0 is natural for binary but not for children; test whether 2–3 can work with "cards above it".
- Real faro shuffles are hard to do by hand; check that the dealing-and-zipping method is accurate for 8 and 16 cards.
