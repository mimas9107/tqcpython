# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 08:04:39 2024

@author: #08 劉志文
tqc python 5 exam1
"""
import math

def compute(p,q):
    return math.gcd(p,q)
    

x,y=eval(input())
m,n=eval(input())


p=x*n+m*y
q=n*y

t=compute(p,q)
print(f'{x}/{y} + {m}/{n} = {int(p/t)}/{int(q/t)}')


