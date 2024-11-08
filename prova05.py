numeroAluno = int(input('digite o numero de alunos '))
mediaTurma = 0

for i in range(numeroAluno):
    
    nome = input(f'digite o nome do {i+1}º aluno:')
    nota1 = int(input(f'digite a primeira nota  do aluno {nome} :'))
    nota2 = int(input(f'digite a segunda nota do aluno {nome} :'))
    nota3 = int(input(f'digite a terceira do aluno {nome} :'))

    mediaAluno = ((nota1) + (nota2) + (nota3)) / 3

    
    print(f'aluno : {nome}')
    print(f'primeira nota: {nota1}')
    print(f'segunda nota: {nota2}')
    print(f'terceira nota: {nota3}')
    print(f'A média do aluno {nome} é {mediaAluno}')

    mediaTurma += mediaAluno

    if mediaAluno >= 7:
        print(f'O aluno {nome} foi aprovado')
    else:
        print(f'o aluno foi reprovado')


mediaTurma /= numeroAluno

print(f'A média da turma é {mediaTurma}')

