# coding: utf-8

# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

print("Para a série H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N")
n = int(input("Digite um valor para N: "))
h = 0
print("\nH = ", end='')
for i in range(1, n+1):
    if i != n:
        print(f"1/{i} + ", end='')
    else:
        print(f"1/{i} = ", end='')
    h += 1/n

print(h)
