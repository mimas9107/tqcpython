## Pangram, 全字母句

## solution1
def isPangram(s:str):

    words=[c for c in 'abcdefghijklmnopqrstuvwxyz']
    cwords=[0 for c in range(26)]

    for i in s.lower().replace(" ",""):
        cwords[words.index(i)]+=1
    # print(cwords)
    if 0 in cwords:
        return False
    else:
        return True

n=eval(input())
for i in range(n):
    # test='Learning Python is funny'
    sentences=input()
    print(isPangram(sentences))

## solution2 set的想法核心:
# 轉 set後可以用 remove(' ')
s=input()
a=set(s.lower())
a.remove(' ')
print(len(a))