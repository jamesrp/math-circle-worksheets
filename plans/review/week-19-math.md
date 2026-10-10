# Week 19 (no card inside another / subset antichains): math check

**Scope.** I checked these current PDFs in `lowell-math-circle-year-2/week-19/`:
- Student packets: `week-19-k-1.pdf` (F19-K-v2, 5 pp.), `week-19-grades-2-3.pdf` (F19-23-v2, 6 pp.) and `week-19-grades-4-5.pdf` (F19-45-v2, 6 pp.). Each band has Problems 1–8.
- The adult guide `week-19-facilitator.pdf` (12 pp., including the p. 12 route update).
- The bonus companion `week-19-bonus.pdf` (W19-BON-v1, 5 pp., Problems 1–8) and `week-19-bonus-facilitator.pdf` (5 pp.).

The sources are `lowell-math-circle-year-2/source/week-19/editable/` and `source/week-19-bonus/`. I ignored the archive folders. I checked on October 10, 2026. I did not import or trust the package's `build_packets.py` checks, `answer_checks.json`, `independent_checks.py` or the bonus `math/independent-check.py`.

**Result: no mathematical errors in any band, the adult guide, the bonus packet or the bonus guide.** Every answer, count, list, partition and argument I could test is correct. Every deck matches its text. I found nothing that needs fixing.

## How it was checked

My scripts and their outputs are in [checks/week-19/](checks/week-19/). Each script finds the repository by walking up from its own folder.

- **Decks read from the PDFs** (`extract_pdf.py` → `pdf_decks.json`, `out_extract_pdf.txt`). The script reads the vector drawing of every student page with pdfplumber. Each symbol is classified by its own geometry: a circle is four Bezier arcs, a triangle a 3-vertex polygon, a square a PDF rectangle and a star a 10-vertex polygon. Each card is assigned to the "Problem N:" label above it. The bonus cards are read from their printed text labels.
  - All 161 base cards and every bonus card were read.
  - Every symbol sits in the same corner on every card in every band: circle top left, triangle top right, square bottom left, star bottom right. So "all its pictures are on the other card" can be judged by position as well as by shape.
  - Cards are square, with height/width 1.000. Circles and squares are 1.000; the star is a regular five-point star at 0.951. The triangle is an isosceles icon at 0.909, which is fine because no problem relies on it being equilateral.
  - Every card has exactly one border mark, including the empty card. No group repeats a card.
- **Consistency** (`check_rebuild.py` → `out_check_rebuild.txt`, 0 failures).
  - The six delivered PDFs are byte-identical to the reference copies in the two source packages.
  - I re-ran `build_packets.py` in a temporary copy. It reproduces the three shipped `.tex` files exactly.
  - The builder's deck orders D4, D8 and D16 equal the decks read from the PDFs.
  - The source ZIP matches `editable/`: 42 files, identical hashes.
  - LaTeX is not installed here, so I did not recompile the PDFs.
- **Exhaustive mathematics** (`check_math.py` → `out_check_math.txt`, 178 checks, 0 failures).
  - Antichains are enumerated by backtracking over the printed decks.
  - The fewest nested rows is computed two ways: as a minimum path cover by bipartite matching, and by an exhaustive row search that confirms r rows are possible and r−1 are not.
  - The bonus families are enumerated over all 2^8 and 2^16 subsets, and all 168 monotone rules are generated directly.
  - Every guide claim tested is first confirmed to appear verbatim in the guide PDF text. All 24 "Student page N" references in the guide match the PDFs.
  - The guide's p. 4 diagram is read from the PDF and its rows and arrows compared with the text: six rows, one arrowhead between each pair of consecutive boxes.

## K–1: checks out completely

- **Rules:** A card fits inside another when all its pictures are on it, and the empty card fits inside every card. This is the subset order.
- **P1:** The four printed groups are empty/A/B, A/AB/B, AB/AC/BC and A/BC/ABC. Their largest legal choices are A/B, A/B, AB/AC/BC and A/BC, sizes 2, 2, 3 and 2. Each is the unique largest choice in its group.
- **P2:** The deck is the full 2-symbol deck: empty, AB, A, B. It has exactly 5 collections of one or more cards: the four single cards and A/B.
- **P3:** The deck is the full 3-symbol deck. It has exactly 9 two-card collections, and they equal the guide's list.
- **P4:** The largest collection has 3 cards. Exactly two collections reach it, A/B/C and AB/AC/BC, so "a different collection just as big" is always possible.
- **P5:** The starts in printed order are ABC, A, AB and A/BC. Their largest final sizes are 1, 3, 3 and 2.
  - ABC and A/BC cannot take another card.
  - The best addition to A is B/C, and the best addition to AB is AC/BC.
- **P6:** The example row A → AB is a valid nesting, and both decks are full decks. The fewest rows are 2 and 3, and an exhaustive search confirms that 1 and 2 rows are impossible.
- **P7:** No legal four-card collection exists.
- **P8:** Yes. For each of the 8 cards set aside, a legal three-card collection remains.
  - P8 prints no deck of its own. "This deck" is the P7 deck printed above it on the same page, which is the deck intended.

## Grades 2–3: checks out completely

- **P1:** As K–1 P2: exactly 5 collections.
- **P2:** The largest collection has 3 cards. There are exactly two: A/B/C and AB/AC/BC.
- **P3:** The starts are ABC, A/BC and AB. They reach 1, 2 and 3 cards. ABC and A/BC are unextendable but smaller than 3, so the answer to the printed question is no.
- **P4:** The fewest rows are 2 and 3.
- **P5:** No four-card collection exists.
- **P6–P8:** The printed sixteen-card deck is exactly the 16 subsets of {A, B, C, D}. The largest collection has 6 cards and the fewest rows is 6.
- A five-row arrangement is impossible, which the exhaustive search confirms.

## Grades 4–5: checks out completely

- **P1:** The largest collections have 2 and 3 cards.
- **P2:** The largest collection has 6 cards.
- **P3:** The starts are ABCD, A/BCD and AB/AC. They reach 1, 2 and 6 cards.
  - ABCD and A/BCD are unextendable.
  - AB/AC extends to six in exactly one way, by adding AD, BC, BD and CD.
- **P4–P5:** The fewest rows are 2, 3 and 6.
- **P6:** The largest collection has 6 cards.
- **P7:** The printed card is the circle card A. The largest collection containing it has 4 cards. Exactly two collections reach it: A/B/C/D and A/BC/BD/CD.
- **P8:** There is exactly one six-card collection, the six two-symbol cards. Given a correct size from P6, the list has one entry.
- Every step of the guide's P8 argument was checked card by card. The largest collection containing a given card has:
  - 1 card if the card is empty or ABCD;
  - 4 cards if it is a singleton or a triple;
  - 6 cards if it is a pair.

## Adult guide: checks out completely

The following were checked and are correct.

- **Overview (p. 1):**
  - A chain partition into r rows bounds every antichain by r.
  - The maxima are 2, 3 and 6, and the six two-symbol cards are the unique six-card antichain.
  - Sperner's theorem is stated correctly: the maximum is C(n, ⌊n/2⌋), attained by a middle level. I also checked it for n = 1…5.
  - The guide correctly limits the packets to the small cases and correctly separates maximal from maximum.
- **Supplies (p. 2):**
  - 3 tables × 2 decks gives 6 decks and 96 cards, and 3 tables × 20 counters gives 60 counters.
  - The inventory lists the 16 cards once each.
  - Keeping only the cards without unused symbols gives exactly the printed 4- and 8-card decks.
- **Certificates (pp. 3–4):** The 2-, 3- and 6-row partitions each cover their deck exactly once, and every row is nested. The drawn p. 4 diagram equals the rows stated in 2–3 P7. "ABCD" and "A/BCD" are unextendable.
- **Solutions (pp. 5–10):** Every answer, list and argument is correct. This includes:
  - the uniqueness claims in K–1 P1;
  - the singleton argument in K–1 P4 and 2–3 P2;
  - the A/BC and A/BCD obstructions;
  - the P7 reduction to the three-symbol deck on B, C, D;
  - the complement argument in 4–5 P8: complementing reverses containment, so every antichain stays an antichain. This was checked on all antichains for 3 and 4 symbols.
- **Extensions (p. 11):**
  - Removing A and BC from the 3-symbol deck leaves a maximum of 2. Nine two-card removals do this: each pairs one singleton with one pair card.
  - Removing a pair card from the 4-symbol deck leaves a maximum of 5. Removing any other card leaves 6.
  - The counts 6, 20 and 168, including the zero-card family, are the Dedekind numbers.
- **Route update (p. 12):** It describes the problems correctly and changes no answer.

## Bonus packet and bonus guide: check out completely

- **The decks:** P1, P2 and P7 print the full 3-symbol deck. P3, both P4 grids and P8 print the full 4-symbol deck.
- **P1:** The largest pairwise-sharing collection without the empty card has 4 cards. There are 4 such collections.
- **P2:** Exactly one of those 4 has no common symbol, AB/AC/BC/ABC, as the guide says.
- **P3:** The largest pairwise-sharing collection has 8 cards. The guide's second example, AB, AC, BC, ABC, ABD, ACD, BCD, ABCD, shares pairwise and has no common symbol. There are 12 maxima in all.
- **P4:** Both lists of ten working cards are correct.
- **P5:** The given working set is closed under adding symbols. Its minimal cards are B and AC, and an exhaustive search confirms that 2 triggers are the fewest possible.
- **P6:** I tested all 168 monotone rules. The cards that fail on every single-symbol removal always recreate the rule.
  - This relies on the empty card counting vacuously when every card works, and the guide says so.
  - Under the other reading, "some removal makes it fail", the only rule not recreated is the all-working rule.
- **P7:** With nested triples forbidden, the largest collection has 6 cards. The unique maximum is A/B/C/AB/AC/BC, as the guide claims.
- **P8:** The largest collection has 10 cards. Exactly two collections reach it: the singletons with the pairs, and the pairs with the triples.
- **Chain covers:** Covers with row lengths 4, 2, 2 and 5, 3, 3, 1, 3, 1 are valid, and the second has room for 10 chosen cards.
- **Guide extension:** With nested chains of four forbidden on 3 symbols, the largest collection has 7 cards, and only by omitting either the empty card or ABC.
- **Other guide statements:** These are also correct:
  - the complement counterexample, ABC/ABD against D/C;
  - B, AB, AC give the same rule as B, AC;
  - 256 and 65,536 families.

## Not checked

- **Source citations:**
  - Base guide p. 11: Stanley, MIT 18.318 (2006), §4 pp. 17–25, Proposition 4.4 and Corollary 4.8, and Rozhkovskaya's introduction.
  - Bonus guide p. 5: *Math Circle by the Bay*, Preface pp. vii–x.

  None of these books is available locally.
- **Not mathematics:** Physical card size, preparation time and classroom timing are outside this check.
