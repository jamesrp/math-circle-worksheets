# Week 95 revised student sources

Student pages only; two packets, four pages each. K–1 omitted by the authorized outline override. These are unpiloted revised drafts. Physical mixing, marker retention, erase/reset and tactile uniformity have not been rehearsed.

Build with Python 3 standard library and a TeX installation containing pdflatex, TikZ, Latin Modern, fancyhdr, array and amsmath:

```
python3 build.py --output-dir /path/to/output
python3 verify.py
```

`build.py` is the editable source, including text and TikZ diagrams. It accepts an arbitrary output directory and suppresses dates, IDs and path metadata for deterministic reconstruction. Generated TeX, aux and log files are build intermediates. No absolute source locations are needed; the /Library/TeX fallback only locates the Mac TeX executable if it is absent from PATH.

The printed repeat records are **invented illustrative records**, not collected classroom data or a seeded simulation. Lower: first=second=4, overlaps 2,1,3,1,2,0; these can all occur in the same unchanged population of 8, or of 16. Upper: first=second=6, overlaps 1,2,3,2,0; all can occur in the same unchanged population of 18. The examples intentionally include a zero and contradictory single-record guesses. Neither packet claims that its example series uniquely determines the hidden total. Clear all marks and return all objects between rounds. The model treats each catch as a uniform subset; shaking a real bag approximates this assumption.

Material choice: use an opaque bag and 24 identical commercial flat counters with visible, erasable marker dots that cannot be detected by touch. Where letter identities are used, write small letters on otherwise identical counters. Alternatively use identical-size flat cards with erasable faces. Diagrams are illustrations, not cutouts. A screen hides the keeper's count. Return the whole first catch, mix, and keep the second catch out until recording its overlap. The population remains fixed through all rounds in a series.

Mathematical verification is in `verify.py`: exact overlap support and expectation, all displayed identities and guesses, positive support for the printed repeated records, and balanced budget optimization. The lower packet's first identity pair has union A–G (7 objects), overlap B,D,E (3). The next has union A–J (10). For fixed M,n,R the minimum total is M+n−R; there is no finite maximum without an external cap. For the upper zero record, finite examples include N=12 and N=18.

The uniform-subset expectation is M*n/N. Fraction matching produces M*n/R when R>0. It is an estimate, not a guarantee or generally unbiased estimator. R=0 gives no fraction-matching finite total but is compatible with every N≥M+n. With fixed budget s≤N, balanced integer M,n maximize M*n and therefore expected overlap; no claim is made about every definition of estimator quality. Lost marks can lower observed overlap and inflate a positive-ratio estimate, or produce a zero overlap.

Source basis: the supplied Week 95 outline, citing Brett McClintock, *Mark-resight models*, chapter 18 in Cooch and White's MARK book, PDF pp. 2–3 (printed 18-2–18-3). The writer did not independently retrieve the source. Exact finite sampling and budget checks are independently verified here. No old worksheets were inspected or used.

Revision record: both p.1 shared rules preserve the same objects across a series, distinguish blind sampling trials from deliberately arranged legal catches, and retain uniform-subset sampling, full return/mixing, no within-catch repeats and mark retention. Lower p.3 Problem 5 explicitly permits arrangement. Upper p.2 Problem 3 now shows a non-task fraction-matching example before its first task: second catch A*,B,C; two marked objects in the bag; a matching model with groups A*,B,C and D*,E,F; estimate six because 2/6=1/3. This is a model for the rule's guess, not a claim that a sample recovers truth. Existing variability and counterexamples are retained.
