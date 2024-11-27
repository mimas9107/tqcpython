## 808 社會安全碼
SSN:str=input()
if(SSN[0].isdigit() 
   and SSN[1].isdigit() 
   and SSN[2].isdigit() 
   and SSN[3] == '-' 
   and SSN[4].isdigit()
   and SSN[5].isdigit()
   and SSN[6] == '-'
   and SSN[7].isdigit()
   and SSN[8].isdigit()
   and SSN[9].isdigit()
   and SSN[10].isdigit()):
    print('Valid SSN')
else:
    print('Invalid SSN')
