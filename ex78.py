valores = []
for i in range(5):
    v = int(input('digite um número: '))
    if i == 0 or v > valores[-1]:
        valores.append(v)
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos, v)


print('-'*50)
print(f'A lista em ordem  crescente é: {valores}')