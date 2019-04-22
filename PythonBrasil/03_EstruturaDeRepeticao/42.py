# coding: utf-8

# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos
# deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados
# deverá terminar quando for lido um número negativo.

nums0025 = nums2650 = nums5175 = nums76100 = 0

while True:
    num = int(input("Digite um número inteiro positivo (negativo para parar): "))
    if num < 0:
        break

    if num < 26:
        nums0025 += 1
    elif 26 <= num <= 50:
        nums2650 += 1
    elif 51 <= num <= 75:
        nums5175 += 1
    elif 76 <= num <= 100:
        nums76100 += 1

print(f"""

Quantidade de números entre 0 e 25: {nums0025}
Quantidade de números entre 26 e 50: {nums2650}
Quantidade de números entre 51 e 75: {nums5175}
Quantidade de números entre 76 e 100: {nums76100}
""")
