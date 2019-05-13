# coding: utf-8

# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []
consoantes = 0

print("Digite 10 caracteres:")

for i in range(10):
    c = str(input(f"Caractere {i+1}: "))
    lista.append(c)

print("\nConsoantes digitadas:")

for c in lista:
    if c.lower() in 'bcdfghjklmnpqrstvwxyz':
        print(c)
        consoantes += 1

print(f"Total de consoantes: {consoantes}")
