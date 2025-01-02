#703
L=[]
while(True):
    buf=input()
    if(buf=='end'): break
    L.append(buf)
print(tuple(L))
print(tuple(L[0:3]))
print(tuple(L[-3::]))