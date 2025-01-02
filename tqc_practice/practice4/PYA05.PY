#510
def compute(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        
        return compute(num-1)+compute(num-2)


n=eval(input())
for i in range(n):
    print(f"{compute(i)} ", end='')