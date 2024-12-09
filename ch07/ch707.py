X=set()
Y=set()
# X={'Math','Literature', 'English','History','Geography'}
# Y={'Math','Literature','Chinese','Physical','Chemistry'}
print("Enter group X's subjects:")
subjects=" "
while(subjects != 'end'):
    subjects=input()
    if subjects=='end':
        break
    else:
        X.add(subjects)

print("Enter group Y's subjects:")
subjects=" "
while(subjects != 'end'):
    subjects=input()
    if subjects=='end':
        break
    else:
        Y.add(subjects)

#(1)X union Y
#(2)X intersect Y
#(3)Y-X
#(4)X ^ Y

print(sorted(X | Y))
print(sorted(X & Y))
print(sorted(Y - X))
print(sorted(X ^ Y))