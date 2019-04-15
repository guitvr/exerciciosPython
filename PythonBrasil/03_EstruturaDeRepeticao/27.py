# coding: utf-8

# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade
# de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

nTurmas = int(input("Digite a quantidade de turmas: "))
nAlunos = 0
for i in range(nTurmas):
    n = int(input(f"Digite a quantidade de alunos da turma {i+1}: "))

    while not 0 < n <= 40:
        print("As turmas não podem ter mais de 40 alunos!!")
        n = int(input(f"Digite a quantidade de alunos da turma {i + 1}: "))

    nAlunos += n

print(f"""
Total de turmas: {nTurmas}
Total de alunos: {nAlunos}
Número médio de alunos por turma: {nAlunos/nTurmas}
""")
