soma = 0
cout = 0
for c in range(1, 7):
    num = int(input('digite {}°  número:'.format(c)))
    if num % 2 == 0:
        soma = num + soma
        cout = cout + 1

print('''Números pares: {}
Soma:{}.'''.format(cout, soma))