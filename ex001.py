dia = int(input('quantos dias alugados?'))
km = float(input('quatos km rodados?'))
p = (dia * 60) + (km * 0.15)
print('O total a ser pago é de R${:.2f}'.format(p))