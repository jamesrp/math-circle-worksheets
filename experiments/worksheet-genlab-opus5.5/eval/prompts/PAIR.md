You are advising the organizer of an elementary-school math circle. Two candidate worksheet packets, X and Y, were written from the same activity outline for the same one-hour session. He will take one of them to class, and he will have only about fifteen minutes per band to edit it first. For each band, and overall, decide which packet he should take.

Judge what will happen in the room: whether the mathematics is real and well developed, whether children of that band will be productively busy for the whole working time, whether the tasks are clear and concrete enough that children can work without constantly asking what to do, whether the level fits, whether the diagrams and workspace are usable, and whether the page reads like an experienced human leader wrote it (nothing decorative, cutesy, or filler, no hints that give the thinking away). Check the mathematics: a wrong or broken problem is a serious defect. Do not prefer a packet for being longer or more polished unless that actually serves the children. The order in which the packets are presented means nothing.

{{STANDARD}}

=== Activity outline both packets were written from ===

{{OUTLINE}}

=== Session context ===

{{CONTEXT}}

=== The packets ===

Packet X: {{BUNDLE_X}}
Packet Y: {{BUNDLE_Y}}
Inside each folder, each band has a folder (k-1, grades-2-3, grades-4-5) containing page images page-01.png, page-02.png, ... and text.txt. Read every page image of both packets with the Read tool and read each text.txt. The images are rendered so that diagrams are legible; crop or zoom only when you cannot verify something you need to check. Read nothing else on this machine.

=== How to work ===

For each band in turn, read both versions completely, work their central problems, and list the main strengths and weaknesses of each before deciding. Then decide the band: X, Y, or tie (use tie only when you would honestly be equally happy with either). Give a strength of 1 (slight preference), 2 (clear preference), or 3 (strong preference; the other would cause real problems in class). Then make an overall decision for the whole packet the same way.

=== Output ===

Write a single JSON file to {{OUT}} with exactly this structure (use the Write tool):

{
  "x": "{{PID_X}}",
  "y": "{{PID_Y}}",
  "bands": {
    "k-1": {"x_notes": "<main strengths and weaknesses of X>", "y_notes": "<same for Y>", "winner": "<X|Y|tie>", "strength": <1|2|3 or 0 for tie>, "reason": "<one or two sentences>"},
    "grades-2-3": { same fields },
    "grades-4-5": { same fields }
  },
  "overall": {"winner": "<X|Y|tie>", "strength": <1|2|3 or 0 for tie>, "reason": "<two or three sentences>"}
}

Make sure the file is valid JSON. Then reply with only the word "done".
