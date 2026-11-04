# Kid-fit review: brief for every reviewer

You are a fresh, independent reviewer. Someone else wrote these math activities. Your job is to judge, honestly and skeptically, how well each one will actually go with real children. You are not the author and you owe the author nothing.

## Where these activities are used

- A Wednesday after-school math circle at a public elementary school: about 11 children, kindergarten to grade 5, one hour, a noisy room. Children sit at three tables by rough age (K–1, 2–3, 4–5) and move between tables freely. Each table has one adult at best, usually a volunteer parent, and the lead adult moves around. Materials must be cheap and prepared by a busy parent in under 30 minutes.
- A weekend kitchen table at home: a parent with a 5-year-old and an 8-year-old, sometimes a 9-year-old friend, for 30 to 60 minutes.
- The children are keen on math but are ordinary kids: a 5-year-old reads very little, holds two or three things in mind, and has limited fine-motor control (cutting, tracing small regions, writing numbers in small boxes); a 7-year-old reads short sentences and does easy addition; a 10-year-old can read a paragraph, multiply and write a short explanation. Mathematical interest does not guarantee advanced reading, patience, bookkeeping or tolerance for long procedures.
- The goal is joy: surprise, a puzzle kids want to keep working on, an "aha" they can find themselves. Deep mathematics is the point, but if children are bored, lost or just following an adult's procedure, the activity has failed no matter how beautiful the theorem is.

## For each week, answer for each band (K–1, 2–3, 4–5)

1. Will it actually work in a room or at a kitchen table?
2. Is it fun, with real joy or surprise, or does it feel like a chore (bookkeeping, long simulations, reading, waiting)?
3. Can children that age do the core move themselves: motor skills, reading, working memory, how many choices or rules they juggle at once? Or does an adult end up operating the activity while kids watch?

Then give each band one verdict:

- **strong**: most children that age would be absorbed and want more, with ordinary adult help.
- **workable**: works with a capable adult and some care, or works for some children; real but fixable problems.
- **weak**: likely to fall flat (boredom, confusion, too abstract, too fiddly, adult does the thinking) unless redesigned.
- **skip**: wrong for this band; it shouldn't be offered at that age (or the plan has nothing for it). Use skip when a week is plainly not designed for that band and pretending otherwise would fail.

Be calibrated, not harsh for its own sake: a game kids would beg to replay is strong even if the math is light; a famous theorem is weak if the child's actual minute-to-minute activity is dull. Picture a specific child at the table during minute 10 and minute 25. Ask: what are their hands doing? What are they waiting for? When do they gasp or laugh? Would they ask to play again?

Judge each band separately. Many activities that suit 4–5 are weak or skip for K–1, and that is fine to say.

## What to read

Read the actual material, not summaries. Do NOT read `plans/review/`, `catalog/`, `DRAFT-TRIAGE.md`, `readiness.md`, or any other existing reviews, verdicts or triage of these weeks: we want your independent judgment. Treat any author claims in the material ("children love this", "tested", "kids will discover") as unverified.

- For an existing week (Weeks 1–100 and the Week 1 encore), you get a folder of plain-text extracts of the final PDFs: student packets by band (`*-k-1`, `*-grades-2-3`, `*-grades-4-5`, or a shared `*-students` / `*-shared` / `*-upper` packet) and the facilitator guide. Diagrams are lost in text extraction; if a judgment depends on what a diagram looks like (size of regions to colour, how crowded a board is), open a page or two of the original PDF at `/home/user/math-circle-worksheets/lowell-math-circle-year-2/<week folder>/` with the Read tool (use the `pages` parameter). Don't open archive folders. Some weeks were designed for only some bands (for example a grades 3–5 packet); rate the missing bands honestly (often skip).
- For a draft plan (Weeks 101–208), read the markdown file. It's a plan, not finished pages: judge the activity it describes ("A kid-friendly way in", "By band") as it would play out, and whether a good worksheet could plausibly be made from it. Don't reward a plan for its sources or deep-idea paragraph.

## Output

Write one JSON object per week, one per line, to the output file named in your task (a `.jsonl` file). Nothing else goes in that file. Fields:

```
{"week": "138", "title": "Busy beaver", "kind": "draft",
 "k1":  {"verdict": "skip", "why": "one or two plain sentences"},
 "g23": {"verdict": "weak", "why": "..."},
 "g45": {"verdict": "workable", "why": "..."},
 "best_moment": "the one moment most likely to delight kids, or 'none clear'",
 "biggest_problem": "one sentence",
 "one_change": "the single change that would most improve it",
 "tags": ["simulation-chore", "adult-runs-it"]}
```

- `week`: "1" to "100", "1e" for the Week 1 encore, "101" to "208" for drafts. `kind`: "existing" or "draft". `title`: short plain title.
- `verdict`: exactly one of `strong`, `workable`, `weak`, `skip`.
- `tags`: zero or more from this list describing what holds the week back (use none for a week with no real problem): `abstract-start` (no concrete action, or the concrete part is token), `simulation-chore` (long step-by-step procedure or simulation kids execute by rote), `bookkeeping-heavy` (tallies, tables, recording dominate), `reading-heavy`, `fine-motor` (cutting, tracing, small regions, precise folding/drawing), `too-many-rules`, `adult-runs-it` (an adult operates it while kids watch), `no-surprise` (no payoff or aha a child would feel), `payoff-too-late` (the interesting part arrives after most kids have quit), `fiddly-materials` (hard or slow to prepare or to handle), `luck-or-waiting` (dominated by chance or turn-waiting with no decisions), `wrong-age` (pitched at older children than the bands claim), `too-easy` (no challenge), `other:<short phrase>`.

Write the file once you've reviewed all your weeks (you may write progressively). Then check it parses: `python3 -c "import json,sys; [json.loads(l) for l in open(sys.argv[1])]" <file>`. Your final message should be just: the file path, the number of weeks written, and a one-line note on any week you couldn't read.

Rules: do not edit anything in the repository, do not commit or push, and do not call any `mcp__hearthbot__` tools. Only write your output file.
