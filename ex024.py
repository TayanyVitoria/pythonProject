frase = str(input('Digite uma frase qualquer:')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A aparece posição: {}'.format(frase[0]))
print(' a ultima letra A aparece na posição: {}'.format(frase.rfind('A')))

