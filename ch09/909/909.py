filename='data.dat'
f=open(filename,'w')
for i in range(5):
    buf=input()
    f.write(buf+'\n')
f.close()

f=open(filename,'r')
print('The content of "data.dat":')
buf=f.readlines()
for e in buf:
    print(e)


f.close()
