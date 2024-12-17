# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:09:18 2024

@author: #08 Justin
"""

d1=dict()
d2=dict()

print("Create dict1:")
while(True):
    k=input("Key: ")
    if k=='end': break
    v=input("Value: ")
    d1[k]=v

print("Create dict2:")
while(True):
    k=input("Key: ")
    if k=='end': break
    v=input("Value: ")
    d2[k]=v
    
d1.update(d2)

for e in sorted(d1):
    print(f"{e}: {d1[e]}")