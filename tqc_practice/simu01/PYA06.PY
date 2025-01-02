# -*- coding: utf-8 -*-
#SIMU01 #06

total=0
for i in range(5):
    poker=input()
    if(poker=='J' or poker=='j'):
        total+=11
    elif(poker=='Q' or poker=='q'):
        total+=12
    elif(poker=='K' or poker=='k'):
        total+=13
    elif(poker=='A' or poker=='a'):
        total+=1
    else:
        total+=eval(poker)
print(f"{total}")
        
