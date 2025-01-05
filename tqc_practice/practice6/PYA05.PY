#507
x=eval(input())

def compute(x):
    if(x<=1):
        return False
    elif(x==2):
        return True
    else:
        for e in range(2,x):
            if (x%e==0):
                return False
        else:
            return True    
     

if compute(x):
    print("Prime")
else:
    print("Not Prime")