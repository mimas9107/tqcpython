filename:str=input()
s:str=input()

f=open(filename,'r')
bufs=f.readlines()

newbufs=[]
print("=== Before the deletion")
for e in bufs:
    print(e.strip('\n'))

for e in bufs:
    
    if(s in e):
        newbufs.append(e.replace(s,"").strip('\n'))
    else:
        newbufs.append(e.strip('\n'))
    # print(newbufs)

f.close()
print()
print("=== After the deletion")
ff=open(filename,'w')
for e in newbufs:
    ff.write(e+'\n')
    print(e)
ff.close()