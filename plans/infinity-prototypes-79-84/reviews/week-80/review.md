# Week 80 adversarial review

Reviewed 9 October 2026. Fresh critic stage only; no student or guide edits made.

## Scope and evidence

Read PROMPT.md, CRITIC.md and the selected-band override, current AGENTS.md, student LaTeX and portable builder, and the separate facilitator LaTeX. Rendered the actual draft PDFs with PyMuPDF at 1.6 scale and visually inspected every page: students/materials 1–5; facilitator 1–4. Images are in critic-render/. This is a digital/mathematical review, not a physical rehearsal or classroom test.

Reviewed student PDF SHA-256: `66c4b79d7ccee260040991860ef7a975d424a3b3e42fb881a75498d8629fa6e1`.

Reviewed facilitator PDF SHA-256: `94357ae2c541a9fed574145d143e634dc14b563ae069814de064022f04fc416a`.

## Verdict

Revise the physical stopping rule and adult material preparation before delivery. The mathematical kernel is sound, the endpoint question is kept open, and the packet is visually clean. No redesign of the accepted infinity theme is needed. The principal risk is children encountering paper-folding/counter-size failure before reaching the mathematical comparison.

## Required changes

### 1. Student Problem 1 demands a materially smaller fold than the guide admits

Student page 1 says “Make the first six switching marks.” The supplied working/cutout line has exactly 180 mm between START and MIDNIGHT. Its remaining gap after marks 4, 5, and 6 is 11.25, 5.625, and 2.8125 mm respectively. A sixth repeated end-to-mark fold is therefore a fine-motor/measurement task at a few millimetres, and a normal small counter cannot accurately show these late positions without covering the endpoint. This is not merely a distant infinite-stage concern.

Facilitator page 2 instead says to work on “the first four to six halves only,” and that late marks are not microscopic folding demands. Those instructions conflict with the child-facing mandatory six. An adult obeying the practical advice must override the printed task. Revise the student task to a manageable fixed prefix (four marks on the supplied strip is defensible) and let later marks be described from the rule. Alternatively specify and actually supply a longer usable strip for six folds, with exact preparation; the 180 mm cutouts alone do not provide that. Retain the open last-switch question. This concern is an unpiloted physical hypothesis supported by exact printed dimensions, not a claim that children can never fold at this scale.

For Problem 2 likewise state in adult notes that a counter centre is the position, and stop physical placement when the size of the counter makes the remaining gap hard to display. Use the same manageable prefix for both experiments so late motion does not falsely look like a finite arrival at END.

### 2. The printed ON/OFF pieces do not yet make a reversible card without an unstated preparation step

Student/material page 5 has two separate one-sided rectangular cutouts labelled ON and OFF. The guide calls for a “reversible ON/OFF card” but never explains making it from those cutouts. Simply cutting them produces two cards whose backs are blank; flipping one will not toggle between the required two states. This would undermine the intended move visibility, particularly after the organizer’s earlier paper-rule experience.

Add explicit adult preparation: cut the two equal panels and attach them back-to-back, or use a single existing card with ON on one face and OFF on the other. Say that a legal flip reverses this one object. This belongs in preparation, not as extra task prose on child pages. Two loose face-up cards are a different manipulation and should not be silently substituted.

## Recommended clarifications

### 3. Keep the timing line distinct from the counter-position line during Problem 2

Page 2’s only board is the position line START–END. “Use the same switching marks” means the clock/time strip from Problem 1 must stay on the table at the same time. The material page does provide both, which is good. Specify in the adult setup that the two strips are placed side by side and given different roles: an event on START–MIDNIGHT triggers the flip and one halfway motion on START–END. A partner can point to the current event while the other changes the objects; adult-scribed observations can replace repeated transcription. This makes the comparison about time versus state visible rather than relying on remembering the previous page.

An ordinary whole-group demonstration of one combined event is sufficient for this new simultaneous action; no additional worked-answer student panel is needed. The existing fold visual already gives an appropriate input/action/output example without answering the infinity question.

### 4. Problem 2’s comparison language could be more operational

“What, if anything, does each get closer to” is natural for the counter but metaphorical for the two-state card. A child might interpret the physical card as getting closer to MIDNIGHT because it is being moved along the timeline. Keeping the card in a fixed place and asking whether its displayed side settles, alongside where the counter approaches, would remove that ambiguity. The desired discovery should remain open. This is a wording/handling improvement, not a mathematical error in the current task.

### 5. Make the source pointer usable in the delivered guide

Facilitator page 4 points to `SOURCES.md`, but that file is absent from the reviewed Week 80 source directory. The bibliographic names and page locators are present, so attribution is not missing; the claimed pointer needs to match the final portable source package or be replaced by direct primary-source links. In a phone-readable PDF, clickable source links would be more useful than a bare filename. Coordinate this with the root’s batch SOURCES/index arrangement rather than copying external papers.

## Mathematical checks

The switch times satisfy `t_(n+1) > t_n`, remain strictly before 1 and tend to 1. Given any displayed switching mark, the next halfway mark is later and still before MIDNIGHT, so there is no last switch. The printed shared rule limits its prescription to before midnight and does not covertly assign an endpoint.

The OFF-start post-switch sequence is ON, OFF, ON, OFF, … . Odd/even post-switch subsequences have different constant values, so no ordinary left limit exists. Because the two possible lamp states are distinct, averaging does not produce a third allowable binary state. Assigning either ON or OFF at midnight as an additional isolated endpoint rule is consistent with all the earlier switches; demanding agreement with a left limit is impossible. The guide distinguishes those two failures correctly.

The halfway-motion recurrence has position `x_n = 1 - 2^(-n)` after n actions from START=0 toward END=1. It stays short of END at each finite stage and has limit END. Its spatial state and the event-time index must remain different roles even though their normalized formulas happen to be equal.

Student Problem 3 asks what the switching rule alone determines and does not print the adult conclusion. Problem 4 comes after that open investigation and invites added conventions; it does not imply an endpoint convention is a deduction. Problem 5 explicitly calls its approach-to-endpoint instruction an added rule, so it preserves the difference between that convention and the initial prescription. There are no prewritten endpoint envelopes in this packet; the two blank panels are student-created rule spaces. Their absence is acceptable and avoids prematurely supplying ON/OFF answers.

The theorem-first overview is appropriately before solutions, includes assumptions and limits, maps manipulation to Grades 2–3 and the convention discussion to Grades 4–5, and does not promote six trials to proof. The real-ordered-field meaning of the counter’s convergence is adequately specified by its “positive real tolerance” sentence. There is no claim of physically performing infinitely many actions, nor an unsupported ordinal/surreal arithmetic identification.

## Every-page visual audit

- **Student p.1:** consistent header/footer; brief shared rules; legible three-panel fold visual; ordinary numbered task and a large 180 mm line. No overlap or clipping. Required change is the six-fold demand, not diagram quality.
- **Student p.2:** clear START/END position line and large split Card/Counter response space; header/footer are present in the actual PDF. No clipping. Keep the separate time strip beside it and centre the physical counter deliberately.
- **Student p.3:** Grades 4–5 header correctly gates the endpoint question; large blank MIDNIGHT display space; no printed answer. Clean layout.
- **Student p.4:** two generous blank extra-rule panels followed by the added-limit-rule comparison; numbering 4 and 5 continues correctly. Neither ON nor OFF is supplied as an answer. Clean layout.
- **Material p.5:** two distinct 180 mm cutout lines and large ON/OFF panels; labels are legible and cut boundaries clear. Adult preparation must assemble the panels back-to-back. No unwanted numbered busywork.
- **Guide p.1:** theorem-first opening and assumptions clear; accurate mathematical contrast; comfortable typography and margins.
- **Guide p.2:** prerequisites, adult staffing, whole-group launch and route given. Physical prefix and card fabrication need correction as above; otherwise no layout issue.
- **Guide p.3:** correct explanations/hints kept with adults. An “undefined” response is examined rather than imposed. No layout issue.
- **Guide p.4:** encore and sources clear; unpiloted and physical-fit/timing/rehearsal limitations explicit. Repair the source-file pointer. No clipping.

## Age/readiness and task independence

Grades 2–3 have an actionable fold-and-flip core, followed by a tangible second process. Upper pages involve enough abstract language to justify the selected Grades 4–5 label and nearby adult discussion. No forced K–1 variant is present. After the physical fixes, the printed comparisons can retain children’s mathematical choices: they can predict, challenge and design endpoint rules. The adult should read and record, and physically witness actions, rather than perform all the reasoning. Whether the two core pages occupy the proposed 35–40 minutes remains a pacing hypothesis; the guide’s concrete encore designs can extend a group that finishes quickly. Do not add bookkeeping or extra tiny fold tasks simply to fill time.

## Revision acceptance checks

Rebuild the revised selected-band PDF and guide; inspect all 5 student/material pages and all guide pages again. Verify the child/adult physical-prefix instructions agree, the reversible-card fabrication is stated, and the last-switch/endpoint questions retain their open form. Check that the final source package includes or correctly links any referenced source index. Keep the stated unpiloted and untested-physical-rehearsal status even after digital checks pass.
