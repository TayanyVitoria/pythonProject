maior = 0
menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f"digite um número para posição {c}:  ")))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Números digitados: {valores}')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'Maior valor foi {maior} nas posições: ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
print(f'Menor valor: {menor} nas posições: ', end=' ')