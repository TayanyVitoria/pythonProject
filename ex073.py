num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os números: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'numeros pares digitados: ',end='')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')