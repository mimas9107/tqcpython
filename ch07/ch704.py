S=set()
n=-99999
while(n!=-9999):
    n=eval(input())
    if(n==-9999):break
    S.add(n)

print(f"Length: {len(S)}")
print(f"Max: {max(S)}")
print(f"Min: {min(S)}")
print(f"Sum: {sum(S)}")