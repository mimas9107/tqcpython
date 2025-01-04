#506
a=eval(input())
b=eval(input())
c=eval(input())

def compute(a,b,c):
    det=b*b-4*a*c
    if det < 0:
        print("Your equation has no root.")
    elif det == 0.0:
        root=(-b+det**0.5)/(2*a)
        print(root)
    else:
        r1=(-b+det**0.5)/(2*a)
        r2=(-b-det**0.5)/(2*a)
        print(f"{r1}, {r2}")

compute(a,b,c)