from pathlib import Path
import pymupdf as fitz
root=Path(__file__).resolve().parents[1]
doc=fitz.open(root/'return-visit.pdf')
assert len(doc)==3, len(doc)
out=root/'render';out.mkdir(exist_ok=True)
for i,page in enumerate(doc,1):
    txt=page.get_text()
    assert f'Problem {i}:' in txt
    assert 'Week 3 / Shuffle-machine return visits / Grades 2' in txt
    assert 'Bellingham Math Circle / Week 3 / W03-RV-v1' in txt
    assert page.rect.width==612 and page.rect.height==792
    for word in page.get_text('words'):
        assert word[0]>=20 and word[1]>=20 and word[2]<=592 and word[3]<=772,word
    page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out/f'page-{i}.png')
    (out/f'page-{i}.txt').write_text(txt)
print('All three pages rendered; Letter bounds and labels passed.')
