# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:20:23 2024

@author: user
"""

"""
110
"""

import math
n=eval(input())
s=eval(input())
Area=(n*s**2)/(4*math.tan(math.pi/n))
print("Area = {:.4f}".format(Area))