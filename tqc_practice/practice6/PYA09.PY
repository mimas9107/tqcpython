#908
filename=input()
n=eval(input())
f=open(filename,'r')
buf=f.read()
buf=buf.replace('\n',' ').split(' ')
print(buf)
tmp=[]
for e in buf:
    if buf.count(e) == 3:
        tmp.append(e)
        # print(e)
for e in sorted(set(tmp)):
    print(e)

f.close()