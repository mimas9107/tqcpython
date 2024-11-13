# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:15:37 2024

Python 204 算術運算
題目說明：¶
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。
"""

a=eval(input())
b=eval(input())

op=input()

if(op == '+'):
    print(f"{a+b}")

if(op == '-'):
    print(f"{a-b}")

if(op == '*'):
    print(f"{a*b}")

if(op == '/'):
    print(f"{a/b}")

if(op == '//'):
    print(f"{a//b}")

if(op == '%'):
    print(f"{a%b}")