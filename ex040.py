n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
if n1 > n2:
    print('O maior número é: {}'.format(n1) )
    print('O menor número é: {}'.format(n2))
elif n1 < n2:
    print('O maior número é: {}'.format(n2))
    print('O menor número é {}'.format(n1))
else:
    print('Os dois número são iguais.')
