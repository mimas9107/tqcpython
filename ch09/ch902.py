fileread='read.txt'

f=open(fileread,'r')
buf = f.read()
L=[eval(e) for e in buf.split(" ")]
print(sum(L))