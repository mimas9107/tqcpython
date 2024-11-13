# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:19:30 2024

@author: user
"""

n=eval(input())

total=0
## 題目雖然是 n>1 但難保 check answer時會不會餵邊界條件 n=1:
if(n>1): 
    for i in range(2,n+1):
        total += (1/((i-1)**0.5+(i)**0.5))
else:
    total=1
print(f"{total:.4f}")