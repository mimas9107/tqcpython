## 806 字元次數計算

def compute(ss:str, cc:str):
    return ss.count(cc)


s=input()
c=input()
print(f"{c} occurs {compute(s,c)} time(s)")