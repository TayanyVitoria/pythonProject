import random
num = int(input('Digite um número entre 1 e 5:'))
nume = random.randrange(1, 5)
print('O número escolhido foi {}'.format(nume))
if num == nume:
    print('Você acertou, parábens!!!')
else:
    print('Você errou, tente novamente!')