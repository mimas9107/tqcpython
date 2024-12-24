# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:27:26 2024

@author: user
"""

def findroot(a,b,c):
    det=(b**2-4*a*c)
    if det<0:
        print("Your equation has no root.")
    elif det==0:
        root1=(-b+(det)**0.5)/(2*a)
        root2=(-b-(det)**0.5)/(2*a)
    
        print(f"{root1}")
    else:
        root1=(-b+(det)**0.5)/(2*a)
        root2=(-b-(det)**0.5)/(2*a)
    
        print(f"{root1}, {root2}")
    
aa=eval(input())
bb=eval(input())
cc=eval(input())

findroot(aa,bb,cc)