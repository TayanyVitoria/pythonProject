from datetime import date
print('CONSULTANDO ALISTAMENTO MILITAR')
atual = date.today().year
nasc = int(input('Digite o ano que você nasceu:'))
idade = atual - nasc
print('Você nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE')
elif idade < 18:
    falta = 18 - idade
    print('Falta {} anos para você se alistar'.format(falta))
    ano = atual + falta
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    passou = idade - 18
    print('Já se passaram {} anos do ano que você deveria se alistar'.format(passou))
    ano = atual - passou
    print('Seu alistamento foi em {}'.format(ano)[0:])
