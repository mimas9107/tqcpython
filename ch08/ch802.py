## 802 字元對應

s=input()
total=0
for e in s:
    print(f"ASCII code for '{e}' is {ord(e)}")
    total+=ord(e)
print(total)