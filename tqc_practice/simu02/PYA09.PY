# -*- coding: utf-8 -*-
# simu02 #09

filename=input()
male=0
female=0
f=open(filename,'r',encoding='utf-8')

buf=f.readlines()
for e in buf:
    print(e)
    if(e.split()[2]!='性別'):
        if(eval(e.split()[2]) == 0): female+=1
        elif(eval(e.split()[2]) == 1): male+=1    
f.seek(0)
print(f"Number of males: {male}")
print(f"Number of females: {female}")


f.close()
