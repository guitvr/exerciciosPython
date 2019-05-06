# coding: utf-8

# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

print("Para a série S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m")
n = int(input("Digite o termo n da série: "))
m = 1
s = 0
print("\nS = ", end='')
for i in range(1, n+1):
    if i != n:
        print(f"{i}/{m} + ", end='')
    else:
        print(f"{i}/{m}", end='')
    s += i/m
    m += 2
print(f" = {s}")
