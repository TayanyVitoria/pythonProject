s = float(input('Digite o seu salário:'))
c = (10/100*s)+s
c2 = (15/100*s)+s
if s >= 1250.0:
    print('Seu salário com aumento é: R${:.2f}'.format(c))
else:
    print('Seu salário com aumento é: R${:.2f}'.format(c2))