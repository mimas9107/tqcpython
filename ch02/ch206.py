# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:36:49 2024

Python 206 等級判斷
題目說明：¶
請使用選擇敘述撰寫一程式，根據使用者輸入的分數顯示對應的等級。標準如下表所示：
分 數	等級
80 ~ 100	A
70 ~ 79	B
60 ~ 69	C
<= 59	F
"""

score=eval(input())

if(score<60):
    print("F")
elif(score<70):
    print("C")
elif(score<80):
    print("B")
elif(score<=100):
    print("A")