# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:00:46 2024

@author: #08 Justin
"""
X=set()
Y=set()

buf=" "
print("Enter group X's subjects:")
while(buf!='end'):
    buf=input()
    if(buf=='end'): break
    X.add(buf)


buf=" "    
print("Enter group Y's subjects:")
while(buf!='end'):
    buf=input()
    if(buf=='end'): break
    Y.add(buf)

# or
print(sorted(X | Y))
# and
print(sorted(X & Y))
# Y diff X
print(sorted(Y - X))
# X xor Y
print(sorted(X ^ Y))