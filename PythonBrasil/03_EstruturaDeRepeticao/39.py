# coding: utf-8

# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno
# e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

for i in range(10):
    numAluno = int(input("Digite o número do aluno: "))
    alturaAluno = float(input(f"Digite a altura do aluno {numAluno} (em metros): "))

    if i == 0:
        altMaior, numMaior, altMenor, numMenor = alturaAluno, numAluno, alturaAluno, numAluno
    else:
        if alturaAluno > altMaior:
            altMaior, numMaior = alturaAluno, numAluno
        if alturaAluno < altMenor:
            altMenor, numMenor = alturaAluno, numAluno

print(f"""
Com {altMaior} metros de altura, o aluno {numMaior} é o maior.
Com {altMenor} metros de altura, o aluno {numMenor} é o menor.
""")
