s=input()
total=0
for i in s:
    print(f"ASCII code for '{i}' is {ord(i)}")
    total+=ord(i)
print(total)