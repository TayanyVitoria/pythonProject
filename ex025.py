n = str(input('Digite seu Nome Completo:')).strip()
di = n.split()
print('Seu Primeiro Nome é: {}'.format(di[0]))
print('Seu Último Nome é: {}'.format(di[len(di)-1]))
