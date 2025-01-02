# -*- coding: utf-8 -*-
# SIMU01 #01
import math
n=eval(input()) # n個邊
s=eval(input()) # 邊長

Area=(n*s**2)/(4*math.tan(math.pi/n))

print(f"Area = {Area:.4f}")