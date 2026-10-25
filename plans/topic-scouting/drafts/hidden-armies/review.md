# Review of the Hidden armies draft (hidden-armies-v1)

Reviewer: critic stage. I did not edit the draft. I read PROMPT.md and every source file, rendered all 17 pages (K–1 6, grades 2–3 5, grades 4–5 6) at 80 dpi with close-ups at 150 dpi, rebuilt the three PDFs from a scratch copy of `draft/src/build.py` (the text matches the delivered PDFs, and the LaTeX logs have no overfull, underfull or warning lines), and checked every answer with my own enumeration code, separate from the author's `check_answers.py`.

## Verdict

This is a strong draft. It follows the outline closely. Every band opens with play, the counter-plan idea and the cycles come before the explanations, and each band ends with deeper material (fewest cubes, unequal armies, mixed plans). The pages carry no titles, encouragement, hints or Name/Date fields. Headers and footers are consistent. Every given plan, count and claimed answer that I checked is correct.

The draft still has five problems worth fixing before the organizer sees it:

1. **K–1 Problems 2 and 4 tell children to find something that does not exist.** With 4 or 5 cubes there is no unbeatable plan. The near-even plans are so hard to beat that children and the non-mathematician parent at that table are likely to "find" a false answer.
2. **Grades 2–3 Problem 7 has a rule that rules out one of its own answers.** The rule allows only fewer cubes, but beating 1-1-1 needs 4 cubes, which is more than 3.
3. **Grades 2–3 Problem 3 and grades 4–5 Problem 2 print a false general claim** ("beat any plan"), which the next problem then contradicts.
4. **Some K–1 recording boards have no clear purpose (Problems 2 and 4), and others are too small for kindergarten drawing (Problem 7).**
5. **K–1 Problem 5 says "group of three plans" over a box that shows six pictures.**

Everything else below is a smaller suggestion.

---

## Must fix

### M1. K–1, page 1, Problem 2, and page 3, Problem 4: the wording assumes an answer that does not exist

Quoted text:
- P2: "Find a plan with 5 cubes that nobody can beat."
- P4: "Find a plan that nobody can beat when each player has 2 cubes, then 3 cubes, then 4 cubes."

Evidence from enumeration:
- 1 cube: every plan is unbeaten.
- 2 cubes: only 1-1-0, 1-0-1 and 0-1-1 are unbeaten.
- 3 cubes: only 1-1-1 is unbeaten.
- 4 or more cubes: **no plan is unbeaten**. I checked every N up to 12.

So two of the four cases these problems pose have no answer, yet the wording promises one. That is a false premise, and it is risky for this table for two reasons:
- **The near-even plans are very hard to beat.** With 4 cubes, 2-1-1 (or 1-2-1, 1-1-2) is beaten by exactly one of the 15 plans: 0-2-2 in the matching arrangement. With 5 cubes, 2-2-1 and its arrangements are beaten by only 2 of the 21 plans: 3-0-2 and 0-3-2 for 2-2-1. A pair of kindergartners testing 2-1-1 will very likely fail to find 0-2-2 and decide they have succeeded. The page told them success is possible, so they have no reason to doubt it.
- **The adult at the K–1 table is the parent volunteer, who is not a mathematician, and the deliverable has no answer key.** Reading "Find a plan…", the adult will reasonably keep children searching, or accept 2-1-1 or 2-2-1.

The older bands already pose this as an open question ("Is there a plan with 6 cubes that nobody can beat?"). AGENTS.md also asks for open questions rather than prescribed conclusions.

Smallest fix:
- P2: "Your partner can see your plan and tries to beat it. Is there a plan with 5 cubes that nobody can beat?"
- P4: "Is there a plan that nobody can beat when each player has 2 cubes? 3 cubes? 4 cubes?"

Both stay within two short sentences for reading aloud.

### M2. Grades 2–3, page 5, Problem 7: the rule rules out the answer for 1-1-1

Quoted text: "Now you may use fewer cubes than your partner. Beat each plan below with as few cubes as you can." The list includes "3 cubes: 1 1 1".

Evidence: the fewest cubes that beat 1-1-1 is 4 (for example 0-2-2, 2-1-1 or 2-2-0). No plan with 3 or fewer cubes beats it, by enumeration. Under the printed rule, which allows fewer cubes but not more, 1-1-1 cannot be beaten at all. A careful child answers "impossible", while the general rule the problem is building toward (sum of the two smaller hills plus 2) says 4. 2-2-2 needs 6, the same as the partner, which is allowed. 1-1-1 is the only case that needs more.

The 4–5 version already has the right wording. Smallest fix: "Now the two players may have different numbers of cubes. Beat each plan below with as few cubes as you can. …"

The contrast is worth keeping: 1-1-1 is the one plan that costs more than the partner spent.

### M3. Grades 2–3, page 2, Problem 3, and grades 4–5, page 2, Problem 2: a false universal claim

Quoted text:
- 2–3 P3: "Then explain how you can beat any plan that your partner names."
- 4–5 P2: "Then explain a way to beat any plan that your partner names."

Evidence: this claim is true only from 4 cubes up. With 3 cubes, 1-1-1 cannot be beaten. With 2 cubes, 1-1-0 cannot be beaten, and with 1 cube nothing can be. The very next problem in each band (2–3 P4, 4–5 P3) is built on that exception, so the page states a claim and then asks children to find its counterexamples. The tension is good mathematics, but the printed sentence prescribes a conclusion that is false. A child who absorbs "any plan can be beaten" may also answer the next problem wrongly ("never") without testing.

The counter-plan rule (take 2 from the biggest hill, add 1 to each of the others) needs a biggest hill of at least 2. That condition is exactly what fails at 3 cubes, and it is what the 4–5 children should discover.

Smallest fix, with either wording:
- Keep it open: "Then explain how to beat a plan that your partner names, whatever it is, or find a plan you cannot beat."
- Restrict it truthfully, without giving a hint: "…beat any plan with 6 or more cubes that your partner names."

The first wording connects better to the next problem.

---

## Should fix

### S1. K–1, page 1, Problem 2, and page 3, Problem 4: three blank boards per row with no clear purpose

P2 shows one row of three blank boards beside five cube icons. P4 shows three rows of three. A child cannot tell what to draw on them:
- The plan they offered, or the partner's counter?
- Their best candidate?
- One board per answer?

In P4 the count of three boards also matches the three unbeaten 2-cube plans (1-1-0, 1-0-1, 0-1-1). For 3 cubes, though, there is one answer, and for 4 cubes there is none. A child may feel obliged to fill three boards in each row.

The older bands solve this with "plan shown / plan that beats it" columns.

Fix, either way:
- Pair the boards as "shown" and "beats it". In K–1 this could be two boards joined by a small arrow, with no words.
- Drop the drawing from P2, keep it as a play problem, and give P4 one board per cube count, labelled as extra space if more are kept.

### S2. K–1, page 6, Problem 7, and pages 1 and 3: the drawing boards are small for kindergarten hands

Measured from the source:
- P7 answer boards are about 4.1 cm wide and 3.4 cm tall. The hills are 1.3 cm apart, with 2.6 cm of space above each hill. Answers need towers up to 4 cubes (0-1-4 beats 4-0-1), so a child must draw squares smaller than 6.5 mm in a column about 1 cm wide. The boards also nearly touch one another.
- P2 and P4 boards have 3.0 cm above the hill at 1.5 cm spacing.
- P3 and P6 have 3.4 cm at 1.8 cm spacing. These are the most workable.

The standard asks for boards "at a size they can work on". K–1 P7 is the problem where children produce the most drawings (up to 9 on one plan).

Fix: move P7's second plan (4-0-1, with 9 boards) to its own page so the boards can grow to the P3 size. Alternatively, accept dots or numerals per hill, but the recording would then need a one-line demonstration at launch, which belongs in facilitator notes.

### S3. K–1, page 4, Problem 5: "group of three plans" over a box of six pictures

Quoted text: "Build the two plans in each row and circle the winner. In each group of three plans, is one plan the best?"

Each framed box holds six pictures: three rows of two. The three distinct plans each appear twice, sometimes on the left and sometimes on the right (0-0-5 is on the right in row 2 and on the left in row 3). A K–1 listener must first realize that the six pictures are only three plans. Only then can they ask whether one plan circled twice is "best".

The mathematics is right:
- Group 1: 2-2-1 beats 4-1-0 and 0-0-5, and 4-1-0 beats 0-0-5, so 2-2-1 is best.
- Group 2: 0-1-4 beats 2-0-3, 2-0-3 beats 1-2-2, and 1-2-2 beats 0-1-4, so there is a circle and no best plan.
- The contrast between the two groups is excellent.

Only the presentation hides it.

Fix:
- Option 1: show each group's three plans once, side by side in the frame, and say: "Play every two of these plans against each other. Is one plan the best?" This removes the six duplicate pictures, frees space, and lets children choose the pairings, though there are only three.
- Option 2: keep the rows and say "In each box, is one plan the best?"

### S4. Grades 4–5: pages 5–6 put the deepest problem before easier ones

The 4–5 order is:
- P4: rank the 28 plans
- P5: which plans lie on a circle
- P6: mixed plans by die roll (the outline's "4–5 continuation" and the most abstract idea in the packet)
- P7 and P8: fewest cubes and unequal armies

P7 extends P2's counter-plan rule directly, and it is more accessible than P6. PROMPT.md says deeper and more abstract questions belong late. A child who finishes P2–P3 and wants more of the same will skip past the large pooled P4 table and the hard P6 to reach P7.

Suggested order:
1. P1–P3, unchanged.
2. Fewest cubes (now P7), then P8.
3. Ranking the 28 plans (now P4), then circles (now P5).
4. Mixed plans (now P6) last.

This is the organizer's call. Present it as an option, not a defect.

### S5. Grades 4–5, page 2, Problem 3: limited to 1–5 cubes, so the boundary at 4 stays implicit

Quoted text: "When each player has 1, 2, 3, 4 or 5 cubes, is there a plan that nobody can beat? Explain which numbers of cubes have a plan like that, and why."

The outline asks 4–5 to "explain the counter-plan rule for any number of soldiers, find why 3 soldiers is different". The full theorem is that unbeaten plans exist exactly for 1, 2 and 3 cubes. With the list capped at 5, children can answer by checking cases without connecting to P2's rule.

The two sentences also ask nearly the same thing twice.

Fix: "For which numbers of cubes is there a plan that nobody can beat? Explain." This is one shorter question that covers every N and invites the link to P2's rule (it works whenever the biggest hill has at least 2 cubes).

### S6. Grades 4–5, page 3, Problem 4: count circles are 6 mm across

Each of the 28 count circles has a radius of 0.3 cm. The counts run up to 12 (2-2-2), so two digits must fit in a 6 mm circle. Fix: use a radius of 0.42–0.45 cm. The rows are 1.6 cm apart, so there is room.

A related pacing note for the facilitator, not for the page: the full table is 378 games, or 189 if children notice that rearranging the hills of a plan does not change its count (7 types × 27 games). Even pooled among three children it can fill most of the session. The symmetry is the key discovery, so it should stay off the page.

---

## Minor

- **Redundancy (older bands).**
  - 2–3 P3 and 4–5 P2: "with a plan that has the same number of cubes" repeats both the shared rule and the row labels ("6 cubes", "7 cubes", …). Suggest "Beat each plan below."
  - 4–5 P1 says "6 cubes" three times in three sentences: "Play the game with 6 cubes each. Is there a plan with 6 cubes that nobody can beat? … try to beat it with 6 cubes."
  - 2–3 P2 repeats it twice.
  - Trim to one mention per problem.
- **K–1 shared rules, page 1.** Ten sentences, about 95 words, are long for a single read-aloud to kindergartners. The launch demonstrates the game, so this is tolerable. If anything is trimmed, the tie-game sentence is the least essential for 5-cube play, though it matters when two hills are tied. Low priority.
- **K–1 P6 and the shared rule.** The rules say "put all your cubes on the three hills". P6 ("as few cubes as you can") changes that without the explicit "Now…" sentence the older bands use. The wording itself works when read aloud. Consider "You may use any number of cubes. For each plan below, draw a plan that beats it with as few cubes as you can." The 1-1-1 row, a 3-cube plan that needs 4, is a nice surprise. Keep it.
- **Grades 2–3 P5 and P6 order.** P5 asks for a circle containing 2-2-2 before P6 asks for every plan that beats 2-2-2. Any such circle must pass through 3-3-0, 3-0-3 or 0-3-3, since these are the only plans that beat 2-2-2. Swapping the two problems would let the enumeration feed the construction. Either order works, because P5 by trial is also fine.
- **Grades 2–3 P6, second part (all 15 plans that beat 6-0-0).** This is a good organized-listing task, but it does not connect to P5's 6-0-0 question, which depends on what 6-0-0 beats (nothing), not on what beats it. It is fine as is. Just note that it is a listing exercise, not part of the circle argument.
- **Grades 4–5 P6** needs no die (the problem is a thought experiment), but children may want to play it. If the organizer wants that, add a die to the materials list. Nothing on the page needs to change.
- **"Week NN"** is still a placeholder in every header and footer, as in the outline. It must be filled in before printing.
- **Internal only:** `check_answers.py` labels the K–1 checks "P2" (the four counter-plans) and "P3" (no unbeaten 5-cube plan), but those are Problems 3 and 2 on the page. It also labels the P8 checks "P7". The checks themselves are right. Relabel them if the reviser relies on the script.

---

## Independent mathematical check (all correct unless listed above)

I computed everything with my own enumeration of plans and pairwise results.

**General facts**
- Unbeaten plans: N=1, all 3 plans; N=2, the arrangements of 1-1-0; N=3, 1-1-1 only; N=4 to 12, none.
- There are 28 six-cube plans.
- 2-2-2 beats 12 and is beaten by 3 (the arrangements of 3-3-0). It is the unique maximum.
- 6-0-0, 0-6-0 and 0-0-6 beat 0 and are each beaten by 15.
- The arrangements of 3-2-1 beat 11. Other counts: 4-1-1, 3-3-0 types 9; 4-2-0 types 8; 5-1-0 types 5.
- There are 180 three-plan circles. Every plan except 6-0-0, 0-6-0 and 0-0-6 lies on one.
- Two circles cover all six remaining types: 0-2-4 → 3-1-2 → 1-5-0 and 2-2-2 → 4-1-1 → 3-3-0. So the four triangles in 4–5 P5 are enough.
- The outline's circle 0-1-5 → 2-0-4 → 1-2-3 is correct.

**K–1**
- Rules picture: 2-3-0 beats 1-0-4, and the tokens are on the correct hills.
- P3: every given plan can be beaten with 5 cubes. Numbers of beaters: 5-0-0 has 10, 0-4-1 has 6, 0-3-2 has 4, 2-1-2 has 2 (3-2-0 and 0-2-3).
- P5: winners and groups are as described in S3.
- P6: fewest cubes are 2, 3, 4, 5 and 4 for 5-0-0, 1-4-0, 1-3-1, 2-2-1 and 1-1-1.
- P7: 3-1-1 has 3 beaters (0-2-3, 0-3-2, 1-2-2). 4-0-1 has 6 beaters (0-1-4, 0-2-3, 0-3-2, 1-1-3, 1-2-2, 2-1-2). The 6 and 9 boards do not give away the counts.

**Grades 2–3**
- P3: the counter-plan rule beats all nine given plans with the same number of cubes.
- P4: 1-1-1, and none with 4 cubes.
- P5: 12 circles contain 2-2-2, for example 2-2-2 → 4-1-1 → 3-3-0. No circle contains 6-0-0.
- P6: 3 plans beat 2-2-2, and 15 beat 6-0-0 (the second and third hills each at least 1). The 6 and 20 boards are enough.
- P7: 2, 4, 5, 6, 5, 4, 4 and 7 for 6-0-0, 4-1-1, 3-2-1, 2-2-2, 3-3-0, 1-1-1, 8-1-1 and 5-3-2, matching "two smaller hills plus 2". The only problem is the 1-1-1 rule clash in M2.

**Grades 4–5**
- P2: all nine given plans can be beaten, including 34-33-33 and 50-0-50 (for example 48-1-51).
- P3 as above.
- P6: Ben's die (arrangements of 3-2-1) is exploited by 3-3-0, 3-0-3 or 0-3-3, which beat 2 of his plans and lose to 0. Against Mia's die (arrangements of 4-2-0), no six-cube plan beats more than it loses to. Her mixture holds every opponent to a net of 0 or less, so it is an optimal strategy for this game. That makes the problem a genuine instance of Borel's point and worth keeping.
- P7: 40-30-30 needs 62 (0-31-31), and no 61-cube plan beats it.
- P8: 8 cubes (3-3-2 type) is the fewest that no 6-cube plan beats. 9 cubes (3-3-3) is the fewest that beats every 6-cube plan, and no 8-cube plan does.
- The "fewest = two smaller hills + 2" rule holds in general. Winning one hill and tying the other two costs N + 1, which is never cheaper when the biggest hill is at least 1.

## Format and standard checklist

| Check | Result |
|---|---|
| Header and footer | Consistent on all 17 pages, with page numbers. |
| Problem numbering | Consecutive in each band. |
| Name/Date fields | None. |
| Extra titles or section labels | None. The column labels ("plan shown", "Ben", "Mia", "6 cubes") are labels inside diagrams. |
| Exclamation marks, encouragement, "Let's" or talk about the activity | None. |
| Dashes used for asides | None. |
| Hints or method suggestions | None, apart from "Share the work" in 4–5 P4, which follows the outline's pooling plan and is acceptable. |
| Worked visual for the strip notation | Present: towers on the mat → 3-0-2 strip, using a non-task 5-cube example. |
| K–1 sentence length | Every problem is two sentences or fewer. |
| Pages per band | 6, 5 and 6, meeting the "four or more" standard. Each band has more than 40 minutes of work, and stopping anywhere is fine. |
| Overflow or overlap | None found. In 4–5 P2 and 2–3 P3/P7, the last answer row sits close above the first writing line, but they do not touch. |
