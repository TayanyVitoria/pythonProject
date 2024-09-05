from random import randint
print('\033[1;33m-=+\033[m'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('\033[1;33m-=+\033[m'*10)
venceu = 0
while True:
    jogador = int(input('Digite número: '))
    computador = randint(1, 15)
    soma = computador + jogador
    print(f'Você jogou {jogador} e computador jogou {computador}')
    resposta = ' '
    while resposta not in 'PI':
        resposta = str(input('Escolha [I] ou [P]: ')[0]).upper().strip()
        if resposta == 'I':
            jogador = 'Ímpar'
            computador = 'Par'
            print(f'Você escolheu {jogador} e computador escolheu {computador}')
        else:
            jogador = 'Par'
            computador = 'Ímpar'
            print(f'Você escolheu {jogador} e computador escolheu {computador}')

    if soma % 2 == 0:
        if resposta == 'P':
            print('\033[1;32mVocê venceu!!\033[m')
            print(f'A soma foi {soma} que é PAR')
            print('Vamos jogar novamente...')
            venceu += 1
            print('-'*40)
        if resposta == 'I':
            print('\033[1;31mVocê Perdeu!!\033[m')
            print(f'A soma foi {soma} que é PAR')
            print(f'Total de vitorias: {venceu}')
            break
    else:
        if resposta == 'I':
            print('\033[1;32mVocê venceu!!\033[m')
            print(f'A soma foi {soma} que é ÍMPAR')
            venceu += 1
            print('Vamos jogar novamente...')
            print('-' * 40)
        if resposta == 'P':
            print('\033[1;31mVocê Perdeu!!\033[m')
            print(f'A soma foi {soma} que é ÍMPAR')
            print(f'Total de vitorias: {venceu}')
            break
