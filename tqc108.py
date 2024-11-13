# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:03:20 2024

@author: user
"""

"""
108
"""
x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())

dx=x1-x2
dy=y1-y2
dis=(dx*dx+dy*dy)**0.5

print("( {} , {} )".format(x1,y1))
print("( {} , {} )".format(x2,y2))
print("Distance = {:.4f}".format(dis))
