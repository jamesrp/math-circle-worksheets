# Portable independent verification adaptation

Created `portable_check.py` and `baseline_check.py` in this math run. The latter is a byte-identical copy of the original Problems 1–5 independent checker. The original `independent_check.py` and `final-independent-check.py` remain unchanged. Production/reviser files were only read.

## Interface and dependencies

Place both scripts together, under any directory name. The entrypoint may also be renamed to `independent_check.py`; it always runs its distinct sibling `baseline_check.py` and guards against self-recursion.

Typical package command:

```sh
python3 checks/portable_check.py --source-dir student --verify-only
```

`--source-dir` must contain `students.tex` and `README.md`. Verification uses only Python's standard library. It checks all six mathematical problems, the final source's five pages, task statements, exact printed stage lists, edge paths, coordinates, launch tokens, and material conventions. There are no absolute workspace paths or mandatory PDF/TeX/Poppler dependencies. Input hashes are keyed by portable filenames rather than original locations.

Optional flags:

- `--results results.json` saves all detailed finite cases and verification results.
- `--pdf students.pdf` additionally audits PDF text with `pdftotext`. This is optional and does not replace the already documented visual inspection.

## Isolated tests

Working directory:

`portable-isolated-DIAZpu/`

The isolated student directory contains only copied `students.tex` and `README.md`. Its checks directory contains only copied review scripts. No production checker or PDF was copied. The following exact command used a PATH with no external tools and Python isolated mode:

```sh
PATH=/nonexistent /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I checks/portable_check.py --source-dir student --verify-only --results results.json
```

Output, exit status 0:

```text
PASS: source consistency, five pages and Problems 1-6.
PASS: Problems 1-5 baseline, exact boundary witnesses and inclusion ranks.
PASS: Problem 6, 15 loops, 4 qualifying loops, 6 pairs, 24 filling orders, 1 reversible pair.
PASS: diagram coordinates, tied stages, token supplies, and no-resurrection argument.
PDF audit: not requested; no PDF or pdftotext used.
```

Standalone baseline command, exit status 0:

```sh
PATH=/nonexistent /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I checks/baseline_check.py > baseline-results.json
```

The full JSON reports `"result": "PASS"` and exactly matches `problems1to5` in the portable result. It covers the original four square schedules, four joined-triangle schedules, four proposed tied-stage changes, and 1,742 legal inclusion pairs.

Renaming regression test, exit status 0:

```sh
cp checks/portable_check.py checks/independent_check.py
PATH=/nonexistent /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I checks/independent_check.py --source-dir student --verify-only
```

Output was byte-identical to the five lines above. There was no recursion.

A negative test changed only the isolated source's `Stage 2: one of DA and AC` to stage 3. The verifier rejected it at the exact stage-list assertion. The isolated source was then restored.

Optional PDF audit also passed against the existing reviewed final PDF. The output was the same first four lines, followed by:

```text
PDF audit: PASS (text only; prior visual review is separate).
```

## Preservation

- Original `independent_check.py` and new `baseline_check.py`: SHA-256 `52426a4f0039b6df0ef235aab79d6c8273c82db07429873216796f77bf72aa4f`.
- Original `final-independent-check.py`: SHA-256 `b43b06b3a15bb4f052a2a85b1441256a4c84be64663370f1f0cc1369e20ca2ed`.
- New `portable_check.py`: SHA-256 `ae857303f98cd803a0f03d9f86c2a898182ec4ff933a4744933a06e447293b75`.

No mathematical claim was changed. Physical/classroom readiness remains untested.
