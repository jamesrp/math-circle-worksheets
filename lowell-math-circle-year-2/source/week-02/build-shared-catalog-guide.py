#!/usr/bin/env python3
"""Build the adult guide for the compact Week 2 catalog (Problems 1-10).

Writes lowell-math-circle-year-2/week-02/week-02-shared-catalog-facilitator.pdf
(or the path given as the first argument). The answer lists are read from
plans/week-02-catalog-kit-data.json, which plans/verify-week-02-catalog-kit.py
replays move by move; the graphs come from plans/week-02-shared-data.json.
"""
from pathlib import Path
import importlib.util
import json
import sys

from reportlab import rl_config
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Flowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer

rl_config.invariant = 1
SOURCE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("shared_explore", SOURCE / "build-shared-explore.py")
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)

ROOT = shared.ROOT
GRAPHS = shared.DATA["graphs"]
KIT = json.loads((ROOT / "plans/week-02-catalog-kit-data.json").read_text())
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else \
    ROOT / "lowell-math-circle-year-2/week-02/week-02-shared-catalog-facilitator.pdf"
W, H = 612, 792
LEFT = 50
ID = "F02-S-CAT-FAC-v1"

shared.fonts()
BODY = ParagraphStyle("body", fontName="Aux", fontSize=10.2, leading=13.6, spaceAfter=5.5, textColor="#161616")
SMALL = ParagraphStyle("small", parent=BODY, fontSize=9.2, leading=12.2, spaceAfter=4)
TITLE = ParagraphStyle("title", parent=BODY, fontName="AuxB", fontSize=18, leading=22, spaceAfter=4)
H2 = ParagraphStyle("h2", parent=BODY, fontName="AuxB", fontSize=12.2, leading=15.5, spaceBefore=7, spaceAfter=4,
                    keepWithNext=True)
ANS = ParagraphStyle("ans", parent=BODY, leftIndent=12, firstLineIndent=-12, spaceAfter=4)

NAMES = {"square": "square", "ring6": "six-ring", "tree8": "tree", "grid9": "3 × 3 grid", "islands8": "islands"}


def lamps(s):
    return "{" + ", ".join(map(str, s)) + "}"


def moves(presses):
    return ", ".join(f"{a}-{b}" for a, b in presses)


class Keys(Flowable):
    """Small numbered copies of the five boards, in the catalog's orientation."""

    def __init__(self, width):
        super().__init__()
        self.width = width
        self.height = 112

    def draw(self):
        c = self.canv
        slots = [("square", 70, 1.0), ("ring6", 70, 1.0), ("tree8", 120, 1.0), ("grid9", 70, 1.0),
                 ("islands8", 110, 1.0)]
        total = sum(w for _, w, _ in slots)
        gap = (self.width - total) / (len(slots) - 1)
        x = 0
        for name, w, _ in slots:
            g = GRAPHS[name]
            xs = [p[0] for p in g["xy"]]
            ys = [p[1] for p in g["xy"]]
            r = 7.5
            sc = min((w - 2 * r) / max(max(xs) - min(xs), 1e-9), (80 - 2 * r) / (max(ys) - min(ys)))
            cx = x + w / 2
            cy = 20 + 80 / 2
            pts = [(cx + (a - (min(xs) + max(xs)) / 2) * sc, cy + (b - (min(ys) + max(ys)) / 2) * sc)
                   for a, b in g["xy"]]
            c.setStrokeGray(.25)
            c.setLineWidth(1)
            for a, b in g["edges"]:
                c.line(*pts[a - 1], *pts[b - 1])
            for i, (px, py) in enumerate(pts, 1):
                c.setFillGray(1)
                c.setStrokeGray(.25)
                c.circle(px, py, r, fill=1, stroke=1)
                c.setFillGray(0)
                c.setFont("Aux", 8)
                c.drawCentredString(px, py - 2.8, str(i))
            c.setFont("AuxB", 8.5)
            c.drawCentredString(cx, 2, NAMES[name])
            x += w + gap


def decorate(c, doc):
    c.saveState()
    c.setFont("AuxB", 9.5)
    c.setFillGray(.12)
    c.drawString(LEFT, H - 36, "Week 2 / Lamp lab / Adult guide to the compact catalog")
    c.setStrokeGray(.55)
    c.setLineWidth(.6)
    c.line(LEFT, H - 43, W - LEFT, H - 43)
    c.line(LEFT, 44, W - LEFT, 44)
    c.setFont("Aux", 8.5)
    c.setFillGray(.25)
    c.drawString(LEFT, 30, f"Bellingham Math Circle / Week 2 / {ID} / unpiloted")
    c.drawRightString(W - LEFT, 30, str(doc.page))
    c.restoreState()


def P(text, style=BODY):
    return Paragraph(text, style)


def answers():
    out = []
    probs = {p["catalog"]: p for p in KIT["problems"]}
    head = {
        1: "square, all OFF to start",
        2: "six-ring, lamp 1 ON to start",
        3: "six-ring, lamp 1 ON to start and to finish",
        4: "tree, lamp 1 ON to start",
        5: "tree, all OFF to start",
        6: "six-ring, all OFF to start",
        7: "3 × 3 grid, all OFF to start",
    }
    for n in range(1, 8):
        p = probs[n]
        items = ". ".join(f"{lamps(a['target'])}: {moves(a['presses'])}" for a in p["answers"])
        extra = ""
        if n == 2:
            extra = " Going the other way round also works."
        if n == 3:
            extra = (" One light walks round the ring and comes home; detours are fine. Read the one-light rule "
                     "aloud (see above).")
        if n == 4:
            extra = " Backtracking is legal."
        if n == 5:
            extra = (" These are the presses of the trip to 8 in Problem 4: from all OFF the starting lamp lights "
                     "too, and the middle lamps flip twice. On a tree this is the only set of lines that works.")
        if n == 6:
            extra = " The ring has a loop, so other sets work too: pressing every line of the ring changes nothing."
        if n == 7:
            extra = " Pair the target lamps and join each pair by a path."
        out.append(P(f"<b>Problem {n}</b> ({head[n]}). {items}.{extra}", ANS))
    p9 = probs[9]["answers"][0]
    out.append(P("<b>Problem 8</b> (islands, lamp 1 ON to lamp 5 ON). Impossible. Every press changes two lamps "
                 "on one island, so the left island's number of ON lamps stays odd: its one light can never go "
                 "out. Accept that reason in any words, or a convincing run of failed tries for younger children, "
                 "and keep the search short.", ANS))
    out.append(P(f"<b>Problem 9</b> (the same start and target, with one bridge). Every one of the 16 possible "
                 f"bridges works. With bridge {p9['bridge'][0]}-{p9['bridge'][1]}: {moves(p9['presses'])}. Each "
                 "child's bridge needs its own route: walk the light to the bridge, across, and on to 5. Draw the "
                 "bridge on the islands board. In the catalog the start and target pictures sit closer together "
                 "than the two islands, so a child drawing there may join start to target instead.", ANS))
    out.append(P("<b>Problem 10</b> (invented puzzles). See the test above. A puzzle made by pressing lines from "
                 "the start can always be undone by pressing the same lines again; a target drawn freehand may "
                 "be impossible.", ANS))
    return out


def build():
    doc = SimpleDocTemplate(str(OUT), pagesize=(W, H), leftMargin=LEFT, rightMargin=LEFT, topMargin=58,
                            bottomMargin=56, title="Week 2 / Lamp lab / Adult guide to the compact catalog",
                            author="Bellingham Math Circle")
    width = W - 2 * LEFT
    s = []
    s.append(P("Lamp lab: adult guide to the compact catalog", TITLE))
    s.append(P("For week-02-shared-catalog.pdf (F02-S-CAT-v2, Problems 1–10) with the boards and counters in "
               "week-02-shared-catalog-boards.pdf. Unpiloted. Every answer below is replayed by "
               "plans/verify-week-02-catalog-kit.py.", SMALL))

    s.append(P("Mathematical overview", H2))
    s.append(P("<b>The move.</b> Pressing a line flips both lamps at its ends, OFF to ON or ON to OFF. Pressing "
               "the same line again undoes it, and the order of presses does not matter. So any run of presses "
               "does what the set of lines pressed an odd number of times does, and a puzzle asks for a set of "
               "lines that touches each lamp to be changed an odd number of times and every other lamp an even "
               "number of times. The lamps to be changed are the ones that differ between start and target."))
    s.append(P("<b>Theorem.</b> A target can be made from a start exactly when every island (connected piece "
               "of the board) has an even number of lamps that differ between start and target."))
    s.append(P("<b>Proof.</b> An odd island is impossible because a press changes two lamps of one island, "
               "so the number of ON lamps on each island changes by 0 or 2 and stays odd or even for ever (the "
               "invariant). Every even case works by path pairing: on one island, pair up the lamps to be changed "
               "and press every line along a path joining each pair. The two ends flip once; each lamp inside "
               "the path flips twice, which is no change. For adults: states are vectors over the field with "
               "two elements, a press adds the two end lamps, and the reachable changes are exactly the vectors "
               "with an even sum on every island."))
    s.append(P("<b>A walking light</b> is the special case children meet first: with one lamp ON, pressing the "
               "lines of a path from it moves the light to the path's far end (Problems 2–4). From all OFF the "
               "same presses light both ends (Problem 5)."))
    s.append(P("<b>Assumptions and limits.</b> Both lamps flip on every press. A child who changes one lamp "
               "breaks the invariant without noticing, which is what happened when the rule lived only on paper; "
               "hence counters and a partner who flips both. Solutions are not unique on a board with a loop "
               "(square, ring, grid), since pressing every line of a loop changes nothing; on the tree a "
               "reachable target has exactly one set of lines. Shortest solutions belong to the upper catalog."))
    s.append(P("<b>What children are meant to find.</b> Experiments: Problems 1–7, where every target can be made "
               "and a press is undone by pressing again. Conjecture: Problem 8, after some tries, “it can't be "
               "done.” Explanation: the left island starts with one light and every press changes two of its "
               "lamps, so that light can never go out. Problem 9 tests the explanation, since any bridge makes the "
               "trip possible, and Problem 10 makes children the puzzle makers."))
    s.append(P("<b>Band map.</b> K–1: Problems 1–4 and 6 with counters, the adult reading each prompt; Problem 8 "
               "as a short “can you?” Grades 2–3: all ten, with Problems 8–10 the core. Grades 4–5: the upper "
               "catalog (week-02-shared-catalog-upper.pdf and plans/week-02-catalog-upper.md), with Problems 8–9 "
               "here as an optional five-minute start."))

    s.append(P("Materials and preparation", H2))
    s.append(P("<b>Catalog:</b> one per child (4 pages). Its small pictures are the start and target cards. "
               "<b>Boards:</b> sheets 1–3 of week-02-shared-catalog-boards.pdf on copy paper, one set per pair: "
               "K–1 2, grades 2–3 2, grades 4–5 1 and one for the launch, 18 sheets. <b>Counters:</b> sheet 4 on "
               "card stock, one sheet cut into six sets of 11 with a paper trimmer. Dot up is ON. Two-colour "
               "counters already on hand also work; choose one colour for ON. <b>Also:</b> pencils and erasers "
               "for the Problem 9 bridge and scrap paper for Problem 10. <b>Preparation:</b> about 20 minutes. The "
               "boards and counters are digitally checked but physically unrehearsed: run the launch once on a "
               "board before class."))

    s.append(P("Launch together (about 5 minutes)", H2))
    s.append(P("Gather everyone at the adults' square board, all counters blank up. (1) “Each counter is a lamp. "
               "Dot up is ON.” Let children turn a few over, then set all OFF again. (2) <b>Press:</b> one child "
               "points to a line and a partner flips both counters at its ends; two lamps are ON. (3) <b>Press "
               "again:</b> point to the same line and flip both again; all OFF. Pressing twice undoes. (4) <b>One "
               "target:</b> show Problem 1's first pair, start all OFF and target top and right ON, and ask which "
               "press makes it. Then hand out catalogs and boards. Pointer and flipper swap after each press; a "
               "third child checks that both counters flipped. Laying out a start picture is setup, not a press."))

    s.append(P("The one-light rule", H2))
    s.append(P("The catalog dropped “Keep exactly ONE lamp ON” from Problems 2–4. Problems 2 and 4 stand as "
               "printed: any route counts, and the answers below keep one light anyway. Problem 3 needs the rule: "
               "“the light” means one light, and without the rule the tour can be done by lighting lamps and "
               "undoing them (from lamp 1: 2-3, 4-5, 6-1, 6-1, 4-5, 2-3 lights every lamp at some point and ends "
               "with lamp 1 alone). When you read Problem 3 aloud, add: “Keep exactly one lamp ON after every "
               "press.”"))

    s.append(P("Testing an invented puzzle (Problem 10)", H2))
    s.append(P("On each island, count the lamps that differ between the start and the target. If every count is "
               "even, the puzzle can be made; if any count is odd, it cannot. The old shared guide promised that "
               "“reversing the moves always succeeds.” That holds only for a puzzle made by pressing lines from "
               "the start. A drawn target can be impossible: on the square, all OFF to one lamp ON; on the "
               "islands, all OFF to one lamp ON on each island, although two lamps change in all. Ask the maker "
               "to make the target by presses first, or to apply the count."))

    s.append(P("Answers", H2))
    s.append(P("Lamp numbers follow these keys; the children's boards are unnumbered. “1-2, 2-3” means press "
               "line 1-2, then line 2-3, and {1, 3} names the target with lamps 1 and 3 ON. Reset to the printed "
               "start for each pair of pictures. Any working list counts; these are examples.", SMALL))
    s.append(Keys(width))
    s.append(Spacer(1, 6))
    s.extend(answers())

    s.append(P("Timing and hints", H2))
    s.append(P("A first visit: launch 5 minutes; Problems 1–3, 15; Problems 4–7, 15; Problems 8–9, 10; "
               "Problem 10 as time allows. Stop a route after a satisfying attempt; finishing the catalog is not "
               "the goal. Hints, only when needed: “Which lamps have to change?”; “Find a path from one lamp you "
               "want ON to the other.”; for Problem 8, “Count the lights on the left island after each press.” "
               "For a pair that finishes early: “Make a target your partner cannot make, and explain why.”"))

    s.append(P("Sources and status", H2))
    s.append(P("Answers and trio roles come from the archived shared guide, F02-S-FAC-v1 "
               "(archive-before-deslopping/, old Problems 2 and 5–13), renumbered. The reversal caveat and the "
               "one-light decision answer the math check, plans/review/week-02-math.md, items 4 and 5. Lowell "
               "year-1 Handout 9, Problem 9.1, toggles doors, a related earlier activity. Adult reading: sets of "
               "lines with prescribed odd lamps are T-joins (Cornuéjols, Combinatorial Optimization: Packing "
               "and Covering, ch. 2). Status: unpiloted. A paper lamp session went poorly when the rule lived "
               "only on paper (worksheet-workflow/context.md, October 3, 2026); the counters and partner presses "
               "respond to that and are untested.", SMALL))
    doc.build(s, onFirstPage=decorate, onLaterPages=decorate)
    print(f"Built {OUT}")


if __name__ == "__main__":
    build()
