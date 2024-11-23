lst=[]
for w in range(1,5):
    print(f"Week {w}:")
    for d in range(1,4):
        print(f"Day {d}:",end='')
        lst.append(eval(input()))
average=sum(lst)/len(lst)
highest=max(lst)
lowest=min(lst)

print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")