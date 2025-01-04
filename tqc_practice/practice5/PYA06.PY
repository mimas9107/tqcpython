#603
L=[eval(input()) for i in range(10)]

print(f"{sorted(L, reverse=True)[0]} {sorted(L, reverse=True)[1]} {sorted(L, reverse=True)[2]}")