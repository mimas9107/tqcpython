#403
a=eval(input())
b=eval(input())
L=[]
for e in range(a,b+1):
    if(e%4==0 or e%9==0):
        L.append(e)

for i,e in enumerate(L):
    print(f"{e:<4d}",end='',sep='')
    if((i+1)%10==0):
        print()
print()
print(i+1)
print(sum(L))
