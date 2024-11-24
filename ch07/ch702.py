

L=[[] for i in range(2)]
# L=[ [9,0,-1,3,8],[28,16,39,56,78,88] ]
for i in range(2):
    print(f"Create tuple{i+1}:")
    e=-9998
    while(e!=-9999):
        e=eval(input())
        if(e==-9999):
            break
        L[i].append(e)

# print(L)
t=tuple(L[0])+tuple(L[1])
print(f"Combined tuple before sorting: {t}")
s=sorted(t)
print(f"Combined list after sorting: {s}")
