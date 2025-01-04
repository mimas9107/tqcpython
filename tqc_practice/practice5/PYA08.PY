#807
buf=input()

L=[eval(e) for e in buf.split()]
total=sum(L)
print(total/len(L))    