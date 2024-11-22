# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:13:12 2024

@author: user
"""

def sigma(a,b):
    total=0
    for i in range(a,b+1):
        total+=i
    return total

aa=eval(input())
bb=eval(input())

print(sigma(aa,bb))