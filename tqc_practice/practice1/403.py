a=eval(input())
b=eval(input())
total=0
n=1
for i in range(a,b+1):
    
    if i%4==0 or i%9==0 :
        total+=i
        print(f"{i:<4d}",end='')
        if n%10==0:
            print()
        n+=1
else:
    print()
print(n-1)
print(total)

#=====================
l=[]
total=0
for i in range(a,b+1):
    if(i%4==0) or (i%9==0):
       total+=i
       l.append(i)

for idx,e in enumerate(l):
    print(f"{e:<4d}",end='')
    if((idx+1)%10==0): print()
print()
print(len(l))
print(total)