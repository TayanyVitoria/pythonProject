cont = 0
valores = []
while True:
    print('-' * 60)
    v = int(input('digite um número: '))
    valores.append(v)
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar:[S/N]: ')).strip().upper()
    if continuar == 'N':
        break
valores.sort(reverse=True)
print('-'*60)
print(f'Quantidades de números digitados: {cont}')
print(f'lista em ordem decrescente: {valores}')
if 5 in valores:
    print(f'O valor 5 aparece na lista')
else:
    print('O valor 5 não foi encotrado na lista')
print('-'*60)






