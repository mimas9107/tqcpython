#702
L1=[]
L2=[]

print('Create tuple1:')
while(True):
    buf=eval(input())
    if(buf==-9999): break
    L1.append(buf)

print('Create tuple2:')
while(True):
    buf=eval(input())
    if(buf==-9999): break
    L2.append(buf)
    
print(f'Combined tuple before sorting: {tuple(L1+L2)}')
print(f'Combined list after sorting: {sorted(L1+L2)}')