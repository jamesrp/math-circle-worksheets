from pathlib import Path
import zipfile,subprocess,hashlib,json,shutil
r=Path(__file__).resolve().parent.parent; final=r/'final';z=final/'week-87-source.zip'
with zipfile.ZipFile(z,'w',compression=zipfile.ZIP_DEFLATED) as out:
 for p in sorted((final/'src').iterdir()):
  if p.suffix not in ['.py','.txt','.md']:continue
  info=zipfile.ZipInfo('week-87-student-source/'+p.name,(2026,10,17,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;out.writestr(info,p.read_bytes())
 for p in sorted(final.glob('*.pdf')):
  info=zipfile.ZipInfo('week-87-student-source/reference-pdfs/'+p.name,(2026,10,17,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;out.writestr(info,p.read_bytes())
clean=r/'revision-clean-extract'
if clean.exists():shutil.rmtree(clean)
with zipfile.ZipFile(z) as f:f.extractall(clean);members=f.namelist()
root=clean/'week-87-student-source'
subprocess.run(['python3',str(root/'check_math.py')],check=True)
subprocess.run(['python3',str(root/'build.py'),'--out',str(clean/'rebuilt'),'--work',str(clean/'work')],check=True)
results={}
for name in ['shared','line','upper','materials']:
 p=final/(name+'.pdf');q=clean/'rebuilt'/(name+'.pdf');ref=root/'reference-pdfs'/(name+'.pdf')
 assert p.read_bytes()==q.read_bytes()==ref.read_bytes(),name
 results[name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'byte_identical':True}
(r/'revision-audit/rebuild.json').write_text(json.dumps({'files':results,'zip_members':members,'zip_sha256':hashlib.sha256(z.read_bytes()).hexdigest()},indent=2)+'\n')
print('Clean extraction: all 4 PDFs byte-identical;',len(members),'owned ZIP members.')
