from pathlib import Path
import sys
w=int(sys.argv[1]);root=Path(__file__).resolve().parents[2]
run=root/f'tmp/worksheet-runs/encore-week-{w:02d}-20261004-v1';guide=run/'guide-src';guide.mkdir(exist_ok=True)
topic={2:'Lamp lab',3:'Shuffle machines',4:'Stars and wheels',5:'Tower cities'}[w]
body=(root/f'plans/encore-01-05/guide{w:02d}-body.tex').read_text()
assert 'INSERT PRINTED CASE ANSWERS HERE' not in body,'Fill actual printed case answers before generating finalguide'
s=(root/'plans/encore-01-05/guide_template.tex').read_text().replace('@W@',str(w)).replace('@TOPIC@',topic).replace('@ID@',f'{w:02d}').replace('@BODY@',body)
(guide/'facilitator.tex').write_text(s)
(run/'guide-build').mkdir(exist_ok=True)
