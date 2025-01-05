#807
buf=input()

L=[eval(e) for e in buf.split()]
total=sum(L)
print(f"Total = {total}")
print(f"Average = {total/len(L)}")    