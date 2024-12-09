filename='read.txt'
f=open(filename,'r')
data=[]
data=f.readlines()
total_h=0
total_w=0
datas=[]
for e in data:
    l=e.split(" ")
    datas.append([l[0],int(l[1]),int(l[2])])
    total_h+=int(l[1])
    total_w+=int(l[2])
    print(e)
f.close()

print(f"Average height: {total_h/3:.2f}")
print(f"Average weight: {total_w/3:.2f}")
tallestname=sorted(datas,key=lambda student: student[1])[-1][0]
tallest_h=sorted(datas,key=lambda student: student[1])[-1][1]

heaviestname=sorted(datas,key=lambda student: student[2])[-1][0]
heavist_w=heaviestname=sorted(datas,key=lambda student: student[2])[-1][2]
print(f"The tallest is {tallestname} with {tallest_h:.2f}cm")
print(f"The heaviest is {heaviestname} with {heavist_w:.2f}kg ")

## 這題有錯