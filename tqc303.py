'''

303請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數（<100），
然後以三角形的方式依序輸出此數的相乘結果。

'''
a = int(input())

if(a<100):
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(f"{i*j:>4d}",sep='',end='')
        print()