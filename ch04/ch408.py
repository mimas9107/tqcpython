odd=0
even=0
L=[]
for i in range(10):
    L.append(eval(input()))
    if(L[i]%2==0):
        even+=1
    else:
        odd+=1

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
