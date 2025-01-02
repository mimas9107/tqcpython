#407
# (y%4==0 and y%100!=0) or y%400==0 
y=1
while(y!=-9999):
    y=eval(input())
    if y==-9999: break

    if((y%4==0 and y%100!=0) or y%400==0):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")