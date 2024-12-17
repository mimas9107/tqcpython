# -*- coding: utf-8 -*-
"""
901
題目說明
請撰寫一程式，將使用者輸入的五筆資料寫入到write.txt（若不存在，則讓程式建立它），每一筆資料為一行，包含學生名字和期末總分，以空白隔開。檔案寫入完成後要關閉。
"""

file=open("write.txt","w")
for i in range(5):
    data=input()
    file.write(data+'\n')



file.close()