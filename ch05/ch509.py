# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:18:51 2024

@author: user
"""

import math

def compute(a,b):
    return math.gcd(a,b)
    
x,y=eval(input())
m,n=eval(input())

p=n*x+m*y
q=n*y
t=compute(p,q)
p=int(p/t)
q=int(q/t)
    
print(f"{x}/{y} + {m}/{n} = {p}/{q}")