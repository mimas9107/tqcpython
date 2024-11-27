## 807 字串加總
s=input()
total=0

total = sum([int(e) for e in s.split(" ")])
Average = total/5

print(f"Total = {total}")
print(f"Average = {Average}")