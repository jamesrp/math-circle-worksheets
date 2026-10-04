#!/usr/bin/env python3
"""Refresh one week in existing combined PDFs, preserving all other week pages.

Use when only one week changed, including when other standalone inputs have
moved. Requires the existing combined PDFs and their build manifest. Contents
ranges and week bookmarks are regenerated. Never falls back to archived inputs.
"""
from pathlib import Path
import argparse
import importlib.util
import json
from pypdf import PdfReader, PdfWriter

SOURCE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('assemble', SOURCE / 'assemble.py')
assemble = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assemble)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--week', type=int, required=True, choices=list(assemble.WEEKS))
    args = parser.parse_args()
    manifest_path = assemble.QA / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    assemble.register_cover_fonts()
    staged = []
    for suffix, (level, description) in assemble.LEVELS.items():
        previous = manifest[suffix]
        destination = assemble.ROOT / previous['file']
        old = PdfReader(destination)
        assert len(old.pages) == previous['pages'], destination
        week_suffix = ('shared-facilitator' if suffix == 'facilitator' else 'shared') if args.week == 2 else suffix
        replacement = assemble.YEAR2 / f'week-{args.week:02d}' / f'week-{args.week:02d}-{week_suffix}.pdf'
        count = assemble.check_pdf(replacement, student=suffix != 'facilitator')
        entries, next_page = [], 2
        for row in previous['weeks']:
            size = count if row['week'] == args.week else row['pages']
            entries.append({**row, 'pages':size, 'start_page':next_page, 'end_page':next_page+size-1})
            next_page += size
        writer = PdfWriter()
        writer.append(PdfReader(assemble.cover(level, description, entries)))
        for before, after in zip(previous['weeks'], entries):
            title = f"Week {after['week']}: {assemble.WEEKS[after['week']]}"
            if after['week'] == args.week:
                writer.append(replacement, outline_item=title, import_outline=False)
            else:
                writer.append(old, pages=(before['start_page']-1,before['end_page']),
                              outline_item=title, import_outline=False)
        writer.add_metadata({k:str(v) for k,v in (old.metadata or {}).items() if v is not None})
        temporary = assemble.QA / f'refresh-{destination.name}'
        with temporary.open('wb') as stream:
            writer.write(stream)
        assemble.check_pdf(temporary)
        updated = PdfReader(temporary)
        assert len(updated.pages) == next_page-1
        for before, after in zip(previous['weeks'], entries):
            source = PdfReader(replacement) if after['week'] == args.week else old
            start = 0 if after['week'] == args.week else before['start_page']-1
            for offset in range(after['pages']):
                a,b = source.pages[start+offset], updated.pages[after['start_page']-1+offset]
                assert a.extract_text() == b.extract_text()
                assert a.get_contents().get_data() == b.get_contents().get_data()
        bookmarks = [entry for entry in updated.outline if not isinstance(entry,list)]
        assert len(bookmarks) == len(entries)
        assert [updated.get_destination_page_number(x)+1 for x in bookmarks] == [x['start_page'] for x in entries]
        staged.append((temporary,destination))
        manifest[suffix] = {**previous, 'pages':next_page-1, 'weeks':entries}
        print(f'Checked {destination.name}: {next_page-1} pages; replaced Week {args.week} only')
    for temporary,destination in staged:
        temporary.replace(destination)
    manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')

if __name__ == '__main__':
    main()
