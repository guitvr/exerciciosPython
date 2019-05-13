# coding: utf-8

# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
# números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
pares = []
impares = []

print("Digite 20 números inteiros:")

for i in range(20):
    n = int(input(f"Número {i+1}: "))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nNúmeros digitados:\n    ", end='')
for n in numeros:
    print(n, end=' ')
print("\nNúmeros pares:\n    ", end='')
for n in pares:
    print(n, end=' ')
print("\nNúmeros ímpares:\n    ", end='')
for n in impares:
    print(n, end=' ')
