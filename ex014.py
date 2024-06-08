import math
co = float(input('Digite a medida do cateto oposto:'))
ca = float(input('Digite a medida do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
