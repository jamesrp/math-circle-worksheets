"""Copy and ZIP-extract the lean guide source, build, compare every PDF page."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile
import pymupdf as fitz

FILES=['facilitator.tex','build.py','verify_math.py','verify_rebuild.py','README.md']
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pages(path):
    d=fitz.open(path);result=[]
    for p in d:
        result.append({'text':p.get_text(),'dimensions':list(p.rect),'pixels_108dpi':hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).samples).hexdigest()})
    return result
def main():
    p=argparse.ArgumentParser();p.add_argument('output',type=Path);a=p.parse_args()
    out=a.output.resolve();src=Path(__file__).resolve().parent;qa=out/'guide-qa'/'rebuild';qa.mkdir(parents=True,exist_ok=True)
    assert sorted(x.name for x in src.iterdir() if x.is_file())==sorted(FILES)
    copy=qa/'copied-src';copy.mkdir(exist_ok=True)
    for name in FILES:shutil.copy2(src/name,copy/name)
    archive=qa/'guide-source-check.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for name in FILES:z.write(src/name,'guide-src/'+name)
    extract=qa/'extracted';extract.mkdir(exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        assert sorted(z.namelist())==sorted('guide-src/'+name for name in FILES);z.extractall(extract)
    original=pages(out/'facilitator.pdf');checks={}
    for label,source in [('copy',copy),('ZIP',extract/'guide-src')]:
        target=qa/(label.lower()+'-build')
        for script in ('build.py','verify_math.py'):
            r=subprocess.run([sys.executable,str(source/script),str(target)],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (qa/(label.lower()+'-'+script+'.log')).write_text(r.stdout)
            if r.returncode:raise RuntimeError(r.stdout)
        assert all(sha(source/name)==sha(src/name) for name in FILES)
        rebuilt=pages(target/'facilitator.pdf');assert rebuilt==original
        checks[label]={'pages':len(rebuilt),'text_dimensions_pixels_equal':True,'source_bytes_equal':True,'pdf_sha256':sha(target/'facilitator.pdf')}
    r={'source_sha256':{name:sha(src/name) for name in FILES},'final_pdf_sha256':sha(out/'facilitator.pdf'),'page_count':len(original),'page_evidence':original,'checks':checks,'zip_members':['guide-src/'+x for x in FILES],'limits':'No physical printer, cutting, rails, compass, timing or classroom check.'}
    dest=qa/'rebuild-verification.json';dest.write_text(json.dumps(r,indent=2)+'\n');print(dest)
if __name__=='__main__':main()
