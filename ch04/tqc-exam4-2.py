# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 08:09:59 2024

@author: #08 劉志文
"""
## 第4第2題

n=-9998
while(n!=-9999):
    n=eval(input())
    if(n==-9999):break
    
    if(n<60):
        print('E')
    elif(n<70):
        print('D')
    elif(n<80):
        print('C')
    elif(n<90):
        print('B')
    elif(n<=100):
        print('A')