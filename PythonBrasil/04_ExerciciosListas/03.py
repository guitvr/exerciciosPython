# coding: utf-8

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma = media = 0

print("Digite 4 notas: ")

for i in range(4):
    n = float(input(f"Nota {i+1}: "))
    notas.append(n)
    soma += n
media = soma / len(notas)

print("\nNotas:")

for n in notas:
    print(f"    {n}")

print(f"Média:\n    {media}")
