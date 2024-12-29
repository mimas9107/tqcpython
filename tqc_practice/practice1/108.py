x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())

dx=x1-x2
dy=y1-y2

dist=dx*dx+dy*dy
dist=dist**0.5

print(f"( {x1} , {y1} )")
print(f"( {x2} , {y2} )")
print(f"Distance = {dist:.4f}")