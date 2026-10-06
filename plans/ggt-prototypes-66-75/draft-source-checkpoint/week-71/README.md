# Week 71 student prototype

One four-page shared Grades 4–5 student draft, unpiloted; writer stage only. Entry requires ruler use, matching a reflected picture and recording successive letters. The first page demonstrates a non-task AD path both in one room and across reflected copies. Children choose rays in the supplied windows. A partner checks letters and forbidden corner hits. The final comparison asks for a general explanation and is readiness-dependent. Actual mirror handling and print-scale tracing have not been rehearsed with children.

Build with `python3 build.py` or `python3 build.py --out /chosen/directory`; requires Python 3 and pdfLaTeX/TikZ with geometry, fancyhdr, amsmath, amssymb, array and Latin Modern. No network or repository files are needed. `students.tex` is the editable entrypoint and includes `windows.tex`. Run `python3 make_diagrams.py` to regenerate the two exact-reflection window macros after changing their geometry. The generated macros are included for direct TeX compilation.

Run `python3 check_math.py` to independently verify the AD worked example, an ABA rhombus witness using explicit radical coordinates, open-wall intersections and reflection laws, plus 30 twelve-bounce words under rectangle scaling. The ABA witness is only in the verification script, not supplied as a student answer. For a rectangle, the first and third A crossing lines in the A-B-A unfolding are the same line; a noncorner straight shot cannot cross it twice. No assertion of impossibility is inferred from failed searches.

Primary references: *How to hear the shape of a billiard table*, introductory examples, pp. 3–6, https://justinlanier.org/wp-content/uploads/2020/10/bounce.pdf ; bounce-spectrum rigidity context, https://arxiv.org/pdf/1804.05690 . The elementary rectangle comparison concerns existence of words, not preservation of individual angles under nonuniform scaling. The student text and diagrams are newly authored; no reference text is bundled.

Digital QA: four pages built, rendered and viewed individually at 100 dpi; no overflow warnings. The build writes `students.pdf` and `build.log` into the requested output directory.
