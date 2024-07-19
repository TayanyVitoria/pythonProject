from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Digite {}° ano de nascimento:'.format(c)))
    idade = ano - atual
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Total de pessoa maior de idade: {}'.format(maior))
print('Total de pessoa menor de idade: {}'.format(menor))