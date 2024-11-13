# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:14:45 2024

Python 201 偶數判斷
題目說明：¶
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）。
"""

number=eval(input())

if(number%2 == 0):
    print(f"{number} is an even number.")
else:
    print(f"{number} is not an even number.")