# Week 81 K–1 adult guide writer source

Writer-stage only; no critic/reviser approval is implied. Output: `../k1-guide.pdf` (four US Letter pages).

## Rebuild

Use Python 3, PyMuPDF (`import fitz`), pdfLaTeX, and the standard LaTeX packages named in `k1-guide.tex` (including Latin Modern and TikZ). Run:

```sh
./build.sh
```

The script first checks the final student PDF, generates answer tables from the independent solver, compiles twice, rejects overfull boxes, removes temporary TeX files, then runs the full checker. No machine-specific environment or absolute checkout path is embedded.

The checker first looks for `../k-1.pdf`; otherwise it searches ancestor folders for `plans/k1-drafts/week-81/k-1.pdf`. For a portable copy, put the final student `k-1.pdf` beside this `src` directory. It must match the inspected final seven-page W81-K-v1 PDF (SHA-256 is pinned in the checker). An intentional student revision requires a new inspection and revalidation, not merely changing the hash.

`check_guide.py` directly counts circles inside bucket outlines in the student PDF, validates page/problem order and empty answer spaces, and independently enumerates every legal descendant for one-bucket starts 0–12, two-bucket starts 0–8 each, and three-bucket starts 0–5 each. It verifies winners, unique winning moves, copying replies, every possible game length, all splits for Problems 6–7, board maxima, the launch, and guide page/header/diagram checks. It does not import the student checker or generator. `verified-data.tex` is generated, deterministic and included for inspection.

Sources consulted: final student PDF and its editable sources; the K–1 outline, two prior student reviews and drafts README; the original Week 81 shared packet/guide and owned source notes; the Week 98 facilitator model. The original reference books are not present in this checkout. The guide inherits game attribution from the owned Week 81 notes and makes no newly verified book-specific pedagogical claim.

The guide and kit remain unpiloted and physically unrehearsed. Digital checks do not validate counter fit, handling, adult workload or timings.
