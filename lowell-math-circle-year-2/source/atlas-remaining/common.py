"""Staged student prompts and complete, data-backed facilitator notes."""
import json
from html import escape
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from sheet import DATA, FONT, BOLD, TEAL, GRAY, LIGHT, text_markup, clean


def family_data(batch):
    data=json.loads((DATA/f'{batch}-data.json').read_text())
    return {f['id']:f for f in data['families']}


def start(book,family,page_no,subtitle=None):
    page=family['pages'][page_no-1]
    book.new_page(family['id'],page['title'],family['title'] if subtitle is None else subtitle,
                  part=f"{page_no} / {len(family['pages'])}")
    if page.get('gate'):
        book.p(page['gate'],size=10.5,color=GRAY);book.y+=10
    if page.get('intro'):
        book.rule(page['intro']);book.y+=12
    return book.y


def question(book,family,prompt_id,y=None,size=11.5,text=None,width=524,x=44):
    prompt=next(p for pg in family['pages'] for p in pg['prompts'] if str(p['id'])==str(prompt_id))
    wording=prompt['text'] if text is None else text
    book.printed_tasks.append(dict(family_id=family['id'],prompt_id=str(prompt_id),page=book.page_no,text=wording))
    book.p(str(prompt_id)+'. '+wording,x=x,y=y,width=width,size=size,leading=size*1.32)
    book.y+=8
    return book.y


def blank(book,y=None,height=70,label='',x=44,width=524):
    if y is None:y=book.y
    if y+height>746:raise ValueError(f"Answer space exceeds page on {book.family_id}: {y}+{height}")
    book.box(x,y,width,height,label=label)
    book.y=y+height+12
    return book.y


def lines(book,y=None,n=2,spacing=23,width=524,x=44):
    if y is None:y=book.y+12
    if y+(n-1)*spacing>746:raise ValueError('Writing lines exceed page')
    book.lines(x,y,width,n,spacing)
    book.y=y+(n-1)*spacing+14
    return book.y


def measured(text,size=11,font=FONT):
    style=ParagraphStyle('measure-guide',fontName=font,fontSize=size,leading=size*1.35)
    return Paragraph(text_markup(text,font),style).wrap(524,1000)[1]


def paragraphs(text):
    return [s.strip() for s in str(text).split('\n') if s.strip()]


def section(book,title,items):
    chunks=[p for item in items for p in paragraphs(item)]
    heading=measured(title,14,BOLD)+7
    total=heading+sum(measured(p)+9 for p in chunks)
    needed=total if total<560 else heading+(measured(chunks[0])+9 if chunks else 0)
    if book.y+needed>730:book.new_page(book.family_id,book.page_title,part='continued')
    book.flow_h(title)
    for p in chunks:book.flow_p(p,size=11)


def render_facilitator(book,family,module):
    f=family
    book.new_page(f['id'],f['title'],'Facilitator guide / exact answers and staged hints / not classroom-piloted')
    section(book,'The investigation and a satisfying stop',[f['assessment'],f['satisfying_stop']])
    section(book,'Prerequisites and preparation',[
        'Core: '+f['core_gate'], 'Extensions: '+f['extension_gate'],
        'Reading and representation: '+f['reading'],
        f"Materials: {f['materials']} Preparation: about {f['prep_minutes']} minutes.",f['timing']])
    section(book,'Launch and facilitation',[f['launch']])
    for i,page in enumerate(f['pages'],1):
        section(book,f"Student page {i}: {page['title']}",[page['gate'] or 'Use the core prerequisites.',page['intro']])
        for p in page['prompts']:
            section(book,str(p['id'])+' / prompt and solution',[p['text'],'Solution: '+p['solution']])
            if p.get('hints'):
                section(book,str(p['id'])+' / hints to offer only after exploration',
                        [f'{j}. {hint}' for j,hint in enumerate(p['hints'],1)])
    if hasattr(module,'render_key_figures'):
        module.render_key_figures(book,f['id'])
    for i,extension in enumerate(f.get('extensions',[]),1):
        section(book,f'Optional facilitator extension {i}',[
            'Gate: '+extension['gate'],extension['prompt'],'Solution: '+extension['solution']])
    section(book,'Mathematics and prior use',[f['mathematical_connection'],'Prior use: '+f['prior_use']])
    for s in f['sources']:
        heading='Source: '+s['title']
        description=s['locator']+'. '+s['adaptation']+' Evidence: '+s['checked']
        needed=measured(heading,14,BOLD)+7+measured(description)+9+measured(s['url'],10.5)+9
        if needed<560 and book.y+needed>730:book.new_page(book.family_id,book.page_title,part='continued')
        section(book,heading,[description])
        url=escape(s['url'],quote=True)
        book.flow_p('<link href="'+url+'" color="#126E78">'+escape(s['url'])+'</link>',size=10.5,rich=True)

