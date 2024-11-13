# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:30:06 2024

@author: user
"""
numbers=[]
for i in range(10):
    numbers.append(eval(input()))
## 偏偏任性不用 min():    
min=999999999999999999999999999999999999999
for i in numbers:
    if(i<min):
        min=i

print(min)