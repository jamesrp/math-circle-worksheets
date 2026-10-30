# Revise the {KIND} for Week {WEEK}, "{TOPIC}"

Work only inside `{RUN}`. The draft is `{RUN}/draft/{OUT}` with sources in `{RUN}/draft/src/`. An independent reviewer wrote `{RUN}/review-guide.md`. Copy `draft/src/` to `final/src/`, revise there, and compile the result to `{RUN}/final/{OUT}`. Do not change the student pages; if a finding is really about the pages, say so in your report instead.

Read `{REPO}/AGENTS.md` (the facilitator overview and launch rules), the review, the draft, the week's existing guide `{BASEGUIDE}`{BASEMAT}, and the final student pages it serves, {PAGES} (render and read them). The outline is `{OUTLINE}`.

Fix every must-fix and should-fix finding, and the minor ones where they help. Where you disagree with a finding, check it against the pages and your own computation, and keep your version only with a reason you can state. Recompute every answer you change with a script in `final/src/`. Compile with no errors or overfull boxes, render every page and look at it. Make sure `final/src/build.sh` still compiles to `../{OUT}` from `final/src/` and runs the checker with paths relative to the script, and run it once.

Report back in a few sentences: the final page count, what you changed, any finding you declined and why, and anything about the student pages the guide had to work around.
