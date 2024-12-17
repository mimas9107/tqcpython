# -*- coding: utf-8 -*-
"""
906
題目說明：¶
請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。
"""

# filename=input()
filename='data.txt'
# s1=input()
s1='pen'
# s2=input()
s2='sneakers'


file=open(filename,'r+')

buf=file.read()

print("=== Before the replacement")
print(buf)
buf2=buf.replace(s1,s2)
print("=== After the replacement")
print(buf2)

file.close()

file=open(filename,'w')
file.write(buf2)
file.close()