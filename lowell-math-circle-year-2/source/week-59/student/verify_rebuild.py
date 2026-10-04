"""Clean copied-source and ZIP-extracted rebuilds, compared page by page."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile
import pymupdf

FILES=['README.md','mathematical-notes.md','students.tex','materials.tex','geometry.py',
       'make_assets.py','build.py','verify_math.py','verify_rebuild.py']


def fingerprint(pdf):
    doc=pymupdf.open(pdf)
    result=[]
    for p in doc:
        pix=p.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5),alpha=False)
        result.append(dict(dimensions_pt=list(p.rect),text=p.get_text(),
                           rendered_size=[pix.width,pix.height],
                           pixel_sha256=hashlib.sha256(pix.samples).hexdigest()))
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('reference',type=Path)
    args=ap.parse_args()
    reference=args.reference.resolve()
    src=Path(__file__).resolve().parent
    qa=reference/'qa'/'rebuild-checks'
    if qa.exists():
        shutil.rmtree(qa)
    qa.mkdir(parents=True)
    copied=qa/'copied-src'
    copied.mkdir()
    for name in FILES:
        shutil.copy2(src/name,copied/name)
    archive=qa/'week59-revised-source-check.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            z.write(src/name,'src/'+name)
    extracted=qa/'extracted'
    extracted.mkdir()
    with zipfile.ZipFile(archive) as z:
        assert z.namelist()==['src/'+name for name in FILES]
        z.extractall(extracted)
    receipts={}
    for label,source in [('copied',copied),('zip-extracted',extracted/'src')]:
        assert sorted(p.name for p in source.iterdir())==sorted(FILES)
        assert all((source/name).read_bytes()==(src/name).read_bytes() for name in FILES)
        out=qa/(label+'-output')
        done=subprocess.run([sys.executable,str(source/'build.py'),str(out)],capture_output=True,text=True)
        (qa/(label+'-build.log')).write_text(done.stdout+done.stderr)
        assert done.returncode==0,done.stdout+done.stderr
        checks=subprocess.run([sys.executable,str(source/'verify_math.py'),str(out)],capture_output=True,text=True)
        (qa/(label+'-math.log')).write_text(checks.stdout+checks.stderr)
        assert checks.returncode==0,checks.stdout+checks.stderr
        receipts[label]={}
        for name in ['students','materials']:
            original=fingerprint(reference/(name+'.pdf'))
            rebuilt=fingerprint(out/(name+'.pdf'))
            assert original==rebuilt,(label,name,'text/dimensions/pixel mismatch')
            receipts[label][name]=dict(pages=len(original),letter_dimensions=True,
                                      identical_text=True,identical_pixels=True,
                                      identical_source_bytes=True,
                                      page_pixel_sha256=[p['pixel_sha256'] for p in original])
    result=dict(rebuilds=receipts,source_members=FILES,
                source_sha256={n:hashlib.sha256((src/n).read_bytes()).hexdigest() for n in FILES},
                check_zip=str(archive),physical_pretests='unperformed',piloting='unperformed')
    (qa/'rebuild-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: copied source and ZIP-extracted source each reproduce all 9 pages with identical text, dimensions and pixels.')


if __name__=='__main__':
    main()
