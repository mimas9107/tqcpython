#309

money=eval(input())
ratey=eval(input())
month=eval(input())

balance=money
print(f"Month \t  Amount")
for i in range(1,month+1):
    balance+=balance*ratey/1200
    print(f"{i:>3d} \t {balance:.2f}")


