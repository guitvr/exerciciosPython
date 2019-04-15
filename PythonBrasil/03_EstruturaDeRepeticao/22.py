# coding: utf-8

# Altere o programa de cálculo dos números primos, informando, caso
# o número não seja primo, por quais número ele é divisível.

n = int(input("Digite um número inteiro: "))
div = 0
for i in range(1, n):

    if n % i == 0:
        div += 1
        if div == 2:
            print(f"\n{n} não é um número primo")
            print(f"\nAlém de ser divisível por 1 e por {n},\nele é divisível por: ")
        if div > 1:
            print(f"{i}")

if div == 1:
    print(f"\n{n} é um número primo")
    print(f"\n{n} só é divisível por 1 e por ele mesmo")
