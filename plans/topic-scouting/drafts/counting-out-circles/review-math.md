# Mathematical review: Counting-out circles, draft v1

Reviewer: independent math check (CRITIC-MATH stage). The draft was not edited.

## Method

I rendered all 15 pages of `draft/k-1.pdf`, `draft/grades-2-3.pdf` and `draft/grades-4-5.pdf`. These files are byte-identical to the copies in `draft/src/`. I then simulated the game literally: a fixed ring of spots, a chant ("stand, sit" or "stand, stand, sit") said only to standing counters, sitting counters flipped and skipped. I did not use the author's `check.py`. I simulated the main game for n = 1 to 1024 and the every-third game for n = 1 to 100. The simulation confirms:

- every-second survivor J(n) = 2L + 1, where n = 2^m + L and L < 2^m;
- the binary answer is n with its leading 1 moved to the end;
- J(2k) = 2J(k) − 1 and J(2k + 1) = 2J(k) + 1;
- every-third survivor J₃(n) = (J₃(n − 1) + 2) mod n + 1;
- for every n < 200, the first n/2 people to sit (rounded down) are exactly the even numbers, in order.

I also simulated one misreading: the chant starts again at "stand" every time the count passes spot 1.

Every stated fact and every printed number is correct: J(26) = 21, the binary forms of 13 and 11, and the numbered rings and table headings. All ring diagrams have the right number of spots, numbered 1..n clockwise from the top. All table headings match their problems. The issues below are about readings, edge cases and examples, not arithmetic errors.

## Located problems

### 1. All bands, mainly K–1: the rule does not say the chant carries past spot 1, and the planned launch cannot show it

- **Where:** K–1 page 1, shared rules: "Start at 1 and go round and round the circle saying stand, sit, stand, sit." Grades 2–3 and 4–5 page 1, shared rules: "The standing counters take turns: 1 stays standing, the next one sits down, the next one stays standing, the next one sits down, and so on."
- **Evidence:**
  - If a child starts the chant again at "stand" whenever the count reaches 1, then 1 never sits. The simulation gives 1 as the last one standing for every n from 2 to 16. Under that reading:
    - every K–1 answer in Problems 1 and 2 becomes 1;
    - every ring in Problem 3 gets circled;
    - Problem 5 becomes impossible;
    - the 2–3 and 4–5 tables become all 1s.
  - The planned launch circle of about eight children cannot show which reading is right. For n = 8, and for any power of two, the count arrives back at 1 on a "stand" in every lap, so both readings give the same play.
  - The first case where the readings differ is K–1 Problem 1's ring of 3. Under the correct reading, 3 stands, then 1 sits. That table is run by the parent volunteer.
  - The every-third version has no such risk: the restart reading never ends there (1 and 2 stand forever), so children would notice.
  - The 2–3 and 4–5 phrase "take turns" points to the right reading, but it does not say so outright.
- **Smallest fix:**
  - K–1: add one sentence to the shared rules: "Keep the chant going when you come back round to 1."
  - Grades 2–3 and 4–5: add the same idea: "Keep taking turns when you come back round to 1."
  - Outside the pages: launch with an odd number of children, for example 5 or 7, so the group sees the lap where 1 sits.

### 2. K–1, page 4, Problem 5: the question asks for one answer but has several, and page 1 already answers it

- **Quoted:** "How many people should be in the circle so that number 5 is the last one standing? So that number 3 is the last one standing?" The answer boxes are labelled "5" and "3".
- **Evidence:**
  - Number 5 is last for n = 6, 10, 18, 34, …
  - Number 3 is last for n = 3, 5, 9, 17, 33, …
  - "How many people should be" suggests one answer. For number 3, the children have already found two answers (3 and 5) in Problem 1.
  - All the answers up to 8 are already circled on page 1: the rings of 3 and 5 give 3, and the ring of 6 gives 5. A child can answer by looking back without doing the inverse search the problem is meant to be.
- **Smallest fix:** "On the mat with 16 spots, find a circle bigger than 8 where number 5 is the last one standing. Then find one where number 3 is the last one standing."
  - Between 9 and 16 each answer is unique: 10 for number 5 and 9 for number 3. The search is real, and a 16-spot mat is enough.
  - A second option is "Find every circle up to 16 people where number 5 is the last one standing. Then do the same for number 3." Its answers are 6 and 10, then 3, 5 and 9.

### 3. Grades 4–5, page 5, Problem 10: the worked example also fits a wrong rule

- **Quoted:** "the last one standing in a circle of 13 people is 11. In binary, 13 is written 1101 … and 11 is written 1011". The first table row is 13 / 1101 / 11 / 1011.
- **Evidence:**
  - Reversing the digits also turns 1101 into 1011. Swapping the 2nd and 3rd digits does too.
  - Reversal gives the right answer for 10 of the circles from 1 to 16: n = 1, 2, 3, 4, 7, 8, 10, 13, 15, 16. A child who guesses "reverse it" from the example can confirm it on many easy rows before finding a failure. For example, 6 = 110 reversed is 011 = 3, but the answer is 5 = 101.
  - The correct rule, moving the leading 1 to the end, is the only one the page should seem to support.
- **Smallest fix:** use n = 12 as the example. 12 = 1100 (8 + 4) and the last one standing is 9 = 1001 (8 + 1). Reversing gives 0011 = 3 and swapping gives 1010 = 10, so neither wrong rule fits, and the example gives away no more than the current one.

### 4. Grades 2–3 page 3 and grades 4–5 page 3, Problem 7: "3 sits down" cannot be done in circles of 1 and 2

- **Quoted:** "Now every third counter sits down: 1 and 2 stay standing, 3 sits down, the next two stay standing, the next one sits down, and so on. Play circles of 1 to 12 people". The table starts at 1 and 2.
- **Evidence:**
  - In a circle of 2, spot 3 is empty, and the shared rules say to skip empty spots.
  - The intended play is 1 stands, 2 stands, then 1 sits (the count wraps), so 2 is last. The table expects 2.
  - A literal reader may decide that nobody sits, or may skip spot 3 and count only to 2.
  - The circle of 1 is trivial (answer 1).
  - The table values 1, 2, 2, 1, 4, 1, 4, 7, 1, 4, 7, 10 are correct under the intended reading.
- **Smallest fix:** "1 and 2 stay standing, the next standing counter sits down, the next two stay standing, the next one sits down, and so on."

### 5. Grades 2–3 Problems 2 and 9, grades 4–5 Problem 2: they need a 32-spot mat, but the outline allows a 24-spot mat

- **Quoted:** "Then play them on the mat with 32 spots to check" (circles of 20, 25 and 32). Grades 2–3 Problem 9 asks about a circle of 30.
- **Evidence:** the outline's materials say "a second mat with 24 or 32 spots". With a 24-spot mat, the circles of 25, 30 and 32 cannot be played.
- **Smallest fix:** no change to the pages. Make the larger mat 32 spots, with 32 counters per pair, wherever the materials list is settled.
- **Related, not an error:** grades 4–5 Problem 9 (circle of 41) and the "up to 40" and "up to 100" searches go beyond any mat. They are reasoning tasks and do not say to play them, which is fine. For Problem 9 the expected route is to continue the add-3 pattern from 24 up to 41, and the page gives open space for that.

### 6. Grades 2–3, page 2, Problem 5, second part: whether a circle of 1 counts (minor)

- **Quoted:** "Then find every circle up to 40 people where the last one standing has the biggest number in the circle."
- **Evidence:** J(n) = n exactly when n = 1, 3, 7, 15 or 31. A circle of 1 meets the condition trivially, so a correct answer is either {3, 7, 15, 31} or {1, 3, 7, 15, 31}.
- **Smallest fix:** "every circle from 2 to 40 people". Alternatively, leave the wording and accept both answers. Grades 4–5 Problem 3 also includes n = 1 in {1, 2, 4, 8, 16, 32, 64}, which is harmless there.

## Answers checked (no problem found unless listed above)

**K–1**

| Problem | Answer |
|---|---|
| 1 | Rings 3, 4, 5, 6 → 3, 1, 3, 5. |
| 2 | Rings 7, 8 → 7, 1. |
| 3 | Of the seven thumbnails (2 to 8), only 2, 4 and 8 leave number 1. The rings of 3 to 8 were played in Problems 1 and 2, so only the circle of 2 is new. That fits a collection task. |
| 4 | 16 → 1. The drawn ring is too small for counters, but the text sends children to the 16-spot mat. |
| 5 | See problem 2 above. |
| 6 | No. Person 2 is always the first to sit in any circle of 2 or more, and a circle of 1 has no person 2. |
| 7 | Stand, stand, sit: rings 3, 4, 5, 6 → 2, 1, 4, 1. |
| 8 | Rings 7, 8 → 4, 7. |

Ring geometry: neighbouring spots never overlap. The closest pair of centres is 2.85 cm apart, against a spot width of 2.6 cm.

**Grades 2–3**

| Problem | Answer |
|---|---|
| 1 | Circles 1–16 → 1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9, 11, 13, 15, 1. |
| 2 | 20 → 9, 25 → 19, 32 → 1. |
| 3 | Exactly the even numbers. Every even-numbered person sits on the first lap, and every odd number 2L + 1 is last for n = 2^m + L. |
| 4 | 50 → 37, 100 → 73. |
| 5 | Number 9 is last for n = 12, 20, 36. The biggest number is last for 3, 7, 15, 31 (see problem 6 above). |
| 6 | Correct claim (16 → 1, 32 → 1). |
| 7 | 1, 2, 2, 1, 4, 1, 4, 7, 1, 4, 7, 10 (see problem 4 above). |
| 8 | 13–20 → 13, 2, 5, 8, 11, 14, 17, 20. These can be predicted from the 1–12 table with "add 3, and subtract the circle size if the result is too big". |
| 9 | Circle of 30, every third: stand at 29. |

**Grades 4–5**

| Problem | Answer |
|---|---|
| 1, 2 | Same as grades 2–3. |
| 3 | 1, 2, 4, 8, 16, 32, 64. |
| 4 | 100 → 73, 1000 → 977. |
| 5 | The premise J(26) = 21 is true. J(52) = 2·21 − 1 = 41 and J(53) = 2·21 + 1 = 43, both confirmed by simulation. |
| 6 | Number 21 is last for n = 26, 42, 74. Number 22: none. The empty answer looks like a deliberate contrast, so no fix is needed. Adults should expect "none, because even numbers sit on the first lap"; no other 4–5 problem asks about even numbers. |
| 7 | Same as grades 2–3 Problem 7. |
| 8 | 13–24 → 13, 2, 5, 8, 11, 14, 17, 20, 2, 5, 8, 11. |
| 9 | Circle of 41, every third: stand at 31. Number 16 is the last to sit. |
| 10 | Rule: move the leading 1 to the end and drop any leading zeros, for example 4 = 100 → 001 = 1. It is explained by n = 2^m + L → 2L + 1 (see problem 3 above). |

Apart from the items above, all three bands check out.
