# coding: utf-8

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi

r = float(input("Digite o raio do círculo: "))
area = pi * r**2
print(f"A área do círculo é igual a {area:.2f}")
