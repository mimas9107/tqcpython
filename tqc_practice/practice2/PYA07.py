#709
k=" "
d=dict()
while(k!="end"):
    k=input("Key: ")
    if(k == "end"): break
    v=input("Value: ")
    d[k]=v

s=input("Search key: ")
print(s in d.keys())