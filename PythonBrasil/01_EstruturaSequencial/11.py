# coding: utf-8

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   a. o produto do dobro do primeiro com metade do segundo .
#   b. a soma do triplo do primeiro com o terceiro.
#   c. o terceiro elevado ao cubo.

numInt1 = int(input("Digite um número inteiro: "))
numInt2 = int(input("Digite outro número inteiro: "))
numFloat = float(input("Digite um número real: "))

a = (numInt1 * 2) * (numInt2 / 2)
b = (numInt1 * 3) + numFloat
c = numFloat ** 3

print(f"O produto do dobro do primeiro com metade do segundo = {a}")
print(f"A soma do triplo do primeiro com o terceiro = {b}")
print(f"O terceiro elevado ao cubo = {c}")
