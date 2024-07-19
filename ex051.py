frase = str(input('Digite uma frase ou palavra:')).strip().upper()
palavra = frase.split()
jun = ''.join(palavra)
inv = ''
for letra in range(len(jun) -1, -1, -1):
    inv += jun[letra]
if inv == jun:
    print('O inverso da frase {} é igual a frase {} .'.format(inv, jun))
    print('Então ela é um PALINDROMO')
else:
    print('O inverso da frase {} é diferente da frase {} .'.format(inv, jun))
    print('Então ela não é um PALINDROMO.')