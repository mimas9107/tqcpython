data=[]
for i in range(3):
    if(i==0):
        print("The 1st student:")
    elif(i==1):
        print("The 2nd student:")
    elif(i==2):
        print("The 3rd student:")

    score=[eval(input()) for s in range(5)]
    data.append(score)

for i in range(3):
    print(f"Student {i+1}")
    print(f"#Sum {sum(data[i])}")
    print(f"#Average {sum(data[i])/5:.2f}")