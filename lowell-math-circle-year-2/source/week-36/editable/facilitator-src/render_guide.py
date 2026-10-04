from pathlib import Path
import fitz
from PIL import Image
here=Path(__file__).resolve().parent
out=here.parent/'facilitator-qa';out.mkdir(exist_ok=True)
doc=fitz.open(here.parent/'facilitator-guide.pdf')
for i,p in enumerate(doc):
 p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out/f'page-{i+1}.png')
for start in range(0,len(doc),2):
 ims=[Image.open(out/f'page-{j+1}.png') for j in range(start,min(start+2,len(doc)))]
 sheet=Image.new('RGB',(sum(im.width for im in ims),max(im.height for im in ims)),'white')
 x=0
 for im in ims:sheet.paste(im,(x,0));x+=im.width
 sheet.save(out/f'sheet-{start//2+1}.png')
print(f'Rendered {len(doc)} pages')
