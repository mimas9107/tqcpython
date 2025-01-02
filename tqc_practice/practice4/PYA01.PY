#110
n=eval(input())
s=eval(input())

import math

Area=(n*s**2)/(4*math.tan(math.pi/n))

print(f"Area = {Area:.4f}")