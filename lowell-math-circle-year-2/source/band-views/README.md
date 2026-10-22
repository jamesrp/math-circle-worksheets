# Band views: page indexes and builder

Builds [../../band-views/](../../band-views/README.md): band slices and a one-page menu for each shared student packet (Weeks 52–84, 88–93 and 97). The packets themselves are not changed.

- `indexes/week-NN.toml` lists every page of a week's packet: its grade range as printed in the page header, its problem numbers, and `rules_for` when an earlier page's opening rules are needed by a later band. Each index was drafted from the page headers on October 22, 2026, then checked against the rendered pages. Weeks 52, 91 and 92 have `rules_for` pages; the comment at the top of those indexes says why.
- `band_views.py build` checks every index against its PDF (footer id, page count, ranges and problem numbers) and stops for any week that no longer matches, then writes the slices, the menus and the folder README. Builds are reproducible: the same inputs give byte-identical PDFs.
- `band_views.py draft week-NN` writes a new index from the headers and never overwrites one. Check it by eye, add `rules_for` where needed, and set `checked`.

Requirements: Python 3.11+, `pypdf`, Poppler `pdftotext`, and pdfLaTeX with `graphicx`, `fancyhdr` and `helvet`.

```sh
python3 lowell-math-circle-year-2/source/band-views/band_views.py build
```

When a listed packet is revised, rebuild here in the same change. If the build reports a mismatch, update that week's index first, then look at its new menu.
