# Week 94 K–1 Problems 4–6 and guide p. 3: independent review

Reviewer: Claude (critic stage; not the writer). October 23, 2026. Read from origin/main at 48976ba (Week 94 change a4b598d).

Reviewed: `lowell-math-circle-year-2/week-94/week-94-k-1.pdf` (W94-K-v2, 4 pp.; new pp. 3–4 with P4–P6), `week-94-facilitator.pdf` (W94-F-v2; K–1 route on p. 2, K–1 page p. 3, overview p. 1), and the problem files 10, 11, 12 and 14 with `template.tex`. All four K–1 pages and guide pp. 1–3 were rendered with `pdftoppm -r 80` (pp. 3–4 also at 150 dpi) and inspected. The reference copy in `editable/reference-pdfs/` is byte-identical to the delivered K–1 PDF. The K–1 band view prints P1–P6.

Standard applied: `worksheet-workflow/blocks/spec.md`, `neg.md`, `exemplars.md`, `context.md` (one parent volunteer at a K–1 table of two kindergartners and two first graders, children in two pairs) and AGENTS.md.

## Verdict

The must on the card is fixed in substance. K–1 now plays the secret-extra machine with cube towers, meets the several-worlds idea (outputs 4 and 6 fit three input pairs with Q always 2 taller), and then uses a known tower to pick one pair. That follows the 2–3 order (P1, P2–P3, P4) at a smaller scale, and every number checks. I found no must. There are four shoulds. They are all about the rules a five-year-old has to keep without the adult: which towers share one extra, how the secret stays fixed and gets checked, how much is written during the game, and one claim in the guide that has not been observed.

## Checks run

`scripts/k1_check.py` in this folder reads the drawn heights from the problem-file TikZ and checks the answers by brute force. Output is in `k1_check.out`.

- P5: the drawn outputs are P 4 and Q 6. With one shared extra in {1, 2, 3} and towers of at least one cube, the worlds are (3, 5), (2, 4) and (1, 3), and Q − P = 2 in all of them. That is 3 answers in 4 slots, with a tallest answer of 5 in 6-cell columns. Cube count: 18 for the answers, 28 with the two outputs.
- P6: the known towers are 1→2, 2→5 and 3→5. Each gives exactly one extra (1, 3, 2), so P and Q are (3, 5), (1, 3) and (2, 4). That is P5's three pairs, each once, and each fits the 6-cell columns.
- Worked example: 2 in, 1 extra, 3 out. It is not a P6 machine and it reveals neither P5's list nor its difference.
- P4: any single known tower identifies the extra.
- Misreading P5 with a separate extra for each tower gives 9 pairs, including P = Q = 3 (finding 1).
- The guide's P5 extension, extras up to 5, has one more world, (0, 2), if an empty tower counts (finding 9).
- The week's own `editable/check_math.py` also passes. Its K–1 data are typed in by hand, so the check above reads them from the source instead.

## What works (keep)

- **The sequence.** The machine is played first (P4). Then the outputs alone leave several worlds (P5), and a known tower collapses them (P6). Each step is something children build and see. P6's second and third machines both turn out a 5-cube tower from different inputs, which is a good contrast: the input matters.
- **The worked visual on p. 3.** It shows "in: 2 cubes → add 1 extra → out: 3 cubes", with a labelled intermediate step, before first use. It is a non-task instance. The darker extra cube is in the middle frame only, and the output is one shade, which matches the guide's colour rule.
- **The P5 slots.** There are four slots for three answers, so the page does not give away the count. "Could P be taller than Q?" is a real impossibility question that depends on knowing the list is complete. It is the K–1 version of 2–3 P3.
- **The guide.** p. 1 now states the K–1 claim, "three worlds" with c in {1, 2, 3}. The K–1 page has every answer, a reason why the list is complete, a held hint and an extension for each problem, plus a materials paragraph and per-problem times (8 + 7 + 6 minutes). The colour rule for the extra and the 18/28 cube count are details a parent needs.
- **The pages are clean.** The header and footer match the spec. There are no titles, no encouragement, no exclamation marks and no "explain your thinking". The only labels are diagram labels.

## Findings

### 1. should: K–1 p. 3 (shared rule) and p. 4 (P5). P5 never says that P and Q share one extra

> "The extra stays the same for the whole game." (p. 3)
> "Problem 5: Build every pair of towers that could have gone in, and colour each pair you find. Could P be taller than Q?" (p. 4)

**Why:** The shared extra is the mathematics of P5. If each tower may get its own extra, outputs 4 and 6 fit 9 pairs, including P = Q = 3. Then the four slots are too few, and "Q is always 2 taller" is false. The only printed statement of the shared extra ties it to "the whole game", and P5 is not a game. It is a static puzzle on the next page. The terms also clash: the K–1 rule says "game", the K–1 table and the guide say "round" ("keeps it for the round"), and 2–3 says "round". In P4 the keeper changes after "switch jobs", so the extra is not fixed for the whole game anyway. AGENTS.md asks that "task-specific rules and the requested action [go] directly in the numbered problem". P6's "each machine has its own extra" helps after the fact, not during P5.

**Fix:** Make the rule about machines, which covers P4 (each keeper is a machine), P5 and P6. On p. 3, write "A machine always adds the same secret extra: 1, 2 or 3 cubes." Start P5 with "P and Q went into the same machine." In the guide, P4 can then say "keeps it until the jobs switch".

### 2. should: K–1 p. 3, P4, and guide p. 3, P4. Nothing on the page or in the materials fixes the secret, and there is no check

> "Play the machine: choose a secret extra, and behind a cover build what comes out for each tower your partner gives you. Your partner finds your extra; then switch jobs."

**Why:** The secret exists only in a five-year-old keeper's head. Nothing makes the keeper hold it for every tower, and nothing confirms the finder's answer. 2–3 P1 ends with "Reveal it". K–1 has no reveal, and the guide only says the keeper "then shows it". This is the lamp-puzzle failure that `context.md` warns about: a rule that lives only on paper, or in memory, and gets quietly changed. The parent is watching two pairs at once and cannot police both.

The hand-over is also unclear. The page and the guide say neither whether the keeper hands back the tower that went in, nor whether the keeper copies the tower or snaps cubes onto it. The guide's hint ("if the finder handed over their only tower, suggest building a twin") covers only one of these cases.

**Fix:** Let the materials carry the rule. On the page: "...Your partner finds your extra, then lift the cover to check. Switch jobs." In the guide's materials paragraph: "Before the first tower, the keeper snaps that many cubes into a short stick and leaves it behind the folder. Each tower that comes out is a copy of the tower that went in, with that many more cubes, in the tower's own colours. Lift the folder to check at the end of the round." Also say which tower comes back: either the output only (then the finder needs the twin they kept) or both. Then the twin hint follows from that choice.

### 3. should: K–1 p. 3, P4 table. A three-column transcription during a two-person game

> Table columns: "Round | Towers in | Towers out | Extra", four 17 mm rows.

**Why:** The comparison in P4 is physical: the tower that came out sticks up past the twin. Writing every tower's height in and out, for several towers a round, adds transcription to the game. For October kindergartners that can become the main demand. AGENTS.md says "Keep bookkeeping light... Avoid making transcription or memory the main demand". The page does not say who writes (keeper, finder or both), and the guide never mentions the table. The guide's own follow-up, "How few towers did you need?", wants exactly one number a round, and the table does not ask for it.

**Fix:** Change the columns to "Round | Towers you gave | Extra you found". The first column is a count or tally marks, and the guide says the finder fills it in. Across four rounds the column of 1s lets "one tower is enough" show up without being printed as a question. Add one guide sentence: "The finder records; the adult can scribe for a kindergartner."

### 4. should: guide p. 3, P4. An unobserved behaviour is stated as fact

> "Children often ask for several towers at first; afterwards ask 'How few towers did you need?'"

**Why:** The activity is unpiloted, and both the commit and QA.md say the new K–1 pages are unrehearsed. AGENTS.md asks the guide to "distinguish observations from hypotheses". A parent will read "often" as experience.

**Fix:** "Children may ask for several towers at first. If they do, ask afterwards..."

### 5. could: K–1 p. 3, P4. The read-aloud sentence is long for one hearing

> "Play the machine: choose a secret extra, and behind a cover build what comes out for each tower your partner gives you."

**Why:** This is 25 words with three chained actions and an implied role ("you" is the keeper). The spec asks for one or two short sentences per K–1 problem that "make sense after one hearing". The table demonstration before P4 carries much of it, which is why this is a could.

**Fix:** Put "The machine works behind a cover" in the shared rule. Then P4 becomes "Take turns being the machine. Your partner finds your secret extra, then lift the cover to check." This also absorbs finding 2.

### 6. could: K–1 p. 4, P6. The outputs 4 and 6 are not drawn in the three machine panels

> "P and Q still come out as 4 and 6 cubes, but each machine has its own extra."

**Why:** A child on the third panel has to remember 4 and 6 from the sentence, or look back up at P5. Each panel shows the known tower's in and out, but not P's and Q's outputs, which are what the child must take the extra away from.

**Fix:** In each panel's lower half, add small shaded 4- and 6-cube towers labelled "came out", left of the empty P and Q columns. That is the same "came out | went in" layout as P5. The sentence could then shorten to "Each machine has its own extra. Build P and Q for each machine, and color them."

### 7. could: K–1 p. 4, P5 and P6. The colouring cells are small for crayons

**Why:** The answer cells are 7 mm in P5 and 6.5 mm in P6, while the worked example uses 9 mm. Kindergartners colour with crayons, per the guide's materials, and there is about 25 mm of unused space at the bottom of p. 4.

**Fix:** Raise P5 to about 8 mm and P6 to about 7.5 mm, or use the whole page height. Also align the "in" and "out" labels in P6: at 150 dpi, "in" sits lower than "out".

### 8. could: K–1 p. 4. Spelling

> "colour each pair you find", "and colour them"

**Why:** The other K–1 packets use "color" (about 47 uses) against "colour" in Week 7 and here. The circle is in Bellingham. The guide also uses "colour".

**Fix:** Use "color" and "colors" on the student page, and in the guide for consistency.

### 9. could: guide p. 3, P5 extension. The answer depends on an unprinted convention

> "Extension: if extras up to 5 were allowed, which new pairs would appear? None, since extra 4 would leave P with no cubes."

**Why:** A child who says "extra 4: P had no cubes and Q had 2" has reasoned correctly. Whether an empty tower can "go in" is a convention, stated only on guide p. 1 ("towers of at least one cube"), not on the student page. AGENTS.md notes that zero-valued inputs can count as participants. As written, the extension rewards guessing the convention.

**Fix:** "If extras up to 5 were allowed, which new pairs would appear? Only extra 4, with P empty and Q 2 cubes, if an empty tower can go in; extra 5 is impossible." Or ask about extras up to 4 and accept either answer with a reason.

### 10. could: guide p. 3, P5 hint. Add the forward check that children can do themselves

> "Hint: choose an extra and take that many cubes off the top of each tower that came out."

**Why:** The only printed help is the backward method, which an adult has to supply. The material check works the other way: send a candidate pair through by adding the same extra to both towers, and see whether 4 and 6 come out. That lets a pair confirm or reject each answer themselves. It is the best protection against the parent running P5 for both pairs, and P5's backward reasoning over an unknown extra is the step most likely to need adult help (a hypothesis, unpiloted).

**Fix:** Add "Check a pair by putting it through: add the same number of cubes to P and to Q. Does 4 and 6 come out?" Put it before the existing hint.

### 11. could: guide p. 2, K–1 route. The route skips a printed problem

> "K–1: handle and measure, then Problems 1–2 (about 15 minutes). Before Problem 4, play one round... Problems 4–6 take about 20 minutes; Problem 3 suits a child who finishes early."

**Why:** "Finishes early" could mean finishing Problems 1–2 before the other pair, or finishing everything. The table demonstration needs both pairs ready at once, so the first reading is probably meant.

**Fix:** "A pair that finishes Problem 2 before the other can do Problem 3 while waiting for the table's machine round; otherwise come back to Problem 3 after Problem 6."

### 12. could: guide pp. 2–3, materials. Crayons and cubes are counted per pair, but each child has a page

> "about 30 interlocking cubes ... and add a crayon" (per K–1 pair)

**Why:** Each child colours their own page, so one crayon per pair makes children wait. P5's full set is 28 cubes, so the two children in a pair cannot each build their own set from 30. That works only if the pair builds one set together, and the guide does not say so.

**Fix:** "A crayon per child. The pair builds Problem 5's towers together and each child colours." Or supply about 50 cubes per pair.

## Not findings (checked and fine)

- **Is the worked example a giveaway?** No. It shows the forward machine only, and the K–1 tasks are inverse questions. Showing the extra on top is the machine's definition, not P5's list or invariant.
- **Are the problems substantial?** P5 (three pairs to build, colour and certify complete) and P6 (three machines, each needing a comparison and then two take-aways) each plausibly fill 5–7 minutes at K–1. P4 is a two-role game with four rounds. Its thinking per round is light, a comparison, but switching jobs and the held follow-up make it reasonable as the activity that brings the machine in. All timings are predictions.
- **Narration, method or encouragement on the new pages?** None. "Build" and "colour" are the requested actions and recording. The diagram labels are short and consistent across P5 and P6.
