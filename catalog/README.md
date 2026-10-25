# Activity catalog

One record per theme (Weeks 1–100 and the Week 1 encore), one per atlas investigation family, one per draft theme awaiting the organizer's review, a concept map, and a builder that turns them into a browsable explorer and the [catalog page](../CATALOG.md). The records describe the activities; the PDFs, guides and review cards stay where they are, and the builder finds each week's current print files itself.

The explorer is one self-contained page, `explorer/index.html`: download it and open it in a browser. The organizer's published copy is the [Math Circle Explorer](https://claude.ai/artifact/DarUYkLh2qfEBBDGF4cZm1) (private to the owner unless shared). It has five views: an activity list with filters (band, area, reasoning move, concept, status, review verdict, materials, app) and a detail panel with print links and connected themes; the concept map in area lanes; the network of links between themes; strands, one per area, ordered by prerequisites for planning return visits; and the path, the [proposed six-year path](../plans/six-year-path.md) as six year columns of session cards, with links back to the sessions each one returns to and a selector that follows a child from a chosen starting grade. The published copy was updated with the path view on October 24; republish it when the explorer changes. Marks for themes used with a group stay in the viewer's browser.

[Drafts awaiting review](#drafts-awaiting-review) appear with dashed outlines on a yellow ground: draft themes in the list (the Library filter, on by default, and an "Awaiting review" filter that also finds weeks with draft pages), on the concept map (a count on each concept a draft is about, and dashed boxes for concepts only drafts use) and in the network (dashed dots placed near the weeks they link to, without moving any week); a week's detail panel lists its pending drafts. A switch on each map hides them. Drafts stay out of the strands and the path.

```
catalog/
  concepts.toml       areas, reasoning mechanisms and the concept map (each concept names the concepts it requires)
  weeks/week-NN.toml  one record per theme; week-01e.toml is the encore
  atlas/XX-NN.toml    one record per atlas investigation family (AD, GA, AP)
  drafts/<slug>.toml  one record per draft theme awaiting the organizer's review, with no week number yet
  path.toml           the proposed six-year path: 120 sessions by year, as week, return-visit and atlas ids
  check_path.py       checks path.toml against the records; build.py runs it, and --tables prints the plan's year tables
  build.py            checks every record and the path, and writes explorer/index.html and CATALOG.md
```

Rebuild after changing a record, a concept or a week's PDFs:

```sh
python3 catalog/build.py
```

The build stops on an unknown concept, mechanism, area or week, a cycle in the concept map, a missing required field, or a draft whose folder, outline or band PDFs do not match its record. It also stops when the six-year path breaks one of its rules: an unknown id, a concept before one it requires, the same theme twice in a year, three sessions in a row from one area, a year with fewer than five areas, a revisit closer than a year or without a catalog link behind it, three heavy kits in a row, or a session without a K–1 or Grades 2–3 entry. Run `python3 catalog/check_path.py` to check the path alone and print its summary. When a record change breaks the path, change [path.toml](path.toml) and the [plan](../plans/six-year-path.md) together.

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
| `[[drafts]]` | no | New pages for this week awaiting the organizer's review; see [below](#new-pages-for-an-existing-week). |

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

## Drafts awaiting review

Drafts that are waiting for the organizer's review go into the catalog so that the explorer can show where they would sit, but they are kept apart from the library: they are not approved, piloted or on the path, and nothing about a week changes until its draft is adopted.

### A draft theme

A new theme drafted with the worksheet workflow, with no week number yet, has a record in `catalog/drafts/<slug>.toml` named after its outline. It mirrors a week record, without the review-card and app fields:

```toml
id = "poisoned-cookie"           # the outline's slug, and the file name
title = "Poisoned cookie"        # the topic the draft pages' header names
status = "draft"                 # always; an approved theme gets a week record instead
rank = 3                         # optional: its rank in the scouting list
date = "2026-10-24"              # when the student-page drafts were made
folder = "plans/topic-scouting/drafts/poisoned-cookie/"   # the draft pages and reviews
outline = "plans/topic-scouting/poisoned-cookie.md"
hook = "Take turns biting a grid of cookie counters with an L-shaped bite card, ..."
math = "On every rectangle bigger than one cookie the first player can win: ..."
discover = "..."
gem = "Strategy stealing proves a win exists with no strategy in hand."
concepts = ["strategy-stealing", "backward-induction", "copying-strategies"]
uses = []
mechanisms = ["copying", "work-backward", "every-case"]
bands = ["K-1", "2-3", "4-5"]    # must match the folder's k-1.pdf, grades-2-3.pdf, grades-4-5.pdf
reading = "..."
arithmetic = "..."
materials = ["25 mm counters, about 25 per pair, with one different poison counter", "a 15 cm L-shaped bite card per pair"]
prep = "..."
untried = "The bite card on neighbouring boards (the build checks the spacing)."   # optional: the drafts index's "not yet tried physically"

[[related]]                      # 2–6 links to existing weeks, same kinds as week records
week = "7"
kind = "same-theorem"
note = "Week 7 labels take-away piles win or lose by working backward from the end; the older tables label small Chomp boards the same way."
```

The fields mean what they mean on a week record. `id`, `title`, `hook`, `math`, `concepts`, `mechanisms` (one to three), `bands`, `reading`, `arithmetic`, `materials`, `status`, `date`, `folder` and `outline` are required; `discover`, `gem`, `uses`, `prep`, `untried`, `rank` and `related` are optional, though every draft so far has 2–6 related weeks. Take the content from the outline, the scouting table and the drafts index; describe the drafts and add no new claims. A related link points from the draft to an existing week, so use the symmetric kinds unless the draft really prepares children for that week. The builder lists the folder's PDFs and its `review.md` and `review-math.md`, and links the outline and the indexes beside them; it stops on an unknown concept, mechanism or week, a bad relation kind, a missing folder or outline, a band without its PDF (or a band PDF the record does not list), or two drafts with the same rank. The explorer labels draft themes D1, D2, … by rank.

When the organizer approves a draft theme, give it a week number, add its week record (`catalog/weeks/week-NN.toml`) and delete its draft record in the same change.

### New pages for an existing week

A return visit or a set of K–1 pages drafted for an existing week is a `[[drafts]]` entry on that week's record. It changes nothing else: the week's `bands`, `status` and print files stay as they are until the pages are adopted.

```toml
[[drafts]]
kind = "return visit"            # return visit | K-1 pages
path = "plans/return-visit-drafts/week-53/"
date = "2026-10-25"
note = "Dearest links, paid trips and optional places."   # optional: what the pages are about, from the drafts index
```

The folder must exist and hold at least one PDF. The explorer shows the entry in the week's detail panel with links to its pages, reviews and the drafts index, marks the week in the list and the network, and the list's "Awaiting review" filter finds every week with one. When the pages are adopted, remove the entry in the same change that updates the week's bands, print files and status.
