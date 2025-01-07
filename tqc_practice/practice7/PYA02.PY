#210
a=eval(input())
b=eval(input())
c=eval(input())

if(a+b>c):
    if(b+c>a):
        if(a+c>b):
            print(f"{a+b+c}")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")