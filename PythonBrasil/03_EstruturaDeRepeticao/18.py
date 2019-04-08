# coding: utf-8

# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input("Digite a quantidade de números a ser digitada: "))

soma = 0

for i in range(n):
    num = int(input(f"n{i+1}: "))

    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    soma += num

print(f"""
Dos números digitados:
o maior é {maior}
o menor é {menor}
a soma dos números digitados é {soma}""")
