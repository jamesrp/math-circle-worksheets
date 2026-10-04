#!/usr/bin/env python3
"""Copy the source to a new directory and compare the standalone rebuild."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile
import pymupdf

parser = argparse.ArgumentParser()
parser.add_argument("pdf", type=Path)
parser.add_argument("report", type=Path)
args = parser.parse_args()
src = Path(__file__).resolve().parent
args.report.parent.mkdir(parents=True, exist_ok=True)
def compare(rebuilt_path):
    original = pymupdf.open(args.pdf)
    rebuilt = pymupdf.open(rebuilt_path)
    assert len(original) == len(rebuilt) == 12
    checks = []
    for i, (a, b) in enumerate(zip(original, rebuilt), 1):
        assert a.rect == b.rect
        assert a.get_text() == b.get_text()
        pa = a.get_pixmap(matrix=pymupdf.Matrix(1.2, 1.2), alpha=False)
        pb = b.get_pixmap(matrix=pymupdf.Matrix(1.2, 1.2), alpha=False)
        assert pa.samples == pb.samples
        checks.append({"page": i, "text_identical": True, "dimensions_identical": True,
                       "rendered_pixels_identical": True,
                       "pixel_sha256": hashlib.sha256(pa.samples).hexdigest()})
    return checks


with tempfile.TemporaryDirectory(prefix="clean-rebuild-", dir=args.report.parent) as tmp:
    root = Path(tmp)
    shutil.copytree(src, root / "copied" / "src")
    subprocess.run(["sh", str(root / "copied" / "src" / "build.sh"), str(root / "copied" / "output")], cwd=root, check=True)
    copy_checks = compare(root / "copied" / "output" / "students.pdf")
    with zipfile.ZipFile(root / "source.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(src.rglob("*")):
            if path.is_file():
                archive.write(path, Path("src") / path.relative_to(src))
    with zipfile.ZipFile(root / "source.zip") as archive:
        archive.extractall(root / "extracted")
    subprocess.run(["sh", str(root / "extracted" / "src" / "build.sh"), str(root / "extracted" / "output")], cwd=root, check=True)
    extracted_checks = compare(root / "extracted" / "output" / "students.pdf")
    args.report.write_text(json.dumps({"copied_source": copy_checks, "extracted_source_archive": extracted_checks}, indent=2) + "\n")
print("Clean copied-source and extracted-archive rebuilds: all 12 pages have identical text, dimensions and rendered pixels.")
