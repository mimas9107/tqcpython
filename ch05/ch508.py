# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:41:07 2024

@author: user
"""

 
## solution1 用內建方法 math.gcd
# import math
# def compute(x,y):
#     return math.gcd(x,y)

## solution2 自己寫演算法
def compute(x,y):
    while(y!=0):
        x,y=y,x%y
    return x

## 輸入用 tuple方式輸入:
(n1,n2)=eval(input())
## 輸出:
print(compute(n1,n2))