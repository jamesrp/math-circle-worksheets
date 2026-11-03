# Week 118 (draft plan): Card magic

**Strand:** symmetry and logic (Codes and logic). **Deep-math field:** combinatorics (invariants under shuffles, counting and the pigeonhole principle). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Two classic tricks rest on two different theorems. Gilbreath's principle (Norman Gilbreath's "Magnetic Colors"): start with cards alternating red and black, split them into two piles whose exposed cards differ in colour, and riffle the piles together in any way at all; then every consecutive pair (cards 1 and 2, 3 and 4, and so on) has one red and one black. The reason is an invariant: after each card drops, the two exposed cards still differ, so the next card is always the opposite colour of the one before it within a pair. Dealing some cards into a pile before merging reverses them and guarantees different exposed cards, so no careful cut is needed. One riffle therefore leaves a lot of order behind, and a general version for any repeating pattern appears in Diaconis and Graham's *Magical Mathematics* (2012). The Fitch Cheney five-card trick (William Fitch Cheney Jr., analysed by Michael Kleber in 2002): a spectator picks 5 cards from 52; an assistant hands 4 of them to the magician in a chosen order, and the magician names the fifth. Five cards and four suits force two of one suit (pigeonhole); on a 13-hour clock one of those two is 1 to 6 hours after the other, so the assistant shows the earlier one first and hides the later; the remaining three cards have 3! = 6 orders, enough to say "1 to 6 hours later". Counting gives the limit: n chosen cards, n − 1 shown in order, from a deck of d cards needs C(d, n) hands to fit into d(d − 1)⋯(d − n + 2) messages, which holds exactly when d ≤ n! + n − 1; Kleber shows (with Hall's marriage theorem) that this bound is reached, so 5 cards work with up to 124. For children the small case is sharp: 3 cards from 8, show 2, has 56 hands and 56 messages, and 9 cards is impossible (84 hands, 72 messages). Proved: both principles and the bound. Checked here: Gilbreath on every merge of alternating decks up to 10 cards, the five-card method on 20,000 random hands, a complete code for 3 cards from 8, and the 9-card and 21-card column tricks.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Best Card Trick](https://classes.csail.mit.edu/6.042/spring18/Kleber-cardTrick.pdf). Michael Kleber, *Mathematical Intelligencer* 24 (1), 2002. The five-card trick, pigeonhole for suit, the 13-cycle offset at most 6, 3! orders, and the n! + n − 1 bound with Berlekamp's 124-card method (read November 3, 2026).
- [Red-Black Pairs Card Trick](https://math.hmc.edu/funfacts/?p=407). Math Fun Facts, Harvey Mudd College (Francis Su et al.). The alternating-deck riffle trick and the exposed-card argument (read November 3, 2026).
- [Mathematics Awareness Month 2014: Mathematics, Magic, and Mystery](https://ww2.amstat.org/mam/2014/calendar/gilbreath.html). American Statistical Association calendar page on the Gilbreath principle. Gilbreath's "Magnetic Colors", the deal-then-riffle "Gilbreath shuffle", classroom challenge questions, and the pointer to Diaconis and Graham, ch. 5 (read November 3, 2026).
- Prior use with children: [The Best Card Trick?](https://nrich.maths.org/1479). NRICH, ages 11 to 16. Students decode the five-card code from examples and a crib sheet, then perform it in pairs (read November 3, 2026).

## A kid-friendly way in

Perform first, then ask how. Each table gets a 10-card deck of alternating red and black (or two colours of picture cards), a 9-card picture deck, and later a short deck numbered 1 to 8. Pairs trick for every band: deal a few cards into a pile, then make one row on the table by taking the top card of either pile, any way you like; flip the row in pairs and every pair has both colours. Taking a top card from either pile is a riffle a five-year-old can do. Prep: sort decks and print a 13-hour clock card, about 15 minutes. Launch (2 to 3 minutes): the facilitator does the pairs trick once with a child choosing every pile, then a child does it while the facilitator looks away.

## By band

- **K–1:** perform the pairs trick for each other; try hard to break it (make a pair of the same colour). Then the 9-card column trick: deal three columns of three, the friend points to the column with their card, pick up with that column in the middle, deal again, point again; the card is always fifth. Counting and colours only.
- **2–3:** why the pairs trick works: what is true about the two top cards after each move? Try a plain cut instead of dealing a pile: when does it fail? (When the two top cards match.) Then the warm-up magic code: from cards 1, 2, 3 a friend keeps two, you show one, the magician names the other (show the one whose next number round the 3-clock is hidden).
- **4–5:** the code puzzle: a friend picks 3 cards from 1 to 8 and you show 2 in an order of your choice; design a code that always lets the magician name the third. Counting first: 56 hands and 56 ordered pairs, so a code must use every message, and with 9 cards none can exist (84 hands, 72 messages). Then learn and perform the full five-card trick with a 13-hour clock.

## Checked facts

Computed in `check_symmetry_games.py`, `check_week_118()`:

- for alternating decks of 2 to 10 cards, every way of dealing some cards into a pile and then merging gives mixed pairs; a cut with matching top cards (RB|RBRBRB split as RB and RBRBRB) can fail;
- on a 13-hour clock, of any two different hours one is 1 to 6 hours after the other; the five-card encode and decode agree on 20,000 random hands;
- the largest deck for n cards with n − 1 shown is n! + n − 1 for n = 2 to 5 (3, 8, 27, 124); C(8, 3) = 56 = 8 × 7 and C(9, 3) = 84 > 72;
- a complete 3-from-8 code: hide the card whose position in sorted order is the sum mod 3; the shown order picks between the exactly two cards consistent with that rule; all 56 hands decode;
- the 9-card trick ends with the chosen card fifth after two deals; the 21-card trick ends with it eleventh after three.

Cited, not computed: Kleber's matching proof that the bound n! + n − 1 is reached; the general Gilbreath principle.

## Nearest existing themes

Week 43 (Shuffling picture cards) asks when a shuffle is fair; this week shows that one riffle is far from fair, since it keeps the pair structure. Week 3 (Shuffle machines) studies fixed shuffles as permutations. Week 6 (Code breaking) and Week 18 (Hidden changes) count messages against possibilities, which is the same move as the n! + n − 1 bound; the card trick is a code with a fixed message budget. New here: an invariant that survives a random process, and a code whose capacity is exactly used up (56 for 56). The 21-card trick is weaker mathematically and is offered only as a performance warm-up.

## App connection

Codes and logic. A "Magic assistant" family: the child plays the assistant, choosing which card to hide and the order to show so that a computer magician (who knows the code) names it; later the child plays the magician. Example puzzles: "Your friend picked 2, 5, 7 from cards 1–8: show two cards so the magician can name the third"; "Merge these two piles so that some pair matches" (impossible when the top cards differ, with the exposed-card argument as the certificate). Ticket shuffles (Week 43) could host a riffle bench. Fit B.

## Open questions

- Can K–1 children merge two piles one card at a time without dropping or flipping cards? Rehearse with picture cards.
- Is designing the 3-from-8 code a satisfying 4–5 task or too open; should a partial crib (like NRICH's) be ready in the guide?
- How much performance time to allow; magic tricks invite repetition, which is fine, but the "why" questions need protected time.
