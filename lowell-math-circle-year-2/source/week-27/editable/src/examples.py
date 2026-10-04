def blocking_example(tx,ln,token,box,rules):
    s=tx(.6,.9,rules,size=13.7,lead=17)
    s+=tx(.6,2.1,'Example: check P with U. First choice is on the left.',size=14)
    for base,both in ((.65,True),(4.5,False)):
        s+=tx(base,2.9,'Current pairs',w=3.25,size=12)
        x=base+.4; X=base+2.75
        s+=ln(x,3.65,X,3.65,'black,line width=1.2pt')+ln(x,4.5,X,4.5,'black,line width=1.2pt')
        s+=ln(x,3.65,X,4.5,'gray!65,dashed,line width=.8pt')
        for xx,yy,ch,side in ((x,3.65,'P','L'),(x,4.5,'Q','L'),(X,3.65,'V','R'),(X,4.5,'U','R')):
            s+=token(xx,yy,ch,side,d=.55,size=17)
        for row,who,choices,current in ((0,'P','UV','V'),(1,'U','PQ' if both else 'QP','Q')):
            y=5.65+row*.8
            s+=token(base+.25,y,who,'L' if who=='P' else 'R',d=.5,size=16)
            s+=tx(base+.62,y-.16,':',w=.15,size=16)
            s+=box(base+.85,y-.33,2.1,.66,'black,line width=.65pt')
            for i,ch in enumerate(choices):
                t=token(base+1.36+i*.99,y,ch,'R' if who=='P' else 'L',d=.5,size=16)
                if ch==current:t=t.replace('fill=white','fill=gray!22')
                s+=t
        s+=tx(base,7.25,'P prefers U to V: yes',w=3.35,size=13.5)
        s+=tx(base,7.8,'U prefers P to Q: '+('yes' if both else 'no'),w=3.35,size=13.5)
        s+=tx(base,8.6,'Both yes: P and U block.' if both else 'P and U do not block.',w=3.35,size=14)
    s+=tx(.6,9.35,'Shaded choice = current partner. This check is only for P and U.',size=12.5)
    return s
