#!/usr/bin/env python3
"""Audit actual PDF geometry and copied-source/ZIP rebuilds; never write in src.

Requires PyMuPDF/Pillow. Every rendered page must also be visually inspected.
"""
from pathlib import Path
from itertools import product
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
import pymupdf
from PIL import Image, ImageDraw

p=argparse.ArgumentParser()
p.add_argument("pdf",type=Path)
a=p.parse_args()
pdf=a.pdf.resolve()
source=Path(__file__).resolve().parent
qa=pdf.parent/"qa"
if qa==source or source in qa.parents:
    p.error("PDF/evidence directory must be outside editable source")
qa.mkdir(parents=True,exist_ok=True)
render=qa/"render"
render.mkdir(exist_ok=True)
doc=pymupdf.open(pdf)
assert len(doc)==7
bands=("3–5","3–5","3–5","4–5","4–5","3–5","4–5")
problems=[]
pages=[]
scale=pymupdf.Matrix(1.7,1.7)
for i,page in enumerate(doc,1):
    text=page.get_text()
    assert tuple(page.rect)==(0,0,612,792)
    assert f"Week 60 / Take it or pass / Grades {bands[i-1]}" in text
    assert "Bellingham Math Circle / Week 60 / W60-S-v2" in text
    assert text.rstrip().endswith(str(i))
    labels=[int(n) for n in re.findall(r"Problem (\d+):",text)]
    problems+=labels
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines",[]):
            for span in line["spans"]:
                r=pymupdf.Rect(span["bbox"])
                assert r.x0>=40 and r.x1<=572 and r.y0>=24 and r.y1<=778,(i,span)
    pix=page.get_pixmap(matrix=scale)
    pix.save(render/f"page-{i:02d}.png")
    pages.append({"page":i,"grade_band":bands[i-1],"problems":labels,
                  "points":list(page.rect),"pixel_sha256":hashlib.sha256(pix.samples).hexdigest()})
assert problems==list(range(1,10))
first=" ".join(doc[0].get_text().split())
forced="With one counter left, you must take the offer, even if it is 0."
removal="Remove one turn counter after deciding on each offer."
assert forced in first and removal in first and first.index(forced)<first.index(removal)
assert "opposite winners in two six-round matches" in first
assert "Show possible offers for both" in first

def cards(page):
    result=[]
    for path in page.get_drawings():
        if path["dashes"]!="[] 0":
            r=path["rect"]
            # TikZ emits four line segments, rather than a PDF rectangle opcode.
            edges=path["items"]
            assert len(edges)==4 and all(edge[0]=="l" for edge in edges)
            for i,edge in enumerate(edges):
                assert edge[2]==edges[(i+1)%4][1]
                assert edge[1].x==edge[2].x or edge[1].y==edge[2].y
            tokens=page.get_textbox(r).split()
            assert tokens[-1]=="score"
            result.append((r,tuple(int(x) for x in tokens[:-1])))
    return sorted(result,key=lambda row:(row[0].y0,row[0].x0))

pairs=cards(doc[1]);triples=cards(doc[2]);new=cards(doc[5])
assert (len(pairs),len(triples),len(new))==(9,27,18)
collections=[("p2 0/4/6",pairs,(0,4,6),2),
             ("p3 0/4/6",triples,(0,4,6),3),
             ("p6 0/3/6",new[:9],(0,3,6),2),
             ("p6 0/5/6",new[9:],(0,5,6),2)]
card_evidence=[]
for label,rows,bag,n in collections:
    assert [word for _,word in rows]==list(product(bag,repeat=n))
    assert max(r.width for r,_ in rows)-min(r.width for r,_ in rows)<0.001
    assert max(r.height for r,_ in rows)-min(r.height for r,_ in rows)<0.001
    assert abs(rows[0][0].width-154.8)<0.01
    assert abs(rows[0][0].height-(63.36 if n==2 else 50.4))<0.01
    for i,(r,_) in enumerate(rows):
        assert all(not r.intersects(s) for s,_ in rows[i+1:])
    card_evidence.append({"collection":label,"count":len(rows),
                          "width_pt":rows[0][0].width,"height_pt":rows[0][0].height,
                          "words":[word for _,word in rows]})
assert all(not r.intersects(s) for r,_ in new[:9] for s,_ in new[9:])

# Actual circular paths contain four cubic segments at equal axis scaling.
circles=[path["rect"] for path in doc[3].get_drawings()
         if len(path["items"])==4 and all(item[0]=="c" for item in path["items"])
         and abs(path["rect"].width-path["rect"].height)<0.001]
assert len(circles)==5
assert sum(r.x0<306 for r in circles)==2 and sum(r.x0>306 for r in circles)==3
assert all(abs(r.width-17.28)<0.01 for r in circles)

# Non-deduplicated header/footer evidence prevents display tooling hiding repeats.
images=[Image.open(render/f"page-{i:02d}.png").convert("RGB") for i in range(1,8)]
montage=Image.new("RGB",(images[0].width,7*180),"white")
draw=ImageDraw.Draw(montage)
for i,im in enumerate(images):
    top=im.crop((0,0,im.width,105));bottom=im.crop((0,im.height-75,im.width,im.height))
    assert top.convert("L").getextrema()[0]<80 and bottom.convert("L").getextrema()[0]<80
    montage.paste(top,(0,i*180));montage.paste(bottom,(0,i*180+105))
    draw.text((8,i*180+5),f"page {i+1}",fill="black")
montage.save(qa/"headers-footers.png")

allowed={"students.tex","build.py","check_math.py","check_pdf.py","README.md","mathematics.md"}
actual={str(f.relative_to(source)) for f in source.rglob("*") if f.is_file()}
assert actual==allowed,(actual,allowed)
source_hashes={name:hashlib.sha256((source/name).read_bytes()).hexdigest() for name in sorted(allowed)}
copied=qa/"copied-source"
if copied.exists():
    shutil.rmtree(copied)
shutil.copytree(source,copied)
archive=qa/"source-roundtrip.zip"
with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED) as z:
    for name in sorted(allowed):
        z.write(source/name,f"week-60-source/{name}")
extracted=qa/"zip-extracted"
if extracted.exists():
    shutil.rmtree(extracted)
with zipfile.ZipFile(archive) as z:
    assert {Path(name).name for name in z.namelist()}==allowed
    z.extractall(extracted)

builds=[]
for label,src in (("copied",copied),("zip",extracted/"week-60-source")):
    out=qa/f"{label}-clean-build"
    if out.exists():
        shutil.rmtree(out)
    subprocess.run([sys.executable,str(src/"build.py"),str(out)],check=True)
    fresh=pymupdf.open(out/"students.pdf")
    assert len(fresh)==len(doc)
    for before,after in zip(doc,fresh):
        assert before.get_text()==after.get_text()
        assert before.rect==after.rect
        assert before.get_pixmap(matrix=scale).samples==after.get_pixmap(matrix=scale).samples
    assert "Overfull" not in (out/".build/students.log").read_text()
    assert {name:hashlib.sha256((src/name).read_bytes()).hexdigest()
            for name in sorted(allowed)}==source_hashes
    builds.append({"source":label,"pages":7,"text_dimensions_pixels":"identical"})
assert {str(f.relative_to(source)) for f in source.rglob("*") if f.is_file()}==allowed
evidence={"PASS":True,"pdf":str(pdf),"pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
          "pages":pages,"actual_card_collections":card_evidence,
          "counter_geometry":{"left":2,"right":3,"diameter_pt":circles[0].width},
          "after_decision_rule_and_opposite_sample_task":True,
          "clean_rebuilds":builds,"source_files_sha256":source_hashes,
          "portable_source_contains_only_authored_files":True,
          "physical_rehearsal":"unperformed","classroom_pilot":"unperformed"}
(qa/"verification.json").write_text(json.dumps(evidence,indent=2)+"\n")
print("PASS: seven Letter pages; all labels; 9+27+9+9 complete cards; equal circles; copied and ZIP-extracted sources reproduce every page's text/dimensions/pixels.")
