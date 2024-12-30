#901
filename='write.txt'
f=open(filename,'w')
for i in range(5):
    buf=input()
    f.write(buf+'\n')
f.close()
