# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:39:29 2024

Python 207 折扣方案
題目說明：¶
請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於8,000（含）以上，並顯示折扣優惠後的實付金額。購物金額折扣方案如下表所示：
金  額	折 扣
8,000（含）以上	9.5折
18,000（含）以上	9折
28,000（含）以上	8折
38,000（含）以上	7折
"""
price=eval(input())
discount=1
if(price >=38000):
    discount=0.7
elif (price >=28000):
    discount=0.8
elif (price >=18000):
    discount=0.9
elif (price >=8000):
    discount=0.95
    
print(f"{discount*price}")

