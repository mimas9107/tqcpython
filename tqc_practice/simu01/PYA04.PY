# -*- coding: utf-8 -*-
#SIMU01 #04

L=[eval(input()) for i in range(10)]

even=0
odd=0

for e in L:
    if(e%2==0):
        even+=1
    else:
        odd+=1
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")