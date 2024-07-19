from random import randint
from time import sleep
print('-=+'*13)
print('ADIVINHE O NÚMERO QUE ESTOU PENSANDO')
print('-=+'*13)
computador = randint(0,10)
tentativas = 0
jogador = ''
while not jogador == computador:
    jogador = int(input('Digite seu palpite:'))
    tentativas += 1
    if jogador == computador:
        print('Eu escolhi...')
        sleep(5)
        print(computador)
        print('Parabens você ACERTOU!!')
        print('Você precisou de {} tentativas para adivinhar'.format(tentativas))
    else:
        print('Não foi esse número que eu pensei :-(')
        if jogador < computador:
            print('Eu escolhi um número maior...')
            print('tente novamente!')
        if jogador > computador:
            print('Eu escolhi um número menor...')
            print('tente novamente!')
            