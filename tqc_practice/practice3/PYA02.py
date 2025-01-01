#202
x=eval(input())

if (x % 3==0) and (x % 5==0) :
    # 3 and 5
    print(f"{x} is a multiple of 3 and 5.")
else:
    if(x % 3 ==0):
        print(f"{x} is a multiple of 3.")
    elif( x % 5 ==0):
        print(f"{x} is a multiple of 5.")
    else:
        print(f"{x} is not a multiple of 3 or 5.")

        