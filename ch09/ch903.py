filename='data.dat'
f=open(filename,"a+")

for i in range(5):
    name=input()
    f.write(name+'\n')
print("Append completed!")
f.close()

print(f"Content of \"{filename}\":")
ff=open(filename,'r')

#buf=ff.read() ## 這題這樣寫有錯
#print(buf)    ## 這題這樣寫有錯

# 正解: 
for e in ff:
    print(e)

ff.close()
