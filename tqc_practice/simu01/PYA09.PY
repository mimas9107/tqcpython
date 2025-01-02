# -*- coding: utf-8 -*-
#simu01 #09

filename='read.txt'
n=[]
h=[]
w=[]

f=open(filename,'r')

buf=f.readlines()
for i in range(len(buf)):
    print(buf[i])

for e in buf:
    
    n.append(e.strip('\n').split()[0])
    h.append(eval(e.strip('\n').split()[1]))
    w.append(eval(e.strip('\n').split()[2]))

print(f'Average height: {sum(h)/len(h):.2f}')

print(f"Average weight: {sum(w)/len(w):.2f}")

print(f"The tallest is {n[h.index(max(h))]} with {max(h):.2f}cm")

print(f"The heaviest is {n[w.index(max(w))]} with {max(w):.2f}kg")


f.close()