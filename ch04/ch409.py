No1=0
No2=0
NUll=0
i=0
while(i!=5):
    vote=eval(input())
    if(vote == 1):
        No1+=1
    elif(vote == 2):
        No2+=1
    else:
        NUll+=1    
    i+=1
    print("Total votes of No.1: Nami = {}".format(No1))
    print("Total votes of No.2: Chopper = {}".format(No2))
    print("Total null votes = {}".format(NUll))
if(No1>No2):
    print("=> No.1 Nami won the election.")
elif(No2>No1):
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")