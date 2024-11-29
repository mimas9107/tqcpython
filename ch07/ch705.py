s=[set(), set(), set()]
# s=[{3, 39, 7, 28, -2}, {0, 2, 77}, {65, 99, 3, 39, 7, 12, -2, 28, -1}]
times=[5,3,9]

for i in range(0,3):             ## 要賦值的 set組數: 0,1,2,
    print(f"Input to set{i+1}:") ## 顯示: 1,2,3,
    for t in range(times[i]):    ## 分別執行 5次, 3次, 9次 輸入,
        s[i].add(eval(input()))


# print(s)
print("set2 is subset of set1:",s[1].issubset(s[0]))
print("set3 is superset of set1:",s[2].issuperset(s[0]))