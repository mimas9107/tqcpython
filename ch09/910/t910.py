females = male = 0
with open("read.dat", 'r', encoding='utf-8')as f:
    content = f.readlines()
    for i in content:
        print(i)
        if i.split()[2]== '0':
            females += 1
        elif i.split()[2] == '1':
            male += 1
print("Number of males: %d"%male)
print("Number of females: %d"%females)

