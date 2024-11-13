# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:03:03 2024

@author: #08 劉志文
"""
#02 歐式距離計算

x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
dx=(x1-x2)
dy=(y1-y2)
dist=(dx*dx+dy*dy)**0.5

print(f"( {x1} , {y1} )")
print(f"( {x2} , {y2} )")
print(f"Distance = {dist:.4f}")