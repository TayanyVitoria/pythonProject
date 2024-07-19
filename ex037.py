n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite segunda nota do aluno:'))
m = (n1+n2)/2
if m < 4.9:
    print('A média do aluno foi {:.1f}: ALUNO REPROVADO'.format(m))
elif m >= 5.0 and m <= 6.9:
    print('A média do aluno foi {:.1f}: ALUNO DE RECUPERAÇÃO'.format(m))
elif m > 7.0:
    print('A média do aluno foi {:.1f}: ALUNO DE APROVADO'.format(m))
