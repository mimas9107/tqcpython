# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
解題 107
"""
print("="*32)
sumation=0
scores=[0,0,0,0,0]
for i in range(5):
    scores[i] = int(input())
    sumation+=scores[i]
    
print("{} {} {} {} {}".format(scores[0],scores[1], scores[2], scores[3],scores[4]))

print("Sum = {:.1f}".format(sumation))
print("Average = {:.1f}".format(sumation/5))
print("="*32)


print(f"Sum = {sum:>9.1f}")
print(f"Average = {sum/5:>9.1f}")