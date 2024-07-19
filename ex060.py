from time import sleep
print('-=+'*8)
print('PROGRESSÃO ARITMÉTICA')
print('-=+'*8)
print('''1O primeiros termos da progessão''')
primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão da PA:'))
termos = primeiro
contador = 1
total = 0
continuar = 10
while continuar != 0:
    total = total + continuar
    while contador <= total:

        print('{}'.format(termos),end=' ➙ ')
        termos+=razão
        contador += 1
    print('PAUSA')
    continuar = int(input('Quantos termos a mais você quer ver:'))
    print('Digite 0 para sair!')
    if continuar == 0:
        total += 1 - 1
        print('O total de termos mostrados foi:{}'.format(total))
        print('Saindo...')
        sleep(5)
        print('FIM')
#execicio v3.0