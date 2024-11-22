# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:03:01 2024

第3類測驗, 第二題 數字反轉

@author: #08 劉志文
"""

#solution1 python小白 不知道有可以用時:
num=input()
length=len(num)
for i in range(length-1,-1,-1):
    print(num[i],sep='',end='')