# -*- coding: utf-8 -*-
# simu02 #04

No1=0
No2=0
NULL=0

for i in range(5):
    vote=eval(input())
    if(vote==1):
        No1+=1
        
    elif(vote==2):
        No2+=1
        
    else:
        NULL+=1
    print(f"Total votes of No.1: Nami =  {No1}")
    print(f"Total votes of No.2: Chopper =  {No2}")
    print(f"Total null votes =  {NULL}")
    
    
if No1 == No2:
    print("=> No one won the election.")
elif No1 > No2:
    print("=> No.1 Nami won the election.")
elif No2 > No1:
    print("=> No.2 Chopper won the election.")