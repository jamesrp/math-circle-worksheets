# Week 95 revision response

The authorized deliverable is two revised student packets: `grades-2-3.pdf` and `grades-4-5.pdf`, four pages each. No K–1 packet or facilitator guide was authored. Sources are self-contained in `src/`, with `build.py --output-dir` preserved. `final-source.zip` contains exactly `src/build.py`, `src/verify.py`, and `src/README.md`.

## Focused review responses

| Review requirement | Delivered change and exact location |
|---|---|
| Complete non-task fraction-matching convention before first use | `grades-4-5.pdf`, p.2, Problem 3: input says two marked objects in the bag and shows second catch A*,B,C; intermediate matching model retains that SAME A*,B,C sample as one group and adds D*,E,F as a second equal group; output labels **Rule’s guess: 6 total**, with 2/6 = 1/3. The example precedes the instruction to estimate record A. The original task illustration and different-population counterexample remain. `src/build.py`, `UPPER`; example checked in `src/verify.py`. |
| Closed unchanged population, not merely unchanged count | Both PDFs p.1 shared rules now require the same objects throughout a series, with nothing added, removed or exchanged except temporary catches. Both Problem 1 prompts say “same objects.” `src/build.py`, `RULES`, `LOWER`, `UPPER`. |
| Separate blind trials from constructive possibility | Both PDFs p.1 apply blind draws to sampling trials and explicitly allow arranged catches to show a record is possible, using distinct objects per catch from the same bag. `grades-2-3.pdf`, p.3, Problem 5 now explicitly asks for arranged legal catches, so no rare random event must be awaited. The shared construction rule also covers the other build/possible-record tasks. `src/build.py`, `RULES`, `LOWER`. |

The uniform-subset model, mark-independent sampling, catch held out until counted, full first-catch return/mixing, retained marks through both catches, and clearing marks only before a new round are retained. The same-population capture/mark/return/mix/recapture/overlap visual is unchanged. Both printed variability collections remain unchanged on p.3. `src/README.md` still identifies them as invented illustrative records, not collected data, and records physical limitations. All substantial bounds, counterexamples, zero-overlap questions, budget optimization and lost-mark investigation remain.

## Verification and page coverage

- Built both PDFs with Python 3 and `/Library/TeX/texbin/pdflatex`; no overfull-box warnings.
- Ran `src/verify.py`: PASS, including the new matching-example identities and fractions, sharp overlap support, record feasibility, exact expectations through N=24, and budget optima 2–24. Evidence: `checks/source-verify.txt`.
- Ran the critic’s unmodified `../independent_check.py`: PASS for 818 finite models and every original task. Evidence: `checks/independent-check-results.json`. Its prior independent review remains separate from this reviser’s check of the added non-task example.
- Rendered and actually inspected **every final page**, both bands p.1–4, at 90 dpi. Images: `render/grades-2-3-1.png` through `render/grades-2-3-4.png`; `render/grades-4-5-1.png` through `render/grades-4-5-4.png`. Checked legibility, layout, consecutive numbering, header/footer consistency, same-object diagram identities and marks, new sample-to-model bridge, data tables and retained answer space. No clipping, collision or overflow observed.
- Extracted `final-source.zip` into the fresh run-local `../clean-rebuild/`, built with its extracted `src/build.py --output-dir`, and ran its extracted `src/verify.py`. Both rebuilt PDFs are **byte-for-byte identical** to these delivered PDFs. Evidence and SHA-256 values: `checks/clean-rebuild.json`, `checks/clean-build.txt`, `checks/clean-source-verify.txt`.

No digital blocker remains. Physical uniformity, tactile equivalence, retention/reset, and classroom use remain untested. These revised drafts have not been uploaded, published, or promoted into the library by this revision stage.
