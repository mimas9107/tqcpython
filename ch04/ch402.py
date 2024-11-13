# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:02:34 2024

@author: user
"""
numbers=[]
n=0
while(n != 9999):
    n=eval(input())
    ## 9999 不能被 append到 list中:
    if(n !=9999):
        numbers.append(n)
    else:
        #break
        pass
    print("這時的清單:",numbers)
print(min(numbers))
        