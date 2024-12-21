filename='read.dat'
f=open(filename,'r')
buf=f.readlines()
for e in buf:
    print(e)
#print(buf)
male=0
female=0
for e in buf:
    tmp=e.split()
    if tmp[2] == '0':
       female+=1
    elif tmp[2] == '1':
        male+=1

print(f"Number of males: {male}")
print(f"Number of females: {female}")


f.close()
