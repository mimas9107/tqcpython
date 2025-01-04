#910
filename='read.dat'
female=0
male=0
f=open(filename,'r',encoding='utf-8')
buf=f.readlines()
for e in buf:
    print(e)
    if e.split()[2] == '0':
        female+=1
    elif e.split()[2] == '1':
        male+=1
print(f"Number of males: {male}")
print(f"Number of females: {female}")

f.close()