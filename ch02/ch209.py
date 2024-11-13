# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:46:23 2024

Python 209 距離判斷
請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，判斷此點是否與點(5, 6)的距離小於或等於15，如距離小於或等於15顯示【Inside】，反之顯示【Outside】。
"""

x1=eval(input())
y1=eval(input())

dis=( (x1-5)**2 + (y1-6)**2 )**0.5

if(dis <= 15):
    print("Inside")
else:
    print("Outside")