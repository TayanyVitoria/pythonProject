from random import randint
print('-=-='*5)
print('VAMOS JOGAR JOKENPÔ')
print('-=-='*5)
print('''
OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2]TESOURA''')
jogador = int(input('Escolha digitando apenas número:'))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
print('-=+'*11)
print('COMPUTADOR ESCOLHEU:{}'.format(lista[computador]))
print('-=+'*11)
print('VOCÊ ESCOLHEU:{}'.format(lista[jogador]))
print('-=+'*11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0: # jogador jogou pedra
      print('Empatamos!')
    elif jogador == 1: # jogador jogou papel
      print('Você VENCEU!!')
    elif jogador == 2: # jogador jogou tesoura
      print('Você PERDEU!!')
    else:
      print('jogada inválida')
elif computador == 1: #computador jogou papel
    if jogador == 0: # jogador jogou pedra
      print('Você PERDEU!!')
    elif jogador == 1: # jogador jogou papel
      print('Empatamos!!')
    elif jogador == 2: # jogador jogou tesoura
      print('Você VENCEU!!')
    else:
      print('jogada inválida')
elif computador == 2:#computador jogou tesoura
  if jogador == 0: # jogador jogou pedra
    print('Você VENCEU!!')
  elif jogador == 1: # jogador jogou papel
    print('Você PERDEU!!')
  elif jogador == 2: # jogador jogou tesoura
    print('Empatamos!!')
  else:
    print('jogada inválida')
