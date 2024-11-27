filewrite='write.txt'
f=open(filewrite,"w+")
for u in range(5):
    s = input()
    f.write(s+'\n')

f.close()