prin = [[], []]
valor = 0
for i in range(7):
    valor = int(input('Digite qualquer número: '))
    if valor % 2 == 0:
        prin[0].append(valor)
    else:
        prin[1].append(valor)
prin[0].sort()
prin[1].sort()
print(f'Os números pares digitados {prin[0]}')
print(f'Os números impares digitados {prin[1]}')


