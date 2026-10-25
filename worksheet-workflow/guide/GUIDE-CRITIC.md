# Review the facilitator guide for "{TOPIC}"

You are an adversarial reviewer. You did not write this guide. Work only inside `{RUN}`; write your review to `{RUN}/review-guide.md` and any scripts to `{RUN}/review-guide-check/`. Do not edit the guide or the student pages.

Read `/home/claude/math-circle-worksheets/AGENTS.md` (especially "Facilitator mathematical overview", "Launch together", "Make activities usable" and "Review age fit operationally"), then:

- the guide, `{RUN}/draft/facilitator.pdf` (source in `{RUN}/draft/src/`);
- the final student pages it serves, `{DRAFT}/k-1.pdf`, `{DRAFT}/grades-2-3.pdf`, `{DRAFT}/grades-4-5.pdf`{EXTRA}; render every page and read it;
- the outline `{OUTLINE}` and the page reviews `{DRAFT}/review.md` and `{DRAFT}/review-math.md`;
- a model guide for comparison: `/home/claude/math-circle-worksheets/lowell-math-circle-year-2/week-98/week-98-facilitator.pdf`.

Check, and report each finding with its page and a concrete fix:

1. **Correctness.** Re-derive every answer the guide prints, by your own code where answers come from enumeration or simulation, against the final pages. Wrong answers, incomplete "find all" lists and false general claims are must-fix.
2. **Agreement with the pages.** Every problem number, page number, picture description, board size and material count matches the final PDFs. A guide keyed to an earlier draft is must-fix.
3. **The overview.** Does it state the actual theorems with assumptions, limits and a followable proof idea, distinguish experiment, conjecture and explanation, and map the bands, before any solution? A vague purpose sentence is must-fix.
4. **The launch.** Is it brief, concrete, on a non-task instance, and free of the main theorem and every answer?
5. **Usability.** Realistic preparation and staffing, a one-hour first route per band, hints that are questions rather than procedures, materials that match what the pages need.
6. **Brevity.** Repetition, narration of the pages, generic encouragement, padding.

Sort findings into must-fix, should-fix and minor. End with what works and should be kept. Report back in a few sentences.
