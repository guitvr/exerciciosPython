# coding: utf-8

# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))


# Usando estruturas de decisão

maior = menor = n1

if n2 >= maior:
    maior = n2
elif n2 <= menor:
    menor = n2

if n3 >= maior:
    maior = n3
elif n3 <= menor:
    menor = n3

print("O maior número é:", maior)
print("O menor número é:", menor)

# Usando listas e funções max() e min()
'''
nums = [n1, n2, n3]
print("O maior número é:", max(nums))
print("O menor número é:", min(nums))
'''
