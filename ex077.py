valores = list()
while True:
   v = int(input(f"digite um número:  "))
   if v not in valores:
      valores.append(v)
      print('Número adicionado com sucesso')
   else:
      print('Esse número ja existe na lista! ele não foi adicionado')

   continuar = ' '
   while continuar not in 'SN':
      continuar = str(input('Quer continuar [S/N]? ')[0]).upper().strip()
      print('-' * 50)
   if continuar == 'N':
      break
valores.sort()
print(f'Números digitados: {valores}')