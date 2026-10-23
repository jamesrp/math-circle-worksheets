# Problem files

Organizer decision, October 22, 2026: store a week as problem files when it is next revised, and store approved new weeks the same way. Finished weeks that nobody is changing stay as they are. The pilot and its results are in [experiments/atomic-problems-pilot/](../../../experiments/atomic-problems-pilot/README.md); its Week 50 folder is the worked example.

One file per problem holds everything about that problem for every band. A week's packets are views built from the files: the K–1, 2–3 and 4–5 packets, first-route and return packets, a one-page problem menu, an adult key with one entry per problem, and a session pack.

## A week folder

```
source/week-NN/
  week.toml          week, topic, footer packet id and version, each band's header, footer tag and prompt size, guide files
  figures.py         the week's figure code, called by name from problem files
  guide/*.tex        week-level guide prose: the theorem-first overview, launch, hints, sources
  problems/NN-slug.md   one per problem, in packet order
```

## A problem file

```
+++
id = "w50.same-length"            # permanent; never reuse or renumber
title = "A one-step and a two-step staircase"
grades = ["K-1", "2-3", "4-5"]
route = "first"                   # first | return | bonus
page = "same"                     # optional: stay on the previous problem's page
scale = "actual"                  # optional: must print at 100%, so no shrinking format may use it
kernel = "Regrouping horizontal and vertical pieces proves the two lengths equal."
app = ""                          # optional: the app family or group that ports it
+++

## prompt [K-1]
Follow both staircases with string. Compare the two pieces of string.

## prompt
Compare the lengths of these two staircases. Find their exact lengths using the width and height.

## figure
diagram(42, [...])

## text @9,184 [K-1]
Circle: same length / solid longer / dashed longer

## text @9,184
Solid: \rule{20mm}{.3pt} mm     Dashed: \rule{20mm}{.3pt} mm

## key
Both solid and dashed routes are \textbf{280 mm}. ...
```

- **Sections.** `prompt`, `text` and `figure` are what children see; `key`, `key-figure` and `hints` go only to adults. Bodies are LaTeX; a `figure` body is a Python expression evaluated in `figures.py`.
- **Band variants.** Consecutive sections of one kind are alternatives: a band uses the section that names it, else the untagged one, else nothing. A tag may only name bands in the problem's `grades`.
- **Numbers belong to views.** Each view numbers its problems; route packets keep the full packet's numbers so the guide's references hold. Refer to problems by id or title in notes and the use log.
- **Positions.** `@x,y` (millimetres) and `w=` place text on a canvas page. A shared rule or worked example is a problem file with `kind = "setup"`, which is not numbered.

## Layouts

`layout = "canvas"` in `week.toml` draws each page as one fixed TikZ picture with positions in millimetres, as Week 50's builder did; Weeks 42–51 and a few others use builders of that kind. Weeks written as flowing LaTeX, which is most of the rest, need `layout = "flow"`, which is not built yet: the first such week to be converted adds it to `atoms.py`, keeping the same problem-file format.

## Converting a week on revision

The adult guide and any materials pages are not stored in problem files, so a correction confined to the guide, or a new printable kit, does not wait for a conversion. Convert when a student problem's wording, figure or order changes.

1. Claim the week on [WORKBOARD.md](../../../WORKBOARD.md).
2. Write `week.toml`, `figures.py`, `guide/` and the problem files in `source/week-NN/`, carrying wording and figure code over unchanged. Keep the existing builder until the conversion passes.
3. Build into `tmp/` and compare with the current print PDFs until pages, extracted text and 100-dpi pixels all match:

   ```sh
   python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-NN --out tmp/week-NN-views
   python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-NN-views lowell-math-circle-year-2/week-NN week-NN
   ```

4. Commit the conversion on its own, with no wording changes. Move the old builder into the week's `archive-…` folder.
5. Make the revision in the problem files, then follow AGENTS.md as for any revision: mathematical checks, rendered inspection of every changed page and band, the theorem-first guide, the portable source ZIP and the indexes.

## Tools

| File | Does |
|---|---|
| `atoms.py` | Reads a week folder, resolves band variants, numbers and places problems |
| `canvas.py` | House page template and drawing primitives for canvas pages |
| `build.py` | Writes every view; `--tables K-1=3,2-3=4,4-5=3` adds a session pack |
| `compare.py` | Checks rebuilt band packets against the current print PDFs |

Requirements: Python 3.11+ (for `tomllib`), `pypdf`, Pillow, Poppler `pdftotext`/`pdftoppm`, and pdfLaTeX with TikZ, `fancyhdr`, `amsmath`, `booktabs` and `helvet`.
