# Week 38 revised student source

Revised and unpiloted. Physical paper/tape models, exact center cuts, the movable-arrow procedure, and marker handling have NOT been pretested. Those practical checks remain gates before classroom use; digital seam and rendering checks do not clear them. All cuts are adult-only. Use the four-strip allocation: two initial A/B bands and two spare strips. Grades 4–5 rebuilds uncut A/B from the spares before arrow transport. K–1 access depends on the child tracking an edge through the joined seam with an adult.

Run `bash build.sh` with Python 3, pdfLaTeX, TikZ, Latin Modern, AMS fonts, and Poppler. The portable build uses the caller's TeX environment, runs TeX twice, and writes three five-page PDFs one directory above this folder, with render/check files in `../qa/`.

Four-dot pictures denote reachability classes of dots on boundary components; unoccupied boundary components are allowed. The five integer partitions of four exhaust the targets. With b boundary components exactly the partitions with at most b groups are possible. Before cutting A has b=2 and B b=1; afterward all A pieces together have b=4, and B b=2. Problem 7 in the younger bands is possible on the cut A result and impossible on the cut B result. Four edge dots occupy four distinct edges of the two cut A annuli, covering both pieces.

Seam maps U→U, L→L and U→L, L→U give the verified cut connectivity; each result component is an annulus. The movable transverse arrow crosses the reversing seam once on uncut B, reversing direction relative to its start, and preserves direction on A. No physical trial or classroom pilot is claimed.
