# Problem files

Organizer decision, October 22, 2026: store a week as problem files when it is next revised, and store approved new weeks the same way. Finished weeks that nobody is changing stay as they are. The pilot and its results are in [experiments/atomic-problems-pilot/](../../../experiments/atomic-problems-pilot/README.md). Worked examples: its Week 50 folder (canvas layout), its Week 3 folder (flow layout), and [source/week-43/](../week-43/README.md), the first week converted for revision (canvas, with its own page template and an editable package).

One file per problem holds everything about that problem for every band. A week's packets are views built from the files: the K–1, 2–3 and 4–5 packets, first-route and return packets, a one-page problem menu, an adult key with one entry per problem, and a session pack.

## A week folder

```
source/week-NN/
  week.toml          week, topic, footer packet id and version, layout, each band's header and footer tag, guide files
  problems/NN-slug.md   one per problem, in packet order (file names sort into packet order)
  figures.py         canvas: figure code and, optionally, the page template; flow: only if figures are drawn in Python
  template.tex       flow only: the whole LaTeX document, with <<body>> where the problems go
  guide/*.tex        optional week-level prose for the key view: overview, prepare, hints, sources
  editable/          optional: the week's portable package (guide source, fonts, reference PDFs), see below
```

## A problem file

```
+++
id = "w50.same-length"            # permanent; never reuse or renumber
title = "A one-step and a two-step staircase"
grades = ["K-1", "2-3", "4-5"]
route = "first"                   # first | return | bonus; a list; or a table by band
page = "same"                     # optional: new | same; or a table by band
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

- **Sections.** `prompt`, `text` and `figure` are what children see; `key`, `key-figure` and `hints` go only to adults. `prompt`, `text`, `key` and `hints` bodies are LaTeX. A `figure` or `key-figure` body is a Python expression evaluated in the week's `figures.py`, returning LaTeX; in the flow layout, LaTeX pictures can go straight into a `text` section.
- **Band variants.** Consecutive sections of one kind are alternatives: a band uses the section that names it, else the untagged one, else nothing. A tag may only name bands in the problem's `grades`. A numbered problem needs a prompt that reaches each of its bands.
- **Setup files.** A shared rule or worked example is a problem file with `kind = "setup"`. It is not numbered and has no `prompt`; its rules go in `text`.
- **Numbers belong to views.** Each view numbers its problems; route packets keep the full packet's numbers so the guide's references hold. Refer to problems by id or title in notes and the use log.
- **Routes.** `route` says which route packets carry the file. It may differ by band, e.g. `route = { "2-3" = "return", "4-5" = "first" }`, and a setup that both routes need takes a list, `route = ["first", "return"]`.
- **Pages.** `page = "new"` starts a new page before the file and `page = "same"` keeps it on the current one. The default is `"new"` in the canvas layout and `"same"` (keep flowing) in the flow layout. Band differences go in a table: `page = { "4-5" = "same" }`.
- **Front matter** may hold only the keys above; anything else stops the build with the list of known keys.

## Layouts

`layout` in `week.toml` says how a band's sections become pages.

### Canvas

`layout = "canvas"` draws each page as one fixed TikZ picture. Sections carry positions: `@x,y` (or `@y`), `w=` and `size=` on a heading place text, and figure expressions place themselves. Weeks 11–51 and a few others were built this way. Problems on one page are files with `page = "same"`. In a route packet, a `"same"` file whose predecessor was left out starts a new page, so nothing is drawn over a missing problem's space.

The default page template is the house template in `canvas.py` (Week 50's: 185 × 235 mm, millimetres, y down). A week whose old builder used other units or margins defines any of these in its `figures.py`, and they replace the defaults:

| Name | What it is |
|---|---|
| `page_preamble(week, topic, header, footer)` | LaTeX from `\documentclass` to `\begin{document}` |
| `PAGE_OPEN`, `PAGE_CLOSE` | the LaTeX that opens and closes each page's picture |
| `page_prompt(n, body, x, y, size)` | a numbered prompt, from a `prompt` section |
| `page_text(x, y, body, w, size)` | a `text` section |

Unset `x`, `y`, `w` and `size` arrive as `None`; a band's `prompt_size` and `text_size` in `week.toml` fill `size` when a heading has none. [Week 43's figures.py](../week-43/figures.py) is the example: centimetres, y negated, Latin Modern, carried over from its old builder so the rebuilt LaTeX is byte-identical.

### Flow

`layout = "flow"` treats the sections as LaTeX that flows in reading order inside the week's own document template, as most weeks outside 11–51 were written. LaTeX breaks pages itself; a file with `page = "new"` forces a break before it.

`week.toml` for a flowing week:

```toml
week = 3
topic = "Shuffle machines"
packet = "F03"
version = "v5"
layout = "flow"
template = "template.tex"        # the whole document, with <<body>> where the problems go
prompt = '\textbf{Problem <<n>>:} <<body>>'   # how a numbered prompt is written (this is the default)
page_break = '\newpage'          # what page = "new" inserts (this is the default)
inputs = ["../week-03/src"]      # optional: other folders searched for \input files and graphics

[bands."K-1"]
header = "K–1"
tag = "K"
size = "14pt"                    # any other value here is a placeholder for the template
```

`template.tex` holds the document around the problems, usually the head of one of the old band files with its band differences replaced by placeholders:

```latex
\documentclass[<<size>>,letterpaper]{extarticle}
\newcommand{\packetlevel}{<<header>>}
\newcommand{\packetid}{<<footer>>}
\input{preamble}

\begin{document}

<<body>>

\end{document}
```

Placeholders are `<<week>>`, `<<topic>>`, the band's `<<header>>` and `<<tag>>`, `<<footer>>` (packet-tag-version, with `-first` or `-return` in route packets), `<<band>>`, and any other string or number in the band's table. A band table may also set its own `template` or `prompt`. The week folder and `inputs` are searched for files the LaTeX inputs, so a shared preamble or figure files can stay where they are.

The body is assembled from the band's files in order:

- a `prompt` becomes the `prompt` pattern with `<<n>>` and `<<body>>` filled in;
- a `text` section is copied exactly as written, apart from leading and trailing blank lines, so comments, `\\`, environments and `\newpage` inside it all work;
- a `figure` section is the LaTeX its Python expression returns;
- the sections of a file, and the files, are separated by a blank line, so each section starts a new paragraph;
- a forced page break goes on its own line between files.

A problem file in a flowing week:

```
+++
id = "w03.run-machines"
title = "Run each machine until every block is home"
grades = ["K-1", "2-3", "4-5"]
route = "first"
+++

## prompt [K-1]
Put each block in the top slot under its picture. Do turns until every block is back under its own picture, and make a tally mark for each turn.

## prompt
Put each block under its picture and run each machine. For each block, find the first turn after which it is back home. Then find the first turn after which all the blocks are back home at the same time.

## text [K-1]
\fig{k-p1a}
\fig[12pt]{k-p1b}

## text
\fig{m-p1a}
\fig[18pt]{m-p1b}
```

**Carrying a flowing week over.** Make `template.tex` from the head and tail of a band file. Cut each band file's body at its problems: the material before the first problem is a setup file, each problem's statement is its `prompt`, and everything after it up to the next problem is its `text`, copied verbatim. Remove the `\newpage` that preceded a problem and give that file `page = "new"`; a `\newpage` inside a problem's material stays in its text. Since every section starts a new paragraph, keep material that has no blank line before it in the same section as what precedes it. If the week's problem macro numbers itself with a counter, set the counter in the prompt pattern, so route packets keep the packet's numbers: `prompt = '\setcounter{prob}{<<n>>}\addtocounter{prob}{-1}\problem{<<body>>}'`. Merge files across bands where the bands do the same problem, with band-tagged sections for the differences; the file order must suit every band. Then compare (below). The [Week 3 example](../../../experiments/atomic-problems-pilot/week-03/) rebuilds all three band packets with no differing pixel; `build.py --tex` writes the LaTeX for a line-by-line diff against the old files.

## Views

`build.py <week> --out tmp/week-NN-views` writes, for each band, the full packet (`k-1.pdf`, `grades-2-3.pdf`, `grades-4-5.pdf`) and its first-route and return packets, then:

- `menu.pdf`: one page, every numbered problem once with a thumbnail of its page, its number in each band and its route. The grid shrinks to fit up to about forty problems on the page.
- `guide-keys.pdf`: the adult key, one entry per problem with its numbers by band, kernel, keys and hints, plus the `guide/` files that `week.toml` names (`overview`, `prepare`, `hints`, `sources`, each optional, and a `note` line).
- `session-pack.pdf` with `--tables K-1=3,2-3=4,4-5=3`: first-route packets in copies for each table.
- `<band>.tex` with `--tex`.
- With `--publish DIR`, the menu, key and route packets are copied to `DIR` as `week-NN-<view>.pdf`. Published views live in [band-views/](../../band-views/README.md) beside the shared-packet slices; after publishing, run `python3 lowell-math-circle-year-2/source/band-views/band_views.py readme` to list them.

The same files always give byte-identical PDFs.

## Converting a week on revision

The adult guide and any materials pages are not stored in problem files, so a correction confined to the guide, or a new printable kit, does not wait for a conversion. Convert when a student problem's wording, figure or order changes.

1. Claim the week on [WORKBOARD.md](../../../WORKBOARD.md).
2. Write `week.toml`, the problem files and `figures.py` or `template.tex` in `source/week-NN/`, carrying wording and figure code over unchanged. Keep the existing builder until the conversion passes.
3. Build into `tmp/` and compare with the current print PDFs until pages, extracted text and 100-dpi pixels all match:

   ```sh
   python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-NN --out tmp/week-NN-views --tex
   python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-NN-views lowell-math-circle-year-2/week-NN week-NN
   ```

   For a canvas week, also diff `tmp/week-NN-views/<band>.tex` against the old builder's LaTeX; byte-identical LaTeX is the strongest check.
4. Commit the conversion on its own, with no wording changes. Move the old builder into the week's `archive-before-problem-files-YYYY-MM-DD/` folder, with the previous source ZIP if the week has one.
5. Make the revision in the problem files, then follow AGENTS.md as for any revision: mathematical checks, rendered inspection of every changed page and band, the theorem-first guide, the portable source ZIP, the published views and the indexes.

### A week with an editable package

Weeks 11–51 ship a portable `editable/` package and source ZIP whose root `build.py` builds the student packets and the adult guide. After conversion (Week 43 is the pattern):

- The problem files are the student pages' only source. The old student generator is archived; `editable/src/regenerate.py` writes the band LaTeX from the problem files, and the package's `src/build.sh` runs it before compiling, so the package build and `build.py` give the same PDFs.
- The adult guide keeps its own source in `editable/` (for Week 43, `facilitator-src/guide.json`). If the problem files repeat its answer keys for the key view, a check script beside `week.toml` compares the two (Week 43's `check_guide_copy.py`); change both together.
- `package.py` writes the ZIP: the `editable/` package, plus the problem files in `problem-files/` and these tools in `problem-files/tools/`, so the ZIP alone can rebuild and edit everything. Check a clean rebuild from the extracted ZIP with the package's own `build.py` and verifier.

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-43 \
      --zip shuffling-picture-cards-week43-editable-source.zip --top shuffling-picture-cards-week43-source
  ```

- To release a revision (Week 43's October 23 card fixes are the example), build the package from an extracted ZIP in `tmp/`, archive the PDFs it replaces, copy the new ones to the print folder and `editable/reference-pdfs/`, update `review/reference-manifest.json` and drop any pixel allowances of changed pages, then republish the views and repackage. The print copies are the package build's; their student pages match `build.py`'s in pages, text and 100-dpi pixels.

## Errors

The tools stop at the first problem with the file, the line and what to change, for example:

```
error: source/week-43/problems/07-k1-two-starts.md, line 13 "## figure": the figure expression failed: NameError: name 'k1_two_start' is not defined
error: experiments/atomic-problems-pilot/week-03/template.tex, line 5: <<extras>> is not defined. Defined here: <<band>>, <<body>>, <<extra>>, ... Set other values in the band's table in week.toml
error: pdflatex failed for k-1.pdf:
! Undefined control sequence.
l.16 \fgi
That line comes from experiments/atomic-problems-pilot/week-03/problems/01-run-machines.md, line 14 "## text [K-1]".
```

Unknown front-matter keys, section kinds, routes and page values; band tags outside `grades`; a band with no prompt; duplicate ids; positions in a flowing week; and a template without `<<body>>` are all reported this way. A failed LaTeX run leaves `<view>.log` and `<view>.failed.tex` in the output folder.

## Tools

| File | Does |
|---|---|
| `atoms.py` | Reads and checks a week folder, resolves band variants, numbers problems and assembles canvas pages |
| `canvas.py` | The house canvas page template and drawing primitives |
| `flow.py` | The flow layout: fills the week's template with the problems in reading order |
| `build.py` | Writes every view; `--tables` adds a session pack, `--tex` the LaTeX, `--publish` copies the extra views |
| `compare.py` | Checks rebuilt band packets against the current print PDFs: pages, extracted text, 100-dpi pixels |
| `package.py` | Writes the portable source ZIP of a week that has an `editable/` package |

Requirements: Python 3.11+ (for `tomllib`), `pypdf`, Pillow, Poppler `pdftotext`/`pdftoppm`, and pdfLaTeX with TikZ, `fancyhdr`, `amsmath`, `booktabs`, `graphicx` and `helvet`, plus whatever a week's own template loads.
