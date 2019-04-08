# coding: utf-8

# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1

n = int(input("Digite um número inteiro: "))
div = 0
for i in range(1, n):

    if n % i == 0:
        div += 1

if div > 1:
    print(f"{n} não é um número primo")
else:
    print(f"{n} é um número primo")
