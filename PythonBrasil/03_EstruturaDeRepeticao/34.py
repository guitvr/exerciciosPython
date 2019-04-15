# coding: utf-8

# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que
# peça um número inteiro e determine se ele é ou não um número primo.

n = int(input("Digite um número inteiro: "))
div = 0
for i in range(1, n+1):
    if n % i == 0:
        div += 1
    print(f"{n} % {i} = {n%i}")
    if div > 2:
        print(f"{n} não é um número primo")
if div <= 2:
    print(f"{n} é um número primo")
