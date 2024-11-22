# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:11:19 2024

第3類測驗, 第1題 存款本利和以複利計算問題.
balance=money
balance=balance(1+rate)^unittime

@author: #08 劉志文
"""
money=eval(input()) ## 本金
yearrate=eval(input()) ## 年利率
month=eval(input()) ## 期數(月)

balance=money

print("Month \t  Amount") ## 表格 header
for i in range(month):
    balance=balance*(1+yearrate/1200)


    print(f"{i+1:>3d} \t {balance:.2f}")
    

