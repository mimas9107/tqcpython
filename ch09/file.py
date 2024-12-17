
#1 mode='r' 'r+'
# file=open("fileread.txt","r+")
# file.write('123')
# for e in file:
#     print(e,end='↩')
# file.close()
#=================
#2 mode='w' 'w+'
# file=open("fileread.txt","w")
# for i in file:
#     print(i, end='')
# file.close

#====================
#3 mode='a' 'a+'
file=open("fileread.txt","a+")

file.close()

file=open("fileread.txt","r")

print(file.readlines())

file.close()