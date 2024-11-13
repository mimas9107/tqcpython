# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:03:36 2024

@author: user
"""

x=eval(input())
y=eval(input())
z=eval(input())

vkph=z/((x*60+y)/3600)
vmph=vkph/1.6

print("Speed = {:.1f}".format(vmph))