s=input()
L=s.replace('-','')
if(L.isalnum()):
    print('Valid SSN')
else:
    print('Invalid SSN')