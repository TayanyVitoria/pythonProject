print('Qual moeda você quer cambiar?\n a)USS (dólar)\n b)EUR (euro)\n c)ARS (peso argentino)')
a = input('digite a resposta:')
if a == 'a':
    d = float(input("digite quantos você quer cambiar?R$"))
    do = d / 5.17
    print('O seu dinheiro vale USS{:.2f}'.format(do))
elif a == 'b':
    e = float(input('digite quantos você quer cambiar?R$'))
    eu = e / 5.61
    print('O seu dinheiro vale EUR{:.2f}'.format(eu))
elif a == "c":
    ar = float(input('digite quantos você quer cambiar?R$'))
    ars = ar / 0.0058
    print('O seu dinheiro vale ARS{:.2f}'.format(ars))
else:
    print('Escolha uma das opções!!!')
