# coding: utf-8

# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

a = []
somaQuadrados = 0
print("Digite 10 números inteiros: ")
for i in range(10):
    num = int(input(f"Digite o número {i+1}/10: "))
    a.append(num)

for i in range(10):
    somaQuadrados += a[i]**2

print(f"Soma dos quadrados dos números digitados: {somaQuadrados}")
