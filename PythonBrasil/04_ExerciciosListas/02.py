# coding: utf-8

# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []
print("Digite 10 números: ")
for i in range(10):
    n = float(input(f"Digite o número {i+1}: "))
    lista.append(n)
for n in lista[::-1]:
    print(n)
