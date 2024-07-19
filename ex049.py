print('-=+'*8)
print('PROGRESSÃO ARITMÉTICA')
print('-=+'*8)
print('''1O primeiros termos da progessão''')
primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão da PA:'))
decimo = primeiro + (10 - 1) * razão
for cout in range (primeiro, decimo + razão, razão,):
    print('{}'.format(cout), end=' ➝ ')
print('ACABOU')
#ex v1.0