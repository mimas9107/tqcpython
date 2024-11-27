## 809 密碼規則

s:str=input()
## GeeksforGeek 上範例程式, 不用任何 build-in函數的寫法:
## 逐字撿出來判斷並記錄下小寫、大寫、數字個數; 並判斷大寫至少>=1個; 小寫+大寫+數字 == 字串總長度
# l, u, p, d = 0, 0, 0, 0
l,u,d=0,0,0
# s = "Rmf0rtu9e"
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"

# specialchar="$@_"
digits="0123456789"
if (len(s) >= 8):
    for i in s:

        # counting lowercase alphabets
        if (i in smallalphabets):
            l+=1            

        # counting uppercase alphabets
        if (i in capitalalphabets):
            u+=1            

        # counting digits
        if (i in digits):
            d+=1            

        # counting the mentioned special characters
        # if(i in specialchar):
        #     p+=1        
# if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
if (l>=1 and u>=1 and d>=1 and l+u+d==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")