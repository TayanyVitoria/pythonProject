valor = float(input('digite o preço do produto R$'))
avista = valor - (valor*7/100)
print('o valor avista com 7% de desconto é {:.2f}'.format(avista))
parcelado = valor + (valor*7/100)
print('o valor do produto á prazo (parcelado) é {:.2f}'.format(parcelado))
