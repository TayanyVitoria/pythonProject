menor = prod1000 = total = cont = 0
barato = ''
print('=-'*20)
print('{:^40}'.format('MERCADO PYTHON'))
print('=-'*20)
while True:
    nome = str(input('Digite nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço: R$ '))
    total += preco
    cont += 1
    if preco > 1000.00:
        prod1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        print('-' * 20)
        continuar = str(input('Quer continuar?[S/N]')[0]).upper().strip()
        print('-' * 20)
    if continuar == 'N':
            break

print(f'Total da compra:{total:.2f}')
print(f'Produto mais barato: Preço:R${menor:.2f} Nome:{barato}')
print(f'Quantidade de produtos custado mais de R$1000.00: {prod1000} ')

