#902

filename='read.txt'
f=open(filename,'r')
buf=f.read()
buf=buf.replace('\n','').split(' ')
# print(buf)
print(sum([eval(e) for e in buf]))



f.close()
