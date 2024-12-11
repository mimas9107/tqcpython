## solution A: 不去用 Set,Dict的方式:
## 會製作出一組查詢陣列:
## (1)紀錄從 orig被 pop出來的元素之陣列(不會有重複元素)
S=[]
## (2)相對應元素的個數之陣列
C=[]

orig=[eval(input()) for i in range(10)]  
#orig=[34,18,22,32,18,29,30,38,42,18]


#不用 orig.copy() 為了避免淺複製問題, 保持原資料完整.
target=[e for e in orig]

# for i in range(len(orig)):
#     print(f"o,t= {id(orig[i])}, {id(target[i])}")

# 跑 len(orig)次
for i in range(len(target),0,-1):
    # 將原串列尾端 pop取出值放在 tmp
    tmp = target.pop()
    
    # 將 tmp判斷在 S有無存在, 不存在就推入 S,及 C推入1;
    if tmp not in S:
        S.append(tmp)
        C.append(1)
    else:
        # tmp判斷在 S有出現過, 此時的 tmp在 S中出現在第幾個 index, 將 C[index]+=1
        C[S.index(tmp)]+=1

## 印結果
## 從 C找最大的數字位於哪一個index, 對應此 index的 S陣列元素即眾數. 
print(S[C.index(max(C))])
print(max(C)) ## 眾數個數

debug=False
if(debug):
    print("原始陣列: ",orig)
    print("查詢陣列: ",S)
    print("計數陣列: ",C)

##solution B: 老師/標準解法:
if(debug):
    
    
    D=dict()
    # 建立查詢字典:
    for e in orig:
        if(e not in D):
            D[e]=1
        else:
            D[e]+=1
            
    # 找出查詢字典 value最大值(次數最多):
    maxv=max(D.values())
    
    # 反查字典 value最大值是哪個 key:
    for k,v in D.items():
        if (v==maxv):
            maxk=k
    print(maxk)
    print(maxv)