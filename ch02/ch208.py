# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:08:54 2024

Python 208 十進位換算
題目說明：¶
請使用選擇敘述撰寫一程式，讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，將num轉換成十六進位值。
"""

number=int(input())

if(number<10):
    print(number)
elif(number==10):
    print("A")
elif(number==11):
    print("B")
elif(number==12):
    print("C")
elif(number==13):
    print("D")
elif(number==14):
    print("E")
elif(number==15):
    print("F")
