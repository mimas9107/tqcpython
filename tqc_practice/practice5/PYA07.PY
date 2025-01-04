#704
S=set()
buf=0
while(True):
    buf=eval(input())
    if(buf==-9999):break
    S.add(buf)
print(f"length: {len(S)}")
print(f"Max: {max(S)}")
print(f"Min: {min(S)}")
print(f"Sum: {sum(S)}")