#!/usr/bin/env python3
"""Build a room plan's printable PDF from its Markdown.

    python3 plans/room-plans/build/build.py plans/room-plans/2026-11-11-bridges.md

Writes the PDF beside the Markdown (same name, .pdf). Needs pandoc and LibreOffice (soffice).
Pandoc makes HTML with style.css; the "The hour" section starts a new page so the timetable
prints whole; LibreOffice's web export makes the PDF (the November 4 plan's pipeline).
"""
import pathlib, re, shutil, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
md = pathlib.Path(sys.argv[1]).resolve()
with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    html = tmp / (md.stem + ".html")
    subprocess.run(["pandoc", "-s", str(md), "-f", "gfm", "-t", "html5",
                    "--metadata", "pagetitle=" + md.stem, "-o", str(html)], check=True)
    text = html.read_text()
    text = re.sub(r"<header[^>]*>.*?</header>", "", text, flags=re.S)
    text = re.sub(r"<style>.*?</style>", "", text, flags=re.S)
    text = text.replace("</head>", "<style>" + (HERE / "style.css").read_text() + "</style></head>")
    text = re.sub(r'<h2 id="the-hour">', '<h2 id="the-hour" style="page-break-before: always">', text)
    html.write_text(text)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf:writer_web_pdf_Export",
                    "--outdir", str(tmp), str(html)], check=True, capture_output=True)
    shutil.copy(tmp / (md.stem + ".pdf"), md.with_suffix(".pdf"))
print("wrote", md.with_suffix(".pdf"))
