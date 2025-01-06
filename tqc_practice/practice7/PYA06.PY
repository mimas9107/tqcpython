#605
scores=[eval(input()) for i in range(10)]
MAX=max(scores)
MIN=min(scores)

scores.remove(MAX)
scores.remove(MIN)
total=sum(scores)
avg=total/len(scores)
print(f"{total}")
print(f"{avg:.2f}")