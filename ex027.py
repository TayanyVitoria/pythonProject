velo = int(input('Digite a velocidade:'))
mul = (velo - 80) * 7
if velo < 80:
    print('Você está no dentro do limite permitido.')
else:
    print('Você foi multado por ultrapassar o limite de velocidade permitido  ')
    print('Valor da multa:R${:.2f}'.format(mul))