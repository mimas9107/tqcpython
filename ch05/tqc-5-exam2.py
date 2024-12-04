# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:07:51 2024

@author: #08 劉志文
tqc python 5 exam2
"""

n=eval(input())

def compute(x):
    if x==0:
        print("Not Prime")
        return
    if x==1:
        print("Not Prime")
        return
    if x<0:
        print("Not Prime")
        return
    if x>=2:
        for i in range(2,x):
            if x%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")
        

compute(n)