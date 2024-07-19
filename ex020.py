print('\033[1;31m-=\033[m'*12)
print('\033[1;35mANALISANDO TRIÂNGULOS\033[m')
print('\033[1;31m-=\033[m'*12)
r1 = float(input('Digite a medida da primeira reta:'))
r2 = float(input('Digite a medida da segunda reta:'))
r3 = float(input('Digite a medida da terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('\033[1;33mEsses segmentos pode formar um triângulo\033[m', end='')
    if r1 == r2 == r3:
        print('EQULÁTERO')
    elif r1 != r2 and r2 != r1 and r3 != r1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Esses segmentos de retas não pode formar um triângulo')