# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:59:55 2024

Python 202 倍數判斷
題目說明：¶
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是3或5的倍數，顯示【x is a multiple of 3.】或【x is a multiple of 5.】；若此數值同時為3與5的倍數，顯示【x is a multiple of 3 and 5.】；如此數值皆不屬於3或5的倍數，顯示【x is not a multiple of 3 or 5.】，將使用者輸入的數值代入x。
"""

number = eval(input())

if((number%3 ==0) or (number%5 ==0)):
    if(number%3 ==0):
        if(number%5 ==0):
            print("x is multiple of 3 and 5")
        else:
            print("x is multiple of 3.")
    else:
        print("x is multiple of 5.")
else:
    print("x is not a multiplt of 3 or 5")