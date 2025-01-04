#110  
import math
n=eval(input())
s=eval(input())
area=s**2*n/(4*math.tan(math.pi/n))
print(f"Area = {area:.4f}")