dicts=[{},{}]


for dd in range(2):
    bufkey=' '
    bufvalue=' '
    print(f"Create dict{dd+1}:")
    while(bufkey!='end'):
        
        bufkey=input("Key: ")
        if(bufkey=='end'): break
        
        bufvalue=input("Value: ")
        if(bufvalue=='end'): break
        
        dicts[dd][bufkey]=bufvalue
      
# print(dicts[0])
# print(dicts[1])

# dicts[0] 將 dicts[1]合併進來
dicts[0].update(dicts[1])
# 遍歷已經排好序的 keys:
for k in sorted(dicts[0]):
    print(f"{k}: {dicts[0][k]}")
