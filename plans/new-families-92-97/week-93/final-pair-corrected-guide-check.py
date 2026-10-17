from pathlib import Path
import pymupdf,hashlib,subprocess,shutil,os,json
R=Path(__file__).resolve().parent
base=Path('/Users/jamespfeiffer/Documents/Codex/2026-10-16/task-5/analysis-family')
f=base/'lowell-math-circle-year-2/week-93/week-93-facilitator.pdf'
current=pymupdf.open(f);old=pymupdf.open(R/'pdfs/week-93-facilitator.pdf')
assert len(current)==len(old)==5
unchanged=[]
for i in range(5):
 pix=current[i].get_pixmap(matrix=pymupdf.Matrix(1.4,1.4))
 pix.save(R/'renders'/f'corrected-guide-page-{i+1:02}.png')
 if i!=3:
  assert pix.samples==old[i].get_pixmap(matrix=pymupdf.Matrix(1.4,1.4)).samples
  unchanged.append(i+1)
assert 'permits finer decimal endpoints' in current[3].get_text()
src=base/'lowell-math-circle-year-2/source/week-93/guide'
dest=R/'independent-build/corrected-guide'
shutil.copytree(src,dest,dirs_exist_ok=True)
env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1',TZ='UTC')
logs=[]
for i in range(2):
 p=subprocess.run(['/Library/TeX/texbin/pdflatex','-interaction=nonstopmode','-halt-on-error','facilitator.tex'],cwd=dest,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 logs.append(p.stdout);assert p.returncode==0
assert 'Overfull' not in logs[-1]
(R/'independent-build/corrected-guide-build.log').write_text('\n'.join(logs))
assert (dest/'facilitator.pdf').read_bytes()==f.read_bytes()
out={'corrected_guide':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'pixel_identical_pages':unchanged,'visually_reinspected_changed_page':4,'clean_rebuild':'byte-identical','physical_rehearsal':'untested','piloting':'unpiloted'}
(R/'corrected-guide-check-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
# Related-activity context: extract actual existing guides, no novelty claim from a broad absence search.
for week in [20,48,51]:
 p=base/f'lowell-math-circle-year-2/week-{week:02}/week-{week:02}-facilitator.pdf'
 d=pymupdf.open(p)
 print('WEEK',week,'FIRST PAGE',d[0].get_text()[:2700])
