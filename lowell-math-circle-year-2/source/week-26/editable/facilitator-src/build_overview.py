"""Build the unnumbered mathematical overview, then preserve the numbered guide."""
from pathlib import Path
import io,json,os,subprocess
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor
from pypdf import PdfReader,PdfWriter
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
D=json.loads((HERE/'overview-content.json').read_text())
family=D['font']
def font_path(bold=False):
    base='LiberationSans' if family=='Liberation Sans' else 'DejaVuSans'
    suffix=('-Bold.ttf' if bold else ('-Regular.ttf' if family=='Liberation Sans' else '.ttf'))
    filename=base+suffix
    env=os.environ.get('LIBERATION_FONT_DIR' if family=='Liberation Sans' else 'DEJAVU_FONT_DIR')
    if env and (Path(env)/filename).is_file(): return str(Path(env)/filename)
    try:
        path=subprocess.check_output(['fc-match','-f','%{file}',family+(':style=Bold' if bold else ':style=Regular')],text=True).strip()
        if Path(path).name==filename:return path
    except (OSError,subprocess.CalledProcessError):pass
    for folder in [Path.home()/'.fonts',Path.home()/'.local/share/fonts',Path('/usr/share/fonts')]:
        matches=list(folder.rglob(filename)) if folder.exists() else []
        if matches:return str(matches[0])
    raise RuntimeError('Install '+family+' fonts or set the documented font directory variable.')
pdfmetrics.registerFont(TTFont('Overview',font_path()))
pdfmetrics.registerFont(TTFont('Overview-Bold',font_path(True)))
pdfmetrics.registerFontFamily('Overview',normal='Overview',bold='Overview-Bold')
stream=io.BytesIO(); c=canvas.Canvas(stream,pagesize=(612,792),pageCompression=1)
c.setTitle(D['title']+' - facilitator guide')
c.setFillColor(HexColor('#17232b'));c.setFont('Overview-Bold',8.5)
c.drawString(42,756,'BELLINGHAM MATH CIRCLE / WEEK '+str(D['week'])+' / FACILITATOR GUIDE')
y=721
styles={
 'title':ParagraphStyle('t',fontName='Overview-Bold',fontSize=21,leading=25,textColor=HexColor('#17232b')),
 'sub':ParagraphStyle('s',fontName='Overview',fontSize=10,leading=13,textColor=HexColor('#53626b')),
 'head':ParagraphStyle('h',fontName='Overview-Bold',fontSize=12,leading=15,textColor=HexColor('#17232b')),
 'body':ParagraphStyle('b',fontName='Overview',fontSize=10.4,leading=14,textColor=HexColor('#17232b')),
}
def para(text,style,after=7):
 global y
 p=Paragraph(text,styles[style]);w,h=p.wrap(528,720)
 p.drawOn(c,42,y-h);y-=h+after
para(D['title'],'title',8)
para('Mathematical overview | Draft and unpiloted | 3 October 2026','sub',16)
for heading,paragraphs in D['sections']:
 para(heading,'head',7)
 for text in paragraphs:para(text,'body',7)
 y-=4
assert y>=75, (D['title'],'overview overflow',y)
c.setFont('Overview',8.2);c.setFillColor(HexColor('#53626b'))
c.drawString(42,51,'This overview is unnumbered. References in the following guide use its printed page numbers.')
c.drawString(42,37,'Unscheduled library slot / Detailed proofs and problem-by-problem solutions follow')
c.save();stream.seek(0)
target=ROOT/'build/facilitator-guide.pdf';old=PdfReader(target)
writer=PdfWriter();writer.add_page(PdfReader(stream).pages[0])
for page in old.pages:writer.add_page(page)
writer.add_metadata({'/Title':D['title']+' - facilitator guide','/Subject':'Mathematical overview and numbered teaching guide'})
with target.open('wb') as f:writer.write(f)
print('Prepended mathematical overview; total pages:',len(writer.pages))
