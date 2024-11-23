## 先開一個12個元素的陣列
L=[0 for i in range(12)] 

## 12次輸入值
for i in range(12):
    L[i]=eval(input())

total=0
for i in range(12):
    print(f"{L[i]:>3d}",sep='',end='')
    if (i+1)%3==0: ## 控制排版換行: 數1,2,3 ;4就加 一個換行
        print() 
    if (i%2==0): ## index偶數的值加總:
        total+=L[i]

print(total)