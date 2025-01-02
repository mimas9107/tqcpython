# -*- coding: utf-8 -*-
#simu01 #07
d=dict()
buf=' '
while(True):
    buf=input('Key: ')
    if(buf=='end'): break
    v=input('Value: ')
    d[buf]=v

s=input('Search key: ')


print(s in d.keys())
    