# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:45:45 2024

@author: #08 Justin Liu
TQC+第六類考試第二題
"""

m1=[[0,0],
    [0,0]]

m2=[[0,0],
    [0,0]]

msum=[[0,0],
      [0,0]]

print("Enter matrix 1:")
for i in range(2):
    for j in range(2):
        print(f"[{i+1}, {j+1}]: ",end='')
        m1[i][j]=eval(input())

print("Enter matrix 2:")
for i in range(2):
    for j in range(2):
        print(f"[{i+1}, {j+1}]: ",end='')
        m2[i][j]=eval(input())

print("Matrix 1:")
for i in range(2):
    for j in range(2):
        print(f"{m1[i][j]} ", end='')
    print()

print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print(f"{m2[i][j]} ", end='')
    print()
    
print("Sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        msum[i][j]=m1[i][j]+m2[i][j]
        print(f"{msum[i][j]} ",end='')
    print()
    