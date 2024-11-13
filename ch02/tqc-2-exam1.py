# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:00:10 2024

@author: #08 劉志文
第2類題目1
"""

price=eval(input())

discount=1 #折扣

if(price>=38000): #>38000
    discount=0.7
elif(price>=28000): #28000~37999
    discount=0.8
elif(price>=18000): #18000~27999
    discount=0.9
elif(price>=8000): #8000~17999
    discount=0.95
else:
    # 7999~0
    pass 

print(f"{discount * price}")
