data=[input() for i in range(5)]
filename='data.dat'
f=open(filename,'w+')
for e in data:
    f.write(e+'\n')
f.close()
print("The content of \"data.dat\":")
f=open(filename,'r')
for e in f:
    print(e)