"""Record coordinator inspection only after every displayed final page was read."""
import argparse,json,hashlib
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('week',type=int);ap.add_argument('reports',nargs='+');a=ap.parse_args()
root=Path(__file__).resolve().parents[2];index=root/'plans/new-themes-52-63/final-visual-review.json'
data=json.loads(index.read_text())
for report in a.reports:
 for r in json.loads((root/report).read_text()):
  source=Path(r['file']);kind={'students':'student','facilitator':'guide','materials':'materials'}[source.stem]
  assert not r['outside_page_spans'],r['outside_page_spans']
  data=[d for d in data if (d['week'],d['kind'])!=(a.week,kind)]
  d={'week':a.week,'kind':kind,'file':str(source),'sha256':r['sha256'],'pages':r['pages'],
     'root_inspected_pages':list(range(1,r['pages']+1)),'render_report':report,
     'finding':'Every final page visually inspected by coordinator; mathematical review recorded separately. No clipping, overlap or distorted intended regular figures observed.',
     'physical_rehearsal':'unperformed','classroom_piloting':'unperformed'}
  name='students' if kind=='student' else 'facilitator' if kind=='guide' else 'materials'
  released=Path(f'lowell-math-circle-year-2/week-{a.week:02}/week-{a.week:02}-{name}.pdf')
  if (root/released).exists():
   assert hashlib.sha256((root/released).read_bytes()).hexdigest()==r['sha256']
   d.update(released_file=str(released),released_bytes_match_inspected_final=True)
  data.append(d)
index.write_text(json.dumps(sorted(data,key=lambda d:(d['week'],d['kind'])),indent=2)+'\n')
