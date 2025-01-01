#610
L=[]
for w in range(1,5):
    print(f"Week {w}:")
    for d in range(1,4):
        L.append(eval(input(f"Day {d}:")))
High=max(L)
Low=min(L)
average=sum(L)/(len(L))
print(f"Average: {average:.2f}")
print(f"Highest: {High}")
print(f"Lowest: {Low}")
