print('Análise de Empréstimo Para Financiamento de Casa')
casa = float(input('Digite o valor da casa:R$'))
salario = float(input('Digite o valor do seu sálario:R$'))
ano = int(input('Digite quantos anos você ira pagar:'))

def ano_para_mes(ano):
    return ano * 12


meses = ano_para_mes(ano)
vm = casa / meses
if vm < salario * 0.30:
    print('Você pode fazer esse financiamento!!!')
    print('O valor mensal a pagar é: R${:.2f}'.format(vm))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação ficaria R${:.2f} mensalmente.'.format(casa, ano, vm))
    print('Por isso, seu empréstimo foi NEGADO, porque a parcela exede 30% do seu sálario.')
