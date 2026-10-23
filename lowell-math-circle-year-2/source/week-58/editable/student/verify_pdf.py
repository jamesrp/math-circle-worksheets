"""Check all revised Week 58 PDF pages and portable-source reproduction.

Run: python3 verify_pdf.py OUTPUT_DIRECTORY
Requires PyMuPDF. Renders at 108 dpi. Checks every page's text, media box,
rotation, vector inventory and repeated builds, not physical handling/piloting.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import pymupdf

PT_PER_MM = 72 / 25.4
SOURCE_FILES = ['common.tex', 'students.tex', 'materials.tex', 'build.sh', 'regenerate.py',
                'README.md', 'verify_math.py', 'verify_pdf.py']


def mm_dimensions(path):
    r = path['rect']
    return r.width / PT_PER_MM, r.height / PT_PER_MM


def has_size(path, a, b, unordered=False):
    w, h = mm_dimensions(path)
    if unordered:
        w, h = sorted((w, h)); a, b = sorted((a, b))
    return abs(w-a) < .02 and abs(h-b) < .02


def digest(page):
    return hashlib.sha256(page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).samples).hexdigest()


def page_record(page):
    return dict(media_box=list(page.mediabox), visible_box=list(page.rect),
                rotation=page.rotation, text=page.get_text(), pixels_sha256=digest(page))


def compare_all(out, fresh):
    pages = 0
    for name in ['students', 'materials']:
        with pymupdf.open(out / f'{name}.pdf') as original, pymupdf.open(fresh / f'{name}.pdf') as rebuilt:
            assert len(original) == len(rebuilt)
            for i, (a, b) in enumerate(zip(original, rebuilt)):
                assert page_record(a) == page_record(b), (name, i+1)
                pages += 1
    return f'All {pages} pages: identical text, media/visible dimensions, rotation and 108-dpi pixels.'


def check(out):
    src = Path(__file__).resolve().parent
    assert sorted(p.name for p in src.iterdir()) == sorted(SOURCE_FILES), 'Source bundle must stay lean.'
    report = {'scope': 'Digital checks only; physical pretests and classroom piloting unperformed.'}
    for name, count in [('students', 7), ('materials', 8)]:
        with pymupdf.open(out / f'{name}.pdf') as doc:
            assert len(doc) == count, (name, len(doc))
            renders = out / 'renders' / name
            renders.mkdir(parents=True, exist_ok=True)
            for old in renders.glob('page-*.png'):
                old.unlink()
            texts, pages = [], []
            for i, page in enumerate(doc):
                assert abs(page.mediabox.width - 612) < .1
                assert abs(page.mediabox.height - 792) < .1
                assert page.rotation == (90 if name == 'materials' and i in range(1,8) else 0)
                text = page.get_text()
                assert 'Week 58 / Fair division /' in text
                assert 'Bellingham Math Circle / Week 58 /' in text
                assert ('-v4' if name == 'students' else '-v3') in text   # students v4 (critic follow-up), materials v3
                if name == 'students':
                    band = 'Grades 3–5' if i in [3, 5, 6] else 'Grades K–5' if i in [0, 4] else 'Grades 2–5'
                    assert f'Week 58 / Fair division / {band}' in text
                    assert text.count('Problem ') == 1 and f'Problem {i+1}:' in text
                for block in page.get_text('dict')['blocks']:
                    for line in block.get('lines', []):
                        for span in line['spans']:
                            x0, y0, x1, y1 = span['bbox']
                            assert x0 >= 10 and y0 >= 10 and x1 <= 602 and y1 <= 782, (name, i+1, span)
                for drawing in page.get_drawings():
                    assert page.mediabox.contains(drawing['rect']), (name, i+1, drawing['rect'])
                page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(renders / f'page-{i+1:02}.png')
                texts.append(f'PAGE {i+1}\n{text}')
                record = page_record(page); record.pop('text')
                pages.append(record)
            (out / f'{name}-text.txt').write_text('\n'.join(texts))
            report[name] = {'pages': len(doc), 'text_page_box_and_rotation_checks': 'passed', 'page_records': pages}

    with pymupdf.open(out / 'students.pdf') as s:
        # October 23 card fixes: five P1 records, P2's ownership wording and no
        # saved-division table, 120 mm panels, no P6 table and no P7 boxes.
        p1_records = sum(has_size(d,82,26) for d in s[0].get_drawings())
        assert p1_records == 5, p1_records
        p2 = ' '.join(s[1].get_text().split())
        assert all(f'Record {n}' in p2 for n in range(1,7))
        assert 'Find every way to give all four cards to A and B so that neither person envies the other.' in p2
        assert 'Saved division' not in p2 and 'complete division' not in p2
        p3 = ' '.join(s[2].get_text().split())
        assert 'circle the chooser' in p3
        assert 'Left piece’s value' not in p3
        assert 'whole 120 mm color panel' in p3 and p3.count('60 mm') == 2 and '150' not in p3
        assert p3.count('red: 120 mm') == 2 and p3.count('blue: 120 mm') == 2
        assert 'red: 120 mm' in s[3].get_text() and '150' not in s[3].get_text()
        # Launch outputs are as wide as the two equal lengths (24.5 mm each).
        launch = [mm_dimensions(d) for d in s[2].get_drawings() if has_size(d,24.5,13)]
        assert len(launch) == 2, launch
        assert 'replace R3 with its paper copy' in s[4].get_text()
        p6 = s[5].get_text()
        assert 'Initial allocation only' not in p6 and 'Envy-free division' in p6
        assert sum(has_size(d,54,40) for d in s[5].get_drawings()) == 3
        assert 'One observer' not in s[6].get_text() and 'own tray' not in s[6].get_text()
        report['card_fixes_2026_10_23'] = dict(problem_1_record_boxes=p1_records,
            problem_6_empty_boxes=3, launch_output_widths_mm=launch)

    with pymupdf.open(out / 'materials.pdf') as m:
        card_count = sum(has_size(p,25,25) for p in m[0].get_drawings())
        assert card_count == 6, card_count
        assert sorted(re.findall(r'\b[RBG]\d\b', m[0].get_text())) == ['B1','B2','R1','R2','R3','R3','R3','R3'], m[0].get_text()
        material_text = ''.join(p.get_text() for p in m)
        assert not any(x in material_text for x in ['R4','B3','B4','G1','G2','G3','G4'])
        pref_counts = [sum(has_size(p,100,150,True) for p in m[i].get_drawings()) for i in [1,2,3,4]]
        assert pref_counts == [2,2,2,1], pref_counts
        panel_count = sum(has_size(p,50,40,True) for p in m[4].get_drawings())
        assert panel_count == 3, panel_count
        strips = [sum(has_size(p,240,40,True) for p in m[i].get_drawings()) for i in range(5,8)]
        assert strips == [3]*3, strips
        panels = [sum(has_size(p,120,40,True) for p in m[i].get_drawings()) for i in range(5,8)]
        assert panels == [6]*3, panels
        bars, square_icons, dot_counts = [], [], []
        for i, page in enumerate(m):
            drawings = page.get_drawings()
            bar = [mm_dimensions(p) for p in drawings if has_size(p,100,0,True)]
            assert len(bar) == 1, (i+1,bar)
            bars.append(bar[0])
            dots = 0
            for drawing in drawings:
                fill = drawing['fill']
                if fill is None:
                    continue
                assert not (abs(fill[0]-65/255)<.001 and abs(fill[1]-125/255)<.001), 'Unused green icon'
                if abs(fill[0]-41/255)<.001 and abs(fill[1]-107/255)<.001:
                    w,h = mm_dimensions(drawing)
                    assert abs(w-h)<.001
                    items=drawing['items']
                    assert (len(items)==1 and items[0][0]=='re') or (len(items)==4 and all(x[0]=='l' for x in items))
                    square_icons.append(dict(page=i+1, sides=4, equal_side_mm=w))
                if abs(fill[0]-30/255)<.001 and abs(fill[1]-35/255)<.001 and has_size(drawing,2.2,2.2):
                    dots += 1
            dot_counts.append(dots)
        assert len(square_icons)==4, square_icons
        assert dot_counts == [0,8,2,24,12,0,0,0], dot_counts
        strip_labels=[]
        for i in range(5,8):
            got = re.findall(r'Strip (\d+) / red 120 mm, blue 120 mm / 240 × 40 mm',m[i].get_text())
            a=3*(i-5)+1
            assert got == [str(a),str(a+1),str(a+2)], got
            strip_labels.append(got)
        assert '150' not in material_text and '300' not in material_text and 'half' not in material_text
        report['material_geometry'] = dict(cards_25_by_25_mm=card_count,
            preference_cards_100_by_150_mm=pref_counts, panels_50_by_40_mm=panel_count,
            whole_strips_240_by_40_mm=strips, colour_panels_120_by_40_mm=panels,
            scale_bar_mm_dimensions=bars, regular_blue_squares=square_icons,
            preference_dots_by_page=dot_counts, strip_labels=strip_labels)

    # Print recipe is derived from the actual geometry count per page.
    stock_copies=[5,5,5,1,1,5,5,5]
    subset_copies=[5,5,5,1,1,5,5,0]
    assert sum(stock_copies)==32 and sum(subset_copies)==27
    assert 3*sum(stock_copies[5:])==45 and 3*sum(subset_copies[5:])==30
    report['whole_group_print_recipe'] = dict(pair_kits=5, upper_kits=1,
        stock_copies_by_material_page=stock_copies, stock_sheets=32,
        reusable_goods=25, paper_R3_replacements=5, preference_cards=23, upper_panels=3,
        stock_whole_strips=45, stock_strips_per_pair=9,
        first_route_copies_by_material_page=subset_copies, first_route_sheets=27,
        first_route_whole_strips=30, first_route_strips_per_pair=6,
        separately_supplied_trays=13, rulers=5)

    # Both paths rebuild ALL PDFs from a lean complete source package.
    with tempfile.TemporaryDirectory(prefix='week58-rebuild-',dir=out) as task_tmp:
        task_tmp=Path(task_tmp)
        copied=task_tmp/'copied/src'; copied.mkdir(parents=True)
        for name in SOURCE_FILES:
            shutil.copy2(src/name,copied/name)
        fresh=task_tmp/'copied-build'
        subprocess.run(['sh',str(copied/'build.sh'),str(fresh)],check=True)
        report['clean_copied_source_rebuild']=compare_all(out,fresh)
        archive=task_tmp/'source.zip'
        with zipfile.ZipFile(archive,'w') as z:
            for name in SOURCE_FILES:
                z.write(src/name,f'src/{name}')
        with zipfile.ZipFile(archive) as z:
            assert sorted(z.namelist())==sorted(f'src/{n}' for n in SOURCE_FILES)
            z.extractall(task_tmp/'extracted')
        extracted=task_tmp/'extracted-build'
        subprocess.run(['sh',str(task_tmp/'extracted/src/build.sh'),str(extracted)],check=True)
        report['clean_zip_extracted_source_rebuild']=compare_all(out,extracted)
        report['source_files_checked']=SOURCE_FILES
    (out/'qa-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['students','materials']},indent=2))


if __name__ == '__main__':
    check(Path(sys.argv[1]).resolve())
