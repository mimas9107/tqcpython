filename=input()
f=open(filename,'r',encoding='utf-8')
buf=f.readlines()
print(f"{len(buf)} line(s)") # number of lines
f.seek(0)
buf=f.read()
buf=buf.replace('\n',' ').split()
print(f"{len(buf)} word(s)") # number of words
f.seek(0)
buf=f.read()
c=0
c=len(buf.replace('\n',' ').replace(' ',''))
    
print(f"{c} character(s)")
f.close()
