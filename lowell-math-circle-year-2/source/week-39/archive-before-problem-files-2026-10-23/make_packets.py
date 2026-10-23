from common import *
TREE={'A':(0,1),'B':(1,1),'C':(1,0),'D':(2,1),'E':(3,0),'F':(3,2)}
TEDGES=['AB','BC','BD','DE','DF']
RING={'A':(0,1),'B':(1,0),'C':(2,1),'D':(1,2)}
REDGES=['AB','BC','CD','DA']
EIGHT={'H':(2,1),'A':(0,0),'B':(0,2),'C':(4,0),'D':(4,2)}
EEDGES=['HA','AB','BH','HC','CD','DH']
COLORS={'A':'red!65!black','B':'blue!70!black','C':'yellow!80!black','D':'green!55!black','E':'orange','F':'violet','H':'black'}
def graph(x,y,sc,nodes,edges,labels=True):
 s=''
 for e in edges:
  a,b=nodes[e[0]],nodes[e[1]]
  s+=line(x+a[0]*sc,y+a[1]*sc,x+b[0]*sc,y+b[1]*sc,'line width=3mm,gray!25')
  s+=line(x+a[0]*sc,y+a[1]*sc,x+b[0]*sc,y+b[1]*sc,'line width=.7pt')
 for k,(a,b) in nodes.items():
  s+=rf'\draw[fill={COLORS[k]}!20,line width=.7pt] ({x+a*sc},{y+b*sc}) circle (3.5);'+'\n'
  if labels:s+=lab(x+a*sc,y+b*sc,k,12)
 return s


def step_card(x,y,a,b,removed=False):
    nd={'A':(0,1),'B':(1,1),'C':(1,0),'D':(2,1)}
    s=blank(x,y,31,26)
    for e in ['AB','BC','BD']:
        u,v=nd[e[0]],nd[e[1]]
        s+=line(x+5+u[0]*10,y+7+u[1]*10,x+5+v[0]*10,y+7+v[1]*10,'gray!40,line width=1mm')
    u,v=nd[a],nd[b]
    # Draw the step direction in place on a miniature copy of the same map.
    s+=line(x+5+u[0]*10,y+7+u[1]*10,x+5+v[0]*10,y+7+v[1]*10,'-{Stealth[length=2.3mm]},line width=1pt')
    for k,(xx,yy) in nd.items():
        s+=rf'\fill[{COLORS[k]}] ({x+5+xx*10},{y+7+yy*10}) circle (1.2);'+'\n'
        s+=lab(x+5+xx*10,y+3+yy*10,k,7)
    if removed:s+=line(x+2,y+24,x+29,y+2,'gray,line width=.7pt')
    return s

def demo(y):
    s=lab(21,y+13,'input',9,anchor='east')
    for i,(a,b) in enumerate(zip('ABCB','BCBD')):s+=step_card(25+38*i,y,a,b)
    s+=lab(193,y+13,'replay',9)
    s+=lab(21,y+47,'remove',9,anchor='east')
    for i,(a,b) in enumerate(zip('ABCB','BCBD')):s+=step_card(25+38*i,y+34,a,b,i in (1,2))
    s+=lab(193,y+47,'then replay',8)
    s+=lab(21,y+81,'output',9,anchor='east')
    for i,(a,b) in enumerate([('A','B'),('B','D')]):s+=step_card(25+38*i,y+68,a,b)
    s+=text(111,y+74,82,'No steps left means the pawn stays at its start.',10)
    return s

def routes(y,rs,band):
 s=''
 for i,r in enumerate(rs):
  yy=y+i*21
  s+=text(19,yy,175,r'$'+r'\to '.join(r)+r'$'+r'\hfill $\longrightarrow$ \rule{48mm}{.3pt}',13 if band!='k-1' else 14)
 return s

def small_ring_pair(y):return graph(36,y,26,RING,REDGES)+graph(129,y,26,RING,REDGES)


for band in ['k-1','grades-2-3','grades-4-5']:
 b=[]
 rulestr='Move a pawn on the roads. Keep each journey as ordered step tiles; an adult may record. Remove only two adjacent steps along the same road in opposite directions. Replay the other steps in order. The map, start, and finish stay fixed.'
 s=text(16,25,180,rulestr,11)+demo(60)
 if band=='k-1':
  q='Make a three-step trip from A to E and four-step trips from B back to B and from A to D. Make each one as a row of step tiles, then shorten it as much as you can.'
  s+=problem(1,158,q,band)+graph(36,190,32,TREE,TEDGES)
 else:
  q='Shorten each recorded trip until no move is possible. Make a different seven-step trip from C to F that finishes with the same route as the last one.'
  s+=problem(1,159,q,band)+graph(119,207,23,TREE,TEDGES)
  s+=routes(207,['ABABDFDE','ABDFDE','CBCBDF'],band)
  # Short route strings are recorded to the left of the map.
  s=s.replace('text width=175mm','text width=90mm').replace(r'\hfill $\longrightarrow$ \rule{48mm}{.3pt}',r' $\longrightarrow$')
 b.append(s)
 if band=='k-1':
  # Meet a short surviving ring journey before asking for long route histories.
  s=problem(2,27,'Make four-step trips from A back to A on this ring. Which can you shorten to staying at A, and which keep some steps?',band)+graph(50,77,53,RING,REDGES)
  s+=blank(16,202,180,50)
  b.append(s)
  # Retain the previous entry problem as a later investigation, at its original scale.
  s=problem(3,27,'Make a seven-step trip from A to E and a seven-step trip from C to F. Replay each one, removing immediate out-and-back steps until none remain.',band)+graph(36,77,32,TREE,TEDGES)
  s+=blank(16,162,180,90)
  b.append(s)
  s=problem(4,27,'Make trips from A back to A using 4, 6, 8, and 12 road steps. Which can you shorten to staying at A?',band)+graph(30,77,49,TREE,TEDGES)
  s+=problem(5,190,'Make a trip from C to F that uses every road. Can any such trip keep an extra road step after all immediate reversals are removed?',band)+blank(16,235,180,20)
 elif band=='grades-2-3':
  s=problem(2,27,'Make three different 12-step trips from A back to A, each using every road. Can any trip home on this map survive after every immediate reversal is removed?',band)+graph(30,72,49,TREE,TEDGES)+blank(16,184,180,71)
 else:
  s=problem(2,27,'On this map, can a trip from A back to A survive after every immediate reversal is removed? Explain why your answer holds for trips of any length.',band)+graph(30,69,49,TREE,TEDGES)
  s+=blank(16,179,180,34)+problem(3,225,'Can two trips from C to F finish with different routes after every immediate reversal is removed? Explain using the roads.',band)
 b.append(s)
 if band=='k-1':
  s=problem(6,27,'Make every different trip from A back to A that can remain after shortening an eight-step trip on this ring. Replay each result with your pawn.',band)+graph(50,77,53,RING,REDGES)
  s+=blank(16,202,180,50)
 elif band=='grades-2-3':
  s=problem(3,27,'Make every different trip from A back to A that can remain after shortening an eight-step ring trip. Find the fewest road steps in a surviving trip home.',band)+graph(55,71,48,RING,REDGES)
  s+=problem(4,189,'Remove different first detours from the recorded trip below. Can two removal orders end differently?',band)
  s+=routes(221,['ABABCBADCDA'],band)+blank(16,243,180,13)
 else:
  s=problem(4,27,'Shorten each recorded trip in different orders. Can the choice of first reversal ever change the final route on any road map? Explain, or give a counterexample.',band)
  s+=graph(54,68,38,RING,REDGES)+routes(159,['ABABCBADCDA','ABADCBC','ABCDABCBA'],band)+blank(16,225,180,30)
 b.append(s)
 if band=='k-1':
  s=problem(7,27,'Make every different trip from A to C that can remain after shortening a six-step trip. Can two of your remaining trips visit exactly the same roads in a different order?',band)+graph(50,76,53,RING,REDGES)
  s+=blank(16,203,180,49)
 elif band=='grades-2-3':
  s=problem(5,27,'From H, go around the left ring through A, then the right ring through C. Trade only the order of the two full ring trips. Do the two journeys become the same after removing every immediate reversal?',band)+graph(25,87,41,EIGHT,EEDGES)
  s+=problem(6,197,'Make two trips from H back to H, each using both rings and at least 12 road steps. One must shorten to staying at H; the other must lose no steps.',band)+blank(16,235,180,21)
 else:
  s=problem(5,27,'From H, go around the left ring through A, then the right ring through C, then the left ring backward, then the right ring backward. Can the whole trip disappear by removing immediate reversals?',band)+graph(25,84,41,EIGHT,EEDGES)
  s+=problem(6,197,'This trip goes around each ring once each way. Does that information alone tell whether a trip can disappear? Make another trip with those same counts and a different result.',band)+blank(16,237,180,19)
 b.append(s)
 write(39,'Road detours',band,b)
