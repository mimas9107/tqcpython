#904

# print(sys.path[0])
n=[]
h=[]
w=[]
filename='read.txt'
f=open(filename,'r')
buf=f.readlines()

for e in buf:
    print(e)
    n.append(e.split()[0])
    h.append(eval(e.split()[1]))
    w.append(eval(e.split()[2]))

print(f"Average height: {sum(h)/len(h):.2f}")
print(f"Average weight: {sum(w)/len(w):.2f}")

print(f"The tallest is {n[h.index(max(h))]} with {max(h):.2f}cm")
print(f"The heaviest is {n[w.index(max(w))]} with {max(w):.2f}kg")


f.close()