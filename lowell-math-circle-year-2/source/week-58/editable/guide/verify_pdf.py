#!/usr/bin/env python3
"""Render all guide pages and compare copied and ZIP-extracted rebuilds."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZipFile
import pymupdf as fitz


def fingerprint(pdf):
    with fitz.open(pdf) as doc:
        return [{"text": p.get_text(), "dimensions": list(p.rect), "rotation": p.rotation,
                 "pixels": hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False).samples).hexdigest()}
                for p in doc]


def main():
    src = Path(__file__).resolve().parent
    out = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else src.parent
    pdf = out / "facilitator.pdf"
    render = out / "guide-renders"
    render.mkdir(parents=True, exist_ok=True)
    base = fingerprint(pdf)
    assert len(base) == 9, len(base)
    assert all(p["dimensions"] == [0, 0, 612, 792] and p["rotation"] == 0 for p in base)
    with fitz.open(pdf) as doc:
        for i, p in enumerate(doc):
            p.get_pixmap(matrix=fitz.Matrix(1.7, 1.7), alpha=False).save(render / f"page-{i+1:02d}.png")
            words = p.get_text("words")
            assert words and all(w[0] >= 47 and w[1] >= 0 and w[2] <= 565 and w[3] <= 792 for w in words)
            assert "W58-guide-v1" in p.get_text()
    with tempfile.TemporaryDirectory(prefix="week58-guide-check-") as folder:
        root = Path(folder)
        copied = root / "copied"
        shutil.copytree(src, copied)
        copyout = root / "copy-output"
        subprocess.run(["sh", str(copied / "build.sh"), str(copyout)], check=True)
        assert fingerprint(copyout / "facilitator.pdf") == base
        archive = root / "guide-source.zip"
        with ZipFile(archive, "w") as z:
            for f in sorted(src.iterdir()):
                assert f.is_file(), f"unexpected source subdirectory: {f}"
                z.write(f, Path("guide-src") / f.name)
        extracted = root / "extracted"
        with ZipFile(archive) as z:
            z.extractall(extracted)
        zipout = root / "zip-output"
        subprocess.run(["sh", str(extracted / "guide-src" / "build.sh"), str(zipout)], check=True)
        assert fingerprint(zipout / "facilitator.pdf") == base
    result = {"pages": len(base), "page_size_pt": [612, 792], "all_pages_rendered": True,
              "clean_copy_rebuild": "text, dimensions, rotation and pixels identical",
              "zip_extracted_rebuild": "text, dimensions, rotation and pixels identical",
              "source_inventory": sorted(f.name for f in src.iterdir()),
              "pixel_sha256_108dpi": [p["pixels"] for p in base],
              "physical_pretests": "unperformed", "classroom_piloting": "unperformed"}
    (out / "guide-qa.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
