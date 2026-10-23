# Independent mathematical review: Week 92

Reviewed the consolidated `draft/students.pdf`, all six rendered pages, and diagram coordinates in `draft/src/students.tex`. Independent checks, intended outcomes for every problem, proofs, and exact arithmetic are preserved in `math-check/independent_check.py` and `math-check/independent_check.txt`; the script passes. Independently rendered pages and extracted PDF text are in `math-check/`. The writer's verification code was not used.

## Located issue

**Grades 4–5, page 4, Problem 4 — endpoint-only wording admits an unintended trivial answer.**

Exact text: “Find two more starting bands for which moving just the ends misses possible places.”

The intended outcome is a band crossing 8 whose full image extends beyond the interval between its endpoint outputs. The given diagram is correct: `[6,10]` maps to `[12,16]`, although both endpoints map to 12. Further examples include `[5,11] → [10,16]` and `[7,9] → [14,16]`.

However, “moving just the ends” can literally mean retaining only two output points. Under that reading every positive-width band qualifies, including bands wholly on one side of 8. For example, `[1,2]` has endpoint outputs 2 and 4, which miss the valid output 3 from the start 1½. Yet the interval **between** those endpoint outputs is exactly the full correct image `[2,4]`; no fold-related endpoint failure occurs. Thus an ordinary same-side band satisfies the printed request while avoiding its intended distinction.

**Smallest fix:** Replace the final sentence with: “Find two more starting bands for which shading only between the two endpoint outputs misses possible places.” This preserves the intended investigation without prescribing which bands to choose.

## Band status

- **Grades 2–3, pages 1–3, Problems 1–3:** check out completely mathematically, including the point/range worked visuals and all drawn starting bands.
- **Grades 4–5, pages 4–6, Problems 4–9:** the ambiguity above is the only located issue. Numerical answers, interval-width claims, arbitrary finite precision construction, dyadic subdivision pattern, and eventual full-track coverage all check out; diagrams match the intended intervals.
- **K–1:** no packet required or present, as authorized by the run-specific override.

This is a mathematical and rendered-PDF review; physical apparatus rehearsal and classroom piloting were not performed.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.
