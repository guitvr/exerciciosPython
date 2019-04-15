# coding: utf-8

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

n = int(input("Digite um número inteiro: "))
f = 1
print(f"Fatorial de: {n}")
print(f"{n}! = ", end="")
for i in range(n, 0, -1):
    if i == 1:
        print(f"{i} = ", end="")
    else:
        print(f"{i} . ", end="")
    f *= i
print(f)
