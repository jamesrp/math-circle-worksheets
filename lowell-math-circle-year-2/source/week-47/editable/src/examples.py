def height_example(text,label,line,rect,circle,hill):
    s=text(0,17,'One marker in each column shows its tower height.',size=11)
    s+=hill(15,58,[1,2,2,1])+label(28,68,'allowed',11)
    for h in range(3):
        y=58-10*h
        s+=line(72,y,114,y,'gray!45')+label(66,y,str(h),9)
    for i,h in enumerate((1,2,2,1)):
        x=76+11*i
        s+=line(x,38,x,58,'gray!45')+circle(x,58-10*h,2.1,'fill=white,line width=.9pt')
        s+=label(x,64,str(i),9)
    s+=line(48,50,60,50,'-{Stealth[length=2mm]},line width=.8pt')
    s+=line(117,50,128,50,'-{Stealth[length=2mm]},line width=.8pt')
    s+=rect(133,44,44,12,'line width=.8pt')
    for i,h in enumerate((1,2,2,1)):
        if i:s+=line(133+11*i,44,133+11*i,56,'line width=.8pt')
        s+=label(138.5+11*i,50,str(h),13)+label(138.5+11*i,64,str(i),9)
    return s
