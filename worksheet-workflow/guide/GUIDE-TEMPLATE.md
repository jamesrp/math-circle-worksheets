You are writing the adult guide for a finished week of student worksheets for an elementary math circle. The student pages are final; do not change them.

Files in your run folder <run>:
- PROMPT.md: the brief the worksheet author was given. Its "Activity outline" gives the mathematics and materials; its "Session context" describes the children, the adults and the hour. Read it first.
- final/k-1.pdf, final/grades-2-3.pdf, final/grades-4-5.pdf: the final student packets, with sources in final/src/.
- review.md and review-math.md: reviews of an earlier draft. They may help with answers, but the final pages changed after them, so work from the final PDFs.

Write the adult guide as one PDF at exactly <run>/final/facilitator.pdf, with its LaTeX source and any scripts in <run>/final/guide-src/. Header on every page: "<Week N / Topic / Adult guide>". Footer: "Bellingham Math Circle / <Week N> / <F0N-FAC-vX>" with the page number. Use LaTeX; a clean sans-serif font such as Source Sans Pro (\usepackage[default]{sourcesanspro}) matches the student pages.

Who reads it. Three adults, one at each fixed table: a parent volunteer who is not a mathematician at the K–1 table (four children), a mathematician at the 2–3 table (four children), and the organizer, a research mathematician, at the 4–5 table (three children). They read it the evening before, with a full-time job, and glance at it during the session. The parent needs plain-language answers and a few things to say; the mathematicians want the mathematics and the answers quickly.

What the guide contains, in this order:
1. The idea of the week in a few plain sentences, and what a good session looks like for each table.
2. Materials and preparation: exact counts for this group (the counts per child or per pair, the totals with a few spares), what to print for each table (which pages, how many copies; children share or get one page at a time), anything to cut, tape or set up, and anything to test with the real materials before the session. Include the specific notes below.
3. The hour: about five minutes of running around first; then a whole-group launch of two or three minutes showing the one concrete action everyone will use (say exactly what the adult does and says, and what one child does to show a legal move); then how each table pairs up (two pairs at K–1 and at 2–3; at 4–5 a pair with the third child as referee or playing the adult, rotating); a fallback game or activity for each table when attention runs out; and one sharing question at the end.
4. Table by table, problem by problem: what the children do, the answer or answers, and two or three hints to give in order if a child is stuck (the first hint should be a question or an action with the materials, not the answer). Mark which problems are the core of the hour and which are for children who get further. Say what to skip if a child is struggling. If a problem asks "find all", give the full list; if it asks "explain why", give an explanation a child could give with the objects.
5. The mathematics behind the week for the adults, in a page or less: the main facts and short proofs, and where it goes next.
6. What to write down after the session: which problems each table reached, what children tried and said, a drawing or claim worth keeping, and whether each claim was tried, guessed, checked in some cases, or explained.

Check every answer you print independently with code (a short script in guide-src/ that recomputes it from the positions and boards on the student pages). Do not trust the student sources' comments or the reviews. Keep the writing plain and short: tables and short paragraphs, no encouragement or filler. About six to ten pages.

Before you finish, compile the PDF, render every page to images (for example `pdftoppm -r 60 -png facilitator.pdf g`), and look at each one to check that nothing overflows or overlaps. Then reply with the PDF path and page count in under 60 words.

Specific notes for this week:
<materials and physical notes specific to the week>
