# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:22:13 2024

@author: user
"""

def compute(a,x,y):
    tmp=(a+" ")*x
    for i in range(y):
        print(tmp)



aa=input()
xx=eval(input())
yy=eval(input())
compute(aa,xx,yy)
