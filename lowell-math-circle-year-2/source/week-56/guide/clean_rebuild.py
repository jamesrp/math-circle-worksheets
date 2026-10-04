#!/usr/bin/env python3
"""Copy and lean-ZIP clean builds; exact text/dimensions/pixels for every page."""
import hashlib,json,shutil,subprocess,sys,zipfile
from pathlib import Path
import pymupdf as fitz

def compare(baseline,candidate):
    a,b=fitz.open(baseline),fitz.open(candidate)
    assert len(a)==len(b)==10
    pages=[]
    for i,(x,y) in enumerate(zip(a,b)):
        tx=x.get_text();ty=y.get_text();assert tx==ty
        assert tuple(x.rect)==tuple(y.rect)==(0,0,612,792)
        xp=x.get_pixmap(matrix=fitz.Matrix(1.5,1.5));yp=y.get_pixmap(matrix=fitz.Matrix(1.5,1.5))
        assert (xp.width,xp.height,xp.n)==(yp.width,yp.height,yp.n)
        assert xp.samples==yp.samples
        pages.append({'page':i+1,'text_equal':True,'dimensions_equal':True,'pixels_equal':True,
          'pixel_sha256':hashlib.sha256(xp.samples).hexdigest()})
    return pages

def main():
    baseline=Path(sys.argv[1]).resolve();qa=Path(sys.argv[2]).resolve()
    src=Path(__file__).resolve().parent
    assert not qa.is_relative_to(src),'QA must be outside deliverable source'
    qa.mkdir(parents=True,exist_ok=True)
    files=['facilitator.tex','build.sh','check_answers.py','clean_rebuild.py','README.md']
    assert sorted(x.name for x in src.iterdir() if x.is_file())==sorted(files)
    copied=qa/'copied-source';copied.mkdir(exist_ok=True)
    for name in files:shutil.copy2(src/name,copied/name)
    zpath=qa/'guide-source-test.zip'
    with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
        for name in files:z.write(src/name,'guide-src/'+name)
    extracted=qa/'extracted';extracted.mkdir(exist_ok=True)
    with zipfile.ZipFile(zpath) as z:
        assert len(z.namelist())==5
        z.extractall(extracted)
    runs={}
    for label,tree in [('copied',copied),('zip-extracted',extracted/'guide-src')]:
        out=qa/(label+'-output')
        subprocess.run(['sh',str(tree/'build.sh'),str(out)],check=True,capture_output=True,text=True)
        subprocess.run([sys.executable,str(tree/'check_answers.py'),str(qa/(label+'-math'))],check=True,capture_output=True,text=True)
        runs[label]={'pages':compare(baseline,out/'facilitator.pdf'),'math_checker_passed':True}
    data={'baseline':str(baseline),'page_count':10,'render_scale':1.5,'source_files':files,
          'no_reference_or_intermediate_files':True,'runs':runs}
    (qa/'clean-rebuild-checks.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS: copied and ZIP-extracted source reproduce all 10 pages; exact text, Letter dimensions, pixels at 108 dpi; both independent answer checks pass.')

if __name__=='__main__':main()
