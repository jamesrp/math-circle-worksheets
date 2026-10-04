"""Retain compact authored review records; render/build caches remain in tmp."""
import json,re,shutil
from pathlib import Path

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
for week in range(52,64):
    run=ROOT/f'tmp/worksheet-runs/week-{week:02}-new-v1'
    dest=BASE/f'week-{week:02}'/'reviews'
    candidates=[('student-adversarial.md',run/'review.md'),('student-math.md',run/'review-math.md'),
                ('facilitator-independent.md',run/'guide-review.md')]
    revision=next((p for p in [run/'final/revision.md',run/'final/revision-notes.md',run/'final/revision-notes.txt'] if p.exists()),None)
    # Week 57 recorded its revision disposition in its authored source README.
    # Preserve that actual record rather than inventing a separate stage report.
    revision_readme=False
    if revision is None and week==57:
        revision=run/'final/src/README.md'
        revision_readme=True
    if revision:candidates.append(('student-revision.md',revision))
    existing=[(name,src) for name,src in candidates if src.exists()]
    if not existing:continue
    dest.mkdir(parents=True,exist_ok=True)
    for name,src in existing:
        text=src.read_text()
        if name=='student-revision.md' and revision_readme:
            text=('# Revision record retained from the authored source README\n\n'
                  'Week 57 supplied this source-stage README instead of a separate revision report.\n'
                  'The text below is that actual completed revision record; status statements are historical.\n\n'+text)
        # Stage evidence stays in its original repository-relative tmp path.
        # The durable report contains the mathematical finding and disposition.
        def link(m):
            raw=m.group(2).strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',raw) or raw.startswith('#'):return m.group(0)
            target=(src.parent/raw.split('#')[0]).resolve()
            try:relative=target.relative_to(ROOT)
            except ValueError:return m.group(0)
            rebased='../../../../'+str(relative)
            if '#'in raw:rebased+='#'+raw.split('#',1)[1]
            return f'[{m.group(1)}](<{rebased}>)' if ' 'in rebased else f'[{m.group(1)}]({rebased})'
        text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)
        note=('\n\nRecord note: this is the completed authored stage report. Stage-local render/build\n'
              'evidence referenced under `tmp/` is historical and is not included in source ZIPs.\n'
              'Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks\n'
              'are recorded in `../release-checks.json`; coordinator page coverage is recorded\n'
              'in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.\n')
        (dest/name).write_text(text+note)
    check=run/'guide-review-independent.py'
    if check.exists():shutil.copy2(check,dest/'independent-guide-check.py')
    result=run/'guide-review-assets/independent-guide-checks.json'
    if result.exists():
        (dest/'guide-review-assets').mkdir(exist_ok=True)
        shutil.copy2(result,dest/'guide-review-assets/independent-guide-checks.json')
    (dest/'README.md').write_text('# Authored production review records\n\n'+
        '\n'.join(f'- [{name}]({name})' for name,_ in existing)+
        '\n\nThese reports retain findings, exact arguments, stage scope and correction decisions.\n'
        'Rendered images, enumerator scratch files and build caches remain in `tmp/`.\n'
        'If present, `independent-guide-check.py` is the coordinator\'s mathematical checker,\n'
        'using independently transcribed data; its results are in `guide-review-assets/`.\n'
        'The guide author\'s own portable verifiers are separately included with editable sources.\n')
print('Compact available review records preserved for Weeks52–63.')
