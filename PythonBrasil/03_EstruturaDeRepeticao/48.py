# coding: utf-8

# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321

n = int(input("Digite um número inteiro: "))

nStr = str(n)
nStrInvertida = ''

for i in range(len(nStr)-1, -1, -1):
    nStrInvertida += nStr[i]

nInvertida = int(nStrInvertida)

print(nInvertida)
