#!/usr/bin/env python3
"""Build the range inventory from current companion PDFs, without editing indexes."""
from pathlib import Path
import json,re
import pymupdf
ROOT=Path(__file__).resolve().parents[2]
DATA=json.loads(Path(__file__).with_name('catalog-data.json').read_text())
RELEASED=json.loads(Path(__file__).with_name('release-status.json').read_text())
PROBLEM_MAP={'12':[[1],[2,3],[4]],'15':[[1],[2],[3,4]],'16':[[1,2],[3],[4]]}
rows=[];complete=[];total=0;numbered=0;student_pages=0;guide_pages=0
for k,(theme,titles) in DATA.items():
 n=int(k);week=f'week-{n:02}'
 student=ROOT/f'lowell-math-circle-year-2/{week}/{week}-return-visit.pdf'
 adult=ROOT/f'lowell-math-circle-year-2/{week}/{week}-return-visit-facilitator.pdf'
 zipfile=ROOT/f'lowell-math-circle-year-2/source/{week}-return-visit-source.zip'
 page_by_problem={}
 if student.exists():
  for p,x in enumerate(pymupdf.open(student)):
   text=x.get_text();header=text.splitlines()[0] if text else ''
   problem_labels=re.findall(r'Problem\s+(\d+)(?:\s*\(continued\))?\s*:',text)
   workspace=re.findall(r'Extra workspace for Problem\s+(\d+)',text)
   for s in dict.fromkeys(problem_labels+workspace):
    page_by_problem.setdefault(int(s),[]).append((p+1,header.rsplit('/',1)[-1].strip()))
  if n==12 and 1 in page_by_problem:
   page_by_problem[1].append((2,'Grades K–3'))
 problem_groups=PROBLEM_MAP.get(k,[[j] for j in range(1,len(titles)+1)])
 expected_problems={j for group in problem_groups for j in group}
 delivered=k in RELEASED and student.exists() and adult.exists() and zipfile.exists() and expected_problems.issubset(page_by_problem)
 if delivered:
  complete.append(n);total+=len(titles);numbered+=len(page_by_problem)
  student_pages+=len(pymupdf.open(student));guide_pages+=len(pymupdf.open(adult))
 rel=lambda p:'../'+str(p.relative_to(ROOT))
 pdfs=f'[student]({rel(student)}) / [adult]({rel(adult)}) / [source ZIP]({rel(zipfile)})' if delivered else 'Not yet delivered'
 for i,t in enumerate(titles,1):
  problems=problem_groups[i-1]
  locations=[location for j in problems for location in page_by_problem.get(j,[('—','Pending final page')])]
  location='; '.join(dict.fromkeys(f'{band}; p. {page}' for page,band in locations))
  label=('Problem ' if len(problems)==1 else 'Problems ')+', '.join(map(str,problems))
  rows.append(f'| {n} / {theme} | {i}. {t} | {location} | {pdfs+"; "+label if i==1 else "Same companion, "+label} |')
state='Complete' if len(complete)==17 else 'In progress'
lines=[f'# Weeks 1–17 bonus / return-visit inventory ({state.lower()})','',
 'Prepared October 4, 2026. All material is **unpiloted**; physical materials and procedures have **not been rehearsed**. A theme, investigation, packet and classroom visit are counted separately. The companion materials do not replace the existing student packets, adult guides or Week 1/2 extras. No upload, publication, commit or push is part of this work.','',
 f'Current delivery: **{len(complete)} of 17 companion pairs**, **{total} distinct investigations** across {numbered} numbered problems in delivered student PDFs. Scope: 17 themes with three distinct new investigations each (51 total). A continuation with new examples is not counted as another investigation. Delivered weeks: '+(', '.join(map(str,complete)) or 'none')+'.','',
 f'Released page count: {student_pages} student pages and {guide_pages} adult-guide pages ({student_pages+guide_pages} total). Each released week also has its editable source directory and source ZIP.','',
 'Each source ZIP is beside its editable source directory under `lowell-math-circle-year-2/source/`. Its README explains a clean build into a chosen temporary output directory. Band labels below come from the actual current student PDF; detailed prerequisites, adult-assisted younger entries and readiness-dependent continuations are in the adult guide and range inventory.','',
 'Novelty and checks are documented per investigation in the three detailed range inventories: [Weeks 1–5](bonus-weeks-01-05.md), [Weeks 6–10](bonus-weeks-06-10.md), [Weeks 11–17](bonus-weeks-11-17.md). Source reuse is acknowledged there, especially Week 5’s one-swap precursor, Week 10’s base-guide extension seeds and year-1 password-window lineage, and Week 11 known starts/optional loop. Week 10 turns directed routes, safe first streets and overlapping windows, already named on the current base guide’s page 7, into concrete student investigations. Week 9 shares repeated reflection with Week 21: its new goal is wall-order realizability and corner exclusions, while Week 21 optimizes prescribed-contact routes. Reflection itself is not counted as a new investigation. Week 16’s planned center-refinement question was removed when it proved to duplicate a base task; its replacement asks what a fourth interior label can remove and what must remain.','',
 '| Week / existing theme | Investigation | Suitable printed band / page | Deliverables |','|---|---|---|---|',*rows,'',
 '## Verification evidence','',
 '- [Completed delivery and aggregate checks](encore-01-17-support/completion-checks.json).','- [Final PDF metadata, bounds and render inventory](encore-01-17-support/deliverable-qa.json); page inspection is also recorded in each source/review package and range inventory.','- [Independent root small-case checks](encore-01-17-support/independent-small-cases.json) and [fourth-label audit](encore-01-17-support/fourth-label-check.json). These supplement, rather than replace, the independent per-week mathematics stages and represented-example checks.','- [Source pedagogy notes](encore-01-17-support/pedagogy-source-notes.md), distinguishing reported lessons from proposed adaptations.','',
 '- [Source ZIP identity and reference-copy audit](encore-01-17-support/source-package-audit.json), supplementing the recorded extracted rebuilds.','- [Accepted-release byte audit](encore-01-17-support/release-snapshot-audit.json), checking that current PDFs and ZIPs still match the reviewed releases.','- [Producer inventory link audit](encore-01-17-support/inventory-link-audit.json); absent future outputs remain pending until release.','- [Verification workflow and evidence map](encore-01-17-support/README.md).','',
 ('Completed verification covers' if len(complete)==17 else 'Final verification requires')+' all promised companion PDFs and ZIPs, actual page inspection in every delivered variant, mathematically checked represented examples, and an unrelated extracted-source rebuild whose page text and rendered pixels match. No classroom piloting, material-fit test or remote version synchronization is inferred from digital checks.','']
(ROOT/'plans/bonus-weeks-01-17.md').write_text('\n'.join(lines))
print(f'{state}: {len(complete)} pairs, {total} investigations, {numbered} numbered problems, {student_pages+guide_pages} pages; plans/bonus-weeks-01-17.md')
