# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:42:00 2024

@author: user
"""

def compute(number):
    if number <2: return False
    
    i=2
    while(i<number):
        if(number%i==0):
            return False        
        i+=1
    
    return True

a=eval(input())
if((a==0) | (a==1)):
    print("Not Prime")
elif(compute(a)):
    print("Prime")
else:
    print("Not Prime")
        