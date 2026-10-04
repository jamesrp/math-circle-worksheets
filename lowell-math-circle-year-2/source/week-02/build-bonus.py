#!/usr/bin/env python3
"""Build the optional Week 2 bonus packet and separate adult key (ReportLab).

Canonical geometry and puzzle states: plans/week-02-bonus-data.json.
Mathematical verification: plans/verify-week-02-bonus.py.
"""
import json
import math
from pathlib import Path

from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[3]
DATA = json.loads((ROOT / "plans/week-02-bonus-data.json").read_text())
OUT = ROOT / "lowell-math-circle-year-2/week-02"
W, H, M = 612, 792, 44
WIDTH = W - 2 * M


def fonts():
    for folder, regular, bold in [
        ("/System/Library/Fonts/Supplemental", "Arial.ttf", "Arial Bold.ttf"),
        ("/usr/share/fonts/truetype/dejavu", "DejaVuSans.ttf", "DejaVuSans-Bold.ttf"),
    ]:
        base = Path(folder)
        if (base / regular).exists():
            pdfmetrics.registerFont(TTFont("Bonus", str(base / regular)))
            pdfmetrics.registerFont(TTFont("BonusB", str(base / bold)))
            pdfmetrics.registerFontFamily("Bonus", normal="Bonus", bold="BonusB")
            return
    raise RuntimeError("Arial or DejaVu Sans required")


class Book:
    def __init__(self, filename, guide=False):
        self.guide = guide
        self.path = OUT / filename
        self.c = canvas.Canvas(str(self.path), pagesize=(W, H), invariant=1)
        title = "Facilitator notes" if guide else "Fast Finisher / Bonus Challenges"
        self.c.setTitle(f"Week 2 / Lamp lab / {title}")
        self.c.setAuthor("Bellingham Math Circle")
        self.c.setSubject("Optional lamp investigations; prepared September 30, 2026")
        self.page = 0

    def start(self, bookmark):
        if self.page:
            self.c.showPage()
        self.page += 1
        c = self.c
        c.setFillGray(.1)
        c.setFont("BonusB", 10.3)
        suffix = "Bonus challenges / Facilitator" if self.guide else "Bonus challenges"
        c.drawString(M, H - 39, f"Week 2 / Lamp lab / {suffix}")
        c.setStrokeGray(.55)
        c.setLineWidth(.6)
        c.line(M, 44, W - M, 44)
        c.setFont("Bonus", 8.5)
        c.setFillGray(.2)
        doc_id = "F02-BONUS-FAC-v1" if self.guide else DATA["student_id"]
        c.drawString(M, 29, f"Bellingham Math Circle / Week 2 / {doc_id}")
        c.drawRightString(W - M, 29, str(self.page))
        key = f"page-{self.page}"
        c.bookmarkPage(key)
        c.addOutlineEntry(bookmark, key)

    def para(self, text, top, x=M, width=WIDTH, size=None, leading=None):
        size = size or (10.7 if self.guide else 13.5)
        leading = leading or (14.3 if self.guide else 18)
        p = Paragraph(text, ParagraphStyle("body", fontName="Bonus", fontSize=size,
                                          leading=leading, textColor="#171717"))
        _, height = p.wrap(width, H)
        assert top + height <= 729, (self.page, text, top + height)
        p.drawOn(self.c, x, H - top - height)
        return top + height

    def label(self, text, x, top, size=11, centered=False):
        self.c.setFont("Bonus", size)
        self.c.setFillGray(.15)
        method = self.c.drawCentredString if centered else self.c.drawString
        method(x, H - top, text)

    def rule(self, top, x=M, width=WIDTH):
        self.c.setStrokeGray(.78)
        self.c.setLineWidth(.45)
        self.c.line(x, H - top, x + width, H - top)

    def arrow(self, cx, top, width=24):
        c = self.c
        y = H - top
        c.setStrokeGray(.22)
        c.setLineWidth(1.2)
        c.line(cx - width / 2, y, cx + width / 2, y)
        c.line(cx + width / 2 - 5, y + 3, cx + width / 2, y)
        c.line(cx + width / 2 - 5, y - 3, cx + width / 2, y)

    def star(self, x, y, radius=6):
        p = self.c.beginPath()
        for i in range(10):
            r = radius if i % 2 == 0 else radius * .44
            angle = math.pi / 2 + i * math.pi / 5
            px, py = x + r * math.cos(angle), y + r * math.sin(angle)
            (p.moveTo if i == 0 else p.lineTo)(px, py)
        p.close()
        self.c.setFillGray(.12)
        self.c.drawPath(p, fill=1, stroke=0)

    def graph(self, name, cx, top, width, height, on=(), radius=8.5,
              special=False, prices=False, highlight=None, labels=False,
              bridge_label=False):
        g = DATA["graphs"][name]
        if "cycle" in g:
            n = g["cycle"]
            xy = [(math.sin(2 * math.pi * i / n), math.cos(2 * math.pi * i / n))
                  for i in range(n)]
        else:
            xy = g["xy"]
        xs, ys = zip(*xy)
        dx, dy = max(xs) - min(xs), max(ys) - min(ys)
        pad = radius + (22 if prices else 7)
        scale = min((width - 2 * pad) / dx if dx else float("inf"),
                    (height - 2 * pad) / dy if dy else float("inf"))
        points = [(cx + (x - (min(xs) + max(xs)) / 2) * scale,
                   H - top - height / 2 + (y - (min(ys) + max(ys)) / 2) * scale)
                  for x, y in xy]
        assert top + height < 730
        assert all(math.dist(a, b) > 2 * radius + 3
                   for i, a in enumerate(points) for b in points[i + 1:])
        c = self.c
        for i, (a, b) in enumerate(g["edges"]):
            chosen = highlight is not None and i in highlight
            c.setStrokeGray(.05 if chosen else (.73 if highlight is not None else .2))
            c.setLineWidth(3.5 if chosen else 1.25)
            c.line(*points[a - 1], *points[b - 1])
        if prices:
            for i, (a, b) in enumerate(g["edges"]):
                x = (points[a - 1][0] + points[b - 1][0]) / 2
                y = (points[a - 1][1] + points[b - 1][1]) / 2
                offsets = [(0, 13), (15, 0), (0, -16), (-15, 0)]
                ox, oy = offsets[i]
                c.setFillGray(.1)
                c.setFont("BonusB", 13)
                c.drawCentredString(x + ox, y + oy - 4, str(g["costs"][i]))
        for i, (x, y) in enumerate(points, 1):
            c.setFillGray(1)
            c.setStrokeGray(.18)
            c.setLineWidth(1.25)
            c.circle(x, y, radius, stroke=1, fill=1)
            if i in on:
                c.setFillGray(.1)
                c.circle(x, y, radius * .41, stroke=0, fill=1)
            if labels:
                c.setFillGray(.15)
                c.setFont("Bonus", 9)
                c.drawCentredString(x, y + radius + 5, str(i))
            if special and i == g["special_lamp"]:
                self.star(x + radius + 11, y + radius + 3)
        if bridge_label:
            a, b = g["edges"][g["bridge_index"]]
            x = (points[a - 1][0] + points[b - 1][0]) / 2
            y = (points[a - 1][1] + points[b - 1][1]) / 2
            self.label("bridge", x, H - y + 16, size=9, centered=True)

    def finish(self, count):
        assert self.page == count
        self.c.save()
        print(f"Built {self.path}: {self.page} pages")


def students():
    b = Book("week-02-bonus-challenges.pdf")
    b.start("Problem 1: Do-nothing moves")
    b.para("Empty is OFF. A dot is ON. Pressing a line changes BOTH lamps at "
           "its ends: OFF becomes ON, and ON becomes OFF.", 65)
    b.para("<b>Problem 1:</b> Do-nothing moves", 138)
    b.para("Start all OFF. Choose at least one line. Press each chosen line once. "
           "Can you finish with every lamp OFF again?", 169)
    b.label("A.", M, 248)
    b.label("B.", 324, 248)
    b.graph("path4", 168, 264, 215, 108)
    b.graph("ring5", 435, 257, 170, 124)
    b.para("C. Find EVERY nonempty set of lines that changes nothing.", 409)
    b.graph("square_diagonal", 133, 451, 175, 175)
    b.para("What do all the answers have in common?", 658)
    b.rule(702)

    b.start("Problem 2: Bridge detective")
    b.para("<b>Problem 2:</b> Bridge detective", 65)
    b.para("For this problem, press each line at most once.", 96)
    b.para("Before solving each puzzle, must you press the bridge, or must you "
           "leave it alone? How can you know without solving the whole puzzle? "
           "Then solve to check your prediction.", 127)
    for case, top in zip(DATA["bridge_cases"], [224, 477]):
        b.label(case["label"] + ".", M, top)
        for cx, state, caption in [(164, case["start"], "Start"),
                                   (448, case["target"], "Target")]:
            b.label(caption, cx, top + 22, centered=True)
            b.graph("bridge", cx, top + 38, 231, 117, state, radius=8,
                    bridge_label=True)
        b.arrow(306, top + 96)
        b.rule(top + 199)
        b.rule(top + 229)

    b.start("Problem 3: One solo switch")
    b.para("<b>Problem 3:</b> One solo switch", 65)
    b.para("NEW RULE - this problem only: The lamp with a star has a special "
           "button. The button changes ONLY its own lamp. Lines still change "
           "the two lamps at their ends.", 96)
    b.para("Start all OFF each time.", 184)
    tasks = [
        "A. Make exactly the special lamp ON.",
        "B. Make exactly a neighboring lamp ON.",
        "C. Make exactly a lamp far away ON.",
        "D. Make any target you want.",
    ]
    for i, task in enumerate(tasks):
        row, col = divmod(i, 2)
        x = M + col * 280
        top = 229 + row * 214
        b.para(task, top, x=x, width=244)
        b.graph("ring6", x + 116, top + 48, 156, 156, radius=10, special=True)
    b.para("With the special button, can you make EVERY target picture?", 689)

    b.start("Problem 4: Cheapest, not fewest")
    b.para("<b>Problem 4:</b> Cheapest, not fewest", 65)
    b.para("Start all OFF. Make the target picture.\n"
           "<br/>A press costs the number written on its line.", 96)
    for cx, state, caption in [(166, [], "Start"), (446, DATA["priced_target"], "Target")]:
        b.label(caption, cx, 174, centered=True)
        b.graph("priced_square", cx, 187, 206, 206, state, radius=10, prices=True)
    b.arrow(306, 290)
    for text, top, line in [
        ("a. What solution uses the FEWEST presses?", 421, 488),
        ("b. What solution costs the LEAST?", 523, 590),
        ("c. Why are the answers different?", 625, 702),
    ]:
        b.para(text, top)
        b.rule(line)
    b.finish(4)


def guide():
    b = Book("week-02-bonus-facilitator.pdf", guide=True)
    b.start("Use at the table; Problems 1 and 2")
    top = b.para("<b>Fast Finisher / Bonus Challenges - adult key</b>", 65,
                 size=14, leading=18)
    top = b.para("Prepared September 30, 2026; <b>unpiloted reserve</b>. Student pages "
                 "1-4 contain Problems 1-4. Offer one page when a child wants another "
                 "investigation; these are choices, not a speed test.", top + 9)
    top = b.para("<b>Entry and setup.</b> Know the pair-flip rule and track several moves. "
                 "Adults may read or scribe. Problems 1-3 need only small counts and "
                 "picture matching; Problem 4 needs counting presses and adding costs "
                 "up to 5. Use pencils/erasers, blank paper or the existing whiteboards; "
                 "two-sided counters are optional. Print US Letter at Actual Size.", top + 8)
    top = b.para("<b>Launch and timing.</b> Keep the usual common launch: let children try "
                 "the materials, then show one line changing both lamps. At the bonus "
                 "table say, 'Choose a question and show what one legal press does.' "
                 "For Problem 3, demonstrate the special button separately. Allow about "
                 "10-15 minutes for 1 or 2, 10-20 for 3, and 5-10 for 4 within the "
                 "existing hour. Staying with one problem is fine.", top + 8)
    top = b.para("<b>1. Do-nothing moves.</b> A is impossible. B works by pressing the "
                 "whole ring. C has exactly three answers, shown in bold below: either "
                 "triangle, or the outside square. No other nonempty set works.", top + 13)
    diagram_top = top + 9
    for cx, chosen in zip([135, 306, 477], DATA["do_nothing"][2]["expected_nonempty_sets"]):
        b.graph("square_diagonal", cx, diagram_top, 114, 99, highlight=chosen, radius=6)
    top = b.para("<b>Reasoning.</b> Each lamp must be changed an even number of times. "
                 "On A, the endpoint forces its only line to be unused; continue inward. "
                 "On C, an unused diagonal forces either no outside lines or all four. "
                 "A used diagonal forces one of the two outside routes joining its ends. "
                 "The successful sets all close up, touching each used lamp twice.", diagram_top + 108)
    top = b.para("<b>If needed:</b> 'What happened to one lamp after all your presses?' "
                 "<b>Extension:</b> add another line to a drawing and search for new "
                 "do-nothing sets. Two closed loops meeting at a lamp show that a lamp "
                 "may be changed four times too.", top + 7)
    top = b.para("<b>2. Bridge detective.</b> A: <b>press</b> the bridge. Press the far-left "
                 "vertical line and the bridge to reach the target. B: <b>leave it alone</b>. "
                 "Press the far-left vertical line and the upper sloping line of the "
                 "right triangle. Each is a two-press solution.", top + 13)
    top = b.para("<b>Reasoning.</b> In A, all three lamps on the left must change, and "
                 "only the bridge-end lamp on the right must change. In B, two lamps "
                 "on each side must change. A line inside one side changes two lamps "
                 "there; only the bridge changes just one. Thus odd change-counts force "
                 "the bridge and even change-counts forbid it. The at-most-once rule "
                 "makes this a yes/no choice; with repeats, it would mean odd/even "
                 "numbers of bridge presses.", top + 7)
    b.para("<b>If needed:</b> 'Which lamps differ between the two pictures?' "
           "<b>Extension:</b> invent a new pair of pictures with the same bridge "
           "prediction. Use changed lamps, not just the lamps ON in the target.", top + 7)

    b.start("Problems 3 and 4; source and use notes")
    top = b.para("<b>3. One solo switch.</b> A: press the special button. B: press the "
                 "button and a line to a neighboring lamp. C: press the button and "
                 "the three consecutive lines leading to the opposite lamp. Every "
                 "intermediate lamp changes twice, so only the far lamp remains ON. "
                 "Either way around works; other choices of a far lamp also count.", 65)
    top = b.para("<b>D and the final question: yes, every target is possible.</b> For "
                 "any lamp other than the special one, press the button and every "
                 "line along a route from the special lamp to it. The special lamp "
                 "and all lamps in between change twice. Only the chosen lamp changes "
                 "once. For the special lamp, use the button alone. Repeat for each "
                 "desired ON lamp. Overlapping routes cause no problem: two identical "
                 "presses cancel. An all-OFF target needs no presses.", top + 8)
    top = b.para("Without the button, only even numbers of ON lamps could be made "
                 "from all OFF. Now the odd targets work too. The six-lamp ring has "
                 "64 target pictures, all reachable. The same route argument works "
                 "whenever every lamp can be reached from the special lamp along lines.", top + 8)
    top = b.para("<b>If needed:</b> let the child light the special lamp, then ask how "
                 "to move that light one place. <b>Extension:</b> move the special "
                 "button elsewhere, or try a drawing with a separate piece. One "
                 "button cannot remove the restriction on an unreachable piece.", top + 8)
    top = b.para("<b>4. Cheapest, not fewest.</b> a: the top line, <b>1 press, cost 5</b>. "
                 "b: the other three lines, <b>3 presses, total cost 3</b>. c: a press "
                 "can have a different price from another press; taking more cheap "
                 "steps can cost less than one expensive step.", top + 15)
    diagram_top = top + 8
    for cx, chosen in [(190, [0]), (422, [1, 2, 3])]:
        b.graph("priced_square", cx, diagram_top, 132, 132, prices=True,
                highlight=chosen, radius=6)
    top = b.para("<b>Why these are best.</b> Zero presses cannot change the start, so "
                 "the one-press solution is shortest. If the top line is omitted, the "
                 "two target lamps force the side lines; the two lower lamps then "
                 "force the bottom line. If the top line is used, its endpoints force "
                 "both side lines to be unused, and then the bottom line must be unused "
                 "too. These are the only two sets of lines. Repeating a line "
                 "twice changes nothing and increases the cost, so repetitions cannot "
                 "produce a cheaper solution.", diagram_top + 143)
    top = b.para("<b>If needed:</b> 'Can you avoid the line priced 5?' "
                 "<b>Extension:</b> change its price to 3, then 2. At 3 both routes "
                 "cost the same; at 2 the direct line is cheapest.", top + 8)
    top = b.para("<b>Sources and status.</b> The four variants follow the organizer's "
                 "September 30 brief. Visual format follows the two approved Week 2 "
                 "catalogs. Earlier related work: Lowell Fall 2025, Handout 9, Problem "
                 "9.1 (divisor-based door switching). Format evidence: Natasha "
                 "Rozhkovskaya, <i>Math Circles for Elementary School Students</i>, "
                 "'Introduction: Berkeley 2009' (adult help), Lesson 6, 'At the lesson,' "
                 "item 4 (reported response to concrete geometry). These are teaching "
                 "references, not sources for the new puzzle instances.", top + 13, size=9.7, leading=12.6)
    b.para("All finite instances were exhaustively checked. Record the exact bonus "
           "problem, child attempts, discoveries and explanations only after use. "
           "The layouts and pacing remain unpiloted. Detailed data, proofs and "
           "rebuild instructions: plans/week-02-bonus.md.", top + 7, size=9.7, leading=12.6)
    b.finish(2)


def main():
    fonts()
    OUT.mkdir(parents=True, exist_ok=True)
    students()
    guide()


if __name__ == "__main__":
    main()
