#408
L=[eval(input()) for i in range(10)]
even=0
odd=0
for i in L:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")