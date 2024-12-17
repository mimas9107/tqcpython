# -*- coding: utf-8 -*-
"""
902
題目說明：
請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。檔案讀取完成後要關閉。
"""

file=open("read.txt","r")

buf=file.read()
total=0
l=[ int(i) for i in buf.split(' ')]
print(sum(l))


file.close()