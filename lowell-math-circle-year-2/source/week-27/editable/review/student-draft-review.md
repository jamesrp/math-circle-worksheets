# Independent adversarial review

## Verdict

The packet is mathematically sound and substantially follows the organizer's unusually strict student-page style. I found no incorrect printed preference list, false mathematical task, missing solution, clipped content, or actual overlap. The two-sided condition is preserved throughout; neither first-choice matching nor unilateral switching has replaced stability. The main revisions are narrow: make the K–1 single-strip experiment unambiguous, resolve the older packets' departure from the stated 20 mm icon size, and make the proposing-side comparison an explicit mathematical question rather than just a second run.

I would request these targeted changes rather than a rewrite. The K–1 packet is a genuine optional two-pair entry, with substantial inverse problems later; it should not be padded with unrelated work or expanded to three pairs.

## Review performed

- Read `PROMPT.md` before inspecting the draft.
- Independently rendered all three delivered PDFs at 100 dpi into `review-render/` and visually inspected every page: K–1, 6 pages; grades 2–3, 5 pages; grades 4–5, 6 pages. All are US Letter.
- Read the extracted text and the generating sources to check exact wording, positions, dimensions, and preference data.
- Independently enumerated perfect matchings for every supplied profile, all 16 two-pair preference profiles, and all 46,656 three-pair profiles with a fixed final matching. The fixed-matching reduction is legitimate by relabeling the receivers and independently verifies the last-choice extremum.
- Independently explored every possible order of free askers for the four-pair instance in grades 4–5 Problem 2. Both runs terminate with the intended distinct outcomes; every left-side schedule uses 8 requests and every right-side schedule uses 7.
- Checked compilation logs for warnings/overfull boxes and inspected font embedding. No relevant warnings; all fonts are embedded.

The draft and its sources have not been edited.

## Findings requiring attention

### 1. K–1, page 3, Problem 3: say explicitly that each candidate change is made on its own

**Priority: medium; clarity of the mathematical experiment.**

“Circle every strip whose two choices you could swap to make the drawn pairing stay” intends four separate tests, each starting from the printed lists. It does not explicitly prohibit keeping an earlier successful swap while trying the next strip. That is a consequential ambiguity for young children physically manipulating strips.

For the top case, swapping A alone works and swapping Y alone works. Swapping B alone does not. But after a child has already changed A, changing B also leaves the drawn pairing stable. A cumulative interpretation can therefore produce a mathematically different answer while the child believes they followed the instruction.

Add a few words such as “on its own” or “change only that strip.” Preserve the intended two contrasting cases and the impossible second case. This is an essential rule, not a hint. The first sentence is also the most syntactically demanding K–1 prompt: a relative clause, a hypothetical change, and a condition on the resulting pairing. Simplify that structure if possible rather than adding a third sentence.

### 2. Grades 2–3 and 4–5: printed icons are substantially smaller than the brief's material specification

**Priority: medium if these pages are the provided manipulatives; otherwise a specification question to resolve.**

The outline explicitly asks for icons “at least 20 mm across” and removable materials large enough to read aloud. K–1 meets that: the source uses 0.79-inch icons, approximately 20.1 mm. In the older packets, preference icons are approximately 10.4–13.0 mm, and matching-diagram icons approximately 9.7–13.0 mm. These dimensions are visible in the rendered PDFs and confirmed by `strips()` and `board()` in `build_packets.py`.

The older pages are perfectly legible as pencil worksheets, so this is not a claim that the text is unreadable. It matters if the printed preference strips or diagram positions are expected to carry the hands-on work at the specified scale. Simply printing these PDFs at 100% does not provide the outlined full-size materials.

Resolve whether separately supplied, full-size table materials are assumed. If not, enlarge the relevant icons/strips and reflow onto additional pages. Do not shrink K–1 to match the older layout. Do not silently treat the stipulated 20 mm size as satisfied by readable 10–13 mm symbols.

### 3. Grades 4–5, page 2, Problem 2: the comparison is implicit rather than asked

**Priority: low; strengthen the intended mathematical development.**

The problem asks for the procedure twice and records the two answers, but ends without a question about what choosing the proposing side changes. The chosen example is good: A and C change partners, B and D do not, and both resulting matchings are stable. The page can therefore make the outline's side-dependence point directly without adding another example or giving away the conclusion.

A short, substantive question about whether choosing who asks can change the final pairing would complete the goal. This would not be one of the organizer's prohibited automatic “compare with a partner” follow-ups: comparison of the proposing sides is specifically a core mathematical objective here. It is a refinement, not a correctness blocker; a child who notices the two different outcomes already has the relevant evidence.

## Smaller layout and pacing observations

- **Grades 4–5, page 1, upper case:** the top of the first matching diagram sits only about 0.03 inch below the bottom of the preference-strip block. It does not overlap, but the circular A is nearly tangent to the strip above it, making the boundary between the supplied data and the work diagram less clear than elsewhere. Add a small vertical gap if reflowing the page.
- **K–1, Problems 1 and 2:** each has only two tiny markets. A child who has already passed the “both prefer” prerequisite can plausibly finish either in less than the requested five minutes. This is a mild mismatch with the per-problem duration standard, not evidence that the whole packet is too short. Problems 3–6 add genuine search, impossibility, and inverse design; page count is ample. Do not repair this by adding repetitive filler. Combining or strengthening an opening problem is preferable if a change is needed.
- **K–1 readiness remains a real gate:** the first page's general rule is accurate but is three sentences and a nested two-sided condition. It is suitable as a rule the adult demonstrates, not a substitute for the prerequisite demonstration. The later pages appropriately stay within two pairs, yet constructing preferences is substantially harder than recognizing a blocking pair. This is acceptable for the optional participating group in the outline; it should not be interpreted as an independent packet for every kindergartner.
- **Request logs, grades 4–5 page 2:** each box is approximately 3.35 by 1.96 inches for 8 or 7 requests. This is workable for compact letter-pair notation and the physical proposal markers in the outline, but not roomy for a child writing full sentences. It is acceptable as drawn and does not require an imposed logging method. Preserve or enlarge this space if the diagrams are enlarged.

## Mathematical audit by problem

These are review checks, not proposed additions to the student PDFs.

### K–1

1. **Top:** only AX/BY can stay. **Bottom:** only AX/BY can stay. The top crossed pairing has two blocking pairs; the bottom crossed pairing has the blocking pair AX. The examples genuinely distinguish the two-sided condition from a single piece's dissatisfaction.
2. **Top:** both AX/BY and AY/BX can stay. **Bottom:** only AY/BX can stay. The four blank recording diagrams are sufficient.
3. **Top:** the individual reversible strips are A and Y. **Bottom:** no individual strip reversal works. In the bottom case AX/BY has both AY and BX blocking, so changing one of the four strips cannot remove both blockers.
4. **Top blank Y strip:** A before B. **Bottom:** impossible. Because A and B both put X first in the bottom case, whichever is not paired with X needs X to prefer its current partner; the two candidate matchings impose contradictory requirements on X.
5. Exactly seven of the sixteen possible complete strict two-pair profiles make only AX/BY stable. Asking for two different profiles is feasible and provides real choice.
6. Exactly two profiles make both matchings stable: A: XY, B: YX, X: BA, Y: AB; and A: YX, B: XY, X: AB, Y: BA. Two complete blank sets provide exactly enough recording space.

### Grades 2–3

1. **Top:** AX/BY alone is stable; AX blocks the crossed alternative. **Bottom:** both pairings are stable. The request to connect a blocking pair on each rejected diagram is meaningful rather than an automatic explanation demand.
2. Exactly one stable matching: AY/BZ/CX. No false invitation to find several answers is made by the six blank trial diagrams.
3. Exactly three stable matchings: AY/BX/CZ; AZ/BX/CY; AZ/BY/CX. The completeness question is appropriate and nontrivial.
4. Exactly four stable matchings: AW/BX/CY/DZ; AW/BX/CZ/DY; AX/BW/CY/DZ; AX/BW/CZ/DY. Four recording diagrams suffice. No pairing can give all eight letters their first choice; already A wants W while W wants B. This example correctly prevents “stable” from becoming synonymous with everyone getting a first choice.
5. A complete three-pair profile with exactly two stable matchings exists. For example, extend the two-pair two-stable case with C and Z ranking each other first and put C or Z last in the other lists. C/Z is then forced in every stable matching and the two-pair core supplies exactly two choices. The task does not accidentally demand the impossible.

### Grades 4–5

1. **Two-pair case:** two stable matchings. **Three-pair case:** uniquely AY/BZ/CX. The contrast is correct.
2. **A–D ask:** AW/BY/CZ/DX, 8 requests. **W–Z ask:** AZ/BY/CW/DX, 7 requests. Both are stable, and these are the only two stable matchings for this profile. Exhaustive branching over the free-asker choice confirmed that the omission of a fixed asking order does not make the result ambiguous. The rule that only free askers act, the no-repeat rule, tentative holds, and choosing the receiver's preferred asker are all present.
3. The changed rule can produce an unstable pairing. For example, let A and B prefer X to Y, let X prefer B to A, let A ask X first, and let B subsequently be rejected by X and go to Y; use C/Z as a mutually first-choice isolated third pair. BX then blocks AX/BY/CZ. Recording a chosen request sequence is enough to make the counterexample precise; the task need not prescribe an asking order.
4. Sixteen requests is a valid bound for four per side, and one hundred for ten. A stronger sharp bound is not requested. A complete explanation must also rule out a free asker exhausting its list: if it had asked all receivers, every receiver would be holding someone, leaving no asker free. Thus a finite no-repeat argument alone is insufficient, but the task correctly asks for both boundedness and complete pairing and does not give the proof away.
5. The universal stability statement is true. An asker who prefers another receiver must already have asked and been rejected by it; that receiver's held partner can only improve. The problem asks for the genuine correctness explanation, not merely a conclusion from a sample run.
6. The maximum number receiving a last choice is three. A stable construction gives every member of one side its first choice and every member of the other side its last. Four last-choice recipients among six would include last-choice recipients on opposite sides who are not paired to each other; they would block. Independent exhaustive verification agrees. This is a worthwhile final extension and does not silently require the optional proposer-optimality theorem.

## Standard and production checks that passed

- Correct one-line week/topic/level headers, numbered “Problem N:” labels, and consistent one-line footers with packet IDs and page numbers.
- No extra activity titles, cute narrative, praise, exclamation marks, rhythmic asides, or small lettered sub-steps.
- The concrete labels and shape convention are consistent. Every printed supplied preference list is strict and complete for the exact objects used.
- No real children's friendships or personal preferences are solicited.
- Problems are goals rather than worked solutions. The deferred-acceptance rules on the older page are the procedure being investigated, not an illicit suggested solution to the earlier search problems.
- The young packet is all two-sided stability mathematics; its length has not been achieved by unrelated sorting.
- Sufficient work exists for a strong older or middle-band child, with sensible places to stop. The explanation pages have generous room; the blank construction pages have the objects needed to start.
- All 17 rendered pages have clear type, intact symbols, uncut diagrams, visible margins, and unobstructed headers and footers. No rendered answer marks or accidental pre-completed answers appear.

## Recommended disposition

Keep the mathematical examples and overall progression. Clarify K–1 Problem 3, resolve the full-size-material issue, and consider the small explicit comparison question in grades 4–5 Problem 2. Re-render any changed pages and inspect them at 100% scale. No mathematical reauthoring is necessary.
