# Review: facilitator guide for Train-yard sorting (draft v1)

Reviewed: `draft/facilitator.pdf` (6 pages) and `draft/src/facilitator.tex`, against the final student pages `k-1.pdf` (5 pp.), `grades-2-3.pdf` (4 pp.), `grades-4-5.pdf` (5 pp.) and `track-mat.pdf` (1 p.). I rendered and read every page (images in `review-guide-check/img/`), and also read the page sources (`build.py`), the outline, both page reviews, the drafts README entry and the Week 98 model guide.

How I checked: `review-guide-check/check.py`, output in `review-guide-check/check.out`. It does not use the guide's `check_guide.py` or the pages' `verify.py`. For one siding it searches every legal move sequence, with no greedy rule, both unlimited and with five places. For two sidings it searches every state, with and without a waiting track between the mats, unlimited and with five places. It tests every train, mark, triple, gap list, path word, decoding, count and printed two-siding drive in the guide, plus the steps of the hand proof for 2 4 3 5 7 6 1. Result: **0 failures.**

## Verdict

This is a strong guide. Every printed answer is right, and every problem number, page number, picture description and material count matches the final PDFs. Nothing is keyed to the earlier draft: for example, five-car K–1 Problem 4 and Problem 5 are numbered as on the final pages, and 4–5 Problem 4 has 14 grids. The overview is theorem-first and comes before any solution. Its proofs can be followed, and it separates experiment, conjecture and explanation. The launch uses a non-task train.

Two sentences need correcting before use. One is a false claim about what counts as evidence for a ✗. The other is an extension answer that is wrong on the band's actual mat. The rest is tightening.

---

## Must fix

### 1. The overview says what earns a ✗, and the claim is false (p. 1, "What children discover")

**Text:** "A stuck drive proves nothing by itself; a ✗ is earned by showing the bigger car parked on a smaller car that has to leave first."

**Problem:** A wrong move produces exactly that picture in a train that works. The guide's own Theorem 2 example, two paragraphs earlier, is "1 3 2, with 3 parked on 1": 3 is bigger, it is parked on 1, and 1 has to leave first, yet 1 3 2 works. Adults will apply this sentence at every table, so it would endorse the most common wrong ✗. The K–1 key (p. 3) avoids the mistake only through the words "has to wait", and a parent will not see the difference.

**Fix:** Replace the sentence with: "A stuck drive proves nothing by itself, since one wrong move strands a good train (1 3 2 with 3 parked on 1). A ✗ is earned by showing that the bigger car had no choice: when it arrived, the smaller car below it could not leave yet, because a still smaller car had not come. That is a middle, largest, smallest triple. It is also what happens when the needed car always leaves as soon as it is on top." In the K–1 key, add: "Before accepting a ✗, check that each needed car went out as soon as it was on top."

### 2. The Grades 2–3 six-car extension prints 132, but the 2–3 mat gives 131 (p. 4, 2–3 Problem 7)

**Text:** "Extension: six cars (132)."

**Problem:** The 2–3 rules do not include the 4–5 sentence "pretend the siding is long enough". On the five-place mat, 6 5 4 3 2 1 cannot leave. My check confirms that it is the only six-car train lost, so the count on the mat is 131. The guide says this itself under 4–5 Problem 7 ("giving 131"). In addition, the 2–3 table has no car 6 in its materials.

**Fix:** "Extension: six cars, with a paper car 6 and the siding treated as long enough: 132. On the five-place mat, 6 5 4 3 2 1 cannot leave, which gives 131." Add one blank paper square to the 2–3 materials if the extension stays.

---

## Should fix

### 3. The insertion count does not give the convolution formula (p. 1, Theorem 3)

**Text:** "Two child-sized counts give C_n = Σ C_k C_{n−1−k}. *Largest car:* … *Insertion:* …"

**Problem:** Only the largest-car split gives that sum. Insertion gives a different count: C_n is the total number of allowed gaps over the working (n−1)-car trains, as in 5 + 4·3 + 3·5 + 2·5 = 42. Read as written, both counts give the same formula.

**Fix:** "The largest-car split gives C_n = Σ C_k C_{n−1−k}: … Insertion gives a second count: add the allowed gaps for car n over the working trains of the other cars. The 14 working four-car trains have 42 such gaps."

### 4. "Snap cubes work" states an untested fit as fact (p. 2, Materials)

**Problem:** The Status paragraph above it says correctly that the cars have not been tried in the 29 mm places. Snap cubes have a peg on one face. That adds about 5 mm in one direction, and with the peg pointing up, the "top" where the number goes is the peg face. Whether they slide and fit five deep in the 145 mm siding is exactly what is unrehearsed.

**Fix:** Drop "(snap cubes work)", or write: "25 mm card squares or plain 2 cm cubes; snap cubes are untried (their peg adds length, so keep it pointing up and number a side face)."

### 5. The 4–5 first visit is likely to end before the band's own material (p. 2, "A first visit"; p. 4, 4–5 Problem 1)

**Problem:** 4–5 Problem 1 asks for the count of all 24 four-car trains. The trio has no cards and the guide offers no way to share the work. The guide gives the 2–3 table 15–20 minutes for the same 24 with four children. Add Problem 2's ten trains (up to eight cars, made from paper squares) and Problem 3's rule and proof, and 35–40 minutes is optimistic. Paths then wait for a second visit and two sidings for a third. The guide states that outcome honestly but offers no readiness-dependent alternative. GUIDE.md asks for one, and AGENTS.md allows children to share cases and pool a collection that can be checked.

**Fix:**
- Under 4–5 Problem 1, add: "Expect 10–15 minutes. If the trio wants to share the 24, ask how to split them so that nobody repeats a train. Splitting by first car keeps the pieces checkable (5, 2, 2, 5 work)."
- Under "A first visit", add a faster route for a quick trio: "Problem 1, the five-car rows of Problem 2, and Problem 3 as a conversation, then the first grids of Problem 4. The long trains in Problem 2 can test the rule later."

### 6. The 2–3 adult's role in Problem 2 is described two ways (p. 2, Staffing; p. 4, 2–3 Problem 2)

**Problem:** Staffing says the mathematician "coordinates the two pairs' shared cards in Problem 2". The Problem 2 note says to wait until the pairs ask how to share the work, and then only ask a question. Organizing a complete case list is part of the mathematics here.

**Fix:** In Staffing, write "keeps the shared pile in one place and leaves the splitting and the completeness check to the children; may write a rule a child says aloud in Problem 4". The last clause adds a scribing note for third graders, whose Problem 4 asks for a written rule.

---

## Minor

7. **Launch details (p. 2).**
   - The middle panel is labelled "One step", but it shows the state after three moves (2 in, 1 in, 1 out). Relabel it "Partway", or "After 2 in, 1 in, 1 out".
   - "Then point to page 1's picture" comes before packets are handed out. Say "hold up page 1".
   - "Ask the partner to watch the exit and say 'stop'": the whole group has no partner yet. Say "ask the group to say 'stop'; at the tables the partner does this job".
8. **The K–1 route is inconsistent (p. 2).** It reads "then Problem 5's partner game if time remains; Problems 4–6 make a return visit". Write "Return visit: Problem 4, more of Problem 5, then Problem 6."
9. **The K–1 key is not in page order (p. 3).** It lists all ✓ trains, then all ✗ trains. A parent checking a sheet would be faster with marks read row by row, for example Problem 2: "✓ ✗ / ✓ ✓ / ✗ ✓ / ✓ ✗", and Problem 4: "✗ ✓ / ✓ ✓ / ✗ ✗".
10. **The printed triples are not always the ones the drive shows (p. 4, 2–3 Problems 3 and 5).** All are valid 2-3-1 patterns. However, 4 2 5 1 3 strands 2 under 5, so a child will name 2, 5, 1 rather than 4, 5, 1, and in 2 4 3 5 1 the top car on 2 is 5. Add once: "Any middle, largest, smallest triple is right; the drive often shows a different one than listed."
11. **Two hints are instructions rather than questions.**
    - 4–5 Problem 4 (p. 5): "Drive the train and say in or out at every move." Try instead "Which moves make the 1 3 2 path go up?"
    - 4–5 Problem 5's "With objects: line up five cars lettered A to E …" is a full method. Mark it as a fallback for a stuck child. It also needs lettered cars, which are not in the materials, so say "letter five of the blank paper squares".
12. **"First return" is never defined (p. 5, 4–5 Problem 7).** The heading "Largest car or first return" names two different splits that give the same terms. The first return corresponds to the number of the first car. Add those few words, or drop "first return".
13. **Arrival-track capacity (p. 2, Print).** "Trains longer than about five cars wait on the table": the arrival track is 125 mm on paper, less after printer margins. That holds four 25 mm squares, or five to six 2 cm cubes. Say "about four or five".
14. **Brevity.**
    - K–1 Problem 5 says "42 of the 120 … so 'stuck' is the better blind guess". This is trivia for the K–1 parent, since partners choose their trains on purpose. Cut it.
    - 4–5 Problem 8 repeats the overview's "every train of up to six cars works and only 22 of 5,040 …". Cut it to a cross-reference.
    - The Sources sentence about how `check_guide.py` searches can be shortened to "independently checked".
    - "Hints:" in 4–5 Problem 8 introduces a single hint.
15. **Optional: the open-question sentence (p. 1, Theorem 4).** "No simple rule like Theorem 1 is known" is safe. If someone can verify it, a sharper statement is that no finite list of forbidden patterns describes two sidings in series. I recall this as M. M. Murphy's 2002 St Andrews thesis, but I have not checked it, so do not add it without a source.

---

## Coverage of the checks asked for

- **Correctness.** Every answer the guide prints was re-derived for the final pages, and all are right. This covers:
  - K–1 Problems 1–4 and 6, including the "waits on" pairs, the six fillings, the five-car extension, the ten stuck trains, the "seven met before" claim and the first-car rules.
  - 2–3 Problems 1–7, including the 14/10 list, the triples, the counterexamples to the tempting rules, the gap lists and the per-card gap counts summing to 42.
  - 4–5 Problems 1–8, including the car-4 position counts, the marks and triples, the four-place maximum, all 14 path words, the four decodings, 42/132/131, the three printed first-siding drives, 22 failures that all end in car 1, 51 failures with five-place sidings (with or without a waiting track), and every step of the 2 4 3 5 7 6 1 proof (all 429 first-siding outputs contain a 2-3-1).
  - The general theorems up to n = 8, the bijection up to n = 6, and that the launch train 2 1 has one forced drive and appears in no problem.

  The only wrong items are Must-fix 1 (a false general claim) and Must-fix 2 (an answer that is wrong on the band's mat).
- **Agreement with the pages.** All problem and page numbers, the "top row / bottom row" reading of 4–5 Problem 5, the 14 grids, the 29 mm places, the five-place siding, the packet page counts and the mat counts (seven) match. Nothing is keyed to an earlier draft.
- **Overview.** It meets the standard: theorems with assumptions and limits (five places versus unlimited, two sidings as research), followable proofs, an evidence paragraph and a band map, all before any solution. The two corrections are Must-fix 1 and Should-fix 3.
- **Launch.** It is brief and concrete, on 2 1, a non-task train with a meaningful middle state. It gives away no answer and says nothing about what makes a train stick. Only the small fixes in item 7 apply.
- **Usability.** Preparation (30–35 minutes, 27 cars) and staffing fit the group in `context.md`. Every band has a route for the first hour. Most hints are questions. The gaps are items 4, 5, 6 and 11.
- **Brevity.** At 6 pages, the guide is within the 5–8-page model range and has little padding; see item 14.

## What works and should be kept

- **The overview.** Theorems 1–3 come with short proofs an adult can follow: the blocking argument, the first-trouble argument, forced moves, and decoding a path to a train. Theorem 4 is honest about computer evidence and the open problem, with a correct hand proof for one seven-car train. The paragraph on what counts as evidence, apart from the one sentence in Must-fix 1, and the line "honest evidence for a false conjecture" are exactly what the standard asks for.
- **The launch on 2 1.** It has no task overlap, no possible wrong move and a labelled input, middle and output, and it tells the adult explicitly not to drive 2 3 1.
- **The K–1 plain-words key in a box,** placed where the parent needs it. Also keep "If the adult is moving cars, go back to three-car trains" and "adult choice of moves means the task should shrink".
- **The completeness arguments for every "find all" problem:** by first car, by position of the largest car, and the 14 grids against Problem 1's count. Also keep K–1 Problem 6's account of which stuck trains are new.
- **The two routes to 42 in 2–3 Problem 7,** each checked by its own reasoning, and the 4–5 note that the long siding is what makes 132, not 131.
- **The Status paragraph** names every physically untested point, and the closing list says what to record.
