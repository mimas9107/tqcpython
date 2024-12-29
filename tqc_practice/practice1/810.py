k=eval(input())

for i in range(k):
    num=input()
    L=[eval(e) for e in num.split()]
    print(f"{max(L)-min(L):.2f}")