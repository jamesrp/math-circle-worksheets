# Adversarial review: Week 76, Substitution strips

## Verdict

**No blocking mathematical or rendering defect found. Keep the present four-page investigation.** The packet meets the shared Grades 3–5 prototype scope, has a usable concrete entry, and preserves the important distinction between a whole generated row and a crop. The best revision is a small clarification of cut-edge rules, ideally accompanied by one more purposeful boundary case. A separate minor wording clarification would make the final infinite object more precise. These are bounded recommendations, not reasons to replace the sequence or add student-facing proof scaffolding.

I read PROMPT.md and the run-local addendum, inspected all four freshly rendered pages, read all four portable source files, ran the supplied checker, checked the fixed instances independently, and rebuilt the PDF. I did not edit the draft.

## Recommended revisions

### R1. Page 3, Problem 4: make the two-cut-edge case explicit

The sentence “A cut may leave one lone tile at either end” is easy to hear as allowing one lone tile in total, chosen at one end or the other. The actual convention permits one at **each** end simultaneously. That distinction matters when repeatedly decoding crops: treating an even-length crop as if its left edge had to be a generation boundary can give a false rejection.

Suggested essential-rule wording: “Use every tile, apart from at most one lone tile at each end. Decode only complete pairs.” This states the legal move without telling children how to discover the alignment.

The current task instances cover one-end losses and no loss, but none requires a lone tile at both ends. Consider replacing BBAAB with AABB. AABB is a genuine crop, and its only legal placement is A | AB | B, retaining the one complete parent A. The existing AABBA convention visual already supplies a left-only loss; ABA supplies the two possible short alignments; BAABA supplies a right-only loss; ABBAABBA supplies no loss. The replacement therefore adds a genuinely missing case without adding another problem or more transcription.

This is a clarity/coverage recommendation, not a claim that the current crops or their answers are wrong. If the case changes, update its exact expectation in check_math.py and re-render the page.

### R2. Page 4, Problem 7: identify one endless strip

“Imagine continuing the A-grown rows forever” can refer to an endless sequence of different finite rows rather than to the single limiting strip. The question then immediately asks about a tail of that strip. A small change such as “Imagine the endless strip made by growing from A” would keep the object singular and make the intended question clearer. There is no need to print the parity argument or add a chain of leading subquestions.

This is minor. The present intended interpretation is mathematically sound, and placing this difficult question last is consistent with the readiness-dependent scope. Its success with these children remains untested.

## Mathematical audit

- The substitution convention visual is correct: BA becomes BA | AB and hence BAAB. The decoding convention is also correct: BAABBA becomes BA | AB | BA and hence BAB. The latter is a non-task replacement example, not a false assertion that a six-tile row was grown from the single starting A.
- Problem 1 has the correct 16-tile target, ABBABAABBAABABBA. Its distinct three-tile crops are AAB, ABA, ABB, BAA, BAB and BBA. Eight blank three-cell strips do not force an incorrect answer count; children are asked to record each found strip once.
- Problem 2 has answer no for both AAA and BBB. Any three neighboring child tiles contain a complete replacement pair, whose two letters differ. This gives a structural reason, not an inference from a finite search.
- Problem 3’s only true whole-row claim is ABBABAAB. Its successive parents are ABBA, AB and A. ABBAABBA decodes to ABAB and then AA, which cannot be a whole substituted row. ABBABBAB fails immediately because its third aligned pair is BB. ABBABAABABBABAAB decodes to ABBAABBA and then follows the same failed ancestry. These are purposeful levels of failure.
- Two of Problem 3’s rejected whole rows, ABBAABBA and ABBABAABABBABAAB, really do occur as crops. That is a strength of the design, not an error. Preserve “whole row” and the explicit starting A. In particular, do not revise these questions into claims that every rejected row is an impossible crop.
- Every crop printed in Problem 4 is genuine. ABA has the placements AB | A and A | BA, retaining A and B respectively, and both placements arise in actual generated rows. BAABA has BA | AB | A, retaining BA. BBAAB has B | BA | AB, retaining BA. ABBAABBA has AB | BA | AB | BA, retaining ABAB. The AABBA convention visual correctly discards the incomplete left pair rather than silently treating the cut as a generation boundary.
- Problem 5’s answer is no. Both pair alignments could fit only if the five letters alternated throughout, giving ABABA or BABAB. Neither is a genuine crop: either possible alignment in an actual child row forces three equal letters in the parent once the cut-edge parent letters are accounted for. The supplied checker independently verifies the exact five-letter factor set and uniqueness for each genuine factor. The worksheet correctly asks for the explanation rather than asserting that a finite search proves the claim.
- Problem 6’s two repeating strips are correctly drawn. AB repetition supplies the forbidden crop ABABA. ABBA repetition avoids AAA, BBB, ABABA and BABAB, so it genuinely demands another scale. One convenient witness using only complete first-level pairs is ABBAABBAABBA: its forced first-level decoding is ABABAB, which contains forbidden ABABA. The checker's nine-letter witness ABBAABBAA is also valid, though explaining that shorter witness uses information from its cut edge. The task does not require the shortest witness, so this is not a student-facing defect.
- Problem 7 has answer no, including eventual periodicity after an arbitrary finite prefix. Equal adjacent letters occur arbitrarily far out, and their first indices are odd under zero-based indexing. An odd eventual period moves such a pair to an impossible even position. An even period can be halved by reading the even positions, which recover the parent word. Repeated halving produces the odd-period contradiction. The packet makes no false claim that its finite examples alone establish this conclusion.

The supplied exact-factor computation has a valid coverage argument: after choosing an expansion scale at least as long as the desired factor, any factor crosses at most two expanded letters; all four possible adjacent parent pairs occur. This is stronger than an unexplained finite sampling cutoff. My separate finite enumeration agreed with every printed fixed instance; I have not treated that second enumeration as an infinite proof.

## Student usability and organizer's standard

- Four pages, seven consecutively numbered problems, consistent required headers and footers, no name/date fields or decorative activity headings. Diagram labels identify parts of convention visuals rather than adding gratuitous section titles.
- The pages do not print the equal-neighbor alignment discovery, tell children to run a fixed rejection algorithm, or break the investigation into a succession of lettered steps. The three worked visuals teach conventions on non-task examples, as explicitly required.
- The early work is genuinely concrete: separate old/new rows and partner checking constrain simultaneous substitution; the printed 16-cell row provides recoverable state. Later tasks supply exact strips and sufficient space to retain decoding records. They do not require copying a long chain of increasingly large generations.
- The case progression is coherent: generate and classify local pieces; distinguish full ancestry; handle cut boundaries; investigate uniqueness; test deceptive repetition; then consider the infinite tail. Reusing ABBAABBA under different claims is especially valuable.
- The packet has plausible work beyond forty minutes for quick children. Problems 5–7 can also be substantial adult-supported conversations. That judgment is a design assessment, not evidence of actual timing or independent success at Grades 3–5. Do not advertise this as a classroom-tested route.
- Problem 7 is a large abstraction jump, but the brief explicitly permits a late readiness-dependent continuation. I would not remove the mathematical depth or put discretionary proof hints onto the student page merely because this final question needs adult support.

## Rendering and source checks

- Inspected every page at a rendered 1600-pixel long edge. No clipped text, collisions, broken letters, page overflow, crowding at the footer, or missing diagram elements found. The cells are legible and there is substantial working space.
- US Letter, four pages, 95,387 bytes: comfortably below the requested 200 KB target.
- The portable source folder contains students.tex, build.py, check_math.py and README.md only. It contains no borrowed pictures, downloaded resources, workflow prompts, or absolute environment-specific file dependencies.
- The builder accepts --out DIRECTORY, invokes the standard-library checker, builds in temporary storage under the output directory, and rejects overfull TeX boxes. The README states appropriate TeX/Python prerequisites and correctly distinguishes 7–10 mm pencil cells from separately handled counters of at least 15 mm.
- The initial plain rebuild failed because this execution environment lacks a configured pdfLaTeX format and tried to initialize it in a read-only home directory. Using the already supplied run-local format and standard installed TeX trees resolved this: TEXMF='{/usr/share/texmf,/usr/share/texlive/texmf-dist}' and TEXFORMATS=<run>/tex-runtime:. This is an environment configuration limitation, not a demonstrated portable-source defect. No runtime format files belong in the portable source folder.
- The successful independent rebuild is also four pages and 95,387 bytes. Its extracted text and all four rendered PNGs match the inspected draft exactly.
- README limitations are appropriately candid: physical handling, timing, adult support and classroom use are untested. No guide is required or requested in this stage.

## Revision priority

1. Clarify the permitted cut-edge leftovers in Problem 4; the AABB substitution is a useful accompanying improvement.
2. Optionally tighten the singular endless-strip wording in Problem 7.
3. Preserve the rest of the packet's mathematical structure, roomy layout and restricted student-page register. Re-run checks and inspect all four pages after any change.
