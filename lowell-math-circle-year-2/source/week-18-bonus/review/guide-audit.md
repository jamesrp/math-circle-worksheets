# Week 18 independent adult-guide audit

**Verified against the current guide JSON and PDF.** All overview, solutions P1–7, hints, extensions, assumptions, source roles and revised launch were independently checked. Five rendered pages were inspected; checksum evidence is in `guide-checks.json`. The new staffing/readiness/route wording changes no theorem. `guide-independent-check.py` is portable and uses only Python's standard library.

| Final task / claim | Independent result |
|---|---|
| P1–2 known holes | Verified every one-hole observation of 000,011,101,110 and minimum length 3. General recovery after at most e known erasures is equivalent to pairwise distance at least e+1; holes retain their positions. The two-message 000/111 extension survives two holes. |
| P3–4 check counter | Verified exactly odd distinct flip counts fail parity; 2 and 4 pass, zero passes, including changes to the check itself. Detection does not identify a flip: 00000 and 11000 can both produce 10000 by one flip. Flipping one cell twice is excluded and restores it. |
| New grid convention | Verified 11/01 → 110/011 → 110/011/101. Row checks are 0,1; column checks are 1,0; corner is 1; every completed row and column has exactly two filled counters. The printed convention and revised launch agree. |
| P5 | Verified completion 1100/0101/1001/0000 and the single-flip intersection rule including check counters. All 512 data arrays and 8,192 possible single flips pass the independent student checker. Corner values agree by counting the same data total modulo 2. |
| P6 | Verified nonempty minimum 4, and all 36 four-corner rectangles. All 65,536 flip subsets were checked. Every used row and column requires at least two flips; the minimum remains 4 whenever both dimensions are at least two. |
| P7 | Verified diagonal/off-diagonal ambiguity against one unchanged reference and the shared-row/shared-column ambiguity. Two arbitrary flips cannot be uniquely located from parity alone. |

The smaller-array extension was additionally enumerated: 2×2 has 2 invisible patterns including empty, 2×3 has 4, and 3×3 has 16; their positive minimum is four and their four-flip rectangle counts are 1, 3 and 9. This substantiates the classification question without replacing its open prompt with a procedure.

The theorem-first overview distinguishes erasure recovery, detection and location, with fixed orientation and once-per-selected-cell assumptions. Hints use valid unchanged states and respect those limits. Optional oral entry allows adults to read/record while children retain choices; explicit fixed KK11/3333/445 staffing is present.

Attribution is accurate: Hamming section 5 is recorded base context, with no new source-body reading asserted. Math Circle by the Bay Preface vii–x (PDF 8–11) supports the described teaching context; proposed transmission and return routes are distinguished from classroom observations. No unresolved mathematical issue. Physical procedures and fit remain unrehearsed; extracted-source ZIP verification is a separate release check.

## Verification-text refresh

Verified the final status-text revision independently against the saved pre-revision JSON. Only `verification` changed; every other parsed field is identical, including all overview, solution, hint, extension, material, launch and source content. Both new verification paragraphs were read in source and on the rebuilt page 5; that page was rendered and inspected, remains legible, and the guide remains five pages. All 39 JSON prose paragraphs occur in the rebuilt PDF. The packaged `guide-src/guide.json` is byte-identical. The independent guide checker passed again without mathematical changes.

Current guide JSON SHA-256: `dc0410e1ee3667e61bcc6cb0040d2527ba8fa82f8cb61d9c357b2a2887146267`.

Current guide PDF SHA-256: `3dd3bf54b87cce2658cc9cb9ba47da5821069f61b19ab2002a6e2355376b889e`.

The inspected release-validation record reports completed passing checks for its recorded reference files; current package synchronization and repeated ZIP validation belong to the root release process. This refresh confirms the new status wording and mathematical identity rather than claiming an additional ZIP rebuild by this reviewer. Physical fit and classroom rehearsal remain untested.
