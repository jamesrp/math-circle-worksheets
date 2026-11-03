# Week 139 (draft plan): Secret messages and two padlocks

**Strand:** logic (Codes and logic), information. **Deep-math field:** cryptography, modular arithmetic. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Two facts, one old and one modern. First, a substitution cipher (each letter always replaced by the same symbol) has 26! ≈ 4 × 10^26 keys, far too many to try, yet it keeps every letter's frequency, so counting symbols in a long enough message breaks it; al-Kindi described this method in his Manuscript on Deciphering Cryptographic Messages (9th century). Lesson: a huge number of keys is not the same as security. Second, two people who share no secret can still agree on one over a public channel. Physically: Ana locks a box with Ana's padlock and sends it, Ben adds a second padlock and sends it back, Ana removes the first, Ben removes the second; the box is never unlocked in transit and no key ever travels (Shamir's three-pass idea, used with children as the "two padlocks" activity). The mathematical version is Diffie and Hellman's 1976 key exchange: with a public prime p and base g, Ana publishes g^a mod p, Ben publishes g^b mod p, and both compute g^(ab) mod p, while an eavesdropper seems to need a "logarithm" mod p. Its security is not proved: it rests on the belief that discrete logarithms are hard (Diffie and Hellman say the best known methods need about √p operations, and do not prove more). Children can discover why the padlocks must be special: if each padlock is a shift on the letter wheel, an eavesdropper who sees M + a, M + a + b and M + b recovers M = (M + a) + (M + b) − (M + a + b), so shift padlocks leak; multiplying padlocks leak the same way; powers on a clock do not leak in any obvious way. What is proved here is that shifts and multiplications leak; that powers are safe is believed, not proved.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Arab Code Breakers](https://simonsingh.net/media/articles/maths-and-science/arab-code-breakers) — Simon Singh (read November 3, 2026). Al-Kindi's treatise (about 850 AD, found in the Sulaimaniyyah archive), frequency analysis by matching the commonest symbols to the commonest letters.
- [New Directions in Cryptography](https://ee.stanford.edu/~hellman/publications/24.pdf) — Whitfield Diffie and Martin E. Hellman, IEEE Transactions on Information Theory IT-22(6), November 1976 (read November 3, 2026). The public key distribution system K = α^(X1·X2) mod q and its reliance on the apparent hardness of logarithms mod q.
- Prior use with children: [How to explain modern security concepts to your children](https://sancy.iut.uca.fr/~iso/publis/cryptologia.pdf) — Xavier Bultel, Jannik Dreier, Pascal Lafourcade and Malika More, Cryptologia, 2017 (read November 3, 2026). Unplugged activities including the box with two padlocks (3-pass Shamir protocol) and colour mixing for Diffie–Hellman; authors report teaching "from primary school to master courses" but give no ages per activity.
- Prior use with children: [Public Key Encryption (Kid Krypto)](https://classic.csunplugged.org/activities/public-key-encryption/) — CS Unplugged (read November 3, 2026). A whole-class public-key message game aimed at junior high, noted as hard for younger students.

## A kid-friendly way in

Two activities. A real box: a zippered pencil case with two zipper pulls, two small luggage padlocks with keys (each lock through both pulls holds the case shut), and a "mail carrier" child who carries the case and tries to peek. Plus a message of about 180 letters written in a made-up symbol alphabet (shapes or a scrambled alphabet), one copy per table, and a tally sheet. Prep: buy or borrow two padlocks, write the cipher message once and photocopy it, about 25 minutes. Launch (3 minutes): Ana wants to send a sticker to Ben but the carrier is nosy and Ana and Ben have no shared key. Hand the class the case and two padlocks and let them try; then act out the four trips together.

## By band

- **K–1:** Act out the two-padlock exchange in pairs with a carrier, then a picture-symbol message: a row of 20 to 30 symbols standing for a few short words the children know; they count which symbol appears most, and the adult tells them that the commonest letter in English is usually E. Counting and matching only.
- **2–3:** Break a substitution message (the facilitator's 183-letter story, enciphered with a scrambled alphabet, not a shift). Children tally symbols, guess E and T, then use short words (A, THE, AND) to finish. Contrast: Week 4's wheel shifts have only 26 keys, so you can try them all; a scrambled alphabet has 26! keys, yet counting still wins.
- **4–5:** Can padlocks be made of numbers? First try shifts on the Week 4 code wheel: Ana adds a secret shift, Ben adds another, Ana subtracts the first, Ben subtracts the second. Then play eavesdropper: from the three public messages, recover the letter. Then the 11-hour clock: powers of 2 visit every hour (2, 4, 8, 5, 10, 9, 7, 3, 6, 1). Ana keeps 3 and says 2^3 = 8; Ben keeps 7 and says 2^7 → 7; each raises the other's number to their own secret and both reach 2. Ask: what would an eavesdropper have to do, and why is it harder than undoing a shift?

## Checked facts

All in `check_logic.py`, function `check_week_139()`:
- 26! = 403,291,461,126,605,635,584,000,000, between 4 × 10^26 and 5 × 10^26; shift keys: 26.
- The sample story (in the script as `SAMPLE`) has 183 letters; E occurs 33 times (between one sixth and one fifth of all letters), T 19, N 18; six letters (B, J, K, Q, X, Z) never occur, so the message is long enough for E but not for the full alphabet.
- Shift padlocks leak for every message and secret mod 26: (M + a) + (M + b) − (M + a + b) = M; the app example 9, 14, 17 gives 12. Multiplying padlocks leak whenever the products can be undone mod 26.
- Powers of 2 mod 11 are 2, 4, 8, 5, 10, 9, 7, 3, 6, 1 (every hour once). Secrets 3 and 7 give public numbers 8 and 7 and shared key 2; every pair of secrets 1–10 gives both sides the same key.
- Three-pass with powers mod 11: message 5, locks 3 and 7 (undone by 7 and 3) go 5 → 4 → 5 → 3 → 5, and every message 1–10 survives every pair of locks from 1, 3, 7, 9.
- Cited, not computed: al-Kindi's date and method (Singh); hardness of discrete logarithms is an assumption (Diffie–Hellman).

## Nearest existing themes

Week 4 (Stars and wheels) already makes a 26-place code wheel and proves shifts add, undo and generate; this week must not rebuild it. It reuses the wheel as the broken padlock. Week 18 (Hidden changes) and atlas AP-28 are error-correcting codes, about noise, not secrecy; the applied-probability survey notes that "a secret cipher is not automatically error correction", which this week respects. Week 6 (Code breaking) is about finding a hidden row with few questions, not about ciphers. Week 84 (Public knowledge) is about who knows what; the key exchange is the opposite design problem: making sure an eavesdropper who hears everything still does not know. New: frequency analysis, key exchange without a shared secret, and the difference between proved leaks and believed hardness.

## App connection

Codes and logic region, possible family "Two padlocks" in Signal Lanterns: the board shows Ana, Ben and a nosy carrier; the child chooses padlock types and watches what the carrier sees. Puzzles: "The carrier saw 9, 14, 17 on a 26-letter wheel. What was the letter?" (answer 12: shift padlocks leak); "On the 11-clock, Ana said 8 and Ben said 7; Ana's secret is 3. What is the shared key?" A second family "Letter counts" gives a short cipher and a tally tool. Codebooks in Signal Lanterns (Week 18) shares the region and look.

## Open questions

- Material fit: test that one small padlock through both zipper pulls really keeps a pencil case shut and that children can open the locks quickly.
- Message length for 2–3: 183 letters may be too long to tally by hand; splitting it across a table and pooling tallies needs testing.
- Whether the 4–5 clock-power arithmetic (repeated multiplication with remainders mod 11) is fluent enough; a printed power table could carry the arithmetic so the reasoning stays in focus.
- Wording: say plainly to adults that clock powers are believed safe for very large clocks, not proved safe, and that on an 11-hour clock anyone can try all ten secrets.
