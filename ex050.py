num = int(input('Digite número:'))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('o número {} foi divisivel {}'.format(num, cont), end = ' ')
if cont == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo')

