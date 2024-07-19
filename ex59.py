print('-=+'*8)
print('PROGRESSÃO ARITMÉTICA')
print('-=+'*8)
print('''1O primeiros termos da progessão''')
primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão da PA:'))
termos = primeiro
contador = 1
while contador >= 10:
    print(contador)
    termos *= razão
    print(termos)