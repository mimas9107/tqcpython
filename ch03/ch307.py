# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:48:15 2024

@author: user
"""

n = eval(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{j:<2d}* {i:<2d}= {i*j:<4d}", end='')
    print()