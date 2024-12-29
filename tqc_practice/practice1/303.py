n=eval(input())

for i in range(n+1):
    for j in range(i):
        print(f"{i*(j+1):>4d}", end='')
    print()