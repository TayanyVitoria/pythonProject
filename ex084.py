matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'Digite um numero para [{i}, {c}]'))
print('-'*60)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[i][c]:^5}', end=' ')
        print()
