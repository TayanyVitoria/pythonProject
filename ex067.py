from time import sleep
print('-'*20)
print('CADASTRANDO PESSOAS')
print('-'*20)
homem = 0
mulher = 0
total = 0
while True:
    idade = int(input('Digite idade:'))
    genero = ' '
    while genero not in 'FM':
        genero = str(input('Digite genero [F/M]:')[0]).upper().strip()
    if idade >= 18:
        total += 1
    if genero == 'F' and idade < 20:
        mulher += 1
    if genero == 'M':
         homem += 1

    resposta = '  '
    while resposta not in 'SN':
        print('-' * 20)
        resposta = str(input('Quer continuar?[S/N]')[0]).upper().strip()
        print('-' * 20)
    if resposta == 'N':
        break


print(f'Quantiade de pessoas maior de 18 anos:{total}\nQuantidade de homens: {homem}\nQuatidade de mulher menor de 20 anos: {mulher}')