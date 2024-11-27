## Pangram, 全字母句

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
