num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar:[S/N]: ')).strip().upper()
        print('-' * 50)
    if continuar == 'N':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
       par.append(v)
    else:
        impar.append(v)
print('-'*50)
print(f'\nA lista com todos os números é:{num} ')
print(f'\nlista de números pares: {par}')
print(f'\nlista de números impar: {impar} ')
print('-'*50)