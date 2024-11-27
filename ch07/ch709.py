color_dict={}

k=' '
while(k!='end'):
    k=input("Key: ")
    if(k=='end'): break
    v=input("Value: ")

    color_dict[k]=v

for e in sorted(color_dict):
    print(f"{e}: {color_dict[e]}")
    