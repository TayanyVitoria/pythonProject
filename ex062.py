resposta = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while resposta == 'S':
    num = int(input('Digite um número: '))
    resposta = str(input('Quer Continuar [S/N]: ')[0]).upper().strip()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('''Quantidade de números digitados: {} 
Média entre eles : {}'''.format(cont, media))
print('''
Maior número digitado: {}
Menor número digitado: {}'''.format(maior, menor))
