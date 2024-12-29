a=eval(input())
b=eval(input())

t=0
total=0
for i in range(a,b+1):
    if((i%4==0) or (i%9==0)):
        print(f"{i:<4d}", end='')
        t+=1
        # print("t=",t)
        total+=i
        if t%10==0:
            print()
print()
print(t)
print(total)