# coding: utf-8

# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números

lista = []
soma = 0
mult = 1

print("Digite 5 números inteiros")
for i in range(5):
    num = int(input(f"Digite o número {i+1}/5: "))
    lista.append(num)

print("\nNúmeros digitados: ", end='')
for num in lista:
    print(num, end=' ')
    soma += num
    mult *= num
print(f"\nSoma: {soma}\nMultiplicação: {mult}")
