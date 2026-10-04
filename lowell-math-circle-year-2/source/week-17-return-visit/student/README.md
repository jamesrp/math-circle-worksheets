# Week 17 student return-visit draft

Three investigations, one per page, in a shared collection. The approximate band appears in each page header. Adult reading and arrow drawing can support the concrete first investigation.

Build from this folder with a TeX installation containing pdfLaTeX, TikZ/PGF, geometry, fancyhdr, array, amsmath, Helvetica and Latin Modern:

```sh
sh build.sh
```

The PDF is written to `../return-visit.pdf`. If pdfLaTeX is not on PATH, set `PDFLATEX` to its executable path. No external graphics, private fonts or repository-relative dependencies are needed. Print single-sided, US Letter, at 100 percent.

`verify.py` checks the example machine, the target machine constructions, parity outputs, and the common-ending argument. It writes a JSON report to a path supplied as its only argument. These are mathematical and digital checks; the materials, physical procedures and classroom use remain untested.
