from typing import Union, Any

soma = 0
medida = 0
velhohomem = 0
nomevelho = ''
mulher20 = 0
for p in range (1, 5):
    print('_______{}° PESSOA_______'.format(p))
    nome = str(input('Digite o nome:')).strip()
    idade = int(input('digite idade:'))
    sexo= str(input('Digite o gênero[F/M]:')).strip()
    soma = soma + idade
    if p == 1 and sexo in 'mM':
        velhohomem = idade
        nomevelho = nome
    if sexo in 'mM' and idade > velhohomem:
        velhohomem = idade
        nomevelho = nome
    if sexo in 'fF'and idade < 20:
        mulher20 += 1
media = soma / 4
print('A média de idade do grupo é: {:.2f}'.format(media))
print('O homem mais velho é {} e tem {} anos.'.format(nomevelho, velhohomem))
print('Total de mulheres menor de 20 anos: {}'.format(mulher20))