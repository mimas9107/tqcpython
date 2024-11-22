# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:30:52 2024

@author: user
"""

def compute(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        f0=0
        f1=1
        for i in range(2,n+1):
            tmp=f0+f1
            f0=f1
            f1=tmp
            print(i, tmp)


print(compute(0))            
print(compute(1))
print(compute(2))
print(compute(3))
print(compute(5))
print(compute(10))
        
    
    