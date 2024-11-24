# L=['president','dean','chair','staff','teacher','student']
L=[]
c=' '
while(c!='end'):
    c=input()
    if(c=='end'): break

    L.append(c)

print(tuple(L))
print(tuple(L[:3]))
print(tuple(L[-3:]))
