# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:51:02 2024

@author: user
"""

count=eval(input())

for j in range(count):
    total=0
    num=input()
    for k in range(len(num)):
        total+=int(num[k])
    print(f"Sum of all digits of {num} is {total}")
