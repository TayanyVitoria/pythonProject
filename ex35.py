n = int(input('Digite um número inteiro:'))
print('[1]Converter número para BINÁRIO\n[2] Converter número para OCTAL\n[3]Converter número para HEXADECIMAL')
res =int(input('ESCOLHA UMA DAS OPÇÕES DE ACORDO COM O NÚMERO:'))
if res == 1:
    print('Esse número em binário é:'.format(bin(n)[2:]))
elif res == 2:
    print('Esse número em octal é'.format(oct(n)[2:]))
elif res == 3:
    print('Esse número em hexadeciamal é:{}'.format(hex(n)[2:]))
else:
    print('Por favor escolha uma das opções!!')