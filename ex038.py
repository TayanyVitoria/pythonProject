idade = int(input('Digite a idade do atleta:'))
if idade <= 9:
    print('A categoria do atleta é MIRIM.')
elif idade >= 10 and idade <= 14:
    print('A categoria do atleta é INFANTIL.')
elif idade >= 15 and idade <= 19:
    print('A categoria do atleta é JUNIOR.')
elif idade == 20:
    print('A categoria do atleta é SÊNIOR')
elif idade < 21:
    print('A categoria do atleta é MASTER')