#509
import math
x,y=eval(input())
m,n=eval(input())

#x/y+m/n=p/q
#p=xn+my
#q=ny

p=x*n+m*y
q=n*y

def compute(p,q):
    return math.gcd(p,q)

print(f"{x}/{y} + {m}/{n} = {int(p/compute(p,q))}/{int(q/compute(p,q))}")