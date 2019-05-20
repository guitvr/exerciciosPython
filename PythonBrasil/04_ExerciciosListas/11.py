# coding: utf-8

# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

v1 = []
v2 = []
v3 = []
vIntercalado = []

print("Digite 10 números do vetor 1: ")
for i in range(10):
    num = int(input(f"Digite o número {i+1}/10: "))
    v1.append(num)

print("\nDigite 10 números do vetor 2: ")
for i in range(10):
    num = int(input(f"Digite o número {i+1}/10: "))
    v2.append(num)

print("\nDigite 10 números do vetor 3: ")
for i in range(10):
    num = int(input(f"Digite o número {i+1}/10: "))
    v3.append(num)

for i in range(10):
    vIntercalado.append(v1[i])
    vIntercalado.append(v2[i])
    vIntercalado.append(v3[i])

print(f"\nVetor 1: {v1}")
print(f"Vetor 2: {v2}")
print(f"Vetor 3: {v3}")
print(f"Vetor Intercalado: {vIntercalado}")
