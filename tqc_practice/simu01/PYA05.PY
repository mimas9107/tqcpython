# -*- coding: utf-8 -*-
#simu01 #05

a=eval(input())
b=eval(input())
c=eval(input())

det=b**2-4*a*c
r1=(-b-det**0.5)/(2*a)
r2=(-b+det**0.5)/(2*a)
if(det<0.0):
    print("Your equation has no root.")
elif(det==0):
    
    if(r1==r2):
        print(f"{r1}")
elif(det>0):
    if(r1<r2):
        print(f"{r1}, {r2}")
    else:
        print(f"{r2}, {r1}")