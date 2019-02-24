# coding: utf-8

# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

maior, meio, menor = n1, 0, 0

if n2 >= maior:
    maior = n2
if n3 >= maior:
    maior = n3

if maior == n1:
    if n2 >= n3:
        meio, menor = n2, n3
    else:
        meio, menor = n3, n2

if maior == n2:
    if n1 >= n3:
        meio, menor = n1, n3
    else:
        meio, menor = n3, n1

if maior == n3:
    if n1 >= n2:
        meio, menor = n1, n2
    else:
        meio, menor = n2, n1

print(maior, meio, menor)

'''
nums = [n1, n2, n3]
nums.sort(reverse=True)
print(nums)
'''
