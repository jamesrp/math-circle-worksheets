"""Original TikZ assets generated from the editable network descriptions."""
import json
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('networks.json').read_text())


def key(a, b):
    return ''.join(sorted((a,b)))


def graph(name, scale=None, selected=(), dots=False, prices=True, compact=False, additions=()):
    g=DATA[name]
    scale=g['scale'] if scale is None else scale
    selected=set(selected)
    nsize=0.28 if compact else 0.52
    fsize=r'\small' if compact else r'\normalsize'
    s=[rf'\begin{{tikzpicture}}[x={scale}cm,y={scale}cm,baseline=(current bounding box.center)]']
    for v,x,y in g['vertices']:
        s.append(rf'\coordinate ({v}) at ({x},{y});')
    for a,b,w in g['edges']:
        s.append(rf'\draw[available] ({a}) -- ({b});')
    for a,b,w in g['edges']:
        if key(a,b) in selected:
            s.append(rf'\draw[bought] ({a}) -- ({b});')
    positions={v:(x,y) for v,x,y in g['vertices']}
    for a,b,w in g['edges']:
        if not prices: continue
        ax,ay=positions[a]; bx,by=positions[b]
        fraction=g.get('label_fractions',{}).get(key(a,b),0.5)
        mx,my=ax+(bx-ax)*fraction,ay+(by-ay)*fraction
        # Prices are offset perpendicular to their links, leaving continuous
        # printed links to trace. Physical offset is independent of map scale.
        dx,dy=bx-ax,by-ay
        length=(dx*dx+dy*dy)**0.5
        ox,oy=-dy/length,dx/length
        if abs(dx)<1e-6: ox,oy=-1,0
        if abs(dy)<1e-6: ox,oy=0,-1 if ay<0.1 else 1
        off=0.18 if compact else 0.32
        px,py=mx+ox*off/scale,my+oy*off/scale
        if w is None:
            label=r'\makebox[0.6cm]{\rule{0.5cm}{0.35pt}}'
        elif dots:
            label=rf'{w}\;\pricedots{{{w}}}'
        else:
            label=str(w)
        s.append(rf'\node[price,font={fsize}] at ({px:.5f},{py:.5f}) {{{label}}};')
    for v,x,y in g['vertices']:
        s.append(rf'\node[place,minimum size={nsize*2}cm,font={fsize}] at ({v}) {{{v}}};')
    s.extend(additions)
    s.append(r'\end{tikzpicture}')
    return '\n'.join(s)


def command(name, diagram):
    return rf'\newcommand{{\{name}}}{{%'+'\n'+diagram+'\n}\n'


def generate():
    s=[]
    s.append(command('ExampleAvailable',graph('convention',compact=True,dots=True)))
    s.append(command('ExamplePaid',graph('convention',selected=['XY','YZ'],compact=True,dots=True)))
    s.append(command('ExampleRecord',graph('convention',selected=['XY','YZ'],compact=True,prices=False)))
    s.append(command('TriangleOne',graph('triangle_one',dots=True)))
    s.append(command('TriangleTwo',graph('triangle_two',dots=True)))
    s.append(command('FourTies',graph('four_ties',dots=True)))
    s.append(command('FourTiesRecord',graph('four_ties',scale=0.75,compact=True,prices=False)))
    s.append(command('FourTrap',graph('four_trap')))
    s.append(command('FourTrapRecord',graph('four_trap',scale=0.9,compact=True,prices=False)))
    s.append(command('FiveTies',graph('five_ties')))
    s.append(command('FiveTiesRecord',graph('five_ties',scale=0.78,compact=True,prices=False)))
    s.append(command('SwapBefore',graph('swap_demo',selected=['UV','VW'],compact=True)))
    s.append(command('SwapMiddle',graph('swap_demo',selected=['UV','VW','UW'],compact=True)))
    s.append(command('SwapAfter',graph('swap_demo',selected=['UV','UW'],compact=True)))
    s.append(command('SwapFirst',graph('swaps',selected=['AB','AD','AC'])))
    s.append(command('SwapSecond',graph('swaps',selected=['AB','BC','CD'])))
    s.append(command('SixCert',graph('six_cert')))
    s.append(command('PriceDesign',graph('price_design')))
    s.append(command('SixGood',graph('six_cert',scale=1.25,selected=['AB','BC','CD','DE','EF'])))
    s.append(command('SixBad',graph('six_cert',scale=1.25,selected=['AB','AC','BD','DE','DF'])))
    s.append(command('Distinct',graph('distinct')))
    return '\n'.join(s)


if __name__=='__main__':
    import sys
    Path(sys.argv[1]).write_text(generate())
