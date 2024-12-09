# matrix=[eval(input()) for i in range(9)]
matrix=[6,4,8,39,12,3,-3,49,33]

imax=matrix.index(max(matrix))
imin=matrix.index(min(matrix))

# print(imax,imin)

# matrix:
# 0 1 2 => (0,0) (0,1) (0,2)
# 3 4 5 => (1,0) (1,1) (1,2)
# 6 7 8 => (2,0) (2,1) (2,2)

print(f"Index of the largest number {max(matrix)} is: ({imax//3}, {imax % 3})")
print(f"Index of the smallest number {min(matrix)} is: ({imin//3}, {imin % 3})")