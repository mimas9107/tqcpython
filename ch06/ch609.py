M1=[[0 for c in range(2)] for r in range(2)]
print(f"Enter matrix 1:")
for i in range(2):
    for j in range(2):
        print(f"[{i+1}, {j+1}]: ",end='')
        
        M1[i][j]=eval(input())

##print(M1)
print(f"Enter matrix 2:")
M2=[[0 for c in range(2)] for r in range(2)]
for i in range(2):
    for j in range(2):
        print(f"[{i+1}, {j+1}]: ",end='')
        
        M2[i][j]=eval(input())

print("Matrix 1:")
for i in range(2):
    for j in range(2):
        print(f"{M1[i][j]} ",sep='',end='')
    print()

print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print(f"{M2[i][j]} ",sep='',end='')
    print()

print("Sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        print(f"{M1[i][j]+M2[i][j]} ",sep='',end='')
    print()