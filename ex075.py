tupla = ('Aula', 'Curso', 'Palavras', 'Aluno', 'Materia', 'Coisas')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')