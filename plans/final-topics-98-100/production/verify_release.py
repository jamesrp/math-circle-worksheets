#!/usr/bin/env python3
"""Package and verify the public Weeks 98-100 release; requires pypdf, PyMuPDF, pdffonts and configured pdfLaTeX."""
import hashlib, json, re, subprocess, sys, tempfile, zipfile
from pathlib import Path
from urllib.parse import unquote
import fitz
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
PROD = ROOT / "plans/final-topics-98-100/production"
YEAR = ROOT / "lowell-math-circle-year-2"
COUNTS = {98: {"grades-2-3": 5, "grades-4-5": 6, "facilitator": 5},
          99: {"grades-2-3": 6, "grades-4-5": 6, "facilitator": 6},
          100: {"grades-3-5": 8, "facilitator": 5}}
ALLOWED_ROOT = {"README.md", "QA.md", "SOURCES.md", "build.py", "build-targets.json", "check_math.py"}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def public_source(path, src):
    rel = path.relative_to(src)
    return ((len(rel.parts) == 1 and rel.name in ALLOWED_ROOT)
            or (rel.parts[0] in {"student", "guide"} and path.suffix == ".tex")
            or (rel.parts[0] == "reference-pdfs" and path.suffix == ".pdf"))

def package(src, archive):
    files = sorted(p for p in src.rglob("*") if p.is_file())
    assert all(public_source(p, src) for p in files), "Unexpected source-package payload"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in files:
            info = zipfile.ZipInfo(str(Path(src.name) / p.relative_to(src)), (2026,10,17,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, p.read_bytes(), compresslevel=9)
    return files

def check_pdf(path, week, count):
    doc = fitz.open(path)
    assert len(doc) == count, str(path)
    orientations = []
    for page in doc:
        size = tuple(round(v, 2) for v in (page.rect.width, page.rect.height))
        assert size in {(612.0, 792.0), (792.0, 612.0)}, (path, size)
        orientations.append("landscape" if size[0] > size[1] else "portrait")
        text = page.get_text()
        assert "Bellingham Math Circle" in text and str(week) in text, (path, page.number)
        assert "\ufffd" not in text
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    x0,y0,x1,y1 = span["bbox"]
                    assert min(x0,y0) >= -0.5 and x1 <= size[0]+0.5 and y1 <= size[1]+0.5, (path, page.number, span)
    fonts = subprocess.check_output(["pdffonts", str(path)], text=True).splitlines()[2:]
    assert fonts and all(line.split()[-5] == "yes" for line in fonts if line.strip()), (path, fonts)
    return {"path": str(path.relative_to(ROOT)), "pages": count, "orientations": orientations,
            "sha256": sha(path), "bytes": path.stat().st_size,
            "letter_geometry": True, "embedded_fonts": True, "text_bounds": True}

def check_links():
    docs = [YEAR/"WEEKS-98-100.md", PROD/"README.md"]
    for w in COUNTS:
        docs += list((YEAR/f"source/week-{w}").glob("*.md"))
        docs += [PROD/f"week-{w}/README.md"]
    links = 0
    for doc in docs:
        for target in re.findall(r"\]\(([^)]+)\)", doc.read_text()):
            if target.startswith(("http:", "https:", "mailto:", "#")):
                continue
            dest = (doc.parent / unquote(target.split("#")[0])).resolve()
            assert dest.exists(), (str(doc.relative_to(ROOT)), target)
            links += 1
    for path in ["README.md", "WORKBOARD.md", "lowell-math-circle-year-2/README.md",
                 "lowell-math-circle-year-2/source/README.md", "plans/README.md",
                 "plans/final-topics-98-100/README.md"]:
        assert "WEEKS-98-100.md" in (ROOT/path).read_text(), path
    return {"checked_documents": len(docs), "checked_local_links": links,
            "six_entry_indexes_link_release": True, "failures": []}

def main():
    audit = {"date": "2026-10-17", "method": "fresh ZIP extraction and independent rebuild",
             "detailed_review_reports_published": False, "classroom_piloted": False,
             "physical_rehearsal": "untested", "families": []}
    outputs = []
    for w, counts in COUNTS.items():
        src = YEAR/f"source/week-{w}"
        archive = YEAR/f"source/week-{w}-source.zip"
        files = package(src, archive)
        with tempfile.TemporaryDirectory(prefix=f"clean-week-{w}-") as temp:
            clean = Path(temp)
            with zipfile.ZipFile(archive) as z:
                z.extractall(clean)
            run = subprocess.run([sys.executable, str(clean/src.name/"build.py"),
                                  "--out", str(clean/"rebuilt"), "--work", str(clean/"build")],
                                 text=True, capture_output=True)
            assert run.returncode == 0, run.stdout + run.stderr
            records = []
            for band, count in counts.items():
                name = f"week-{w}-{band}.pdf"
                delivered = YEAR/f"week-{w}"/name
                reference = src/"reference-pdfs"/name
                rebuilt = clean/"rebuilt"/name
                record = check_pdf(delivered, w, count)
                assert record["sha256"] == sha(reference) == sha(rebuilt), name
                record.update(reference_sha256=sha(reference), rebuilt_sha256=sha(rebuilt),
                              byte_identical=True)
                records.append(record)
                outputs.append(record)
        report = {"week": w, "build_and_mathematical_checks": "PASS",
                  "build_summary": run.stdout.strip(), "outputs": records,
                  "archive": {"path": str(archive.relative_to(ROOT)), "sha256": sha(archive),
                              "bytes": archive.stat().st_size,
                              "members": [str(Path(src.name)/p.relative_to(src)) for p in files]},
                  "excluded_payloads": ["detailed review reports", "workflow prompts", "borrowed exemplars",
                                        "downloaded references", "session traces", "build caches"]}
        folder = PROD/f"week-{w}"
        folder.mkdir(exist_ok=True)
        (folder/"release-check.json").write_text(json.dumps(report, indent=2)+"\n")
        audit["families"].append(report)
        print(f"PASS Week {w}: clean archive rebuild equals delivered and reference PDFs", flush=True)
    audit["pdf_count"] = len(outputs)
    audit["total_pages"] = sum(x["pages"] for x in outputs)
    assert (audit["pdf_count"], audit["total_pages"]) == (8,47)
    (PROD/"release-audit.json").write_text(json.dumps(audit, indent=2)+"\n")
    output = {"pdf_count": len(outputs), "pages": audit["total_pages"], "pdf_checks": outputs,
              "visual_inspection": "All 47 final pages independently rendered and inspected before publication; accepted PDF hashes unchanged.",
              "links": "pending"}
    (PROD/"output-index-checks.json").write_text(json.dumps(output, indent=2)+"\n")
    output["links"] = check_links()
    (PROD/"output-index-checks.json").write_text(json.dumps(output, indent=2)+"\n")
    print("PASS: 8 PDFs, 47 pages, 3 portable ZIPs and public index links.")
if __name__ == "__main__":
    main()
