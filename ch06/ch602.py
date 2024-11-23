
total=0
for i in range(5):
    p=input()
    if(p=='J' or p=='j'):
        total+=11
    elif(p=='Q' or p=='q'):
        total+=12
    elif(p=='K' or p=='k'):
        total+=13
    elif(p=='A' or p=='a'):
        total+=1
    else:
        total+=int(p)

print(total)