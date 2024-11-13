# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:00:54 2024

@author: user
"""

money=eval(input())

yearrate=eval(input())

n_month=eval(input())

##第0期的本金
balance=money 

print("Month \t  Amount") ##<= 老師的解答格式, codejudger還是錯?
# print("{}\t {}".format('Month','Amount')) ##<= 我自己調的

for i in range(1,n_month+1):

    ##第1~n期 複利計算, 當期的本利和是下期的本金.
    balance=balance*(1+yearrate/1200)
    print("{:>3d} \t {:.2f}".format(i,balance))
    # print("{:>3d}\t\t{:.2f}".format(i,balance)) ##<= 我自己調的
    
    
## 表格標題 \t 間隔會影響數空格, 輸出會被誤導... 太機車了!