# Week 17 return-visit packet: fresh adversarial review

Reviewed October 4, 2026. Scope: **critic stage only**. The current AGENTS.md, README.md, PROMPT.md and CRITIC.md were read. The outline's explicit shared-collection instruction controls over the harness's older three-band output defaults. Reviewed the actual `draft/return-visit.pdf`, all three pages, rendered independently at 1.6x in `critic-render/`; checked the editable TeX for exact wording and conventions. No student, guide, base, global, or other-stage files were edited.

## Verdict

**No mandatory student-page changes.** This is a coherent three-investigation companion, not a collection of three trivial variants. Its concrete actions are choosing state meanings, drawing transitions, moving a marker through a partner's card row, and finding a row that exposes an incorrect machine. The first task is a persistent occurrence detector, the second combines two parity memories, and the third investigates a limit of fixed memory. Do not add answer diagrams or a step-by-step pigeonhole procedure to the student pages.

The pages support return visits and readiness-dependent choices. They should not be treated as three pages every child must complete in one hour. The operational concerns below are unpiloted hypotheses and guide/launch requirements, not a reason to remove the deeper mathematics or demand formal automata prerequisites.

## Rules, representation and independence

The shared rules on page 1 identify a fixed START, a fixed YES/NO output at every state, and exactly one fixed R and B outgoing arrow. They explicitly cover self-loops, fresh starts for new rows, hiding used cards, and stopping at any point. These prevent the operator from supplying an extra counter, an output that changes with the history, or a special stopping action. The marker's current state is expressly the whole memory. An observer may know the input in order to check the answer; the machine operator must follow the fixed arrows rather than use that knowledge to alter the machine's response.

The non-task last-blue example is a useful worked convention. Input RBB leads X -> X -> Y -> Y, with the arrows labeled R, B and B and final output YES. The full diagram's R/B transitions agree with that trace: either state's R goes to X, either state's B goes to Y. X starts at NO, so the empty row is handled consistently. Both self-loops and transitions between distinct states are shown without revealing the RR solution, parity board, or equal-count obstruction.

The example is compact and readable, and its role is procedural rather than a disguised solution. The input cards carry letters as well as color. Children can test any additional rows; the printed rows do not require a particular method or a complete enumeration. The record tables require only a row and final machine response rather than simultaneous counts and intermediate-state tallies. Problem numbering, headers, footers and page numbers are consistent. There are no Name/Date fields, extra section headings, hints, or unsolicited encouragement.

## Page 1 / Problem 1 / Grades K-1 and up

The task correctly asks for RR **anywhere**, and explicitly requires YES to persist after later cards. The printed RRBB and BRRB contrast with RBR. Thus a suffix-only machine or a machine that resets YES on B can be challenged directly. Asking for the fewest states gives an investigation beyond operating the example. The mathematical target has three states; the page does not hand over those states or their meanings.

The blank 6.9-inch by 2.5-inch construction area can accommodate three approximately 4-cm discs in a row with arrows, as well as smaller drawn circles. Printed example circles are demonstration-sized, not intended to hold the supplied state discs. Nothing clips or overlaps in the rendered page.

**Readiness concern:** the page has seven short shared-rule sentences before the example and a three-sentence task. This is more to retain than a young nonreader should be expected to absorb in one uninterrupted reading. The return-visit setting and the visual procedure make the task viable, provided the ordinary launch has children actually move the marker and check a row before designing. Adult reading and drawing arrows at a child's direction are routine support; supplying the meanings of all three states or deciding every transition would take away the investigation. State minimization can be concrete experimentation for K-1, while an all-rows explanation remains a later readiness-dependent conversation. Keep these distinctions explicit in the separate adult guide. No separate forced younger version is needed.

## Page 2 / Problem 2 / Grades 2-3 and up

The target requires each color count to be even, and zero is explicitly even. This distinguishes the task from having an even total number of cards. The supplied rows give purposeful contrasts: empty -> YES, R -> NO, RB -> NO, RRBB -> YES, BBR -> NO, BRBR -> YES. The two balanced four-card orders help children check that order should not change the final required answer, even though order does change the marker's route.

There is adequate room for four state discs or a four-state drawing and clearly separated labeled transitions. The lower six-row table is legible and has room for YES/NO responses. It does not print the four parity labels or direct children to arrange states as a square, preserving their design choices.

**Readiness concern:** a child who has not yet connected evenness to pairing will need a concrete pairing check before they can judge a proposed machine. The adult may help pair the test cards outside the machine run, then hide used cards during the run. The child should retain the choice of how to represent the two memories. The shared rules are located only on page 1; if an adult hands out page 2 alone, provide the already-launched page 1 conventions or its rules/example alongside it. Do not duplicate the rules on every student page merely to make them standalone.

## Page 3 / Problem 3 / Grades 4-5

The construction-and-attack game gives an elementary action before the all-length question. RRBB and RBRB show that equality need not mean alternation; BRR supplies an unequal row. The page asks whether **any fixed number of states** can work for **every length**, so it does not mistake failure of one small proposal for a proof that all finite machines fail. The large construction area and three-row record support a partner's proposed machine and a few counterexamples. The explanation lines are spacious.

The deeper claim needs no formal automata course: following sufficiently many all-red histories forces a repeated state; continuing both histories with the same number of blue cards produces the same final state but different required answers. That proof idea belongs with the adult until children need it. A child can own the proposed machine, the attacks, the repeated-state observation, and a checked pair of histories. Avoid requiring vocabulary such as deterministic finite automaton, pumping lemma, equivalence classes, or formal quantifier notation.

**Readiness and materials concerns:** moving from many failed proposals to an explanation about every finite machine is a substantial step. Preserve it as a return-visit continuation for children comfortable with fixed-rule machines and comparing histories. The proposed finite card stock supports experiments; it must not be described as establishing the unlimited-length assertion. For larger hypothetical machines the adult can reuse concealed cards or draw the proposed histories without letting the operator acquire extra memory. An adult acting as referee may check the target's counts; that checking knowledge must not affect the machine's transitions or YES/NO output.

## Revision and guide handoff

The reviser should preserve the three investigations, the correct last-blue example, the persistent RR wording, the zero-even convention, the current-state-only memory rule, and the explicit all-length question. Recheck the actual final pages if source or layout changes; no visual change is requested by this review.

The separate guide should state exact targets and assumptions before solutions, supply a concrete launch and prerequisite gates, distinguish child-owned design from adult reading/drawing, keep minimization proofs and the all-length argument discretionary, and acknowledge that materials, physical procedures, and classroom use are untested. This critic review does not certify a facilitator guide, a source ZIP rebuild, the final release, or physical readiness. A separate mathematical review is still appropriate for the minimum-state and unbounded-memory claims.
