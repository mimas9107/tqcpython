filename=input()
num=eval(input())

f=open(filename,'r')

buf=f.read()

buf=buf.replace('\n',' ').split(' ')[:-1]
#print(buf)
L=set()
for e in buf:
    if buf.count(e) == num:
        L.add(e)

#print(sorted(L))
for e in sorted(L):
    print(e)

f.close()

