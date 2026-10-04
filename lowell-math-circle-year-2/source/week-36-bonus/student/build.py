from common import *
p=Packet(outdir(),36,'Making threes');c=p.c
p.start('Grades 2-5')
para(c,'An allowed three uses three different tiles. Its shapes are all the same or all different; its fills are also all the same or all different. Positions do not count. Ownership counters do not change a tile.',715,small=True)
problem(c,1,'Take turns claiming an unused tile with your own counter. The first player to own an allowed three loses. Play several games, swapping who starts. Can either player guarantee a win?',641)
board9(c,190,500,108)
workspace(c,220,145);p.end()
p.start('Grades 2-5')
problem(c,2,'Put a red, blue or green ownership counter on every tile. No allowed three may have all three counters the same color. Can you do this using only two counter colors? Using three? Find designs and explain any impossible request.')
board9(c,190,520,108)
workspace(c,240,165);p.end()
p.start('Grades 4-5')
para(c,'Every shape-fill tile now comes with number 1, 2 or 3. An allowed three must also have its numbers all the same or all different.',715,small=True)
label(c,'cards',126,673,10);label(c,'attribute checks',323,673,10);label(c,'result',509,673,10)
for y,nums,result in [(646,[1,1,2],'not allowed'),(592,[1,2,3],'allowed')]:
 for j,x in enumerate([74,126,178]):
  tile(c,x,y,j,j,23);label(c,str(nums[j]),x,y-22,10)
 label(c,'shapes: all different',323,y+9,10)
 label(c,'fills: all different',323,y-4,10)
 label(c,'numbers: '+('two alike' if nums[0]==nums[1] else 'all different'),323,y-17,10)
 arrow(c,205,y,238,y);arrow(c,403,y,443,y);label(c,result,509,y-4,11)
problem(c,3,'Choose one numbered version of every shape-fill tile so your nine tiles contain no allowed three. All three numbers must appear. Find different designs. Can changing only the numbers make an allowed three appear?',548)
for j,x in enumerate([125,305,485]):
 label(c,f'number {j+1}',x,449,12);board9(c,x-58,401,58,j+1)
for x in [170,400]:
 board9(c,x-56,190,56)
 for a in range(3):
  for b in range(3):line(c,x-56+b*56-12,190-a*56-20,x-56+b*56+12,190-a*56-20,.7,GRAY)
p.end();p.save()
