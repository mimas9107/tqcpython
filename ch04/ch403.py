# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:09:11 2024

@author: user
"""

a=eval(input())
b=eval(input())

crlf=0
count=0
total=0
for i in range(a,b+1):
    if((i%4 == 0) or (i%9 == 0)):
        count+=1 
        total+=i
        if(count % 11 == 0): print()
        print(f'{i:<4d}',end='')
print()

print(count)
print(total)
