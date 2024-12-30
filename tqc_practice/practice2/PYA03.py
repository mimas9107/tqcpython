#310
n=eval(input())
total=0
for i in range(2,n+1):
    # print(i)
    total+=1/((i-1)**0.5+(i)**0.5)
print(f"{total:.4f}")