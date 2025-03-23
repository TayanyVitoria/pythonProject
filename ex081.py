expressao = str(input('Digite a expressão: '))
pilha = []
for simbulo in expressao:
    if simbulo == '(':
        pilha.append('(')
    elif simbulo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Essa expressão está válida!!')
else:
    print('Essa expressão está inválida!')