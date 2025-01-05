#710
d=dict()
while(True):
    buf=input('Key: ')
    if buf=='end': break
    v=input('Value: ')
    d[buf]=v

s=input('Search key: ')
print(s in d.keys())