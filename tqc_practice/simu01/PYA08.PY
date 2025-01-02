# -*- coding: utf-8 -*-
# simu01 #08
l=0
d=0
C=0

pw=input()
if(len(pw)<8):
    print("Invalid password")
else:
    for e in pw:
        if(e.isdigit()):
            d+=1
        
        if(e.isalpha()):
            l+=1
            if(e.upper()):
                C+=1
            
                

    # print(len(pw))
    # print(l)
    # print(d)
    # print(C)
    if(C>0 and l>=1 and d>=1):
        print("Valid password")
    else:
        print("Invalid password")