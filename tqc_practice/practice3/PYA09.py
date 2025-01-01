#903

filename='data.txt'
f=open(filename,'a+')

for i in range(5):
    buf=input()
    f.write('\n'+buf)
print("Append completed!")
print("Content of \"data.txt\":")
f.seek(0)
buf=f.read()
print(buf)

f.close()
