#609

print('Enter matrix 1:')
m1_11=eval(input('[1, 1]: '))
m1_12=eval(input('[1, 2]: '))
m1_21=eval(input('[2, 1]: '))
m1_22=eval(input('[2, 2]: '))

print('Enter matrix 2:')
m2_11=eval(input('[1, 1]: '))
m2_12=eval(input('[1, 2]: '))
m2_21=eval(input('[2, 1]: '))
m2_22=eval(input('[2, 2]: '))

print('Matrix 1:')
print(f'{m1_11} {m1_12} ')
print(f'{m1_21} {m1_22} ')

print('Matrix 2:')
print(f'{m2_11} {m2_12} ')
print(f'{m2_21} {m2_22} ')

print('Sum of 2 matrices:')
print(f'{m1_11+m2_11} {m1_12+m2_12} ')
print(f'{m1_21+m2_21} {m1_22+m2_22} ')