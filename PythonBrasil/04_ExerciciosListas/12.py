# coding: utf-8

# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.

alunos = []
somaAlturas = 0

for i in range(30):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    altura = float(input(f"Digite a altura do aluno {i+1} (em metros): "))

    aluno = (idade, altura)
    alunos.append(aluno)

    somaAlturas += altura

mediaAlturas = somaAlturas / len(alunos)

cont = 0
for aluno in alunos:
    if aluno[0] > 13 and aluno[1] < mediaAlturas:
        cont += 1

print(f"Média da altura dos {len(alunos)}: {mediaAlturas:.2f} m")
print(f"Quantidade de alunos maiores de 13 anos com altura menor que a média total: {cont}")
