# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:35:49 2024

@author: #08 Justin Liu
TQC+第六類考試第一題
"""

L=[eval(input()) for i in range(9)]
# L=[6,4,8,39,12,3,-3,49,33]
Max=max(L)
Min=min(L)

# index
# 0 1 2 (0,0) (0,1) (0,2)
# 3 4 5 (1,0) (1,1) (1,2)
# 6 7 8 (2,0) (2,1) (2,2)

Max_i=L.index(Max)
Min_i=L.index(Min)
# print(Max_i//3, Max_i%3)
# print(Min_i//3, Min_i%3)
print(f"Index of the largest number {Max} is: ({Max_i//3}, {Max_i%3})")
print(f"Index of the smallest number {Min} is: ({Min_i//3}, {Min_i%3})")
