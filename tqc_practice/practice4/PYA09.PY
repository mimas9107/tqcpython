#907
filename=input()
f=open(filename,'r')
print(f"{len(f.readlines())} line(s)")
f.seek(0)
print(f"{len(f.read().split())} word(s)")
f.seek(0)
c=f.read().replace('\n','').replace(' ','')
print(f"{len(c)} character(s)")
f.close()