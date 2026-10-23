#!/usr/bin/env python3
"""Independent ideal-linkage checks; finite tests complement the guide's proof."""
from math import cos,sin,pi,hypot,isclose
from fractions import Fraction as F

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(k,a): return tuple(k*x for x in a)
def sub(a,b): return add(a,mul(-1,b))
def area(poly):return abs(sum(x*v-y*u for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1])))/2

def main():
 count=0
 for i in range(36):
  for j in range(36):
   if (i-j)%36 in (0,18):continue
   u=(80*cos(i*pi/18),80*sin(i*pi/18));v=(80*cos(j*pi/18),80*sin(j*pi/18))
   O=(0,0);X=u;Q=mul(2,u);Y=add(Q,v);T=add(u,v);P=add(Y,v)
   for a,b in [(O,X),(X,Q),(Q,Y),(Y,P),(X,T),(T,Y)]:
    assert isclose(hypot(*sub(b,a)),80,abs_tol=1e-8)
   assert all(isclose(a,2*b,abs_tol=1e-8) for a,b in zip(P,T))
   count+=1
 for shape in [[(0,0),(20,0),(20,20),(0,20)],[(0,0),(20,0),(20,10),(10,10),(10,20),(0,20)],[(0,0),(20,0),(0,20)]]:
  assert area([mul(2,p) for p in shape])==4*area(shape)
  assert area([mul(F(1,2),p) for p in shape])==area(shape)/4
 for O in [(40,140),(50,150),(70,140)]:
  for T in [(110,115),(110,165),(160,115),(160,165),(135,140)]:
   P=sub(mul(2,T),O)
   assert add(O,mul(F(1,2),sub(P,O)))==T
   for d in [(30,0),(0,10),(-10,5)]: assert sub(sub(mul(2,T),add(O,d)),P)==mul(-1,d)
 # Independently transcribed task geometry; checks exact paper regions, not thumbnails.
 O=(40,140)
 inputs={'A':[(115,125),(150,125),(150,145)],'B':[(120,120),(150,120),(140,150)],'C':[(115,135),(125,135),(125,150),(145,150),(145,125),(155,125)],'G':[(120,125),(140,125),(140,145),(120,145)],'H':[(120,125),(150,125),(150,135),(130,135),(130,145),(120,145)],'I':[(120,125),(150,125),(120,155)],'M':[(130,125),(150,125),(140,150)]}
 outputs={'D':[(190,110),(220,180),(270,160),(260,100),(210,140)],'E':[(200,110),(260,110),(260,150),(230,175),(200,150)],'J':[(200,110),(260,110),(260,150),(200,150)],'K':[(190,135),(240,135),(240,125),(270,145),(240,165),(240,155),(190,155)]}
 for pts in inputs.values():
  for T in pts:
   P=sub(mul(2,T),O);assert 110<=T[0]<=160 and 115<=T[1]<=165;assert 180<=P[0]<=290 and 90<=P[1]<=190
 for pts in outputs.values():
  for P in pts:
   T=mul(F(1,2),add(P,O));assert 110<=T[0]<=160 and 115<=T[1]<=165
 assert [area(inputs[k])/100 for k in 'GHI']==[4,4,F(9,2)]
 for T in inputs['M']:
  shifted=add(T,(10,0));assert shifted[0]<=160
  assert sub(mul(2,T),O)==sub(mul(2,shifted),(60,140))
 assert [mul(F(1,2),add(P,O)) for P in [(220,125),(260,155)]]==[(130,F(265,2)),(150,F(295,2))]
 print(f'PASS: {count} noncollapsed ideal poses; length, inverse, area, all task coordinates and anchor identities.')
 card_fixes()
 print('Finite checks do not certify physical hardware, print fit or classroom use.')

def card_fixes():
 """Claims added with the review card's fixes (v2, October 23, 2026)."""
 O=(40,140)
 # Shared Problem 4: P stays in F's box (220..260 x 125..155) exactly when T stays in the
 # half-size box (130..150 x 132.5..147.5); checked both ways on a 1/4 mm grid.
 inF=lambda P:220<=P[0]<=260 and 125<=P[1]<=155
 inH=lambda T:130<=T[0]<=150 and F(265,2)<=T[1]<=F(295,2)
 n=0
 for i in range(4*100,4*190+1):
  for j in range(4*110,4*170+1):
   T=(F(i,4),F(j,4)); P=sub(mul(2,T),O)
   assert inF(P)==inH(T); n+=1
 assert (150-130,F(295,2)-F(265,2))==(20,15)
 # The half-size box lies in the T zone, where OT stays between 70 and about 123 mm.
 assert 110<=130 and 150<=160 and 115<=F(265,2) and F(295,2)<=165
 zone=[(110+x/2,115+y/2) for x in range(101) for y in range(101)]
 d=[hypot(*sub(T,O)) for T in zone]
 assert isclose(min(d),70) and 122<max(d)<123
 # Guide, Shared Problem 3: at full stretch (u=v) T reaches Q; in the folded pose T=Q with
 # OT=TP=160 but O, T, P not collinear unless u is parallel to v. At collapse (v=-u)
 # Y meets X and T, P meet O.
 for i in range(36):
  u=(80*cos(i*pi/18),80*sin(i*pi/18))
  assert hypot(*sub(add(u,u),mul(2,u)))<1e-9
  for j in range(36):
   v=(80*cos(j*pi/18),80*sin(j*pi/18))
   Q=mul(2,u);P=add(Q,mul(2,v));T=Q
   assert isclose(hypot(*T),160) and isclose(hypot(*sub(P,T)),160)
   cross=T[0]*P[1]-T[1]*P[0]
   assert (abs(cross)<1e-6)==((i-j)%36 in (0,18))
  v=mul(-1,u); X=u;Y=add(mul(2,u),v);T=add(u,v);P=add(mul(2,u),mul(2,v))
  assert hypot(*sub(Y,X))<1e-9 and hypot(*T)<1e-9 and hypot(*P)<1e-9
 # Materials: one 9 x 12 inch tracing sheet covers both drawing zones (x 100..290, y 90..190);
 # the 20 x 30 inch base meets the 450 x 400 mm minimum and holds the 431.8 x 279.4 mm mat.
 assert (290-100,190-90)<=(12*25.4,9*25.4) and 190<12*25.4 and 100<9*25.4
 assert 20*25.4>=400 and 30*25.4>=450 and 431.8<30*25.4 and 279.4<20*25.4
 # Template: holes 80 mm apart and 11 mm from the strip ends; a 7 mm pencil in an 18 mm
 # strip leaves 5.5 mm of foam each side and 7.5 mm to the end.
 assert 182==2*80+2*11 and 102==80+2*11 and (18-7)/2==5.5 and 11-7/2==7.5
 print(f'PASS: card fixes; Problem 4 region ({n} grid points), fold and collapse poses, T-zone distances, overlay, base and template sizes.')

if __name__=='__main__':main()
