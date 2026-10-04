#!/usr/bin/env python3
"""Audit portable ZIP paths, editable-file identity, and current PDF references.

The per-week coordinators separately execute unrelated extracted-source rebuilds.
This audit supplements those checks; it does not claim to execute a build.
"""
from pathlib import Path, PurePosixPath
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[2]
records=[]
for n in range(1,18):
    week=f'week-{n:02}'
    archive=ROOT/f'lowell-math-circle-year-2/source/{week}-return-visit-source.zip'
    directory=archive.with_name(f'{week}-return-visit')
    if not archive.exists():continue
    unsafe=[];mismatches=[];references=[]
    with zipfile.ZipFile(archive) as z:
        names=z.namelist()
        for name in names:
            path=PurePosixPath(name)
            if path.is_absolute() or '..' in path.parts or '\\' in name:
                unsafe.append(name);continue
            if name.endswith('/'):continue
            relative=PurePosixPath(*path.parts[1:]) if path.parts[0]==directory.name else path
            local=directory/str(relative)
            data=z.read(name)
            if not local.is_file() or local.read_bytes()!=data:mismatches.append(name)
            if relative.suffix.lower()=='.pdf':
                current=ROOT/f'lowell-math-circle-year-2/{week}/{relative.name}'
                references.append({'entry':name,'matches_current_bytes':current.exists() and current.read_bytes()==data})
    record={'week':n,'zip':str(archive.relative_to(ROOT)),'entries':len(names),
            'unsafe_paths':unsafe,'has_readme':any(PurePosixPath(x).name=='README.md' for x in names),
            'has_build_script':any(PurePosixPath(x).name=='build.sh' for x in names),
            'editable_file_mismatches':mismatches,'reference_pdfs':references,
            'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
    records.append(record)
Path(__file__).with_name('source-package-audit.json').write_text(json.dumps(records,indent=2)+'\n')
failures=[r['week'] for r in records if r['unsafe_paths'] or r['editable_file_mismatches'] or not r['has_readme'] or not r['has_build_script'] or any(not x['matches_current_bytes'] for x in r['reference_pdfs'])]
print(f'{len(records)} source packages audited; failed weeks: {failures}')
if failures:raise SystemExit(1)
