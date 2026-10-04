"""Assemble the nine weekly packets into five bookmarked print sets.

Uses the bundled runtime's pypdf, pdfplumber, and reportlab. Individual weekly
PDFs are built by their own build.sh scripts before this command is run.
"""
from io import BytesIO
from pathlib import Path
import json
import argparse

from pypdf import PdfReader, PdfWriter
import pdfplumber
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[3]
YEAR2 = ROOT / "lowell-math-circle-year-2"
OUT = YEAR2 / "combined"
QA = ROOT / "tmp" / "pdfs" / "fall-weeks-02-10"
WEEKS = {
    2: "Switches and lamps", 3: "Repeating secret machines", 4: "Around the ring",
    5: "Tower cities", 6: "Code-breaking with guarantees", 7: "Take-away games",
    8: "Rooks and piles", 9: "Bouncing paths", 10: "Bridges and delivery routes",
}
LEVELS = {
    "k-1": ("K-1", "Spoken instructions; matching, building, and small counts."),
    "grades-2-3": ("Grades 2-3", "Small counts and concrete arguments; adult reading help is welcome."),
    "grades-4-5": ("Grades 4-5", "Investigate all cases, prove an obstruction, or explain an optimum."),
    "extra-grades-6-7": ("Extra / grades 6-7", "Optional investigations; offer the next page by readiness."),
    "facilitator": ("Facilitator guides", "Preparation, pacing, hints, proofs, source notes, and extra-page solutions."),
}


def register_cover_fonts():
    # Embed TrueType fonts so printing does not depend on PDF-viewer substitutes.
    candidates = [
        (Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
         Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")),
        (Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
         Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")),
    ]
    for regular, bold in candidates:
        if regular.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont("CoverSans", str(regular)))
            pdfmetrics.registerFont(TTFont("CoverSansBold", str(bold)))
            return
    raise RuntimeError("Install Arial or DejaVu Sans to build embedded-font covers.")


def check_pdf(path, student=False):
    reader = PdfReader(path)
    assert not reader.is_encrypted, path
    for number, page in enumerate(reader.pages, 1):
        assert tuple(round(float(x)) for x in page.mediabox[2:]) == (612, 792), (path, number)
        text = page.extract_text() or ""
        assert len(text.strip()) > 80, (path, number, "empty or almost empty page")
        assert "\ufffd" not in text, (path, number, "replacement glyph")
        if student:
            assert "Problem " in text, (path, number, "missing numbered problem")
            for label in ("Name:", "Date:", "Go further:", "Build first.",
                          "Try it with objects."):
                assert label not in text, (path, number, "obsolete worksheet label", label)
    with pdfplumber.open(path) as doc:
        for number, page in enumerate(doc.pages, 1):
            for char in page.chars:
                if not char["text"].strip():
                    continue
                if not (24 <= char["x0"] <= char["x1"] <= 588 and
                        20 <= char["top"] <= char["bottom"] <= 775):
                    raise AssertionError((str(path), number, "text outside safe page", char))
    return len(reader.pages)


def cover(level, description, entries):
    stream = BytesIO()
    c = canvas.Canvas(stream, pagesize=letter, initialFontName="CoverSans")
    c.setFillGray(.12)
    c.setFont("CoverSansBold", 11)
    c.drawString(47, 741, "BELLINGHAM MATH CIRCLE  /  FALL YEAR A")
    c.setFont("CoverSansBold", 26)
    c.drawString(47, 692, "Weeks 2-10")
    c.setFont("CoverSansBold", 20)
    c.drawString(47, 659, level)
    c.setFont("CoverSans", 10.5)
    c.drawString(47, 629, description)
    lines = [
        "Grade bands are entry points. Begin with objects, then try to explain what happens.",
        "Give one page at a time. The packet is a menu, not a checklist for one hour.",
        "Keep facilitator solutions separate from student pages.",
    ]
    for i, text in enumerate(lines):
        c.drawString(47, 596-17*i, text)
    c.setFont("CoverSansBold", 11)
    c.drawString(47, 512, "Week and investigation")
    c.drawRightString(565, 512, "PDF pages")
    c.setStrokeGray(.65)
    c.line(47, 501, 565, 501)
    for index, row in enumerate(entries):
        y = 477-32*index
        c.setFont("CoverSans", 11)
        c.drawString(47, y, f'{row["week"]:02d}    {WEEKS[row["week"]]}')
        start, end = row["start_page"], row["end_page"]
        c.drawRightString(565, y, str(start) if start == end else f"{start}-{end}")
    c.setFont("CoverSans", 10)
    footer = [
        "Print US Letter, single-sided, at 100% / Actual Size.",
        "Page ranges above count this cover as page 1. Bookmarks open each week.",
        "Weekly footers retain their own page numbers and activity IDs for the use log.",
        "Unpiloted. Week 2 updated September 28; other core revisions September 27.",
    ]
    for i, text in enumerate(footer):
        c.drawString(47, 155-17*i, text)
    c.showPage()
    c.save()
    stream.seek(0)
    return stream


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--level', action='append', choices=list(LEVELS),
                        help='Rebuild selected set(s); default is all five.')
    args = parser.parse_args()
    register_cover_fonts()
    QA.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    manifest_path = QA / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if args.level and manifest_path.exists() else {}
    for suffix, (level, description) in LEVELS.items():
        if args.level and suffix not in args.level:
            continue
        entries = []
        next_page = 2
        for week in WEEKS:
            path = YEAR2 / f"week-{week:02d}" / f"week-{week:02d}-{suffix}.pdf"
            count = check_pdf(path, student=suffix != "facilitator")
            entries.append({"week": week, "file": str(path.relative_to(ROOT)),
                            "pages": count, "start_page": next_page,
                            "end_page": next_page+count-1})
            next_page += count
        writer = PdfWriter()
        writer.append(PdfReader(cover(level, description, entries)))
        for row in entries:
            writer.append(ROOT / row["file"], outline_item=f'Week {row["week"]}: {WEEKS[row["week"]]}')
        writer.add_metadata({"/Title": f"Bellingham Math Circle: Weeks 2-10 / {level}",
                             "/Author": "Bellingham Math Circle",
                             "/Subject": "Concrete investigations, explanations, and deeper mathematics"})
        destination = OUT / f"fall-weeks-02-10-{suffix}.pdf"
        with destination.open("wb") as output:
            writer.write(output)
        check_pdf(destination)
        manifest[suffix] = {"file": str(destination.relative_to(ROOT)), "pages": next_page-1,
                            "weeks": entries}
        print(f"Built {destination.name}: {next_page-1} pages")
    (QA / "manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")


if __name__ == "__main__":
    main()
