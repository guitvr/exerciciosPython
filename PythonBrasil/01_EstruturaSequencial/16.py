# coding: utf-8

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

from math import ceil

area = float(input("Digite o valor da área a ser pintada (em metros quadrados): "))
tinta = area / 3
latas = ceil(tinta / 18)
valor = latas * 80

print(f"\nQuantidade de latas necessárias: {latas}\nValor: R$ {valor:.2f}")
