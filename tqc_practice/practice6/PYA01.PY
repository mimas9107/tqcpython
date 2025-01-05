#106
x=eval(input()) #min
y=eval(input()) #sec
z=eval(input()) #km
#1miles=1.6km
# kph=> ?mph
mph=(z/(x/60+y/3600))/1.6
print(f"Speed = {mph:.1f}")