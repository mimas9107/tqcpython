# -*- coding: utf-8 -*-
"""
904
題目說明：¶
請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。
"""
file=open("read.txt", "r")

N=[]
H=[]
W=[]

# print(file.read())
for e in file.readlines():
    print(e)
    data=e.split()
    N.append(data[0])
    H.append(int(data[1]))
    W.append(int(data[2]))

# print(N)
# print(H)
# print(W)

print(f"Average height: {sum(H)/3:.2f}")
print(f"Average weight: {sum(W)/3:.2f}")
print(f"The tallest is {N[H.index(max(H))]} with {max(H):.2f}cm")
print(f"The heaviest is {N[W.index(max(W))]} with {max(W):.2f}kg")
file.close()
