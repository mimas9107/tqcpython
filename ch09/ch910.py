filename='read.dat'
females=0
males=0

f=open(filename,'r',encoding='utf-8')
print(f"{'學號'} {'姓名'} {'性別'} {'科系'}")
buf=f.readlines()
buf=buf[1:]

# print(buf)
for i in buf:
    c=0
    for e in i.split(' '):
        print(f"{e} ",end='')
        
        if(c==2): 
            if(e=='0'): 
                females+=1
            elif(e=='1'):
                males+=1
        c+=1
    print()


f.close()
print("Number of males: {}".format(males))
print("Number of females: {}".format(females))