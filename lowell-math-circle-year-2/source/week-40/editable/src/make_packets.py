from common import *
from knot_geometry import *
COL={'R':'red!75!black','B':'blue!70!black','G':'green!45!black'}
def cord_path(coords,color='black',thick=1.5):
 co='--'.join(f'({a:.3f},{b:.3f})' for a,b in coords)
 return rf'\draw[{color},line width={thick}mm] {co};'+'\n'
def rope(coords):
 return cord_path(coords,'black',3.2)+cord_path(coords,'white',2.4)
def trefoil(top,labels=True):
 cy=top-min(y for x,y in pts)*S;cx=106
 s=''
 for i,a in enumerate(under):
  b=under[(i+1)%3]
  if b<a:b+=TAU
  ts=[a+.045+(b-a-.090)*j/280 for j in range(281)]
  p=[(cx+S*(math.sin(t)+2*math.sin(2*t)),cy+S*(math.cos(t)-2*math.cos(2*t))) for t in ts]
  s+=rope(p)
  if labels:
   t=(a+b)/2
   xx=math.sin(t)+2*math.sin(2*t);yy=math.cos(t)-2*math.cos(2*t)
   norm=math.hypot(xx,yy)
   s+=lab(cx+S*xx+8*xx/norm,cy+S*yy+8*yy/norm,'123'[i],13)
 return s

def arc_demo():
 s=lab(22,63,'input',10,anchor='west')
 for yy,output in [(77,False),(132,True)]:
  # A whole X arc begins after the left underpass, passes over the middle,
  # and ends before the right underpass.
  s+=rope([(32,yy),(40,yy)])+rope([(50,yy),(160,yy)])+rope([(170,yy),(186,yy)])
  # Middle horizontal is over; vertical below has a six-mm gap.
  s+=rope([(105,yy-12),(105,yy-5)])+rope([(105,yy+5),(105,yy+12)])
  for x in [45,165]:s+=rope([(x,yy-12),(x,yy+12)])
  s+=lab(54,yy-6,'X',12)
  if output:
   s+=cord_path([(51,yy),(159,yy)],'blue!65!black',1.6)
   s+=lab(49,yy+8,'start',9)+lab(161,yy+8,'stop',9)
 s+=text(16,98,181,'process: follow X across the overpass to the next gap.',11)
 s+=lab(22,118,'output',10,anchor='west')
 return s


def crossing(x,y,a,b,c,title=None):
 segments=[[(x-16,y),(x-5,y)],[(x,y-13),(x,y+13)],[(x+5,y),(x+16,y)]]
 s=''
 for coords,val in zip(segments,[a,b,c]):
  s+=rope(coords)
  if val in COL:s+=cord_path(coords,COL[val],1.7)
 for val,xx,yy in [(a,x-20,y),(b,x,y-18),(c,x+20,y)]:s+=lab(xx,yy,val if val else '?',12)
 if title:s+=lab(x,y+20,title,10)
 return s

def records(y):
 s=''
 for row in range(3):
  for col in range(4):
   x=25+45*col; yy=y+11*row
   for k in range(3):
    s+=rf'\draw[gray,line width=.4pt] ({x+9*k},{yy}) circle (3.3);'+'\n'
    s+=lab(x+9*k,yy-5,str(k+1),7)
 return s

def loop(top):return rf'\draw[black,line width=3.2mm] (106,{top+64}) ellipse (74 and 57);\draw[white,line width=2.4mm] (106,{top+64}) ellipse (74 and 57);'+'\n'
def rtwo(x,y,before=True):
 # Fixed four endpoints: L,R at horizontal height; P,Q at top.
 s=''
 if before:
  s+=rope([(x,y+32),(x+18,y+32)])+rope([(x+28,y+32),(x+45,y+32)])+rope([(x+55,y+32),(x+74,y+32)])
  s+=rope([(x+23,y),(x+23,y+48),(x+50,y+48),(x+50,y)])
 else:
  s+=rope([(x,y+32),(x+74,y+32)])+rope([(x+23,y),(x+23,y+17),(x+50,y+17),(x+50,y)])
 for a,xx,yy in [('L',x,y+32),('R',x+74,y+32),('P',x+23,y),('Q',x+50,y)]:
  s+=rf'\fill ({xx},{yy}) circle (1);'+'\n'
  s+=lab(xx+( -5 if a=='L' else 5 if a=='R' else 0),yy+( -5 if a in 'PQ' else 0),a,10)
 return s

for band in ['k-1','grades-2-3','grades-4-5']:
 b=[]
 s=text(16,25,180,'Keep cords on the table. Move them without cutting or passing strands through each other. Use red (R), blue (B), and green (G).',11.5)
 s+=arc_demo()
 s+=text(16,153,180,'An arc runs between underpasses and continues through overpasses. A closed strand with no underpasses is one whole arc. Give each whole arc one color. At each crossing the colors must be all the same or all different.',11)
 s+=crossing(46,207,'R','R','R','valid')+crossing(106,207,'R','B','G','valid')+crossing(166,207,'R','R','B','invalid')
 s+=problem(1,236,'Show an adult which strand goes over at each crossing above. Trace one whole arc on the next page without changing strands.',band)
 b.append(s)
 q2={'k-1':'Find every valid coloring of this loop, using tracing paper for new tries. Record each coloring with color dots for whole arcs 1, 2, and 3.',
     'grades-2-3':'Find every valid coloring of this loop, including one-color choices. Record color dots for whole arcs 1, 2, and 3; use tracing paper for new tries.',
     'grades-4-5':'Find every valid coloring of this loop, including one-color choices. The numbers name whole arcs; record each coloring and explain why your list is complete.'}[band]
 s=problem(2,27,q2,band)+trefoil(75)
 s+=records(232)
 b.append(s)
 q3={'k-1':'Can you color this loop using more than one color while keeping one color on each whole arc?',
     'grades-2-3':'Find every valid coloring of this plain loop. Can any use more than one color?',
     'grades-4-5':'Count all valid colorings of this plain loop. Compare that count with the count for the three-crossing loop.'}[band]
 s=problem(3,27,q3,band)+loop(62)
 q4={'k-1':'Try each of the four adult-prepared closed cords in the tray. Can you move it into this plain loop shape without cutting or passing strands through one another?',
     'grades-2-3':'Try to move each of the four adult-prepared closed cords in the tray into this plain loop shape. What can your attempts tell you, and what remains uncertain?',
     'grades-4-5':'Try to move each of the four adult-prepared closed cords in the tray into this plain loop shape. Separate what you managed to do from what you only suspect cannot be done.'}[band]
 s+=problem(4,205,q4,band)+blank(16,240,180,17)
 b.append(s)
 if band=='k-1':
  s=problem(5,27,'Choose the missing colors so every crossing follows the rule. Can any question mark have two different answers?',band)
  for i,(a,over) in enumerate(itertools.product('RBG',repeat=2)):
   s+=crossing(46+60*(i%3),92+66*(i//3),a,over,None)
 elif band=='grades-2-3':
  s=problem(5,27,'Color both pictures so matching end dots have the same colors. An arc may stop at an end dot here. Find every pair of colors at L and P that works.',band)
  s+=lab(61,68,'before',11)+lab(154,68,'after',11)+rtwo(22,85,True)+rtwo(118,85,False)
  s+=line(98,121,112,121,'-{Stealth[length=3mm]},line width=1pt')
  s+=blank(16,151,180,40)
  s+=problem(6,206,'Can the same colors at L and P give two different valid colorings of either whole picture? Explain using the crossing rule.',band)+blank(16,236,180,20)
 else:
  s=problem(5,27,'An arc may stop at an end dot here. Which colors at L and P allow both pictures to be colored with matching end-dot colors? Can the same choice have more than one completion? Explain.',band)
  s+=lab(61,70,'before',11)+lab(154,70,'after',11)+rtwo(22,85,True)+rtwo(118,85,False)+line(98,121,112,121,'-{Stealth[length=3mm]},line width=1pt')
  s+=problem(6,155,'Mathematicians have shown that moving a closed loop without cutting or passing strands through each other preserves its number of valid colorings. Use your counts to decide whether the three-crossing loop can become the plain loop.',band)
  s+=blank(16,190,180,19)
  s+=problem(7,221,'A knot called the figure-eight also has only three colorings, yet cannot become a plain loop. What can equal coloring counts tell you about two loops?',band)
 b.append(s)
 if band=='k-1':
  s=problem(6,27,'Keep each end dot its shown color. Which color choices let you color both whole strands and obey both crossings?',band)
  s+=rtwo(64,70,True)
  # The two crossing strands continue between all four named end dots.
  s+=text(16,137,180,'A strand may stop at an end dot in this picture. Use tracing paper for each try.',11.5)
  cases=[('R','B','R','B'),('R','R','B','R'),('G','B','G','B'),('B','G','B','R'),('B','B','B','B'),('R','G','R','G')]
  for i,case in enumerate(cases):
   xx=23+90*(i%2); yy=172+29*(i//2)
   for j,(name,val) in enumerate(zip('LP RQ'.replace(' ',''),case)):
    s+=lab(xx+17*j,yy-6,name,9)
    s+=rf'\draw[fill={COL[val]},line width=.5pt] ({xx+17*j},{yy}) circle (3.4);'+'\n'
    s+=lab(xx+17*j,yy+7,val,8)
  b.append(s)
 write(40,'Loop colors',band,b)
