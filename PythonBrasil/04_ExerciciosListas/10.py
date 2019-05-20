# coding: utf-8

# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

v1 = []
v2 = []
vIntercalado = []

print("Digite 10 números do vetor 1: ")
for i in range(10):
    num = int(input(f"Digite o número {i+1}/10: "))
    v1.append(num)

print("\nDigite 10 números do vetor 2: ")
for i in range(10):
    num = int(input(f"Digite o número {i+1}/10: "))
    v2.append(num)

for i in range(10):
    vIntercalado.append(v1[i])
    vIntercalado.append(v2[i])

print(f"\nVetor 1: {v1}")
print(f"Vetor 2: {v2}")
print(f"Vetor Intercalado: {vIntercalado}")
