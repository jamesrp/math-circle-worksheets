from itertools import product
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
from math import factorial,comb
import json
def histories(colors,n,mode='copy'):
    bag=[c+'0' for c in colors];out=[]
    def draw(bag,word,k):
        if k>n:out.append((word,bag));return
        for identity in bag:
            nextbag=bag[:]
            if mode!='nothing':nextbag.append((identity[0] if mode=='copy' else {'R':'B','B':'R'}[identity[0]])+str(k))
            draw(nextbag,word+[identity],k+1)
    draw(bag,[],1);return out
two={}
for mode in ['copy','opposite','nothing']:
    hs=histories('RB',2,mode);hist=Counter(sum(i[0]=='R' for i in word) for word,bag in hs)
    two[mode]={'histories':len(hs),'red_draw_counts':dict(hist),'mixed_chance':str(F(hist[1],len(hs))),'all_marked_words':[w for w,b in hs]}
forecasts={}
for w in map(''.join,product('RB',repeat=4)):
    forecasts[w]=str(F(1+w.count('R'),6))
three={}
for n in range(1,6):
    hs=histories('RBG',n);hist=Counter(tuple(sum(x[0]==c for x in w) for c in 'RBG') for w,bag in hs)
    assert len(hist)==comb(n+2,2) and set(hist.values())=={factorial(n)} and len(hs)==factorial(n+2)//2
    three[n]={'marked_history_count':len(hs),'count_vector_count':len(hist),'history_multiplicity_per_vector':factorial(n),'vectors':{str(k):v for k,v in hist.items()} if n<=3 else 'all vectors checked'}
result={'two_draw_mechanisms':two,'four_draw_forecasts':forecasts,'three_color_checks':three,'new_final_week35_example':{'input':'RBB','edit':'RRB','changed_positions':1,'two_repeats':'RRBRRB'},'new_final_week36_examples':{'shape_fill':['open circle','striped triangle','solid square'],'112_allowed':False,'123_allowed':True}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
