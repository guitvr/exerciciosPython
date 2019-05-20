# coding: utf-8

# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

mediasAlunos = []

for i in range(10):
    aluno = int(input("Digite o número do aluno: "))

    soma = 0
    media = 0

    for j in range(4):
        nota = float(input(f"Digite a nota {j+1}/4 do aluno {aluno}: "))
        soma += nota

    media = soma / 4
    mediasAlunos.append((aluno, media))

    print()

print("Alunos com média maior ou igaul a 7.0:")
for i in range(10):
    if mediasAlunos[i][1] >= 7:
        print(f"Aluno: {mediasAlunos[i][0]} | Média: {mediasAlunos[i][1]}")
