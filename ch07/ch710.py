dicts={}

k=' '
while(k!='end'):
    k=input("Key: ")
    if(k=='end'): break

    v=input("Value: ")

    dicts[k]=v

searchkey=input("Search key: ")

print(searchkey in dicts.keys())