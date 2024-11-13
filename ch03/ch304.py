# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:10:34 2024

@author: user
"""

num = eval(input())

total=0
for i in range(1,num+1):
    if(i%5==0):
        total+=i
print(total)