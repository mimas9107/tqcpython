# -*- coding: utf-8 -*-
# simu02 #06

L=[input() for i in range(5)] ## List<string>
total=0
for e in L:
    if(e == 'J'):
       total+=11
    elif(e=='Q'):
        total+=12
    elif(e=='K'):
        total+=13
    elif(e=='A'):
        total+=1
    else:
        total+=eval(e)
print(total)