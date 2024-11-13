# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:30:47 2024

@author: user
"""

a="""What is Python language
Python is a widely used high level general purpose interpreted dynamic programming language
Its design philosophy emphasizes code readability and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C or Java
Python supports multiple programming paradigms including object oriented imperative and functional programming or procedural styles
It features a dynamic type system and automatic memory management and has a large and comprehensive standard library
The best way we learn anything is by practice and exercise questions We have started this section for those beginner to intermediate who are familiar with Python
"""
file=input()
fopen=open(file,'r')

# 讀檔案存 buf字串
buf=fopen.read()
ddd={}
# print(a.split())

# buf字串用 split(" ")空白拆成 list
# 走一次 list, 放到字典中, 沒出現過就加入然後數字初始為1, 有出現的字的次數再加1
for e in buf.split(" "):
    if(e in ddd.keys()):
       ddd[e]+=1
    else:
        ddd[e]=1

# 走一次 "排過序"的 keys清單
# 其值為 3的就把 key印出
for v in sorted(ddd.keys()):
    if ddd[v] == 3:
        print(v)
# 關檔案 結束這題
fopen.close