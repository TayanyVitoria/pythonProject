km = int(input('Digite a distância da sua viagem em KM:'))
p1 = km * 0.50
p2 = km * 0.45
if km <= 200:
    print('O valor da sua passagem é R${:.2f}'.format(p1))
else:
    print('O valor da sua passagem é R${:.2f}'.format(p2))
print('Boa viagem!!')