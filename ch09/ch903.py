filename='data.txt'
f=open(filename,"a+")

for i in range(5):
    name=input()
    f.write(name+'\n')
print("Append completed!")
f.close()

print(f"Content of \"{filename}\":")
ff=open(filename,'r')
buf=ff.read()
print(buf)
ff.close()
