scores=[eval(input()) for e in range(10)]
# scores=[89,78,67,80,75,98,77,89,76,60]
minscore=min(scores)
maxscore=max(scores)
scores.remove(minscore)
scores.remove(maxscore)
# print(scores)
# print(minscore)
# print(maxscore)
print(sum(scores))
print(f"{sum(scores)/(len(scores)):.2f}")