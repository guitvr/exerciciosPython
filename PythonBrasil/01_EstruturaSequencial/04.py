# coding: utf-8

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

b1 = float(input("Digite a nota do primeiro bimestre: "))
b2 = float(input("Digite a nota do segundo bimestre: "))
b3 = float(input("Digite a nota do terceiro bimestre: "))
b4 = float(input("Digite a nota do quarto bimestre: "))

media = (b1 + b2 + b3 + b4) / 4

print(f"Média = {media:.1f}")
