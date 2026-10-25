# Review: Counting-out circles, draft v1

Reviewer stage. I rendered every page of the three draft PDFs (K–1: 6 pages, grades 2–3: 4 pages, grades 4–5: 5 pages), read the sources in `draft/src/`, and checked every answer with my own simulation (written separately from the author's `check.py`). I did not edit the draft.

## Verdict

This is a strong draft. The mathematics is correct throughout. The format follows the standard: one header and footer, "Problem N:" labels, no titles, no encouragement, no hints, no Name/Date lines, and no overfull boxes. The sequence works: act it out, build a table, predict, explain, then generalize. Several problems are excellent and should be kept as they are (see "Keep" at the end).

Two problems need fixing before printing:

1. No page says that the turn-taking carries on past person 1, and the planned 8-person launch never shows it.
2. The pages depend on mats that are not in the packet, and the specified mat sizes do not fit the stated paper.

There are also medium-sized design issues in K–1 (look-up problems, duplicated problems, circles the rules prevent you from playing) and in the ordering and wording of grades 2–3 and 4–5.

## Mathematics check (all correct)

Every second person sits (J):

- n = 1–16: 1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9, 11, 13, 15, 1
- J(20) = 9, J(25) = 19, J(32) = 1, J(50) = 37, J(100) = 73, J(1000) = 977
- J(26) = 21, J(52) = 41, J(53) = 43

Every third person sits (J₃):

- n = 1–12: 1, 2, 2, 1, 4, 1, 4, 7, 1, 4, 7, 10
- n = 13–24: 13, 2, 5, 8, 11, 14, 17, 20, 2, 5, 8, 11
- J₃(30) = 29, J₃(41) = 31

Problem by problem:

- **K–1:**
  - P1: circles 3, 4, 5, 6 give 3, 1, 3, 5.
  - P2: circles 7 and 8 give 7 and 1.
  - P3: number 1 is last in circles 2, 4 and 8.
  - P4: circle 16 gives 1.
  - P5: number 5 is last in circles 6, 10, 18, …; number 3 in circles 3, 5, 9, 17, ….
  - P6: no, because 2 always sits on the first count.
  - P7: circles 3, 4, 5, 6 give 2, 1, 4, 1.
  - P8: circles 7 and 8 give 4 and 7.
- **Grades 2–3:**
  - P3: exactly the even numbers can never be last. No even survivor occurs for n ≤ 2000, and every odd number 2L+1 is last for n = 2^m + L.
  - P5: number 9 is last for n = 12, 20, 36. The last one standing equals n for n = 1, 3, 7, 15, 31.
- **Grades 4–5:**
  - P3: n = 1, 2, 4, 8, 16, 32, 64.
  - P6: number 21 is last for n = 26, 42, 74. Number 22 is never last.
  - P10: the printed facts (13 is 1101, 11 is 1011, J(13) = 11) are correct. Rotating the leading 1 to the end checks out for all n < 2000.

## Must fix

### 1. The rule never says the turns carry on past 1, and an 8-person launch hides this (all bands)

**Where:**

- K–1 rule, p. 1: "Start at 1 and go round and round the circle saying stand, sit, stand, sit."
- 2–3 and 4–5 rule, p. 1: "The standing counters take turns: 1 stays standing, the next one sits down, … and so on."
- 2–3 and 4–5 P7: "1 and 2 stay standing, 3 sits down, … and so on."

**Problem:** The whole activity depends on continuing the alternation across laps. In a circle of 3, the turns go 1 stays, 2 sits, 3 stays, then **1 sits**. A child who starts each lap afresh ("1 stays standing" again) gets **1 as the last one standing for every n**. My simulation of that misreading returns 1 for all n = 1–16, so the table, the pattern and every later problem collapse. With every third person sitting, the misreading is not even well defined: in a circle of 2, nobody ever sits.

The planned launch makes this worse. The outline says about eight children play once, and 8 is a power of two. Every lap in a circle of 8 has an even length (8, 4, 2), so every lap really does start with 1 staying. The one demonstration children see is consistent with the wrong rule. It also gives away J(8) = 1, which is the discovery K–1 P3 is built around.

The K–1 table is most exposed. It is staffed by the non-mathematician parent, and K–1 P3 would then read "number 1 wins every circle."

**Fix on the pages:** Add one rule sentence to each band's opening rules. This states a rule; it is not a hint.

- K–1: "Keep going past 1 without starting over."
- 2–3 and 4–5: "When you come round past 1 again, keep taking turns from where you left off." This also covers the every-third rule in P7.

If the reviser wants a visual, a small strip for a non-task case would do. For example, a circle of 3 drawn twice: after the first lap (2 flipped), then with 1 flipped. But 3 is a task case in every band, so the sentence alone is probably better.

**Fix outside the pages (for the organizer's outline and launch):** Launch with all 11 children, or with 10, instead of about 8.

- With 11 people, the sitting order is 2, 4, 6, 8, 10, **1**, 5, 9, 3, 11, and 7 is left standing. Person 1 sits at the first wrap, so the carry-over is unmissable, and nobody is left out.
- With 10 people, the order is 2, 4, 6, 8, 10, 3, 7, **1**, 9, and 5 is left standing.

Either size avoids priming "1 wins."

### 2. The pages depend on mats that do not exist yet, and the specified mats do not fit Letter paper

**Where the pages rely on mats:**

- K–1 P4: "play it on the mat with 16 spots". The ring printed on the page has 0.66 cm spots, which are too small for counters.
- 2–3 and 4–5 rules: "put counters on spots 1 to 10 of the mat".
- 2–3 and 4–5 P2: "play them on the mat with 32 spots".
- 2–3 P9: a circle of 30 with every third person sitting, which needs the 32-spot mat if played.

**Problems:**

- **The 32-spot mat is not settled.** The outline's materials list says "a second mat with 24 or 32 spots", but P2 needs 32, because a 24-spot mat cannot play 25 or 32. Pin it to 32 in the materials.
- **The 16-spot mat does not fit.** The outline specifies 3 cm spots on a 22 cm circle, which is about 25 cm across plus labels. US Letter is 21.6 cm wide, and the session context says pages print on Letter at 100%.
- **A counter-sized 32-spot circle does not fit either.** With 2.6 cm spots and small gaps, 32 spots need a ring about 29.5 cm across (about 32 cm with spots). That is wider than tabloid's 27.9 cm short side. It needs two taped Letter sheets or a stadium-shaped loop on tabloid paper.
- **Counter size is unchecked.** The K–1 working rings have 2.6 cm spots with only about 0.25 cm between neighbouring spots in the 5- and 6-rings. Standard 1-inch (2.54 cm) two-colour counters fit. Counters near the outline's "3 cm" would overlap neighbours. No one has rehearsed this.

**Fix:**

- Either add the 16-spot working ring as a page in each packet, or name exactly where the mats come from. A 16-spot ring with 2.6 cm spots is about 14.8 cm across (17.4 cm with spots), so it fits on a Letter page. K–1 P4 could simply print this full-size ring and play on the page, which removes one loose material from the parent volunteer's table.
- Settle the 32-spot format in the materials list. Mark physical fit as untested until someone rehearses with the actual counters.

## Should fix

### 3. K–1 P3 and P5 are mostly look-ups, and the K–1 rule blocks the circles P5 needs (K–1 pp. 3–4)

**P3** ("Find every circle where number 1 is the last one standing", with thumbnails of circles 2–8): every case except the circle of 2 was already played and ringed on pp. 1–2. The task is to flip back two pages and copy, which is about a minute rather than five. The circle of 2 is printed only as a thumbnail with 0.44 cm spots. The K–1 rule ("Put a counter on every spot") means it cannot be played on the 16-spot mat either.

**P5** ("How many people should be in the circle so that number 5 is the last one standing? So that number 3 is the last one standing?") has three issues:

- **Wording.** "Should be" implies a single answer, but the answers are 6 and 10 for number 5, and 3, 5 and 9 for number 3.
- **Cases within reach.** Among the circles K–1 can play (3–8 and 16), the only answers are 6, and 3 and 5. Both are look-ups again. A child who wants to look further (9, 10) cannot under the K–1 rule.
- **Wrong noun.** K–1 never calls the counters "people".

**Suggested fix:**

- Give K–1 two more big rings, for 9 and 10, on one page laid out like P2. The 9-ring needs radius about 4.2 cm and the 10-ring about 4.7 cm at the current spot size.
- Pose P5 as a real search over the played circles: "Which circles leave number 3 standing? Which leave number 5 standing?" Use "counters", not "people".
- Results for 3–10 are 3, 1, 3, 5, 7, 1, 3, 5. Children see 3 and 5 come round again after 8. That is the K–1 version of the reset pattern older bands find in their tables.
- Optionally add one K–1 record strip ("counters 2 3 4 5 6 7 8 9 10 / last one") so P3, P4 and P5 read from one place instead of scattered rings. This matches the outline's record strip and the guidance to prefer one recoverable record.
- Fold P3 into P4: "Find every circle where number 1 is last. Guess who will be last in a circle of 16, then play it." This gives one problem of real length whose noticing feeds straight into the guess.

### 4. K–1 P2 repeats P1, and P8 repeats P7 (K–1 pp. 2 and 6)

- **P2** has exactly P1's wording ("Play each circle. Draw a ring around the number of the last one standing.") for circles 7 and 8. It is one task split at a page break.
- **P8** ("Draw a ring around the number where you should stand to be the last one standing") is P7 with circles 7 and 8. Choosing where to stand is the same thing as playing the circle and ringing the survivor. A K–1 child may be confused about whether "you" means picking a spot before playing.

**Fix:**

- Either merge each pair into one problem that runs across two pages, or give the second problem its own job.
- A real K–1 inverse question for stand, stand, sit would work: "Which of your stand, stand, sit circles left number 1 standing?" The answers among 3–8 are 4 and 6.
- If the "where should you stand" story is wanted, use it once for a circle the child has not yet played.

### 5. Grades 2–3 ordering: abstract questions come before concrete ones, and the narrower explanation comes last (2–3 pp. 2–3)

The current order is:

- P4: circles of 50 and 100, with an explanation
- P5: inverse search up to 40
- P6: explain why 16 and 32 leave number 1
- P7: concrete acting with every third person sitting

Two issues:

1. **P6 should come earlier.** It is the most concrete explanation, about circles the children just played in P1 and P2. The far prediction in P4 builds on that halving-and-restart idea, so P6 should come before P4.
2. **Children who stall have nowhere concrete to go.** A third grader who stalls on P4 meets two more abstract problems before the next thing they can act out (P7). The context says the first problems should let everyone start right away, deeper problems come late, and stopping anywhere is fine. Stopping is fine here, but a child who is stuck is not routed to work they can do.

**Suggested order:** P1, P2, P3 (evens), P6 (why 16 and 32), P5 (inverse), P4 (50 and 100), then P7–P9. Alternatively, move P7 and P8 forward to follow P3. Grades 4–5 can keep its order, because the organizer is at that table and P3 to P4 already runs from the powers of two to the general rule.

### 6. Grades 4–5 P10: binary is introduced cold, and the one example fits a rival rule (4–5 p. 5)

**Prerequisite.** According to the session context, this group has had two sessions (tiling and lamps), so no binary week has been used with these children. P10 introduces binary in one sentence with two examples. Filling seven more rows needs the place values 16, 32 and 64, which the page never shows.

**Fix:** Head each "in binary" column with place-value boxes (32 16 8 4 2 1) so children write digits under them. This is a representation, not a hint, and it makes the conversion something to do rather than something to know.

**Rival rule.** "Reverse the digits" also turns 1101 into 1011. Reversal matches J(n) for n = 1, 2, 3, 4, 7, 8, 10, 13, 15, 16, and fails only on 5, 6, 9, 11, 12, 14. A child who tests 7, 10 and 15 will confirm the wrong rule.

This can be a good conjecture-testing moment if the organizer knows about it. If not wanted, print a different example that rules out reversal, for example 12 = 1100 giving 9 = 1001 (reversal gives 0011 = 3). Either way, record it for the facilitator.

### 7. Grades 2–3 P5, second part, can be misread (2–3 p. 2)

"find every circle up to 40 people where the last one standing has the biggest number in the circle". This can be read as "which circle up to 40 has the biggest survivor", which gives the single answer 31.

**Fix:** "…where the last one standing has the same number as the number of people in the circle." The answers are 1, 3, 7, 15, 31.

## Smaller points

- **2–3 and 4–5 P8, "Then play two of them to check".** Children who pick 19 and 20 never test the wrap-around step. Up to 12, most wraps land on 1 (n = 4, 6, 9), so children may conjecture "drop back to 1". Then 14 (answer 2) and 21 (answer 2) refute it. Consider naming the check cases ("Then play circles of 14 and 20 to check" for 2–3; "14 and 21" for 4–5). Choosing the cases is the page's job, so this is not a hint. Otherwise leave it, and tell the facilitator which checks are informative.
- **4–5 P6, "Do the same for number 22."** The answer is none. Impossibility is exactly where the standard wants an explanation, so add "If there are none, explain why." Also, P5's statement ("Number 21 is the last one standing in a circle of 26 people") hands over the first answer to P6's number-21 list. Either use a different number in P6 (for example 19: n = 25, 41, 73) or accept it as intended linkage.
- **4–5 P3 answer box.** At 5.6 cm high it is small for a list plus the main explanation in the 4–5 band (why powers of two leave 1), and unlike 2–3 P6 it has no ring to draw on. Enlarge it, perhaps moving P3 to its own half page, and consider a small 16-ring inside the box as in 2–3 P6.
- **2–3 P6 ring.** It is very small (0.42 cm spots, footnote-size labels) and sits in the left third of a large box. A ring 7–8 cm across would make a usable drawing for the halving argument.
- **K–1 P4.** There is nowhere to record the guess before playing, so a guess made after the fact is not a prediction. A small box, or "Tell your guess first", would help. If the full-size 16-ring from item 2 is adopted, it also removes the question of whether to ring the mat or the page.
- **Mixed nouns.** "Counter" (2–3 and 4–5 P7, P8) and "person" (4–5 P9, P10) are mixed in the upper bands. Harmless, but pick one per band.
- **Small circles on the 16-spot mat (2–3, 4–5).** For n = 2–6, the "leave the other spots empty" convention leaves 10–14 empty spots between the last counter and 1. It works, and the rule covers it, but children may lose sight of the circle closing. Facilitator note only.
- **Header and footer.** "Week NN" is a placeholder in all three headers and footers. It is fine for the draft, but fill it in before printing.
- **Table row labels.** "people" and "last one standing" sit slightly above the vertical centre of their cells. This is cosmetic.

## Pacing and age-fit notes (hypotheses, not piloted)

- **Counting errors are the main risk, and nothing on the table catches them.** The flipped counters record who is sitting. Nothing records whose turn it is, or whether the next standing counter "stays" or "sits". That turn lives only in the child's head, which is the same weakness as the lamp rule that existed only on paper. One wrong table entry hides the pattern. Two ideas for the materials and launch rather than the page:
  - a pointer token moved to each standing counter as it is counted;
  - in each pair, one child chants while the other flips.

  Pooling tables across pairs at the 2–3 table will expose disagreements. The 4–5 table has only one pair, so the organizer should spot-check.
- **Grades 4–5 time.** P1 and P2 are about 194 flips for a single pair plus a referee. That may take 15–20 minutes, so P3–P6 may be the realistic first-visit reach, with every third person and binary as return-visit material. That is fine under the standard ("finishing every page is not the goal"). The organizer may want the three children to split the circles in P1.
- **K–1 load looks right.** It has 8 problems over 6 pages and about 40 minutes of K–1 work if the counting runs smoothly, and each problem is one or two sentences read aloud. After the fixes in items 3 and 4, it should still meet "as much to do as the other bands."

## Keep

- **K–1 P6** ("Can number 2 ever be the last one standing? Explain."). It is a real impossibility question at K–1 scale, with an object-level explanation (2 always sits on the first count). It pairs with 2–3 P3.
- **2–3 P3** (which numbers can never be last).
- **4–5 P5** (from 26 to 52 and 53: the recurrence posed concretely without notation).
- **4–5 P6** (the number-22 trap) and **4–5 P9** (41 people, every third person: the classic survivor 31).
- **Large K–1 working rings** with numbers outside the spots, so counters never cover them.
- **The grades 2–3 and 4–5 rule paragraph's mapping** ("To play a circle of 10 people, put counters on spots 1 to 10"), which makes one mat serve every circle size.
