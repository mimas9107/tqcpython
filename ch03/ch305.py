# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:50:54 2024

Python 305 數字反轉
題目說明：¶
請撰寫一程式，讓使用者輸入一個正整數，將此數值以反轉的順序輸出。
"""

num=input()

## solution1
print(num[::-1])

## solution2
for i in range(len(num)-1, -1, -1):
    print(num[i],end='')
print()    

## solution3
print(''.join([num[i] for i in range(len(num)-1, -1, -1)]))