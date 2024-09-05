from time import sleep
n1 = int(input('Digite primeiro número:'))
n2 = int(input('Digite segundo número:'))
r = 0
while r != 5:
    print('-=+'*10)
    print('''
    [1] somar
    [2] multiplicar
    [3] maior e menor
    [4] escolher novos números
    [5] sair
            ''')
    print('-=+' * 10)
    r = int(input('Digite sua escolha:'))
    print('números digitados: {} e {}'.format(n1, n2))

    if r == 1:
            soma = n1 + n2
            print('A soma: {} + {} = {}'.format(n1, n2, soma))
    elif r == 2:
            multiplicacao = n1 * n2
            print('A multiplicação: {} x {} = {}'.format(n1, n2, multiplicacao))
    elif r == 3:
         if n1 > n2:
                print('Maior:{}\nMenor:{}'.format(n1, n2))
         elif n2 > n1:
                print('Maior:{}\nMenor:{}'.format(n2, n1))
         else:
            print('Os dois são iguais')
    elif r == 4:
        print('Qual será os novos números:')
        n1 = int(input('Digite primeiro número: '))
        n2 = int(input('Digite segundo número:'))
    elif r == 5:
        print('finalizando...')
        sleep(2)
        print('ACABOU')


