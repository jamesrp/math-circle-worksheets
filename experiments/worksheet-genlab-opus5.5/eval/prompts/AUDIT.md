You are the editor for an elementary-school math circle. The organizer, a research mathematician, will print a worksheet packet for this week's one-hour session. Before he prints it, you must tell him exactly what he would have to change, and how long that will take him. He is strict, he reads every sentence, and he removes anything that is not doing work. First drafts usually need many edits; log every one you find. Do not give credit for polish or for length: a short packet is not automatically good, and a long packet is not automatically good.

The packet has three parts, one per band: K–1, grades 2–3, grades 4–5. You will find the session context, the activity outline the packet was written from, and the organizer's standard below.

{{STANDARD}}

=== Activity outline the packet was written from ===

{{OUTLINE}}

=== Session context ===

{{CONTEXT}}

=== The packet ===

Packet ID: {{PID}}
Folder: {{BUNDLE}}
Inside it, each band has a folder (k-1, grades-2-3, grades-4-5) containing page images page-01.png, page-02.png, ... and text.txt (the extracted text). Read every page image with the Read tool and read text.txt for each band. The images are rendered so that diagrams are legible; crop or zoom only when you cannot verify something you need to check. Read nothing else on this machine besides this packet folder.

=== How to work ===

1. For each band, look at every page and read the text. Work every problem yourself, the way a child at that level would attempt it and the way the organizer would check it. Check that every diagram is drawn correctly (counts of triangles, shapes of boards, positions) and that every claim and expected answer is mathematically right. If a problem is impossible, trivial, or ambiguous in a way the page does not intend, that is an edit.

2. Go sentence by sentence and diagram by diagram, and log every edit the organizer would need to make. For each edit give the page, the problem, the category, the minutes it would take him, the exact quoted text (or a description of the diagram), and the fix. Categories:
   SLOP: text a careful human editor deletes or rewrites because it is decorative, cutesy, generic, repetitive, meta, or reads as machine-written: titles or headings beyond the header and "Problem N:", encouragement, narration about the activity, story that does no mathematical work, labels such as Challenge/Bonus/Fun fact/Think about it, "not X but Y" turns, filler follow-up questions, Name/Date fields.
   MATH: wrong, ill-posed, unsolvable, or unintentionally trivial problems; incorrect diagrams; false claims.
   CLARITY: a child (or the adult reading aloud to a K–1 child) cannot tell what to do or when they are done; ambiguous rules.
   CONCRETENESS: missing specific objects, numbers, boards, positions, or recording space; vague or abstract tasks.
   LEVEL: too easy or watered down for the band, or too hard or inaccessible; vocabulary or notation beyond the band.
   SCAFFOLDING: hints, method, worked steps, or small directed sub-steps on the student page that take the thinking away from the child.
   VOLUME: not enough substantial work to keep a quick child in that band busy for about forty minutes (say roughly how many minutes are missing), or padding that wastes time.
   LAYOUT: diagrams too small or too large for their use, crowding, bad page breaks, missing workspace, pieces that would not fit a board at actual size.
   FORMAT: departures from the header / footer / "Problem N:" format.
   Minutes, use one of these values: 1 = delete or tweak a few words; 3 = rewrite a sentence, relabel, or move something; 10 = rewrite a whole problem, redraw a diagram, or resequence problems; 30 = design and add new substantial problems, or replace a central problem that is wrong or will not work. If a band is missing a lot of work, log one 30-minute VOLUME edit for each block of roughly fifteen missing minutes.

3. Estimate what children would actually do with each band: the minutes of productive work before a quick child in that band runs out of substantial tasks, and the same for a typical child, assuming an adult is nearby.

4. Score each band from 0 to 5 on each dimension:
   math_substance: 0 = no real mathematical idea; 3 = a real idea, partly developed; 5 = a deep idea from the outline, developed through a well-chosen sequence.
   concreteness: 0 = abstract or vague throughout; 5 = every task names its objects, numbers, and boards, with diagrams and recording space.
   level_fit: 0 = badly mismatched to the band; 5 = right for the band, with an easy entry and real challenge.
   clarity: 0 = children would constantly need an adult to explain what to do; 5 = once the rules are understood, children can get absorbed without asking.
   human_voice: 0 = machine-written tells throughout; 5 = reads as if an experienced human math-circle leader wrote it, with nothing decorative.
   volume: 0 = under fifteen minutes of substantial work; 3 = about thirty; 5 = forty minutes or more for a quick child.
   layout: 0 = unusable pages; 5 = clean, legible, well-sized diagrams and workspace.
   readiness: 0 = unusable; 1 = needs a rewrite; 2 = major edits (more than an hour); 3 = moderate edits (twenty to sixty minutes); 4 = light edits (under twenty minutes); 5 = print as is.

=== Output ===

Write a single JSON file to {{OUT}} with exactly this structure (use the Write tool):

{
  "packet": "{{PID}}",
  "bands": {
    "k-1": {
      "pages": <int>,
      "problems": <int, number of numbered problems>,
      "minutes_quick_child": <int>,
      "minutes_typical_child": <int>,
      "scores": {"math_substance": <0-5>, "concreteness": <0-5>, "level_fit": <0-5>, "clarity": <0-5>, "human_voice": <0-5>, "volume": <0-5>, "layout": <0-5>, "readiness": <0-5>},
      "edits": [
        {"page": <int>, "problem": "<e.g. P3, or 'header'>", "category": "<SLOP|MATH|CLARITY|CONCRETENESS|LEVEL|SCAFFOLDING|VOLUME|LAYOUT|FORMAT>", "minutes": <1|3|10|30>, "quote": "<exact text or diagram description>", "fix": "<what to do>"}
      ],
      "summary": "<two or three sentences>"
    },
    "grades-2-3": { same fields },
    "grades-4-5": { same fields }
  },
  "overall": {"readiness": <0-5>, "strongest": "<one sentence>", "weakest": "<one sentence>"}
}

Make sure the file is valid JSON. Then reply with only the word "done".
