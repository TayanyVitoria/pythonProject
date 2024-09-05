produtos = ('Lapis', 1.50, 'Caderno', 30.00, 'Caneta', 2.00, 'Apontador', 3.50, 'Folha sulfite 1und.', 0.10, 'Folha almaço 1und.', 0.30, 'Estojo', 20.00, 'Trasferidor', 7.00, 'Mochila', 120.00, )
print('-'*40)
print(f"{'LISTA DE PREÇOS':^40}")
print('-'*40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'|{produtos[pos]:.<30}|', end='')
    else:
       print(f'|R${produtos[pos]:>7.2f}|')