contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis', 'dezessete ', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num > 20:
        print('Tente novamente!!', )
        print('Você digitou um número maior que vinte')
    else:
        print(f'O número digitado foi: {contagem[num]}')
    continuar = ' '
    while continuar not in 'SN':
        print('-' * 40)
        continuar = str(input('Quer continuar?[S/N]')[0]).upper().strip()
        print('-' * 40)
    if continuar == 'N':
        break

