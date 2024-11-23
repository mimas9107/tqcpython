
def compute(r,c):
    for i in range(rows):
        for j in range(cols):
            print(f"{j-i:4d}",sep='',end='')
        print()

rows=eval(input())
cols=eval(input())
compute(rows,cols)
