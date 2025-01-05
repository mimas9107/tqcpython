#604
L=[]
#34 18 22 32 18 29 30 38 42 18
d=dict()

for i in range(10):
    L.append(eval(input()))
    if L[i] not in d:
        d[L[i]]=1
    else:
        d[L[i]]+=1

MAX_v=-1
MAX_k=-1
for k,v in d.items():

    if v > MAX_v:
        MAX_v=v
        MAX_k=k
print(MAX_k)
print(MAX_v)