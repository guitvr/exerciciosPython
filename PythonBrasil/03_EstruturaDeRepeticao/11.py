# coding: utf-8

# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = 0

for i in range(n1+1, n2):
    print(i)
    soma += i

print("Soma:", soma)
