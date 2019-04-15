# coding: utf-8

# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista
# dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

n = int(input("Digite um número inteiro: "))

print(f"Números primos entre 1 e {n}:")
cont = 0
for num in range(1, n+1):
    div = 0
    for i in range(1, num):
        if num % i == 0:
            div += 1
        cont += 1
    if div <= 1:
        print(num)
