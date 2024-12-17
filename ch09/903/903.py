# -*- coding: utf-8 -*-
"""
903
題目說明：¶
請撰寫一程式，要求使用者輸入五個人的名字並加入到data.txt的尾端。之後再顯示此檔案的內容。
"""
#Daisy
#Kelvin
#Tom
#Joyce
#Sarah
## 題目為了印出原檔案內容 所以用 "a+"
file=open("data.txt","a+")
for i in range(5):
    buf=input()
    file.write('\n'+buf) ## 寫入 "換行" 是重點

file.seek(0) ## 返回檔案頭
print("Append completed!")
print('Content of "data.txt":')
print(file.read())


file.close()