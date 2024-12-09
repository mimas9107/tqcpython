filename=input()
lines=0
words=0
chars=0

f=open(filename,'r')
buf=f.read()

buf=buf.split('\n')[:-1] ## 取到最後一個元素(不含)之前:相當於將尾端的 ""捨棄掉.
lines=len(buf) ##有幾個換行
print(lines,"lines(s)")

buf2 = [e.strip('\n') for e in buf]
# print(buf2)
buf3=[]
for e in buf2:
    for i in e.split(' '):
        buf3.append(i)
# print(buf3)
print(len(buf3),'word(s)')

for e in buf3:
    chars+=len(e)

print(chars, 'character(s)')

f.close()