pessoa = list()
pessoas = list()
maipesso = 0
menpesso = 0
while True:
    pessoa.append(str(input('Digite nome: ')))
    pessoa.append(float(input('Digite o pesso: ')))
    if len(pessoas) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]

    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar = ' '
    while continuar not in 'SN':
        print('-' * 50)
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()
        print('-'*50)
    if continuar == 'N':
        break

print(f'total de pessoas cadastrada: {len(pessoas)}')
print(f'O maior pesso cadastrado foi {mai}Kg peso de ', end=' ')

for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso cadastrado foi {men}Kg peso de ', end=' ')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
