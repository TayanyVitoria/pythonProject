a = int(input('Digite seu ano:'))
if a % 4 == 0:
    print('Esse ano é bissexto!!')
elif a % 400 == 0:
    print('Esse ano é bissexto!!')
else:
    print('Esse ano não é bissexto!')