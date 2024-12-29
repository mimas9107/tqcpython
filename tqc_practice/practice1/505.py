a=input()
x=eval(input()) ## repeat col
y=eval(input()) ## repeat row
def compute(a,x,y):
    for r in range(y):
        print((a+" ")*x )
compute(a,x,y)
