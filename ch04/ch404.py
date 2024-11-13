# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:25:50 2024

@author: user
"""

n = eval(input())
if(n!=0):
    m=n
    while(m!=0):
        finaldigit = str(m%10)
        print(finaldigit,end='')
        m=m//10
    # print()
else:
    print(0)