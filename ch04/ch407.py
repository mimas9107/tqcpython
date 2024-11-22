year=1
while(year!=-9999):
    year=eval(input())
    if(year == -9999): break
    if(((year%4==0) and (year%100 !=0)) or (year%400==0)):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.") 