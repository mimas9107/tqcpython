# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:41:07 2024

@author: user
"""

## GCD 
## solution1
# import math
# def compute(x,y):
#     return math.gcd(x,y)

## solution2
def compute(x,y):
    while(y!=0):
        x,y=y,x%y
    return x

(n1,n2)=eval(input())
print(compute(n1,n2))