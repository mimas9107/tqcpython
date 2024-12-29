L=[eval(input()) for i in range(9)]

MAX=max(L)
MIN=min(L)
#0 1 2 (0,0) (0,1) (0,2)
#3 4 5 (1,0) (1,1) (1,2)
#6 7 8 (2,0) (2,1) (2,2)
print(f"Index of the largest number {MAX} is: ({L.index(MAX)//3}, {L.index(MAX)%3})")
print(f"Index of the smallest number {MIN} is: ({L.index(MIN)//3}, {L.index(MIN)%3})")