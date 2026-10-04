"""Author-created TikZ figures and a matching, auditable geometry manifest."""
import json
import math
from pathlib import Path
from geometry import arcs, transform, vertices


def num(x):
    return f"{x:.9f}"


def pt(p):
    return f"({num(p[0])},{num(p[1])})"


class Picture:
    def __init__(self, name, width, height):
        self.name, self.width, self.height = name, width, height
        self.code = [r"\begin{tikzpicture}[x=1mm,y=1mm,line cap=round,line join=round]",
                     f"\\path[use as bounding box] (0,0) rectangle ({width},{height});"]
        self.records = []

    def line(self, a, b, style="line width=.55pt", role="line"):
        self.code.append(f"\\draw[{style}] {pt(a)} -- {pt(b)};")
        self.records.append(dict(kind="line", a=a, b=b, role=role))

    def poly(self, points, style="line width=.55pt,fill=white", role="polygon"):
        self.code.append(f"\\draw[{style}] " + " -- ".join(pt(p) for p in points) + " -- cycle;")
        self.records.append(dict(kind="polygon", points=points, role=role))

    def circle(self, c, r, style="line width=.55pt,fill=white", role="circle"):
        self.code.append(f"\\draw[{style}] {pt(c)} circle ({num(r)});")
        self.records.append(dict(kind="circle", center=c, radius=r, role=role))

    def ellipse(self, c, rx, ry, style="line width=.55pt,fill=white", role="ellipse"):
        self.code.append(f"\\draw[{style}] {pt(c)} ellipse ({num(rx)} and {num(ry)});")
        self.records.append(dict(kind="ellipse", center=c, rx=rx, ry=ry, role=role))

    def arc(self, c, r, a, b, style="line width=.65pt", role="arc"):
        s = (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
        e = (c[0] + r * math.cos(math.radians(b)), c[1] + r * math.sin(math.radians(b)))
        self.code.append(f"\\draw[{style}] {pt(s)} arc[start angle={num(a)},end angle={num(b)},radius={num(r)}];")
        self.records.append(dict(kind="arc", center=c, radius=r, start=a, end=b,
                                 start_point=s, end_point=e, role=role))

    def label(self, x, y, text, options="", size="\\small"):
        self.code.append(f"\\node[font={size},inner sep=1pt,{options}] at ({num(x)},{num(y)}) {{{text}}};")

    def dot(self, p, label=None, offset=(0, -3), role="point"):
        self.code.append(f"\\fill {pt(p)} circle (.55);")
        self.records.append(dict(kind="point", point=p, role=role))
        if label:
            self.label(p[0] + offset[0], p[1] + offset[1], label, size="\\footnotesize")

    def shape(self, kind, cx, cy, w=60, scale=1, angle=0, labels=False,
              marked=False, skeleton=False, role=None):
        role = role or kind
        if kind == "disk":
            self.circle((cx, cy), w * scale / 2, role=role)
            if marked:
                self.dot((cx, cy), "$O$", (3, -3), role="disk_center")
            return
        if kind == "oval":
            assert angle == 0
            self.ellipse((cx, cy), 30 * scale, 20 * scale, role=role)
            return
        if kind == "square":
            a = math.radians(angle)
            ps = [(cx + scale * (x * math.cos(a) - y * math.sin(a)),
                   cy + scale * (x * math.sin(a) + y * math.cos(a)))
                  for x, y in ((-w/2, -w/2), (w/2, -w/2), (w/2, w/2), (-w/2, w/2))]
            self.poly(ps, role=role)
            return
        ps = [transform(p, cx, cy, scale, angle, w) for p in vertices(w)]
        if kind == "triangle":
            self.poly(ps, role=role)
        elif kind == "reuleaux":
            # Three actual 60-degree minor circular arcs, no polygon sampling.
            pieces = []
            records = []
            for x, y, a, b in arcs(w):
                c = transform((x, y), cx, cy, scale, angle, w)
                r = w * scale
                aa, bb = a + angle, b + angle
                s = (c[0] + r * math.cos(math.radians(aa)), c[1] + r * math.sin(math.radians(aa)))
                e = (c[0] + r * math.cos(math.radians(bb)), c[1] + r * math.sin(math.radians(bb)))
                if not pieces:
                    pieces.append(pt(s))
                pieces.append(f"arc[start angle={num(aa)},end angle={num(bb)},radius={num(r)}]")
                records.append(dict(kind="arc", center=c, radius=r, start=aa, end=bb,
                                    start_point=s, end_point=e, role=role + "_boundary"))
            self.code.append("\\draw[line width=.55pt,fill=white] " + " ".join(pieces) + " -- cycle;")
            self.records.extend(records)
            self.records.append(dict(kind="reuleaux", centers=ps, radius=w*scale, role=role,
                                     nominal_width_mm=w, display_scale=scale, rotation=angle))
        else:
            raise ValueError(kind)
        if skeleton or marked:
            for i in range(3):
                self.line(ps[i], ps[(i+1)%3], "gray,densely dashed,line width=.35pt", role="equilateral_side")
        if marked:
            for i in range(3):
                mid = tuple((ps[(i+1)%3][j] + ps[(i+2)%3][j])/2 for j in range(2))
                self.line(ps[i], mid, "gray,densely dotted,line width=.35pt", role="median")
            self.dot((cx, cy), "$O$", (3, 0), role="equilateral_centroid")
        if labels:
            for p, letter in zip(ps, "ABC"):
                dx, dy = p[0]-cx, p[1]-cy
                z = math.hypot(dx, dy)
                self.dot(p, f"${letter}$", (3.8*dx/z, 3.8*dy/z), role="arc_center")

    def output(self):
        return "\\newcommand{\\" + self.name + "}{%\n" + "\n".join(self.code) + "\n\\end{tikzpicture}\\par}\n"


KINDS = ["disk", "oval", "square", "triangle", "reuleaux"]
NAMES = ["disk", "oval", "square", "straight\\\\triangle", "curved\\\\triangle"]


def table(name, rowh=25, fixed=False, marked=False):
    kinds = ["disk", "reuleaux"] if marked else KINDS
    names = ["marked disk", "marked curved\\\\triangle"] if marked else NAMES
    head = 12 if fixed else 9
    p = Picture(name, 180, head + rowh * len(kinds))
    top = p.height
    xs = [0, 56, 99, 142, 180] if fixed else [0, 56, 118, 180]
    p.poly([(0,0),(180,0),(180,top),(0,top)], "line width=.45pt", role="record_frame")
    for x in xs[1:-1]:
        p.line((x,0),(x,top), "line width=.4pt", "record_divider")
    for i in range(len(kinds)):
        p.line((0,top-head-i*rowh),(180,top-head-i*rowh), "line width=.4pt", "record_divider")
    if fixed:
        p.label(77.5, top-head/2, "turn inside?", "text width=37mm,align=center", "\\footnotesize")
        p.label(120.5, top-head/2, "touch both\\\\throughout?", "align=center", "\\footnotesize")
        p.label(161, top-head/2, "deciding\\\\position", "align=center", "\\footnotesize")
    else:
        p.label(87, top-head/2, "smallest gap" if not marked else "smallest $O$-to-edge distance", size="\\footnotesize", options="text width=59mm,align=center")
        p.label(149, top-head/2, "largest gap" if not marked else "largest $O$-to-edge distance", size="\\footnotesize", options="text width=59mm,align=center")
    for i, (k, n) in enumerate(zip(kinds,names)):
        y = top-head-rowh*(i+.5)
        p.shape(k, 15, y, scale=.22, marked=marked)
        p.label(28,y,n,"anchor=west,text width=25mm,align=left", "\\footnotesize")
    return p


def make_all(dest):
    pics = []
    p = Picture("measureExample", 180, 40)
    q = [(0,0),(38,0),(46,32),(8,32)]
    for x, stage in [(6,"piece"),(67,"parallel contacts"),(128,"record")]:
        t = [(x+.55*a,10+.55*b) for a,b in q]
        p.poly(t, "fill=gray!8,line width=.55pt", "example_parallelogram")
        if stage != "piece":
            for xx in [x,x+25.3]:
                p.line((xx,6),(xx,31), role="parallel_support")
            p.line((x,5),(x+25.3,5), "<->,line width=.5pt", "perpendicular_gap")
            p.line((x+1.5,5),(x+1.5,6.5), "line width=.4pt", "right_angle")
            p.line((x,6.5),(x+1.5,6.5), "line width=.4pt", "right_angle")
        if stage == "parallel contacts":
            p.label(x,1,"0", size="\\footnotesize")
            p.label(x+25.3,1,"46 mm", size="\\footnotesize")
        if stage == "record":
            p.label(x+39,18,"46 mm",size="\\small")
        p.label(x+13,36,stage,size="\\footnotesize")
    p.line((43,20),(57,20), "->,gray", "sequence_arrow")
    p.line((104,20),(118,20), "->,gray", "sequence_arrow")
    pics.append(p)
    pics.append(table("extremeTable"))
    pics.append(table("turnTable", rowh=31, fixed=True))

    p = Picture("compassExample",180,53)
    for i in range(3):
        d=(12+60*i,15); e=(d[0]+17.5,d[1]); f=(d[0],d[1]+17.5)
        p.dot(d,"$D$",(-3,-2)); p.dot(e,"$E$",(3,-2)); p.dot(f,"$F$",(-3,2))
        p.line(d,e,"gray,dashed,line width=.4pt","example_radius")
        p.line(d,f,"gray,dashed,line width=.4pt","example_radius")
        if i==0:
            p.label(d[0]+9,10,"25 mm",size="\\footnotesize")
            p.label(d[0]+10,46,"given points",size="\\footnotesize")
        elif i==1:
            joint=(d[0]+8.75,d[1]+23)
            p.line(d,joint,"line width=.8pt","compass_leg")
            p.line(joint,e,"line width=.8pt","compass_leg")
            p.circle(joint,1,"line width=.55pt","compass_joint")
            p.label(d[0]+10,47,"opening $DE$",size="\\footnotesize")
            p.label(d[0]+10,4,"point at $D$",size="\\footnotesize")
        else:
            p.arc(d,17.5,0,90,"line width=1pt","non_task_quarter_arc")
            p.label(d[0]+10,46,"arc $EF$",size="\\footnotesize")
    p.line((43,25),(57,25),"->,gray","sequence_arrow")
    p.line((103,25),(117,25),"->,gray","sequence_arrow")
    pics.append(p)

    p = Picture("constructionRecords",180,90)
    p.poly([(0,0),(180,0),(180,90),(0,90)],"line width=.45pt","record_frame")
    p.line((90,0),(90,90),"line width=.4pt","record_divider")
    for x,w in [(0,60),(90,40)]:
        p.label(x+45,82,f"{w} mm triangle",size="\\small")
        p.label(x+7,66,"predicted width:","anchor=west", "\\footnotesize")
        p.label(x+7,50,"measured gaps:","anchor=west", "\\footnotesize")
    pics.append(p)

    p=Picture("tangentExample",180,46)
    for i,cx in enumerate([26,87,148]):
        p.circle((cx,24),12.35,role="example_circle")
        p.dot((cx,24),"$X$",(-3,-3))
        if i>=1:
            p.line((cx-20,36.35),(cx+20,36.35),role="circle_support")
            p.dot((cx,36.35),"$P$",(3,3))
        if i==2:
            p.line((cx,24),(cx,36.35),role="contact_radius")
            p.line((cx,33.85),(cx+2.5,33.85),role="right_angle")
            p.line((cx+2.5,33.85),(cx+2.5,36.35),role="right_angle")
        p.label(cx,5,["circle","one contact","right angle"][i],size="\\footnotesize")
    p.line((49,24),(61,24),"->,gray","sequence_arrow")
    p.line((110,24),(122,24),"->,gray","sequence_arrow")
    pics.append(p)
    p=Picture("proofPositions",180,65)
    for cx,a in [(30,7),(90,37),(150,83)]:
        p.shape("reuleaux",cx,32,scale=.55,angle=a,labels=True,skeleton=True,
                role=f"proof_reuleaux_{a}")
    pics.append(p)
    # Non-task marked rectangle: O=(12,9), right support x=44, distance 32.
    # O is deliberately off center; display at 0.6 scale preserves right angles.
    p=Picture("pointSupportExample",180,40)
    for x,stage in [(7,"marked piece"),(68,"one touching edge"),(129,"record")]:
        p.poly([(x,10),(x+26.4,10),(x+26.4,26.8),(x,26.8)],
               "fill=gray!8,line width=.55pt","point_example_rectangle")
        o=(x+7.2,15.4)
        if stage != "marked piece":
            contact=(x+26.4,15.4)
            p.line((x+26.4,6),(x+26.4,32),role="point_example_support")
            p.line(o,contact,"line width=.5pt","point_example_perpendicular")
            p.line((contact[0]-1.6,contact[1]),
                   (contact[0]-1.6,contact[1]+1.6),role="point_example_right_angle")
            p.line((contact[0]-1.6,contact[1]+1.6),
                   (contact[0],contact[1]+1.6),role="point_example_right_angle")
        p.dot(o,"$O$",(-2,-3),role="point_example_mark")
        if stage == "one touching edge":
            p.label(x+17.4,21,"32 mm",size="\\footnotesize")
        if stage == "record":
            p.label(x+38,18,"32 mm",size="\\small")
        p.label(x+13,36,stage,size="\\footnotesize")
    p.line((45,19),(58,19),"->,gray","sequence_arrow")
    p.line((106,19),(119,19),"->,gray","sequence_arrow")
    pics.append(p)
    pics.append(table("heightTable",rowh=48,marked=True))

    p=Picture("perimeterCompare",180,103)
    p.shape("disk",22,57,scale=.63,role="perimeter_disk")
    p.dot((22,57))
    p.line((22,57),(40.9,57),role="disk_radius")
    p.label(22,32,"radius 30 mm",size="\\footnotesize")
    p.label(22,22,"disk",size="\\small")
    p.shape("reuleaux",65,57,scale=.63,labels=True,skeleton=True,role="perimeter_reuleaux")
    c=transform((0,0),65,57,.63,0,60)
    p.arc(c,37.8,0,60,"line width=1.3pt","highlight_reuleaux_arc")
    p.label(65,22,"curved triangle",size="\\small")
    big=(135,53)
    p.circle(big,37.8,role="generating_circle")
    for a in range(0,360,60):
        endpoint=(big[0]+37.8*math.cos(math.radians(a)),big[1]+37.8*math.sin(math.radians(a)))
        p.line(big,endpoint,"gray,densely dashed,line width=.35pt","sixth_radius")
        p.dot(endpoint)
    p.dot(big,"$A$",(-3,-3))
    p.label(177,53,"$B$",size="\\footnotesize")
    p.label(156,90,"$C$",size="\\footnotesize")
    p.arc(big,37.8,0,60,"line width=1.3pt","highlight_sixth_arc")
    p.label(135,9,"radius 60 mm",size="\\footnotesize")
    pics.append(p)

    p=Picture("cutoutSheet",200,223)
    for kind,cx,cy,caption,marked in [
            ("disk",48,44,"disk: diameter 60 mm",True),
            ("oval",150,44,"oval: 60 by 40 mm",False),
            ("square",48,114,"square: side 60 mm",False),
            ("triangle",150,114,"triangle: side 60 mm",False),
            ("reuleaux",48,184,"curved triangle: width 60 mm",False),
            ("reuleaux",150,184,"marked curved triangle",True)]:
        p.shape(kind,cx,cy,marked=marked,role="cutout_"+kind+("_marked" if marked else ""))
        p.label(cx,cy-(30.5 if kind=="reuleaux" else 36),caption,size="\\footnotesize")
    pics.append(p)

    p=Picture("gridMat",200,200)
    for k in range(0,201,10):
        p.line((k,0),(k,200),"gray!45,line width=.3pt","grid_vertical")
        p.line((0,k),(200,k),"gray!45,line width=.3pt","grid_horizontal")
    p.poly([(0,0),(200,0),(200,200),(0,200)],"line width=.65pt","grid_outer")
    pics.append(p)
    p=Picture("triangleTemplates",200,190)
    for w,cy in [(60,145),(40,49)]:
        for cx in [48,150]:
            p.shape("triangle",cx,cy,w=w,labels=True,role=f"compass_template_{w}")
            p.label(cx,cy-w/2-12,f"{w} mm sides",size="\\small")
    pics.append(p)
    p=Picture("checkBar",200,9)
    p.line((50,5),(150,5),"line width=.7pt","100mm_check_bar")
    p.line((50,3),(50,7),role="check_endpoint")
    p.line((150,3),(150,7),role="check_endpoint")
    p.label(100,1,"100 mm",size="\\footnotesize")
    pics.append(p)
    dest=Path(dest)
    dest.mkdir(parents=True,exist_ok=True)
    (dest/"assets.tex").write_text("% Original generated TikZ assets; x = y = 1 mm.\n"+"\n".join(p.output() for p in pics))
    (dest/"geometry.json").write_text(json.dumps([dict(name=p.name, width=p.width,height=p.height,primitives=p.records) for p in pics],indent=2)+"\n")


if __name__=="__main__":
    import sys
    make_all(sys.argv[1])
