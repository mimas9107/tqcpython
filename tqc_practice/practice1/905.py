#filename='data.txt'
filename=input()

s=input()
print("=== Before the deletion")
f=open(filename,'r')
buf=f.read()
print(buf)
f.close()

print("=== After the deletion")
buf=buf.replace(s,"")

f=open(filename, 'w+')
f.write(buf)
f.seek(0)
buf=f.read()
print(buf)

f.close()