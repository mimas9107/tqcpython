# filename='data.txt'
filename=input()
s1:str=input()
s2:str=input()
f=open(filename,"r")
buf=f.read()
print("=== Before the replacement")
print(buf)
buf=buf.replace(s1,s2)
print("=== After the replacement")
print(buf)
f.close()

f=open(filename,'w')
f.write(buf)
f.close()

