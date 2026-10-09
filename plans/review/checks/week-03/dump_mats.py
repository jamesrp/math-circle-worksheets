"""Print every mat read from the final Week 3 PDFs: page, pictures, arrows (1-indexed targets), labels."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pdfmats import read_pdf  # noqa: E402

for name in ["week-03-k-1.pdf", "week-03-grades-2-3.pdf", "week-03-grades-4-5.pdf",
             "week-03-facilitator.pdf", "week-03-return-visit.pdf", "week-03-return-visit-facilitator.pdf"]:
    print("=" * 20, name)
    for pno, mats in read_pdf(name):
        for k, m in enumerate(mats):
            pics = " ".join(p or "-" for p in m.pictures) if any(m.pictures) else ""
            perm = m.perm if m.perm else ("blank" if all(t is None for t in m.targets) else m.targets)
            w = m.top[0].width / 72
            heads = max((abs(o) for _, o in m.heads), default=0)
            print(f"p{pno} mat{k + 1} n={m.n} slot={w:.2f}in perm={perm} pics=[{pics}] "
                  f"maxhead_off={heads:.2f} labels={' '.join(m.labels)[:60]!r}")
