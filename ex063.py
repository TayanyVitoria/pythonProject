num = cont = soma = 0
while num != 999:
    num = int(input('digite qualquer número [DIGITE 999 PARA PARAR]:'))
    if num != 999:
        cont += 1
        soma = soma + num
print('voce digitou {} números, e a soma de todos eles é: {}'.format(cont, soma))
print('Acabou')

