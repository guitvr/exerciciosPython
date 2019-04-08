# coding: utf-8

# Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números impares.

print("Digite 10 números inteiros:")

par = 0
impar = 0

for i in range(10):
    n = int(input(f"n{i+1}: "))

    if n % 2 == 1:
        par += 1
    else:
        impar += 1

print(f"\nForam digitados:\n{par} números pares\n{impar} números ímpares")
