# Week 76 math check: Substitution strips (shared Grades 3–5 packet and adult guide)

Checked: `lowell-math-circle-year-2/week-76/week-76-students.pdf` (4 pages, rendered to `render/s-*.png`), `week-76-facilitator.pdf` (4 pages, `render/f-*.png`), sources `source/week-76/student/students.tex` and `guide/facilitator.tex`, plus `MATHEMATICS.md` where it bears on the guide.

Script: `plans/review/checks/week-76/check_math.py`, output in `check_math.out` (0 failures). The script generates the first 2^18 letters of T itself. It reads every printed strip from the source, then compares them letter by letter with the delivered PDF (all 4 pages match). It enumerates the factors of T up to length 24, checking that the factor sets are the same in prefixes of length 2^14 and 2^18. It also enumerates pairings under the Problem 4 convention and checks every answer string in the delivered guide PDF.

## What verifies

- **P1.** The 16-tile row is ABBABAABBAABABBA. It has exactly 6 distinct triples: AAB, ABA, ABB, BAA, BAB and BBA. These are all the triples of T, and all 6 already appear in the 8-tile row. There are 14 window starts. The 8 printed slots are covered by the guide.
- **P2.** No AAA or BBB appears. Every 3-window contains an even-start pair, and every even-start pair is unequal.
- **P3.** The worked example BAABBA decodes to BAB. Only claim 1 is a whole row. The guide's decode chains are exact:
  - ABBAABBA → ABAB → AA
  - ABBABBAB fails at BB
  - ABBABAABABBABAAB → ABBAABBA → ABAB → AA
- **P4.** All four crops occur in T, and the guide's pairings and kept tiles are complete and correct:
  - ABA has two pairings, and both alignments occur in T.
  - BAABA, AABB and ABBAABBA each have one pairing.
  - The worked example AABBA has the single pairing (A) | AB | BA, and it occurs in T.
- **P5.** All 12 five-tile factors have equal neighbours and exactly one pairing, so the answer "none exists" is right. Every genuine crop of length 5 to 24 has exactly one pairing. The crops with two pairings are only those of length at most 4: A, B, AB, BA, ABA, BAB, ABAB, BABA. ABABA and BABAB force parents AAA or BBB in both alignments.
- **P6.** ABABA is the shortest impossible piece of the AB strip. The ABBA strip avoids AAA, BBB, ABABA and BABAB. ABBAABBAAB is forced to split as AB|BA|AB|BA|AB, which decodes to ABABA, so it is impossible. ABBAABBA is genuine.
- **P7.** The answer is no, and the guide's proof is correct:
  - T[2n] = T[n] and T[2n+1] is the complement of T[n].
  - Equal neighbours occur only at odd indices, and aligned 4-blocks are ABBA or BAAB.
  - Odd periods and halving of even periods are handled correctly.
  - As a sanity check (not a proof), no p ≤ 4096 is a period of the second half of the prefix.
- **Diagrams.** Cells are square because the TikZ x and y units are both 1 mm. Labels and the "from B"/"from A" brackets sit over the right strips. Page 1 has 16 blank cells and 8 three-cell slots. The printed strips are (AB)^8 and (ABBA)^4.
- **Guide arithmetic.** The largest build is 24 ≤ 32 tiles. Kit totals are 36/6 and 108/14. Print counts are 16 and 20 sheets.

## Problems found

### 1. Student page 2, Problem 3: comparing with the Problem 1 row settles every claim at once

**Quoted text:** "Each row below claims to be a whole row grown from a single A. Which claims can be right? Keep a record that settles each decision."

**Evidence.** There is exactly one whole row of each length, and the rows are nested prefixes. The 16-tile row the children recorded on page 1 is ABBABAABBAABABBA, and its first 8 tiles are the only 8-tile whole row. So:

- Claim 1 equals those 8 tiles.
- Claims 2 and 3 differ from them at tiles 5 and 6.
- Claim 4 differs from the page 1 row at tile 9.

The guide says pages are issued one at a time, so page 1 is in hand. Matching is therefore a complete and valid "record that settles each decision", and it bypasses the undoing that the problem is meant to exercise. The guide's P3 section lists only decode records, so an adult may not recognise this answer or know how to respond to it. The check is in `check_math.out`, line "P3 SHORTCUT".

**Smallest fix.** Add a guide line to P3: "Matching against the Problem 1 row also settles every claim, because each length has only one whole row and its first 8 tiles are that row. Accept it, then ask for an undo record that shows *why* a claimed row cannot shrink to A."

### 2. Student page 3, Problem 5: the answer depends on the lone-tile rule, which is stated only in Problem 4

**Quoted text:** "Can two different ways of pairing it fit the replacement rule? Find such a piece, or explain why none exists."

**Evidence.** The restriction "apart from at most one lone tile at each end" appears only in Problem 4. A five-tile piece always has exactly one lone tile. If a child allows that tile to sit inside the piece, four genuine five-tile crops have two valid pairings, and the answer flips from "none" to "yes":

| Crop | Pairing 1 | Pairing 2 |
|---|---|---|
| ABAAB | (A) \| BA \| AB | AB \| (A) \| AB |
| ABBAB | AB \| BA \| (B) | AB \| (B) \| AB |
| BAABA | BA \| AB \| (A) | BA \| (A) \| BA |
| BABBA | (B) \| AB \| BA | BA \| (B) \| BA |

BAABA is one of Problem 4's own printed crops. The check is in `check_math.out`, line "P5 if the one lone tile may sit mid-piece".

**Smallest fix.** Change the text to "Can two different ways of pairing it, as in Problem 4, fit the replacement rule?" Alternatively, move the lone-tile sentence into the unnumbered opening guidance, since Problems 4–6 all use it.

### 3. Guide page 3, Problem 6: the ABBA-strip certificate and hint 3 assume the piece starts on the strip's 1st or 3rd tile

**Quoted text:** "This is a finite certificate, with no discarded or invented endpoint. The eight-tile ABBAABBA alone is not a certificate". Hint 3: "If eight tiles give only ABAB, extend the piece by one complete pair and decode again."

**Evidence (enumeration by start offset, in `check_math.out`).** The guide's rule is to decode only complete pairs, as in the student P4 text. Under that rule:

- A piece starting on the strip's 1st or 3rd tile reaches a forbidden parent at 10 tiles, as the guide says.
- A piece starting on the 2nd or 4th tile needs 11 tiles. For example, BBAABBAA keeps BAB, and BBAABBAABB keeps BABA, which is still genuine. Only BBAABBAABBA, which is (B)|BA|AB|BA|AB|BA → BABAB, gives a contradiction. Hint 3 does not cover this case.

Conversely, the shortest impossible pieces of the ABBA strip have 8 tiles: BBAABBAA and AABBAABB. They become certificates once the lone end tiles' parents are read. A first lone tile is the second half of its pair, so its parent is the opposite letter; a last lone tile is a first half, so its parent is the same letter. This gives ABABA and BABAB. The guide itself uses this step in its P5 explanation ("extend the clipped end-pair"). `MATHEMATICS.md`'s phrase "discarding those ends does not reveal their missing parent letters" is literally true. However, it hides the fact that each lone end tile's parent is determined once the alignment is forced.

**Smallest fix.** Add to the guide's P6 section: "A piece starting on the strip's 2nd or 4th tile needs 11 tiles if only complete pairs are decoded. If a child reads the lone end tiles' parents (the first lone tile came from the opposite letter, the last from the same letter), the 8-tile BBAABBAA or AABBAABB already gives ABABA or BABAB. Accept that as a certificate." Optionally, reword the MATHEMATICS.md sentence to match.

**Otherwise.** The student page and guide statements, solutions, hints and the Problem 7 proof all check out.
