# coding: utf-8

# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação
# no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

alturas = []
idades = []

for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    alturas.append(altura)
    idades.append(idade)

for i in range(4, -1, -1):
    print(f"Altura da pessoa {i+1}: {alturas[i]} metros")
    print(f"Idade da pessoa {i+1}: {idades[i]} anos")
