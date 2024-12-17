# -*- coding: utf-8 -*-
"""
905
題目說明：¶
請撰寫一程式，要求使用者輸入檔案名稱data.txt和一字串s，顯示該檔案的內容。接著刪除檔案中的字串s，顯示刪除後的檔案內容並存檔。
"""
# filename="data.txt"
filename=input()
# target="Tomato"
target=input()


file=open(filename,"r+")
buf=file.read()
print("=== Before the deletion")
print(buf)
print("=== After the deletion")
buf=buf.replace(target,"")
print(buf)
file.close()

file=open(filename,"w+")
file.write(buf)
file.close()