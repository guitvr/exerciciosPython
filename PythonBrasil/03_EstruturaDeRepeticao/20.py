# coding: utf-8

# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:

    n = int(input("\nDigite um número: "))

    while not (1 <= n < 16):
        print("Digite apenas números inteiros positivos e menores que 16\n")
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

    op = int(input("\nDeseja calcular novamente? [1] sim - [0] não: "))
    if op == 0:
        break
