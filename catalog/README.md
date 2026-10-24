# Activity catalog

One record per theme (Weeks 1–100 and the Week 1 encore), one per atlas investigation family, a concept map, and a builder that turns them into a browsable explorer and the [catalog page](../CATALOG.md). The records describe the activities; the PDFs, guides and review cards stay where they are, and the builder finds each week's current print files itself.

The explorer is one self-contained page, `explorer/index.html`: download it and open it in a browser. The organizer's published copy is the [Math Circle Explorer](https://claude.ai/artifact/DarUYkLh2qfEBBDGF4cZm1) (private to the owner unless shared). It has five views: an activity list with filters (band, area, reasoning move, concept, status, review verdict, materials, app) and a detail panel with print links and connected themes; the concept map in area lanes; the network of links between themes; strands, one per area, ordered by prerequisites for planning return visits; and the path, the [proposed six-year path](../plans/six-year-path.md) as six year columns of session cards, with links back to the sessions each one returns to and a selector that follows a child from a chosen starting grade. The published copy was updated with the path view on October 24; republish it when the explorer changes. Marks for themes used with a group stay in the viewer's browser.

```
catalog/
  concepts.toml       areas, reasoning mechanisms and the concept map (each concept names the concepts it requires)
  weeks/week-NN.toml  one record per theme; week-01e.toml is the encore
  atlas/XX-NN.toml    one record per atlas investigation family (AD, GA, AP)
  path.toml           the proposed six-year path: 120 sessions by year, as week, return-visit and atlas ids
  check_path.py       checks path.toml against the records; build.py runs it, and --tables prints the plan's year tables
  build.py            checks every record and the path, and writes explorer/index.html and CATALOG.md
```

Rebuild after changing a record, a concept or a week's PDFs:

```sh
python3 catalog/build.py
```

The build stops on an unknown concept, mechanism, area or week, a cycle in the concept map, or a missing required field. It also stops when the six-year path breaks one of its rules: an unknown id, a concept before one it requires, the same theme twice in a year, three sessions in a row from one area, a year with fewer than five areas, a revisit closer than a year or without a catalog link behind it, three heavy kits in a row, or a session without a K–1 or Grades 2–3 entry. Run `python3 catalog/check_path.py` to check the path alone and print its summary. When a record change breaks the path, change [path.toml](path.toml) and the [plan](../plans/six-year-path.md) together.

## A week record

```toml
week = "9"                       # "1e" for the encore
title = "Bouncing paths"         # the theme as the packets name it
hook = "Send a ball at 45 degrees across a grid table and predict which corner pocket it falls into."
math = "Unfolding the table into mirror copies turns the bouncing path into a straight line, so on a p-by-q table the ball reaches a corner after lcm(p, q) diagonal steps, and the parities of p/g and q/g (g = gcd) decide which corner. Scaling the table changes nothing."
discover = "Only the shape of the table matters, and a parity rule predicts the pocket."
gem = "Billiards on a rectangle is a straight line on a torus in disguise."
concepts = ["reflection", "lcm", "parity"]   # what it is about, most central first (1–4)
uses = ["gcd"]                   # concepts it assumes beyond everyday K–5 arithmetic (0–3)
mechanisms = ["unfold", "invariant"]          # 1–3 reasoning moves children actually use
bands = ["K-1", "2-3", "4-5"]    # bands with student pages (for a shared packet, the bands its pages name)
reading = "K–1 needs none with an adult reading; upper bands read one-sentence tasks."
arithmetic = "Counting squares; 4–5 uses multiples and common multiples."
materials = ["grid tables (printed)", "a counter or toy car"]
prep = "Print packets; about 10 minutes."
status = "unpiloted"             # piloted | organizer-approved | unpiloted
verdict = "revise"               # review card verdict: keep | revise | revised (its must-fixes done) | rework | merge | none (no card yet)
verdict_note = "The guide's walking rule is wrong once the ball is coming down."
app = "Mirror Couriers"          # the app family or group that carries it, or ""
app_decision = "in app"          # in app | not porting | open

[[related]]
week = "21"
kind = "leads-to"
note = "Unfolding again, now to prove a reflected path is shortest."

[[related]]
week = "31"
kind = "same-theorem"
note = "gcd decides both the corner a ball reaches and which orchard trees are visible."
```

### Fields

| Field | Required | Meaning |
|---|---|---|
| `week`, `title` | yes | The library number and the theme's name. |
| `hook` | yes | One sentence in plain words: what a child does with their hands and eyes. |
| `math` | yes | One to three sentences for an adult: the actual theorem, invariant or fact children can reach, with its assumptions. Not a topic label. |
| `discover` | no | What children are meant to discover, in one sentence. |
| `gem` | no | One sentence on why a mathematician would enjoy it: the connection or surprise. |
| `concepts` | yes | One to four concept ids from `concepts.toml`, most central first. |
| `uses` | no | Concept ids the activity assumes; these draw the prerequisite edges. |
| `mechanisms` | yes | One to three mechanism ids from `concepts.toml`. |
| `bands` | yes | Any of `K-1`, `2-3`, `4-5` with student pages. |
| `reading`, `arithmetic` | yes | Short prerequisite notes, as the guide and card state them. |
| `materials` | yes | What a table needs beyond the printed pages, paper and pencils. An empty list means paper only. |
| `prep` | no | Preparation for a parent volunteer, short. |
| `status` | yes | `piloted` only with a classroom report; `organizer-approved` when the organizer reviewed and promoted it; otherwise `unpiloted`. |
| `verdict`, `verdict_note` | yes, note when not keep | From the review card in `plans/review/`. `none` when no card exists. |
| `app`, `app_decision` | yes | From the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md). |
| `[[related]]` | 2–6 entries | Links to other weeks, each with a `kind` and a one-line `note` saying what the connection is. |

Relation kinds:

| Kind | Means |
|---|---|
| `leads-to` | This week prepares children for that one: it introduces an object, move or idea that week relies on. |
| `revisits` | The same object or theme returns with a genuinely different question. |
| `same-theorem` | Different objects, the same underlying theorem or mechanism. |
| `same-object` | They share a board, material or object but ask about different mathematics. |
| `contrast` | Worth putting side by side because they differ instructively. |

Write `leads-to` on the earlier week only; the explorer shows the reverse link on the later week. The other kinds can be written on either side, and the explorer merges duplicates.

Records are descriptions, not new claims: take the mathematics from the theorem-first guide and the review card, and say "unpiloted" unless a classroom report exists.

## Atlas investigations

The [mathematics atlas](../plans/atlas/README.md) has ninety investigation families with student pages and facilitator guides in four print books (the random ten, and the algebra/discrete, geometry/analysis and probability/applications books). They are not weekly themes, but they belong on the same map, so the explorer can show them beside the weeks (the Library filter) and on the concept map and strands. Each family has a short record in `catalog/atlas/XX-NN.toml`. The builder takes the printed title and page ranges from the two page finders and the random-ten builder, and the adult question, anchor theorem, capability gates, materials and preparation from `plans/atlas/families/*.json`, so the record holds only what those files lack:

```toml
id = "AD-09"
hook = "Advance two small clocks of different sizes together one step at a time and decide which pairs of readings can occur at the same moment, and when."
concepts = ["remainders", "gcd", "lcm"]   # 1–4 concept ids, most central first
uses = ["divisibility"]                  # concept ids assumed
mechanisms = ["every-case", "construct"]
bands = ["2-3", "4-5"]                   # K–5 bands with a genuine entry on the printed pages; [] when the entry needs algebra or more
gem = "The Chinese remainder theorem as two clocks."   # optional
proposed_concepts = []                   # optional: "id: description" for a concept the map lacks

[[related]]                              # links to weekly themes, same kinds as week records
week = "4"
kind = "revisits"
note = "Week 4's hops follow one remainder orbit; here two orbits must agree at the same time."
```

The builder checks these like week records. The cards' launches are not shown, because the print books often use a different example from the card; [plans/atlas/catalog-notes.md](../plans/atlas/catalog-notes.md) lists the differences the readers found.
