r = 'F' or 'M'
while r not in 'M' or 'F':
    nome = str(input('Digite se nome:'))
    r = str(input('Qual seu gênero [M/F]:')).upper().strip()[0]

    if r != 'F' and 'M':
        print('digite F ou M')
    else:
        print('Gênero registrado com sucesso.')
        print('acabou')
