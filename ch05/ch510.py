# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:30:52 2024

@author: user
"""
def compute2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    if n>1:
        return compute2(n-1)+compute2(n-2)
    
    
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
            # print(i, tmp)
        return tmp
n=eval(input())
for i in range(n): 
    print(compute2(i),end=' ')
        
    
    