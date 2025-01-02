#605
L=[eval(input()) for i in range(10)]
MAX=max(L)
MIN=min(L)

L.remove(MAX)

L.remove(MIN)
print(sum(L))
print(f"{sum(L)/len(L):.2f}")