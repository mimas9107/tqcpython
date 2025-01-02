# -*- coding: utf-8 -*-
# simu02 #01

L=[eval(input()) for i in range(5)]

print(f"{L[0]} {L[1]} {L[2]} {L[3]} {L[4]}")
print(f"Sum = {sum(L):.1f}")
print(f"Average = {sum(L)/len(L):.1f}")