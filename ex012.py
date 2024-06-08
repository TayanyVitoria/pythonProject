l = float(input('digite a largura da parede:'))
al = float(input('digite a altura da sua parede:'))
area = l * al
print('sua parede tem dimensão {}x{} e sua área é de {}m²'.format(l, al, area))
tinta = area / 2
print('para pintar essa parede você precisa de {} litro de tinta'.format(tinta))