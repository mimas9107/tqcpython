k = eval(input())
for i in range(k):
    s = input()
    L =[eval(e) for e in s.split(" ")]
    print(f"{max(L) - min(L):.2f}")
