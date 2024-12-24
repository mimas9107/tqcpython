filename='data.dat'

f=open(filename,'w+')
for i in range(5):
    buf=input()
    # buf=buf.split(' ')
    f.write(buf+'\n')

f.close()

f=open(filename,'r')
print("The content of \"data.dat\":")
# buf=f.read()
# print(buf)
for e in f:
    print(e)

f.close()