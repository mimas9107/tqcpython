#307

n=eval(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{j:<2d}* {i:<2d}= {j*i:<4d}", end='', sep='')
    print()
    