#!/usr/bin/env python3
"""Render guide and check bounds; optionally rebuild copied and ZIP source."""
import argparse,hashlib,json,shutil,subprocess,tempfile,zipfile
from pathlib import Path
import pymupdf as fitz

def signature(path):
    with fitz.open(path) as d:
        return [{'text':p.get_text(),'box':list(p.rect),'pixels':hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).samples).hexdigest()} for p in d]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('pdf');ap.add_argument('out');ap.add_argument('--clean-rebuild',action='store_true');a=ap.parse_args();out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=True)
    pdf=Path(a.pdf).resolve();report={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':[]}
    with fitz.open(pdf) as d:
        assert len(d)==10,len(d)
        for i,p in enumerate(d):
            assert list(p.rect)==[0,0,612,792]
            text=p.get_text();assert 'Week 52 / Hinged frames and braces / Adult guide' in text
            assert 'F52-FAC-v2' in text
            bounds=[]
            for b in p.get_text('dict')['blocks']:
                for line in b.get('lines',[]):
                    for span in line['spans']:
                        box=fitz.Rect(span['bbox']);assert box.x0>=40 and box.x1<=573,(i,span)
                        assert box.y0>=20 and box.y1<=780,(i,span)
                        bounds.append(list(box))
            p.get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(out/f'page-{i+1:02}.png')
            report['pages'].append({'page':i+1,'Letter':True,'header_footer':True,'text_inside_margins':True})
        (out/'text.txt').write_text('\n\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)))
    if a.clean_rebuild:
        src=Path(__file__).resolve().parent;expected=signature(pdf);cases=[]
        with tempfile.TemporaryDirectory(prefix='week52-guide-rebuild-') as t:
            t=Path(t);copy=t/'copied-source';shutil.copytree(src,copy)
            archive=t/'guide-source.zip'
            with zipfile.ZipFile(archive,'w') as z:
                for p in src.rglob('*'):
                    if p.is_file():z.write(p,Path('guide-src')/p.relative_to(src))
            with zipfile.ZipFile(archive) as z:z.extractall(t/'extracted')
            for name,folder in [('copied',copy),('zip-extracted',t/'extracted'/'guide-src')]:
                target=t/(name+'-build');subprocess.run(['sh',str(folder/'build.sh'),str(target)],cwd='/tmp',check=True,capture_output=True)
                assert signature(target/'facilitator.pdf')==expected,name
                cases.append({'source':name,'working_directory':'/tmp','all_text_dimensions_pixels_identical':True})
        report['clean_rebuild']=cases
    (out/'digital-checks.json').write_text(json.dumps(report,indent=2)+'\n');print('Guide PDF checks passed:',len(report['pages']),'pages')
if __name__=='__main__':main()
