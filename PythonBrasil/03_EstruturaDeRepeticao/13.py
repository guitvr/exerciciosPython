# coding: utf-8

# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
# número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite um número para a base: "))
exp = int(input("Digite um número para o expoente: "))

x = 1

for i in range(exp):
    x *= base

print(f"{base}^{exp} = {x}")
