# -*- coding: utf-8 -*-
# simu02 #07

s1=set()
s2=set()
s3=set()

print("Input to set1:")
for i in range(5):
    s1.add(eval(input()))
    
print("Input to set2:")
for i in range(3):
    s2.add(eval(input()))
    
print("Input to set3:")
for i in range(9):
    s3.add(eval(input()))

print(f"set2 is subset of set1: {s2.issubset(s1)}")
print(f"set3 is superset of set1: {s3.issuperset(s1)}")