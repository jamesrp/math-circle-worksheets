#!/usr/bin/env python3
"""Reconstruct each portable family in an empty directory and compare every output."""
import argparse, hashlib, json, re, subprocess, tempfile, zipfile, sys
from urllib.parse import unquote
import pymupdf  # Inspect the delivered PDF page inventory.
from pathlib import Path

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('repo',type=Path); ap.add_argument('weeks',nargs='+',type=int); ap.add_argument('--out',type=Path,required=True); ap.add_argument('--index',type=Path); a=ap.parse_args(); repo=a.repo.resolve(); rows=[]
 tempbase=repo/'tmp'/'seven-week-release'; tempbase.mkdir(parents=True,exist_ok=True)
 for w in a.weeks:
  stem=f'week-{w:02d}'; package=repo/'lowell-math-circle-year-2'/'source'/stem; archive=package.parent/(stem+'-source.zip'); outputs=repo/'lowell-math-circle-year-2'/stem
  with tempfile.TemporaryDirectory(prefix=stem+'-',dir=tempbase) as td:
   td=Path(td)
   with zipfile.ZipFile(archive) as z:
    members=[n for n in z.namelist() if not n.endswith('/')]
    assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in members), 'unsafe archive path'
    assert all(not any(p in {'.git','__pycache__','node_modules'} for p in Path(n).parts) for n in members), 'cache in archive'
    z.extractall(td)
   candidates=list(td.rglob('build.py')); assert candidates, 'no builder'; depth=min(len(p.relative_to(td).parts) for p in candidates); builders=[p for p in candidates if len(p.relative_to(td).parts)==depth]; assert len(builders)==1,builders
   result=subprocess.run([sys.executable,str(builders[0]),'--out',str(td/'rebuilt'),'--work',str(td/'tmp')],text=True,capture_output=True)
   (tempbase/f'{stem}-rebuild.log').write_text(result.stdout+result.stderr)
   assert result.returncode==0, result.stdout+result.stderr
   pdfs=[]
   original=sorted(p.name for p in outputs.glob('*.pdf')); rebuilt=sorted(p.name for p in (td/'rebuilt').glob('*.pdf'))
   assert original==rebuilt,(original,rebuilt)
   assert all(p.name in original for p in builders[0].parent.rglob('*.pdf')), 'unexpected PDF bundled in source'
   for name in original:
    p=outputs/name; q=td/'rebuilt'/name; assert digest(p)==digest(q),name+' output mismatch'
    references=list(builders[0].parent.rglob(name))
    for r in references: assert digest(r)==digest(p),str(r)+' reference mismatch'
    doc=pymupdf.open(p)
    page_sizes=[[round(page.rect.width,3),round(page.rect.height,3)] for page in doc]
    assert all(page.get_text().strip() for page in doc), name+' blank PDF page'
    pdfs.append({'pages':len(doc),'page_sizes_points':page_sizes,'file':str(p.relative_to(repo)),'sha256':digest(p),'rebuilt_byte_identical':True,'packaged_reference_count':len(references)})
   packaged_files=[]
   for n in members:
    rel=Path(n).relative_to(builders[0].parent.relative_to(td)); actual=package/rel
    assert actual.is_file(),str(actual)+' missing editable'
    assert digest(actual)==digest(td/n),str(actual)+' source differs'
    packaged_files.append(str(rel))
   actual_files=sorted(str(p.relative_to(package)) for p in package.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
   assert sorted(packaged_files)==actual_files, 'ZIP/editable inventory mismatch'
   rows.append({'week':w,'archive':str(archive.relative_to(repo)),'archive_sha256':digest(archive),'members':members,'pdfs':pdfs,'portable_check':'passed'})
 links=[]
 if a.index:
  index=a.index.resolve()
  for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',index.read_text()):
   if '://' in target or target.startswith('#'): continue
   path=(index.parent/unquote(target.split('#')[0])).resolve()
   assert path.exists() or path==a.out.resolve(), 'broken index link: '+target
   links.append({'target':target,'resolved':str(path.relative_to(repo))})
 report={'packages':rows,'pdf_count':sum(len(r['pdfs']) for r in rows),'page_count':sum(p['pages'] for r in rows for p in r['pdfs']),'index_links':links}
 a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(report,indent=2)+'\n'); print(f'PASS: {len(rows)} packages rebuilt byte-identically; {report["pdf_count"]} PDFs, {report["page_count"]} pages; {len(links)} local index links')
if __name__=='__main__':main()
