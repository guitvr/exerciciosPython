# coding: utf-8

# Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input("Digite o número de notas para o cálculo da média entre eles: "))

soma = 0

for i in range(n):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma / n

print(f"\nMédia: {media:.2f}")
