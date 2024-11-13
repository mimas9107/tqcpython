# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:22:53 2024

Python 205 字元判斷
題目說明：¶
請使用選擇敘述撰寫一程式，
讓使用者輸入一個字元，
判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。

例如：a為英文字母、9為數字、$為其它字元。
"""
c=input() ## 1個字元

## 霸氣的寫法 XD
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['1','2','3','4','5','6','7','8','9','0']

if ((c not in alphabet) and (c not in number)):
    print(f"{c} is a symbol.")
else:
    if(c in alphabet):
        print(f"{c} is a alphabet.")
    else:
        print(f"{c} is a number.")

## 其實需要用 isdigit() 和 isalpha()
