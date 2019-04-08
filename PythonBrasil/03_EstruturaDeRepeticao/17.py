# coding: utf-8

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input("Digite um número: "))
x = 1

print(f"{n}! = ", end="")

for i in range(n, 0, -1):
    if i != 1:
        print(f"{i}", end=" . ")
    else:
        print(f"{i}", end=" = ")
    x *= i
print(x)
