lst=[]
buf=-9999999999999999
while(buf != -9999):

    buf=eval(input())
    if buf==-9999:
        break
    lst.append(buf)


print(tuple(lst))
print(f"Length: {len(lst)}")
print(f"Max: {max(lst)}")
print(f"Min: {min(lst)}")
print(f"Sum: {sum(lst)}")