# Week 68 adult guide source

Rebuild with Python 3 and a standard TeX Live installation providing pdflatex,
article, geometry, fancyhdr, amsmath, amssymb, booktabs, array, and hyperref:

    python3 check_math.py
    python3 build.py --out /path/to/output

The builder writes facilitator.pdf and a diagnostic guide-build.log. It runs the
independently authored, standard-library-only answer checker before compilation.
No student files, downloaded references, or machine-specific cache is needed.
The student packet is a separate source package. Numerical checks are finite
evidence; general mathematical arguments and activity limits are in the guide.
This is an unpiloted prototype. Physical materials have not been rehearsed.
